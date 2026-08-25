---
title: deleteRole
description: "In deleteUser, the parameter user has the type WSUser. In deleteRole, the parameter role has the type WSRole."
---

# 1.0.1 deleteRole

In `deleteUser`, the parameter `user` has the type `WSUser`. In `deleteRole`, the parameter `role` has the type `WSRole`.

Here are examples of calls to `deleteUser` and `deleteRole`:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="language-text highlight"><pre><code>WSRole role = new WSRole();
role.setRoleName(&quot;ROLE_WS&quot;);
role.setTenantId(&quot;organization_1&quot;);
binding.deleteRole(role);</code></pre></div></td>
</tr>
</tbody>
</table>

There is no return.
