---
title: Non-alphabetical Characters not Prioritized While Sorting Fields in Reports
description: "When a user sorts a string column in Ad Hoc or JRXML reports, values that begin with non-alphabetical characters (for example, a hyphen (-)) are not sorted correctly. Instead of appearing first as..."
---

# Non-alphabetical Characters not Prioritized While Sorting Fields in Reports

When a user sorts a string column in Ad Hoc or JRXML reports, values that begin with non-alphabetical characters (for example, a hyphen (-)) are not sorted correctly. Instead of appearing first as they would in an ASCII sort, they are sorted among the alphabetical entries.

The values are ordered lexicographically using the Unicode codepoint sequence. This ordering ensures that basic characters follow the established ASCII sort order.

<table>
<thead>
<tr>
<th colspan="3"><p>Non-alphabetical Characters not Prioritized While Sorting Fields in Reports</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>WEB-INF/classes/jasperreports.properties</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><code>net.sf.jasperreports.sorting.use.collator</code></td>
<td colspan="2"><p>Set the property value to <code>false</code> to use a standard Java string comparison, which is a simple, binary comparison based on the character's ASCII or Unicode value.</p></td>
</tr>
</tbody>
</table>
