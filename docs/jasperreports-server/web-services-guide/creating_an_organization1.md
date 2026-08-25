---
title: Creating an Organization
description: "To create an organization, put all information in an organization descriptor, and include it in a POST request to the restv2/organizations service, with no ID specified in the URL. The organization..."
---

# 1.0.1 Creating an Organization

To create an organization, put all information in an organization descriptor, and include it in a POST request to the rest_v2/organizations service, with no ID specified in the URL. The organization is created in the organization specified by the `parentId` value of the descriptor.

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/<span>rest_v2/organizations</span>?&lt;argument&gt;</p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><div class="language-text highlight"><pre><code>createDefaultUsers</code></pre></div></td>
<td><p>Optional<br />
Boolean</p></td>
<td colspan="2"><p>Set this argument to false to suppress the creation of default users (joeuser, jasperadmin) in the new organization. When not specified, the default behavior is true and organizations are created with the standard default users.</p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p>application/xml</p>
<p>application/json</p></td>
<td colspan="2"><p>A partial or complete organization descriptor that includes the desired properties for the organization.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>201 Created – The organization was successfully created using the values in the descriptor or default values if missing.</p></td>
<td><p>404 Not Found – When the ID of the parent organization cannot be resolved.</p>
<p>400 Bad Request – When the ID or alias of the new organization is not unique on the server, or when the ID in the description contains illegal symbols. The following symbols are not allowed:</p>
<p>id and alias: <code>~!+-#$%^|</code></p>
<p>tenantName: <code>|&amp;*?&lt;&gt;/\</code></p></td>
</tr>
</tbody>
</table>

The descriptor sent in the request should contain all the properties you want to set on the new organization. Specify the `parentId` value to set the parent of the organization, not the `tenantUri` or `tenantFolderUri` properties. The following example shows the descriptor in JSON format:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;id&quot;</span><span class="fu">:</span><span class="st">&quot;Audit&quot;</span><span class="fu">,</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;alias&quot;</span><span class="fu">:</span><span class="st">&quot;Audit&quot;</span><span class="fu">,</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;parentId&quot;</span><span class="fu">:</span><span class="st">&quot;Finance&quot;</span><span class="fu">,</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;tenantName&quot;</span><span class="fu">:</span><span class="st">&quot;Audit&quot;</span><span class="fu">,</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;tenantDesc&quot;</span><span class="fu">:</span><span class="st">&quot;Audit Department of Finance&quot;</span><span class="fu">,</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;theme&quot;</span><span class="fu">:</span><span class="st">&quot;default&quot;</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
</tbody>
</table>

However, all properties have defaults or can be determined based on the alias value. The minimal descriptor necessary to create an organization is simply the alias property. In this case, the organization is created as a child of the logged-in user’s home organization. For example, if `superuser` posts the following descriptor, the server creates an organization with the name, ID, and alias of “HR” as a child of the root organization:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;alias&quot;</span><span class="fu">:</span><span class="st">&quot;HR&quot;</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
</tbody>
</table>
