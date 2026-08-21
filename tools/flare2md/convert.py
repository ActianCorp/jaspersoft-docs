#!/usr/bin/env python3
"""
flare2md — Convert a MadCap Flare guide (source .htm topics) to clean Markdown
for a Zensical / MkDocs-Material site.

Pipeline per topic:
  1. Parse the Flare XHTML (MadCap namespace) with lxml.
  2. Inline snippets (<MadCap:snippetBlock/snippetText>) recursively.
  3. Resolve variables (<MadCap:variable>) from the guide's .flvar sets.
  4. Drop content excluded by conditions (DoNotPublish, ExcludeFromBuilds, ...).
  5. Flatten autonum labels (Note:, Important:, Figure:, procedure numbering).
  6. Convert xrefs / unresolvedLinks to plain anchors.
  7. Strip index keywords and residual MadCap attributes/namespaces.
  8. Hand the cleaned HTML <body> to pandoc -> GitHub-Flavored Markdown.
  9. Rewrite image srcs (copy into assets/) and .htm links -> .md.
 10. Prepend YAML front matter (title from the first heading).

This resolves the mechanical MadCap layer. Editorial cleanup (legacy TIBCO
branding, exact figure numbering) is intentionally out of scope and is logged.

Usage:
    python3 convert.py --guide ../../jrs-user \
        --content "Content/JasperReports-Server-User-Guide" \
        --out ../../zensical-site/docs/jasperreports-server-user-guide
"""
from __future__ import annotations

import argparse
import html
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

from lxml import etree

MC_NS = "http://www.madcapsoftware.com/Schemas/MadCap.xsd"
MC = "{%s}" % MC_NS

# Condition tokens that mean "do not render on the public docs site".
DROP_CONDITION_TOKENS = (
    "donotpublish",
    "excludefrombuilds",
    "excludefromhelp",
    "donotimport",
    "printonly",
    "draft",
    "deprecated",
)

warnings: list[str] = []


def warn(msg: str) -> None:
    warnings.append(msg)


# --------------------------------------------------------------------------- #
# Parsing helpers
# --------------------------------------------------------------------------- #
def parse_flare(path: Path) -> etree._Element:
    """Parse a Flare .htm/.flsnp file, tolerant of named HTML entities."""
    data = path.read_bytes()
    # Strip a UTF-8 BOM if present.
    if data.startswith(b"\xef\xbb\xbf"):
        data = data[3:]
    parser = etree.XMLParser(recover=True, resolve_entities=False, huge_tree=True)
    try:
        root = etree.fromstring(data, parser=parser)
    except etree.XMLSyntaxError as exc:  # pragma: no cover - defensive
        warn(f"parse error {path}: {exc}")
        # Last-ditch: replace stray named entities and retry.
        text = data.decode("utf-8", "replace")
        text = re.sub(r"&(?!amp;|lt;|gt;|quot;|apos;|#)", "&amp;", text)
        root = etree.fromstring(text.encode("utf-8"), parser=parser)
    return root


def body_of(root: etree._Element) -> etree._Element | None:
    for tag in ("body", "{http://www.w3.org/1999/xhtml}body"):
        b = root.find(tag)
        if b is not None:
            return b
    # Some snippets have no <html> wrapper.
    if root.tag in ("body", "{http://www.w3.org/1999/xhtml}body"):
        return root
    return root


# --------------------------------------------------------------------------- #
# 1. Variables
# --------------------------------------------------------------------------- #
def load_variables(project_dirs: list[Path]) -> dict[str, str]:
    """Return {set.name: value} and {name: value} using EvaluatedDefinition.

    Flare allows multiple definitions per name (resolved per target); we keep
    the first non-empty one and warn on genuine conflicts.
    """
    variables: dict[str, str] = {}
    for proj in project_dirs:
        vs_dir = proj / "Project" / "VariableSets"
        if not vs_dir.is_dir():
            continue
        for flvar in sorted(vs_dir.glob("*.flvar")):
            setname = flvar.stem
            root = parse_flare(flvar)
            for var in root.iter("Variable"):
                name = var.get("Name")
                if not name:
                    continue
                value = var.get("EvaluatedDefinition")
                if value is None:
                    value = "".join(var.itertext())
                value = value.strip()
                if not value:
                    continue
                for key in (f"{setname}.{name}", name):
                    if key not in variables:
                        variables[key] = value
    return variables


