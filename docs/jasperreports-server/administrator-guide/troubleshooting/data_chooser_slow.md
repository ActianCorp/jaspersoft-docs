---
title: Data Chooser is Slow
description: "When building a list of available data sources for Ad Hoc Views, the Data Chooser runs sub-queries to filter out ad hoc reports and views that are stored at /adhoc/topics. When a large number of ad..."
---

# Data Chooser is Slow

When building a list of available data sources for Ad Hoc Views, the Data Chooser runs sub-queries to filter out ad hoc reports and views that are stored at `/adhoc/topics`. When a large number of ad hoc reports and views are stored in the repository under that location, the sub-query can be slow. To improve performance, you can disable the sub-uery by setting`skip.adhoc.datasource.check` to `true` in `jasperserver-pro/WEB-INF/js.config.properties`.

If `skip.adhoc.datasource.check` is enabled, avoid using ad hoc reports as a data source.

<table>
<tbody>
<tr>
<td colspan="2">Configuration File</td>
</tr>
<tr>
<td colspan="2"><code>.../WEB-INF/js.config.properties</code></td>
</tr>
<tr>
<td>Property</td>
<td>Description</td>
</tr>
<tr>
<td><code>skip.adhoc.datasource.check</code></td>
<td>To improve performance, disable the sub-queries by setting <code>skip.adhoc.datasource.check</code> to <code>true</code>.</td>
</tr>
</tbody>
</table>
