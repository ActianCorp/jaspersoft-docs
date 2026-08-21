---
title: WAR File Distribution
description: The WAR file distribution comes in a file named
---

# WAR File Distribution

The WAR file distribution comes in a file named

`js-jrs``_10.1.0`

\_bin.zip in compressed ZIP format.

The WAR file distribution includes `js-install` shell scripts (for Linux and Windows) that automate much of the installation using a single properties file. These scripts are:

- `js-install`` ``.bat`
- `js-install`` ``.sh`

The main contents of the WAR file binary distribution are shown in the following table:

| Content Item | Description |
|----|----|
| JasperReports Server js-install Scripts | Found at `<js-install>/buildomatic/``js-install`` .bat` and `js-install` .sh. |
| JasperReports Server Database Scripts | SQL scripts for each supported database. |
| JasperReports Server Documentation | Guides for end users and administrators. |
| JasperReports Server Extra Samples | Web Service example applications, sample reports, custom data source examples, and other sample files. |
| JasperReports Server Standard Sample Data | Sample data that highlights JasperReports Server features. |
| JasperReports Server WAR file archive | All JasperReports Server class files and dependent jars. |
| JasperReports IO for JasperReports Web Studio | JasperReports IO application is required for JasperReports Web Studio preview. |
| Repository for JasperReports Web Studio | Repository connector application is required for JasperReports Web Studio integration with JasperReports Server. |

The application server should reside on the local machine, but the target database can be on a remote server. Using a remote PostgreSQL database on some Linux platforms requires a change to its configuration file, as described in [Enabling Connections to a Remote Host](../binary-installer/select-postgresql.md).

### About Bundled Apache Ant

The War File Distribution ZIP includes Apache Ant version 1.10.*latest* version. The buildomatic Ant scripts come with Windows and Linux batch scripts pre-configured to use the bundled version of Apache Ant. You call the buildomatic Ant scripts from the command line in the following manner:

|                    |                          |
|--------------------|--------------------------|
| Windows:           | `js-ant <target-name>`   |
| Linux and Mac OSX: | `./js-ant <target-name>` |

If you want to run your own version of Ant, version 1.10.*latest*.

The bundled Apache Ant has an additional jar (ant-contrib.jar) that enables conditional logic in Ant. If you're running your own Ant, copy this jar to your Ant/lib folder.

!!! note

    On Linux and Solaris, the js-ant commands may not be compatible with all shells. If you have errors, use the `bash` shell explicitly. For more information, see [Bash Shell for Solaris, IBM AIX, HP UX and FreeBSD](../troubleshooting/bash_shell_for_other_linux.md).
