---
title: Setting JVM Options for Application Servers
description: "The settings in this section apply specifically to the Oracle/Sun JVM. Other JVMs may or may not have equivalent settings. For a list of supported JDK/JVMs and application servers, see the TIBCO..."
---

# Setting JVM Options for Application Servers

!!! note

    The settings in this section apply specifically to the Oracle/Sun JVM. Other JVMs may or may not have equivalent settings. For a list of supported JDK/JVMs and application servers, see the TIBCO Jaspersoft Platform Support document.

You may need to set the following options for your JVM:

- Memory: Java Virtual Machine (JVM) runtime parameters normally need to be explicitly set so that the memory settings have values larger than the default settings. The options and values depend on your version of Java and the application server that you use. You may need to increase the memory assigned for the JVM according to your usage.

!!! note

    If JasperReports Web Studio is deployed in the same application server as JasperReports Server, the memory demand increases. Hence, the memory assigned for Tomcat must be adjusted. It is recommended to increase Xmx at least by 0.5 GB.

- Garbage collection: You may need to tune garbage collection for your JVM, depending on your memory and CPU usage as well as JasperReports Server throughput. Different collectors have different performance characteristics. Consult the documentation for your JVM for information on available collectors.

- UTF-8 support for Oracle: If you need to support UTF-8 for your Oracle database, set `defaultNChar` to `true` to ensure that the database implicitly converts all `CHAR` data to `NCHAR` when you access `CHAR` columns. If you do not need to support UTF-8 for your Oracle database, you can omit this setting.

!!! note

    For the Oracle database, setting the Oracle localization option `defaultNChar` can substantially impact the performance of JDBC queries. If you do not need to support UTF-8 for your Oracle database, you can omit this setting.

## Tomcat and JBoss JVM Options

The following tables present some typical settings of JVM options that affect JasperReports Server. For information about changing a JVM option setting for your particular environment, see your application server documentation.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th colspan="2"><p>JVM Options on Windows (64 bit)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Options for all app servers</p></td>
<td><p>set <code>JAVA_OPTS=%JAVA_OPTS% -Xms2048m -Xmx4096m -Xss2m</code></p>
<p>set <code>JAVA_OPTS=%JAVA_OPTS% -XX:+UseG1GC</code></p></td>
</tr>
<tr>
<td>Java 17</td>
<td>set <code>JAVA_OPTS=%JAVA_OPTS% --add-opens java.base/java.io=ALL-UNNAMED --add-opens java.base/java.lang.ref=ALL-UNNAMED --add-opens java.base/java.lang=ALL-UNNAMED --add-opens java.base/java.nio.channels.spi=ALL-UNNAMED --add-opens java.base/java.nio.channels=ALL-UNNAMED --add-opens java.base/java.nio=ALL-UNNAMED --add-opens java.base/java.security=ALL-UNNAMED --add-opens java.base/java.text=ALL-UNNAMED --add-opens java.base/java.util.concurrent.atomic=ALL-UNNAMED --add-opens java.base/java.util.concurrent.locks=ALL-UNNAMED --add-opens java.base/java.util.concurrent=ALL-UNNAMED --add-opens java.base/java.util.regex=ALL-UNNAMED --add-opens java.base/java.util=ALL-UNNAMED --add-opens java.base/javax.security.auth.login=ALL-UNNAMED --add-opens java.base/javax.security.auth=ALL-UNNAMED --add-opens java.base/jdk.internal.access.foreign=ALL-UNNAMED --add-opens java.base/sun.net.util=ALL-UNNAMED --add-opens java.base/sun.nio.ch=ALL-UNNAMED --add-opens java.rmi/sun.rmi.transport=ALL-UNNAMED --add-opens java.base/sun.util.calendar=ALL-UNNAMED</code></td>
</tr>
<tr>
<td><p>For Oracle (optional)</p></td>
<td><p>set <code>JAVA_OPTS=%JAVA_OPTS% -Doracle.jdbc.defaultNChar=true</code></p></td>
</tr>
</tbody>
</table>

