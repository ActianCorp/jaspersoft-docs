---
title: The user Service
description: "The GET method for the user service returns descriptors for all users that match the search string. In commercial editions, the scope of the search is the administrator’s organization and all..."
---

# 1.1 The user Service

The GET method for the user service returns descriptors for all users that match the search string. In commercial editions, the scope of the search is the administrator’s organization and all suborganizations. In the community project, there are no organizations, and the scope is all users defined in the server. If no search string is specified, all users are returned. If no users match the search string, the method returns an empty list.

<table>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>GET</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest/user</span>/&lt;searchString&gt;</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The content is a descriptor for each of the users that match the search.</p></td>
<td></td>
</tr>
</tbody>
</table>

The following example shows the descriptors for users that match the search string “joe”:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">users</span>&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">user</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">enabled</span>&gt;true&lt;/<span class="kw">enabled</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">externallyDefined</span>&gt;false&lt;/<span class="kw">externallyDefined</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">fullName</span>&gt;Joe User&lt;/<span class="kw">fullName</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">previousPasswordChangeTime</span>&gt;2011-11-29T10:18:38.062-08:00</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>      &lt;/<span class="kw">previousPasswordChangeTime</span>&gt;</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">roles</span>&gt;</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">externallyDefined</span>&gt;false&lt;/<span class="kw">externallyDefined</span>&gt;</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">roleName</span>&gt;ROLE_USER&lt;/<span class="kw">roleName</span>&gt;</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">roles</span>&gt;</span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">tenantId</span>&gt;organization_1&lt;/<span class="kw">tenantId</span>&gt;</span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">username</span>&gt;joeuser&lt;/<span class="kw">username</span>&gt;</span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">user</span>&gt;</span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">user</span>&gt;</span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">emailAddress</span>&gt;&lt;/<span class="kw">emailAddress</span>&gt;</span>
<span id="cb1-17"><a href="#cb1-17" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">enabled</span>&gt;true&lt;/<span class="kw">enabled</span>&gt;</span>
<span id="cb1-18"><a href="#cb1-18" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">externallyDefined</span>&gt;false&lt;/<span class="kw">externallyDefined</span>&gt;</span>
<span id="cb1-19"><a href="#cb1-19" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">fullName</span>&gt;joeuser&lt;/<span class="kw">fullName</span>&gt;</span>
<span id="cb1-20"><a href="#cb1-20" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">previousPasswordChangeTime</span>&gt;2011-11-29T15:52:18.407-08:00</span>
<span id="cb1-21"><a href="#cb1-21" aria-hidden="true" tabindex="-1"></a>      &lt;/<span class="kw">previousPasswordChangeTime</span>&gt;</span>
<span id="cb1-22"><a href="#cb1-22" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">roles</span>&gt;</span>
<span id="cb1-23"><a href="#cb1-23" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">externallyDefined</span>&gt;false&lt;/<span class="kw">externallyDefined</span>&gt;</span>
<span id="cb1-24"><a href="#cb1-24" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">roleName</span>&gt;ROLE_USER&lt;/<span class="kw">roleName</span>&gt;</span>
<span id="cb1-25"><a href="#cb1-25" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">roles</span>&gt;</span>
<span id="cb1-26"><a href="#cb1-26" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">tenantId</span>&gt;SubOrganization&lt;/<span class="kw">tenantId</span>&gt;</span>
<span id="cb1-27"><a href="#cb1-27" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">username</span>&gt;joeuser&lt;/<span class="kw">username</span>&gt;</span>
<span id="cb1-28"><a href="#cb1-28" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">user</span>&gt;</span>
<span id="cb1-29"><a href="#cb1-29" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">users</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

The descriptor above is from a commercial edition, and each user has a `tenantId` element to indicate which organization the user belongs to. The community project does not have organizations and thus does not specify the `tenantId` element.

!!! note

    The `externallyDefined` property is true when the user is authenticated by a 3rd party such as an LDAP directory or single sign-on mechanism. For more information, see the JasperReports Server Authentication Cookbook.
