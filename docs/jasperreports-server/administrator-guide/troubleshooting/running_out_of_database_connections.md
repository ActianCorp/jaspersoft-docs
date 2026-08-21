---
title: Running Out of Database Connections
description: "JasperReports Server manages a pool of connections for each JDBC data source. The default number of connections is 20, but if you run many reports concurrently against the same data source you may..."
---

# Running Out of Database Connections

JasperReports Server manages a pool of connections for each JDBC data source. The default number of connections is 20, but if you run many reports concurrently against the same data source you may reach the connection limit and see degraded performance. In particular, using the web service APIs, REST clients can easily launch many report executions at the same time and reach the limit.

The connection pool size is limited to avoid having too much memory permanently allocated to connections. But if you need more concurrent connections on a regular basis, you can increase the limit with the following configuration:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>Reducing the Size Limit for Ad Hoc Dimensions</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>.../WEB-INF/applicationContext.xml</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Bean</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>&lt;constructor-arg type="int" value="20"/&gt;</code><br />
</p></td>
<td><p><code>dataSource</code><br />
<code>ObjectPool</code><br />
<code>Factory</code><br />
<br />
</p></td>
<td><p>Change the default value to match your concurrent connections. Make sure you have enough memory to handle the connections and the concurrent report executions.</p></td>
</tr>
</tbody>
</table>

If you are using JNDI data sources, you can configure the number of connections in your application server. For more information, see the sections on JNDI in [Working With Data Sources](working_with_data_sources.md).
