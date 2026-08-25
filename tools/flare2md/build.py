#!/usr/bin/env python3
"""build.py — convert every guide in guides.py and regenerate the Zensical site.

    python3 tools/flare2md/build.py            # all guides
    python3 tools/flare2md/build.py user-guide # one guide (by key)

What it produces under zensical-site/:
    docs/<family>/<guide>/**.md      converted topics (paths mirror Flare)
    docs/<family>/<guide>/index.md   guide landing page
    docs/<family>/index.md           product-family landing page
    docs/index.md                    portal home
    nav.toml                         generated `nav` block, included by hand
    zensical.toml                    nav block replaced in place
    _reports/<guide>.log             per-guide conversion warnings
    _reports/summary.md              coverage + warning counts for all guides

Topic selection is the TOC plus the link closure of those topics, so a page
that is only reachable by a cross-reference still gets converted and its link
still resolves.
"""
from __future__ import annotations

import json
import re
import shutil
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import flare2md as f2
import guides as G
import make_brand_assets
from lxml import etree

REPO = Path(__file__).resolve().parents[2]
SITE = REPO / "zensical-site"
DOCS = SITE / "docs"
REPORTS = SITE / "_reports"

ALL_GUIDE_CONDITIONS = [
    "jrio-pro-relnotes", "jrio-pro-user", "jrio-user", "jrs-admin", "jrs-domains",
    "jrs-install", "jrs-olap-ultimate", "jrs-olap-user",
    "jrs-platform-support-commercial", "jrs-platform-support-community",
    "jrs-rest-api-ref", "jrs-security", "jrs-sourceBuild", "jrs-ultimate",
    "jrs-upgrade", "jrs-visualize",
]

# Book-only artifacts: the printed title page, the generated table of contents
# and the index. The site provides its own landing pages, nav and search.
SKIP_TOPICS = {
    "_globalpages/title.htm",
    "_globalpages/contents.htm",
    "_globalpages/index.htm",
    "_templates/home.htm",
    "bookmatter/toc.htm",
    "bookmatter/index.htm",
    "bookmatter/frontmatter.htm",
}

HREF_RE = re.compile(r"""(?:href|src)\s*=\s*["']([^"'#]+)""", re.I)


# --------------------------------------------------------------------------- #
# TOC handling
# --------------------------------------------------------------------------- #
def toc_link_to_rel(link: str):
    """'/Content/dir/topic.htm' -> Path('dir/topic.htm'); None if not local."""
    if not link:
        return None
    link = link.split("#", 1)[0]
    marker = "/Content/"
    if marker not in link:
        return None
    from urllib.parse import unquote
    rel = unquote(link.split(marker, 1)[1])
    if not rel.lower().endswith(f2.TOPIC_SUFFIXES):
        return None
    return Path(rel)


def parse_toc(path: Path, warn):
    """Return the TOC as a nested list of {'title', 'rel', 'children'}."""
    root = f2.parse_flare(path, warn)

    def walk(elem):
        out = []
        for entry in elem.findall("TocEntry"):
            title = entry.get("Title") or ""
            if title.startswith("[%="):
                title = ""
            rel = toc_link_to_rel(entry.get("Link", ""))
            out.append({"title": title, "rel": rel, "children": walk(entry)})
        return out

    return walk(root)


def flatten_toc(nodes):
    for node in nodes:
        if node["rel"] is not None:
            yield node["rel"]
        for rel in flatten_toc(node["children"]):
            yield rel


# --------------------------------------------------------------------------- #
# Topic selection
# --------------------------------------------------------------------------- #
def project_topic_index(content_root: Path):
    """filename -> {content-relative paths}, for repairing bad relative links."""
    index = {}
    for suffix in f2.TOPIC_SUFFIXES:
        for path in content_root.rglob("*" + suffix):
            rel = path.relative_to(content_root)
            index.setdefault(path.name.lower(), set()).add(rel)
    return index


