---
title: Updating Report Options
description: Use the following method to modify the values in a given report option.
---

# 1.0.1 Updating Report Options

Use the following method to modify the values in a given report option.

<table>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>PUT</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/reports</span>/path/to/report<span>/options</span>/&lt;optionID&gt;/</p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p>application/json</p></td>
<td colspan="2"><p>A JSON object that lists the input control selections. See example below.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK</p></td>
<td><p>404 Not Found – When the specified report URI is not found in the repository.</p></td>
</tr>
</tbody>
</table>

For example, we change the report option we created in section [Creating Report Options](creating_report_options.md) with the following header:

http://&lt;host&gt;:&lt;port&gt;/jasperserver\[-pro\]/rest_v2/reports/reports/samples/Cascading_multi_select_report/options/MyReportOption

And the following request body:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>   <span class="dt">&quot;Country_multi_select&quot;</span><span class="fu">:</span><span class="ot">[</span><span class="st">&quot;USA&quot;</span><span class="ot">]</span><span class="fu">,</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>   <span class="dt">&quot;Cascading_state_multi_select&quot;</span><span class="fu">:</span><span class="ot">[</span><span class="st">&quot;CA&quot;</span><span class="ot">,</span> <span class="st">&quot;WA&quot;</span><span class="ot">]</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
</tbody>
</table>
