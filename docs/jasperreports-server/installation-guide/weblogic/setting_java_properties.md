---
title: Setting Java Properties
description: "Edit the WebLogic startup script for your platform to include the settings described in the following tables. Substitute the location of your JasperReports Server license file where necessary:"
---

# Setting Java Properties

Edit the WebLogic startup script for your platform to include the settings described in the following tables. Substitute the location of your JasperReports Server license file where necessary:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th colspan="2"><p>WebLogic Startup Settings on Windows</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Filename</p></td>
<td><p><code>&lt;wl-domain&gt;\bin\startWebLogic.cmd</code></p></td>
</tr>
<tr>
<td><p>Settings</p></td>
<td><p><code>set JAVA_OPTIONS=%JAVA_OPTIONS%</code><br />
<code>-Djs.license.directory=C:\&lt;js-install&gt;\</code><br />
<code>-Dfile.encoding=UTF-8</code><br />
<code>-Dcom.sun.xml.namespace.QName.useCompatibleSerialVersionUID=1.0</code><br />
<code>-Dlog4j.configurationFile=WEB-INF/log4j2.properties</code><br />
<code>-Xms2048m</code><br />
<code>-Xmx4096m</code><br />
<code>-Xss2m</code></p></td>
</tr>
<tr>
<td><p>For Oracle (optional)</p></td>
<td><p><code>set JAVA_OPTIONS=%JAVA_OPTIONS% -Doracle.jdbc.defaultNChar=true</code></p></td>
</tr>
</tbody>
</table>

!!! note

    Setting the Oracle localization option, defaultNChar, can substantially impact the performance of JDBC queries. If you don't need to support UTF-8 for your Oracle database, you can omit this setting.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th colspan="2"><p>WebLogic Startup Settings on Linux</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Filename</p></td>
<td><p><code>&lt;wl-domain&gt;/bin/startWebLogic.sh</code></p></td>
</tr>
<tr>
<td><p>Settings</p></td>
<td><p><code>export JAVA_OPTIONS="$JAVA_OPTIONS</code><br />
<code>-Djs.license.directory=/home/&lt;user&gt;/weblogic/jasperlicense/</code><br />
<code>-Dfile.encoding=UTF-8</code><br />
<code>-Dcom.sun.xml.namespace.QName.useCompatibleSerialVersionUID=1.0</code><br />
<code>-Dlog4j.configurationFile=WEB-INF/log4j2.properties</code><br />
<code>-Xms2048m</code><br />
<code>-Xmx4096m</code><br />
<code>-Xss2m"</code></p></td>
</tr>
<tr>
<td><p>For Oracle (optional)</p></td>
<td><p><code>export JAVA_OPTIONS="$JAVA_OPTIONS -Doracle.jdbc.defaultNChar=true"</code></p></td>
</tr>
</tbody>
</table>

!!! note

    Setting the Oracle localization option, `defaultNChar`, can substantially impact the performance of JDBC queries. If you don't need to support UTF-8 for your Oracle database, you can omit this setting.
