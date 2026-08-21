---
title: putUser
description: "In putUser, the parameter user has the type WSUser and returns type WSUser."
---

# 1.0.1 putUser

In `putUser`, the parameter `user` has the type `WSUser` and returns type `WSUser`.

`putUser` updates an existing object; if the specified user does not exist, a new one is created.

!!! note

    Before adding users and roles, note that there is a server-side configuration which specifies the default roles that a new user can receive. See the JasperReports Server Administrator Guide for details

To call `putUser`:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><pre class="text"><code>WSUser user = new WSUser();
user.setUsername(&quot;john&quot;);
user.setTenantId(&quot;organization_1&quot;);
user.setEnabled(true);
user.setFullName(&quot;John Doe&quot;);
WSRole role = new WSRole();
role.setRoleName(&quot;ROLE_ANONYMOUS&quot;);
role.setTenantId(null);
user.setRoles(new WSRole[] {role});
WSUser value = binding.putUser(user);</code></pre></td>
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
