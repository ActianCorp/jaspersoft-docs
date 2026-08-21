---
title: Setting Permissions
description: "PUT is implemented as a synonym of POST for the permission service. Both will create an explicit permission for a given role or user on a resource, overriding the previous explicit permission for the..."
---

# 1.0.1 Setting Permissions

PUT is implemented as a synonym of POST for the permission service. Both will create an explicit permission for a given role or user on a resource, overriding the previous explicit permission for the same role or user. To set a permission use either method and include the permission descriptors (`objectPermissionImpl`) such as those returned by the GET method.

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
<td><p>PUT or</p>
<p>POST</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest/permission</span>/path/to/resource/</p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p>text/plain</p></td>
<td colspan="2"><p>A well-formed XML entityResource that defines the permissions you want to set.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Value on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK</p></td>
<td><p>404 Not Found – When the specified resource URI is not found in the repository.</p></td>
</tr>
</tbody>
</table>

Setting a permission creates an explicit permission for the given user or role. To reset the inherited permission value, remove the explicit permission with the DELETE method. This method does not take a permission descriptor, instead specify the roles and users to reset to the inherited permission as parameters.

<table>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>DELETE</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest/permission</span>/path/to/resource/?&lt;argument&gt;</p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p>roles</p></td>
<td><p>String</p></td>
<td colspan="2"><p>A comma-separated list of role names. The access permission for the specified roles will revert to the resource’s inherited permission for those roles.</p></td>
</tr>
<tr>
<td><p>users</p></td>
<td><p>String</p></td>
<td colspan="2"><p>A comma-separated list of user IDs. The access permission for the specified users will revert to the resource’s inherited permission for those users.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK</p></td>
<td><p>404 Not Found – When the specified resource URI is not found in the repository.</p></td>
</tr>
</tbody>
</table>
