---
title: Setting Multiple Permissions
description: "The POST method assigns any number of permissions to any number of resources specified in the body of the request. All permissions must be newly assigned, and the request will fail if a recipient..."
---

# Setting Multiple Permissions

The POST method assigns any number of permissions to any number of resources specified in the body of the request. All permissions must be newly assigned, and the request will fail if a recipient already has an assigned (not inherited) permission. Use the PUT method to update assigned permissions.

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
<td><p>POST</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/permissions</span></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p>application/collection+json</p></td>
<td colspan="2"><p>A JSON object that describes a set of permissions, for example:</p>
<div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;permission&quot;</span> <span class="fu">:</span><span class="ot">[</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="fu">{</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;uri&quot;</span><span class="fu">:</span><span class="st">&quot;/properties&quot;</span><span class="fu">,</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;recipient&quot;</span><span class="fu">:</span><span class="st">&quot;role:ROLE_USER&quot;</span><span class="fu">,</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;mask&quot;</span><span class="fu">:</span><span class="st">&quot;1&quot;</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span><span class="ot">,</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    <span class="fu">{</span></span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;uri&quot;</span><span class="fu">:</span><span class="st">&quot;/properties&quot;</span><span class="fu">,</span></span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;recipient&quot;</span><span class="fu">:</span><span class="st">&quot;role:ROLE_ADMINISTRATOR&quot;</span><span class="fu">,</span></span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;mask&quot;</span><span class="fu">:</span><span class="st">&quot;32&quot;</span></span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span></span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a><span class="ot">]</span><span class="fu">}</span></span></code></pre></div></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>201 Created – The request was successful.</p></td>
<td><p>400 Bad Request – A permission is already assigned or the given permission mask is invalid.</p></td>
</tr>
</tbody>
</table>

The PUT method modifies exiting permissions (already assigned).

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/permissions</span>/path/to/resource</p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p>application/collection+json</p></td>
<td colspan="2"><p>A JSON object that describes a set of permissions. Because a single resource is specified in the URL, all permissions apply to the same resource, and the server ignores the <code>uri</code> field in the JSON object.</p>
<div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;permission&quot;</span> <span class="fu">:</span><span class="ot">[</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="fu">{</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;uri&quot;</span><span class="fu">:</span><span class="st">&quot;/foo&quot;</span><span class="fu">,</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;recipient&quot;</span><span class="fu">:</span><span class="st">&quot;role:ROLE_MANAGER|organization_1&quot;</span><span class="fu">,</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;mask&quot;</span><span class="fu">:</span><span class="st">&quot;30&quot;</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span><span class="ot">,</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    <span class="fu">{</span></span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;uri&quot;</span><span class="fu">:</span><span class="st">&quot;/bar&quot;</span><span class="fu">,</span></span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;recipient&quot;</span><span class="fu">:</span><span class="st">&quot;user:joeuser|organization_1&quot;</span><span class="fu">,</span></span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;mask&quot;</span><span class="fu">:</span><span class="st">&quot;32&quot;</span></span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span></span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a><span class="ot">]</span><span class="fu">}</span></span></code></pre></div></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The request was successful.</p></td>
<td><p>400 Bad Request – If a recipient or mask is invalid.</p>
<p>404 Not Found – If the resource in the URL is invalid.</p></td>
</tr>
</tbody>
</table>
