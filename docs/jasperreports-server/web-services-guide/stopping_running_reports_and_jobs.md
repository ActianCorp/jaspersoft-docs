---
title: Stopping Running Reports and Jobs
description: "To stop a report that is running and cancel its output, use the PUT method and specify a status of “cancelled” in the body of the request."
---

# 1.0.1 Stopping Running Reports and Jobs

To stop a report that is running and cancel its output, use the PUT method and specify a status of “cancelled” in the body of the request.

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/report</span><strong>Executions/</strong>requestID/<strong>status</strong>/</p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p>application/xml</p>
<p>application/json</p></td>
<td colspan="2"><p>Send a <code>status</code> descriptor in either XML or JSON format with the value <code>cancelled</code>. For example:</p>
<p>XML: <code>&lt;status&gt;cancelled&lt;/status&gt;</code></p>
<p>JSON: <code>{ "value": "cancelled" }</code></p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p>accept: application/xml (default)</p>
<p>accept: application/json</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – When the report execution was successfully stopped, the server replies with the same status:</p>
<p>XML: <code>&lt;status&gt;cancelled&lt;/status&gt;</code></p>
<p>JSON: <code>{ "value": "cancelled" }</code></p>
<p>204 No Content – When the report specified by the request ID is not running, either because it finished running, failed, or was stopped by another process.</p></td>
<td><p>404 Not Found – When the request ID specified in the request does not exist.</p></td>
</tr>
</tbody>
</table>
