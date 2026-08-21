---
title: Post-Installation Tasks
description: Installing JasperReports Server automatically generates encryption keys that reside on the file system. These keys are stored in a dedicated Jaspersoft keystore. Make sure that this keystore is...
---

# Post-Installation Tasks

!!! note

    Installing JasperReports Server automatically generates encryption keys that reside on the file system. These keys are stored in a dedicated Jaspersoft keystore. Make sure that this keystore is properly secured and backed up, as described in the JasperReports Server Security Guide.

## Updates Made by the Installer During Installation

This section lists the standard updates the installer makes to your local environment when you install. When the installation completes, you can check whether the updates, or corresponding changes, were successful.

Updates made to the application server

If you installed to an existing Tomcat, the installer attempted to make updates to the Tomcat environment, as shown in the following table.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>File or Directory</p></th>
<th><p>Updates</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Windows: <code>bin/setclasspath.bat</code></p>
<p>Linux and Mac OSX: <code>bin/setclasspath.sh</code></p></td>
<td><p>Modifies <code>JAVA_OPTS</code> to add <code>-Djs.license.directory</code>.</p>
<p>(Commercial installer only)</p></td>
</tr>
<tr>
<td><p>All platforms: <code>lib</code></p></td>
<td><p>Adds JDBC drivers for databases to this directory.</p></td>
</tr>
</tbody>
</table>

Updates made to the PostgreSQL database

If you installed to an existing PostgreSQL database, the installer created new schemas and users in your database instance:

| PostgreSQL Updates | Description |
|----|----|
| Database `jasperserver` created | This is the JasperReports Server repository database. This database holds all of system information, such as users, roles, data sources, and report definitions. |
| Database user `jasperdb` created | The JasperReports Server application uses this user to connect to the database. |
| Sample database `foodmart` created | (optional) Database created if install sample data option was chosen. |
| Sample database `sugarcrm` created | (optional) Database created if install sample data option was chosen. |

## Installer Log File

The installer creates a log during installation that records information as the installation progresses. If you encounter problems during installation, ensure that your system meets all prerequisites, and then check the installer log for potential problems.

The installer log file captures information such as:

- Environment details such as the user that invoked the installer, host name, operating system details, and so on.

- List of assemblies installed.

- Information related to the Ant scripts executed by the installer.

You can find the installer log at `<js-install>/installation.log`.

## Setting your Java JVM Options

You need to set your Java JVM options. There are number of files where you can do this; refer to [Setting JVM Options for Application Servers](../additional/setting_jvm_options_for_application_.md).

## Installing a New License File

By default, JasperReports Server is installed with an evaluation license that expires a number of days after installation. After the license expires, you can start the server, but you can not log in.

To obtain a commercial license, contact [Jaspersoft Technical Support](https://www.jaspersoft.com/support) or your sales representative.

To upgrade the evaluation license to a commercial one, copy the commercial license file over the evaluation license file.

Application servers have work directories where JSP files are compiled and cached and other objects are stored. These directories can cause errors when upgrading a license. To avoid errors, clear the work directory before upgrading your license. For instance, if you are using Tomcat:

1.  Change the directory to `<tomcat>/work`

2.  Delete all the files in the directory.

After changing to a commercial license, make sure you stop the server before replacing the license file:

1.  Stop the server.

2.  Replace the license named `jasperserver.license` in the deployed JasperReports Server root directory with the new license file.

    The file name should be: `jaspersoft.jrs.license`.

3.  Restart the server.

By default, the license is in the \<js-install\> directory, but can be located elsewhere. You need to define the `‑Djs.license.directory` Java Environment Variable in the Tomcat startup scripts to point to the license location. The name of the license file is `jaspersoft.jrs.license`. Make sure that the new license file has this name.

Restart JasperReports Server and log in to see if the license grants access. For information about license errors, see the troubleshooting section [License-related Errors](../troubleshooting/license_related_errors.md).

For additional license configuration options, refer to [Setting Up the JasperReports Server License](../additional/setting_up_the_jasperreports_server_.md).

## License File for Existing Tomcat as Windows Service

If you installed JasperReports Server into an existing Tomcat installation on a Windows system running as a Windows Service and the license file is not in the default location, because you didn't choose the default `<js-install>` installation directory, manually configure Tomcat to locate the license file.

Follow the steps below to examine and update the license location:

1.  Open the Tomcat configuration tool by right-clicking the Tomcat icon in your quick-launch bar (usually in the lower-right corner of your desktop) or from the Windows 10 menu, expand ****Start \> Apache Tomcat**. Right-click Configure Tomcat** and select **Run as administrator**.

2.  Select the **Java** tab.

3.  At the bottom of the **Java Options** field, enter the following option:

    `-Djs.license.directory=<js-install>`

For example:

`-Djs.license.directory=C:\Jaspersoft\10.1.0`

4.  Stop and restart the application server.

You should now be able to run JasperReports Server.

## Configuration when Web Server is Run as Root on Linux

The export of reports, Ad Hoc views, and dashboards fails when Tomcat is run as root in the JasperReports Server installation on Linux. The Tomcat log file displays an error, for example:

```
2020-06-11T17:32:19,031 ERROR SecureExceptionHandlerImpl,http-nio-8080-exec-8:116 - com.github.kklisura.cdt.launch.exceptions.ChromeProcessTimeoutException: Failed while waiting for chrome to start: Timeout expired! Chrome output: [0611/173218.897370:ERROR:zygote_host_impl_linux.cc(89)] Running as root without --no-sandbox is not supported. See https://crbug.com/638180.
```

To resolve this you need to set the following property in the jasperreports.properties file:

```
net.sf.jasperreports.chrome.argument.no-sandbox=true
```

After setting this property, restart JasperReports Server to enable it.

For information about configuring this property, see the JasperReports Server Administrator Guide.
