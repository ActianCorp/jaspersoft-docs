---
title: Modifying a Role
description: "To change the name of a role, send a PUT request to the restv2/roles service and specify the new name in the role descriptor."
---

# 1.0.1 Modifying a Role

To change the name of a role, send a PUT request to the rest_v2/roles service and specify the new name in the role descriptor.

-   In the community edition of the server, or commercial editions without organizations, use the first form of the URL.
-   In commercial editions with organizations, use the second URL to specify the user’s organization. When specifying the organization, use its unique ID, not its path. When logged in as the system admin (`superuser`), use the first URL to modify roles in the root organization.

The only property of a role that you can modify is the role’s name. After the update, all members of the role are members of the new role name, and all permissions associated with the old role name are updated to the new role name.

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/roles</span>/roleID</p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/organizations</span>/orgID/<span>roles</span>/roleID</p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p>application/xml</p>
<p>application/json</p></td>
<td colspan="2"><p>A role descriptor containing a single property:</p>
<ul>
<li><code>name</code> – The new name for the role.</li>
</ul></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The role was successfully updated. The response contains the full descriptor of the updated role.</p></td>
<td><p>404 Not Found – When the organization ID cannot be resolved.</p></td>
</tr>
</tbody>
</table>
