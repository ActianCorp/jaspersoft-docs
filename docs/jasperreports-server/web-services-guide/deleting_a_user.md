---
title: Deleting a User
description: Use the DELETE method of the user service to remove an existing user.
---

# 1.0.1 Deleting a User

Use the DELETE method of the user service to remove an existing user.

<table>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>DELETE</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest/user</span>/&lt;userID&gt;/</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK</p></td>
<td><p>404 Not Found – When the specified user ID is not found in the server.</p></td>
</tr>
</tbody>
</table>
