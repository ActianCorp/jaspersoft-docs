---
title: Requesting Report Output
description: "After requesting a report execution and waiting synchronously or asynchronously for it to finish, your client is ready to download the report output."
---

# 1.0.1 Requesting Report Output

After requesting a report execution and waiting synchronously or asynchronously for it to finish, your client is ready to download the report output.

Every export format of the report has an ID that is used to retrieve it. For example, the HTML export in the previous example has the ID 195a65cb-1762-450a-be2b-1196a02bb625. To download the main report output, specify this export ID in the following method:

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/report</span><strong>Executions/</strong>requestID/<strong>exports</strong>/exportID/<strong>outputResource</strong></p></td>
</tr>
<tr>
<td colspan="2">Response Header</td>
<td colspan="2">Description</td>
</tr>
<tr>
<td colspan="2">output-final</td>
<td colspan="2">As of JasperReports® Server 5.6, this value indicates whether the out put is in its final form or not. When false, report items such as total page count are not finalized, but output is available early. You should reload the output resource again until this value is true.</td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The content is the main output of the report, in the format specified by the <code>contentType</code> property of the <code>outputResource</code> descriptor, for example:</p>
<p>text/html</p></td>
<td><p>404 Not Found – When the request ID specified in the request does not exist.</p></td>
</tr>
</tbody>
</table>

For example, to download the main HTML of the report execution response above, use the following URL:

GET http://localhost:8080/jasperserver-pro/rest_v2/reportExecutions/b487a05a-4989-8b53-b2b9-b54752f998c4/exports/195a65cb-1762-450a-be2b-1196a02bb625/outputResource

!!! note

    JasperReports Server does not support exporting Highcharts charts with background images to PDF, ODT, DOCX, or RTF formats. When exporting or downloading reports with Highcharts that have background images to these formats, the background image is removed from the chart. The data in the chart is not affected.

To download file attachments for HTML output, use the following method. You must download all attachments to display the HMTL content properly. The given URL is the default path, but it can be modified with the `attachmentsPrefix` property in the reportExecutionRequest, as described in [“Report Execution Properties”](running_a_report_asynchronously.md).

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/report</span><strong>Executions/</strong>requestID/<strong>exports</strong>/exportID/<strong>attachments</strong>/fileName</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The content is the attachment in the format specifiedin the <code>contentType</code> property of the <code>attachment</code> descriptor, for example:</p>
<p><span>image/png</span></p></td>
<td><p>404 Not Found – When the request ID specified in the request does not exist.</p></td>
</tr>
</tbody>
</table>

For example, to download the one of the images for the HTML report execution response above, use the following URL:

GET http://localhost:8080/jasperserver-pro/rest_v2/reportExecutions/912382875_1366638024956_2/exports/html/attachments/img_0_46_0
