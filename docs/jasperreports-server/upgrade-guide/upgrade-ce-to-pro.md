---
title: Upgrading from the Community Project
description: "If you are running a Community Project (CP) instance of JasperReports Server and want to upgrade to a commercial version of JasperReports Server, follow the instructions in this chapter."
---

# Upgrading from the Community Project

If you are running a Community Project (CP) instance of JasperReports Server and want to upgrade to a commercial version of JasperReports Server, follow the instructions in this chapter.

This upgrade process uses the JasperReports Server commercial WAR File Distribution release package and the included buildomatic scripts.

!!! warning

    This CP to commercial upgrade procedure is valid only for upgrade within a major JasperReports Server release, for example 10.1 CP to 10.1 commercial.

This chapter contains the following sections:

- General Procedure

- Backing Up Your JasperReports Server CP Instance

- Exporting Your CP Repository Data

- Preparing the JasperReports Server 5.5 WAR File Distribution

- Configuring Buildomatic for Your Database and Application Server

- Upgrading to the Commercial Version of JasperReports Server 5.5

- Starting and Logging into JasperReports Server 5.5

- Re-Configuring XML/A Connections (Optional)

## General Procedure

The upgrade procedure consists of the following main steps:

1.  Back up your JasperReports Server CP instance.
2.  Export your CP repository data.
3.  Upgrade your instance to JasperReports Server Commercial.
4.  Import your CP repository data.

If you customized or extended JasperReports Server CP, you need to keep track of these modifications and integrate them with your JasperReports Server commercial instance after completing the upgrade.

## Backing Up Your JasperReports Server CP Instance

Back up the old JasperReports Server CP WAR file and `Jasperserver` database in case a problem occurs with the upgrade. Perform these steps from the command line in a Windows or Linux shell.

These instructions assume you have a Tomcat application server and the PostgreSQL or MySQL database. Other application servers require a similar procedure. If you have another database, consult your DB administration documentation for backup information.

### Backing Up Your JasperReports Server CP WAR File

For example, for Apache Tomcat, back up the `jasperserver` directory from the `<tomcat>/webapps` folder:

1.  Go to the `<tomcat>` directory.
2.  Make a new directory with a name, `js-cp-war-backup`.
3.  Copy `<tomcat>/webapps/ jasperserver` to `<tomcat>/js-cp-war-backup`.
4.  Delete the `<tomcat>/webapps/jasperserver` directory.

### Backing Up Your JasperReports Server Database

Go to the location where you originally unpacked your CP WAR File Distribution zip. (Or create a new local folder to hold your backup file.)

1.  Go to the `<js-install-cp>` directory.
2.  Run one of the following commands:
    - For PostgreSQL on Windows or Linux:

      ``` bash
      cd <js-install-cp>
      pg_dump --username=postgres  jasperserver  >  js-db-cp-dump.sql
      ```

    - For MySQL on Windows:

      ``` text
      mysqldump --user=root --password=<password> jasperserver > js-db-cp-dump.sql
      ```

    - For MySQL on Linux:

      ``` text
      mysqldump --user=root --password=<password> --host=127.0.0.1 jasperserver >js-db-cp-dump.sql
      ```

!!! note

    For MySQL, if you receive an error about packet size, see the Troubleshooting appendix of the JasperReports Server Installation Guide.

### Backing Up Your Keystore

**Back up your JasperReports Server Keystore**

1.  Create a folder (if you did not do so already) where you can save your server's keystore, for example `C:\JS_BACKUP` or `/opt/JS_BACKUP`.

2.  As the user who originally installed the server, copy `$HOME/.jrsks` and `$HOME/.jrsksp`  to  `<path>/JS_BACKUP`. Remember that these files contain sensitive keys for your data, so they must always be transmitted and stored securely.

## Exporting Your CP Repository Data

Before exporting your CP repository data, check to see if you have the `default_master.properties` file in this directory.

`<js-install-cp>/buildomatic/default_master.properties`

