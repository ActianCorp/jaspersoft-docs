---
title: Downloading Report Output
description: "Once a report has been generated with the PUT request, it is possible to download its files using a GET request."
---

# 1.0.1 Downloading Report Output

Once a report has been generated with the PUT request, it is possible to download its files using a GET request.

<table>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>GET</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest/report</span>/&lt;UUID&gt;?&lt;arguments&gt; (see example below)</p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p>file?</p></td>
<td><p>String</p></td>
<td colspan="2"><p>One of the files specified in the report xml. If the file parameter is not specified, the service returns the report descriptor.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The content is the requested file.</p></td>
<td><p>404 Not Found – When the specified UUID is not found in the user’s session.</p></td>
</tr>
</tbody>
</table>

For example, the URL to download the HTML of the report generated in the previous example is:

http://&lt;host&gt;:&lt;port&gt;/jasperserver\[-pro\]/rest/report/d7bf6c9-9077-41f7-a2d4-8682e74b637e?file=report

As a side effect of storing the report output in the user session, the UUID in the URL is visible only to the currently logged user. Other applications using different user IDs cannot access this report output.

!!! note

    JasperReports Server does not support exporting Highcharts charts with background images to PDF, ODT, DOCX, or RTF formats. When exporting or downloading reports with Highcharts that have background images to these formats, the background image is removed from the chart. The data in the chart is not affected.
