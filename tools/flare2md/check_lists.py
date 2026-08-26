#!/usr/bin/env python3
"""Check that every nested list in the markdown survives into the built page.

This is the check that would have caught the defect the reviewers found: the
converter wrote a correctly nested list, but the page rendered it flat, so
sub-steps and sub-bullets read as top-level ones.

The cause was indentation width. pandoc's `gfm` writer indents a nested bullet
by two spaces; Python-Markdown, which Zensical parses with, only treats a list
as nested at four. Two-space nesting therefore parsed as one flat list.

So the invariant is: for each page, the number of list items the markdown puts
below the top level must equal the number the HTML renders below the top level.
Run after `build.py` and `zensical build`:

    python3 tools/flare2md/check_lists.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def _project_root():
    """Where the Zensical project lives.

    Two layouts use this script: the working repo, where the project sits in
    `zensical-site/`, and the published repo, where it sits at the root. One
    copy of the script then serves CI and local runs alike.
    """
    for candidate in (ROOT, ROOT / "zensical-site"):
        if (candidate / "docs").is_dir() and (candidate / "site").is_dir():
            return candidate
    return ROOT / "zensical-site"


PROJECT = _project_root()
DOCS = PROJECT / "docs"
SITE = PROJECT / "site"

FENCE_RE = re.compile(r"^\s*(```+|~~~+)")
# A list item, capturing its indent. Ordered and unordered both count.
ITEM_RE = re.compile(r"^(\s*)(?:[-*+]|\d+[.)])\s+\S")
# Blocks that indent their own content by four spaces without being a list:
# an admonition body sits at four, and a list starting there is still top level.
CONTAINER_RE = re.compile(r"^(\s*)(?:!!!|\?\?\?\+?|>)\s")


def markdown_nested_items(text: str) -> int:
    """List items the markdown puts below the top level of their own list.

    Front matter, fenced code and raw HTML blocks are skipped: a `- ` inside
    any of them is content, not a list marker. Admonition and blockquote
    bodies carry their own four-space indent, so the depth of an item is
    measured from the innermost such body it sits in, not from the margin.
    """
    lines = text.splitlines()
    if lines and lines[0].strip() == "---":
        end = next((i for i, l in enumerate(lines[1:], 1) if l.strip() == "---"), 0)
        lines = lines[end + 1:]
    count, fence, in_html = 0, None, False
    baselines = []
    for line in lines:
        m = FENCE_RE.match(line)
        if m:
            if fence is None:
                fence = m.group(1)[:3]
            elif line.strip().startswith(fence):
                fence = None
            continue
        if fence is not None:
            continue
        stripped = line.strip()
        if in_html:
            if re.match(r"^</(table|div|pre|ul|ol)>", stripped):
                in_html = False
            continue
        if re.match(r"^<(table|div|pre)\b", stripped):
            in_html = True
            continue
        if not stripped:
            continue
        indent = len(line) - len(line.lstrip(" "))
        while baselines and indent < baselines[-1]:
            baselines.pop()
        container = CONTAINER_RE.match(line)
        if container:
            baselines.append(len(container.group(1)) + 4)
            continue
        item = ITEM_RE.match(line)
        if item and len(item.group(1)) - (baselines[-1] if baselines else 0) >= 4:
            count += 1
    return count


LIST_TAG_RE = re.compile(r"<(/?)(ul|ol|li)\b[^>]*>")


def html_nested_items(page: Path) -> int:
    """List items the page renders inside a list that is itself inside a list."""
    text = page.read_text(errors="replace")
    start, end = text.find("<article"), text.find("</article>")
    if start < 0:
        return 0
    body = text[start:end if end > start else len(text)]
    # The theme's own navigation lives outside <article>, so what is left is
    # page content only.
    depth, count = 0, 0
    for m in LIST_TAG_RE.finditer(body):
        closing, tag = m.group(1), m.group(2)
        if tag in ("ul", "ol"):
            depth += -1 if closing else 1
        elif not closing and depth >= 2:
            count += 1
    return count


def page_for(md: Path) -> Path:
    rel = md.relative_to(DOCS)
    if rel.name == "index.md":
        return SITE / rel.parent / "index.html"
    return SITE / rel.with_suffix("") / "index.html"


def main() -> int:
    checked = flat = 0
    md_total = html_total = 0
    problems = []
    for md in sorted(DOCS.rglob("*.md")):
        page = page_for(md)
        if not page.is_file():
            problems.append((md, "no built page", 0, 0))
            continue
        want = markdown_nested_items(md.read_text())
        got = html_nested_items(page)
        checked += 1
        md_total += want
        html_total += got
        if got < want:
            flat += 1
            problems.append((md, "flattened", want, got))
    print("pages checked: %d" % checked)
    print("nested list items: %d in markdown, %d rendered" % (md_total, html_total))
    print("pages rendering a nested list flat: %d" % flat)
    for md, why, want, got in problems[:20]:
        print("  %s: %s (markdown %d, rendered %d)"
              % (md.relative_to(DOCS), why, want, got))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
