---
title: putPermission
description: "In putPermission, the parameter objPerm has the type WSObjectPermission and returns type WSObjectPermission."
---

# 1.0.1 putPermission

In `putPermission`, the parameter `objPerm` has the type `WSObjectPermission` and returns type `WSObjectPermission`.

To call `putPermission`:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="language-text highlight"><pre><code>WSObjectPermission objectPermission = new WSObjectPermission();
objectPermission.setUri(resourceUri);
objectPermission.setPermissionMask(2);
WSUser wsUser = new WSUser();
wsUser.setUsername(&quot;joeuser&quot;);
wsUser.setTenantId(&quot;organization_1&quot;);
objectPermission.setPermissionRecipient(wsUser);
WSObjectPermission value = binding.putPermission(objectPermission);</code></pre></div></td>
</tr>
</tbody>
</table>

The setPermissionMask() function accepts the following values. It is not a true mask because bit-wise combinations of these values are not supported by the server. These values should be treated as constants:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td><ul>
<li>No access: 0</li>
</ul></td>
<td><ul>
<li>Read-delete: 18</li>
</ul></td>
</tr>
<tr>
<td><ul>
<li>Administer: 1</li>
</ul></td>
<td><ul>
<li>Read-write-delete: 30</li>
</ul></td>
</tr>
<tr>
<td><ul>
<li>Read-only: 2</li>
</ul></td>
<td><ul>
<li>Execute-only: 32</li>
</ul></td>
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
