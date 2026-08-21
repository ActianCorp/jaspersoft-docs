---
title: Deleting Resources
description: "The DELETE method has two forms, one for single resources and one for multiple resources."
---

# 1.0.1 Deleting Resources

The DELETE method has two forms, one for single resources and one for multiple resources.

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
<td><p>DELETE</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/resources</span>/path/to/resource<br />
</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>204 No Content – The request was successful and there is no descriptor to return.</p></td>
<td><p>404 Not Found – When the resource path or ID is not valid.</p></td>
</tr>
</tbody>
</table>

To delete multiple resources at once, specify multiple URIs with the resourceUri parameter.

<table>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>DELETE</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/resources</span>?resourceUri={uri]&amp;...</p></td>
</tr>
<tr>
<td><p>Parameter</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p>resourceUri</p></td>
<td><p>string</p></td>
<td colspan="2"><p>Specifies a resource to delete. Repeat this paramter to delete multiple resources.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>204 No Content – The request was successful and there is no descriptor to return.</p></td>
<td><p>404 Not Found – When the {resourceUri} is not valid.</p></td>
</tr>
</tbody>
</table>
