---
title: Planning Your Upgrade
description: "Some of the new and enhanced features in JasperReports Server can affect your deployment, and you should plan your upgrade accordingly. Before upgrading make sure to:"
---

# Planning Your Upgrade

Some of the new and enhanced features in JasperReports Server can affect your deployment, and you should plan your upgrade accordingly. Before upgrading make sure to:

- Review this information carefully and determine how the changes described affect your deployment.

- Back up your current JasperReports Server installation, repository, and keystore.

- Run the upgrade script as the same user who originally installed the server, or make sure the server's keystore is available in the home directory of the user running the upgrade script.

The versions and their affected functionality are:

- Changes in 10.0 affect upgrades.

- Changes in 9.0 affect upgrades

- Changes in 8.2 affect upgrades.

- Changes in 8.1 affect upgrades. Users will not be able to upgrade from 8.0 Compact to 8.1 Split, or from 8.0 Split to 8.1 Compact. Currently, the **js-upgrade-newdb.sh/bat** script does not import the access, audit, monitoring data when upgrading.

- Changes in 8.0 affect the installation and upgrades. The Split installation has been introduced from this release. The Audit, Access, and Monitoring events can be moved to a different audit database using the Split installation or upgrade, which improves the performance of JasperReports server.

- Changes in 7.8 affect PhantomJS/Rhino JavaScript engine. With this release, the supported JavaScript engine is Chrome/Chromium.

- Changes in 7.5 affect Simba and Impala drivers, the MongoDB query language, custom themes, and encryption keys.

- Changes in 7.2 affect legacy dashboards, customizations to the login page, external authentication, and customizations to the Spring Security framework.

- Changes in 7.1 affect customizations to the login page.

- Changes in 6.4 affect the Impala community connector.

  Changes in 6.2.1 affect the Impala community connector.

  Changes in 6.2 affect the default Ad Hoc templates.

- Changes in 6.1 affect themes.

Changes are cumulative, so review all topics that affect you. For example, if you are upgrading from 6.1 to 7.1, you may be affected by changes in 6.1, 6.2, 6.2.1, and 6.4.

For versions of the software earlier than 6.1, see earlier versions of the JasperReports Server Upgrade Guide.

This section describes only those changes that can significantly impact your existing deployment. For an overview of new features, improvements, and bug fixes see the release notes in the root directory of the distribution. For information on how to use the new features, see the JasperReports Server User Guide or the JasperReports Server Administrator Guide.

## Generic Changes That May Affect Your Upgrade

### UI Customizations Note

If you have done any customizations for your UI (JavaScript and CSS files), you have to first perform the JasperReports Server upgrade, then get the JasperReports Server Source Packages, apply the customizations in the UI source files, rebuild them and publish into the upgraded JasperReports Server.

### Newdb Upgrade Note

Starting version 7.9.0, the **js-upgrade-newdb.sh/bat** script does not import the access, audit, monitoring data when upgrading.

However, once the upgrade process has completed, you can use the **JRS UI - Import** page to reimport the JasperReports Server export file that was passed in with the `newdb` script and select the checkboxes for including access, audit, and monitoring data. Once this import is completed, then the access, audit, monitoring data exist in the new database/release.

This chapter contains the following sections:

- [Changes in 10.0 That May Affect Your Upgrade](plan-upgrade-10.0.md)

- [Changes in 9.0 That May Affect Your Upgrade](plan-upgrade-9.0.md)

- [Changes in 8.2 That May Affect Your Upgrade](plan-upgrade-8.2.md)

- [Changes in 8.1 That May Affect Your Upgrade](plan-upgrade-8.1.md)

- [Changes in 8.0 That May Affect Your Upgrade](plan-upgrade-8.0.md)

- [Changes in 7.8 That May Affect Your Upgrade](plan-upgrade-7.8.md)

- [Changes in 7.5 That May Affect Your Upgrade](plan-upgrade-7.5.md)

- [Changes in 7.2 That May Affect Your Upgrade](plan-upgrade-72.md)

- [Changes in 7.1 That May Affect Your Upgrade](plan-upgrade-7-1.md)

- [Changes in 6.4 That May Affect Your Upgrade](plan-upgrade-7-1.md)

  [Changes in 6.2.1 That May Affect Your Upgrade](plan-upgrade-621.md)

- [Changes in 6.1 That May Affect Your Upgrade](plan-upgrade-61-landscape.md)
