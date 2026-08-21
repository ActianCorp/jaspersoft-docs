---
title: Creating an Organization
description: Use the PUT method of the organization service to create a new organization.
---

# 1.0.1 Creating an Organization

Use the PUT method of the organization service to create a new organization.

<table>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>PUT</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/<span>rest/organization</span>/</p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p>text/plain</p></td>
<td colspan="2"><p>A well-formed <code>tenant</code> descriptor that accurately describes the desired organization.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>201 Created</p></td>
<td><p>404 Not Found – When the parent organization ID in the descriptor is not found in the server.</p></td>
</tr>
</tbody>
</table>
