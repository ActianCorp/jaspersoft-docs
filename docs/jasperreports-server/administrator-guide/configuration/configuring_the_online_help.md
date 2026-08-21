---
title: Configuring the Online Help
description: "JasperReports Server professional edition includes an online help system that describes the web interface. If your users don't have Internet connectivity, or if you don't want to provide access to..."
---

# Configuring the Online Help

JasperReports Server professional edition includes an online help system that describes the web interface. If your users don't have Internet connectivity, or if you don't want to provide access to this system, you can configure the server to hide the help links completely.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>Online Help Configuration Options</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>.../WEB-INF/applicationContext-webHelp.xml</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Bean</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>showHelp</code></p></td>
<td><p><code>webHelp</code></p></td>
<td><p>Determines whether the help links are displayed in the JasperReports Server web UI. Valid values are <code>true</code> and <code>false</code>.</p>
<p>The <strong>Help</strong> link appears at the top right corner of the web UI's pages.</p></td>
</tr>
<tr>
<td><p><code>hostURL</code></p></td>
<td><p><code>webHelp</code></p></td>
<td><p>Indicates the name of the computer hosting the web server where the help is running. The value depends on the version of JasperReports Server. Do not change this value.</p></td>
</tr>
<tr>
<td><p><code>pagePrefix</code></p></td>
<td><p><code>webHelp</code></p></td>
<td><p>Defines the default page name to pass to the web server hosting the help system. The only valid value is <code>Default_CSH.htm</code> for this property.</p></td>
</tr>
<tr>
<td><p><code>helpContextMap</code></p></td>
<td><p><code>webHelp</code></p></td>
<td><p>Maps contexts in the application to topic identifiers in the help system. Many pages in the web application are configured for context-sensitivity. When a user clicks <code>Help</code> on such a page, JasperReports Server loads a specific topic in the help system. The topic that appears is determined by a map in the <code>applicationContext-webHelp.xml</code> file. The only valid values are the defaults.</p></td>
</tr>
</tbody>
</table>
