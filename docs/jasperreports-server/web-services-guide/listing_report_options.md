---
title: Listing Report Options
description: "The following method retrieves a list of report options summaries. The summaries give the name of the report options, but not the input control values that are associated with it."
---

# 1.0.1 Listing Report Options

The following method retrieves a list of report options summaries. The summaries give the name of the report options, but not the input control values that are associated with it.

<table>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>GET</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/reports</span>/path/to/report<span>/options/</span></p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p>accept: application/json</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The content is a JSON object that lists the names of the report options for the given report.</p></td>
<td><p>404 Not Found – When the specified report URI is not found in the repository.</p></td>
</tr>
</tbody>
</table>

The body of the response contains the labels of the report options, for example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;reportOptionsSummary&quot;</span><span class="fu">:</span> <span class="ot">[</span><span class="fu">{</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;uri&quot;</span><span class="fu">:</span> <span class="st">&quot;/reports/samples/Options&quot;</span><span class="fu">,</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;id&quot;</span><span class="fu">:</span> <span class="st">&quot;Options&quot;</span><span class="fu">,</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;label&quot;</span><span class="fu">:</span> <span class="st">&quot;Options&quot;</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>  <span class="fu">}</span><span class="ot">,</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>  <span class="fu">{</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;uri&quot;</span><span class="fu">:</span> <span class="st">&quot;/reports/samples/Options_2&quot;</span><span class="fu">,</span></span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;id&quot;</span><span class="fu">:</span> <span class="st">&quot;Options_2&quot;</span><span class="fu">,</span></span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;label&quot;</span><span class="fu">:</span> <span class="st">&quot;Options 2&quot;</span></span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>  <span class="fu">}</span><span class="ot">]</span></span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
</tbody>
</table>