!!! note

    The java opts from the first line "Options for all app servers" should be added, and then an additional line is added either for Java 11 or Java 17.

    JasperReports Server doesn’t provide a virtual X frame buffer on Linux. If your Linux applications are graphical, set the `‑Djava.awt.headless=true` to prevent Java from trying to connect to an X Server for image processing.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th colspan="2"><p>JVM Options on Linux and Mac OSX (64 bit)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Options for all app servers</p></td>
<td><p>export<code> JAVA_OPTS="$JAVA_OPTS -Xms2048m -Xmx4096m -Xss2m"</code></p>
<p>export <code>JAVA_OPTS="$JAVA_OPTS -XX:+UseG1GC"</code></p></td>
</tr>
<tr>
<td>Java 11</td>
<td>export <code>JAVA_OPTS="$JAVA_OPTS -Djava.locale.providers=COMPAT"</code></td>
</tr>
<tr>
<td>Java 17</td>
<td>export <code>JAVA_OPTS="$JAVA_OPTS --add-opens java.base/java.io=ALL-UNNAMED --add-opens java.base/java.lang.ref=ALL-UNNAMED --add-opens java.base/java.lang=ALL-UNNAMED --add-opens java.base/java.nio.channels.spi=ALL-UNNAMED --add-opens java.base/java.nio.channels=ALL-UNNAMED --add-opens java.base/java.nio=ALL-UNNAMED --add-opens java.base/java.security=ALL-UNNAMED --add-opens java.base/java.text=ALL-UNNAMED --add-opens java.base/java.util.concurrent.atomic=ALL-UNNAMED --add-opens java.base/java.util.concurrent.locks=ALL-UNNAMED --add-opens java.base/java.util.concurrent=ALL-UNNAMED --add-opens java.base/java.util.regex=ALL-UNNAMED --add-opens java.base/java.util=ALL-UNNAMED --add-opens java.base/javax.security.auth.login=ALL-UNNAMED --add-opens java.base/javax.security.auth=ALL-UNNAMED --add-opens java.base/jdk.internal.access.foreign=ALL-UNNAMED --add-opens java.base/sun.net.util=ALL-UNNAMED --add-opens java.base/sun.nio.ch=ALL-UNNAMED --add-opens java.rmi/sun.rmi.transport=ALL-UNNAMED --add-opens java.base/sun.util.calendar=ALL-UNNAMED</code></td>
</tr>
<tr>
<td><p>For Oracle (optional)</p></td>
<td><p>export <code>JAVA_OPTS="$JAVA_OPTS -Doracle.jdbc.defaultNChar=true"</code></p></td>
</tr>
</tbody>
</table>

!!! note

    The java opts from the first line "Options for all app servers" should be added, and then an additional line is added either for Java 11 or Java 17.