# --------------------------------------------------------------------------- #
# 2. Snippets
# --------------------------------------------------------------------------- #
def inline_snippets(elem: etree._Element, base_dir: Path, depth: int = 0) -> None:
    if depth > 10:
        warn(f"snippet recursion too deep under {base_dir}")
        return
    for node in list(elem.iter(f"{MC}snippetBlock", f"{MC}snippetText")):
        src = node.get("src")
        parent = node.getparent()
        if parent is None:
            continue
        if not src:
            parent.remove(node)
            continue
        snippet_path = (base_dir / src).resolve()
        if not snippet_path.is_file():
            warn(f"missing snippet: {src} (from {base_dir})")
            parent.remove(node)
            continue
        sroot = parse_flare(snippet_path)
        sbody = body_of(sroot)
        # Recurse into the snippet relative to its own location.
        inline_snippets(sbody, snippet_path.parent, depth + 1)
        idx = list(parent).index(node)
        # Splice the snippet body's children in place of the node.
        children = list(sbody)
        for child in reversed(children):
            parent.insert(idx, child)
        # Preserve any tail text on the snippet node.
        if node.tail:
            if children:
                children[-1].tail = (children[-1].tail or "") + node.tail
            elif idx > 0:
                prev = parent[idx - 1]
                prev.tail = (prev.tail or "") + node.tail
        parent.remove(node)


# --------------------------------------------------------------------------- #
# 3. Variables resolution
# --------------------------------------------------------------------------- #
def resolve_variables(elem: etree._Element, variables: dict[str, str]) -> None:
    for node in list(elem.iter(f"{MC}variable")):
        name = node.get("name", "")
        value = variables.get(name)
        if value is None and "." in name:
            value = variables.get(name.split(".", 1)[1])
        if value is None:
            value = variables.get(name.split(".")[-1])
        if value is None:
            warn(f"unresolved variable: {name}")
            value = ""
        _replace_with_text(node, value)


def _replace_with_text(node: etree._Element, text: str) -> None:
    """Replace an inline element with a plain text run, preserving flow."""
    parent = node.getparent()
    if parent is None:
        return
    prev = node.getprevious()
    combined = text + (node.tail or "")
    if prev is not None:
        prev.tail = (prev.tail or "") + combined
    else:
        parent.text = (parent.text or "") + combined
    parent.remove(node)


# --------------------------------------------------------------------------- #
# 4. Conditions
# --------------------------------------------------------------------------- #
def apply_conditions(elem: etree._Element) -> None:
    for node in list(elem.iter()):
        cond = node.get(f"{MC}conditions")
        if not cond:
            continue
        tokens = [t.strip().lower() for t in cond.split(",")]
        if any(any(drop in tok for drop in DROP_CONDITION_TOKENS) for tok in tokens):
            parent = node.getparent()
            if parent is not None:
                # Keep tail text so surrounding prose isn't broken.
                if node.tail:
                    prev = node.getprevious()
                    if prev is not None:
                        prev.tail = (prev.tail or "") + node.tail
                    else:
                        parent.text = (parent.text or "") + node.tail
                parent.remove(node)


def drop_draft_comments(elem: etree._Element) -> None:
    for node in list(elem.iter()):
        cls = node.get("class") or ""
        if "draft-comment" in cls.split():
            parent = node.getparent()
            if parent is not None:
                parent.remove(node)


# --------------------------------------------------------------------------- #
# 5. autonum labels (Note:, Important:, Figure:, ...)
# --------------------------------------------------------------------------- #
def _autonum_label(raw: str) -> str:
    """Extract a human label from an autonum spec like '<i>Figure 1: </i>'."""
    text = html.unescape(raw)
    text = re.sub(r"<[^>]+>", "", text)  # strip embedded tags
    # Drop MadCap numbering tokens; keep leading label words.
    text = text.replace(" ", " ").strip()
    return text


