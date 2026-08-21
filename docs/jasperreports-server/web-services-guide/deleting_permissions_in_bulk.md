---
title: Deleting Permissions in Bulk
description: "The DELETE method removes all assigned permissions from the designated resource. After returning successfully, all effective permissions for the resource are inherited."
---

# Deleting Permissions in Bulk

The DELETE method removes all assigned permissions from the designated resource. After returning successfully, all effective permissions for the resource are inherited.

<table>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>DELETE</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/permissions</span>/path/to/resource</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>204 No Content – The request was successful.</p></td>
<td><p>404 Not Found – If the resource in the URL is invalid.</p></td>
</tr>
</tbody>
</table>
