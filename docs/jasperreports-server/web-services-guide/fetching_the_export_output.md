---
title: Fetching the Export Output
description: "When the export state is ready, you can download the zip file containing the export catalog. Specify any filename in the request to receive the export in zip format with that name."
---

# 1.0.1 Fetching the Export Output

When the export state is `ready`, you can download the zip file containing the export catalog. Specify any filename in the request to receive the export in zip format with that name.

<table>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>GET</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/export</span>/&lt;export-id&gt;/&lt;filename&gt;</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – Returns the exported catalog as a zip file with the given &lt;filename&gt;.</p></td>
<td><p>404 Not Found – When the specified export ID is not found.</p></td>
</tr>
</tbody>
</table>

# 1.0.2 Canceling an Export Operation

To cancel any export operation that you have started, send a DELETE request with the ID of the export operation.

<table>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>DELETE</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/export</span>/&lt;export-id&gt;</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>204 No Content – The specified export operation was cancelled.</p></td>
<td><p>404 Not Found – When the specified export ID is not found.</p></td>
</tr>
</tbody>
</table>