def link_closure(seeds, content_root: Path, warn):
    """TOC topics plus every topic reachable from them by a link.

    Links whose relative depth is wrong in the source (Flare tolerates some of
    these) are repaired when the filename is unique in the project, so the
    target page is still published rather than silently lost.
    """
    index = project_topic_index(content_root)
    kept, queue = set(), list(seeds)
    while queue:
        rel = queue.pop()
        if rel in kept:
            continue
        path = content_root / rel
        if not path.is_file():
            warn("TOC/link target missing on disk: %s" % rel)
            continue
        kept.add(rel)
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            warn("unreadable topic %s: %s" % (rel, exc))
            continue
        for href in HREF_RE.findall(text):
            if href.startswith(("http:", "https:", "mailto:", "data:", "ftp:")):
                continue
            if not href.lower().endswith(f2.TOPIC_SUFFIXES):
                continue
            from urllib.parse import unquote
            target = f2._normalize(rel.parent / unquote(href))
            if target is None or not (content_root / target).is_file():
                matches = index.get(Path(unquote(href)).name.lower(), set())
                target = next(iter(matches)) if len(matches) == 1 else target
            if target is not None and target not in kept:
                queue.append(target)
    return kept


def main_content_dir(seeds):
    """The guide's own content directory, as named by its TOC.

    Ties break on the directory name, not on iteration order: a small guide can
    have as many TOC entries in `_templates` as in its own directory, and page
    URLs must not depend on which one a set happened to yield first.
    """
    tops = Counter(rel.parts[0] for rel in seeds if len(rel.parts) > 1)
    if not tops:
        return None
    return min(tops.items(), key=lambda item: (-item[1], item[0]))[0]


def output_layout(kept, seeds, warn):
    """content-rel -> guide-relative .md path.

    The guide's own content directory is stripped from the URL (it repeats the
    guide name), shared directories such as BookMatter are kept. The main
    directory is taken from the TOC only: topics dragged in by cross-references
    must not be able to change every other page's URL. Names are lowercased and
    spaces hyphenated for clean URLs; collisions fall back to the full path.
    """
    main = main_content_dir(seeds or kept)
    layout, taken = {}, {}
    for rel in sorted(kept):
        parts = list(rel.parts)
        if main and parts[0] == main and len(parts) > 1:
            parts = parts[1:]
        slug = "/".join(_slug(p) for p in parts)
        slug = str(Path(slug).with_suffix(".md"))
        if slug in taken:
            slug = "/".join(_slug(p) for p in rel.parts)
            slug = str(Path(slug).with_suffix(".md"))
            warn("output name collision, using full path for %s" % rel)
        taken[slug] = rel
        layout[rel] = slug
    return layout


def _slug(name: str) -> str:
    name = name.replace(" ", "-").replace("%20", "-")
    name = re.sub(r"-{2,}", "-", name)
    return name.lower()


