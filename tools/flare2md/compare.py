#!/usr/bin/env python3
"""compare.py — check every published page against its Flare source.

For each converted topic it extracts the visible text from

  * the Flare source, after snippet inlining, condition filtering and variable
    resolution (i.e. exactly what the source would publish), and
  * the built HTML page in zensical-site/site,

then reports the pages where text is missing, so content loss shows up without
anyone opening 1,500 pages by hand. Structural counts (images, list items,
headings) are compared too, since those go wrong without changing the text.

    python3 tools/flare2md/compare.py                  # all guides
    python3 tools/flare2md/compare.py user-guide       # one guide

Writes zensical-site/_reports/compare.md and prints the worst offenders.
"""
from __future__ import annotations

import html as html_mod
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import build as B
import flare2md as f2
import guides as G

SITE = B.SITE / "site"
TAG_RE = re.compile(r"<[^>]+>")
WORD_RE = re.compile(r"[0-9a-z]+(?:['’][a-z]+)?")

# Pages whose text legitimately differs from the source.
IGNORE_NAMES = {"index.md"}


def visible_text(html_str: str) -> str:
    text = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", html_str)
    text = TAG_RE.sub(" ", text)
    return re.sub(r"\s+", " ", html_mod.unescape(text)).strip()


def words(text: str):
    return WORD_RE.findall(text.lower())


def source_text(rel: Path, plan, warn):
    """The visible text the Flare source would publish for this topic."""
    topic = plan["content_root"] / rel
    root = f2.parse_flare(topic, warn)
    body = f2.body_of(root)
    f2.inline_snippets(body, topic.parent, warn, fallbacks=plan["snippet_roots"])
    f2.apply_conditions(body, plan["target"])
    f2.resolve_variables(body, plan["variables"], plan["target"].overrides, warn)
    f2.resolve_variable_syntax(body, plan["variables"], plan["target"].overrides, warn)
    # Same brand rename the conversion applies, or every renamed sentence
    # would read as a difference.
    f2.apply_brand(body, G.BRAND_REPLACEMENTS)
    f2.drop_draft_content(body)
    f2.strip_madcap(body)
    # A <br> renders as a space; without this the source text reads
    # "Click Next.The Add a Report..." and looks different from the page.
    for br in body.iter("br"):
        br.tail = " " + (br.tail or "")
    counts = {
        # Callout icons become the admonition itself, so they are not expected
        # to appear as images in the output.
        "img": len([img for img in body.findall(".//img")
                    if not _is_callout_icon(img)]),
        "h": sum(len(body.findall(".//h%d" % n)) for n in range(1, 7)),
    }
    return visible_text(f2.inner_html(body)), counts, _list_item_keys(body)


LIST_KEY_LEN = 30


def _normalize_key(text: str, limit: int = LIST_KEY_LEN) -> str:
    """Letters and digits only.

    Whitespace is dropped as well: the source joins text across element
    boundaries without a space ("operator.Text fields") where the rendered page
    has one, and neither difference is a defect worth reporting.
    """
    return re.sub(r"[^0-9a-z]", "", text.lower())[:limit]


def _own_text(node) -> str:
    """The element's own text, excluding any nested list.

    A list item's key must describe that item, not the sub-items under it:
    the page renders those as separate items, so a combined key would never
    match anything.
    """
    parts = [node.text or ""]
    for child in node:
        if child.tag in ("ul", "ol"):
            parts.append(child.tail or "")
            continue
        parts.append(_own_text(child))
        parts.append(child.tail or "")
    return "".join(parts)


def _list_item_keys(body):
    """A short key per source list item, real or Flare pseudo-list."""
    keys = []
    for li in body.findall(".//li"):
        text = re.sub(r"\s+", " ", _own_text(li)).strip()
        if text:
            keys.append(_normalize_key(text))
    for node in body.iter("p"):
        for cls in (node.get("class") or "").split():
            if f2.BULLET_CLASS_RE.match(cls.lower()) or f2.NUMBER_CLASS_RE.match(cls.lower()):
                text = re.sub(r"\s+", " ", _own_text(node)).strip()
                if text:
                    keys.append(_normalize_key(text))
                break
    return [k for k in keys if len(k) > 8]


def _is_callout_icon(img) -> bool:
    """Note/warning icons become the admonition itself, not an image."""
    name = Path((img.get("src") or "").replace("\\", "/")).name.lower()
    return any(token in name for token, _kind in f2.ICON_KINDS)


def _strip_tags_outside_code(text: str) -> str:
    """Remove HTML tags, but never inside `code spans`.

    Two things in these pages look like tags without being tags: escaped
    markdown (`\<base_name\>`) and XML shown as inline code
    (`` `<property name="..."/>` ``). Removing those would report the line as
    missing content that is in fact right there.
    """
    parts = text.split("`")
    for i in range(0, len(parts), 2):  # even indexes are outside code spans
        # `<http://...>` is an autolink, not a tag.
        parts[i] = re.sub(r"(?<!\\)</?(?!https?:)[a-zA-Z][^>]*>", " ", parts[i])
    return "`".join(parts)


