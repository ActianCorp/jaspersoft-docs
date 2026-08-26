---
title: findUsers
description: "In findUsers, the parameter criteria has the type WSUserSearchCriteria and returns type WSUser. criteria can be a username mask, an organization/tenant ID, includeSubOrgs, a list of required users,..."
---

# 1.0.1 findUsers

In `findUsers`, the parameter `criteria` has the type `WSUserSearchCriteria` and returns type `WSUser`. `criteria` can be a username mask, an organization/tenant ID, `includeSubOrgs`, a list of required users, and `maxRecords`. Null values indicate "any."

-   The mask has an SQL-like notation. For instance, `U2_`.
-   When `includeSubOrgs` is TRUE, all objects of the specified type are within a search’s scope and result. Otherwise, only objects in the requested organization (or root if `tenantId`=null) are searched.
-   To limit the number of objects to return, set `maxRecords` to the desired number. To allow an infinite number of objects, set `maxRecords` to 0.

To call `findUsers`:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="language-text highlight"><pre><code>WSUserSearchCriteria searchCriteria = new WSUserSearchCriteria();
  searchCriteria.setName(“demo”);
  searchCriteria.setTenantId(“organization_1”); // Name of orga  nization or null
  searchCriteria.setMaxRecords(5);
  searchCriteria.setIncludeSubOrgs(false);
  searchCriteria.setRequiredRoles(requiredRoles);
WSRole role = new WSRole();
role.setRoleName(&quot;ROLE_USER&quot;);
role.setTenantId(null);
searchCriteria.setRequiredRoles(new WSRole[] {role});
WSUser[] list = binding.findUsers(searchCriteria);</code></pre></div></td>
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
<td><div class="language-text highlight"><pre><code>String getUsername()
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
WSUser[] getUsers()</code></pre></div></td>
</tr>
</tbody>
</table>