def handle_autonum(elem: etree._Element) -> None:
    for node in list(elem.iter()):
        raw = node.get(f"{MC}autonum")
        if raw is None:
            continue
        label = _autonum_label(raw)
        # Ordered-list procedures: numbering is intrinsic to <ol>; drop label.
        if node.tag in ("ol", "ul"):
            continue
        if label and not label.lower().startswith(("procedure", "chapter")):
            # Prepend a bold label to the element's text content.
            b = etree.Element("strong")
            b.text = label + " "
            b.tail = node.text
            node.text = None
            node.insert(0, b)


# --------------------------------------------------------------------------- #
# 6. xref / unresolvedLink / conditionalText
# --------------------------------------------------------------------------- #
def handle_links(elem: etree._Element) -> None:
    for node in list(elem.iter(f"{MC}xref")):
        node.tag = "a"
        href = node.get("href")
        if href:
            node.set("href", href)
        _strip_mc_attrs(node)
    for node in list(elem.iter(f"{MC}unresolvedLink")):
        # Broken/placeholder link: keep the visible text only.
        node.tag = "span"
        _strip_mc_attrs(node)
    for node in list(elem.iter(f"{MC}conditionalText")):
        node.tag = "span"
        _strip_mc_attrs(node)


# --------------------------------------------------------------------------- #
# 7. Strip keywords + residual MadCap
# --------------------------------------------------------------------------- #
def strip_madcap(elem: etree._Element) -> None:
    for node in list(elem.iter(f"{MC}keyword")):
        parent = node.getparent()
        if parent is not None:
            if node.tail:
                prev = node.getprevious()
                if prev is not None:
                    prev.tail = (prev.tail or "") + node.tail
                else:
                    parent.text = (parent.text or "") + node.tail
            parent.remove(node)
    # Any other stray MadCap:* elements -> unwrap to their children/text.
    for node in list(elem.iter()):
        if isinstance(node.tag, str) and node.tag.startswith(MC):
            _unwrap(node)
    for node in elem.iter():
        _strip_mc_attrs(node)


def _strip_mc_attrs(node: etree._Element) -> None:
    for attr in list(node.attrib):
        if attr.startswith(MC) or attr.startswith("{" + MC_NS):
            del node.attrib[attr]


# Presentational attributes carried over from Flare that reference stylesheets
# / pixel layouts which don't exist in the target site. Dropping them yields
# clean, theme-styled tables instead of broken inline styling.
CRUFT_ATTRS = ("style", "width", "height", "cellpadding", "cellspacing", "border")


def strip_presentation(elem: etree._Element) -> None:
    for node in elem.iter():
        if not isinstance(node.tag, str):
            continue
        for attr in CRUFT_ATTRS:
            node.attrib.pop(attr, None)
        # Flare table-style classes point at missing CSS; drop them but keep
        # semantic classes elsewhere (e.g. note/warning admonition hints).
        cls = node.get("class")
        if cls and ("TableStyle" in cls or "Column" in cls or "Body" in cls or "Head" in cls):
            node.attrib.pop("class", None)


def rewrite_tree_images(
    elem: etree._Element, topic_dir: Path, assets_dir: Path, assets_rel: str
) -> None:
    """Copy every <img> referenced (in markdown-bound HTML or raw tables) into
    the shared assets dir and repoint its src. Runs on the tree so images
    inside complex tables are handled too."""
    assets_dir.mkdir(parents=True, exist_ok=True)
    for img in elem.iter("img"):
        src = img.get("src")
        if not src or src.startswith(("http://", "https://", "data:")):
            continue
        decoded = unquote(src)
        resolved = (topic_dir / decoded).resolve()
        name = resolved.name
        if resolved.is_file():
            dest = assets_dir / name
            if not dest.exists():
                shutil.copy2(resolved, dest)
        else:
            warn(f"missing image: {decoded} (topic {topic_dir})")
        img.set("src", f"{assets_rel}/{name.replace(' ', '%20')}")