You can set JVM options multiple ways. Sections Changing JVM Options for Tomcat as a Windows Service and Setting JVM Options for Application Servers present step-by-step instructions for performing this task. Alternatively, you can add your `JAVA_OPTS` settings to any of the following files.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>File</p></th>
<th><p>Add JVM Options After This Line on Windows</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>&lt;tomcat&gt;\bin\setclasspath.bat</p></td>
<td><p>set JAVA_ENDORSED_DIRS=%BASEDIR%\common\endorsed</p></td>
</tr>
<tr>
<td><p>&lt;tomcat&gt;\bin\setenv.bat</p></td>
<td><p><code>JAVA_OPTS</code> setting can go anywhere in this file.</p></td>
</tr>
<tr>
<td><p>&lt;jboss&gt;\bin\standalone.conf.bat</p></td>
<td><p>Find the existing <code>JAVA_OPTS</code> line, remove the default memory settings from this line, and add a new line with the recommended <code>JAVA_OPTS</code> after this line.</p>
<p>For example, you might <em>remove</em> the following default settings:</p>
<p><code>-Xms64m -Xmx512m -XX:MetaspaceSize=96M -XX:MaxMetaspaceSize=256m</code></p>
<p>Then add the recommended settings on a new line. We recommend that you do not set MaxMetaspaceSize.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>File</p></th>
<th><p>Add JVM Options After This Line on Linux</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>&lt;tomcat&gt;/bin/setclasspath.sh</p></td>
<td><p>JAVA_ENDORSED_DIRS="$BASEDIR"/common/endorsed</p></td>
</tr>
<tr>
<td><p>&lt;tomcat&gt;/bin/setenv.sh</p></td>
<td><p><code>JAVA_OPTS</code> setting can go anywhere in this file.</p></td>
</tr>
<tr>
<td><p>&lt;jboss&gt;/bin/standalone.conf</p></td>
<td><p>Find the existing <code>JAVA_OPTS</code> line, remove the default memory settings from this line, and add a new line with the recommended <code>JAVA_OPTS</code> after this line.</p>
<p>For example, you might <em>remove</em> the following default settings:</p>
<p><code>-Xms64m -Xmx512m -XX:MetaspaceSize=96M -XX:MaxMetaspaceSize=256m</code></p>
<p>Then add the recommended settings on a new line. We recommend that you do not set MaxMetaspaceSize.</p></td>
</tr>
</tbody>
</table>

## Changing JVM Options for Tomcat as a Windows Service

If you installed JasperReports Server to use Tomcat running as a Windows service, you can set Java options on the Java Tab of the Tomcat Properties dialog:

1.  Launch the Tomcat configuration application. If you installed the bundled Tomcat, you can do this by going to the `<js-install>/apache-tomcat/bin` directory and double-clicking the `jasperreportsTomcat.exe` file. (If you have multiple instances of JasperReports Server installed, the file name will be of the form ` jasperreportsTomcatnum<number>.exe`, for example, ` jasperreportsTomcatnum2.exe`.) If you installed Tomcat using an existing Windows service, look for an `.exe` file in the same location, with the same name as your Tomcat service, or select the service from the Windows Start menu:

****Start \> Programs \> Apache Tomcat \> Configure Tomcat (Run as administrator)****

1.  In the Apache Tomcat Properties dialog, click the **Java** tab.
2.  In the `Java Options` field, add your `JAVA_OPTS` values according to the tables above.

Enter only the options preceded by `-X` or `-D`, not `set JAVA_OPTS=%JAVA_OPTS%`.

Enter only one Java option setting per line.

1.  For instance, add options as follows:

```
-Xms2048m
-Xmx4096m
-Xss2m
```

1.  Click **Apply**, then click **OK**.
2.  Stop and restart Tomcat.

## Changing JVM Options for Bundled Tomcat on Linux

If you installed the bundled Tomcat, you can set Java options by editing the appropriate Tomcat configuration script. The steps to change JVM options are:

1.  Open the following file for editing:

`cd <js-install>/apache-tomcat/scripts/ctl.sh`

1.  Look for the `start_tomcat()` function and locate the `JAVA_OPTS` variable inside it.

<!-- -->

1.  Modify the `JAVA_OPTS` values according to the tables above. For example:

```
start_tomcat() {
    is_tomcat_running
    ...
         export JAVA_OPTS="-Xms2048m -Xmx4096m"
            export JAVA_OPTS="-Xss2m -XX:+UseG1GC"
    ...
}
```

!!! note

    There may be more than one occurrence of the `Java_OPTS` variable in the ctl.sh file. Make sure you edit the instance inside the `start_tomcat()` function.

1.  Save and close the `ctl.sh` file.
2.  Stop and restart PostgreSQL and Tomcat as described in [Starting and Stopping the Server](../../../installation-guide/binary-installer/starting-server.md).
