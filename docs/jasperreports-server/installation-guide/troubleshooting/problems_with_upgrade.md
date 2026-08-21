---
title: Problems with Upgrade
description: "If you have auditing enabled and you run upgrade using js-upgrade-newdb.bat/sh, audit events are not imported by default. To import audit events, you need to run an additional command after the..."
---

# Problems with Upgrade

## Include Audit Events on Upgrade

If you have auditing enabled and you run upgrade using `js-upgrade-newdb.bat/sh`, audit events are not imported by default. To import audit events, you need to run an additional command after the `js-upgrade-newdb` script completes. To do this, change to the buildomatic directory:

`cd <js-install>/buildomatic`

Then run one of the following commands:

`js-import.bat --input-zip=js-my-export-all.zip --include-audit-events` (Windows)

`js-import.sh --input-zip=js-my-export-all.zip --include-audit-events` (Linux)

or

`ant import -DimportFile=js-my-export-all.zip -DimportArgs="--include-audit-events"`

These commands re-import all resources from the specified export file, add the audit event, and do not overwrite existing resources.

!!! warning

    When using either import utility, the server must be stopped to avoid issues with caches, configuration, and security.

## Overlay Upgrade Permissions Error with Bundled Installation

If you are using the overlay upgrade procedure with a PostgreSQL database, and you installed an earlier version of JasperReports Server, you might see an HTTP Status 404 error.

The overlay installer is not supported with the bundled installation and may only be used with a war file installation of JRS.

## Overlay Upgrade Domain Issue with MySQL and MariaDB JDBC Driver

When working with Domains using the MySQL database and using the 1.1.2 version of the MariaDB JDBC driver (`mariadb-java-client-1.1.2.jar`) there can be an issue handling Boolean values correctly. The fix is to upgrade to a higher version of the MariaDB JDBC driver. For supported versions of the driver, see the Jaspersoft Platform Support Guide.

Because the Overlay packages for some previous JasperReports Server versions were distributed with the MariaDB 1.1.2 JDBC driver, this error can also occur even without an upgrade operation.

The issue may occur when a Boolean filter is created on a domain. Because of a bug in older versions of the MariaDB driver, the Boolean filter is evaluated as a numeric filter.

<https://mariadb.atlassian.net/browse/CONJ-72>