This file holds settings specific to your JasperReports Server instance, such as your application server location and your database type and location. If you do not have this file, see 8.5.1, “Example Buildomatic Configuration,” on page 59.

To export your CP repository data

1.  Navigate to the buildomatic directory:

    `cd <js-install-cp>/buildomatic`

2.  Run buildomatic with the export target:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td><p>Windows:</p></td>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode bash"><code class="sourceCode bash"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="ex">js-ant.bat</span> export-everything-ce <span class="at">-DexportFile</span><span class="op">=</span>js-cp-export.zip</span></code></pre></div></td>
</tr>
<tr>
<td><p>Linux:</p></td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode bash"><code class="sourceCode bash"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="ex">./js-ant</span> export-everything-ce <span class="at">-DexportFile</span><span class="op">=</span>js-cp-export.zip</span></code></pre></div></td>
</tr>
</tbody>
</table>

This operation uses the export option `--everything`, which collects all your repository data.

Remember the path to your exported file. You need to specify it when you import to your commercial JasperReports Server repository.

## Preparing the JasperReports Server 10.1 WAR File Distribution

Use the buildomatic scripts included in the commercial 10.1 WAR File Distribution release package for the upgrade. Follow these steps to obtain and unpack the commercial 10.1 WAR file distribution ZIP file:

