# flare2md — Flare sources to the Zensical documentation portal

Converts the MadCap Flare projects in this repository into the Markdown site
under `zensical-site/`, and regenerates that site's navigation.

```bash
python3 tools/flare2md/build.py                       # every guide (~1 min)
python3 tools/flare2md/audit.py                       # prove nothing was missed
python3 tools/flare2md/compare.py                     # diff every page against its source
python3 tools/flare2md/build.py user-guide            # one guide, by key
python3 tools/flare2md/build.py cloud/azure-user-guide  # or family/key

cd zensical-site && zensical build                    # render the site
cd zensical-site && zensical serve                    # preview at :8000

python3 tools/flare2md/check_site.py                  # validate the output
```

Requirements: Python 3.9+ with `lxml`, `pandoc` on `PATH`, and `zensical`.

## Files

| File | Role |
| --- | --- |
| `guides.py` | The guide inventory: which project, TOC and build target make up each published guide, plus the projects deliberately excluded and why. Edit this to add or drop a guide. |
| `flare2md.py` | The conversion engine — one function per Flare idiom, no site knowledge. |
| `build.py` | Orchestration: plan every guide, convert, resolve links across guides, write landing pages, splice the `nav` block into `zensical.toml`. |
| `make_brand_assets.py` | Derives the header logo partial and the favicon from `docs/assets/images/actian-logo-white.svg`. Re-run after replacing that file. |
| `check_site.py` | Post-build validation: every internal link and asset in `zensical-site/site`. |
| `audit.py` | Coverage audit: classifies every source topic in every project and writes `_reports/coverage.md`. |
| `compare.py` | Page-by-page diff against the Flare source: text present in the source but missing from the published page, images, headings, and list items that stopped being list items. Writes `_reports/compare.md`. |
| `convert.py`, `gen_nav.py` | Superseded single-guide scripts from the first pilot pass. Kept for reference; `build.py` replaces both. |

## One version only

`guides.py` sets `SITE_VERSION`, and `build.py` pins every version variable
(`productvar.productVersion`, `JasperPackageNumber`, `BookSoftwareVersion`) to
it before conversion, whatever the project or target carries. The version is
stated on the home page, on every guide landing page, and in the announcement
bar (`overrides/main.html`).

Release numbers written into prose ("as of release X") cannot be pinned that
way; `audit.py` lists every one of them in `coverage.md` for an editorial
decision.

## Branding

Actian acquired the Jaspersoft business, so `BRAND_REPLACEMENTS` in
`guides.py` renames the owning company in page text during conversion, and
`globalvar.company` is overridden to match. Site chrome (copyright, author,
logo, favicon) is set in `zensical.toml` and `overrides/partials/logo.html`.

Three things are deliberately **not** rewritten, and `audit.py` lists every
occurrence in `coverage.md`:

* `TIBCO` where it is part of a product name or prose (313 occurrences),
* links to the previous owner's sites (`cloud.com`, `tibco.com`) — rewriting a
  URL breaks it,
* the exact legal entity name and copyright year range, which the legal owner
  should confirm.

The logo is derived, not redrawn: `make_brand_assets.py` reads the supplied
white-on-dark SVG and emits a header version whose wordmark uses
`currentColor` (legible on both the light and dark header) plus a favicon
using the mark alone, with the darkest stop of the mark's own gradient where
white would vanish on a light browser tab.

## How a guide is resolved

A Flare guide is not a directory; it is a **build target** plus a **TOC**.
The target matters because Flare resolves per-target:

* **variables** — `productvar.productVersion`, product names and support URLs
  are multi-valued in the `.flvar` files and only a target says which value
  applies, and
* **conditions** — `include[...]`/`exclude[...]` decide commercial vs community
  content, print vs screen, and which guide a shared topic belongs to.

Five guides (Security, Domains, both OLAP guides, Ultimate) live in a project
with no per-guide HTML target. For those, `guides.py` names the guide's
`JasperGuideConditions-forHTML` token and `synthetic_target()` reconstructs the
same expression the real targets use: publish the commercial screen variant of
this guide, exclude every sibling guide's marker.

**Topic selection** is the TOC *plus the link closure of those topics*, so a
page reachable only through a cross-reference is still published and its link
still resolves. Book-only artifacts (printed title page, generated TOC and
index) are listed in `SKIP_TOPICS` and dropped.

## What the converter rewrites

| Flare | Markdown / Material |
| --- | --- |
| `MadCap:snippetBlock`/`snippetText` | inlined recursively (falls back to the shared project's snippet library) |
| `MadCap:variable`, `[%=set.var%]` | resolved from the target, then the variable sets; placeholder definitions are skipped |
| `MadCap:conditions` | dropped when the target excludes them |
| `div.note`, `p.Note`, autonum `Note:`/`Warning:`/`Caution:`/`Important:`/`Tip:`/`Restriction:`/`Before you begin` | `!!! note` / `!!! warning` / `!!! info` / `!!! tip` admonitions, with the body converted as markdown |
| note tables (`TableStyle-Note`, or any icon-cell + text-cell table) | the same admonitions |
| `p.Bullet`, `Bullet_2`, `Bullet_3`, `Cell_Bullet` + autonum `•` | real `<ul>` lists, nested by class depth |
| `p.Numbered`, `Numbered_First`, `Numbered_alpha`, `Step` + autonum `1.` | real `<ol>` lists, restarting where Flare restarts |
| paragraphs that start with a typed-in `•` | list items |
| `ol MadCap:continue` | `<ol start="n">` so numbering continues |
| `span.Code`, `span.UI`/`.uicontrol` | `` `code` ``, `**bold**` |
| `pre` | fenced code block with a guessed language |
| `table.TableStyle-Figure` | plain image plus italic caption |
| `MadCap:xref`, `.htm` links | relative links to the converted `.md`, across guides where needed |
| autonum `Figure N:` / `Table N:` | italic caption line under the image |
| `DateTime` variables (`CopyrightYear` = "yyyy") | evaluated for the build date, as Flare does |
| heading levels | shifted so every page starts at a single `h1` |

Links and images whose relative path is wrong in the source (a real defect in
several projects) are repaired by a unique filename match within the same
project; every repair is logged.

## Site chrome

`zensical-site/overrides/main.html` holds the two theme overrides:

* the announcement bar stating the documented version, and
* previous/next page links rendered **at the end of the article**, inside the
  content column, instead of full-width in the site footer. The theme's
  `navigation.footer` feature is off for that reason, and landing pages set
  `hide: [footer]` so they carry no page-to-page links at all.

## Reports

`zensical-site/_reports/` after a run:

* `summary.md` — pages and warnings per guide, plus the excluded projects
* `<family>__<guide>.log` — that guide's warnings
* `<family>__<guide>.manifest.json` — topic → page map, reused so a
  single-guide run can still write the full site navigation
* `link-repairs.log` — every link repaired by filename, and every topic
  absorbed because no TOC referenced it
* `coverage.md` (from `audit.py`) — every source topic accounted for, orphans,
  unused TOCs, excluded projects, and hard-coded version numbers in prose

## Editorial work that is out of scope

The converter never invents content. These are reported, not fixed:

* legacy TIBCO branding in prose where the source still carries it,
* `Figure N:` numbering, which Flare generated per printed book,
* topics whose source content is stale (some upgrade paths, older screenshots).
