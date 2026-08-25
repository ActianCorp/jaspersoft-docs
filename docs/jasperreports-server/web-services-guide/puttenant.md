---
title: putTenant
description: "In putTenant, the parameter tenant has the type WSTenant and returns type WSTenant."
---

# 1.0.1 putTenant

In `putTenant`, the parameter `tenant` has the type `WSTenant` and returns type `WSTenant`.

To call `putTenant`. Note that `tenantUri` and `tenantFolderUri` are calculated automatically from the tenant’s `tenantId` and `parentId`. As a result, the `tenantUri` and `tenantFolderUri` fields of the `WSTenant` object are ignored:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="language-text highlight"><pre><code>WSTenant wsTenant = new WSTenant();
  wsTenant.setTenantId(&quot;suborg1&quot;);
  wsTenant.setParentId(&quot;organization_1&quot;);
  wsTenant.setTenantAlias(&quot;organization_1&quot;);
  wsTenant.setTenantName(&quot;Sub organization1&quot;);
  wsTenant.setTenantDesc(&quot;Sub organization1 description&quot;);
  wsTenant.setTenantNote(&quot;Sub organization notes&quot;);</code></pre></div></td>
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
String getTenantAlias()</code></pre></div></td>
</tr>
<tr>
<td><div class="language-text highlight"><pre><code>String getTenantDesc()
String getTenantNote()
String getTenantUri()
String getTenantFolderUri()
String getParentId()</code></pre></div></td>
</tr>
</tbody>
</table>