1.  The WAR File Distribution comes in a compressed ZIP file named

    `js-jrs``_10.1.0`

    \_bin.zip. Download the WAR File Distribution from [Jaspersoft Technical Support](https://www.jaspersoft.com/support) or contact your sales representative.

2.  Extract all files from

    `js-jrs``_10.1.0`

    \_bin.zip. Choose a destination, such as `C:\Jaspersoft` on Windows, `/home/<user>` on Linux, or `/Applications` on Mac OSX.

    After you unpack the WAR File Distribution Zip, the resulting location is known as:

    `<js-install-pro>`

## Configuring Buildomatic for Your Database and Application Server

This upgrade procedure uses the buildomatic scripts included with the WAR File Distribution ZIP release package.

### Example Buildomatic Configuration

The `default_master.properties` file handles the upgrade configuration. We provide a sample configuration file for each database. You must specify your database credentials and your application server location, and rename the file to `default_master.properties`.

#### PostgreSQL Example

This example uses PostgreSQL (the same general logic applies to other databases).

1.  Copy `postgresql_master.properties` from:

    ``` xml
    <js-install-pro>/buildomatic/sample_conf
    ```

2.  Paste the file to:

    ``` xml
    <js-install-pro>/buildomatic
    ```

3.  Rename the file to: `default_master.properties`

4.  Edit `default_master.properties` for your database and application server. Sample property values are:
    - `appServerType=tomcat (or wildfly, and so on)`
    - `appServerDir=c:\\Apache Software Foundation\\Tomcat 11.0.x (for example)`
    - `dbUsername=postgres`
    - `dbPassword=postgres`
    - `dbHost=localhost`

For the Split upgrade, configure the settings in the `default_master.properties` file as described in [Additional Buildomatic Configuration for Split Installation Upgrade](jrs-install-guide/introduction/installation_types.md).

#### MySQL Example

This example uses MySQL (the same general logic applies to other databases).

1.  Copy `mysql_master.properties` from:

    \<js-install-pro\>/buildomatic/sample_conf\>

2.  Paste the file to:

    `<js-install-pro>/buildomatic`

3.  Rename the file to: `default_master.properties`

4.  Edit `default_master.properties` for your database and application server. Sample property values are:
    - `appServerType=tomcat (or wildfly, and so on)`
    - `appServerDir=c:\\Apache Software Foundation\\Tomcat 11.0.x (for example)`
    - `dbUsername=root`
    - `dbPassword=password`
    - `dbHost=localhost`

For the Split upgrade, configure the settings in the `default_master.properties` file as described in [Additional Buildomatic Configuration for Split Installation Upgrade](jrs-install-guide/introduction/installation_types.md).

## Upgrading to the Commercial Version of JasperReports Server 10.1

After configuring the `default_master.properties` file, you can complete the upgrade.

!!! warning

    Make sure you have backed up your `Jasperserver` database before proceeding.

    Make sure you have backed up your old JasperReports Server WAR file before proceeding.

1.  Stop your application server.

2.  Start your database server.

3.  Upgrade script may check if license is valid since the previous JasperReports Server version contain JRXML in version 6, which when loaded require the use of the LegacyXmlLoader provided by JRL-Pro.

    To avoid license-related errors, valid license should be placed before running the upgrade.

    Place the `jasperserver.jrs.license` file in the `C:\Users\<user>` directory.

    For information about how to set up the license, see the JasperReports Server Installation Guide.

4.  Make sure that the user running the upgrade commands is the same user that installed the server.

5.  Run the following commands:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>Commands</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>cd &lt;js-install-pro&gt;/buildomatic</code></p></td>
<td></td>
</tr>
<tr>
<td><p><code>js-ant drop-js-db</code></p>
<p><code>js-ant create-js-db</code></p>
<p><code>js-ant init-js-db-pro</code></p></td>
<td><p>The first command deletes your <code>jasperserver</code> database. Make sure it is backed up. The other commands recreate and initialize the database.</p></td>
</tr>
<tr>
<td><p><code>js-ant import-minimal-pro</code></p></td>
<td><p>Adds superuser, themes, and default tenant structure.</p></td>
</tr>
<tr>
<td><p>Windows:</p>
<p><code>js-ant import-upgrade</code><br />
<code>-DimportFile="&lt;path&gt;/js-cp-export.zip"</code><br />
<code>-DimportArgs="--include-server-settings</code><br />
<code>--secret-key='0x1b 0xd4 0xa6 ...'"</code></p>
<p>Linux and Mac OSX:</p>
<p><code>js-ant import-upgrade</code><br />
<code>-DimportFile=\"&lt;path&gt;/js-cp-export.zip\"</code><br />
<code>-DimportArgs=\"--include-server-settings</code><br />
<code>--secret-key=\'0x1b 0xd4 0xa6 ...\'\"</code></p></td>
<td><p>The <code>-DimportFile</code> argument should point to the <code>js-cp-export.zip</code> file you created earlier.</p>
<p><code>--include-server-settings --secret-key</code> specifies the key to use for the import. Use the same key that you imported into the keystore.</p>
<p>On Windows, you must use double quotation marks (<code>"</code>) if your path or filename contains spaces. On Linux, you must use double quotation marks escaped with a backslash (<code>\"</code>) in this case.</p></td>
</tr>
<tr>
<td><p><code>js-ant import-sample-data-upgrade-pro</code></p></td>
<td><p>(Optional) Loads the 10.1 commercial sample data.</p></td>
</tr>
<tr>
<td><p><code>js-ant deploy-webapp-cp-to-pro</code></p></td>
<td><p>Delete the CP war file, and deploy the commercial (pro) war file.</p></td>
</tr>
<tr>
<td><code>js-ant create-audit-db</code></td>
<td><p>(Optional) Creates the audit database. Required only for the Split installation.</p></td>
</tr>
<tr>
<td><code>js-ant init-audit-db-pro</code></td>
<td>(Optional) Initializes the audit database. Required only for the Split installation.</td>
</tr>
</tbody>
</table>

!!! note

    On MySQL, if you receive an error about packet size, see the Troubleshooting appendix of the JasperReports Server Installation Guide.

If you are prompted to create a keystore, this means that the server's original keystore was not found in the user's home directory. Proceed with caution:

- In general, it is recommended to exit the upgrade procedure and make sure that the keystore is in the proper location, then rerun the upgrade.

- If you continue and create a keystore, then the upgrade proceeds but your repository is corrupted and users are unable to log in. In this case, you need to export the server's repository with a custom key as described in [“Encryption Keys” on page 1](plan-upgrade-7.5.md). Then replace the `import-upgrade` commands in the table above with the following ones that specify the `secret-key` value from the export:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>Windows</p></th>
<th><p>Linux and Mac OSX</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode bash"><code class="sourceCode bash"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="ex">js-ant</span> import-upgrade</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a><span class="ex">-DimportFile=</span><span class="st">&quot;&lt;path&gt;/js-cp-export.zip&quot;</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a><span class="ex">-DimportArgs=</span><span class="st">&quot;--include-server-settings</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="st">--secret-key=&#39;0xb1 0x44 0x72 ...&#39;&quot;</span></span></code></pre></div></td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode bash"><code class="sourceCode bash"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="ex">js-ant</span> import-upgrade</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a><span class="ex">-DimportFile=\&quot;</span><span class="op">&lt;</span>path<span class="op">&gt;</span>/js-cp-export.zip\&quot;</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a><span class="ex">-DimportArgs=\&quot;--include-server-settings</span></span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a><span class="ex">--secret-key=\&#39;0xb1</span> 0x44 0x72 ...<span class="dt">\&#39;\&quot;</span></span></code></pre></div></td>
</tr>
</tbody>
</table>

## Starting and Logging into JasperReports Server 10.1

Before starting the server:

1.  Set up the JasperReports Server License.

Copy the `<js-install-pro>/jasperserver.jrs.license` file to the `C:\Users\<user>` directory (Windows 7 example).

For information about how to set up the license, see the JasperReports Server Installation Guide.

1.  Delete any files in the `<tomcat>\temp` folder.
2.  Delete any files, directories, or subdirectories in `<tomcat>\work\Catalina\localhost`.
3.  Delete any `jasperserver*.xml` files that might exist in `<tomcat>\conf\Catalina\localhost`.
4.  (Optional) Move any existing `<tomcat-install>\logs` files into a backup directory to clean up old CP log data.

For instructions on clearing directories, see 1.9, “Additional Tasks to Complete the Upgrade,” on page 1.

Now start your Tomcat or JBoss application server. Your database should already be running.

### Clearing Your Browser Cache

Before you log in, make sure you and your end-users clear the browser cache. JavaScript files, which enable UI elements of JasperReports® Server, are typically cached by the browser. Clear the cache to ensure that the newer files are used.

### Logging into the Commercial Version of JasperReports Server 10.1

Log in using the following URL, user IDs, and passwords:

URL: `http://localhost:8080/jasperserver-pro`

| User ID       | Password    | Description                                |
|---------------|-------------|--------------------------------------------|
| `superuser`   | superuser   | System-wide administrator                  |
| `jasperadmin` | jasperadmin | Administrator for the default organization |

!!! warning

    Your jasperadmin password might be reset to the default setting by the upgrade operation. For example, the Jasperadmin password might be reset to `jasperadmin`. For security reasons, you should change your Jasperadmin and superuser passwords to non-default values.

Your JasperReports Server instance has now been upgraded from Community Project (CP) to commercial. If startup or login problems occur, refer to the Troubleshooting appendix of the JasperReports Server Installation Guide.

## Re-configuring XML/A Connections (Optional)

XML/A connection definitions contain a username and password for connecting the Web Services to the server. A commercial edition of JasperReports® Server supports multi-tenancy, which allows multiple organizations on a single instance. The default organization is `organization_1`. Each user (except a `superuser`) must belong to a specific organization. After upgrading to the commercial JasperReports Server, users belong to the default organization.

You need to update XML/A connection definitions to include the organization the user belongs to.

The XML/A connection also specifies an instance URI. You need to update this URI to the commercial instance. Edit your XML/A connections as shown in the following examples:

- User IDs
  - Change `jasperadmin` to `jasperadmin|organization_1`
  - Change `joeuser` to `joeuser|organization_1`

- URI values

  Change:

  `http://localhost:8080/jasperserver/xmla `

  to

  `http://localhost:8080/jasperserver-pro/xmla`

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

```
update JIRepositoryCache set item_reference = null;
delete from JIRepositoryCache;
```
