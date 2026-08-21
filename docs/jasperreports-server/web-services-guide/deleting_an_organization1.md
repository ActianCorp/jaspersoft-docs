---
title: Deleting an Organization
description: "To delete an organization, use the DELETE method and specify the organization ID in the URL. When deleting an organization, all of its resources in the repository, all of its sub-organizations, all..."
---

# 1.0.1 Deleting an Organization

To delete an organization, use the DELETE method and specify the organization ID in the URL. When deleting an organization, all of its resources in the repository, all of its sub-organizations, all of its users, and all of its roles are permanently deleted.

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/<span>rest_v2/organizations</span>/organizationID/</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>204 No Content – The organization was successfully deleted.</p></td>
<td><p>400 Bad Request – When attempting to delete the organization of the logged-in user.</p>
<p>404 Not Found – When the ID of the organization cannot be resolved.</p></td>
</tr>
</tbody>
</table>