# --------------------------------------------------------------------------- #
# Conversion
# --------------------------------------------------------------------------- #
def prepare_guide(guide, warn):
    """Everything needed before conversion: target, variables, TOC, topic set.

    Split out from conversion so that all guides' page maps exist before any
    page is written; cross-guide links can then be resolved to real pages
    instead of being dropped.
    """
    project = REPO / guide["project"]
    content_root = project / "Content"

    if guide.get("target"):
        target = f2.load_target(project / "Project" / "Targets" / guide["target"], warn)
    else:
        target = f2.synthetic_target(guide["guide_condition"], ALL_GUIDE_CONDITIONS, warn)

    # The target's MasterToc wins over the one named in guides.py. A release can
    # introduce a versioned TOC and repoint the target at it — 10.1 does exactly
    # that for the Upgrade Guide — and following the target picks the new
    # structure up without an edit here.
    toc_path = project / "Project" / "TOCs" / guide["toc"]
    if target.toc:
        from_target = project / target.toc.lstrip("/")
        if from_target.is_file():
            if from_target != toc_path:
                warn("using the target's TOC: %s (guides.py names %s)"
                     % (target.toc.lstrip("/"), guide["toc"]))
            toc_path = from_target
        else:
            warn("target names a TOC that is not on disk: %s" % target.toc)

    # Publish one version only: pin every version variable to it, whatever the
    # project or target happens to carry.
    target.overrides["globalvar.company"] = "Actian"
    target.overrides["productvar.productVersion"] = G.SITE_VERSION
    target.overrides["JasperBookVariables.JasperPackageNumber"] = G.SITE_VERSION
    target.overrides["JasperBookVariables.BookSoftwareVersion"] = \
        ".".join(G.SITE_VERSION.split(".")[:2])

    shared = REPO / "js-shared"
    variables = f2.load_variables([project] + ([shared] if shared.is_dir() else []), warn)

    toc = parse_toc(toc_path, warn)
    seeds = [rel for rel in flatten_toc(toc)
             if rel.as_posix().lower() not in SKIP_TOPICS]
    kept = link_closure(seeds, content_root, warn)
    kept = {rel for rel in kept if rel.as_posix().lower() not in SKIP_TOPICS}

    return dict(
        guide=guide,
        project=project,
        content_root=content_root,
        target=target,
        variables=variables,
        toc=toc,
        seeds=set(seeds),
        kept=kept,
        main_dir=main_content_dir(set(seeds)),
        layout=output_layout(kept, set(seeds), warn),
        images=f2.image_index(content_root),
        snippet_roots=[d for d in (REPO / "js-shared" / "Content" / "_globalsnippets",
                                   REPO / "js-shared" / "Content" / "_templates")
                       if d.is_dir()],
        prefix="%s/%s" % (guide["family"], guide["key"]),
        version=f2._lookup_variable("productvar.productVersion", variables, target.overrides) or "",
        ga_date=f2._lookup_variable("productvar.GADate", variables, target.overrides) or "",
    )


NON_CONTENT_DIRS = {"Resources"}


def project_topics(content_root: Path):
    """Every publishable topic in a project, TOC or not."""
    out = set()
    for suffix in f2.TOPIC_SUFFIXES:
        for path in content_root.rglob("*" + suffix):
            rel = path.relative_to(content_root)
            if rel.parts[0] in NON_CONTENT_DIRS:
                continue
            if rel.as_posix().lower() in SKIP_TOPICS:
                continue
            out.add(rel)
    return out


def surviving_content(rel, plan, warn):
    """(text, image count) a topic still has after the source's own filtering.

    Only the cheap front half of the pipeline runs — snippets, conditions,
    variables, draft removal — which is enough to tell whether anything is left
    to publish. Headings are excluded from the text: a topic reduced to its
    title has no content, and that is exactly what a body wrapped in
    `MadCap:conditions="DoNotPublish"` leaves behind.
    """
    topic = plan["content_root"] / rel
    root = f2.parse_flare(topic, warn)
    body = f2.body_of(root)
    f2.inline_snippets(body, topic.parent, warn, fallbacks=plan["snippet_roots"])
    f2.apply_conditions(body, plan["target"])
    f2.resolve_variables(body, plan["variables"], plan["target"].overrides, warn)
    f2.drop_draft_content(body)
    for node in list(body.iter()):
        if isinstance(node.tag, str) and re.fullmatch(r"h[1-6]", node.tag):
            f2._drop_keeping_tail(node)
    text = re.sub(r"\s+", "", "".join(body.itertext()))
    return text, len(body.findall(".//img"))


def prune_empty_topics(plans, warn):
    """Drop topics the source itself empties out.

    A handful of topics are wholly wrapped in `DoNotPublish` /
    `ExcludeFromHelp` / `ExcludeFromBuilds`, so nothing survives conversion and
    the page would be published as a bare title. Pruning here rather than after
    conversion means the link resolver and the navigation never point at them.
    """
    for plan in plans:
        empty = set()
        for rel in sorted(plan["kept"]):
            try:
                text, images = surviving_content(rel, plan, warn)
            except Exception as exc:  # noqa: BLE001
                warn("could not check %s for content: %s" % (rel, exc))
                continue
            if not text and not images:
                empty.add(rel)
        if not empty:
            continue
        plan["kept"] -= empty
        plan["layout"] = output_layout(plan["kept"], plan["seeds"], warn)
        plan["empty"] = sorted(rel.as_posix() for rel in empty)
        for rel in plan["empty"]:
            warn("not published, no content survives the source's conditions: %s" % rel)


