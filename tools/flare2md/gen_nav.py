#!/usr/bin/env python3
"""
gen_nav.py — Build an MkDocs/Zensical `nav:` subtree from a Flare .fltoc,
using the conversion manifest to map source .htm links to output .md paths
and titles.

Flare TocEntry titles are usually "[%=System.LinkedHeader%]" (i.e. take the
linked topic's heading), so titles come from the manifest. Explicit TOC titles
are honored when present.

Usage:
    python3 gen_nav.py \
        --toc ../../jrs-user/Project/TOCs/JasperReports-Server-User-Guide.fltoc \
        --content-prefix "/Content/JasperReports-Server-User-Guide/" \
        --docs-root ../../zensical-site/docs \
        --guide-dir jasperreports-server-user-guide \
        --out ../../zensical-site/nav-jrs-user.yml
"""
from __future__ import annotations

import argparse
from pathlib import Path

from lxml import etree


def load_manifest(guide_out: Path) -> dict[str, tuple[str, str]]:
    """htm_rel -> (md_rel, title)."""
    manifest: dict[str, tuple[str, str]] = {}
    man = guide_out / "_manifest.tsv"
    for line in man.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        htm_rel, md_rel, title = line.split("\t", 2)
        manifest[htm_rel] = (md_rel, title)
    return manifest


def link_to_htm_rel(link: str, content_prefix: str) -> str | None:
    """Turn a TocEntry Link into a content-root-relative .htm path."""
    if not link:
        return None
    link = link.split("#", 1)[0]
    if content_prefix not in link:
        return None  # link into another guide's content; skip in this nav
    rel = link.split(content_prefix, 1)[1]
    return rel


def build_entries(
    toc_elem: etree._Element,
    manifest: dict[str, tuple[str, str]],
    guide_dir: str,
    content_prefix: str,
    unresolved: list[str],
    parent_md: str | None = None,
) -> list:
    """Recursively convert TocEntry nodes to nav entries.

    Flare TOCs deep-link to anchors *within* a topic (subsections of the same
    page). After fragments are stripped these collapse to the same .md, so we
    drop any entry that resolves to the same page as its parent (MkDocs builds
    the in-page TOC from headings), and de-duplicate repeats among siblings.

    Returns a list of nav items: {title: path} or {title: [children]}.
    """
    items = []
    for entry in toc_elem.findall("TocEntry"):
        link = entry.get("Link", "")
        title_attr = entry.get("Title", "")
        htm_rel = link_to_htm_rel(link, content_prefix)

        md_path = None
        title = None
        if htm_rel and htm_rel in manifest:
            md_rel, mtitle = manifest[htm_rel]
            md_path = f"{guide_dir}/{md_rel}"
            title = mtitle
        elif htm_rel:
            unresolved.append(htm_rel)

        children = build_entries(
            entry, manifest, guide_dir, content_prefix, unresolved,
            parent_md=md_path or parent_md,
        )

        # In-page anchor of the parent topic (deep-link to a subsection of the
        # same page): don't emit a node, but flatten its children up so any
        # distinct sub-topics they contain are preserved.
        if md_path and md_path == parent_md:
            items.extend(children)
            continue

        # Explicit title overrides the system-linked-header placeholder.
        if title_attr and not title_attr.startswith("[%="):
            title = title_attr
        if title is None:
            title = "Untitled"

        if md_path and children:
            # Section with a landing page -> list the page as the first child.
            items.append({title: [{title: md_path}] + children})
        elif md_path:
            items.append({title: md_path})
        elif children:
            items.append({title: children})
        # else: no link and no children -> skip (structural/PrintOnly entry)
    return items


def dedup_tree(items: list, seen: set[str]) -> list:
    """Drop leaf entries whose page already appeared earlier in the nav, and
    prune sections left empty as a result. Keeps the first occurrence."""
    out = []
    for item in items:
        (title, value), = item.items()
        if isinstance(value, str):
            if value in seen:
                continue
            seen.add(value)
            out.append({title: value})
        else:
            pruned = dedup_tree(value, seen)
            if pruned:
                out.append({title: pruned})
    return out


