---
title: Setting Attributes
description: "The PUT method of the attributes service adds or replaces attributes on the specified entity (a user, an organization, or the server-level). For possible values of &lt;entity&gt; in the URL, see..."
---

# 1.0.1 Setting Attributes

The PUT method of the attributes service adds or replaces attributes on the specified entity (a user, an organization, or the server-level). For possible values of &lt;entity&gt; in the URL, see [1.1.2, “Entities with Attributes,” on page 1](the_v2_attributes_service.md).

There are two syntaxes; the following one is for adding or replacing all attributes at once.

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/</span>&lt;entity&gt;<strong>attributes</strong></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p>application/xml</p>
<p>application/json</p></td>
<td colspan="2"><p>An attribute descriptor that includes the new list of attributes. All previously defined attributes are replaced by this new list.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>201 Created – When the attributes were successfully created on the given entity.</p>
<p>200 OK – When the attributes were successfully updated.</p></td>
<td><p>404 Not Found – When the user ID or organization ID does not match any user or organization. The content includes an error message.</p>
<p>400 Bad Request – When an attribute name or value is null, blank, or too long (see <a href="the_v2_attributes_service.md">1.1.5, “Attribute Limitations,” on page 1</a>). If one attribute causes an error, the operation stops and returns an error, but attributes that were already set remain.</p></td>
</tr>
</tbody>
</table>

The following example shows how to set all attributes on an organization. The list of attributes in JSON format defines the name and value of each attribute.

PUT http://localhost:8080/jasperserver-pro/rest_v2/organizations/organization_1/attributes

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
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>      <span class="dt">&quot;value&quot;</span><span class="fu">:</span><span class="st">&quot;newValue1&quot;</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span><span class="ot">,</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    <span class="fu">{</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>      <span class="dt">&quot;name&quot;</span><span class="fu">:</span> <span class="st">&quot;Attr2&quot;</span><span class="fu">,</span></span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>      <span class="dt">&quot;value&quot;</span><span class="fu">:</span><span class="st">&quot;newValue2a, newValue2b&quot;</span></span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span><span class="ot">,</span></span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>    <span class="fu">{</span></span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>      <span class="dt">&quot;name&quot;</span><span class="fu">:</span> <span class="st">&quot;Attr3&quot;</span></span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>      <span class="st">&quot;value&quot;</span><span class="er">:</span> <span class="st">&quot;SecureValue3&quot;</span></span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>      <span class="st">&quot;secure&quot;</span><span class="er">:</span> <span class="st">&quot;true&quot;</span></span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span></span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a>  <span class="ot">]</span></span>
<span id="cb1-17"><a href="#cb1-17" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
</tbody>
</table>

The second syntax of the PUT attributes method is for adding or replacing individual attributes.

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/</span>&lt;entity&gt;<strong>attributes</strong>/attrName</p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p>application/xml</p>
<p>application/json</p></td>
<td colspan="2"><p>A single attribute name-value pair. The attribute name must match the <span>attrName</span> exactly as it appears in the URL. If this attribute name already exists on the specified user, this attribute’s value is updated. If the attribute does not exist, it is added to the user’s list of attributes.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>201 Created – When the attribute was successfully created on the given entity.</p>
<p>200 OK – When the attribute was successfully updated.</p></td>
<td><p>404 Not Found – When the user ID or organization ID does not match any user or organization. The content includes an error message.</p></td>
</tr>
</tbody>
</table>

The content in the request is a single attribute, for example:

PUT http://localhost:8080/jasperserver-pro/rest_v2/organizations/organization_1/users/<br>
joeuser/attributes/Attr2

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;name&quot;</span><span class="fu">:</span> <span class="st">&quot;Attr2&quot;</span><span class="fu">,</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;value&quot;</span><span class="fu">:</span><span class="st">&quot;NewValue2&quot;</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
</tbody>
</table>