def absorb_unreferenced(plans, warn):
    """Publish topics that exist in a project but appear in no TOC.

    Several projects have real content (data source chapters, installer modes,
    an OAuth recipe, the glossary) that the printed book's TOC dropped. Leaving
    them out would silently lose content, so each is attached to the guide that
    owns its content directory and listed under "Additional Topics".
    """
    by_project = defaultdict(list)
    for plan in plans:
        by_project[plan["guide"]["project"]].append(plan)

    for project, project_plans in by_project.items():
        content_root = project_plans[0]["content_root"]
        claimed = set()
        for plan in project_plans:
            claimed |= plan["kept"]
        leftovers = sorted(project_topics(content_root) - claimed)
        if not leftovers:
            continue
        # Fall back to the project's largest guide for shared directories
        # (BookMatter, _templates) that belong to no single guide. "Largest" is
        # measured by TOC size, which is stable: measuring converted pages would
        # move these shared pages between guides whenever anything else changed.
        primary = max(project_plans, key=lambda p: (len(p["seeds"]), p["prefix"]))
        extras = defaultdict(list)
        for rel in leftovers:
            owner = next(
                (p for p in project_plans if p["main_dir"] == rel.parts[0]), primary
            )
            extras[id(owner)].append(rel)

        for plan in project_plans:
            new = extras.get(id(plan))
            if not new:
                continue
            added = link_closure(new, content_root, warn) - plan["kept"]
            added = {rel for rel in added if rel.as_posix().lower() not in SKIP_TOPICS}
            plan["kept"] |= added
            plan["extras"] = sorted(added)
            plan["layout"] = output_layout(plan["kept"], plan["seeds"], warn)
            warn("added %d topics that no TOC references" % len(added))


class LinkResolver:
    """Resolves a Flare topic link to a site-relative markdown link.

    Three chances, in order of confidence:
      1. the same guide (the common case),
      2. the same topic published in another guide (shared chapters, and the
         upgrade guide's deliberate references into the installation guide),
      3. a unique filename match inside the same Flare project, which repairs
         links whose relative depth is wrong in the source.
    """

    def __init__(self, plans, warn):
        self.warn = warn
        self.by_topic = {}      # (project, rel) -> site path without .md
        self.by_name = {}       # (project, filename) -> set of rels
        for plan in plans:
            proj = plan["guide"]["project"]
            for rel, out_rel in plan["layout"].items():
                site = "%s/%s" % (plan["prefix"], out_rel)
                key = (proj, rel.as_posix())
                # A topic in a guide's own TOC wins over one pulled in by a link.
                if key not in self.by_topic or rel in plan["seeds"]:
                    self.by_topic[key] = site
                self.by_name.setdefault((proj, rel.name.lower()), set()).add(rel.as_posix())

    def for_topic(self, plan, topic_rel):
        proj = plan["guide"]["project"]
        here = Path("%s/%s" % (plan["prefix"], plan["layout"][topic_rel])).parent

        def resolve(_topic_rel, href_path):
            target = f2._normalize(topic_rel.parent / href_path)
            site = None
            if target is not None:
                site = self.by_topic.get((proj, target.as_posix()))
            if site is None:
                # Wrong relative depth in the source: fall back to a filename
                # match, narrowed by the path tail the source did spell out,
                # and preferring a page inside this same guide.
                name = Path(href_path).name.lower()
                matches = self.by_name.get((proj, name), set())
                tail = "/".join(
                    part for part in href_path.split("/") if part not in ("..", ".")
                ).lower()
                if len(matches) > 1:
                    exact = {m for m in matches if m.lower().endswith(tail)}
                    if exact:
                        matches = exact
                local = {m for m in matches
                         if Path(m) in plan["layout"]}
                if len(local) == 1:
                    matches = local
                if len(matches) == 1:
                    site = self.by_topic.get((proj, next(iter(matches))))
                    if site:
                        self.warn("repaired link by filename: %s (from %s)"
                                  % (href_path, topic_rel))
            if site is None:
                return None
            return f2._relative_to(Path(site), here)

        return resolve


