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
<td><pre class="text"><code>WSObjectPermission[] objectPermissions = binding.getPermissionsForObject(“repo:/”);</code></pre></td>
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
<td><pre class="text"><code>String getUri()
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
WSRole[] getRoles()</code></pre></td>
</tr>
</tbody>
</table>
