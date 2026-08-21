---
title: findRoles
description: "In findRoles, the parameter criteria has the type WSRoleSearchCriteria and returns type WSRole."
---

# 1.0.1 findRoles

In `findRoles`, the parameter `criteria` has the type `WSRoleSearchCriteria` and returns type `WSRole`.

`criteria` can be a rolename mask, an organization/tenant ID, `includeSubOrgs`, a list of required users or roles, and `maxRecords`. Null values indicate "any."

- The mask has a SQL-like notation. For instance, `Ad%`, `U2_`.
- When `includeSubOrgs` is TRUE, all objects of the specified type are within a search’s scope and result. Otherwise, only objects in the requested organization (or root if `tenantId`=null) are searched.
- To limit the number of objects to return, set `maxRecords` to the desired number. To allow an infinite number of objects, set `maxRecords` to 0.

To call `findRoles`:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><pre class="text"><code>WSRoleSearchCriteria searchCriteria = new WSRoleSearchCriteria();
  searchCriteria.setRoleName(“ROLE_USER”);
  searchCriteria.setTenantId(“organization_1”);
  searchCriteria.setMaxRecords(5);
  searchCriteria.setIncludeSubOrgs(false);
WSRole[] list = binding.findRoles(searchCriteria);</code></pre></td>
</tr>
</tbody>
</table>

The return is:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><pre class="text"><code>String getUsername()
String getFullName()
String getPassword()
String getEmailAddress()
Boolean getExternallyDefined()
Boolean getEnabled()
Date getPreviousPasswordChangeTime()
String getTenantId()
WSRole[] getRoles()
String getRoleName()
String getTenantId()
WSUser[] getUsers()</code></pre></td>
</tr>
</tbody>
</table>
