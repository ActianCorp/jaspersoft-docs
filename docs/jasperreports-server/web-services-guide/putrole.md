---
title: putRole
description: "In putRole, the parameter role has the type WSRole and returns type WSRole. putRole updates an existing object; if the specified role does not exist, a new one is created."
---

# 1.0.1 putRole

In `putRole`, the parameter `role` has the type `WSRole` and returns type `WSRole`. `putRole` updates an existing object; if the specified role does not exist, a new one is created.

!!! note

    Before adding users and roles, note that there is a server-side configuration which specifies the default roles that a new user can receive. See JasperReports Server Administrator Guide for details.

To call `putRole`:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="language-text highlight"><pre><code>WSRole role = new WSRole();
role.setRoleName(“ROLE_ANONYMOUS”);
role.setTenantId(null);
WSRole value = binding.putRole(role);</code></pre></div></td>
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
<td><div class="language-text highlight"><pre><code>String getRoleName()
String getTenantId()
WSUser[] getUsers()
String getUserName()
String getFullName()
String getPassword()
String getEmailAddress()
Boolean getExternallyDefined()
Boolean getEnabled()
Date getPreviousPasswordChangeTime()
String getTenantId()
WSRole[] getRoles()</code></pre></div></td>
</tr>
</tbody>
</table>
