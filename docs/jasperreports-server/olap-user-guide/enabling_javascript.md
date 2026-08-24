---
title: Enabling Javascript in OLAP Schemas
description: "Some OLAP schemas contain Javascript to apply additional formatting on cell values. As of JasperReports Server version 8.2, Javascript in OLAP schemas is disabled by default because running scripts..."
---

# Enabling Javascript in OLAP Schemas

Some OLAP schemas contain Javascript to apply additional formatting on cell values. As of JasperReports Server version 8.2, Javascript in OLAP schemas is disabled by default because running scripts within the server can present a security risk.

If you want to use Javascript in OLAP schemas, you can change the following configuration setting and then restart the server:

<table>
<thead>
<tr>
<th colspan="3"><p>Enabling Javascript in OLAP Schemas</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>…/WEB-INF/js.config.properties</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><code>olap.mondrian.scripts.enabled</code></p></td>
<td colspan="2"><p>When this property is set to <code>true</code>, JasperReports Server runs Javascript in OLAP schemas. The default is <code>false</code>, in which case the server will not run any Javascript in an OLAP schema or Ad Hoc view based on a schema containing Javascript will trigger an exception with the message: <strong>OLAP view scripting feature is disabled</strong>.</p></td>
</tr>
</tbody>
</table>

!!! note

    Before enabling Javascript in OLAP schemas, make sure that access to the repository is properly secured by setting permissions so that only trusted users can create or modify your OLAP schemas.
