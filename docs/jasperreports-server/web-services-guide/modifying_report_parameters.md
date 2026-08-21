---
title: Modifying Report Parameters
description: "As of JasperReports® Server 5.6, you can update the report parameters, also known as input controls before running report executions."
---

# 1.0.1 Modifying Report Parameters

As of JasperReports® Server 5.6, you can update the report parameters, also known as input controls before running report executions.

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/reportExecutions</span>/requestID/<strong>parameters</strong></p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><code>freshData</code></p></td>
<td><p>default=true</p></td>
<td colspan="2"><p>When data snapshots are enabled, new parameters must force the server to get fresh data by querying the data source. This overrides the default in <a href="running_a_report_asynchronously.md">Table 1-1, “Report Execution Properties,” on page 1</a>.</p></td>
</tr>
<tr>
<td colspan="2">Media-Type</td>
<td colspan="2">Content</td>
</tr>
<tr>
<td colspan="2"><p>application/json</p></td>
<td colspan="2"><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="ot">[</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="fu">{</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;name&quot;</span><span class="fu">:</span><span class="st">&quot;someParameterName&quot;</span><span class="fu">,</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;value&quot;</span><span class="fu">:</span><span class="ot">[</span><span class="st">&quot;value 1&quot;</span><span class="ot">,</span> <span class="st">&quot;value 2&quot;</span><span class="ot">]</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span><span class="ot">,</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    <span class="fu">{</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;name&quot;</span><span class="fu">:</span><span class="st">&quot;someAnotherParameterName&quot;</span><span class="fu">,</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;value&quot;</span><span class="fu">:</span><span class="ot">[</span><span class="st">&quot;another value&quot;</span><span class="ot">]</span></span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span></span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a><span class="ot">]</span></span></code></pre></div></td>
</tr>
<tr>
<td colspan="2">application/xml</td>
<td colspan="2"><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">reportParameters</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">reportParameter</span> <span class="ot">name=</span><span class="st">&quot;Country_multi_select&quot;</span>&gt;</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">value</span>&gt;Mexico&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">reportParameter</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>     &lt;<span class="kw">reportParameter</span> <span class="ot">name=</span><span class="st">&quot;Cascading_state_multi_select&quot;</span>&gt;</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">value</span>&gt;Guerrero&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">value</span>&gt;Sinaloa&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">reportParameter</span>&gt;</span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">reportParameters</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>204 No Content – There is no content to return.</p></td>
<td><p>404 Not Found – When the request ID specified in the request does not exist.</p></td>
</tr>
</tbody>
</table>
