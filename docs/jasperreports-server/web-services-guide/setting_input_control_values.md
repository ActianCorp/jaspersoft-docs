---
title: Setting Input Control Values
description: "The following method validates the input controls that you send, to ensure that they can be used in the next run of the report."
---

# Setting Input Control Values

The following method validates the input controls that you send, to ensure that they can be used in the next run of the report.

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
<td><p>POST</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/reports</span>/path/to/report<span>/inputControls/</span>&lt;ic1&gt;;<br />
&lt;ic2&gt;;...<span>/values/</span></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p>application/json</p></td>
<td colspan="2"><p>A JSON object that lists your selected values. The value of every input control is given as an array of string values, even for single-select controls or multi-select controls with a single value. See also the example below:</p>
<div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;boolean-input-control&quot;</span> <span class="fu">:</span> <span class="ot">[</span><span class="st">&quot;true&quot;</span><span class="ot">]</span><span class="fu">,</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;integer-input-control&quot;</span> <span class="fu">:</span> <span class="ot">[</span><span class="st">&quot;123456&quot;</span><span class="ot">]</span><span class="fu">,</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;single-select-input-control&quot;</span> <span class="fu">:</span> <span class="ot">[</span><span class="st">&quot;some value&quot;</span><span class="ot">]</span><span class="fu">,</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;multiple-select-input-control-1&quot;</span> <span class="fu">:</span> <span class="ot">[</span><span class="st">&quot;another value&quot;</span><span class="ot">]</span><span class="fu">,</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;multiple-select-input-control-2&quot;</span> <span class="fu">:</span> <span class="ot">[</span><span class="st">&quot;first&quot;</span><span class="ot">,</span> <span class="st">&quot;second&quot;</span><span class="ot">,</span> <span class="st">&quot;third&quot;</span><span class="ot">]</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
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
<td colspan="3"><p>200 OK – The content is a JSON object that describes the new selection of input control values.</p></td>
<td><p>404 Not Found – When the specified report URI is not found in the repository.</p></td>
</tr>
</tbody>
</table>

Assuming the client receives the response given in section [Listing Input Control Values](listing_input_control_values.md), it can send the following request body:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>   <span class="dt">&quot;Country_multi_select&quot;</span><span class="fu">:</span><span class="ot">[</span><span class="st">&quot;Mexico&quot;</span><span class="ot">]</span><span class="fu">,</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>   <span class="dt">&quot;Cascading_state_multi_select&quot;</span><span class="fu">:</span><span class="ot">[</span><span class="st">&quot;Guerrero&quot;</span><span class="ot">,</span> <span class="st">&quot;Sinaloa&quot;</span><span class="ot">]</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
</tbody>
</table>

When specifying the option for the JSON format, the server’s response is:

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
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>    <span class="fu">},</span> <span class="er">{</span></span></code></pre></div></td>
</tr>
<tr>
<td><div class="language-text highlight"><pre><code>      &quot;label&quot; : &quot;Mexico&quot;,
      &quot;selected&quot; : &quot;true&quot;,
      &quot;value&quot; : &quot;Mexico&quot;
    }, {
      &quot;label&quot; : &quot;USA&quot;,
      &quot;selected&quot; : &quot;false&quot;,
      &quot;value&quot; : &quot;USA&quot;
    }
  },
  ...
  ]
}</code></pre></div></td>
</tr>
</tbody>
</table>
