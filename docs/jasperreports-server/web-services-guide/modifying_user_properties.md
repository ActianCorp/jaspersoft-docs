---
title: Modifying User Properties
description: "To modify the properties of a user account, put all desired information in a user descriptor, and include it in a PUT request to the restv2/users service, with the existing user ID (username)..."
---

# 1.0.1 Modifying User Properties

To modify the properties of a user account, put all desired information in a user descriptor, and include it in a PUT request to the rest_v2/users service, with the existing user ID (username) specified in the URL.

-   In the community edition of the server, or commercial editions without organizations, use the first form of the URL.
-   In commercial editions with organizations, use the second URL to specify the user’s organization. When specifying the organization, use its unique ID, not its path. When logged in as the system admin (`superuser`), use the first URL to modify users of the root organization.

To modify a user, the user ID in the URL must already exist on the server or in the organization. If the user ID doesn’t exist, a user account will be created, as described in section [Creating a User](creating_a_user1.md).

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
<td colspan="2"><p>A user descriptor that includes the properties you want to change. Do not specify the following properties:</p>
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
<td colspan="3"><p>200 OK – The user properties were successfully updated.</p></td>
<td><p>404 Not Found – When the organization ID cannot be resolved.</p></td>
</tr>
</tbody>
</table>

To add a role to the user, specify the entire list of roles with the desired role added. To remove a role from a user, specify the entire list of roles with the desired role removed. The following example shows the descriptor in JSON format:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;enabled&quot;</span><span class="fu">:</span><span class="kw">true</span><span class="fu">,</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;password&quot;</span><span class="fu">:</span><span class="st">&quot;newPassword&quot;</span><span class="fu">,</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;roles&quot;</span><span class="fu">:</span><span class="ot">[</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    <span class="fu">{</span><span class="dt">&quot;name&quot;</span><span class="fu">:</span><span class="st">&quot;ROLE_USER&quot;</span><span class="fu">}</span><span class="ot">]</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    <span class="fu">{</span><span class="dt">&quot;name&quot;</span><span class="fu">:</span><span class="st">&quot;ROLE_STOREMANAGER&quot;</span><span class="fu">}</span><span class="er">]</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
</tbody>
</table>
