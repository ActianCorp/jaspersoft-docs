---
title: Viewing Attributes
description: "The GET method of the attributes service retrieves the list of attributes, if any, defined for the specified entity (a user, an organization, or the server-level). For possible values of <entity> in..."
---

# 1.0.1 Viewing Attributes

The GET method of the attributes service retrieves the list of attributes, if any, defined for the specified entity (a user, an organization, or the server-level). For possible values of \<entity\> in the URL, see [1.1.2, “Entities with Attributes,” on page 1](the_v2_attributes_service.md).

There are two syntaxes; the following one is for reading multiple attributes or all attributes at once.

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/</span>&lt;entity&gt;<strong>attributes</strong>?&lt;arguments&gt;</p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><div class="language-text highlight"><pre><code>name</code></pre></div></td>
<td><p>Optional<br />
String</p></td>
<td colspan="2"><p>Specify an attribute name to list the value of that specific attribute. Repeat this argument to view multiple attributes. When this argument is omitted, all attributes and their values are returned for the given entity.</p></td>
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
<td colspan="3"><p>200 OK – The content is the list of attributes for the given entity.</p>
<p>204 No Content – The search did not return any attributes or the entity has no attributes.</p></td>
<td><p>404 Not Found – When the user ID or organization ID does not match any user or organization. The content includes an error message.</p></td>
</tr>
</tbody>
</table>

The list of attributes includes the name and value of each attribute. The following example shows user-level attributes in JSON format:

GET http://localhost:8080/jasperserver-pro/rest_v2/organizations/organzation_1/users/joeuser/attributes

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;attribute&quot;</span><span class="fu">:</span><span class="ot">[</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="fu">{</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>      <span class="dt">&quot;name&quot;</span><span class="fu">:</span> <span class="st">&quot;Attr1&quot;</span><span class="fu">,</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>      <span class="dt">&quot;value&quot;</span><span class="fu">:</span><span class="st">&quot;Value1&quot;</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span><span class="ot">,</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    <span class="er">...</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    <span class="fu">{</span></span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>      <span class="dt">&quot;name&quot;</span><span class="fu">:</span> <span class="st">&quot;AttrN&quot;</span><span class="fu">,</span></span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>      <span class="dt">&quot;value&quot;</span><span class="fu">:</span><span class="st">&quot;ValueN&quot;</span></span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span></span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>  <span class="ot">]</span></span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
</tbody>
</table>

The second syntax reads a single attribute by specifying its name in the URL:

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/</span>&lt;entity&gt;<strong>attributes</strong>/attrName</p></td>
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
<td colspan="3"><p>200 OK – The content is a single attribute for the given entity.</p></td>
<td><p>404 Not Found – When the user ID, organization ID, or attribute name does not match any user, organization, or attribute. The content includes an error message.</p></td>
</tr>
</tbody>
</table>

The response is a single attribute name-value pair. The following example shows an organization-level attribute in JSON format:

GET http://localhost:8080/jasperserver-pro/rest_v2/organizations/organization_1/attributes/Attr2

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;name&quot;</span><span class="fu">:</span> <span class="st">&quot;Attr2&quot;</span><span class="fu">,</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;value&quot;</span><span class="fu">:</span><span class="st">&quot;Value2a,Value2b,Value2c&quot;</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
</tbody>
</table>
