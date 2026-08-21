---
title: Modifying a Resource
description: "Use the PUT method above to overwrite an entire resource. Specify the path of the target resource in the URL and specify resource of the same type. Use overwrite=true to replace a resource of a..."
---

# 1.1.8 Modifying a Resource

Use the PUT method above to overwrite an entire resource. Specify the path of the target resource in the URL and specify resource of the same type. Use overwrite=true to replace a resource of a different type.

The resource descriptor must completely describe the updated resource, not use individual fields. The descriptor must also use only references for nested resources, not other resources expanded inline. You can update the local resources using the hidden folder \_file. For more informations, see Local Resources.

In JasperReports® Server 5.5, Jaspersoft® introduces a new method for modifying resoures. The PATCH method updates individual descriptor fields on the target resource. It also accept expressions that modify the descriptor in the <span href="http://docs.spring.io/spring/docs/3.0.x/reference/expressions.html">Spring Expression Language</span>. This expression language lets you easily modify the structure and values of descriptors.

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
<td><p>PATCH</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/resources</span>/path/to/resource</p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p>application/json</p></td>
<td colspan="2"><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;version&quot;</span> <span class="fu">:</span> <span class="dv">0</span><span class="fu">,</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;patch&quot;</span><span class="fu">:</span><span class="ot">[</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>        <span class="fu">{</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;field&quot;</span><span class="fu">:</span><span class="st">&quot;label&quot;</span><span class="fu">,</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;value&quot;</span><span class="fu">:</span><span class="st">&quot;New Label&quot;</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>        <span class="fu">}</span><span class="ot">,</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>        <span class="fu">{</span></span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;field&quot;</span><span class="fu">:</span><span class="st">&quot;query&quot;</span><span class="fu">,</span></span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;value&quot;</span><span class="fu">:</span><span class="st">&quot;/path/to/query/resource&quot;</span></span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>        <span class="fu">}</span><span class="ot">,</span></span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>        <span class="fu">{</span></span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;expression&quot;</span><span class="fu">:</span><span class="st">&quot;inputControls.add(new com.jaspersoft.</span></span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a><span class="st">                jasperserver.dto.resources.ClientReference().</span></span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a><span class="st">                setUri(&#39;/datatypes/decorate&#39;))&quot;</span></span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a>        <span class="fu">}</span></span>
<span id="cb1-17"><a href="#cb1-17" aria-hidden="true" tabindex="-1"></a>    <span class="ot">]</span></span>
<span id="cb1-18"><a href="#cb1-18" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
<tr>
<td colspan="2"><p>application/xml</p></td>
<td colspan="2"><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">patchItems</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">version</span>&gt;0&lt;/<span class="kw">version</span>&gt;</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">patch</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">field</span>&gt;label&lt;/<span class="kw">field</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">value</span>&gt;New Label&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">patch</span>&gt;</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">patch</span>&gt;</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">field</span>&gt;query&lt;/<span class="kw">field</span>&gt;</span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">value</span>&gt;/path/to/query/resource&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">patch</span>&gt;</span>
<span id="cb2-11"><a href="#cb2-11" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">patch</span>&gt;</span>
<span id="cb2-12"><a href="#cb2-12" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">expression</span>&gt;inputControls.add(new com.jaspersoft.</span>
<span id="cb2-13"><a href="#cb2-13" aria-hidden="true" tabindex="-1"></a>            jasperserver.dto.resources.ClientReference().</span>
<span id="cb2-14"><a href="#cb2-14" aria-hidden="true" tabindex="-1"></a>            setUri(&#39;/datatypes/decorate&#39;))</span>
<span id="cb2-15"><a href="#cb2-15" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">expression</span>&gt;</span>
<span id="cb2-16"><a href="#cb2-16" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">patch</span>&gt;</span>
<span id="cb2-17"><a href="#cb2-17" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">patchItems</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>For confirmation, the response contains the full descriptor of the resource that was just modified.</p></td>
<td><p>400 Bad Request – Mismatch between the patch fields and the fields or syntax of the actual descriptor.</p>
<p>409 Conflict – Old version number; the resource was updated more recently than the last version number received.</p></td>
</tr>
</tbody>
</table>

The patch descriptor contains attributes of the target resource. It can't be used to specify the attributes of nested resources. However, you can apply the patch operation directly to the local resource in the hidden \_files folder.

If your client does not support the PATCH method, use the POST method and specify the following HTTP header:

X-HTTP-Method-Override: PATCH
