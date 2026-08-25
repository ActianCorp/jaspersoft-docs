---
title: Viewing Permissions
description: "The GET method retrieves the permissions defined on a resource, including both user-based and role-based permissions."
---

# 1.0.1 Viewing Permissions

The GET method retrieves the permissions defined on a resource, including both user-based and role-based permissions.

<table>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>GET</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest/permission</span>/path/to/resource/</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The body is XML that describes all permissions for the resource.</p></td>
<td><p>404 Not Found – When the specified resource URI is not found in the repository.</p></td>
</tr>
</tbody>
</table>

The permissions for each user and each role are indicated by the following values. These values are not a true mask; they should be treated as constants:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td><ul>
<li>No access: 0</li>
</ul></td>
<td><ul>
<li>Read-delete: 18</li>
</ul></td>
</tr>
<tr>
<td><ul>
<li>Administer: 1</li>
</ul></td>
<td><ul>
<li>Read-write-delete: 30</li>
</ul></td>
</tr>
<tr>
<td><ul>
<li>Read-only: 2</li>
</ul></td>
<td><ul>
<li>Execute-only: 32</li>
</ul></td>
</tr>
</tbody>
</table>

The response to the GET request is an `entityResource` that defines each permission on the resource. Permissions for roles or users that are not specified are inherited from their parent folder:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">entityResource</span>&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">Item</span> <span class="ot">xsi:type=</span><span class="st">&quot;objectPermissionImpl&quot;</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">permissionMask</span>&gt;2&lt;/<span class="kw">permissionMask</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">permissionRecipient</span> <span class="ot">xsi:type=</span><span class="st">&quot;roleImpl&quot;</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">externallyDefined</span>&gt;false&lt;/<span class="kw">externallyDefined</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">roleName</span>&gt;ROLE_USER&lt;/<span class="kw">roleName</span>&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">permissionRecipient</span>&gt;</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">URI</span>&gt;repo:/path/to/resource&lt;/<span class="kw">URI</span>&gt;</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">Item</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">Item</span> <span class="ot">xsi:type=</span><span class="st">&quot;objectPermissionImpl&quot;</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">permissionMask</span>&gt;30&lt;/<span class="kw">permissionMask</span>&gt;</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">permissionRecipient</span> <span class="ot">xsi:type=</span><span class="st">&quot;roleImpl&quot;</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">externallyDefined</span>&gt;false&lt;/<span class="kw">externallyDefined</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">roleName</span>&gt;ROLE_DEMO&lt;/<span class="kw">roleName</span>&gt;</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">permissionRecipient</span>&gt;</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">URI</span>&gt;repo:/path/to/resource&lt;/<span class="kw">URI</span>&gt;</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">Item</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td><div class="sourceCode" id="cb3"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">Item</span> <span class="ot">xsi:type=</span><span class="st">&quot;objectPermissionImpl&quot;</span>&gt;</span>
<span id="cb3-2"><a href="#cb3-2" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">permissionMask</span>&gt;30&lt;/<span class="kw">permissionMask</span>&gt;</span>
<span id="cb3-3"><a href="#cb3-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">permissionRecipient</span> <span class="ot">xsi:type=</span><span class="st">&quot;userImpl&quot;</span>&gt;</span>
<span id="cb3-4"><a href="#cb3-4" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">externallyDefined</span>&gt;false&lt;/<span class="kw">externallyDefined</span>&gt;</span>
<span id="cb3-5"><a href="#cb3-5" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">fullName</span>&gt;California User&lt;/<span class="kw">fullName</span>&gt;</span>
<span id="cb3-6"><a href="#cb3-6" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">tenantId</span>&gt;organization_1&lt;/<span class="kw">tenantId</span>&gt;</span>
<span id="cb3-7"><a href="#cb3-7" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">username</span>&gt;CaliforniaUser&lt;/<span class="kw">username</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td><div class="language-text highlight"><pre><code>    &lt;/permissionRecipient&gt;
    &lt;URI&gt;repo:/path/to/resource&lt;/URI&gt;
  &lt;/Item&gt;</code></pre></div></td>
</tr>
<tr>
<td><div class="sourceCode" id="cb5"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb5-1"><a href="#cb5-1" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">Item</span> <span class="ot">xsi:type=</span><span class="st">&quot;objectPermissionImpl&quot;</span>&gt;</span>
<span id="cb5-2"><a href="#cb5-2" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">permissionMask</span>&gt;30&lt;/<span class="kw">permissionMask</span>&gt;</span>
<span id="cb5-3"><a href="#cb5-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">permissionRecipient</span> <span class="ot">xsi:type=</span><span class="st">&quot;userImpl&quot;</span>&gt;</span>
<span id="cb5-4"><a href="#cb5-4" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">externallyDefined</span>&gt;false&lt;/<span class="kw">externallyDefined</span>&gt;</span>
<span id="cb5-5"><a href="#cb5-5" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">fullName</span>&gt;Joe User&lt;/<span class="kw">fullName</span>&gt;</span>
<span id="cb5-6"><a href="#cb5-6" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">tenantId</span>&gt;organization_1&lt;/<span class="kw">tenantId</span>&gt;</span>
<span id="cb5-7"><a href="#cb5-7" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">username</span>&gt;joeuser&lt;/<span class="kw">username</span>&gt;</span>
<span id="cb5-8"><a href="#cb5-8" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">permissionRecipient</span>&gt;</span>
<span id="cb5-9"><a href="#cb5-9" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">URI</span>&gt;repo:/path/to/resource&lt;/<span class="kw">URI</span>&gt;</span>
<span id="cb5-10"><a href="#cb5-10" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">Item</span>&gt;</span>
<span id="cb5-11"><a href="#cb5-11" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">entityResource</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>