def convert_guide(plan, resolver, warn):
    manifest = {}
    out_root = DOCS / plan["guide"]["family"] / plan["guide"]["key"]
    # Start from empty: a renamed or dropped topic must not linger as a stale
    # page that is still published and still indexed by search.
    if out_root.is_dir():
        shutil.rmtree(out_root)
    for rel in sorted(plan["kept"]):
        try:
            title = convert_topic(rel, plan, out_root, resolver, warn)
        except Exception as exc:  # noqa: BLE001 - one bad topic must not stop the run
            warn("FAILED %s: %s" % (rel, exc))
            continue
        manifest[rel.as_posix()] = (plan["layout"][rel], title)
    return manifest


def convert_topic(rel, plan, out_root, resolver, warn):
    content_root = plan["content_root"]
    target = plan["target"]
    variables = plan["variables"]
    layout = plan["layout"]

    topic = content_root / rel
    root = f2.parse_flare(topic, warn)
    body = f2.body_of(root)

    f2.inline_snippets(body, topic.parent, warn, fallbacks=plan["snippet_roots"])
    f2.apply_conditions(body, target)
    f2.resolve_variables(body, variables, target.overrides, warn)
    f2.resolve_variable_syntax(body, variables, target.overrides, warn)
    f2.apply_brand(body, G.BRAND_REPLACEMENTS)
    f2.drop_draft_content(body)
    f2.drop_empty_blocks(body)
    f2.unwrap_plain_divs(body)
    f2.fence_code_blocks(body)
    f2.normalize_tables(body)
    f2.note_tables_to_admonitions(body)
    f2.unwrap_figure_tables(body)
    f2.bulletize(body)
    f2.literal_bullets(body)
    f2.numberize(body)
    f2.merge_adjacent_lists(body)
    f2.continue_ordered_lists(body)
    f2.merge_interrupted_lists(body)
    f2.absorb_orphan_sublists(body)
    f2.loosen_list_items(body)
    f2.semantic_inlines(body)
    f2.handle_links(body)
    f2.collapse_nested_admonitions(body)

    title = f2.first_heading(body)

    out_rel = layout[rel]
    out_path = out_root / out_rel
    out_path.parent.mkdir(parents=True, exist_ok=True)
    depth = len(Path(out_rel).parts) - 1
    assets_rel = "../" * depth + "assets"

    f2.rewrite_tree_images(body, topic.parent, out_root / "assets" / "images",
                           assets_rel + "/images", warn, plan["images"])
    f2.copy_linked_files(body, topic.parent, out_root / "assets" / "files",
                         assets_rel + "/files", warn)
    f2.rewrite_tree_links(body, rel, resolver.for_topic(plan, rel), warn)

    # Admonitions must be pulled out before the remaining autonum labels are
    # flattened, otherwise "Note: " becomes bold body text instead of a block.
    admonitions = f2.extract_admonitions(body)
    f2.unwrap_divs(body)
    f2.handle_autonum(body)
    f2.strip_madcap(body)
    f2.strip_presentation(body)
    f2.promote_headings(body)
    f2.flatten_headings(body)
    f2.drop_empty_anchors(body)
    etree.cleanup_namespaces(root)

    chunks = [f2.inner_html(body)] + [a[2] for a in admonitions]
    rendered = f2.pandoc(chunks)
    bodies = [(admonitions[i][0], admonitions[i][1], rendered[i + 1],
               admonitions[i][2])
              for i in range(len(admonitions))]
    md = f2.expand_admonitions(rendered[0], bodies)
    md = f2.clean_markdown(md)

    if not title:
        heading = re.search(r"^#{1,3} (.+)$", md, re.M)
        title = heading.group(1).strip() if heading else Path(rel).stem.replace("_", " ")

    front = ["---", "title: %s" % f2.yaml_scalar(title)]
    desc = f2.description_of(md)
    if desc:
        front.append("description: %s" % f2.yaml_scalar(desc))
    front += ["---", "", ""]
    out_path.write_text("\n".join(front) + md, encoding="utf-8")
    return title


