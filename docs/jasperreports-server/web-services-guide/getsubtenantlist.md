---
title: getSubTenantList
description: "In getSubTenantList, the parameter tenantId has the type String and returns type WSTenant."
---

# 1.0.1 getSubTenantList

In `getSubTenantList`, the parameter `tenantId` has the type `String` and returns type `WSTenant[]`.

To call `getSubTenantList`:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="language-text highlight"><pre><code>String tenantId = &quot;organization_1&quot;;</code></pre></div></td>
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
<td><div class="language-text highlight"><pre><code>String getTenantId()
String getTenantName()
String getTenantAlias()
String getTenantDesc()
String getTenantNote()
String getTenantUri()
String getTenantFolderUri()
String getParentId()</code></pre></div></td>
</tr>
</tbody>
</table>
