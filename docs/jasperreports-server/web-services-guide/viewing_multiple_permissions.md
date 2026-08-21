---
title: Viewing Multiple Permissions
description: The GET method of the v2/permissions service lists permissions on a given resource according to several arguments.
---

# Viewing Multiple Permissions

The GET method of the v2/permissions service lists permissions on a given resource according to several arguments.

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/permissions</span>/path/to/resource/?&lt;arguments&gt;</p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p>effective<br />
Permissions</p></td>
<td><p>boolean<br />
optional</p></td>
<td colspan="2"><p>When set to true, the effective permissions are returned. By default, this argument is false and only assigned permissions are returned.</p></td>
</tr>
<tr>
<td><p>recipientType</p></td>
<td><p>String<br />
optional</p></td>
<td colspan="2"><p>Either <code>user</code> or <code>role</code>. When not specified, the recipient type is the role.</p></td>
</tr>
<tr>
<td><p>recipientId</p></td>
<td><p>String<br />
optional</p></td>
<td colspan="2"><p>Id of the user or role. In environments with multiple organizations, specify the the organization as &lt;recipientID&gt;%7C&lt;orgID&gt;</p></td>
</tr>
<tr>
<td><p>resolveAll</p></td>
<td><p>boolean<br />
optional</p></td>
<td colspan="2"><p>When set to true, shows the effective permissions for all users and all roles.</p></td>
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
<td colspan="3"><p>200 OK – The body describes the requested permissions for the resource.</p></td>
<td><p>400 Bad Request – When the recipient type is invalid. 404 Not Found – When the specified resource URI is not found in the repository or the recipient ID cannot be resolved.</p></td>
</tr>
</tbody>
</table>

For example, the following request shows all permission for a resource, similar to the permissions dialog in the user interface:

GET http://localhost:8080/jasperserver-pro/rest_v2/permissions/public?resolveAll=true

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">permissions</span>&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">permission</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">mask</span>&gt;0&lt;/<span class="kw">mask</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">recipient</span>&gt;user:anonymousUser&lt;/<span class="kw">recipient</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">permission</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">permission</span>&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">mask</span>&gt;0&lt;/<span class="kw">mask</span>&gt;</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">recipient</span>&gt;user:CaliforniaUser|organization_1&lt;/<span class="kw">recipient</span>&gt;</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">permission</span>&gt;</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>  ...</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">permission</span>&gt;</span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">mask</span>&gt;2&lt;/<span class="kw">mask</span>&gt;</span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">recipient</span>&gt;role:ROLE_USER&lt;/<span class="kw">recipient</span>&gt;</span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">uri</span>&gt;/public&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">permission</span>&gt;</span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">permissions</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>
