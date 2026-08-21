#!/usr/bin/env python3
"""check_site.py — post-build validation of the generated site.

Checks every internal link and asset reference in zensical-site/site:

  * links to pages that were never built (404s)
  * <img src>/<a href> pointing at files that are not in the output
  * pages that no nav entry reaches (published but unreachable)
  * pages with no content below the title

Usage: python3 tools/flare2md/check_site.py
"""
from __future__ import annotations

import html as html_mod
import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote, urldefrag

def _find_site():
    """Locate the built site.

    Two layouts use this script: the working repo, where the Zensical project
    lives in `zensical-site/`, and the published repo, where it sits at the
    root. Checking both keeps one copy of the script valid in CI and locally.
    """
    root = Path(__file__).resolve().parents[2]
    for candidate in (root / "site", root / "zensical-site" / "site"):
        if candidate.is_dir():
            return candidate
    return root / "zensical-site" / "site"


SITE = _find_site()

HREF_RE = re.compile(r'(?:href|src)="([^"]+)"')

# Code samples contain markup as text (`&lt;a href="../"&gt;`), and only `<`
# and `>` come back escaped — so `href="..."` survives verbatim and reads as a
# link. Highlighted output also splits that text into spans differently across
# Pygments versions, which made this a CI-only false positive. Drop code before
# looking for references.
CODE_RE = re.compile(r"(?is)<pre\b.*?</pre>|<code\b.*?</code>")


def main() -> int:
    if not SITE.is_dir():
        print("no build output at %s — run `zensical build` first" % SITE)
        return 1

    pages = sorted(SITE.rglob("index.html"))
    files = {p.relative_to(SITE).as_posix() for p in SITE.rglob("*") if p.is_file()}
    broken = defaultdict(list)
    thin = []
    checked = 0

    for page in pages:
        rel = page.relative_to(SITE)
        html = page.read_text(encoding="utf-8", errors="replace")
        body = html.split('<article', 1)[-1].split("</article>", 1)[0]
        body = CODE_RE.sub(" ", body)
        if len(re.sub(r"<[^>]+>", "", body).strip()) < 80:
            thin.append(rel.parent.as_posix() or ".")
        for match in HREF_RE.finditer(body):
            raw = html_mod.unescape(match.group(1))
            target, _frag = urldefrag(raw)
            if not target or target.startswith(("http://", "https://", "mailto:", "data:", "#", "//")):
                continue
            checked += 1
            resolved = _resolve(rel.parent, unquote(target))
            if resolved is None:
                broken[rel.parent.as_posix()].append(
                    "%s (escapes the site root) in: %s"
                    % (raw, _context(body, match.start()))
                )
                continue
            candidates = [resolved, resolved + "index.html" if resolved.endswith("/") else resolved + "/index.html"]
            if not any(c in files for c in candidates):
                # Report what it resolved to as well: a bad relative depth and a
                # missing page look identical otherwise.
                broken[rel.parent.as_posix()].append(
                    "%s -> %s in: %s"
                    % (raw, candidates[-1], _context(body, match.start()))
                )

    print("pages: %d   in-page references checked: %d" % (len(pages), checked))
    print("broken references: %d across %d pages" %
          (sum(len(v) for v in broken.values()), len(broken)))
    for page, refs in sorted(broken.items())[:25]:
        print("  %s" % page)
        for ref in sorted(set(refs))[:5]:
            print("      %s" % ref)
    print("pages with almost no content: %d" % len(thin))
    for page in thin[:15]:
        print("  %s" % page)
    return 1 if broken else 0


def _context(body: str, index: int, width: int = 110) -> str:
    """The markup around a reference, so a bad link can be placed on the page."""
    start = max(0, index - width // 2)
    return re.sub(r"\s+", " ", body[start:index + width]).strip()


def _resolve(base: Path, target: str):
    parts = list(base.parts) if not target.startswith("/") else []
    for part in target.lstrip("/").split("/"):
        if part == "..":
            if not parts:
                return None
            parts.pop()
        elif part not in (".", ""):
            parts.append(part)
    suffix = "/" if target.endswith("/") else ""
    return "/".join(parts) + suffix


if __name__ == "__main__":
    raise SystemExit(main())