def flatten_headings(elem: etree._Element) -> None:
    """Reduce heading (h1-h6) content to plain text. Flare wraps heading text
    in presentational spans (class="UI", etc.) and sometimes icons; leaving
    raw inline HTML inside a heading crashes the downstream TOC renderer and
    produces ugly anchors. Headings are plain text on a docs site anyway."""
    for level in ("h1", "h2", "h3", "h4", "h5", "h6"):
        for h in elem.iter(level):
            text = re.sub(r"\s+", " ", "".join(h.itertext())).strip()
            for child in list(h):
                h.remove(child)
            h.text = text


def drop_empty_anchors(elem: etree._Element) -> None:
    """Remove empty <span id>/<a id|name> bookmark targets. Flare emits these
    for xref anchors; we drop link fragments, so they're now dead clutter that
    otherwise leaks into headings."""
    for node in list(elem.iter("span", "a")):
        has_id = node.get("id") or node.get("name")
        empty = not (node.text and node.text.strip()) and len(node) == 0
        if has_id and empty:
            _unwrap(node)  # preserves any tail text


def slug_relpath(relpath: str) -> str:
    """Hyphenate spaces in each path segment for clean URLs, preserving
    '.'/'..' and the anchor-free target. Applied identically to output paths
    and to link hrefs so intra-guide links stay valid."""
    segs = []
    for seg in relpath.split("/"):
        if seg in ("", ".", ".."):
            segs.append(seg)
        else:
            segs.append(seg.replace(" ", "-"))
    return "/".join(segs)


def rewrite_tree_links(elem: etree._Element) -> None:
    for a in elem.iter("a"):
        href = a.get("href")
        if not href:
            continue
        if href.startswith(("http://", "https://", "mailto:")):
            continue
        # In-page anchors targeted Flare bookmarks we've since removed; keep
        # the visible text but drop the now-dead link.
        if href.startswith("#"):
            a.attrib.pop("href", None)
            continue
        if "#" in href:
            href = href.split("#", 1)[0]
        if not href:
            a.attrib.pop("href", None)
            continue
        if href.endswith(".htm"):
            href = href[:-4] + ".md"
        elif href.endswith(".html"):
            href = href[:-5] + ".md"
        a.set("href", slug_relpath(href))


def _unwrap(node: etree._Element) -> None:
    parent = node.getparent()
    if parent is None:
        return
    idx = list(parent).index(node)
    text = node.text or ""
    if idx > 0:
        prev = parent[idx - 1]
        prev.tail = (prev.tail or "") + text
    else:
        parent.text = (parent.text or "") + text
    for child in reversed(list(node)):
        parent.insert(idx, child)
    if node.tail:
        last = node.getprevious()
        if last is not None:
            last.tail = (last.tail or "") + node.tail
        else:
            parent.text = (parent.text or "") + node.tail
    parent.remove(node)


# --------------------------------------------------------------------------- #
# Serialization + pandoc
# --------------------------------------------------------------------------- #
def inner_html(body: etree._Element) -> str:
    parts = []
    if body.text:
        parts.append(html.escape(body.text))
    for child in body:
        parts.append(
            etree.tostring(child, encoding="unicode", method="html")
        )
    return "".join(parts)


def to_markdown(html_str: str) -> str:
    # Keep raw_html ON so complex tables (rowspan/colspan/table-styles) survive
    # as HTML instead of being dropped to a "[TABLE]" placeholder. MkDocs and
    # Zensical both render embedded HTML fine.
    proc = subprocess.run(
        ["pandoc", "-f", "html", "-t", "gfm+pipe_tables", "--wrap=none"],
        input=html_str.encode("utf-8"),
        capture_output=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.decode("utf-8", "replace"))
    return proc.stdout.decode("utf-8")


# --------------------------------------------------------------------------- #
# Post-processing: front matter + cleanup
# --------------------------------------------------------------------------- #
NS_DECL_RE = re.compile(r'\s*xmlns:[a-zA-Z]+="[^"]*"')
EMPTY_ATTR_RE = re.compile(r"[ \t]*\{\s*\}")


def strip_ns_decls(md: str) -> str:
    """Safety net: remove any stray xmlns:* declarations pandoc kept on
    raw-HTML blocks or attribute lists, plus any empty {} blocks left behind."""
    md = NS_DECL_RE.sub("", md)
    md = EMPTY_ATTR_RE.sub("", md)
    return md


