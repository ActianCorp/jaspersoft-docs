---
title: Terminate Running Report
description: "Use the following method to stop a running report, as found with the previous method."
---

# 1.0.1 Terminate Running Report

Use the following method to stop a running report, as found with the previous method.

!!! note

    This syntax of the v2/reports service is deprecated. See [The v2/reportExecutions Service](the_v2_reportexecutions_service.md).

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
<td><p>PUT</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/reports</span>/&lt;executionID&gt;<span>/status/</span></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p>application/xml</p></td>
<td colspan="2"><p>Either an empty instance of the ReportExecutionCancellation class or</p>
<p>&lt;status&gt;cancelled&lt;/status&gt;.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The content also contains:<br />
&lt;status&gt;cancelled&lt;/status&gt;.</p></td>
<td><p>204 No Content – When the specified execution ID is not found on the server, and the response body is empty.</p></td>
</tr>
</tbody>
</table>
