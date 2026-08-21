---
title: Viewing Resource Details
description: "Use the GET method and a resource URI to request the resource's complete descriptor."
---

# 1.1.5 Viewing Resource Details

Use the GET method and a resource URI to request the resource's complete descriptor.

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/resources</span>/path/to/resource</p></td>
</tr>
<tr>
<td><p>Parameter</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p>expanded</p></td>
<td><p>true|false</p></td>
<td colspan="2"><p>When true, all nested resources will be given as full descriptors. The default behavior, false, has all nested resources given as references. For more information, see <span>Local Resources</span>.</p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p>accept: application/json (default)</p>
<p>accept: application/xml</p>
<p>accept: application/repository.folder+&lt;format&gt; (specifically to view the folder resource)</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The response will indicate the content-type and contain the corresponding descriptor, for example:</p>
<p>application/repository.dataType+json</p></td>
<td><p>404 Not Found – The specified resource is not found in the repository.</p></td>
</tr>
</tbody>
</table>
