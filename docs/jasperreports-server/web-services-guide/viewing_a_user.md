---
title: Viewing a User
description: The GET method with a user ID (username) retrieves a single descriptor containing the full list of user properties and roles.
---

# 1.0.1 Viewing a User

The GET method with a user ID (`username`) retrieves a single descriptor containing the full list of user properties and roles.

- In the community edition of the server, or commercial editions without organizations, use the first form of the URL.
- In commercial editions with organizations, use the second URL to specify the user’s organization. When specifying the organization, use its unique ID, not its path. When logged in as the system admin (`superuser`), use the first URL to specify users of the root organization.

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/users</span>/userID</p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/organizations</span>/orgID/<span>users</span>/userID</p></td>
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
<td colspan="3"><p>200 OK – The content is the descriptor for the given user.</p></td>
<td><p>404 Not Found – When the user ID or organization ID does not match any user or organization. The content includes an error message.</p></td>
</tr>
</tbody>
</table>

The full user descriptor includes detailed information about the user account, including any roles. The following example shows the descriptor in XML format:

GET http://localhost:8080/jasperserver/rest_v2/users/joeuser

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">user</span>&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">enabled</span>&gt;true&lt;/<span class="kw">enabled</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">externallyDefined</span>&gt;false&lt;/<span class="kw">externallyDefined</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">fullName</span>&gt;Joe User&lt;/<span class="kw">fullName</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">previousPasswordChangeTime</span>&gt;2013-04-19T18:53:07.602-07:00</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">previousPasswordChangeTime</span>&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">roles</span>&gt;</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">role</span>&gt;</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">externallyDefined</span>&gt;false&lt;/<span class="kw">externallyDefined</span>&gt;</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">name</span>&gt;ROLE_USER&lt;/<span class="kw">name</span>&gt;</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">role</span>&gt;</span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">roles</span>&gt;</span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">username</span>&gt;joeuser&lt;/<span class="kw">username</span>&gt;</span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">user</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

In servers with multiple organizations, the full descriptor includes the organization (tenant) ID. The following example shows the descriptor in JSON format:

GET http://localhost:8080/jasperserver/rest_v2/organizations/Finance/users/joeuser

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;fullName&quot;</span><span class="fu">:</span><span class="st">&quot;joeuser&quot;</span><span class="fu">,</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;emailAddress&quot;</span><span class="fu">:</span><span class="st">&quot;&quot;</span><span class="fu">,</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;externallyDefined&quot;</span><span class="fu">:</span><span class="kw">false</span><span class="fu">,</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;enabled&quot;</span><span class="fu">:</span><span class="kw">true</span><span class="fu">,</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;previousPasswordChangeTime&quot;</span><span class="fu">:</span><span class="dv">1366429181984</span><span class="fu">,</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;tenantId&quot;</span><span class="fu">:</span><span class="st">&quot;Finance&quot;</span><span class="fu">,</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;username&quot;</span><span class="fu">:</span><span class="st">&quot;joeuser&quot;</span><span class="fu">,</span></span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;roles&quot;</span><span class="fu">:</span><span class="ot">[</span></span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>    <span class="fu">{</span><span class="dt">&quot;name&quot;</span><span class="fu">:</span><span class="st">&quot;ROLE_USER&quot;</span><span class="fu">,</span><span class="dt">&quot;externallyDefined&quot;</span><span class="fu">:</span><span class="kw">false</span><span class="fu">}</span><span class="ot">]</span></span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
</tbody>
</table>
