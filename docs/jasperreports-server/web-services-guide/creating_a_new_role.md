---
title: Creating a New Role
description: "Use the PUT method of the role service to create a new role. In commercial editions, specify the role’s organization in the tenantID element of the role descriptor."
---

# 1.0.1 Creating a New Role

Use the PUT method of the role service to create a new role. In commercial editions, specify the role’s organization in the `tenantID` element of the `role` descriptor.

<table>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>PUT</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest/role</span>/</p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p>text/plain</p></td>
<td colspan="2"><p>A well-formed <code>role</code> descriptor that describes the properties of the desired role.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>201 Created</p></td>
<td><p>404 Not Found – When the organization ID in the descriptor is not found in the server.</p></td>
</tr>
</tbody>
</table>
