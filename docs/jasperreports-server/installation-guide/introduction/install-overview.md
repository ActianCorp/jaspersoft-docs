---
title: Installation and Basic Usage
description: "You can install JasperReports Server either by running an executable installer or deploying a WAR file. For evaluations, we recommend the installer; for most production instances, we recommend the..."
---

# Installation and Basic Usage

This section includes:

- Installation
- Evaluation Licenses
- Login
- Starting and Stopping

## Installation

You can install JasperReports Server either by running an executable installer or deploying a WAR file. For evaluations, we recommend the installer; for most production instances, we recommend the WAR file. Both the executable and the WAR file are available from [Jaspersoft Technical Support](https://www.jaspersoft.com/support) ; download:

- ` `

  `js-jrs``_10.1.0`

  \_\<osType\>-\<arch\>.\<ext\>

- ` `

  `js-jrs``_10.1.0`

  \_bin.zip

For more information, see the installation guide, which is found at \<`js-install` \>/docs/JasperReports-Server-Install-Guide.pdf.

### Binary Installer

To install JasperReports Server, you can use the binary installer, which is available for Windows, Linux, and Mac:

`js-jrs``_10.1.0`

\_installer-\<osType\>-\<arch\>.\<ext\>

Double-click the installer and accept the default installation type to create a standard installation. Select the custom installation type to configure your instance to specify the application server and RDBMS to use, among other options. The installer can also be run from the command line.

### War File Distribution ZIP js-install Script Installation

You can use the js-install command-line shell scripts if you are installing to the third-party products listed in the JasperReports Server Supported Platform Datasheet. The scripts are found in this WAR file Distribution ZIP file:

`js-jrs``_10.1.0`

\_bin.zip.

To install

1.  Go to the buildomatic folder, create and edit a default_master.properties file, and run js-install.sh/bat:

    <table>
    <colgroup>
    <col style="width: 100%" />
    </colgroup>
    <tbody>
    <tr>
    <td><p>cd &lt;js-install&gt;/buildomatic</p>
    <p>cp sample_conf/&lt;dbType&gt;_master.properties default_master.properties</p></td>
    </tr>
    </tbody>
    </table>

2.  Using a text editor, edit default_master.properties to add your application server and database server properties:

    |                                     |
    |-------------------------------------|
    | ./js-install.sh (or js-install.bat) |

3.  Then change the JAVA_OPT memory options for your application server following instructions from the installation guide. For example, under Linux with Tomcat running on JDK 1.8, add the following to the top of the \<tomcat\>/bin/setclasspath.sh file:

    <table>
    <colgroup>
    <col style="width: 100%" />
    </colgroup>
    <tbody>
    <tr>
    <td><p>export JAVA_OPTS="$JAVA_OPTS -Xms1024m -Xmx2048m"</p>
    <p>export JAVA_OPTS="$JAVA_OPTS -Xss2m -XX:+UseConcMarkSweepGC -XX:+CMSClassUnloadingEnabled"</p></td>
    </tr>
    </tbody>
    </table>

4.  Next, copy your jasperserver.license to your application server user's home folder:

|                                                                |
|----------------------------------------------------------------|
| cp \<js-install\>/jasperserver.license \<path-to-home-folder\> |

## Evaluation Licenses

The installer includes several evaluation licenses that allow you to run various editions of JasperReports Server. When the evaluation period expires, you must replace the evaluation license with a commercial license to enable the software. See the JasperReports Server Installation Guide for information on replacing the license.

If you don't have a commercial license, contact your sales representative. During your evaluation, we invite you to use [Jaspersoft Quick Start Guide](https://www.jaspersoft.com/quick-start) and the [online help](http://help.jaspersoft.com/) to learn about our products.

## Login

To login after installation, use the following URL:

`http://<hostname>:8080/``jasperserver`` ``-pro`` `

These users are created during installation:

<table>
<tbody>
<tr>
<td>Default User</td>
<td>Password</td>
</tr>
<tr>
<td colspan="2">Always created</td>
</tr>
<tr>
<td>superuser</td>
<td>superuser</td>
</tr>
<tr>
<td>jasperadmin</td>
<td>jasperadmin</td>
</tr>
</tbody>
</table>

If you install the sample data, these users are also created:

|             |          |
|-------------|----------|
| Sample User | Password |
| joeuser     | joeuser  |
| demo        | demo     |

!!! warning

    For security reasons, always change the default passwords immediately after installing JasperReports Server.

## Starting and Stopping

This section describes how to start and stop the server if you installed using the binary installer. If you used another installation method, see the JasperReports Server Installation Guide.

### Windows

You can start and stop from the Windows menu: click **Programs \> JasperReports Server 10.1.0** **\> Start and Stop \> Start Service or Stop Service**.

### Linux

You can start and stop from the command line:

`./<js-install>/ctlscript.sh (start|stop)`

### Mac OS X

From Finder, double-click the start, stop, or login apps:

`/Applications/` ` 10.1.0/jasperServerStart.app`

`/Applications/10.1.0/jasperServerStop.app`

`/Applications/10.1.0/jasperServerLogin.app`

Alternatively, you can start/stop from the OS X command line:

`./<js-install>/ctlscript.sh (start|stop)`
