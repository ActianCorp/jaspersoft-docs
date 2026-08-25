---
title: Security Check
description: "The security check call is equivalent to a login call. You send the user credentials and you can tell from the response whether they are valid or not on the server. If they are valid, the server..."
---

# Security Check

The security check call is equivalent to a login call. You send the user credentials and you can tell from the response whether they are valid or not on the server. If they are valid, the server creates a user session or if the user has already performed an operation with valid credentials, it accesses the existing user session.

In either case, the successful response contains the JSESSIONID cookie of the user session. As with the login service, once you receive the session cookie, you should return it with future requests and use it to close the session as described in [Logout](logout.md).

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
<td></td>
</tr>
<tr>
<td><p>GET</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>/j_spring_security_check</span>?&lt;arguments&gt;</p></td>
<td></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
<td></td>
</tr>
<tr>
<td>orgId?</td>
<td>Text</td>
<td colspan="2">The organization ID or alias. Required for organization admins and users when there is more than one organization defined. Not required for the system admin (<code>superuser</code> by default).</td>
<td></td>
</tr>
<tr>
<td><p>j_username</p></td>
<td><p>Text</p></td>
<td colspan="2"><p>The user ID.</p></td>
<td></td>
</tr>
<tr>
<td><p>j_password</p></td>
<td><p>Text</p></td>
<td colspan="2"><p>The user’s password. If the server has login encryption enabled, the password must be encrypted as explained in <a href="login_encryption.md">Login Encryption</a>.</p></td>
<td></td>
</tr>
<tr>
<td>userLocale?</td>
<td>Java locale string</td>
<td colspan="2">Set the optional locale for user in this session.</td>
<td></td>
</tr>
<tr>
<td>userTimezone?</td>
<td>Java time zone</td>
<td colspan="2">Set the optional time zone for the user in this session.</td>
<td></td>
</tr>
<tr>
<td colspan="4">Options</td>
<td> </td>
</tr>
<tr>
<td colspan="4">accept: application/json</td>
<td> </td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
<td></td>
</tr>
<tr>
<td colspan="3"><p>302 Moved Temporarily – Response HTTP Header "Location" redirects to "/loginsuccess.html" by default, but often depends on the last session operation.</p>
<p>See below if you specify JSON.</p></td>
<td><p>302 Moved Temporarily – Response HTTP Header "Location" redirects to /login.html?error=1.</p></td>
<td></td>
</tr>
</tbody>
</table>

If you specify `accept: application/json` in your request, the location of the redirect in case of success is always the file /scripts/bower_components/js-sdk/src/common/auth/loginSuccess.json. The content of this file is:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a><span class="dt">&quot;success&quot;</span><span class="fu">:</span><span class="kw">true</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
</tbody>
</table>

You can configure the location of this file. Edit the configuration file applicationContext-security-web.xml and change the constructor value of the following bean:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">bean</span> <span class="ot">id=</span><span class="st">&quot;authSuccessJsonRedirectUrl&quot;</span> <span class="ot">class=</span><span class="st">&quot;java.lang.String&quot;</span>&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>                            </span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">constructor-arg</span> <span class="ot">type=</span><span class="st">&quot;java.lang.String&quot;</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    <span class="ot">value=</span><span class="st">&quot;/scripts/bower_components/js-sdk/src/common/auth/loginSuccess.json&quot;</span>/&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>                            </span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">bean</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

# Using an SSO Token

If you are using Single Sign-On for authentication, you can use the security check to submit the ticket.

<table>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
<td></td>
</tr>
<tr>
<td><p>GET</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>/j_spring_security_check</span>?&lt;arguments&gt;</p></td>
<td></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
<td></td>
</tr>
<tr>
<td>ticket</td>
<td>Text</td>
<td colspan="2">The ticket for your SSO mechanism. The default parameter name for an SSO authentication token is "ticket". This parameter name can be changed in the configuration file applicationContext-externalAuth-&lt;sso&gt;.xml.</td>
<td></td>
</tr>
<tr>
<td colspan="4">Options</td>
<td> </td>
</tr>
<tr>
<td colspan="4">accept: application/json</td>
<td> </td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
<td></td>
</tr>
<tr>
<td colspan="3"><p>302 Moved Temporarily – Response HTTP Header "Location" redirects to "/loginsuccess.html" by default, but often depends on the last session operation.</p></td>
<td><p>302 Moved Temporarily – Response HTTP Header "Location" redirects to /login.html?error=1.</p></td>
<td></td>
</tr>
</tbody>
</table>

For example, if you have configured the server to use CAS as your SSO provider, you can authenticate and receive the session ID with the following request:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="language-text highlight"><pre><code>GET http://localhost:8080/jasperserver-pro/j_spring_security_check?ticket=ST-40-CZeUUnGPxEqgScNbxh9l-sso-cas.eng.jaspersoft.com</code></pre></div></td>
</tr>
</tbody>
</table>

The response has the same behavior as the password-based security check, including the use of a JSON file if requested.

# Using a Pre-Authentication Token

When using a pre-authentication mechanism, the verification of the credentials is performed at the base URL of the server.

<table>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
<td></td>
</tr>
<tr>
<td><p>GET</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/?&lt;arguments&gt;</p></td>
<td></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
<td></td>
</tr>
<tr>
<td>pp</td>
<td>Text</td>
<td colspan="2">The token for your pre-authentication mechanism. The default parameter name for a pre authentication token is "pp". This parameter name can be changed in the configuration file applicationContext-externalAuth-preAuth.xml.</td>
<td></td>
</tr>
<tr>
<td colspan="4">Options</td>
<td> </td>
</tr>
<tr>
<td colspan="4">accept: application/json</td>
<td> </td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
<td></td>
</tr>
<tr>
<td colspan="3"><p>302 Moved Temporarily – Response HTTP Header "Location" redirects to "/loginsuccess.html" by default, but often depends on the last session operation.</p></td>
<td><p>302 Moved Temporarily – Response HTTP Header "Location" redirects to /login.html?error=1.</p></td>
<td></td>
</tr>
</tbody>
</table>

For example, if you have configured the server to use pre-authentication, you can authenticate and receive the session ID with the following request:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="language-text highlight"><pre><code>GET http://localhost:8080/jasperserver-pro?pp=u%3DSteve%7Cr%3DExt_User%7Co%3Dorganization_1%7Cpa1%3DUSA%7Cpa2%3D1</code></pre></div></td>
</tr>
</tbody>
</table>
