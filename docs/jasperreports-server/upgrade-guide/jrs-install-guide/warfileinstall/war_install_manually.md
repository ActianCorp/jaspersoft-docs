---
title: Installing the WAR File Manually
description: You may need to install the WAR file manually when you cannot use the js-install scripts.
---

# Installing the WAR File Manually

You may need to install the WAR file manually when you cannot use the `js-install` scripts.

The manual buildomatic steps described in this procedure execute the same Ant targets as the `js-install` script (`js-install`` .sh`/`.bat`). The procedure shows which buildomatic targets to run manually if you are unable to use the `js-install` scripts.

To install the WAR file distribution using manual buildomatic steps

1.  Start your database server.
2.  Stop your application server.
3.  Create and edit a `default_master.properties` file to add the settings in for your database and application server as described in [Installing the WAR File Using js-install Scripts](../../../installation-guide/warfileinstall/war_install_using_js_install.md).
4.  Open a Command Prompt as Administrator on Windows or open a terminal window on Linux or Mac. Run the following commands.

<table>
<caption><p>Buildomatic Targets to Execute to Install the WAR File</p></caption>
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
<td><p><code>cd &lt;js-install&gt;/buildomatic</code></p></td>
<td><p>Makes the buildomatic directory your current directory.</p></td>
</tr>
<tr>
<td><p><code>js-ant create-js-db</code></p></td>
<td><p>Creates the JasperReports Server repository database.</p></td>
</tr>
<tr>
<td><p><code>js-ant create-sugarcrm-db</code></p>
<p><code>js-ant create-foodmart-db</code></p></td>
<td><p>(Optional) Creates the sample databases.</p></td>
</tr>
<tr>
<td><p><code>js-ant load-sugarcrm-db</code></p>
<p><code>js-ant load-foodmart-db</code></p></td>
<td><p>(Optional) Loads sample data into the sample databases.</p></td>
</tr>
<tr>
<td><p><code>js-ant update-foodmart-db</code></p></td>
<td>(Optional) Initializes the sample databases</td>
</tr>
<tr>
<td><p><code>js-ant init-js-db-</code><span><code>pro</code></span><code> </code></p>
<p><code>js-ant import-minimal-</code><span><code>pro</code></span><code> </code></p></td>
<td><p>Initializes the <code>jasperserver</code> database, loads core application data. Running <span>js-ant import-minimal-<span>pro</span> </span> is mandatory. The server needs this data to function.</p></td>
</tr>
<tr>
<td><p><code>js-ant import-sample-data-</code><span><code>pro</code></span><code> </code></p></td>
<td><p>(Optional) Loads the demos that use the sample data.</p></td>
</tr>
<tr>
<td><p><code>js-ant deploy-webapp-</code><span><code>pro</code></span><code> </code></p></td>
<td><p>Configures and deploys the WAR file to Tomcat or JBoss.</p></td>
</tr>
<tr>
<td><code>js-ant deploy-jrws</code></td>
<td><p>Deploys only JasperReports Web Studio apps into the application server configured using the <code>appServerDir, jrws.repo.url and jrws.jrio.url</code> properties in the <code>default_master.properties</code> file.</p></td>
</tr>
<tr>
<td><code>js-ant create-audit-db</code></td>
<td>(Optional) Creates the audit database. Required only for the Split installation.</td>
</tr>
<tr>
<td><code>js-ant init-audit-db-pro</code></td>
<td>(Optional) Initializes the audit database. Required only for the Split installation.</td>
</tr>
</tbody>
</table>

!!! note

    On non-Linux Unix platforms, the js-ant commands may not be compatible with all shells. If you have errors, use the `bash` shell explicitly. For more information, see [Bash Shell for Solaris, IBM AIX, HP UX and FreeBSD](../../../installation-guide/troubleshooting/bash_shell_for_other_linux.md).

If you encounter an error when running `create-sugarcrm-db`, `create-foodmart-db`, or `create-js-db`, you can create the JasperReports Server database manually using the database administration tool for your particular database type. To create the JasperReports Server database manually for

PostgreSQL, MySQL, Oracle, SQL Server, or DB2

, refer to [Manually Creating the JasperReports Server Database](../../../installation-guide/manual-db/manually_creating_the_jasperreports_.md).

If you have previously installed the databases, you can drop the old versions and then recreate the databases. To do this, run the following drop commands before running the commands in Buildomatic Targets to Execute to Delete Sample Databases.

<table>
<caption><p>Buildomatic Targets to Execute to Delete Sample Databases</p></caption>
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
<td><p><code>js-ant drop-sugarcrm-db</code></p>
<p><code>js-ant drop-foodmart-db</code></p></td>
<td><p>(Optional) Deletes the sample databases.</p></td>
</tr>
<tr>
<td><p><code>js-ant drop-js-db</code></p></td>
<td><p>(WARNING) Deletes the JasperReports Server repository database. Only run this command if you intend to recreate the <code>jasperserver</code> database</p></td>
</tr>
<tr>
<td><code>js-ant drop-audit-db</code></td>
<td><p>(Optional) Deletes the audit database.</p>
<p>Required only for the Split installation, or if the previous installation was Split, or for the database clean up after a Split installation.</p></td>
</tr>
</tbody>
</table>

1.  Set Java JVM Options (required) as described in [Setting JVM Options for Application Servers](../../../installation-guide/additional/setting_jvm_options_for_application_.md).
2.  Set up the license (required) as described in [Setting Up the JasperReports Server License](../../../installation-guide/additional/setting_up_the_jasperreports_server_.md).

!!! note

    Installing JasperReports Server automatically generates encryption keys that reside on the file system. These keys are stored in a dedicated Jaspersoft keystore. Make sure that this keystore is properly secured and backed up, as described in the JasperReports Server Security Guide.
