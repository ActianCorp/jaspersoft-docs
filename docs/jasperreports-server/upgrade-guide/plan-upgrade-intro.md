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

- Changes in 10.1.0 affect upgrades.

- Changes in 10.0 affect upgrades.

- Changes in 9.0 affect upgrades

!!! note

    For details on upgrading from version 8.x or older, see the respective Upgrade Guides for those versions.

This section describes only those changes that can significantly impact your existing deployment. For an overview of new features, improvements, and bug fixes see the release notes in the root directory of the distribution. For information on how to use the new features, see the JasperReports Server User Guide or the JasperReports Server Administrator Guide.

## Generic Changes That May Affect Your Upgrade

### UI Customizations Note

If you have done any customizations for your UI (JavaScript and CSS files), you have to first perform the JasperReports Server upgrade, then get the JasperReports Server Source Packages, apply the customizations in the UI source files, rebuild them and publish into the upgraded JasperReports Server.

### Newdb Upgrade Note

Starting version 7.9.0, the **js-upgrade-newdb.sh/bat** script does not import the access, audit, monitoring data when upgrading.

However, once the upgrade process has completed, you can use the **JRS UI - Import** page to reimport the JasperReports Server export file that was passed in with the `newdb` script and select the checkboxes for including access, audit, and monitoring data. Once this import is completed, then the access, audit, monitoring data exist in the new database/release.

This chapter contains the following sections:

- [Changes in 10.1 That May Affect Your Upgrade](plan-upgrade-10.1.md)

- [Changes in 10.0 That May Affect Your Upgrade](plan-upgrade-10.0.md)

- [Changes in 9.0 That May Affect Your Upgrade](plan-upgrade-9.0.md)
