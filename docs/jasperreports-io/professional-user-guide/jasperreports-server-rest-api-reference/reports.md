---
title: The reports Service
description: "The restv2/reports service has a simple API for obtaining report output, such as PDF and XLSX. The service also provides functionality to interact with running reports, report options, and input..."
---

# The reports Service

The rest_v2/reports service has a simple API for obtaining report output, such as PDF and XLSX. The service also provides functionality to interact with running reports, report options, and input controls.

This chapter includes the following sections:

- Running a Report
- Finding Running Reports
- Stopping a Running Report

## Running a Report

The reports service allows clients to receive report output in a single request-response. The reports service is a synchronous request, meaning the caller is blocked until the report is generated and returned in the response. For large datasets or long reports, the delay can be significant. If you want to use a non-blocking (asynchronous) request, see [REST API Reference - The reportExecutions Service](reportexecutions.md)

The output format is specified in the URL as a file extension to the report URI.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>GET</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/reports</span>/<br />
path/to/report<span>.</span>&lt;format&gt;?&lt;arguments&gt;</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jrio/<span>rest_v2/reports</span>/path/to/report<span>.</span>&lt;format&gt;?&lt;arguments&gt;</span></p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><span>&lt;format&gt;</span></p></td>
<td><p><span>output<br />
type</span></p></td>
<td colspan="2"><p>One of the following: <span>pdf</span>, <span>html</span>, <span>xlsx</span>, <span>rtf</span>, <span>csv</span>, <span>xml</span>, <span>docx</span>, <span>odt</span>, <span>ods</span>, <span>jrprint</span>.</p>
<p>As of JasperReports Server 6.0, it is also possible to specify <span>json</span> if your reports are designed for data export. For more information, see the JasperReports Library samples documentation.</p>
<p>One of the following formats:</p>
<ul>
<li>Regular output: html, pdf, csv, docx, pptx, xlsx, rtf, odt, ods, xml</li>
<li>Metadata output: data_csv, data_xlsx, data_json</li>
</ul></td>
</tr>
<tr>
<td><p><span>page?</span></p></td>
<td><p><span>Integer &gt; = 0</span></p></td>
<td colspan="2"><p>An integer value is used to export a specific page.</p>
<p>Passing 0 (zero) as the page parameter is accepted, and a blank report is displayed.</p></td>
</tr>
<tr>
<td><span>anchor?</span></td>
<td><span>String</span></td>
<td colspan="2">An anchor name in the generated report.</td>
</tr>
<tr>
<td><span>ignore<br />
pagination?</span></td>
<td><span>Boolean</span></td>
<td colspan="2">When set to true, the report is generated as a single page. This can be useful for some formats such as csv. When omitted, this argument's default value is false and the report is paginated normally.</td>
</tr>
<tr>
<td><p><span>&lt;parameter&gt;</span></p></td>
<td><p><span>String</span></p></td>
<td colspan="2"><p>Any parameter that is defined for the report. Parameters that are multivalue may appear more than once. See examples below.</p></td>
</tr>
<tr>
<td><p><span>&lt;inputControl&gt;</span></p></td>
<td><p><span>String</span></p></td>
<td colspan="2"><p>Any input control that is defined for the report. Input controls that are multi-select may appear more than once. See examples below.</p>
<p>By default, the input values are case sensitive. To change them to case insensitive, set <code>inputControl.handler.values.caseSensitive=false</code> in the <code>jasperserver-pro/WEB-INF/js.config.properties</code> file.</p></td>
</tr>
<tr>
<td><p><span>interactive?</span></p></td>
<td><p><span>Boolean</span></p></td>
<td colspan="2"><p>In the commercial edition of the server, where HighCharts are used in the report, this property determines the generation of the JavaScript required for interaction when exported to HTML. By default it is true. If set to false, the chart is generated as a non-interactive image file.</p></td>
</tr>
<tr>
<td><p><span>onePage<br />
PerSheet?</span></p></td>
<td><p><span>Boolean</span></p></td>
<td colspan="2"><p>Valid only for the XLS format. When the value is true, each page of the report is on a separate spreadsheet. If false or omitted, the entire report is on a single spreadsheet. For long reports, set this argument to true, otherwise the report does not fit on a single spreadsheet and causes an error.</p></td>
</tr>
<tr>
<td><span>report<br />
Container<br />
Width?</span></td>
<td><span>Integer</span></td>
<td colspan="2">This property specifies the width of the report container. A report specifying this parameter with integer values receives the current screen size width when the report is run.</td>
</tr>
<tr>
<td><p><span>baseUrl</span></p></td>
<td><p><span>String</span></p></td>
<td colspan="2"><p>Specifies the base URL that the reportusesuses to load static resources such as JavaScript files. You can also set the <span>deploy.base.url</span> property in the<span> .../WEB-INF/js.config.properties</span> file to set this value permanently. If both are set, the <span>baseUrl </span>parameter in this request takes precedence.</p>
<p>Specifies the base URL that the report uses to load static resources such as JavaScript files.</p></td>
</tr>
<tr>
<td><p><span>attachments<br />
Prefix</span></p></td>
<td><p><span>attachments</span></p></td>
<td colspan="2"><p>For HTML output, this property specifies the URL path to use for downloading the attachment files (JavaScript and images).</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The content is the requested file.</p></td>
<td><p>400 Bad Request – When incorrect format is provided in the Get request.</p>
<p>404 Not Found – When the specified report URI is not found in the repository.</p></td>
</tr>
</tbody>
</table>