# --------------------------------------------------------------------------- #
# Navigation
# --------------------------------------------------------------------------- #
def nav_for_guide(toc, manifest, prefix, warn):
    """Flare TOC -> nav items, resolving titles from the converted topics.

    Flare TOCs deep-link to anchors within a topic; after fragments are dropped
    those collapse onto the parent page, so such entries are folded away (the
    in-page TOC already lists them) and repeats are de-duplicated.
    """
    def build(nodes, parent_path=None):
        items = []
        for node in nodes:
            rel = node["rel"]
            path = title = None
            if rel is not None:
                entry = manifest.get(rel.as_posix())
                if entry:
                    path = "%s/%s" % (prefix, entry[0])
                    title = entry[1]
                elif rel.as_posix().lower() not in SKIP_TOPICS:
                    warn("nav: no converted topic for %s" % rel)
            children = build(node["children"], path or parent_path)
            if path and path == parent_path:
                items.extend(children)
                continue
            title = node["title"] or title or "Untitled"
            if path and children:
                items.append({title: [{title: path}] + children})
            elif path:
                items.append({title: path})
            elif children:
                items.append({title: children})
        return items

    items = dedup(build(toc), set())
    # Anything converted but never referenced by the TOC still needs a home,
    # or it would be published but unreachable from the navigation.
    covered = set(iter_paths(items))
    extra = [
        {t: "%s/%s" % (prefix, p)}
        for (p, t) in sorted(manifest.values(), key=lambda x: x[1])
        if "%s/%s" % (prefix, p) not in covered
    ]
    if extra:
        items.append({"Additional Topics": extra})
    return items


def dedup(items, seen):
    out = []
    for item in items:
        (title, value), = item.items()
        if isinstance(value, str):
            if value in seen:
                continue
            seen.add(value)
            out.append({title: value})
        else:
            pruned = dedup(value, seen)
            if pruned:
                out.append({title: pruned})
    return out


def iter_paths(items):
    for item in items:
        for value in item.values():
            if isinstance(value, str):
                yield value
            else:
                for p in iter_paths(value):
                    yield p


def toml_nav(items, indent=1):
    pad = "  " * indent
    lines = []
    for item in items:
        (title, value), = item.items()
        if isinstance(value, str):
            lines.append('%s{ %s = %s },' % (pad, _tstr(title), _tstr(value)))
        else:
            lines.append('%s{ %s = [' % (pad, _tstr(title)))
            lines.append(toml_nav(value, indent + 1))
            lines.append('%s] },' % pad)
    return "\n".join(l for l in lines if l)


def _tstr(s):
    return '"' + str(s).replace("\\", "\\\\").replace('"', '\\"') + '"'


# --------------------------------------------------------------------------- #
# Landing pages
# --------------------------------------------------------------------------- #
ICON_SVG_CACHE = {}
ICON_DIR = Path("/opt/homebrew/lib/python3.11/site-packages/zensical/templates/.icons")


def icon_svg(shortcode):
    """Inline an icon SVG. `md_in_html` (needed for `:icon:` inside a card grid)
    crashes Zensical's link postprocessor, so cards are written as raw HTML."""
    if shortcode in ICON_SVG_CACHE:
        return ICON_SVG_CACHE[shortcode]
    path = ICON_DIR / (shortcode + ".svg")
    svg = ""
    if path.is_file():
        svg = re.sub(r"<\?xml[^>]*\?>", "", path.read_text(encoding="utf-8")).strip()
        svg = svg.replace("\n", " ")
    ICON_SVG_CACHE[shortcode] = svg
    return svg


def card(icon, title, href, summary):
    svg = icon_svg(icon)
    badge = '<span class="twemoji">%s</span> ' % svg if svg else ""
    return (
        '  <div class="card">\n'
        '    <p>%s<strong><a href="%s">%s</a></strong></p>\n'
        '    <p>%s</p>\n'
        '  </div>' % (badge, href, title, summary)
    )


