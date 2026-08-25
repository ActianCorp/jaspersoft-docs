---
title: The attribute Service
description: "The attribute service lets you view and update profile attributes, which are custom properties associated with a user. This service does not delete attributes in this release."
---

# 1.1 The attribute Service

The attribute service lets you view and update profile attributes, which are custom properties associated with a user. This service does not delete attributes in this release.

<table>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>GET</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest/attribute</span>/&lt;userID&gt;/</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The content is a descriptor for the user attributes.</p></td>
<td><p>404 Not Found – When the specified user ID is not found in the server.</p></td>
</tr>
</tbody>
</table>

The following example show the user attributes specified in an `entityResource` element:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">entityResource</span>&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">Item</span> <span class="ot">xsi:type=</span><span class="st">&quot;profileAttributeImpl&quot;</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">attrName</span>&gt;State&lt;/<span class="kw">attrName</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">attrValue</span>&gt;CA&lt;/<span class="kw">attrValue</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">Item</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">Item</span> <span class="ot">xsi:type=</span><span class="st">&quot;profileAttributeImpl&quot;</span>&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">attrName</span>&gt;Cities&lt;/<span class="kw">attrName</span>&gt;</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">attrValue</span>&gt;San Francisco, Oakland, San Jose&lt;/<span class="kw">attrValue</span>&gt;</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">Item</span>&gt;</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">entityResource</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

Use the PUT or POST methods of the attribute service to add attributes to a user. For this service, these methods are synonyms.

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
<td><p>PUT or</p>
<p>POST</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest/attribute</span>/&lt;userID&gt;/</p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p>text/plain</p></td>
<td colspan="2"><p>A well-formed descriptor that contains the attributes to add to the given user.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>201 Created</p></td>
<td><p>404 Not Found – When the user ID is not found in the server.</p></td>
</tr>
</tbody>
</table>

The DELETE on the attribute service is not implemented in this release.
