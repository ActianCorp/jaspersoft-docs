---
title: Deleting a Role
description: Use the DELETE method of the role service to remove an existing role.
---

# 1.0.1 Deleting a Role

Use the DELETE method of the role service to remove an existing role.

<table>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>DELETE</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest/role</span>/&lt;roleName&gt;/</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK</p></td>
<td><p>404 Not Found – When the specified role is not found in the server.</p></td>
</tr>
</tbody>
</table>
