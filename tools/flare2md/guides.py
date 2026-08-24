#!/usr/bin/env python3
"""Guide manifest for the Flare -> Markdown -> Zensical documentation portal.

Every entry describes one published guide: which Flare project holds it, which
TOC defines its structure, and which build target supplies the variable values
and condition filters. Legacy/superseded projects are listed at the bottom with
the reason they are excluded, so the omission is deliberate and auditable.

`target` is preferred over `conditions`/`variables` guesswork: Flare resolves
multi-valued variables and include/exclude condition sets *per target*, so the
target is the only place the correct product name, version and audience
(commercial vs community) are recorded.

Guides whose project has no dedicated HTML target set `guide_condition` instead:
the converter then synthesizes the equivalent condition expression (include this
guide's own JasperGuideConditions token, exclude every sibling guide's token).
"""
from __future__ import annotations

# The single product version published by this site. Only the latest release is
# migrated, so this value overrides the per-project/per-target `productVersion`
# variable, which still names the previous release in several Flare projects.
SITE_VERSION = "10.1.0"

# Actian acquired the Jaspersoft business. The Flare sources still name the
# previous owner, so these entity names are replaced during conversion. Only
# the company name is touched: product names that carry the old "TIBCO" prefix,
# and third-party URLs, are left for an editorial/legal decision and are listed
# in _reports/branding.md.
BRAND_REPLACEMENTS = {
    "Cloud Software Group, Inc.": "Actian",
    "Cloud Software Group": "Actian",
    "Cloud SG": "Actian",
}

# Product families, in the order they should appear in the site navigation.
# The published portal groups the OLAP guides under JasperReports Server rather
# than giving them a family of their own; this mirrors that.
FAMILIES = [
    ("jasperreports-server", "JasperReports Server"),
    ("jaspersoft-studio", "Jaspersoft Studio"),
    ("jasperreports-web-studio", "JasperReports Web Studio"),
    ("jasperreports-io", "JasperReports IO"),
    ("cloud", "Jaspersoft in the Cloud"),
]