def _toml_str(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def to_toml_nav(items: list, indent: int = 0) -> str:
    """Render nav as a TOML array of inline tables (Zensical's native format):
      nav = [
        { "Title" = "path.md" },
        { "Section" = [ { "Child" = "x.md" }, ... ] },
      ]
    """
    pad = "  " * (indent + 1)
    lines = []
    for item in items:
        (title, value), = item.items()
        if isinstance(value, str):
            lines.append(f"{pad}{{ {_toml_str(title)} = {_toml_str(value)} }},")
        else:
            inner = to_toml_nav(value, indent + 1)
            lines.append(f"{pad}{{ {_toml_str(title)} = [")
            lines.append(inner)
            lines.append(f"{pad}] }},")
    return "\n".join(lines)


def to_yaml(items: list, indent: int = 0) -> str:
    lines = []
    pad = "  " * indent
    for item in items:
        (title, value), = item.items()
        # Quote titles that need it.
        t = title
        if any(c in t for c in ':#[]{}",&*?|<>=!%@`') or t != t.strip():
            t = '"' + t.replace('"', '\\"') + '"'
        if isinstance(value, str):
            lines.append(f'{pad}- {t}: {value}')
        else:
            lines.append(f"{pad}- {t}:")
            lines.append(to_yaml(value, indent + 1))
    return "\n".join(l for l in lines if l)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--toc", required=True)
    ap.add_argument("--content-prefix", required=True)
    ap.add_argument("--docs-root", required=True)
    ap.add_argument("--guide-dir", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--section-title", default=None,
                    help="wrap the whole guide under this top-level nav title")
    ap.add_argument("--format", choices=["toml", "yaml"], default="toml")
    args = ap.parse_args()

    docs_root = Path(args.docs_root).resolve()
    guide_out = docs_root / args.guide_dir
    manifest = load_manifest(guide_out)

    root = etree.fromstring(Path(args.toc).read_bytes(),
                            etree.XMLParser(recover=True, huge_tree=True))
    unresolved: list[str] = []
    items = build_entries(
        root, manifest, args.guide_dir, args.content_prefix, unresolved
    )
    items = dedup_tree(items, set())

    # Append any converted topics the TOC never referenced, so no content is
    # unreachable in the published site.
    covered_pre = {v for v in _iter_paths(items)}
    all_md = {f"{args.guide_dir}/{md}" for (md, _t) in manifest.values()}
    orphans = sorted(all_md - covered_pre)
    if orphans:
        orphan_items = []
        for o in orphans:
            # recover title from manifest
            md_rel = o[len(args.guide_dir) + 1:]
            title = next(
                (t for (m, t) in manifest.values() if m == md_rel), o
            )
            orphan_items.append({title: o})
        items.append({"Additional Topics": orphan_items})

    if args.section_title:
        items = [{args.section_title: items}]

    if args.format == "toml":
        text = to_toml_nav(items)
    else:
        text = to_yaml(items)
    Path(args.out).write_text(text + "\n", encoding="utf-8")

    covered = {v for v in _iter_paths(items)}
    all_md = {
        f"{args.guide_dir}/{md}"
        for (md, _t) in manifest.values()
    }
    orphans = sorted(all_md - covered)

    print(f"nav entries -> {args.out}")
    print(f"topics in manifest: {len(manifest)}, in nav: {len(covered)}")
    if orphans:
        print(f"WARNING: {len(orphans)} converted topics not in TOC nav:")
        for o in orphans[:20]:
            print(f"  orphan: {o}")
    if unresolved:
        uniq = sorted(set(unresolved))
        print(f"NOTE: {len(uniq)} TOC links had no converted topic "
              f"(cross-guide or excluded):")
        for u in uniq[:20]:
            print(f"  unresolved: {u}")
    return 0


def _iter_paths(items):
    for item in items:
        for value in item.values():
            if isinstance(value, str):
                yield value
            else:
                yield from _iter_paths(value)


if __name__ == "__main__":
    raise SystemExit(main())
