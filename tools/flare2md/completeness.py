#!/usr/bin/env python3
"""completeness.py — account for every topic in the shared Flare sources.

Answers two questions with evidence, and writes
_reports/migration-completeness.md:

  1. Is anything missing?  Every .htm/.html topic under every project's
     Content/ directory is classified as published, skipped as a book artifact,
     emptied by the source's own conditions, or belonging to a project that is
     not part of this documentation set. For that last group the check is by
     *text*, not by filename: a topic only counts as safely excluded if the same
     prose is already published from another project. Anything else is listed
     individually as unique unpublished content.

  2. Is anything extra?  Every published page is traced back to the Flare topic
     it came from. Pages with no such origin are listed; the only ones expected
     are the generated landing pages (portal home, product family, per-guide
     contents), which are site scaffolding rather than documentation.

Usage: python3 tools/flare2md/completeness.py
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import build as B
import flare2md as f2
import guides as G

REPO = B.REPO
REPORTS = B.REPORTS
DOCS = B.DOCS

NON_CONTENT_DIRS = {"Resources"}
# Enough words that two topics sharing this prefix are the same topic; short
# boilerplate pages are compared on their whole text.
FINGERPRINT_WORDS = 60


def content_roots(project: Path):
    """Content directories in a project; containers hold one project per subdir."""
    if (project / "Content").is_dir():
        return [project / "Content"]
    return sorted(p for p in project.glob("*/Content") if p.is_dir())


def source_projects():
    """Every Flare project in the repository, one row each.

    `ServicePacks/` and `Standalone/` are containers of separate projects, so
    they are reported per subproject: lumping them together would hide which
    release a topic belongs to.
    """
    found = []
    for path in sorted(p for p in REPO.iterdir() if p.is_dir()
                       and not p.name.startswith((".", "zensical", "tools"))):
        if (path / "Content").is_dir():
            found.append(path.relative_to(REPO).as_posix())
        else:
            found.extend(sub.parent.relative_to(REPO).as_posix()
                         for sub in sorted(path.glob("*/Content")))
    return found


def exclusion_reason(project: str) -> str:
    """Documented reason a project is not part of the published set."""
    if project in G.EXCLUDED:
        return G.EXCLUDED[project]
    for prefix, reason in G.EXCLUDED.items():
        if project.startswith(prefix.rstrip("/") + "/") or project.split("/")[0] == prefix:
            return reason
    if project.startswith("ServicePacks/"):
        return "archived release notes for %s" % project.split("/")[1]
    return "not part of the 10.1.0 documentation set"


def topics(project: Path):
    """[(content_root, relative path)] for every publishable topic."""
    out = []
    for root in content_roots(project):
        for suffix in f2.TOPIC_SUFFIXES:
            for path in root.rglob("*" + suffix):
                rel = path.relative_to(root)
                if rel.parts[0] in NON_CONTENT_DIRS:
                    continue
                out.append((root, rel))
    return sorted(set(out))


def fingerprint(path: Path) -> str:
    """Hash of a topic's first words of visible text.

    Filenames differ between an old and a new copy of the same topic, so the
    comparison has to be on the prose itself.
    """
    try:
        raw = path.read_text(encoding="utf-8-sig", errors="replace")
    except OSError:
        return ""
    body = raw.split("<body", 1)[-1]
    text = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", body)
    text = re.sub(r"<[^>]+>", " ", text)
    words = re.findall(r"[0-9a-z]+", text.lower())
    if not words:
        return ""
    return hashlib.sha1(" ".join(words[:FINGERPRINT_WORDS]).encode()).hexdigest()


def main() -> int:
    published_projects = sorted({g["project"] for g in G.GUIDES})

    # ---- what the pipeline published, per project ------------------------- #
    published_rel = defaultdict(set)   # project -> {content-relative posix}
    page_origin = {}                   # (guide prefix, md path) -> source topic
    for guide in G.GUIDES:
        prefix = "%s/%s" % (guide["family"], guide["key"])
        path = REPORTS / ("%s.manifest.json" % prefix.replace("/", "__"))
        if not path.is_file():
            continue
        for htm, (md_rel, _title) in json.loads(path.read_text(encoding="utf-8")).items():
            published_rel[guide["project"]].add(htm)
            page_origin[(prefix, md_rel)] = "%s/Content/%s" % (guide["project"], htm)

    # Fingerprints of everything published, to test excluded projects against.
    published_prints = set()
    for project, rels in published_rel.items():
        for root in content_roots(REPO / project):
            for rel in rels:
                path = root / rel
                if path.is_file():
                    published_prints.add(fingerprint(path))
    published_prints.discard("")

    rows, unique_unpublished, artifacts, emptied = [], [], [], []
    grand = defaultdict(int)

    for project_dir in source_projects():
        entries = topics(REPO / project_dir)
        if not entries:
            continue
        is_published = project_dir in published_projects
        counts = defaultdict(int)
        for root, rel in entries:
            posix = rel.as_posix()
            if is_published and posix in published_rel[project_dir]:
                counts["published"] += 1
            elif posix.lower() in B.SKIP_TOPICS:
                counts["book artifact"] += 1
                artifacts.append("%s/%s" % (project_dir, posix))
            else:
                print_ = fingerprint(root / rel)
                if print_ and print_ in published_prints:
                    counts["same text published elsewhere"] += 1
                elif not print_:
                    counts["no text in source"] += 1
                    emptied.append("%s/%s" % (project_dir, posix))
                else:
                    counts["unique, not published"] += 1
                    unique_unpublished.append((project_dir, posix))
        rows.append((project_dir, is_published, len(entries), counts))
        for key, value in counts.items():
            grand[key] += value
        grand["topics"] += len(entries)

    # ---- pages on the site with no Flare origin --------------------------- #
    generated, unexplained = [], []
    for path in sorted(DOCS.rglob("*.md")):
        rel = path.relative_to(DOCS).as_posix()
        parts = rel.split("/")
        prefix = "/".join(parts[:2])
        md_rel = "/".join(parts[2:])
        if rel == "index.md" or len(parts) == 2 and parts[1] == "index.md":
            generated.append(rel)
        elif (prefix, md_rel) in page_origin:
            continue
        elif md_rel == "index.md":
            generated.append(rel)
        else:
            unexplained.append(rel)

    lines = [
        "# Migration completeness",
        "",
        "Every topic in the shared MadCap Flare sources, and every page on the",
        "site, accounted for. Regenerate with",
        "`python3 tools/flare2md/completeness.py`.",
        "",
        "## Part 1 — nothing missed",
        "",
        "| Project | Topics | Published | Book artifacts | Same text elsewhere | No text | Unique, unpublished | Why not published |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for project, is_published, total, counts in rows:
        why = "" if is_published else exclusion_reason(project)
        lines.append("| `%s` | %d | %d | %d | %d | %d | %d | %s |" % (
            project, total,
            counts["published"], counts["book artifact"],
            counts["same text published elsewhere"], counts["no text in source"],
            counts["unique, not published"], why))
    lines.append("| **total** | **%d** | **%d** | **%d** | **%d** | **%d** | **%d** | |" % (
        grand["topics"], grand["published"], grand["book artifact"],
        grand["same text published elsewhere"], grand["no text in source"],
        grand["unique, not published"]))

    lines += ["", "### Unique topics that are not published", ""]
    if not unique_unpublished:
        lines.append("None: every topic with text either is published, or its "
                     "text is published from another project.")
    else:
        lines.append("Topics whose text appears nowhere in the published set. "
                     "Each needs a decision: publish it, or record why not.")
        lines.append("")
        by_project = defaultdict(list)
        for project, posix in unique_unpublished:
            by_project[project].append(posix)
        for project, items in sorted(by_project.items()):
            reason = G.EXCLUDED.get(project, "")
            lines.append("<details><summary><code>%s</code> — %d topics%s</summary>"
                         % (project, len(items), " — " + reason if reason else ""))
            lines.append("")
            for posix in sorted(items):
                lines.append("- `%s`" % posix)
            lines.append("")
            lines.append("</details>")
            lines.append("")

    lines += ["", "### Topics with no text in the source", "",
              "Empty or wholly condition-excluded topics; nothing to publish.", ""]
    for item in sorted(emptied)[:60]:
        lines.append("- `%s`" % item)
    if len(emptied) > 60:
        lines.append("- ... and %d more" % (len(emptied) - 60))

    lines += ["", "## Part 2 — nothing extra", "",
              "Every page on the site traced back to the Flare topic it came from.", "",
              "| Pages on the site | From a Flare topic | Generated landing pages | Unexplained |",
              "| --- | --- | --- | --- |"]
    total_pages = len(list(DOCS.rglob("*.md")))
    lines.append("| %d | %d | %d | %d |" % (
        total_pages, len(page_origin), len(generated), len(unexplained)))
    lines += ["", "Landing pages are site scaffolding — the portal home, one per",
              "product family, one per guide — and contain no documentation text",
              "beyond the guide titles and summaries in `tools/flare2md/guides.py`.", ""]
    if unexplained:
        lines += ["### Pages with no Flare origin", ""]
        for rel in unexplained:
            lines.append("- `%s`" % rel)
    else:
        lines.append("No page on the site is without a Flare source topic.")

    (REPORTS / "migration-completeness.md").write_text("\n".join(lines) + "\n",
                                                       encoding="utf-8")
    print("\n".join(lines[6:6 + 8 + len(rows)]))
    print()
    print("unique unpublished topics: %d | pages with no Flare origin: %d"
          % (len(unique_unpublished), len(unexplained)))
    print("wrote %s" % (REPORTS / "migration-completeness.md"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
