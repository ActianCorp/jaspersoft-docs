---
title: The keys Service
description: "The restv2/keys service allows you to list the cryptographic keys that have been added to the server's keystore. The keys in the list are identified by their key alias, the keys themselves are not..."
---

# The keys Service

The rest_v2/keys service allows you to list the cryptographic keys that have been added to the server's keystore. The keys in the list are identified by their key alias, the keys themselves are not given. The response never includes the server's own keys that it creates at installation time, only custom keys added to keystore by administrators using the `js-import` or `keytool` commands.

For more information about cryptographic keys and how to add them to the keystore, see the JasperReports Server Security Guide.

This service requires system administrator priviliges on the server (jasperadmin for Community Project, superuser for Professional Edition).

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>GET</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/<span>rest_v2/keys</span>/</span></p></td>
</tr>
<tr>
<td colspan="2"><p>Options</p></td>
<td colspan="2"><p>Response</p></td>
</tr>
<tr>
<td colspan="2"><p><span>accept:application/json</span></p></td>
<td colspan="2"><p>A JSON object that lists custom keys, for example:</p>
<div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="ot">[</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="fu">{</span><span class="dt">&quot;alias&quot;</span><span class="fu">:</span> <span class="st">&quot;myCustomKeyAlias&quot;</span><span class="fu">,</span> <span class="dt">&quot;algorithm&quot;</span><span class="fu">:</span> <span class="st">&quot;AES&quot;</span><span class="fu">,</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>     <span class="dt">&quot;label&quot;</span><span class="fu">:</span> <span class="st">&quot;My Custom Key&quot;</span> <span class="fu">}</span><span class="ot">,</span> </span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    <span class="fu">{</span><span class="dt">&quot;alias&quot;</span><span class="fu">:</span> <span class="st">&quot;productionServerKey&quot;</span><span class="fu">,</span> <span class="dt">&quot;algorithm&quot;</span><span class="fu">:</span> <span class="st">&quot;AES&quot;</span><span class="fu">}</span><span class="ot">,</span> </span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    <span class="fu">{</span><span class="dt">&quot;alias&quot;</span><span class="fu">:</span> <span class="st">&quot;testServerKey&quot;</span><span class="fu">,</span> <span class="dt">&quot;algorithm&quot;</span><span class="fu">:</span> <span class="st">&quot;RSA&quot;</span><span class="fu">}</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a><span class="ot">]</span></span></code></pre></div></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The response contains the custom keys.</p>
<p>204 No Content – When there are no custom keys.</p></td>
<td><p>401 Unauthorized – When system administrator credentials are not provided.</p></td>
</tr>
</tbody>
</table>

You can use the response to create a list of keys available for import or export operations. When present, use the label to display the keys, otherwise use the alias. When specifying keys in import and export operations, specify them by alias. For more information, see [“The export Service” on page 1](export.md) and [“The import Service” on page 1](import.md).
