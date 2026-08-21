---
title: Deleting a Resource
description: "The DELETE method can be used with either a folder or a resource. For the delete to succeed:"
---

# 1.0.1 Deleting a Resource

The DELETE method can be used with either a folder or a resource. For the delete to succeed:

- The logged in user must have read-delete, read-write-delete, or administer permission on the folder or resource.
- The resource must not be a dependency of any other resource, for example the data source of a JasperReport. In this case, you must modify or delete the other resource first.
- If the target is a folder, the above requirements must be satisfied for every resource and folder it contains, including any those contained recursively in subfolders to any level.

<table>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>DELETE</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest/resource</span>/path/to/resource/</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The resource was deleted.</p></td>
<td><p>404 Not Found – When the specified resource URI is not found in the repository</p></td>
</tr>
</tbody>
</table>
