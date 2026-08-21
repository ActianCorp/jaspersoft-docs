---
title: Listing Input Control Values
description: "The following method returns a description of the possible values of all input controls for the report. Among these choices, it shows which ones are selected."
---

# 1.0.1 Listing Input Control Values

The following method returns a description of the possible values of all input controls for the report. Among these choices, it shows which ones are selected.

<table>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>GET</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/reports</span>/path/to/report<span>/inputControls/values/</span></p></td>
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
<td colspan="3"><p>200 OK – The content is a JSON object that describes the input control values and selection.</p></td>
<td><p>404 Not Found – When the specified report URI is not found in the repository.</p></td>
</tr>
</tbody>
</table>

The body of the response contains the structure of the input controls for the report. The following example shows a response in the JSON format:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;inputControlState&quot;</span> <span class="fu">:</span> <span class="ot">[</span> <span class="fu">{</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;uri&quot;</span> <span class="fu">:</span> <span class="st">&quot;/reports/samples/.../Country_multi_select&quot;</span><span class="fu">,</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;value&quot;</span> <span class="fu">:</span> <span class="st">&quot;&quot;</span><span class="fu">,</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;options&quot;</span> <span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>      <span class="dt">&quot;label&quot;</span> <span class="fu">:</span> <span class="st">&quot;Canada&quot;</span><span class="fu">,</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>      <span class="dt">&quot;selected&quot;</span> <span class="fu">:</span> <span class="st">&quot;false&quot;</span><span class="fu">,</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>      <span class="dt">&quot;value&quot;</span> <span class="fu">:</span> <span class="st">&quot;Canada&quot;</span></span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>    <span class="fu">},</span> <span class="er">{</span></span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>      <span class="dt">&quot;label&quot;</span> <span class="fu">:</span> <span class="st">&quot;Mexico&quot;</span><span class="fu">,</span></span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>      <span class="dt">&quot;selected&quot;</span> <span class="fu">:</span> <span class="st">&quot;false&quot;</span><span class="fu">,</span></span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>      <span class="dt">&quot;value&quot;</span> <span class="fu">:</span> <span class="st">&quot;Mexico&quot;</span></span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span><span class="ot">,</span> <span class="fu">{</span></span></code></pre></div></td>
</tr>
<tr>
<td><pre class="text"><code>      &quot;label&quot; : &quot;USA&quot;,
      &quot;selected&quot; : &quot;true&quot;,
      &quot;value&quot; : &quot;USA&quot;
    }
  },
  ...
  ]
}</code></pre></td>
</tr>
</tbody>
</table>

!!! note

    If a selection-type input control has a null value, it is given as `~NULL~`. If no selection is made, its value is given as `~NOTHING~`.
