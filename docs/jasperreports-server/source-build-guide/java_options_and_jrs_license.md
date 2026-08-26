---
title: Java Options and JasperServer License Details
description: "To run properly, JasperReports Server needs more Java memory than the default settings. But for development work, the settings can be simpler than those recommended for production. For full..."
---

# Java Options and JasperServer License Details

## Setting Java JVM Options

To run properly, JasperReports Server needs more Java memory than the default settings. But for development work, the settings can be simpler than those recommended for production. For full information on recommended JAVA_OPTS settings, see the JasperReports Server Installation Guide.

### Tomcat and JBoss JVM Options

Here are some typical settings for JVM options that affect JasperReports Server. For space reasons, some of the options are displayed on multiple lines; make sure you set all options. These are the minimum recommended options; you may need to increase the JVM memory assignment according to your usage.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th colspan="2"><p>JVM Options on Windows</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Options for all app servers</p></td>
<td><p>set JAVA_OPTS=%JAVA_OPTS% -Xms2048m -Xmx4096m</p>
<p>set JAVA_OPTS=%JAVA_OPTS% -Xss2m -XX:+UseConcMarkSweepGC</p></td>
</tr>
<tr>
<td>Java 17</td>
<td><p>set JAVA_OPTS=%JAVA_OPTS% --add-opens java.base/java.io=ALL-UNNAMED -</p>
<p>-add-opens java.base/java.lang.ref=ALL-UNNAMED --add-opens</p>
<p>java.base/java.lang=ALL-UNNAMED --add-opens</p>
<p>java.base/java.nio.channels.spi=ALL-UNNAMED --add-opens</p>
<p>java.base/java.nio.channels=ALL-UNNAMED --add-opens</p>
<p>java.base/java.nio=ALL-UNNAMED --add-opens</p>
<p>java.base/java.security=ALL-UNNAMED --add-opens</p>
<p>java.base/java.text=ALL-UNNAMED --add-opens</p>
<p>java.base/java.util.concurrent.atomic=ALL-UNNAMED --add-opens</p>
<p>java.base/java.util.concurrent.locks=ALL-UNNAMED --add-opens</p>
<p>java.base/java.util.concurrent=ALL-UNNAMED --add-opens</p>
<p>java.base/java.util.regex=ALL-UNNAMED --add-opens</p>
<p>java.base/java.util=ALL-UNNAMED --add-opens</p>
<p>java.base/javax.security.auth.login=ALL-UNNAMED --add-opens</p>
<p>java.base/javax.security.auth=ALL-UNNAMED --add-opens</p>
<p>java.base/jdk.internal.access.foreign=ALL-UNNAMED --add-opens</p>
<p>java.base/sun.net.util=ALL-UNNAMED --add-opens</p>
<p>java.base/sun.nio.ch=ALL-UNNAMED --add-opens</p>
<p>java.rmi/sun.rmi.transport=ALL-UNNAMED --add-opens</p>
<p>java.base/sun.util.calendar=ALL-UNNAMED</p></td>
</tr>
<tr>
<td><p>For Oracle</p></td>
<td><p>set JAVA_OPTS=%JAVA_OPTS% -Doracle.jdbc.defaultNChar=true</p></td>
</tr>
</tbody>
</table>

