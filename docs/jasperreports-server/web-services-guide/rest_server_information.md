---
title: REST Server Information
description: "Use the following service to verify the server information, the same as the About JasperReports Server link in the user interface."
---

# 1.1 REST Server Information

Use the following service to verify the server information, the same as the **About JasperReports Server** link in the user interface.

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/serverInfo</span></p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p>accept: application/xml</p>
<p>accept: application/json</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – Body described below.</p></td>
<td><p>This request should always succeed when the server is running.</p></td>
</tr>
</tbody>
</table>

The server returns a structure containing the information in the requested format, XML or JSON:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">serverInfo</span>&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">build</span>&gt;20141121_1750&lt;/<span class="kw">build</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">dateFormatPattern</span>&gt;yyyy-MM-dd&lt;/<span class="kw">dateFormatPattern</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">datetimeFormatPattern</span>&gt;yyyy-MM-dd&#39;T&#39;HH:mm:ss&lt;/<span class="kw">datetimeFormatPattern</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">edition</span>&gt;PRO&lt;/<span class="kw">edition</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">editionName</span>&gt;Enterprise&lt;/<span class="kw">editionName</span>&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">features</span>&gt;Fusion AHD EXP DB AUD ANA MT &lt;/<span class="kw">features</span>&gt;</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">licenseType</span>&gt;Commercial&lt;/<span class="kw">licenseType</span>&gt;</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">version</span>&gt;6.0.0&lt;/<span class="kw">version</span>&gt;</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">serverInfo</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;dateFormatPattern&quot;</span><span class="fu">:</span> <span class="st">&quot;yyyy-MM-dd&quot;</span><span class="fu">,</span></span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;datetimeFormatPattern&quot;</span><span class="fu">:</span> <span class="st">&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss&quot;</span><span class="fu">,</span></span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;version&quot;</span><span class="fu">:</span> <span class="st">&quot;6.0.0&quot;</span><span class="fu">,</span></span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;edition&quot;</span><span class="fu">:</span> <span class="st">&quot;PRO&quot;</span><span class="fu">,</span></span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;editionName&quot;</span><span class="fu">:</span> <span class="st">&quot;Enterprise&quot;</span><span class="fu">,</span></span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;licenseType&quot;</span><span class="fu">:</span> <span class="st">&quot;Commercial&quot;</span><span class="fu">,</span></span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;build&quot;</span><span class="fu">:</span> <span class="st">&quot;20141121_1750&quot;</span><span class="fu">,</span></span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;features&quot;</span><span class="fu">:</span> <span class="st">&quot;Fusion AHD EXP DB AUD ANA MT &quot;</span></span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
</tbody>
</table>

You can access each value separately with the following URLs. The response is the raw value, XML or JSON are not accepted formats.

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/serverInfo/version</span></p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/serverInfo/edition</span></p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/serverInfo/editionName</span></p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/serverInfo/build</span></p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/serverInfo/licenseType</span></p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/serverInfo/features</span></p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/serverInfo/dateFormatPattern</span><br />
</p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/serverInfo/datetimeFormatPattern</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The requested value.</p></td>
<td><p>These requests should always succeed when the server is running.</p></td>
</tr>
</tbody>
</table>
