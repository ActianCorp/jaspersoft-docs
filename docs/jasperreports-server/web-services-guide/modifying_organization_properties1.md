---
title: Modifying Organization Properties
description: "To modify the properties of an organization, use the PUT method and specify the organization ID in the URL. The request must include an organization descriptor with the values you want to change. You..."
---

# 1.0.1 Modifying Organization Properties

To modify the properties of an organization, use the PUT method and specify the organization ID in the URL. The request must include an organization descriptor with the values you want to change. You cannot change the ID of an organization, only its name (used for display) and its alias (used for logging in).

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>PUT</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/<span>rest_v2/organizations</span>/organizationID/</p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p>application/xml</p>
<p>application/json</p></td>
<td colspan="2"><p>A partial organization descriptor that includes the properties to change. Do not specify the following properties:</p>
<ul>
<li><code>id </code>– The organization ID is permanent and can never be modified.</li>
<li><code>parentId</code> – Organizations cannot change parents.</li>
<li><span>tenantUri</span> – Organizations cannot change the organization hierarchy.</li>
<li><span>tenantFolderUri</span> – The organization folder is automatically based on its parent, which cannot be changed.</li>
</ul></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The organization was successfully updated.</p></td>
<td><p>400 Bad Request – When some dependent resources cannot be resolved.</p></td>
</tr>
</tbody>
</table>

The following example shows a descriptor sent to update the name and description of an organization:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;tenantName&quot;</span><span class="fu">:</span><span class="st">&quot;Audit Dept&quot;</span><span class="fu">,</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;tenantDesc&quot;</span><span class="fu">:</span><span class="st">&quot;Audit Department of Finance Division&quot;</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
</tbody>
</table>
