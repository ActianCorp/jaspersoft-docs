---
title: Login Encryption
description: "JasperReports Server 4.7 introduced the ability to encrypt plain-text passwords over non-secure HTTP. Encryption does not make passwords more secure, it only prevents them from being readable to..."
---

# Login Encryption

JasperReports Server 4.7 introduced the ability to encrypt plain-text passwords over non-secure HTTP. Encryption does not make passwords more secure, it only prevents them from being readable to humans. For more information about security and how to enable login encryption, see the JasperReports® Server Security Guide.

When login encryption is enabled, passwords in both HTTP Basic Authentication and using the login service must be encrypted by the client. Login encryption has two modes:

- Static key encryption – The server only uses one key that never changes. The client only needs to encrypt the password once and can use it for every web service call.
- Dynamic key encryption – The server changes the encryption key for every session. The client must request the new key and re-encrypt the password before every call using HTTP Basic Authentication or every session using the login service.

The GetEncryptionKey service does not take any arguments or content input.

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]<span>/GetEncryptionKey</span>/</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – Body contains a JSON representation of public key:</p>
<div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;maxdigits&quot;</span><span class="fu">:</span><span class="st">&quot;131&quot;</span><span class="fu">,</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;e&quot;</span><span class="fu">:</span><span class="st">&quot;10001&quot;</span><span class="fu">,</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;n&quot;</span><span class="fu">:</span><span class="st">&quot;9f8a2dc4baa260a5835fa33ef94c...&quot;</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
<td><p>200 OK – Body contains {Error: Key generation is off}</p></td>
</tr>
</tbody>
</table>

To encrypt a password with the server’s public key, use the Bouncy Castle provider with the RSA/NONE/NoPadding algorithm.
