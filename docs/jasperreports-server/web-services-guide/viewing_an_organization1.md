---
title: Viewing an Organization
description: "The GET method with an organization ID retrieves a single descriptor containing the list of properties for the organization. When you specify an organization, use its unique ID, not its path."
---

# 1.0.1 Viewing an Organization

The GET method with an organization ID retrieves a single descriptor containing the list of properties for the organization. When you specify an organization, use its unique ID, not its path.

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
<td><p>GET</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/<span>rest_v2/organizations</span>/organizationID</p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p>accept: application/xml (default)</p>
<p>accept: application/json</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The content is the descriptor for the given organization.</p></td>
<td><p>404 Not Found – When the ID does not match any organization. The content includes an error message.</p>
<p>403 Forbidden – When the logged-in user does not have permission to view the given organization</p></td>
</tr>
</tbody>
</table>

The organization descriptor is identical to the one returned when searching or listing organization, but only a single descriptor is ever returned. The following example shows the descriptor in JSON format:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;id&quot;</span><span class="fu">:</span><span class="st">&quot;Finance&quot;</span><span class="fu">,</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;alias&quot;</span><span class="fu">:</span><span class="st">&quot;Finance&quot;</span><span class="fu">,</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;parentId&quot;</span><span class="fu">:</span><span class="st">&quot;organizations&quot;</span><span class="fu">,</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;tenantName&quot;</span><span class="fu">:</span><span class="st">&quot;Finance&quot;</span><span class="fu">,</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;tenantDesc&quot;</span><span class="fu">:</span><span class="st">&quot; &quot;</span><span class="fu">,</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;tenantNote&quot;</span><span class="fu">:</span><span class="kw">null</span><span class="fu">,</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;tenantUri&quot;</span><span class="fu">:</span><span class="st">&quot;/Finance&quot;</span><span class="fu">,</span></span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;tenantFolderUri&quot;</span><span class="fu">:</span><span class="st">&quot;/organizations/Finance&quot;</span><span class="fu">,</span></span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;theme&quot;</span><span class="fu">:</span><span class="st">&quot;default&quot;</span></span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
</tbody>
</table>
