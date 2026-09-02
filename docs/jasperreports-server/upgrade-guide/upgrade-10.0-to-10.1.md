---
title: Upgrading from 10.0 to 10.1
description: This chapter describes the recommended procedure for upgrading to JasperReports Server 10.1 from version 10.0. The examples show you how to upgrade using the js-upgrade shell script.
---

# Upgrading from 10.0 to 10.1

This chapter describes the recommended procedure for upgrading to JasperReports Server 10.1 from version 10.0. The examples show you how to upgrade using the `js-upgrade` shell script.

This chapter contains the following sections:

-   [Upgrade Steps Overview](#upgrade-steps-overview)

-   [Upgrading with Customizations](#upgrading-with-customizations)

-   [Back Up Your JasperReports Server Instance](#back-up-your-jasperreports-server-instance)

-   [Preparing the JasperReports Server 10.1 WAR File Distribution](#preparing-the-jasperreports-server-101-war-file-distribution)

-   [Configuring Buildomatic for Your Database and Application Server](#configuring-buildomatic-for-your-database-and-application-server)

-   [Upgrading to JasperReports Server 10.1](#upgrading-to-jasperreports-server-101)

-   [Starting and Logging into JasperReports Server 10.1](#starting-and-logging-into-jasperreports-server-101)

-   [Additional Tasks to Complete the Upgrade](#additional-tasks-to-complete-the-upgrade)

## Upgrade Steps Overview

These are the general steps used in this section:

1.  Identify your customizations.

2.  Back up your current JasperReports Server instance.

3.  Download and set up the new 10.1 JasperReports Server WAR file distribution zip.

4.  Run the `js-upgrade` script as described in [Upgrading to JasperReports Server 10.1](#upgrading-to-jasperreports-server-101).

If your current instance of JasperReports Server has modifications or extensions, monitor these and reintegrate them into your 10.1 instance after upgrading.

## Upgrading with Customizations

If your current instance of JasperReports Server has modifications or extensions, keep track of these and re-integrate them into your 10.1 instance after upgrading. See [Planning Your Upgrade](plan-upgrade-intro.md) to determine if any customizations you have made to your existing version of JasperReports Server are affected by changes to the updated version.

## Back Up Your JasperReports Server Instance

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

## Preparing the JasperReports Server 10.1 WAR File Distribution

Use the buildomatic `js-upgrade` scripts included in the 10.1 WAR file distribution ZIP release package to carry out the upgrade. The WAR file distribution comes in a compressed ZIP file named

`js-jrs``_10.1.0`

\_bin.zip.

Follow these steps to obtain and unpack the WAR file distribution ZIP file:

1.  [[Jaspersoft Technical Support](https://www.jaspersoft.com/support) ](http://support.jaspersoft.com) or contact your sales representative.

2.  Extract all files from

    `js-jrs``_10.1.0`

    \_bin.zip. Choose a destination, such as a `C:\Jaspersoft `folder on Windows, `/home/<user>` on Linux, or `/Users/<user> `on Mac.

After you unpack the WAR File Distribution, the resulting location will be known as:

`<js-install-10.1>`

## Configuring Buildomatic for Your Database and Application Server

This upgrade procedure uses the `js-upgrade-samedb` shell script.

!!! note

    For Unix, the bash shell is required for the js-upgrade scripts. If you are installing to a non-Linux Unix platform such as IBM AIX, FreeBSD or Solaris, you need to download and install the bash shell. See the Troubleshooting section of the JasperReports Server Installation Guide for more information.

PostgreSQL, MySQL, and Oracle databases. Other databases are similar.

### Example Buildomatic Configuration

The `default_master.properties` file handles the upgrade configuration. We provide a sample configuration file for each database. You must specify your database credentials and application server location, and rename the file to `default_master.properties`.

#### PostgreSQL Example

To configure `default_master.properties` for PostgreSQL:

1.  Locate the `postgresql_master.properties` sample configuration file.

    | Database | Master Properties File |
    |----|----|
    | PostgreSQL | `<js-install-10.1>/buildomatic/sample_conf/postgresql_master.properties` |

2.  Copy the file to `<js-install-10.1>/buildomatic`.

3.  Rename the file `default_master.properties`.

4.  Edit `default_master.properties` for your database and application server.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>Database</p></th>
<th><p>Sample Property Values</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PostgreSQL</p></td>
<td><div class="language-properties highlight"><pre><code><span class="na">appServerType</span><span class="o">=</span><span class="s">tomcat (or wildfly, etc.)</span>
<span class="na">appServerDir</span><span class="o">=</span><span class="s">c:</span><span class="se">\\</span><span class="s">Apache Software Foundation</span><span class="se">\\</span><span class="s">Tomcat 11.0.x (for example)</span>
<span class="na">dbUsername</span><span class="o">=</span><span class="s">postgres</span>
<span class="na">dbPassword</span><span class="o">=</span><span class="s">postgres</span>
<span class="na">dbHost</span><span class="o">=</span><span class="s">localhost</span></code></pre></div></td>
</tr>
</tbody>
</table>

For the Split upgrade, configure the settings in the `default_master.properties` file as described in [Additional Buildomatic Configuration for Split Installation Upgrade](jrs-install-guide/introduction/installation_types.md).

#### MySQL Example

To configure `default_master.properties` for MySQL:

1.  Locate the `mysql_master.properties` sample configuration file:

    | Database | Master Properties File |
    |----|----|
    | MySQL | `<js-install-10.1>/buildomatic/sample_conf/mysql_master.properties` |

2.  Copy the file to `<js-install-10.1>/buildomatic`.

3.  Rename the file `default_master.properties`.

4.  Edit `default_master.properties` for your database and application server.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>Database</p></th>
<th><p>Sample Property Values</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>MySQL</p></td>
<td><div class="language-properties highlight"><pre><code><span class="na">appServerType</span><span class="o">=</span><span class="s">tomcat (or wildfly, etc.)</span>
<span class="na">appServerDir</span><span class="o">=</span><span class="s">c:</span><span class="se">\\</span><span class="s">Apache Software Foundation</span><span class="se">\\</span><span class="s">Tomcat 11.0.x (for example)</span>
<span class="na">dbUsername</span><span class="o">=</span><span class="s">root</span>
<span class="na">dbPassword</span><span class="o">=</span><span class="s">password</span>
<span class="na">dbHost</span><span class="o">=</span><span class="s">localhost</span></code></pre></div></td>
</tr>
</tbody>
</table>

For the Split upgrade, configure the settings in the `default_master.properties` file as described in [Additional Buildomatic Configuration for Split Installation Upgrade](jrs-install-guide/introduction/installation_types.md).

#### Oracle Example

To configure `default_master.properties` for Oracle:

1.  Locate the `oracle_master.properties` sample configuration file:

    | Database | Master Properties File |
    |----|----|
    | Oracle | `<js-install-10.1>/buildomatic/sample_conf/oracle_master.properties` |

2.  Copy the file to `<js-install-10.1>/buildomatic`.

3.  Rename the file to `default_master.properties`.

4.  Edit `default_master.properties` for your database and application server.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>Database</p></th>
<th><p>Sample Property Values</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Oracle</p></td>
<td><div class="language-properties highlight"><pre><code><span class="na">appServerType</span><span class="o">=</span><span class="s">tomcat (or wildfly, etc.)</span>
<span class="na">appServerDir</span><span class="o">=</span><span class="s">c:</span><span class="se">\\</span><span class="s">Apache Software Foundation</span><span class="se">\\</span><span class="s">Tomcat 11.0.x (for example)</span>
<span class="na">dbUsername</span><span class="o">=</span><span class="s">jasperserver</span>
<span class="na">dbPassword</span><span class="o">=</span><span class="s">password</span>
<span class="na">sysUsername</span><span class="o">=</span><span class="s">system</span>
<span class="na">sysPassword</span><span class="o">=</span><span class="s">password</span>
<span class="na">dbHost</span><span class="o">=</span><span class="s">localhost</span>
<span class="na">dbVersion</span><span class="o">=</span><span class="s">oracleDbVersion (for example, 12, 19c, 21c, 23ai, 26ai and so on)</span></code></pre></div></td>
</tr>
</tbody>
</table>

For the Split upgrade, configure the settings in the `default_master.properties` file as described in [Additional Buildomatic Configuration for Split Installation Upgrade](jrs-install-guide/introduction/installation_types.md).

#### Using Vendor's Drivers for Commercial Databases

JasperReports Server doesn't include JDBC drivers for the following commercial databases: Oracle, SQL Server, or DB2. If you want to use one of those databases, you need to obtain one of the available JDBC drivers and copy it into the correct location, and then edit `default_master.properties` before running the upgrade steps. See [Working With JDBC Drivers](jdbc-driver.md) for more information.

## Upgrading to JasperReports Server 10.1

Now that your buildomatic scripts are configured, you can complete the upgrade.

!!! warning

    Make sure you have taken backup of your `Jasperserver` database before proceeding.

    Make sure you have taken backup of your old JasperReports Server WAR file before proceeding.

1.  Stop your application server.

2.  Start your database server.

3.  Upgrade script may check if license is valid since the previous JasperReports Server version contain JRXML in version 6, which when loaded require the use of the LegacyXmlLoader provided by JRL-Pro.

    To avoid license-related errors, valid license should be placed before running the upgrade.

    Place the `jasperserver.jrs.license` file in the `C:\Users\<user>` directory.

    For information about how to set up the license, see the JasperReports Server Installation Guide.

4.  Make sure that the user running the upgrade commands is the same user that installed the server.

5.  Run the following commands:

| Commands | Description |
|----|----|
| `cd <js-install-10.1>/buildomatic` |  |
| `js-upgrade-samedb .bat` | (Windows) Upgrade `jasperserver` `-pro` war file, upgrade Jasperserver database to 10.1, add 10.1 repository resources into the database. |
| `./js-upgrade-samedb .sh` | (Linux) Upgrade `jasperserver` `-pro` war files, upgrade Jasperserver database to 10.1, add 10.1 repository resources into the database. |

If you are prompted to create a keystore, this means that the server's original keystore was not found in the user's home directory. Proceed with caution:

-   In general, it is recommended to exit the upgrade procedure and make sure that the keystore is in the proper location, then rerun the upgrade.
-   If you continue and create a keystore, then the upgrade proceeds but your repository is corrupted and users are unable to log in. In this case, you need to export manually the server's repository with a custom key, then import the key before importing the repository.

For the Split upgrade, after the upgrade is done, to transfer the data (Audit, Access, and Log monitoring data) to the `audit` database from the `Jasperserver` database, run the following command:

-   Windows: `transfer-audit-data.bat`

-   Linux and Mac OSX: `./transfer-audit-data.sh`

The data is transferred to the `audit` database and the tables are deleted from the `Jasperserver` database. Rerun the command if there is any interruption in the data transfer process, it resumes the transfer process from where it was interrupted in the previous run.

### js-upgrade Test Mode

Use the `test` option to run the `js-upgrade` script in test mode. For example, on Windows, enter:

`cd <js-install-10.1>/buildomatic`

`js-upgrade-newdb .bat test <path>/js-9.0-export.zip`

In test mode, the `js-upgrade` scripts check your `default_master.properties` settings and validate your application server location and its ability to connect to your database. Test mode can help you debug issues like an incorrect database password without altering your system.

### Output Log Location

The `js-upgrade` script creates an output log that captures both standard and error output. If problems occur during script execution, or you just want to remember which options you chose, open the output log file located here:

`<js-install-10.1>/buildomatic/logs/js-upgrade-<date>-<number>.log`

### Errors

If you encounter errors running the `js-upgrade` script, first look at the output log to see if you can spot the errors. For help, refer to the Troubleshooting section of the JasperReports Server Installation Guide. The information in this section applies to both `js-upgrade` scripts and `js-install` scripts.

If you need to modify values in your `default_master.properties` file, you can simply edit the file. When you run the `js‑upgrade` script again, it uses the new values.

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
