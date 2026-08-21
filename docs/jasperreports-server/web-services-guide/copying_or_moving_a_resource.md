---
title: Copying or Moving a Resource
description: The POST method on the resource service also has parameters to copy or move a resource. Both folders and individual resources can be copied or moved. The ID of the resource being copied or moved must...
---

# 1.0.1 Copying or Moving a Resource

The POST method on the resource service also has parameters to copy or move a resource. Both folders and individual resources can be copied or moved. The ID of the resource being copied or moved must be unique within the destination folder, otherwise the operation will fail. This implies that copying cannot be used to duplicate a resource within the same folder.

<table>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>POST</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest/resource</span>/path/to/resource/?&lt;argument&gt;</p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p>copyTo?</p></td>
<td><p>/path/to/folder</p></td>
<td colspan="2"><p>Destination folder in the repository.</p></td>
</tr>
<tr>
<td><p>moveTo?</p></td>
<td><p>/path/to/folder</p></td>
<td colspan="2"><p>Destination folder in the repository.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK– The resource was successfully moved or copied.</p></td>
<td><p>An error if the resource cannot be moved or copied, for example if a resource with the same ID already exists in the destination folder.</p></td>
</tr>
</tbody>
</table>
