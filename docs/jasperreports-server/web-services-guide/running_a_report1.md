---
title: Running a Report
description: The v2/reports service allows clients to receive report output in a single request-response. The output format is specified in the URL as a file extension to the report URI.
---

# Running a Report

The v2/reports service allows clients to receive report output in a single request-response. The output format is specified in the URL as a file extension to the report URI.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>GET</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/reports</span>/<br />
path/to/report<span>.</span>&lt;format&gt;?&lt;arguments&gt;</p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p>&lt;format&gt;</p></td>
<td>output<br />
type</td>
<td colspan="2"><p>One of the following formats: pdf, html, xls, xlsx, rtf, csv, xml, docx, odt, ods, jrprint.</p>
<p>As of JasperReports® Server 6.0, it is also possible to specify json if your reports are designed for data export. For more information, see the JasperReports® Library samples documentation.</p></td>
</tr>
<tr>
<td><p><code>page?</code></p></td>
<td><p>Integer &gt; 0</p></td>
<td colspan="2"><p>An integer value used to export a specific page</p></td>
</tr>
<tr>
<td><p>&lt;inputControl&gt;</p></td>
<td><p>String</p></td>
<td colspan="2"><p>Any input control that is defined for the report. Input controls that are multi-select may appear more than once. See examples below.</p></td>
</tr>
<tr>
<td><div class="language-text highlight"><pre><code>interactive?</code></pre></div></td>
<td><p>Boolean</p></td>
<td colspan="2"><p>In a commercial editions of the server where HighCharts are used in the report, this property determines whether the JavaScript necessary for interaction is generated when exporting to HTML. By default it is true. If set to false, the chart is generated as a non-interactive image file.</p></td>
</tr>
<tr>
<td><p><code>onePage PerSheet?</code><br />
</p></td>
<td><p>Boolean</p></td>
<td colspan="2"><p>Valid only for the XLS format. When true, each page of the report is on a separate spreadsheet. When false or omitted, the entire report is on a single spreadsheet. If your reports are very long, set this argument to true, otherwise the report will not fit on a single spreadsheet and cause an error.</p></td>
</tr>
<tr>
<td><code>baseUrl</code></td>
<td>String</td>
<td colspan="2">Specifies the base URL that the report will use to load static resources such as JavaScript files. You can also set the deploy.base.url property in the WEB-INF/js.config.properties file to set this value permanently. If both are set, the baseUrl parameter in this request takes precedence.</td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The content is the requested file.</p></td>
<td><p>404 Not Found – When the specified report URI is not found in the repository.</p></td>
</tr>
</tbody>
</table>

The follow examples show various combinations of formats, arguments, and input controls:

http://\<host\>:\<port\>/jasperserver\[-pro\]/rest_v2/reports/reports/samples/AllAccounts.html (all pages)

http://\<host\>:\<port\>/jasperserver\[-pro\]/rest_v2/reports/reports/samples/AllAccounts.html?page=43

http://\<host\>:\<port\>/jasperserver\[-pro\]/rest_v2/reports/reports/samples/AllAccounts.pdf (all pages)

http://\<host\>:\<port\>/jasperserver\[-pro\]/rest_v2/reports/reports/samples/AllAccounts.pdf?page=1

http://\<host\>:\<port\>/jasperserver\[-pro\]/rest_v2/reports/reports/samples/EmployeeAccounts.html?EmployeeID=sarah_id

http://\<host\>:\<port\>/jasperserver\[-pro\]/rest_v2/reports/reports/samples/Cascading_multi_select_report.html?<br>
Country_multi_select=USA&Cascading_state_multi_select=WA&Cascading_state_multi_select=CA

!!! note

    JasperReports Server does not support exporting Highcharts charts with background images to PDF, ODT, DOCX, or RTF formats. When exporting or downloading reports with Highcharts that have background images to these formats, the background image is removed from the chart. The data in the chart is not affected.
