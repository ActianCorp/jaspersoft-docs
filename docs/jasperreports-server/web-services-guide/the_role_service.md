---
title: The role Service
description: "The role service allows administrators to view, create, edit, and delete role definitions. However, the role service does not define role membership. To add users to a role, edit the user’s..."
---

# 1.1 The role Service

The role service allows administrators to view, create, edit, and delete role definitions. However, the role service does not define role membership. To add users to a role, edit the user’s properties, as described in [Editing a User](editing_a_user.md).

The GET method of the role service returns descriptors for all roles that match the search string. In commercial editions, the scope of the search is the administrator’s organization and all suborganizations. In the community project, there are no organizations, and the scope is all roles defined in the server. If no search string is specified, all roles are returned. If no roles match the search string, the method returns an empty list.

<table>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>GET</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest/role</span>/&lt;searchString&gt;/</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The content is a descriptor for each of the roles that match the search.</p></td>
<td></td>
</tr>
</tbody>
</table>

In commercial editions, roles defined in an organization specify its ID in the `tenantID` element. System roles that appear in every organization are listed without a tenantID property. The community project does not have organizations and thus does not specify the `tenantId` element on any roles.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">roles</span>&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">role</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">externallyDefined</span>&gt;false&lt;/<span class="kw">externallyDefined</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">roleName</span>&gt;ROLE_ADMINISTRATOR&lt;/<span class="kw">roleName</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">role</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">role</span>&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">externallyDefined</span>&gt;false&lt;/<span class="kw">externallyDefined</span>&gt;</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">roleName</span>&gt;ROLE_ANONYMOUS&lt;/<span class="kw">roleName</span>&gt;</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">role</span>&gt;</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">role</span>&gt;</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">externallyDefined</span>&gt;false&lt;/<span class="kw">externallyDefined</span>&gt;</span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">roleName</span>&gt;ROLE_DEMO&lt;/<span class="kw">roleName</span>&gt;</span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">role</span>&gt;</span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">role</span>&gt;</span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">externallyDefined</span>&gt;false&lt;/<span class="kw">externallyDefined</span>&gt;</span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">roleName</span>&gt;ROLE_SUPERMART_MANAGER&lt;/<span class="kw">roleName</span>&gt;</span>
<span id="cb1-17"><a href="#cb1-17" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">role</span>&gt;</span>
<span id="cb1-18"><a href="#cb1-18" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">role</span>&gt;</span>
<span id="cb1-19"><a href="#cb1-19" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">externallyDefined</span>&gt;false&lt;/<span class="kw">externallyDefined</span>&gt;</span>
<span id="cb1-20"><a href="#cb1-20" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">roleName</span>&gt;ROLE_USER&lt;/<span class="kw">roleName</span>&gt;</span>
<span id="cb1-21"><a href="#cb1-21" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">role</span>&gt;</span>
<span id="cb1-22"><a href="#cb1-22" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">role</span>&gt;</span>
<span id="cb1-23"><a href="#cb1-23" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">externallyDefined</span>&gt;false&lt;/<span class="kw">externallyDefined</span>&gt;</span>
<span id="cb1-24"><a href="#cb1-24" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">roleName</span>&gt;ROLE_SAMPLE&lt;/<span class="kw">roleName</span>&gt;</span>
<span id="cb1-25"><a href="#cb1-25" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">tenantId</span>&gt;organization_1&lt;/<span class="kw">tenantId</span>&gt;</span>
<span id="cb1-26"><a href="#cb1-26" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">role</span>&gt;</span>
<span id="cb1-27"><a href="#cb1-27" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">roles</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>
