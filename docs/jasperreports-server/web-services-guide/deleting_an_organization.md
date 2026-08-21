---
title: Deleting an Organization
description: Use the DELETE method of the organization service to remove an existing organization.
---

# 1.0.1 Deleting an Organization

Use the DELETE method of the organization service to remove an existing organization.

<table>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>DELETE</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/<span>rest/organization</span>/organizationID/</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK</p></td>
<td><p>404 Not Found – When the organization ID is not found in the server.</p></td>
</tr>
</tbody>
</table>

Deleting an organization removes all of its users, roles, and all of its suborganizations recursively.
