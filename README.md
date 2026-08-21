# Jaspersoft Documentation

The Jaspersoft product documentation portal: **28 guides, 1,554 pages**, covering
JasperReports Server, Jaspersoft OLAP, Jaspersoft Studio, JasperReports Web
Studio, JasperReports IO and the AWS/Azure editions.

Published to GitHub Pages on every push to `main`:
**https://actiancorp.github.io/jaspersoft-docs/**

Documents Jaspersoft **10.1.0**. Only the current release is published.

## Layout

| Path | Contents |
| --- | --- |
| `docs/` | The site: converted Markdown, one directory per product family, with page assets alongside. |
| `zensical.toml` | Site configuration — theme, navigation, markdown extensions, analytics. The `nav` block between the `BEGIN/END GENERATED NAV` markers is generated; edit `tools/flare2md/guides.py` instead. |
| `nav.toml` | The generated navigation, kept as a separate file for review. |
| `overrides/` | Two theme partials with local additions (`header.html` — version selector, `nav.html` — home-page product list) and `main.html` (announcement bar, in-content previous/next). Each carries a note to re-diff after a Zensical upgrade. |
| `tools/flare2md/` | The MadCap Flare → Markdown conversion pipeline. See its [README](tools/flare2md/README.md). |
| `tools/brand/` | The Actian brand asset the logo and favicon are derived from. |
| `.github/workflows/deploy.yml` | Build and deploy to Pages. |

## Working on the site

```bash
pip install -r requirements.txt

zensical serve      # preview at http://localhost:8000
zensical build      # render to site/ (git-ignored)

python3 tools/flare2md/check_site.py   # validate every internal link and asset
```

Editing a page under `docs/` is enough for a content fix — commit and push, and
the workflow republishes.

## Regenerating from the Flare sources

The pages here are converted from the MadCap Flare projects, which live in the
separate **jaspersoft-userdocs** repository and are deliberately not duplicated
here. To regenerate, run the pipeline in that repository (where
`tools/flare2md/build.py` can see the `.flprj` projects) and copy the refreshed
`docs/`, `nav.toml` and `zensical.toml` across.

`tools/` is included for provenance — it records exactly how each page was
produced — but `build.py`, `audit.py` and `compare.py` need the Flare sources
and will not run in this repository.

## Known follow-ups

* `TIBCO` appears in product names and prose in 72 pages, and 68 pages link to
  `cloud.com` / `tibco.com`. These were left alone during the Actian rename
  because each needs an editorial or legal decision, not a substitution.
* A handful of source pages state a release number in prose ("as of release
  10.0.0"); the version *variable* is pinned to 10.1.0 everywhere.
* Three cross-references point at topics that do not exist in the Flare
  sources and are rendered as plain text rather than broken links.