JasperReports Server doesn’t provide a virtual X frame buffer on Linux. If your Linux applications are graphical, set the `‑Djava.awt.headless=true` to prevent Java from trying to connect to an X-Server for image processing.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th colspan="2"><p>JVM Options on Linux and Mac OSX</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Options for all app servers</p></td>
<td><p>export JAVA_OPTS="$JAVA_OPTS -Xms2048m -Xmx4096m"</p>
<p>export JAVA_OPTS="$JAVA_OPTS -Xss2m"</p>
<p>export JAVA_OPTS="$JAVA_OPTS -XX:+UseConcMarkSweepGC"</p></td>
</tr>
<tr>
<td>Java 17</td>
<td><p>export JAVA_OPTS="$JAVA_OPTS</p>
<p>UNNAMED --add-opens java.base/java.lang.ref=ALL-UNNAMED --add-opens</p>
<p>java.base/java.lang=ALL-UNNAMED --add-opens</p>
<p>java.base/java.nio.channels.spi=ALL-UNNAMED --add-opens</p>
<p>java.base/java.nio.channels=ALL-UNNAMED --add-opens</p>
<p>java.base/java.nio=ALL-UNNAMED --add-opens</p>
<p>java.base/java.security=ALL-UNNAMED --add-opens</p>
<p>java.base/java.text=ALL-UNNAMED --add-opens</p>
<p>java.base/java.util.concurrent.atomic=ALL-UNNAMED --add-opens</p>
<p>java.base/java.util.concurrent.locks=ALL-UNNAMED --add-opens</p>
<p>java.base/java.util.concurrent=ALL-UNNAMED --add-opens</p>
<p>java.base/java.util.regex=ALL-UNNAMED --add-opens</p>
<p>java.base/java.util=ALL-UNNAMED --add-opens</p>
<p>java.base/javax.security.auth.login=ALL-UNNAMED --add-opens</p>
<p>java.base/javax.security.auth=ALL-UNNAMED --add-opens</p>
<p>java.base/jdk.internal.access.foreign=ALL-UNNAMED --add-opens</p>
<p>java.base/sun.net.util=ALL-UNNAMED --add-opens</p>
<p>java.base/sun.nio.ch=ALL-UNNAMED --add-opens</p>
<p>java.rmi/sun.rmi.transport=ALL-UNNAMED --add-opens</p>
<p>java.base/sun.util.calendar=ALL-UNNAMED</p></td>
</tr>
<tr>
<td><p>For Oracle</p></td>
<td><p>export JAVA_OPTS="$JAVA_OPTS -Doracle.jdbc.defaultNChar=true"</p></td>
</tr>
</tbody>
</table>

You can set JVM options in a number of ways. For example, you can add your `JAVA_OPTS` settings to these files:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>File</p></th>
<th><p>Add JVM Options Below the Lines Shown Here:</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>&lt;tomcat&gt;\bin\setclasspath.bat</p></td>
<td><p>set JAVA_ENDORSED_DIRS=%BASEDIR%\common\endorsed</p></td>
</tr>
<tr>
<td><p>&lt;tomcat&gt;/bin/setclasspath.sh</p></td>
<td><p>JAVA_ENDORSED_DIRS="$BASEDIR"/common/endorsed</p></td>
</tr>
<tr>
<td><p>&lt;tomcat&gt;/bin/setenv.bat or</p>
<p>&lt;tomcat&gt;/bin/setenv.sh</p></td>
<td><p>JAVA_OPTS setting can go anywhere in this file.</p></td>
</tr>
<tr>
<td><p><span>&lt;jboss&gt;\bin\standalone.conf.bat</span></p>
<p><span>&lt;jboss&gt;/bin/standalone.conf</span></p></td>
<td><p>set JAVA_OPTS=%JAVA_OPTS% -Dprogram.name=%PROGNAME%</p>
<p>or</p>
<p>export JAVA_OPTS="$JAVA_OPTS -Dprogram.name=$PROGNAME"</p></td>
</tr>
</tbody>
</table>

!!! note

    For information on recommended `JAVA_OPTS` settings for all certified application servers, please refer to the JasperReports Server Installation Guide.

## Configuring the JasperReports Server License File

Commercial editions of JasperReports Server require a license file. The source code includes an evaluation license. You can use this license or replace it with the one you received from [Jaspersoft Technical Support](https://www.jaspersoft.com/support) or your sales representative.

### Configuring the License for All Application Servers

The main source build section describes placing a license in the home folder of the user running the application server. See [Put jaspersoft.jrs.license in Place](building_jasperreports_server_source.md).

### Configure the License in the Tomcat Scripts

If you would like to locate your jaspersoft.jrs.license in a specific folder, you can set a Java property in the shell script files used to control Tomcat.

JasperReports Server will look for a property named `js.license.directory` and use that folder as the location to find the `jaspersoft.jrs.license` file.

For instance, if you want to point JasperReports Server to the license file in the root of the source package, update the following shell script:

|          |                                        |
|----------|----------------------------------------|
| Windows: | &lt;tomcat&gt;\\bin\\setclasspath.bat  |
| Linux:   | &lt;tomcat&gt;/bin/setclasspath.sh     |

And you could update the file with the following setting:

|  |  |
|----|----|
| Windows: | set JAVA_OPTS=%JAVA_OPTS% "-Djs.license.directory=&lt;js-src&gt;" |
| Linux: | export JAVA_OPTS=$JAVA_OPTS -Djs.license.directory="&lt;js-src&gt;" |

The `jaspersoft.jrs.license` file can reside anywhere on the file system that's accessible from your application server. The `js.license.directory` setting should point to the folder containing the `jaspersoft.jrs.license`.

!!! note

    You'll find more information on configuring the jasperserver.license for all certified application servers in the JasperReports Server Installation Guide.