The following examples show various combinations of formats, arguments, and input controls:

- http://\<host\>:\<port\>/jasperserver\[-pro\]/rest_v2/reports/reports/samples/AllAccounts.html (all pages)

- http://\<host\>:\<port\>/jasperserver\[-pro\]/rest_v2/reports/reports/samples/AllAccounts.html?page=43

- http://\<host\>:\<port\>/jasperserver\[-pro\]/rest_v2/reports/reports/samples/AllAccounts.pdf (all pages)

- http://\<host\>:\<port\>/jasperserver\[-pro\]/rest_v2/reports/reports/samples/AllAccounts.pdf?page=1

- http://\<host\>:\<port\>/jasperserver\[-pro\]/rest_v2/reports/reports/samples/EmployeeAccounts.html?<br>
  EmployeeID=sarah_id

- http://\<host\>:\<port\>/jasperserver\[-pro\]/rest_v2/reports/reports/samples/Cascading_multi_select_report.html?<br>
  Country_multi_select=USA&Cascading_state_multi_select=WA&Cascading_state_multi_select=CA

- http://\<host\>:\<port\>/jrio/rest_v2/reports/samples/reports/FirstJasper.html (all pages)

- http://\<host\>:\<port\>/jrio/rest_v2/reports/samples/reports/FirstJasper.html?page=5

- http://\<host\>:\<port\>/jrio/rest_v2/reports/samples/reports/FirstJasper.pdf (all pages)

- http://\<host\>:\<port\>/jrio/rest_v2/reports/samples/reports/FirstJasper.pdf?page=5

- http://\<host\>:\<port\>/jrio/rest_v2/reports/samples/reports/chartthemes/ChartThemesReport.pdf?chartTheme=aegean

!!! note

    JasperReports Server JasperReports IO does not support exporting Highcharts charts with background images to PDF, ODT, DOCX, or RTF formats. When exporting or downloading reports with Highcharts that have background images to these formats, the background image is removed from the chart. The data in the chart is not affected.

## Finding Running Reports

The reports service provides functionality to stop reports that are running. Reports can be running from user interaction, web service calls, or scheduling. The following method provides several ways to find reports that are currently running, in case the client wants to stop them.

!!! note

    This syntax of the reports service is deprecated. See [REST API Reference - The reportExecutions Service](reportexecutions.md).

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>GET</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/reports</span>/path/to/report/</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/reports</span>?&lt;arguments&gt;</span></p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><span>jobID?</span></p></td>
<td><p><span>String</span></p></td>
<td colspan="2"><p>Find the running report based on its <span>jobID</span> in the scheduler.</p></td>
</tr>
<tr>
<td><p><code>jobLabel?</code></p></td>
<td><p><span>String</span></p></td>
<td colspan="2"><p>Find the running report based on its <span>jobLabel</span> in the scheduler.</p></td>
</tr>
<tr>
<td><p><span>userName?</span></p></td>
<td><p><span>String</span></p></td>
<td colspan="2"><p>Name of user who has scheduled a report, in the format <span>&lt;username&gt;%7C&lt;organizationID&gt;</span>. In the commercial editions, <span>%7C&lt;organizationID&gt;</span> is required for all users except system admins (<code>superuser</code>).</p></td>
</tr>
<tr>
<td><p><span>fireTime<br />
From?</span></p></td>
<td><p><span>date/time</span></p></td>
<td colspan="2" rowspan="2"><p>Date and time in the following pattern: <span>yyyy-MM-dd'T'HH:mmZ</span>. Together, these arguments create a time range to find when the running report was started. Both of the range limits are inclusive. Either argument may be null to signify an open-ended range.</p></td>
</tr>
<tr>
<td><p><span>fireTimeTo?</span></p></td>
<td><p><span>date/time</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The content is a list of execution IDs that can be used for cancellation.</p></td>
<td><p>404 Not Found – When the specified report URI is not found in the repository.</p></td>
</tr>
</tbody>
</table>

For security purposes, the search for running reports has the following restrictions:

- The system administrator (`superuser`) can see and cancel any report running on the server.
- An organization admin (`jasperadmin`) can see every running report. But can cancel only the reports that are started by a user of the same organization or its child organizations.
- A regular user can see every running report, but can cancel only the reports that they initiated.

## Stopping a Running Report

Use the following method to stop a running report, as found with the previous method.

!!! note

    This syntax of the reports service is deprecated. See [REST API Reference - The reportExecutions Service](reportexecutions.md).

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>PUT</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/reports</span>/&lt;executionID&gt;<span>/status/</span></span></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/xml</span></p></td>
<td colspan="2"><p>Either an empty instance of the <span>ReportExecutionCancellation</span> class or</p>
<p><span>&lt;status&gt;canceled&lt;/status&gt;</span>.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The content also contains:<br />
<span>&lt;status&gt;canceled&lt;/status&gt;</span>.</p></td>
<td><p>204 No Content – When the specified execution ID is not found on the server, and the response body is empty.</p></td>
</tr>
</tbody>
</table>
