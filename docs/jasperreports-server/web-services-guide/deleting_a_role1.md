---
title: Deleting a Role
description: "To delete a role, send the DELETE method and specify the role ID (name) in the URL."
---

# 1.0.1 Deleting a Role

To delete a role, send the DELETE method and specify the role ID (name) in the URL.

- In the community edition of the server, or commercial editions without organizations, use the first form of the URL.
- In commercial editions with organizations, use the second URL to specify the user’s organization. When specifying the organization, use its unique ID, not its path. When logged in as the system admin (`superuser`), use the first URL to delete roles of the root organization.

When this method is successful, the role is permanently deleted.

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/roles</span>/roleID</p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/organizations</span>/orgID/<span>roles</span>/roleID</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>204 No Content – The role was successfully deleted.</p></td>
<td><p>404 Not Found – When the ID of the organization cannot be resolved.</p></td>
</tr>
</tbody>
</table>
