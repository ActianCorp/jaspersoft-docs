---
title: updateRoleName
description: "In updateRoleName, the parameter oldRole has the type WSRole, and the parameter newName has the type String. They both return type WSRole."
---

# 1.0.1 updateRoleName

In `updateRoleName`, the parameter `oldRole` has the type `WSRole`, and the parameter `newName` has the type `String`. They both return type `WSRole`.

To update a role with a call to `oldRole`:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="language-text highlight"><pre><code>WSRole oldRole= new WSRole();
role.setRoleName(&quot;ROLE_WS&quot;);
role.setTenantId(&quot;organization_1&quot;);
WSRole value = binding.updateRoleName(oldRole, “ROLE_WEB_SERVICE”);</code></pre></div></td>
</tr>
</tbody>
</table>

To rename the role with a call to `newName`: `"ROLE_WEB_SERVICE". `The return for an updated role:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="language-text highlight"><pre><code>String getRoleName()
String getTenantId()
WSUser[] getUsers()
String getUsername()
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
