---
title: Precision Loss in Time Stamp in MS SQL Server
description: "When you run an Ad Hoc Report with a date filter of type BETWEEN (with day and month values), the query generated for Ad Hoc View is translated to a time stamp that includes milliseconds."
---

# Precision Loss in Time Stamp in MS SQL Server

When you run an Ad Hoc Report with a date filter of type BETWEEN (with day and month values), the query generated for Ad Hoc View is translated to a time stamp that includes milliseconds.

For example, `between '2020-07-01 00:00:00' and '2020-07-31 23:59:59.999'`. The time stamp `2020-07-31 23:59:59.999` in MS SQL Server is converted to `2020-08-01 00:00:00.000` which leads to filtering of data that is not required.

To handle this, the `ignoreMillisecondsInTimestampFilter` property should be set to `true`.

<table>
<thead>
<tr>
<th colspan="3"><p>Ignore Milliseconds in Time Stamp Filter</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>applicationContext-semanticLayer.xml</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><code>ignoreMillisecondsInTimestampFilter</code></td>
<td colspan="2"><p>Ignores the milliseconds in a date time stamp. By default, the value is <code>false</code>.</p></td>
</tr>
</tbody>
</table>
