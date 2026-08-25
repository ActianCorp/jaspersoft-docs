---
title: deletePermission
description: "In deletePermission, the parameter objPerm has the type WSObjectPermission. To call deletePermission:"
---

# 1.0.1 deletePermission

In `deletePermission`, the parameter `objPerm` has the type `WSObjectPermission`. To call `deletePermission`:

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
binding.deletePermission(objectPermission);</code></pre></div></td>
</tr>
</tbody>
</table>

There is no return.
