---
title: Searching for Users
description: "The GET method without any user ID searches for and lists user accounts. It has options to search for users by name or by role. If no search is specified, it returns all users. The method has two..."
---

# 1.0.1 Searching for Users

The GET method without any user ID searches for and lists user accounts. It has options to search for users by name or by role. If no search is specified, it returns all users. The method has two forms:

- In the community edition of the server, or commercial editions without organizations, use the first form of the URL without an organization ID.
- In commercial editions with organizations, use the first URL to list all users starting from the logged-in user’s organization (root for the system admin), and use the second URL to list all users in a specified organization.

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/users</span>?&lt;arguments&gt;</p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/organizations</span>/orgID/<span>users</span>?&lt;arguments&gt;</p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><div class="language-text highlight"><pre><code>search</code></pre></div></td>
<td><p>Optional<br />
String</p></td>
<td colspan="2"><p>Specify a string or substring to match the user ID or full name of any user. The search is not case sensitive.</p></td>
</tr>
<tr>
<td><div class="language-text highlight"><pre><code>requiredRole</code></pre></div></td>
<td><p>Optional<br />
String</p></td>
<td colspan="2"><p>Specify a role name to list only users with this role. Repeat this argument to filter with multiple roles. In commercial editions with multiple organizations, specify roles as &lt;roleName&gt;%7C&lt;orgID&gt; (%7C is the | character).</p></td>
</tr>
<tr>
<td><div class="language-text highlight"><pre><code>hasAllRequiredRoles</code></pre></div></td>
<td><p>Optional<br />
Boolean</p></td>
<td colspan="2"><p>When set to false with multiple requiredRole arguments, users will match if they have any of the given roles (OR operation). When true or not specified, users must match all of the given roles (AND operation).</p></td>
</tr>
<tr>
<td><div class="language-text highlight"><pre><code>includeSubOrgs</code></pre></div></td>
<td><p>Optional<br />
Boolean</p></td>
<td colspan="2"><p>Limits the scope of the search or list in commercial editions with multiple organizations. When set to false, the first URL form is limited to the logged-in user’s organization, and the second URL form is limited to the organization specified in the URL. When true or not specified, the scope includes the hierarchy of all child organizations.</p></td>
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
<td colspan="3"><p>200 OK – The content is a set of descriptors for all users in the result.</p>
<p>204 No Content – The search did not return any users.</p></td>
<td><p>404 Not Found – When the organization ID does not match any organization. The content includes an error message.</p></td>
</tr>
</tbody>
</table>

The following example shows the first form of the URL on a community edition server:

GET http://localhost:8080/jasperserver/rest_v2/users?search=j

The response is a set of summary descriptors for all users containing the string “j”:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">users</span>&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">user</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">externallyDefined</span>&gt;false&lt;/<span class="kw">externallyDefined</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">fullName</span>&gt;jasperadmin User&lt;/<span class="kw">fullName</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">username</span>&gt;jasperadmin&lt;/<span class="kw">username</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">user</span>&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">user</span>&gt;</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">externallyDefined</span>&gt;false&lt;/<span class="kw">externallyDefined</span>&gt;</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">fullName</span>&gt;Joe User&lt;/<span class="kw">fullName</span>&gt;</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">username</span>&gt;joeuser&lt;/<span class="kw">username</span>&gt;</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">user</span>&gt;</span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">users</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

The next example shows the second form of the URL on a commercial edition server with multiple organizations:

GET http://localhost:8080/jasperserver/rest_v2/organizations/Finance/users

On servers with multiple organizations, the summary user descriptors include the organization (tenant) ID:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">users</span>&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">user</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">externallyDefined</span>&gt;false&lt;/<span class="kw">externallyDefined</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">fullName</span>&gt;jasperadmin&lt;/<span class="kw">fullName</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">tenantId</span>&gt;Finance&lt;/<span class="kw">tenantId</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">username</span>&gt;jasperadmin&lt;/<span class="kw">username</span>&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">user</span>&gt;</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">user</span>&gt;</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">externallyDefined</span>&gt;false&lt;/<span class="kw">externallyDefined</span>&gt;</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">fullName</span>&gt;jasperadmin&lt;/<span class="kw">fullName</span>&gt;</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">tenantId</span>&gt;Audit&lt;/<span class="kw">tenantId</span>&gt;</span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">username</span>&gt;jasperadmin&lt;/<span class="kw">username</span>&gt;</span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">user</span>&gt;</span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">user</span>&gt;</span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">externallyDefined</span>&gt;false&lt;/<span class="kw">externallyDefined</span>&gt;</span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">fullName</span>&gt;joeuser&lt;/<span class="kw">fullName</span>&gt;</span>
<span id="cb1-17"><a href="#cb1-17" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">tenantId</span>&gt;Finance&lt;/<span class="kw">tenantId</span>&gt;</span>
<span id="cb1-18"><a href="#cb1-18" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">username</span>&gt;joeuser&lt;/<span class="kw">username</span>&gt;</span>
<span id="cb1-19"><a href="#cb1-19" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">user</span>&gt;</span>
<span id="cb1-20"><a href="#cb1-20" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">user</span>&gt;</span>
<span id="cb1-21"><a href="#cb1-21" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">externallyDefined</span>&gt;false&lt;/<span class="kw">externallyDefined</span>&gt;</span>
<span id="cb1-22"><a href="#cb1-22" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">fullName</span>&gt;joeuser&lt;/<span class="kw">fullName</span>&gt;</span>
<span id="cb1-23"><a href="#cb1-23" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">tenantId</span>&gt;Audit&lt;/<span class="kw">tenantId</span>&gt;</span>
<span id="cb1-24"><a href="#cb1-24" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">username</span>&gt;joeuser&lt;/<span class="kw">username</span>&gt;</span>
<span id="cb1-25"><a href="#cb1-25" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">user</span>&gt;</span>
<span id="cb1-26"><a href="#cb1-26" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">users</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>