def write_home(built):
    families = []
    for fam_key, fam_title in G.FAMILIES:
        rows = [g for g in built if g["family"] == fam_key]
        if not rows:
            continue
        cards = "\n".join(
            card(g.get("icon", "material/book-open-variant"), g["title"],
                 "%s/%s/" % (fam_key, g["key"]), g["summary"])
            for g in rows
        )
        families.append(
            '## %s\n\n<div class="grid">\n%s\n</div>' % (fam_title, cards)
        )
    # The home page's h1 repeats the site name, which the theme would render as
    # "Jaspersoft Documentation - Jaspersoft Documentation" in the browser tab;
    # an explicit title keeps that readable.
    body = """---
title: Product Documentation
hide:
  - footer
description: Product documentation for JasperReports Server, Jaspersoft Studio, JasperReports IO and Jaspersoft in the cloud.
---

# Jaspersoft Documentation

Complete product documentation for **Jaspersoft {version}**.

!!! tip "Two ways in"

    Press <kbd>/</kbd> to search everything at once, or pick a product below.
    Every guide has its own contents page listing all of its chapters.

{families}
""".format(version=G.SITE_VERSION, families="\n\n".join(families))
    (DOCS / "index.md").write_text(body, encoding="utf-8")


def write_family_page(fam_key, fam_title, rows):
    cards = "\n".join(
        card(g.get("icon", "material/book-open-variant"), g["title"],
             "%s/" % g["key"], g["summary"])
        for g in rows
    )
    body = """---
title: {title}
description: {title} documentation set.
hide:
  - footer
---

# {title}

<div class="grid">
{cards}
</div>
""".format(title=fam_title, cards=cards)
    path = DOCS / fam_key / "index.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body, encoding="utf-8")


def write_guide_page(guide, nav_items):
    """Guide landing page: what it covers, and its top-level chapters."""
    chapters = []
    for item in nav_items:
        (title, value), = item.items()
        href = value if isinstance(value, str) else _first_path(value)
        if not href:
            continue
        rel = href.split("/", 2)[2]  # strip family/key prefix
        chapters.append("- [%s](%s)" % (title, re.sub(r"\.md$", ".md", rel)))
    meta = "Applies to Jaspersoft **%s**.\n\n" % G.SITE_VERSION
    body = """---
title: {title}
description: {summary}
hide:
  - footer
---

# {title}

{summary}

{meta}## Contents

{chapters}
""".format(title=guide["title"], summary=guide["summary"], meta=meta,
           chapters="\n".join(chapters) or "_No chapters found._")
    path = DOCS / guide["family"] / guide["key"] / "index.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body, encoding="utf-8")


def _first_path(items):
    for p in iter_paths(items):
        return p
    return None


