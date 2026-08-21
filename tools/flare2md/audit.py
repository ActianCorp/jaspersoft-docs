#!/usr/bin/env python3
"""audit.py — prove that nothing was missed.

Walks every Flare project in the repository, classifies every source topic, and
writes zensical-site/_reports/coverage.md:

  * converted            published by at least one guide
  * book artifact        printed title page / generated TOC / index (SKIP_TOPICS)
  * orphan               in a published project but in no TOC and linked from
                         nowhere — reported by name so it can be triaged
  * excluded project     project deliberately not published (reason given)
  * unused TOC           a .fltoc in a published project that no guide uses

Usage: python3 tools/flare2md/audit.py
"""
from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import build as B
import guides as G

REPO = B.REPO
REPORTS = B.REPORTS

# Directories that hold no publishable topics.
NON_CONTENT_DIRS = {"Resources"}


def content_roots(project: Path):
    """Content directories in a project. Some containers (ServicePacks,
    Standalone) hold one Flare project per subdirectory."""
    if (project / "Content").is_dir():
        return [project / "Content"]
    return sorted(p for p in project.glob("*/Content") if p.is_dir())


def project_topics(project: Path):
    out = []
    for content in content_roots(project):
        for suffix in ("*.htm", "*.html"):
            for path in content.rglob(suffix):
                rel = path.relative_to(content)
                if rel.parts[0] in NON_CONTENT_DIRS:
                    continue
                out.append(rel)
    return sorted(set(out))


VERSION_PROSE_RE = re.compile(r"\b(?:9|10)\.\d+(?:\.\d+)?\b")

BRAND_LEFTOVERS = (
    ("TIBCO in product names and prose", re.compile(r"TIBCO")),
    ("Links to the previous owner's sites", re.compile(r"(cloud\.com|tibco\.com)")),
)


def brand_hits(pattern):
    """[(page, occurrences)] for a branding pattern, most-frequent first."""
    docs = REPO / "zensical-site" / "docs"
    hits = []
    for path in sorted(docs.rglob("*.md")):
        count = len(pattern.findall(path.read_text(encoding="utf-8")))
        if count:
            hits.append((path.relative_to(docs).as_posix(), count))
    hits.sort(key=lambda row: (-row[1], row[0]))
    return hits


def version_prose():
    """Sentences in the converted pages that name a release number."""
    docs = REPO / "zensical-site" / "docs"
    hits = []
    for path in sorted(docs.rglob("*.md")):
        if path.name == "index.md":
            continue  # generated landing pages, not source prose
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            stripped = line.strip()
            if not VERSION_PROSE_RE.search(stripped):
                continue
            # Skip code, tables, paths and front matter: only prose needs a call.
            if stripped.startswith(("|", "`", "<", "-", "*", "description:", "title:")):
                continue
            if "```" in stripped or "/" in stripped.split(" ")[0]:
                continue
            hits.append((path.relative_to(docs).as_posix(), number,
                         stripped[:140]))
    return hits


