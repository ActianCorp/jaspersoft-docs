---
title: Data Trimmed in DOCX Export
description: "When report elements, such as crosstabs or tables, exceed the standard page width (for example, if a table is centered but its columns are too wide, pushing it off the left margin, or if a crosstab..."
---

# Data Trimmed in DOCX Export

When report elements, such as crosstabs or tables, exceed the standard page width (for example, if a table is centered but its columns are too wide, pushing it off the left margin, or if a crosstab element expands past the right margin), the content can fall outside the page boundaries.

To solve this, the DOCX export can be configured by making each page a variable size based on the actual, oversized dimensions of its content.

Use the following export configuration property to avoid the unwanted default DOCX page trimmings:

<table>
<thead>
<tr>
<th colspan="3"><p>Data Trimmed in DOCX Export</p></th>
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
<td><code>net.sf.jasperreports.export.docx.size.page.to.content</code></td>
<td colspan="2"><p>Ensures that the page is automatically resized to fit the report's content when exported to a DOCX file. Set the value to <code>true</code> to activate the fix.</p></td>
</tr>
</tbody>
</table>
