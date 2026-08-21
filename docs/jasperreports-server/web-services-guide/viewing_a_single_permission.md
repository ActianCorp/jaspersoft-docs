---
title: Viewing a Single Permission
description: "Specify the recipient in the URL to see a specific assigned permission. To view effective permissions, use the form above."
---

# Viewing a Single Permission

Specify the recipient in the URL to see a specific assigned permission. To view effective permissions, use the form above.

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/permissions</span>/path/to/resource;recipient=<br />
&lt;recipient&gt;</p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p>recipient</p></td>
<td><p>string required</p></td>
<td colspan="2"><p>The recipient format specifies <code>user</code> or <code>role</code>, the object ID and the organization ID if necessary. The vertical bar character must be encoded, for example:</p>
<p>user:joeuser%7Corganization_1</p></td>
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
<td colspan="3"><p>200 OK – The body describes the requested permission.</p></td>
<td><p>404 Not Found – When the specified resource URI or recipient is invalid.</p></td>
</tr>
</tbody>
</table>
