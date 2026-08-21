---
title: Searching for Organizations
description: "The GET method without any organization ID searches for organizations by ID, alias, or display name. If no search is specified, it returns a list of all organizations. Searches and listings start..."
---

# 1.0.1 Searching for Organizations

The GET method without any organization ID searches for organizations by ID, alias, or display name. If no search is specified, it returns a list of all organizations. Searches and listings start from but do not include the logged-in user’s organization or the specified base (`rootTenantId`).

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/<span>rest_v2/organizations</span>?&lt;arguments&gt;</p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><pre class="text"><code>q</code></pre></td>
<td><p>Optional<br />
String</p></td>
<td colspan="2"><p>Specify a string or substring to match the organization ID, alias, or name of any organization. The search is not case sensitive. Only the matching organizations are returned in the results, regardless of their hierarchy.</p></td>
</tr>
<tr>
<td><pre class="text"><code>includeParents</code></pre></td>
<td><p>Optional<br />
Boolean</p></td>
<td colspan="2"><p>When used with a search, the result will include the parent hierarchy of each matching organization. When not specified, this argument is false by default.</p></td>
</tr>
<tr>
<td><pre class="text"><code>rootTenantId</code></pre></td>
<td><p>Optional<br />
String</p></td>
<td colspan="2"><p>Specifies an organization ID as a base for searching and listing child organizations. The base is not included in the results. Regardless of this base, the <code>tenantFolderURI</code> values in the result are always relative to the logged-in user’s organization. When not specified, the default base is the logged-in user’s organization.</p></td>
</tr>
<tr>
<td><pre class="text"><code>sortBy</code></pre></td>
<td><p>Optional<br />
String</p></td>
<td colspan="2"><p>Specifies a sort order for results. When not specified, lists of organizations are in the order that they were created. The possible values are:</p>
<p>name - Sort results alphabetically by organization name.</p>
<p>alias - Sort results alphabetically by organization alias.</p>
<p>id - Sort results alphabetically by organization ID.</p></td>
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
<td colspan="3"><p>200 OK – The content is a set of descriptors for all organizations in the result.</p>
<p>204 No Content – The search did not return any organizations.</p></td>
<td></td>
</tr>
</tbody>
</table>

The following example shows a search for an organization and its parent hierarchy:

GET http://localhost:8080/jasperserver-pro/rest_v2/organizations?q=acc&includeParents=true

This request has the following response, as viewed by superuser at the root of the organization hierarchy:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">organizations</span>&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">organization</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">alias</span>&gt;Finance&lt;/<span class="kw">alias</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">id</span>&gt;Finance&lt;/<span class="kw">id</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">parentId</span>&gt;organizations&lt;/<span class="kw">parentId</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">tenantDesc</span>&gt;&lt;/<span class="kw">tenantDesc</span>&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">tenantFolderUri</span>&gt;/organizations/Finance&lt;/<span class="kw">tenantFolderUri</span>&gt;</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">tenantName</span>&gt;Finance&lt;/<span class="kw">tenantName</span>&gt;</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">tenantUri</span>&gt;/Finance&lt;/<span class="kw">tenantUri</span>&gt;</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">theme</span>&gt;default&lt;/<span class="kw">theme</span>&gt;</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">organization</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">organization</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">alias</span>&gt;Accounts&lt;/<span class="kw">alias</span>&gt;</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">id</span>&gt;Accounts&lt;/<span class="kw">id</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">parentId</span>&gt;Finance&lt;/<span class="kw">parentId</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">tenantDesc</span>&gt;&lt;/<span class="kw">tenantDesc</span>&gt;</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">tenantFolderUri</span>&gt;/organizations/Finance/organizations/Accounts&lt;/<span class="kw">tenantFolderUri</span>&gt;</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">tenantName</span>&gt;Accounts&lt;/<span class="kw">tenantName</span>&gt;</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">tenantUri</span>&gt;/Finance/Accounts&lt;/<span class="kw">tenantUri</span>&gt;</span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">theme</span>&gt;default&lt;/<span class="kw">theme</span>&gt;</span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">organization</span>&gt;</span>
<span id="cb2-11"><a href="#cb2-11" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">organizations</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>
