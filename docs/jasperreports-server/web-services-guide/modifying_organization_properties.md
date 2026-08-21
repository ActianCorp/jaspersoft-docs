---
title: Modifying Organization Properties
description: Use the POST method of the organization service to update the properties of an existing organization.
---

# 1.0.1 Modifying Organization Properties

Use the POST method of the organization service to update the properties of an existing organization.

<table>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>POST</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/<span>rest/organization</span>/organizationID/</p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p>text/plain</p></td>
<td colspan="2"><p>A well-formed <code>tenant</code> descriptor with updated property values for the desired organization.</p></td>
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

As with organizations managed in the user interface, only certain fields may be modified in the tenant descriptor:

- `alias` – Can be used for logging in, but must be unique among all organization aliases.
- `tenantDesc` – Description of the organization, visible only to administrators.
- `tenantName` – Display name of the organization, appearing to users on the organization’s root folder.
- `theme` – The user interface theme that is active for all organization users.