def first_heading(body: etree._Element) -> str:
    for level in ("h1", "h2", "h3"):
        el = body.find(f".//{level}")
        if el is not None:
            txt = "".join(el.itertext()).strip()
            if txt:
                return re.sub(r"\s+", " ", txt)
    return "Untitled"


def clean_markdown(md: str) -> str:
    md = re.sub(r"\n{3,}", "\n\n", md)
    md = "\n".join(line.rstrip() for line in md.splitlines())
    return md.strip() + "\n"


# --------------------------------------------------------------------------- #
# Driver
# --------------------------------------------------------------------------- #
def convert_topic(
    topic: Path, content_root: Path, out_root: Path, variables: dict[str, str]
) -> tuple[Path, str]:
    root = parse_flare(topic)
    body = body_of(root)

    inline_snippets(body, topic.parent)
    resolve_variables(body, variables)
    apply_conditions(body)
    drop_draft_comments(body)
    handle_autonum(body)
    handle_links(body)
    strip_madcap(body)
    strip_presentation(body)
    flatten_headings(body)

    title = first_heading(body)

    orig_rel = topic.relative_to(content_root).with_suffix(".md").as_posix()
    rel = Path(slug_relpath(orig_rel))
    out_path = out_root / rel
    out_path.parent.mkdir(parents=True, exist_ok=True)

    depth = len(rel.parts) - 1
    assets_rel = "../" * depth + "assets/images"
    assets_dir = out_root / "assets" / "images"
    # Rewrite images/links on the tree (covers raw-HTML tables too), then
    # drop the now-unused MadCap namespace before serializing.
    rewrite_tree_images(body, topic.parent, assets_dir, assets_rel)
    rewrite_tree_links(body)
    drop_empty_anchors(body)
    etree.cleanup_namespaces(root)

    html_str = inner_html(body)
    md = to_markdown(html_str)
    md = strip_ns_decls(md)
    md = clean_markdown(md)

    fm = f"---\ntitle: {yaml_scalar(title)}\n---\n\n"
    out_path.write_text(fm + md, encoding="utf-8")
    htm_rel = topic.relative_to(content_root).as_posix()
    return htm_rel, rel.as_posix(), title


def yaml_scalar(s: str) -> str:
    if re.search(r'[:#\[\]{}",&*?|<>=!%@`]', s) or s != s.strip():
        return '"' + s.replace('"', '\\"') + '"'
    return s


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--guide", required=True, help="guide root (has .flprj)")
    ap.add_argument("--content", required=True, help="content subdir to convert")
    ap.add_argument("--out", required=True, help="output docs dir")
    ap.add_argument("--shared", default="../js-shared", help="shared project dir")
    args = ap.parse_args()

    guide = Path(args.guide).resolve()
    content_root = (guide / args.content).resolve()
    out_root = Path(args.out).resolve()
    shared = (guide / args.shared).resolve()

    project_dirs = [guide]
    if shared.is_dir():
        project_dirs.append(shared)
    variables = load_variables(project_dirs)
    print(f"Loaded {len(variables)} variable keys", file=sys.stderr)

    topics = sorted(content_root.rglob("*.htm"))
    print(f"Converting {len(topics)} topics from {content_root}", file=sys.stderr)

    manifest = []
    for topic in topics:
        try:
            htm_rel, md_rel, title = convert_topic(
                topic, content_root, out_root, variables
            )
            manifest.append((htm_rel, md_rel, title))
        except Exception as exc:  # noqa: BLE001
            warn(f"FAILED {topic}: {exc}")

    # Emit a manifest (source .htm path -> output .md path -> title) so the nav
    # generator can resolve .fltoc TocEntry links to final files.
    man_path = out_root / "_manifest.tsv"
    man_path.write_text(
        "\n".join(f"{h}\t{m}\t{t}" for h, m, t in manifest) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {len(manifest)} topics -> {out_root}", file=sys.stderr)

    if warnings:
        log = out_root / "_conversion-warnings.log"
        log.write_text("\n".join(warnings) + "\n", encoding="utf-8")
        print(f"{len(warnings)} warnings -> {log}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
