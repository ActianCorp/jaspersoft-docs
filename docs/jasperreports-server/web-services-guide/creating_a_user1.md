---
title: Creating a User
description: "To create a user account, put all required information in a user descriptor, and include it in a PUT request to the restv2/users service, with the intended user ID (username) specified in the URL."
---

# 1.0.1 Creating a User

To create a user account, put all required information in a user descriptor, and include it in a PUT request to the rest_v2/users service, with the intended user ID (username) specified in the URL.

-   In the community edition of the server, or commercial editions without organizations, use the first form of the URL.
-   In commercial editions with organizations, use the second URL to specify the user’s organization. When specifying the organization, use its unique ID, not its path. When logged in as the system admin (`superuser`), use the first URL to create users in the root organization.

To create a user, the user ID in the URL must be unique on the server or in the organization. If the user ID already exists, that user account will be modified, as described in section [Modifying User Properties](modifying_user_properties.md).

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
<td><p>PUT</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/users</span>/userID</p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/organizations</span>/orgID/<span>users</span>/userID</p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p>application/xml</p>
<p>application/json</p></td>
<td colspan="2"><p>A user descriptor that includes at least the <code>fullName</code> and <code>password</code> for the user. The role ROLE_USER is automatically assigned to all users, so it does not need to be specified. Do not specify the following properties:</p>
<ul>
<li><code>username</code> – Specified in the URL and cannot be modified in the descriptor.</li>
<li><code>tenantID</code> – Specified in the URL and cannot be modified in the descriptor.</li>
<li><code>externallyDefined</code> – Computed automatically by the server.</li>
<li><code>previousPasswordChangeTime</code> – Computed automatically by the server.</li>
</ul></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>201 Created – The user was successfully created using the values in the descriptor. The response contains the full descriptor of the new user.</p></td>
<td><p>404 Not Found – When the organization ID cannot be resolved.</p></td>
</tr>
</tbody>
</table>

The descriptor sent in the request should contain all the properties you want to set on the new user, except for the username that is specified in the URL. To set roles on the user, specify them as a list of roles. The following example shows the descriptor in JSON format:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;fullName&quot;</span><span class="fu">:</span><span class="st">&quot;Joe User&quot;</span><span class="fu">,</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;emailAddress&quot;</span><span class="fu">:</span><span class="st">&quot;juser@example.com&quot;</span><span class="fu">,</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;enabled&quot;</span><span class="fu">:</span><span class="kw">false</span><span class="fu">,</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;password&quot;</span><span class="fu">:</span><span class="st">&quot;mySecretPassword&quot;</span><span class="fu">,</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;roles&quot;</span><span class="fu">:</span><span class="ot">[</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    <span class="fu">{</span><span class="dt">&quot;name&quot;</span><span class="fu">:</span><span class="st">&quot;ROLE_MANAGER&quot;</span><span class="fu">}</span><span class="ot">]</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
</tbody>
</table>
