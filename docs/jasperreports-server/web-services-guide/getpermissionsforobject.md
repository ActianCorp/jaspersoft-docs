---
title: getPermissionsForObject
description: "In getPermissionsForObject, the parameter targetURI has the type String and returns type WSObjectPermission."
---

# 1.0.1 getPermissionsForObject

In `getPermissionsForObject`, the parameter `targetURI` has the type `String` and returns type `WSObjectPermission[]`.

To call `getPermissionsForObject`:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="language-text highlight"><pre><code>WSObjectPermission[] objectPermissions = binding.getPermissionsForObject(“repo:/”);</code></pre></div></td>
</tr>
</tbody>
</table>

In the return, the permissioned object can be a user or role:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="language-text highlight"><pre><code>String getUri()
Object getPermissionRecipient()
int getPermissionMask()
String getRoleName()
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
