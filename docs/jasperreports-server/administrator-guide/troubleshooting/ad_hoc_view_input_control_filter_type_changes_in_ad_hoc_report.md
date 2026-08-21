---
title: Ad Hoc View Filter Type Changes in Ad Hoc Report
description: "When saving an Ad Hoc Report from Ad Hoc View, if the filter has more than a specified number of input values, the input control type changes from a multi-select dropdown to input text field in..."
---

# Ad Hoc View Filter Type Changes in Ad Hoc Report

When saving an Ad Hoc Report from Ad Hoc View, if the filter has more than a specified number of input values, the input control type changes from a multi-select dropdown to input text field in dependent reports. Increasing this value may negatively affect performance.

<table>
<thead>
<tr>
<th colspan="3"><p>Set the Threshold for Ad Hoc Multi-Select Filter</p></th>
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
<td><code>maxAvailableValues</code></td>
<td colspan="2"><p>Sets the threshold value for Ad Hoc filter input values. By default, the value is <code>10000</code>.</p></td>
</tr>
</tbody>
</table>
