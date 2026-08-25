---
title: Searching for Roles
description: "The GET method without any role ID searches for and lists role definitions. It has options to search for roles by name or by user that belong to the role. If no search is specified, it returns all..."
---

# 1.0.1 Searching for Roles

The GET method without any role ID searches for and lists role definitions. It has options to search for roles by name or by user that belong to the role. If no search is specified, it returns all roles. The method has two forms:

- In the community edition of the server, or commercial editions without organizations, use the first form of the URL without an organization ID.
- In commercial editions with organizations, use the first URL to search or list all roles starting from the logged-in user’s organization (root for the system admin), and use the second URL to search or list all roles in a specified organization.

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/roles</span>?&lt;arguments&gt;</p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/organizations</span>/orgID/<span>roles</span>?&lt;arguments&gt;</p></td>
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
<td colspan="2"><p>Specify a string or substring to match the role ID of any role. The search is not case sensitive.</p></td>
</tr>
<tr>
<td><div class="language-text highlight"><pre><code>user</code></pre></div></td>
<td><p>Optional<br />
String</p></td>
<td colspan="2"><p>Specify a username (ID) to list the roles to which this user belongs. Repeat this argument to list all roles of multiple users. In commercial editions with multiple organizations, specify users as &lt;userID&gt;%7C&lt;orgID&gt; (%7C is the | character).</p></td>
</tr>
<tr>
<td><div class="language-text highlight"><pre><code>hasAllUsers</code></pre></div></td>
<td><p>Optional<br />
Boolean</p></td>
<td colspan="2"><p>When set to true with multiple user arguments, this method returns only the roles to which all specified users belong (intersection of users’ roles). When false or not specified, all roles of all users are found (union of users’ roles).</p></td>
</tr>
<tr>
<td><div class="language-text highlight"><pre><code>includeSubOrgs</code></pre></div></td>
<td><p>Optional<br />
Boolean</p></td>
<td colspan="2"><p>Limits the scope of the search or list in commercial editions with multiple tenants. When set to false, the first URL form is limited to the logged-in user’s organization, and the second URL form is limited to the organization specified in the URL. When true or not specified, the scope includes the hierarchy of all child organizations.</p></td>
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
<td colspan="3"><p>200 OK – The content is a set of descriptors for all roles in the result.</p>
<p>204 No Content – The search did not return any roles.</p></td>
<td><p>404 Not Found – When the organization ID does not match any organization. The content includes an error message.</p></td>
</tr>
</tbody>
</table>

The following example shows the first form URL on a commercial edition server with multiple organizations:

GET http://localhost:8080/jasperserver/rest_v2/roles

This method returns the set of all default system and root roles defined on a server with the sample data (no organization roles have been defined yet):

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">roles</span>&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">role</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">externallyDefined</span>&gt;false&lt;/<span class="kw">externallyDefined</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">name</span>&gt;ROLE_ADMINISTRATOR&lt;/<span class="kw">name</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">role</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">role</span>&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">externallyDefined</span>&gt;false&lt;/<span class="kw">externallyDefined</span>&gt;</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">name</span>&gt;ROLE_ANONYMOUS&lt;/<span class="kw">name</span>&gt;</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">role</span>&gt;</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">role</span>&gt;</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">externallyDefined</span>&gt;false&lt;/<span class="kw">externallyDefined</span>&gt;</span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">name</span>&gt;ROLE_DEMO&lt;/<span class="kw">name</span>&gt;</span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">role</span>&gt;</span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">role</span>&gt;</span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">externallyDefined</span>&gt;false&lt;/<span class="kw">externallyDefined</span>&gt;</span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">name</span>&gt;ROLE_PORTLET&lt;/<span class="kw">name</span>&gt;</span>
<span id="cb1-17"><a href="#cb1-17" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">role</span>&gt;</span>
<span id="cb1-18"><a href="#cb1-18" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">role</span>&gt;</span>
<span id="cb1-19"><a href="#cb1-19" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">externallyDefined</span>&gt;false&lt;/<span class="kw">externallyDefined</span>&gt;</span>
<span id="cb1-20"><a href="#cb1-20" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">name</span>&gt;ROLE_SUPERMART_MANAGER&lt;/<span class="kw">name</span>&gt;</span>
<span id="cb1-21"><a href="#cb1-21" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">role</span>&gt;</span>
<span id="cb1-22"><a href="#cb1-22" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">role</span>&gt;</span>
<span id="cb1-23"><a href="#cb1-23" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">externallyDefined</span>&gt;false&lt;/<span class="kw">externallyDefined</span>&gt;</span>
<span id="cb1-24"><a href="#cb1-24" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">name</span>&gt;ROLE_SUPERUSER&lt;/<span class="kw">name</span>&gt;</span>
<span id="cb1-25"><a href="#cb1-25" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">role</span>&gt;</span>
<span id="cb1-26"><a href="#cb1-26" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">role</span>&gt;</span>
<span id="cb1-27"><a href="#cb1-27" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">externallyDefined</span>&gt;false&lt;/<span class="kw">externallyDefined</span>&gt;</span>
<span id="cb1-28"><a href="#cb1-28" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">name</span>&gt;ROLE_USER&lt;/<span class="kw">name</span>&gt;</span>
<span id="cb1-29"><a href="#cb1-29" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">role</span>&gt;</span>
<span id="cb1-30"><a href="#cb1-30" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">roles</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

!!! note

    The `externallyDefined` property is true when the role is synchronized from a 3rd party such as an LDAP directory or single sign-on mechanism. For more information, see the JasperReports Server Authentication Cookbook.
