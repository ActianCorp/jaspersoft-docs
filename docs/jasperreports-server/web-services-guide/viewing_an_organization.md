---
title: Viewing an Organization
description: "The GET method retrieves information about an organization and optionally its child organizations. To specify an organization, use its ID, not its path."
---

# 1.0.1 Viewing an Organization

The GET method retrieves information about an organization and optionally its child organizations. To specify an organization, use its ID, not its path.

<table>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>GET</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/<span>rest/organization</span>/organizationID?&lt;arguments&gt;</p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p>listSubOrgs?</p></td>
<td><p>Boolean</p></td>
<td colspan="2"><p>When this argument is omitted or is false, only the specified organization is returned. When true only the suborganizations are returned.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The content is a descriptor for the organization or its suborganizations.</p></td>
<td><p>404 Not Found – When the specified organization ID is not found in the server.</p></td>
</tr>
</tbody>
</table>

When the `listSubOrgs` argument is omitted or false, the GET method returns a single `tenant` descriptor for the given organization:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">tenant</span>&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">alias</span>&gt;organization_1&lt;/<span class="kw">alias</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">id</span>&gt;organization_1&lt;/<span class="kw">id</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">parentId</span>&gt;organizations&lt;/<span class="kw">parentId</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">tenantDesc</span>&gt; &lt;/<span class="kw">tenantDesc</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">tenantFolderUri</span>&gt;/organizations/organization_1&lt;/<span class="kw">tenantFolderUri</span>&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">tenantName</span>&gt;Organization&lt;/<span class="kw">tenantName</span>&gt;</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">tenantNote</span>&gt; &lt;/<span class="kw">tenantNote</span>&gt;</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">tenantUri</span>&gt;/organization_1&lt;/<span class="kw">tenantUri</span>&gt;</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">theme</span>&gt;default&lt;/<span class="kw">theme</span>&gt;</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">tenant</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

!!! note

    The tenantFolderURI is always relative to the user ID that authenticated the request. In these two examples, the user ID is superuser.

When the `listSubOrgs` argument is true, the GET method returns a list of tenant descriptors. If the given organization has no suborganizations, the list is empty.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">tenantsList</span>&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">tenant</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">alias</span>&gt;SubOrganization&lt;/<span class="kw">alias</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">id</span>&gt;SubOrganization&lt;/<span class="kw">id</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">parentId</span>&gt;organization_1&lt;/<span class="kw">parentId</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">tenantDesc</span>&gt;My SubOrganization&lt;/<span class="kw">tenantDesc</span>&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">tenantFolderUri</span>&gt;/organizations/organization_1/organizations/SubOrganization</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>      &lt;/<span class="kw">tenantFolderUri</span>&gt;</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">tenantName</span>&gt;SubOrganization&lt;/<span class="kw">tenantName</span>&gt;</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">tenantUri</span>&gt;/organization_1/SubOrganization&lt;/<span class="kw">tenantUri</span>&gt;</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">theme</span>&gt;default&lt;/<span class="kw">theme</span>&gt;</span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">tenant</span>&gt;</span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">tenantsList</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>
