---
title: Charts Not Appearing in Excel Export
description: "When exporting a report to Excel, JasperReports Server usually removes images that decorate the report and that do not fit in the Excel data-centric layout. However, JasperReports Server also..."
---

# Charts Not Appearing in Excel Export

When exporting a report to Excel, JasperReports Server usually removes images that decorate the report and that do not fit in the Excel data-centric layout. However, JasperReports Server also converts any charts to images and uses the special property `net.sf.jasperreports.export.xls.ignore.graphics` set to `false` to make the image appear. If your report does not set this property explicitly, the chart images do no appear in your reports when exported to Excel.

If you have a lot of reports with this issue, you can set the property on the server:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>Charts Images in Excel Export</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>.../WEB-INF/classes/jasperreports.properties</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><code>net.sf.jasperreports.</code><br />
<code>export.xls.ignore.graphics</code></p></td>
<td colspan="2"><p>By default, this property is set to <code>true</code>; in this case, images and chart images from the report do not appear when exported to Excel. Set this property to <code>false</code> to make chart images appear in Excel exports.</p></td>
</tr>
</tbody>
</table>