# --------------------------------------------------------------------------- #
# key            : output directory name inside the family directory
# title          : nav/landing-page title
# family         : key from FAMILIES
# project        : Flare project directory (repo-relative)
# toc            : .fltoc, relative to <project>/Project/TOCs/
# target         : .fltar, relative to <project>/Project/Targets/ (optional)
# guide_condition: JasperGuideConditions-forHTML token (when target is absent)
# summary        : one-line description for the landing-page cards
# icon           : Material icon shortcode for the landing-page cards
# --------------------------------------------------------------------------- #
GUIDES = [
    # ----------------------------- JasperReports Server ---------------------
    dict(
        key="user-guide",
        title="User Guide",
        family="jasperreports-server",
        project="jrs-user",
        toc="JasperReports-Server-User-Guide.fltoc",
        target="JasperReports-Server-User-Guide-HTML5.fltar",
        summary="Create, run, schedule and share reports, dashboards and Ad Hoc views as an end user.",
        icon="material/account",
    ),
    dict(
        key="administrator-guide",
        title="Administrator Guide",
        family="jasperreports-server",
        project="jrs-admin",
        toc="JasperReports-Server-Admin-Guide.fltoc",
        target="HTML5-JasperReports-Server-Admin-Guide.fltar",
        summary="Administer organizations, users, roles, data sources, settings and server maintenance.",
        icon="material/shield-account",
    ),
    dict(
        key="installation-guide",
        title="Installation Guide",
        family="jasperreports-server",
        project="jrs-install-family",
        toc="JRS-Install-Guide.fltoc",
        target="JasperReports-Server-Install-Guide-HTML5.fltar",
        summary="Install JasperReports Server with the installer or a WAR file distribution.",
        icon="material/download",
    ),
    dict(
        key="upgrade-guide",
        title="Upgrade Guide",
        family="jasperreports-server",
        project="jrs-install-family",
        toc="JRS-Upgrade-Guide.fltoc",
        target="JasperReports-Server-Upgrade-Guide-HTML5.fltar",
        summary="Plan and perform an upgrade from an earlier release, including repository migration.",
        icon="material/arrow-up-circle",
    ),
    dict(
        key="source-build-guide",
        title="Source Build Guide",
        family="jasperreports-server",
        project="jrs-install-family",
        toc="JRS-Source-Build-Guide.fltoc",
        target="JasperReports-Server-Source-Build-Guide-HTML5.fltar",
        summary="Build JasperReports Server from source, including the build environment and targets.",
        icon="material/hammer-wrench",
    ),
    dict(
        key="security-guide",
        title="Security Guide",
        family="jasperreports-server",
        project="js-jrs-JasperReportsServer",
        toc="jrs-security/JasperReports-Server-Security-Guide.fltoc",
        guide_condition="jrs-security",
        summary="Harden a deployment: encryption, authentication, session security and known concerns.",
        icon="material/lock",
    ),
    dict(
        key="authentication-cookbook",
        title="Authentication Cookbook",
        family="jasperreports-server",
        project="jrs-auth",
        toc="JasperReportsServer-Auth-Cookbook.fltoc",
        target="JasperReports-Server-Auth-Cookbook-HTML5.fltar",
        summary="Recipes for external authentication: LDAP, CAS, SAML, OAuth and custom providers.",
        icon="material/key-chain",
    ),
    dict(
        key="data-management-using-domains",
        title="Data Management Using Domains",
        family="jasperreports-server",
        project="js-jrs-JasperReportsServer",
        toc="jrs-domains/jrs-domain.fltoc",
        guide_condition="jrs-domains",
        summary="Design and maintain Domains, the semantic layer behind Ad Hoc views and Topics.",
        icon="material/database-cog",
    ),
    dict(
        key="web-services-guide",
        title="Web Services Guide",
        family="jasperreports-server",
        project="jrs-web",
        toc="JasperReports-Server-Web-Services-Guide.fltoc",
        target="HTML5.fltar",
        summary="Integrate using the SOAP and REST web services, including repository and report services.",
        icon="material/api",
    ),
    dict(
        key="rest-api-reference",
        title="REST API Reference",
        family="jasperreports-server",
        project="jrs-programming",
        toc="JasperReports-Server-REST-API-Reference.fltoc",
        target="JasperReports-Server-REST-API-Reference-HTML5.fltar",
        summary="Endpoint-by-endpoint reference for the JasperReports Server REST API.",
        icon="material/code-json",
    ),
    dict(
        key="visualize-js-guide",
        title="Visualize.js Guide",
        family="jasperreports-server",
        project="jrs-programming",
        toc="JasperReports-Server-Visualize.js-Guide.fltoc",
        target="JasperReports-Server-Visualize.js-Guide-HTML5.fltar",
        summary="Embed reports, dashboards and Ad Hoc views in web applications with Visualize.js.",
        icon="material/language-javascript",
    ),
    dict(
        key="mobile-guide",
        title="Mobile Guide",
        family="jasperreports-server",
        project="jrs-mobile",
        toc="JasperReports-Server-Mobile-Guide.fltoc",
        target="HTML5.fltar",
        summary="Use and configure the Jaspersoft Mobile applications against JasperReports Server.",
        icon="material/cellphone",
    ),
    dict(
        key="ultimate-guide",
        title="Ultimate Guide",
        family="jasperreports-server",
        project="js-jrs-JasperReportsServer",
        toc="jrs-ultimate/JS Ultimate Guide.fltoc",
        guide_condition="jrs-ultimate",
        summary="Deep-dive reference covering the server architecture, repository internals and APIs.",
        icon="material/book-open-page-variant",
    ),
    dict(
        key="release-notes",
        title="Release Notes",
        family="jasperreports-server",
        project="JRS-release-notes",
        toc="jrs-release-notes-master.fltoc",
        target="relnotes-HTML5.fltar",
        summary="New features, resolved issues, known issues and end-of-support notices per release.",
        icon="material/note-text",
    ),
    # One guide, as the portal publishes it. The Flare project splits platform
    # support across a commercial and a community TOC; the portal ships the
    # commercial one, and the community-only variants of the matrices are picked
    # up as additional topics rather than being dropped.
    dict(
        key="platform-support-guide",
        title="Platform Support Guide",
        family="jasperreports-server",
        project="js-jrs-JasperReportsServer",
        toc="Jaspersoft-platform-support-commercial-edition.fltoc",
        guide_condition="jrs-platform-support-commercial",
        summary="Certified operating systems, application servers, databases and browsers.",
        icon="material/check-decagram",
    ),
    dict(
        key="telemetry-program",
        title="Telemetry Data Collection Program",
        family="jasperreports-server",
        project="jss-user",
        toc="jrs-telemetry-program.fltoc",
        target="jrs-telemetry-program-html.fltar",
        summary="What the telemetry program collects, how it is transmitted, and how to opt out.",
        icon="material/chart-timeline-variant",
    ),
    # Jaspersoft OLAP — filed under JasperReports Server, as the portal does.
    dict(
        key="olap-user-guide",
        title="Jaspersoft OLAP User Guide",
        family="jasperreports-server",
        project="js-jrs-JasperReportsServer",
        toc="jrs-olap-user/Jaspersoft-OLAP-User-Guide.fltoc",
        guide_condition="jrs-olap-user",
        summary="Browse and analyze OLAP data: views, crosstabs, drill-through and MDX queries.",
        icon="material/cube-outline",
    ),
    dict(
        key="olap-ultimate-guide",
        title="Jaspersoft OLAP Ultimate Guide",
        family="jasperreports-server",
        project="js-jrs-JasperReportsServer",
        toc="jrs-olap-ultimate/Jaspersoft-OLAP-Ultimate-Guide.fltoc",
        guide_condition="jrs-olap-ultimate",
        summary="Design and tune OLAP schemas, connections and Mondrian performance.",
        icon="material/cube-scan",
    ),
    # ----------------------------- Jaspersoft Studio ------------------------
    dict(
        key="user-guide",
        title="Jaspersoft Studio User Guide",
        family="jaspersoft-studio",
        project="jss-user",
        toc="jss-user.fltoc",
        target="Jaspersoft-Studio-User-Guide-HTML5.fltar",
        summary="Design reports in the Eclipse-based studio: datasets, bands, charts and publishing.",
        icon="material/pencil-ruler",
    ),
    dict(
        key="source-build-guide",
        title="Jaspersoft Studio Source Build Guide",
        family="jaspersoft-studio",
        project="Standalone/jss-source-guide",
        toc="svn-source.fltoc",
        target="Jaspersoft-Studio-Source-Build-Guide-HTML5.fltar",
        summary="Check out and build Jaspersoft Studio from source.",
        icon="material/source-branch",
    ),
    # ----------------------- JasperReports Web Studio -----------------------
    dict(
        key="user-guide",
        title="JasperReports Web Studio User Guide",
        family="jasperreports-web-studio",
        project="jss-web-jrws",
        toc="User Guide.fltoc",
        target="relnotes-JRWS-UG-HTML5.fltar",
        summary="Design and edit JRXML reports in the browser-based Web Studio.",
        icon="material/web",
    ),
    # ----------------------------- JasperReports IO -------------------------
    dict(
        key="professional-user-guide",
        title="JasperReports IO Professional User Guide",
        family="jasperreports-io",
        project="jrs-programming",
        toc="JasperReports-IO-Pro-User-Guide.fltoc",
        target="JasperReports-IO-Pro-User-Guide-HTML5.fltar",
        summary="Render and embed reports with the JasperReports IO REST and JavaScript APIs.",
        icon="material/server-network",
    ),
    dict(
        key="at-scale-user-guide",
        title="JasperReports IO At Scale User Guide",
        family="jasperreports-io",
        project="jrio-atscale",
        toc="JasperReports-IO-At-Scale-User-Guide.fltoc",
        target="JasperReports-IO-At-Scale-User-Guide-HTML5.fltar",
        summary="Run JasperReports IO in a scaled-out Kubernetes deployment.",
        icon="material/kubernetes",
    ),
    dict(
        key="professional-release-notes",
        title="JasperReports IO Professional Release Notes",
        family="jasperreports-io",
        project="jrs-programming",
        toc="JasperReports-IO-Professional-Edition-Release-Notes.fltoc",
        target="JasperReports-IO-Professional-Edition-ReleaseNotes.fltar",
        summary="Release-by-release changes for JasperReports IO Professional Edition.",
        icon="material/note-text-outline",
    ),
    # --------------------------------- Cloud --------------------------------
    dict(
        key="aws-user-guide",
        title="Jaspersoft for AWS User Guide",
        family="cloud",
        project="js-aws",
        toc="AWS.fltoc",
        target="Jaspersoft-for-AWS-User-Guide-HTML5.fltar",
        summary="Deploy, configure and operate Jaspersoft on Amazon Web Services.",
        icon="material/aws",
    ),
    dict(
        key="aws-getting-started",
        title="Getting Started with Jaspersoft for AWS",
        family="cloud",
        project="js-aws-gettingstarted",
        toc="GettingStartedWithJaspersoft-for-AWS.fltoc",
        target="HTML5.fltar",
        summary="Launch a first Jaspersoft instance on AWS and load sample data.",
        icon="material/rocket-launch",
    ),
    dict(
        key="aws-release-notes",
        title="Jaspersoft for AWS Release Notes",
        family="cloud",
        project="JRS-release-notes",
        toc="relnotes-AWS.fltoc",
        target="relnotes-AWS-HTML.fltar",
        summary="Changes specific to the AWS Marketplace distributions.",
        icon="material/note-text-outline",
    ),
    dict(
        key="azure-user-guide",
        title="Jaspersoft for Azure User Guide",
        family="cloud",
        project="js-azure",
        toc="jrs-azure-user guide.fltoc",
        target="Jaspersoft-Azure-User-Guide-HTML5.fltar",
        summary="Deploy, configure and operate Jaspersoft on Microsoft Azure.",
        icon="material/microsoft-azure",
    ),
]

# Projects deliberately not published, and why. Kept here so a future run can
# tell "not converted" from "forgotten".
EXCLUDED = {
    "jrs-install": "superseded by jrs-install-family (older 8.x content set)",
    "jrs-upgrade": "superseded by jrs-install-family (missing 9.x/10.x upgrade paths)",
    "jrs-build": "superseded by jrs-install-family/JRS-Source-Build-Guide",
    "jrio-user": "stale duplicate; its TOC is missing and content lives in jrs-programming",
    "jrs-rest": "no content topics, only BookMatter/Resources",
    "jrs-help-master": "context-sensitive help shell; links into the other projects",
    "js-shared": "shared snippets/variables only, no standalone guide",
    "Standalone/spring_upgrade_601": "one-off historical hotfix doc (Spring upgrade 6.0.1)",
    "Standalone/dashboard-parameters-2015-02": "one-off historical hotfix doc (2015)",
    "ServicePacks": "archived per-version release-note snapshots (7.1.x-9.0.x)",
    "Templates": "Flare project templates, not product documentation",
}


def guide_out_dir(guide):
    """docs/-relative output directory for a guide."""
    return "{}/{}".format(guide["family"], guide["key"])
