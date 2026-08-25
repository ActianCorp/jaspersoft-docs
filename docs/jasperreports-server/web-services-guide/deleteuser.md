---
title: deleteUser
description: "In deleteUser, the parameter user has the type WSUser."
---

# 1.0.1 deleteUser

In `deleteUser`, the parameter `user` has the type `WSUser`.

To call `deleteUser`:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="language-text highlight"><pre><code>WSUser user = new WSUser();
user.setUsername(&quot;john&quot;);
user.setTenantId(&quot;organization_1&quot;);
binding.deleteUser(user);</code></pre></div></td>
</tr>
</tbody>
</table>

There is no return.
