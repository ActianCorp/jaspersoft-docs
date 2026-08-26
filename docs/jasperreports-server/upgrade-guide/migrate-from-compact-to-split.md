---
title: Migrating from Compact 10.1 to Split 10.1
description: This chapter describes the recommended procedure for upgrading to JasperReports Server 10.1 Split installation from JasperReports Server 10.1 Compact installation.
---

# Migrating from Compact 10.1 to Split 10.1

This chapter describes the recommended procedure for upgrading to JasperReports Server 10.1 Split installation from JasperReports Server 10.1 Compact installation.

This chapter contains the following sections:

-   Migrating From Compact to Split (samedb)

-   Migrating From Compact to Split (newdb)

## Migrating From Compact to Split (samedb)

To migrate from Compact installation to Split installation (samedb):

1.  Configure the settings in the `default_master.properties` file as described in [Additional Buildomatic Configuration for Split Installation Upgrade](jrs-install-guide/introduction/installation_types.md).

2.  Run the following command to migrate from Compact to Split:

    -   Windows: `js-migrate-to-split-samedb.bat`
    -   Linux and Mac OSX: `./js-migrate-to-split-samedb.sh`

    The `audit` database is created with empty tables.

3.  Run the following command to transfer the data (Audit, Access, and Log monitoring data) to the `audit` database from the `jasperserver` database:

    -   Windows: `transfer-audit-data.bat`
    -   Linux and Mac OSX: `./transfer-audit-data.sh`

    The data is transferred to the `audit` database and the tables are deleted from the `jasperserver` database. Rerun the command if there is any interruption in the data transfer process, it will resume the transfer process from where it was interrupted in the previous run.

## Migrating From Compact to Split (newdb)

Prerequisite: Export all the data as described in [Exporting Current Repository Data](upgrading.md).

To migrate from Compact installation to Split installation (newdb):

1.  Configure the settings in the `default_master.properties` file as described in [Additional Buildomatic Configuration for Split Installation Upgrade](jrs-install-guide/introduction/installation_types.md).

2.  Run the following command to migrate from Compact to Split and import the resources:

    -   Windows:

        -   `js-migrate-to-split-newdb.bat js-<ver>-export.zip` (Migrate without the Audit, Access, and Log Monitoring data)
        -   `js-migrate-to-split-newdb.bat js-<ver>-export.zip include-access-events include-audit-events include-monitoring-events` (Migrate with the Audit, Access, and Log Monitoring data)

    -   Linux and Mac OSX:

        -   `./js-migrate-to-split-newdb.sh js-<ver>-export.zip` (Migrate without the Audit, Access, and Log Monitoring data)
        -   `./js-migrate-to-split-newdb.sh js-<ver>-export.zip include-access-events include-audit-events include-monitoring-events` (Migrate with the Audit, Access, and Log Monitoring data)

The `jasperserver` database and `audit` database are created and the resources are imported from the zip file provided as the input.