def output_blocks(md_path: Path):
    """(normalized text, is_list_item) for every block on the generated page.

    A list item's text can continue over a blank line onto indented lines, so
    a block ends only at a blank line that is *not* followed by indented text.
    Comparing line by line would report those continuations as missing.
    """
    if not md_path.is_file():
        return []
    lines = md_path.read_text(encoding="utf-8").splitlines()
    blocks = []
    current, is_list = [], False

    def flush():
        if current:
            blocks.append((_normalize_key(" ".join(current), limit=8000), is_list))

    for number, raw in enumerate(lines):
        stripped = raw.strip()
        starts_list = bool(re.match(r"^([-*+]|\d+[.)])\s", stripped)) or "<li>" in stripped
        if not stripped:
            following = next((l for l in lines[number + 1:] if l.strip()), "")
            if following.startswith("  "):
                continue  # indented continuation of the same item
            flush()
            current, is_list = [], False
            continue
        if starts_list and current:
            flush()
            current, is_list = [], False
        if starts_list:
            is_list = True
        # Drop images (the source alt text is empty) and keep link text without
        # the URL, which would otherwise land mid-sentence.
        # Images drop out with no separator: the source contributes no text
        # there either, and several sentences run straight into an icon.
        text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", stripped)
        text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
        text = _strip_tags_outside_code(text)
        text = re.sub(r"^([-*+]|\d+[.)])\s+", "", text)
        current.append(text)
    flush()
    return blocks


def page_html(prefix: str, out_rel: str):
    stem = out_rel[:-3] if out_rel.endswith(".md") else out_rel
    if stem.endswith("/index"):
        stem = stem[: -len("/index")]
    path = SITE / prefix / stem / "index.html"
    if not path.is_file():
        return None
    return path.read_text(encoding="utf-8", errors="replace")


def main(argv) -> int:
    only = set(argv[1:])
    if not SITE.is_dir():
        print("build the site first (zensical build)")
        return 1

    rows = []
    for guide in G.GUIDES:
        prefix = "%s/%s" % (guide["family"], guide["key"])
        if only and guide["key"] not in only and prefix not in only:
            continue
        warn = []
        plan = B.prepare_guide(guide, warn.append)
        B.absorb_unreferenced([plan], warn.append)
        manifest = B.load_manifest(prefix)
        if not manifest:
            continue
        print("checking %s (%d pages)" % (prefix, len(manifest)), flush=True)
        for rel_str, (out_rel, _title) in sorted(manifest.items()):
            if Path(out_rel).name in IGNORE_NAMES:
                continue
            html_str = page_html(prefix, out_rel)
            if html_str is None:
                rows.append((1.0, prefix, out_rel, "page not built", {}, {}))
                continue
            article = html_str.split("<article", 1)[-1].split("</article>", 1)[0]
            out_text = visible_text(article)
            try:
                src_text, src_counts, src_items = source_text(
                    Path(rel_str), plan, lambda m: None)
            except Exception as exc:  # noqa: BLE001
                rows.append((1.0, prefix, out_rel, "source parse failed: %s" % exc, {}, {}))
                continue

            src_words, out_words = words(src_text), words(out_text)
            if not src_words:
                continue
            out_pool = {}
            for word in out_words:
                out_pool[word] = out_pool.get(word, 0) + 1
            missing = []
            for word in src_words:
                if out_pool.get(word):
                    out_pool[word] -= 1
                else:
                    missing.append(word)
            ratio = len(missing) / len(src_words)
            out_counts = {
                "img": article.count("<img "),
                "h": sum(article.count("<h%d" % n) for n in range(1, 7)),
            }
            note = ""
            for key in ("img", "h"):
                if out_counts[key] < src_counts[key]:
                    note += " %s %d<%d" % (key, out_counts[key], src_counts[key])
            # Lists are checked by content, not by count: nested items and bold
            # markers shift a raw <li> count without anything being lost.
            blocks = output_blocks(B.DOCS / prefix / out_rel)
            lost = [k for k in src_items
                    if not any(k in text for text, is_list in blocks if is_list)]
            if lost:
                note += " list items not in a list: %d (%s)" % (
                    len(lost), "; ".join(lost[:3]))
            if ratio > 0.02 or note:
                detail = ("**" + note.strip() + "** " if note else "") + \
                    " ".join(missing[:18])
                rows.append((ratio, prefix, out_rel, detail, src_counts, out_counts))

    rows.sort(reverse=True)
    lines = [
        "# Source-to-page comparison",
        "",
        "Text present in the Flare source but missing from the published page, "
        "and structural counts that came out lower than the source.",
        "Regenerate with `python3 tools/flare2md/compare.py`.",
        "",
        "| Missing | Page | Lower counts / sample of missing words |",
        "| --- | --- | --- |",
    ]
    for ratio, prefix, out_rel, sample, src, out in rows[:200]:
        lines.append("| %.1f%% | `%s/%s` | %s |"
                     % (ratio * 100, prefix, out_rel, sample.replace("|", "/")[:160]))
    (B.REPORTS / "compare.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n%d pages flagged -> %s" % (len(rows), B.REPORTS / "compare.md"))
    for row in rows[:15]:
        print("  %5.1f%%  %s/%s  %s" % (row[0] * 100, row[1], row[2], row[3][:90]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
