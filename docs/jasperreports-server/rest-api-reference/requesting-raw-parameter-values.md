---
title: Requesting Raw Parameter Values
description: "After returning from the drill down report, you can restore the input control values applied to the main report. Using the following method, you can request raw parameter values."
---

# Requesting Raw Parameter Values

After returning from the drill down report, you can restore the input control values applied to the main report. Using the following method, you can request raw parameter values.

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]<span>/rest_v2/reportExecutions</span>/requestID/<span>rawParameterValues</span></p></td>
</tr>
<tr>
<td colspan="2"><p>Media-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/json</span></p></td>
<td colspan="2"><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a><span class="dt">&quot;someParameterName&quot;</span><span class="fu">:</span><span class="ot">[</span><span class="st">&quot;someValue&quot;</span><span class="ot">]</span><span class="fu">,</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a><span class="dt">&quot;someAnotherParameterName&quot;</span><span class="fu">:</span><span class="ot">[</span><span class="st">&quot;anotherValue1&quot;</span><span class="ot">,</span><span class="st">&quot;anotherValue2&quot;</span><span class="ot">]</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK: The content contains the value as shown above.</p></td>
<td><p>404 Not Found: When the request ID specified in the request does not exist.</p></td>
</tr>
</tbody>
</table>