def main() -> int:
    manifests = {}
    for guide in G.GUIDES:
        prefix = "%s/%s" % (guide["family"], guide["key"])
        path = REPORTS / ("%s.manifest.json" % prefix.replace("/", "__"))
        if path.is_file():
            manifests[prefix] = json.loads(path.read_text(encoding="utf-8"))

    if not manifests:
        print("no manifests in %s — run build.py first" % REPORTS)
        return 1

    # source topic -> guides that published it
    published = defaultdict(set)
    for prefix, manifest in manifests.items():
        project = next(
            "%s/%s" % (g["family"], g["key"]) == prefix and g["project"] or None
            for g in G.GUIDES
            if "%s/%s" % (g["family"], g["key"]) == prefix
        )
        for rel in manifest:
            published[(project, rel)].add(prefix)

    used_tocs = {(g["project"], g["toc"]) for g in G.GUIDES}
    published_projects = sorted({g["project"] for g in G.GUIDES})

    lines = [
        "# Source coverage audit",
        "",
        "Every topic in every Flare project, and where it ended up.",
        "Regenerate with `python3 tools/flare2md/audit.py`.",
        "",
        "## Published projects",
        "",
        "| Project | Topics | Converted | Book artifacts | Orphans |",
        "| --- | --- | --- | --- | --- |",
    ]
    orphans_by_project = {}
    totals = [0, 0, 0, 0]
    for project in published_projects:
        topics = project_topics(REPO / project)
        converted = artifacts = 0
        orphans = []
        for rel in topics:
            key = (project, rel.as_posix())
            if key in published:
                converted += 1
            elif rel.as_posix().lower() in B.SKIP_TOPICS:
                artifacts += 1
            else:
                orphans.append(rel.as_posix())
        orphans_by_project[project] = orphans
        totals = [totals[0] + len(topics), totals[1] + converted,
                  totals[2] + artifacts, totals[3] + len(orphans)]
        lines.append("| `%s` | %d | %d | %d | %d |"
                     % (project, len(topics), converted, artifacts, len(orphans)))
    lines.append("| **total** | **%d** | **%d** | **%d** | **%d** |" % tuple(totals))

    lines += ["", "## Orphans (in a published project, in no guide)", ""]
    if not any(orphans_by_project.values()):
        lines.append("None: every topic in every published project is reachable.")
    for project, orphans in sorted(orphans_by_project.items()):
        if not orphans:
            continue
        lines.append("### `%s` — %d" % (project, len(orphans)))
        lines.append("")
        for rel in orphans:
            lines.append("- `%s`" % rel)
        lines.append("")

    lines += ["", "## Topics published in more than one guide", ""]
    shared = {k: v for k, v in published.items() if len(v) > 1}
    lines.append("%d topics appear in several guides (shared chapters, legal "
                 "notices, deliberate cross-guide references)." % len(shared))

    lines += ["", "## Unused TOCs in published projects", "",
              "Review drafts and per-chapter build TOCs; none define a "
              "published guide.", ""]
    for project in published_projects:
        toc_dir = REPO / project / "Project" / "TOCs"
        if not toc_dir.is_dir():
            continue
        unused = sorted(
            p.relative_to(toc_dir).as_posix()
            for p in toc_dir.rglob("*.fltoc")
            if (project, p.relative_to(toc_dir).as_posix()) not in used_tocs
        )
        if unused:
            lines.append("- `%s`: %s" % (project, ", ".join("`%s`" % u for u in unused)))

    lines += ["", "## Projects not published", ""]
    published_names = {rel.name.lower() for (_p, rel_str) in published
                       for rel in [Path(rel_str)]}
    unique_by_project = {}
    for project, why in sorted(G.EXCLUDED.items()):
        topics = project_topics(REPO / project)
        unique = sorted(rel.as_posix() for rel in topics
                        if rel.name.lower() not in published_names)
        unique_by_project[project] = unique
        lines.append("- `%s` (%d topics, %d with no same-named page in the "
                     "published set) — %s" % (project, len(topics), len(unique), why))

    lines += ["", "### Topics that exist only in an unpublished project", "",
              "Filenames with no counterpart anywhere in the published set. "
              "Review these if anything looks like current content rather than "
              "an older release or a build shell.", ""]
    for project, unique in sorted(unique_by_project.items()):
        if not unique:
            continue
        lines.append("<details><summary><code>%s</code> — %d</summary>"
                     % (project, len(unique)))
        lines.append("")
        for rel in unique[:400]:
            lines.append("- `%s`" % rel)
        if len(unique) > 400:
            lines.append("- ... and %d more" % (len(unique) - 400))
        lines.append("")
        lines.append("</details>")
        lines.append("")

    lines += ["", "## Hard-coded version numbers in prose", "",
              "The site publishes **%s** only, and every `productVersion` "
              "variable is pinned to it. These sentences name a release in the "
              "text itself, so they need an editorial decision rather than a "
              "find-and-replace: some are correct history (\"as of release "
              "X\"), others describe the current release." % G.SITE_VERSION, ""]
    hits = version_prose()
    if not hits:
        lines.append("None found.")
    for path, line_no, text in hits:
        lines.append("- `%s:%d` — %s" % (path, line_no, text))

    lines += ["", "## Branding left for an editorial or legal decision", "",
              "The owning company is renamed to Actian during conversion "
              "(`BRAND_REPLACEMENTS` in `guides.py`). These references are not "
              "touched, because changing them means changing a product name, a "
              "link target, or the entity a legal notice points at:", ""]
    for label, pattern in BRAND_LEFTOVERS:
        hits = brand_hits(pattern)
        lines.append("- **%s** — %d occurrences in %d pages"
                     % (label, sum(n for _f, n in hits), len(hits)))
        for path, count in hits[:8]:
            lines.append("    - `%s` (%d)" % (path, count))
        if len(hits) > 8:
            lines.append("    - ... and %d more pages" % (len(hits) - 8))

    (REPORTS / "coverage.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines[:20]))
    print("...\nwrote %s" % (REPORTS / "coverage.md"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
