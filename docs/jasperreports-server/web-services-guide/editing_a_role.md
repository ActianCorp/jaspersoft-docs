---
title: Editing a Role
description: Use the POST method of the role service to update the properties of an existing role.
---

# 1.0.1 Editing a Role

Use the POST method of the role service to update the properties of an existing role.

<table>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>POST</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest/role</span>/&lt;roleName&gt;/</p></td>
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
<td colspan="3"><p>200 OK</p></td>
<td><p>404 Not Found – When the roleName is not found in the server.</p></td>
</tr>
</tbody>
</table>
