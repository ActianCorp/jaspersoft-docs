---
title: Creating a Role
description: "To create a role, send the PUT request to the restv2/roles service with the intended role ID (name) specified in the URL."
---

# 1.0.1 Creating a Role

To create a role, send the PUT request to the rest_v2/roles service with the intended role ID (name) specified in the URL.

-   In the community edition of the server, or commercial editions without organizations, use the first form of the URL.
-   In commercial editions with organizations, use the second URL to specify the user’s organization. When specifying the organization, use its unique ID, not its path. When logged in as the system admin (`superuser`), use the first URL to create roles in the root organization.

Roles do not have any properties to specify other than the role ID, but the request must include a descriptor that can be empty.

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
<td colspan="2"><p>An empty role descriptor, either &lt;role&gt;&lt;/role&gt; or. Do <span>not</span> specify the following properties:</p>
<ul>
<li><code>name</code> – Specified in the URL and should not be modified in the descriptor.</li>
<li><code>tenantID</code> – Specified in the URL and cannot be modified in the descriptor.</li>
<li><code>externallyDefined</code> – Computed automatically by the server.</li>
</ul></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>201 Created – The role was successfully created. The response contains the full descriptor of the new role.</p></td>
<td><p>404 Not Found – When the organization ID cannot be resolved.</p></td>
</tr>
</tbody>
</table>
