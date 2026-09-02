---
title: Overlay Upgrade
description: "While upgrading from version 10.0 to JasperReports Server 10.1, the appropriate version of Tomcat must be installed. For steps on installation, see JasperReports® Server Installation Guide."
---

# Overlay Upgrade

!!! note

    While upgrading from version 10.0 to JasperReports Server 10.1, the appropriate version of Tomcat must be installed. For steps on installation, see JasperReports® Server Installation Guide.

This chapter describes the overlay process for upgrading to JasperReports Server 10.1.0 and contains the following sections:

-   [Introduction to the Overlay Upgrade](#introduction-to-the-overlay-upgrade)

-   [Upgrade Steps Overview](#upgrade-steps-overview)

-   [Plan Your Upgrade](#plan-your-upgrade)

-   [Back Up Your JasperReports® Server Instance](#back-up-your-jasperreports-server-instance)

-   [Unpack the Overlay Upgrade Package](#unpack-the-overlay-upgrade-package)

-   [Check for JDBC Driver (Oracle, SQL Server, DB2)](#check-for-jdbc-driver-oracle-sql-server-db2)

-   [Configure the Properties in the default_master.properties File](#configure-the-properties-in-the-default_masterproperties-file)

-   [Run the Overlay Upgrade](#run-the-overlay-upgrade)

-   [Rerun the Overlay Upgrade](#rerun-the-overlay-upgrade)

-   [Rollback Procedure](#rollback-procedure)

-   [Starting and Logging into JasperReports Server 10.1](#starting-and-logging-into-jasperreports-server-101)

-   [Additional Tasks to Complete the Upgrade](#additional-tasks-to-complete-the-upgrade)

-   [Running Overlay Upgrade a Second Time](#running-overlay-upgrade-a-second-time)

## Introduction to the Overlay Upgrade

The overlay upgrade procedure is available only for the JasperReports Server Commercial edition installed with the WAR file and only with the Apache Tomcat application server.

!!! warning

    -   The **overlay upgrade supports only the Apache Tomcat application server**.

    -   The **overlay upgrade supports only JasperReports Server installations using the WAR file**. The binary installer is not supported.

    -   The overlay upgrade is not possible if you configured custom encryption keys in your previous server.

    -   Only the certified repository databases are supported.

The overlay upgrade supports upgrading from JasperReports Server versions 9.0 and later to JasperReports Server 10.1.

Although the overlay upgrade does offer a rollback feature, you should always back up your database and application before upgrading.

!!! note

    This section uses 10.0 to 10.1 upgrade as an example.

## Upgrade Steps Overview

These are the general steps used in this section:

1.  Plan your upgrade.

2.  Back up your current JasperReports Server instance.

    (The overlay tool automatically takes back up of your war file and confirms if you have backed up your database.)

3.  Download and unpack the new JasperReports Server overlay upgrade 10.1 package zip file.

4.  Run the upgrade steps.

The overlay upgrade procedure helps you to identify any modifications or extensions you have made to your JasperReports Server instance.

!!! note

    It is always best practice to back up your application and database before upgrading.

## Plan Your Upgrade

If your current instance of JasperReports Server has modifications or extensions, keep track of these and re-integrate them into your 10.1 instance after upgrading. See [Planning Your Upgrade](plan-upgrade-intro.md) to determine if any customizations you have made to your existing version of JasperReports Server are affected by changes to the updated version.

## Back Up Your JasperReports® Server Instance

First back up your JasperReports Server WAR file and `Jasperserver` database so you can restore them if necessary. Perform these steps from the command line in a Windows or Linux shell.

This backup example is for Tomcat with the PostgreSQL or MySQL database. For other databases, consult your DB administration documentation for backup information.

**Back up your JasperReports Server War File**

1.  Create a folder where you can save your `jasperserver`` ``-pro`` ` war file, for example `C:\JS_BACKUP` or `/opt/JS_BACKUP`.
2.  Copy `<tomcat>/webapps/``jasperserver`` ``-pro`` `  to  `<path>/JS_BACKUP`.

**Back up your Jasperserver Database**

1.  Create a folder (if you did not do so in the step above) where you can save your `Jasperserver` database, for example `C:\JS_BACKUP` or `/opt/JS_BACKUP`.

2.  Run the following commands for PostgreSQL or MySQL:

    -   PostgreSQL

        ``` bash
        cd <path>/JS_BACKUP
        pg_dump --username=postgres  jasperserver  >  js-db-dump.sql
        ```

    -   MySQL

        ``` bash
        cd <path>/JS_BACKUP
        ```

        <table>
        <colgroup>
        <col style="width: 50%" />
        <col style="width: 50%" />
        </colgroup>
        <thead>
        <tr>
        <th>Operating System</th>
        <th>Command</th>
        </tr>
        </thead>
        <tbody>
        <tr>
        <td><p>Windows:</p></td>
        <td><div class="language-text highlight"><pre><code>mysqldump --user=root --password=&lt;password&gt; jasperserver &gt; js-db-dump.sql</code></pre></div></td>
        </tr>
        <tr>
        <td><p>Linux:</p></td>
        <td><div class="language-text highlight"><pre><code>mysqldump --user=root --password=&lt;password&gt; --host=127.0.0.1 jasperserver &gt;js-db-dump.sql</code></pre></div></td>
        </tr>
        </tbody>
        </table>

!!! note

    For MySQL, If you receive an error about packet size, see the Troubleshooting section of the JasperReports Server Installation Guide.

**Back up your JasperReports Server Keystore**

1.  Create a folder (if you did not do so already) where you can save your server's keystore, for example `C:\JS_BACKUP` or `/opt/JS_BACKUP`.

2.  As the user who originally installed the server, copy `$HOME/.jrsks` and `$HOME/.jrsksp`  to  `<path>/JS_BACKUP`. Remember that these files contain sensitive keys for your data, so they must always be transmitted and stored securely.

## Unpack the Overlay Upgrade Package

The overlay upgrade package comes in a file named:

`js-jrs``_10.1.0`

\_overlay.zip.

1.  Download the overlay upgrade package from [Jaspersoft Technical Support](https://www.jaspersoft.com/support) or contact your sales representative.

2.  Extract all files from

    `js-jrs``_10.1.0`

    \_overlay.zip. Create or choose a destination folder, such as `C:\JS_OVERLAY`on Windows,`/home/<user>/JS_OVERLAY` on Linux, or `/Users/<user>/JS_OVERLAY` on Mac.

    !!! note

        The overlay upgrade uses paths that exceed the 260-character limit on Windows. To extract the package, **Enable NTFS long paths** (Windows 10 only) or use a third-party file archive such as 7-Zip.

3.  The overlay upgrade package unpacks into a folder named:

    `overlay`

    This document refers to this folder location as:

    `<overlay-folder>`

## Check for JDBC Driver (Oracle, SQL Server, DB2)

JasperReports Server uses the JDBC drivers for the Oracle, SQL Server, and DB2 commercial databases. If you want to use a different JDBC driver, you need to copy it to the correct location. If you use Oracle or DB2, you must also use your existing version of the `db.template.properties` file. For more information, see [Working With JDBC Drivers](jdbc-driver.md).

## Configure the Properties in the default_master.properties File

Before running the overlay upgrade, copy the `default_master.properties` file from the existing JasperReports Server buildomatic directory to the Overlay buildomatic directory.

Edit the `default_master.properties` file and set `appServer` directory path to Tomcat 11.0.x path. For example, `appServerDir=c:\\Apache Software Foundation\\Tomcat 11.0.x`.

Configure the properties specific to the installation type:

-   For Compact upgrade: No additional configuration is required in the `default_master.properties` file.

-   For Split upgrade: Edit the `default_master.properties` file to configure the settings as described in [Installation Types](jrs-install-guide/introduction/installation_types.md).

## Run the Overlay Upgrade

The overlay upgrade works only with the Tomcat application server. It supports only the certified repository databases. You can perform the overlay upgrade whether you have local customizations or not.

1.  Stop the Tomcat application server.

2.  Make sure that your database is running.

3.  Make sure that the user running the overlay commands is the same user that installed the server.

4.  Run the following commands:

    ``` bash
    cd <overlay-folder>
    ```

    Windows: `overlay install`

    Linux: `./overlay install`

5.  You are prompted to specify a path to a working folder:

    -   You can accept the default or specify an alternate folder.
    -   Press `enter` to accept the default `../overlayWorkspace`.

6.  You are prompted to take a back up of your `Jasperserver` database. If you have already backed up your database, choose `y` to continue. If you have not yet backed up your database, choose `n` to exit the overlay and create a backup.

7.  You are prompted to shut down your Tomcat instance:
    -   You can stop Tomcat now if you have not already done so.
    -   Choose `y` for `yes` to continue.

8.  If you are prompted to create a keystore, this means that the server's original keystore was not found in the user's home directory. Proceed with caution:
    -   In general, it is recommended to exit the overlay procedure and make sure that the keystore is in the proper location, then rerun the overlay as described below.

    -   Alternatively, update the current location of the keystore in the `keystore.init.properties` file at the following locations:

        -   `.../WEB-INF/classes/keystore.init.properties`
        -   `.../buildomatic/keystore.init.properties`
        -   `.../buildomatic/conf_source/iePro/keystore.init.properties`

    -   If you continue and create a keystore, then the overlay proceeds but your repository is corrupted and users are unable to log in. In this case, you need to export manually the server's repository with a custom key, then import the key before importing the repository, as described in [Encryption Keys](plan-upgrade-7.5.md).

9.  You are prompted to specify a path to your `master.properties` file:

    Specify the path for your `default_master.properties` file, which is present in the Overlay buildomatic directory.

10. For final verification, the overlay prompts you for the path to your application server:

    -   If you have not moved it, it is located in the path to: `<tomcat>`
    -   Press `enter` to accept the default if it is correct.

11. The overlay begins updating your system:

    -   Your `jasperserver-pro` war file is automatically backed up.
    -   Potential customizations in your environment is analyzed.

    You are prompted to review the report on customizations if you choose to:

    -   Choose **y** for `yes` to continue with the upgrade.
    -   The`Jasperserver`database will be upgraded.
    -   The `jasperserver-pro` war file will be upgraded.
    -   The core data resources will be upgraded in the `Jasperserver` repository database.

When the overlay upgrade has finished, start Tomcat, and log in to test the upgraded JasperReports Server.

If the upgrade was successful, you see `BUILD SUCCESSFUL` on the command line.

For the Split upgrade, after the upgrade is done, to transfer the data (Audit, Access, and Log monitoring data) to the `audit` database from the `Jasperserver` database, run the following command:

-   Windows: `transfer-audit-data.bat`
-   Linux and Mac OSX: `./transfer-audit-data.sh`

The data is transferred to the `audit` database and the tables are deleted from the `Jasperserver` database. Rerun the command if there is any interruption in the data transfer process, it resumes the transfer process from where it was interrupted in the previous run.

!!! note

    Upgrading JasperReports Web Studio requires additional steps. For details, see [Upgrade JasperReports Web Studio](upgrade-jrws.md).

## Rerun the Overlay Upgrade

If you exit the `overlay install` for any reason, you can rerun the overlay by simply running the same command:

``` text
overlay install
```

By default, the overlay runs in resume mode (`resumeMode=true`). This means that your answers to previous prompts are remembered.

If you want to rerun the `overlay` "from scratch", run the following command:

``` text
overlay install -DresumeMode=false
```

For more information on the `overlay` options, run:

`overlay help`

## Rollback Procedure

If you encounter an error with the overlay upgrade, use the following rollback procedure:

1.  Stop Tomcat.

2.  Run the following command:

    ``` text
    overlay rollback
    ```

3.  Specify the path to the working folder:

    The default is `../overlayWorkspace`.

4.  The tool asks if you have rolled back your JasperReports Server database:

    The default is `no`.

    !!! note

        You are manually required to restore your database.

5.  When the tool has finished, restore your database (see below), start Tomcat, and test JasperReports Server.

**To restore your JasperReports Server Database**

1.  Go to the directory location where you saved the backup of your `Jasperserver` database.

    For example, `C:\JS_BACKUP` or `/opt/JS_BACKUP`.

2.  Run the following commands for PostgreSQL:

``` bash
cd /opt/JS_BACKUP
pg_restore --username=postgres  jasperserver  <  js-db-dump.sql
```

**To restore your JasperReports Server Keystore**

1.  Go to the directory location where you saved the backup of your JasperReports Serverkeystore.

    For example, `C:\JS_BACKUP` or `/opt/JS_BACKUP`.

2.  Copy the `.jrsks` and `.jrsksp` files from the `C:\JS_BACKUP` folder back to the `$HOME` folder, where they were originally backed up from.

!!! note

    If the backed up `.jrsks` and `.jrsksp` files are not copied from the `C:\JS_BACKUP` folder back to the `$HOME` folder, the JasperReports Server login page does not open and gives an error.

## Starting and Logging into JasperReports Server 10.1

Start your application server. Your database should already be running.

### Clearing Your Browser Cache

Before you log in, make sure you and your end users clear the browser cache. JavaScript files, which enable the UI elements of JasperReports Server, are typically cached by the browser. Clear the cache to ensure that the newer files are used.

### Logging into JasperReports Server

Log in using the following URL, user IDs, and passwords:

URL: `http://localhost:8080/``jasperserver`` ``-pro`` `

| User ID | Password | Description |
|----|----|----|
| `superuser` | &lt;your-password&gt; | System-wide administrator |
| `jasperadmin` | &lt;your-password&gt; | Administrator for the default organization |

Your JasperReports Server instance has now been upgraded to 10.1. If you have startup or login problems, refer to the Troubleshooting section of the JasperReports Server Installation Guide.

!!! note

    Upgrading JasperReports Web Studio requires additional steps. For details, see [Upgrade JasperReports Web Studio](upgrade-jrws.md).

## Additional Tasks to Complete the Upgrade

!!! note

    Installing JasperReports Server automatically generates encryption keys that reside on the file system. These keys are stored in a dedicated Jaspersoft keystore. Make sure that this keystore is properly secured and backed up, as described in the JasperReports Server Security Guide.

Perform these tasks with the application server shutdown.

### Handling JasperReports Server Customizations

If you made modifications to the original JasperReports® Server application, you need to copy manually configuration changes, like client-specific security classes or LDAP server configurations, from your previous environment and integrate them with your upgraded environment. These configurations are typically found in the files at the `WEB-INF/` location, for example, `applicationContext-*.xml, *.properties, *.js, *.jar,` and so on.

### Clearing the Application Server Work Folder

Application servers have work folders where JasperReports Server files are compiled and cached and other objects are stored. When you update the WAR file or license, the buildomatic `deploy-webapp-``pro`` ` target should automatically clear the application server’s `work` directory, but it is a good practice to double-check. A permission problem, or some other problem, could prevent the clearing of the work folder.

**To clear the work folder in Tomcat**

1.  Change the directory to `<tomcat>/work`.
2.  Delete all the files and folders in this directory.

### Clearing the Application Server Temp Folder

JasperReports Server uses caching to speed operations within the application. Caching files are created and stored in the application server, usually in a `temp` folder. Clear this `temp` folder to avoid any post-upgrade conflicts. Typically, the `temp` folder used by an application server corresponds to the path referenced by the `java.io.tmpdir` Java system property. For Apache Tomcat the `temp `folder is `<tomcat>/temp`.

**To clear the temp folder in Apache Tomcat**

1.  Change the directory to `<tomcat>/temp`.
2.  Delete all the files and folders in this directory.

### Clearing the Repository Cache Database Table

In the `Jasperserver` database, compiled JasperReports Library resources are cached in the `JIRepositoryCache` table for increased efficiency at runtime. Because the JasperReports Library JAR is typically updated with each new release, old cached items can get out of date and cause errors at runtime. If you encounter errors that mention a JasperReports Library "local class incompatible", check your repository cache table. In summary, you can clear your `Jasperserver` database cache table as part of this upgrade process whether there are errors or not.

**To clear the repository cache database table manually, run a SQL command similar to the one shown below**:

``` sql
update JIRepositoryCache set item_reference = null;
delete from JIRepositoryCache;
```

## Running Overlay Upgrade a Second Time

If you run the overlay upgrade a second time, the overlay logic asks if you want to resume the last run of the overlay, so that your previous answers to questions are remembered and reused.

The overlay procedure asks:

``` text
"We have detected that the overlay install was already run. Do you want to resume your last run? The default is 'y' ([y], n):"
```

-   Choose `y` for yes if you do not want to change any information previously given to the overlay.
-   Choose `n` for no if you would like to enter new or different information.

One reason for entering `n` for no would be if you did not give a valid path to your `default_master.properties` file the first time you run the overlay.
