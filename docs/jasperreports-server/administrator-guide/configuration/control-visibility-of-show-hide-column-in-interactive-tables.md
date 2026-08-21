---
title: Show or Hide Columns in Interactive Tables
description: JIVE action of show/hide columns is now enhanced to provide more control over which columns to display. You can now show or hide single/multiple columns.
---

# Show or Hide Columns in Interactive Tables

JIVE action of show/hide columns is now enhanced to provide more control over which columns to display. You can now show or hide single/multiple columns.

You can enable or disable this feature by configuring three properties in the `WEB-INF/classes/jasperreports.properties` file, as listed in the table.

By default, these properties are enabled.

<table>
<thead>
<tr>
<th colspan="2"><p>Show/Hide Columns in Interactive Tables</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="2"><p><code>WEB-INF/classes/jasperreports.properties</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><code>net.sf.jasperreports.htmlviewer.menu.showColumns.visible</code></td>
<td>This property now allows you to control the visibility of the <strong>Show columns</strong> menu item in the JIVE report. By default, it is set to <code>true</code>.</td>
</tr>
<tr>
<td><code>net.sf.jasperreports.htmlviewer.menu.hideColumn.visible</code></td>
<td>This property now allows you to control the visibility of the <strong>Hide column</strong> menu item in the JIVE report. By default, it is set to <code>true</code>.</td>
</tr>
<tr>
<td><code>net.sf.jasperreports.htmlviewer.menu.showHideMultipleColumns.visible</code></td>
<td>This property now allows you to control the visibility of the <strong>Show/Hide multiple columns</strong> menu item in the JIVE report. By default, it is set to <code>true</code>.</td>
</tr>
</tbody>
</table>
