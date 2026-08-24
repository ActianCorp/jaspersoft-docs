#!/usr/bin/env python3
"""compare_published.py — diff our pages against the published source site.

Input  scratchpad/src-pages.jsonl  — one record per page crawled from
       community.jaspersoft.com (?_version=10.1.0): guide, slug, h1, text, imgs
Output _reports/published-comparison.md

The source site and this site are both generated from the same MadCap Flare
topics, and its URLs encode the Flare path: a page at
`Content/JasperReports-Server-User-Guide/introduction/intro_login.htm` is served
as `.../v1010/jasperreports-server-user-guide-_-introduction-_-intro_login/`.
That makes the two page sets directly comparable: the slug is rebuilt from each
entry in our conversion manifests and matched against the crawl.

Reported per guide: pages published there but missing here, pages here with no
counterpart there, and for matched pages the words present in their text but
not in ours, plus any image count shortfall.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
REPORTS = REPO / "zensical-site" / "_reports"
DOCS = REPO / "zensical-site" / "docs"
SITE = REPO / "zensical-site" / "site"

# Published guide (source site) -> our guide directory.
GUIDE_MAP = {
    "jasperreports-server/jasperreports®-server-user-guide": "jasperreports-server/user-guide",
    "jasperreports-server/jasperreports®-server-administrator-guide": "jasperreports-server/administrator-guide",
    "jasperreports-server/jasperreports®-server-installation-guide": "jasperreports-server/installation-guide",
    "jasperreports-server/jasperreports®-server-upgrade-guide": "jasperreports-server/upgrade-guide",
    "jasperreports-server/jasperreports®-server-source-build-guide": "jasperreports-server/source-build-guide",
    "jasperreports-server/jasperreports®-server-security-guide": "jasperreports-server/security-guide",
    "jasperreports-server/jasperreports®-server-authentication-cookbook": "jasperreports-server/authentication-cookbook",
    "jasperreports-server/jasperreports®-server-data-management-using-domains": "jasperreports-server/data-management-using-domains",
    "jasperreports-server/jasperreports®-server-rest-api-reference": "jasperreports-server/rest-api-reference",
    "jasperreports-server/jasperreports®-server-visualizejs-guide": "jasperreports-server/visualize-js-guide",
    "jasperreports-server/jasperreports®-server-release-notes": "jasperreports-server/release-notes",
    "jasperreports-server/jasperreports®-server-platform-support-guide": "jasperreports-server/platform-support-guide",
    "jasperreports-server/jasperreports®-olap-user-guide": "jasperreports-server/olap-user-guide",
    "jasperreports-server/jasperreports®-olap-ultimate-guide": "jasperreports-server/olap-ultimate-guide",
    "jaspersoft®-studio/jaspersoft®-studio-user-guide": "jaspersoft-studio/user-guide",
    "jasperreports-io/jasperreports®-io-professional-edition-user-guide": "jasperreports-io/professional-user-guide",
    "jasperreports-io/jasperreports®-io-at-scale-user-guide": "jasperreports-io/at-scale-user-guide",
    "jasperreports®-web-studio/jasperreports®-web-studio-user-guide": "jasperreports-web-studio/user-guide",
    # Published but not converted; recorded so the gap is explicit.
    "jaspersoft®-studio/jaspersoft®-studio-source-build-guide": "jaspersoft-studio/source-build-guide",
}

WORD_RE = re.compile(r"[0-9a-z]+")
# Site chrome that surrounds the article text on either site.
CHROME = re.compile(
    r"skip to content|sign in|join the community|knowledge base|all activity|"
    r"light mode|dark mode|system preference|cookie|privacy|terms of use|"
    r"was this page helpful|previous\b|next\b|table of contents|on this page|"
    r"products|explore|linkedin|youtube|rss|contact us|search\.\.\.|"
    r"© \d{4}|all rights reserved",
    re.I,
)


def words(text: str):
    return WORD_RE.findall(text.lower())


def slug_for(htm_rel: str) -> str:
    """Flare content path -> published slug.

    Their slugs keep underscores inside a name ("intro_login"), turn spaces into
    hyphens ("user favorites/User Favorites.htm"), and drop dots entirely
    ("Visualize.js-Guide" -> "visualizejs-guide", "plan-upgrade-9.0" ->
    "plan-upgrade-90").
    """
    stem = htm_rel.lower().removesuffix(".htm").removesuffix(".html")
    return stem.replace(" ", "-").replace(".", "").replace("/", "-_-")


def our_pages():
    """(guide prefix -> {published slug: (md path, title)}) from the manifests."""
    out = {}
    for path in sorted(REPORTS.glob("*.manifest.json")):
        prefix = path.name[: -len(".manifest.json")].replace("__", "/")
        manifest = json.loads(path.read_text(encoding="utf-8"))
        out[prefix] = {slug_for(htm): tuple(v) for htm, v in manifest.items()}
    return out


def page_text(prefix: str, md_rel: str) -> str:
    """Visible text of our built page."""
    stem = md_rel[:-3] if md_rel.endswith(".md") else md_rel
    stem = stem[: -len("/index")] if stem.endswith("/index") else stem
    path = SITE / prefix / stem / "index.html"
    if not path.is_file():
        return ""
    html = path.read_text(encoding="utf-8", errors="replace")
    body = html.split("<article", 1)[-1].split("</article>", 1)[0]
    body = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", body)
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", body))


def page_images(prefix: str, md_rel: str) -> int:
    stem = md_rel[:-3] if md_rel.endswith(".md") else md_rel
    stem = stem[: -len("/index")] if stem.endswith("/index") else stem
    path = SITE / prefix / stem / "index.html"
    if not path.is_file():
        return 0
    body = path.read_text(encoding="utf-8", errors="replace")
    body = body.split("<article", 1)[-1].split("</article>", 1)[0]
    return body.count("<img ")


def strip_chrome(text: str) -> str:
    """Drop navigation/footer lines so only article prose is compared."""
    keep = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or CHROME.search(stripped) and len(stripped) < 80:
            continue
        keep.append(stripped)
    return " ".join(keep)


def main(argv) -> int:
    crawl = Path(argv[1]) if len(argv) > 1 else (
        Path("/private/tmp/claude-501/-Users-bipinpandey-jaspersoft-userdocs/"
             "2a253ce5-dd8f-40ec-a4d4-c1e88170a5a7/scratchpad/src-pages2.jsonl"))
    if not crawl.is_file():
        print("no crawl data at %s" % crawl)
        return 1

    source = {}
    for line in crawl.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        rec = json.loads(line)
        source.setdefault(rec["guide"], {})[rec["slug"]] = rec

    ours = our_pages()
    lines = [
        "# Published site comparison",
        "",
        "Our pages against **community.jaspersoft.com (10.1.0)**, matched by the",
        "Flare topic path both sites encode in their URLs.",
        "",
        "| Published guide | Their pages | Matched | Missing here | Extra here |",
        "| --- | --- | --- | --- | --- |",
    ]
    missing_detail, extra_detail, content_detail = [], [], []
    totals = [0, 0, 0, 0]

    for src_guide, pages in sorted(source.items()):
        our_prefix = GUIDE_MAP.get(src_guide, "?")
        if our_prefix is None:
            lines.append("| `%s` | %d | **not converted** | %d | – |"
                         % (src_guide, len(pages), len(pages)))
            totals[0] += len(pages)
            totals[2] += len(pages)
            missing_detail.append((src_guide, "whole guide not converted",
                                   sorted(pages)[:10]))
            continue
        mine = ours.get(our_prefix, {})
        matched = [s for s in pages if s in mine]
        missing = [s for s in pages if s not in mine]
        extra = [s for s in mine if s not in pages]
        totals = [totals[0] + len(pages), totals[1] + len(matched),
                  totals[2] + len(missing), totals[3] + len(extra)]
        lines.append("| `%s` | %d | %d | %d | %d |"
                     % (src_guide, len(pages), len(matched), len(missing), len(extra)))
        if missing:
            missing_detail.append((src_guide, our_prefix, sorted(missing)))
        if extra:
            extra_detail.append((src_guide, our_prefix, sorted(extra)))

        for slug in matched:
            rec = pages[slug]
            md_rel, _title = mine[slug]
            theirs = words(strip_chrome(rec["text"]))
            mine_words = words(strip_chrome(page_text(our_prefix, md_rel)))
            if not theirs:
                continue
            pool = {}
            for w in mine_words:
                pool[w] = pool.get(w, 0) + 1
            lost = []
            for w in theirs:
                if pool.get(w):
                    pool[w] -= 1
                else:
                    lost.append(w)
            ratio = len(lost) / len(theirs)
            their_imgs = len([i for i in rec["imgs"] if i])
            our_imgs = page_images(our_prefix, md_rel)
            # Their icon images (note/warning/pro badges) become admonitions
            # here, so a shortfall of a couple is expected, not a loss.
            if ratio > 0.05 or our_imgs < their_imgs - 2:
                content_detail.append((ratio, our_prefix, md_rel, slug,
                                       their_imgs, our_imgs, " ".join(lost[:20])))

    lines.append("| **total** | **%d** | **%d** | **%d** | **%d** |" % tuple(totals))

    lines += ["", "## Published pages with no page here", ""]
    if not missing_detail:
        lines.append("None.")
    for guide, prefix, slugs in missing_detail:
        lines.append("### `%s` -> `%s` — %d" % (guide, prefix, len(slugs)))
        lines.append("")
        for s in slugs:
            lines.append("- `%s`" % s)
        lines.append("")

    lines += ["", "## Pages here with no published counterpart", "",
              "Expected for shared front/back matter and for topics the "
              "published TOC drops; listed so each can be judged.", ""]
    for guide, prefix, slugs in extra_detail:
        lines.append("<details><summary><code>%s</code> — %d</summary>" % (prefix, len(slugs)))
        lines.append("")
        for s in slugs:
            lines.append("- `%s`" % s)
        lines.append("")
        lines.append("</details>")
        lines.append("")

    lines += ["", "## Matched pages with content differences", "",
              "Words in their article text absent from ours (>5%), or fewer "
              "images than the published page.", "",
              "| Missing | Page | Their imgs | Our imgs | Sample of missing words |",
              "| --- | --- | --- | --- | --- |"]
    for ratio, prefix, md_rel, slug, ti, oi, sample in sorted(content_detail, reverse=True)[:120]:
        lines.append("| %.1f%% | `%s/%s` | %d | %d | %s |"
                     % (ratio * 100, prefix, md_rel, ti, oi, sample[:90]))
    if not content_detail:
        lines.append("| – | none | | | |")

    (REPORTS / "published-comparison.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines[:14]))
    print("...\nwrote %s" % (REPORTS / "published-comparison.md"))
    print("content differences flagged: %d" % len(content_detail))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
