---
title: Configuring the Heartbeat
description: "During installation (or the first time you log in as administrator), you're prompted once to participate in the Heartbeat program, which reports technical information to the JasperReports Server..."
---

# Configuring the Heartbeat

During installation (or the first time you log in as administrator), you're prompted once to participate in the Heartbeat program, which reports technical information to the JasperReports Server product team about your implementation, such as the operating system, JVM, application server, database (type and version), data source types, and server edition and version number.

If you change your mind, you can change the heartbeat behavior by editing the following configuration file:

<table>
<thead>
<tr>
<th colspan="2"><p>Heartbeat Options</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="2"><p><code>.../WEB-INF/js.config.properties</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>heartbeat.enabled=true</code></p></td>
<td><p>When this property is set to <code>true</code>, JasperReports Server reports information about your environment to us once a week. When it is set to <code>false</code>, information is not sent.</p></td>
</tr>
<tr>
<td><p><code>heartbeat.askForPermission.enabled</code></p></td>
<td><p>Determines whether the administrator is prompted (the next time he logs into the web UI) about whether to allow heartbeat data to be sent. Typically, there is never cause to edit this property directly.</p></td>
</tr>
<tr>
<td><p><code>heartbeat.permissionGranted.enabled</code></p></td>
<td><p>Indicates whether a user has granted the server permission to send Heartbeat data. Setting this property to <code>false</code> prevents data from being sent.</p></td>
</tr>
</tbody>
</table>

All of these settings are properties that are substituted into the `heartbeatBean` in the `.../WEB-INF/applicationContext-heartbeat.xml` file.