# --------------------------------------------------------------------------- #
# Driver
# --------------------------------------------------------------------------- #
def main(argv):
    only = set(argv[1:])
    REPORTS.mkdir(parents=True, exist_ok=True)

    # Logo, favicon and the logo partial are derived from tools/brand on every
    # run, so the site can never be published with them missing.
    make_brand_assets.main()

    selected = [g for g in G.GUIDES if not only or g["key"] in only
                or "%s/%s" % (g["family"], g["key"]) in only]
    if not selected:
        print("no guides matched %s" % sorted(only))
        return 1
    selected_keys = {"%s/%s" % (g["family"], g["key"]) for g in selected}

    built, nav_by_family, summary_rows = [], {}, []
    warn_by_guide = {}

    # Always plan every guide: the nav and the landing pages cover the whole
    # site, so a single-guide run must still know about the others.
    print("planning %d guides..." % len(G.GUIDES), flush=True)
    plans = []
    for guide in G.GUIDES:
        warnings = warn_by_guide.setdefault(
            "%s/%s" % (guide["family"], guide["key"]), [])
        plans.append(prepare_guide(guide, warnings.append))

    link_notes = []
    absorb_unreferenced(plans, lambda m: link_notes.append(m))
    # Prune after absorbing, so a topic pulled in by neither TOC nor link is
    # still checked, and before the resolver is built from the page maps.
    for plan in plans:
        prefix = plan["prefix"]
        prune_empty_topics([plan], warn_by_guide[prefix].append)
    resolver = LinkResolver(plans, link_notes.append)

    for plan in plans:
        guide = plan["guide"]
        prefix = plan["prefix"]
        warnings = warn_by_guide[prefix]
        guide["version"], guide["ga_date"] = plan["version"], plan["ga_date"]
        if prefix in selected_keys:
            print("==> %s" % prefix, flush=True)
            manifest = convert_guide(plan, resolver, warnings.append)
            save_manifest(prefix, manifest)
        else:
            manifest = load_manifest(prefix)
            if not manifest:
                print("--- %s (not converted yet, skipped in nav)" % prefix)
                continue
            print("--- %s (kept from previous run)" % prefix)
        nav_items = nav_for_guide(plan["toc"], manifest, prefix, warnings.append)

        write_guide_page(guide, nav_items)
        nav_by_family.setdefault(guide["family"], []).append(
            {guide["title"]: [{guide["title"]: prefix + "/index.md"}] + nav_items}
        )
        row = dict(guide, pages=len(manifest), warnings=len(warnings))
        built.append(row)
        summary_rows.append(row)

        if prefix in selected_keys:
            log = REPORTS / ("%s.log" % prefix.replace("/", "__"))
            log.write_text("\n".join(warnings) + "\n", encoding="utf-8")
            print("    %d pages, %d warnings" % (len(manifest), len(warnings)))

    for fam_key, fam_title in G.FAMILIES:
        rows = [g for g in built if g["family"] == fam_key]
        if rows:
            write_family_page(fam_key, fam_title, rows)
    write_home(built)

    # Assemble the site-wide nav.
    nav = [{"Home": "index.md"}]
    for fam_key, fam_title in G.FAMILIES:
        if fam_key in nav_by_family:
            nav.append({fam_title: [{fam_title: "%s/index.md" % fam_key}]
                        + nav_by_family[fam_key]})
    nav_toml = toml_nav(nav)
    (SITE / "nav.toml").write_text(nav_toml + "\n", encoding="utf-8")
    splice_nav(SITE / "zensical.toml", nav_toml)

    (REPORTS / "link-repairs.log").write_text(
        "\n".join(sorted(set(link_notes))) + "\n", encoding="utf-8")
    write_summary(summary_rows)
    print("\nnav -> %s (spliced into zensical.toml)" % (SITE / "nav.toml"))
    return 0


def manifest_path(prefix):
    return REPORTS / ("%s.manifest.json" % prefix.replace("/", "__"))


def save_manifest(prefix, manifest):
    manifest_path(prefix).write_text(
        json.dumps({k: list(v) for k, v in manifest.items()}, indent=1, sort_keys=True),
        encoding="utf-8")


def load_manifest(prefix):
    path = manifest_path(prefix)
    if not path.is_file():
        return {}
    return {k: tuple(v) for k, v in json.loads(path.read_text(encoding="utf-8")).items()}


BEGIN = "# BEGIN GENERATED NAV"
END = "# END GENERATED NAV"


def splice_nav(config_path: Path, nav_toml: str):
    text = config_path.read_text(encoding="utf-8")
    block = "%s\n%s\n%s" % (BEGIN, nav_toml, END)
    if BEGIN in text and END in text:
        head, rest = text.split(BEGIN, 1)
        _, tail = rest.split(END, 1)
        text = head + block + tail
    else:
        raise SystemExit("nav markers not found in %s" % config_path)
    config_path.write_text(text, encoding="utf-8")


def write_summary(rows):
    lines = [
        "# Conversion summary",
        "",
        "| Guide | Family | Source project | Pages | Warnings |",
        "| --- | --- | --- | --- | --- |",
    ]
    for r in sorted(rows, key=lambda r: (r["family"], r["title"])):
        lines.append("| %s | %s | `%s` | %d | %d |" % (
            r["title"], r["family"], r["project"], r["pages"], r["warnings"]))
    lines += [
        "",
        "Totals: **%d guides**, **%d pages**, **%d warnings**." % (
            len(rows), sum(r["pages"] for r in rows), sum(r["warnings"] for r in rows)),
        "",
        "## Projects deliberately not published",
        "",
    ]
    for proj, why in sorted(G.EXCLUDED.items()):
        lines.append("- `%s` — %s" % (proj, why))
    (REPORTS / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
