---
title: Creating Report Options
description: The following method creates a new report option for a given report. A report option is defined by a set of values for all of the report’s input controls.
---

# 1.0.1 Creating Report Options

The following method creates a new report option for a given report. A report option is defined by a set of values for all of the report’s input controls.

<table>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>POST</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/reports</span>/path/to/report<span>/options</span>?&lt;arguments&gt;</p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><code>label</code></p></td>
<td><p>string</p></td>
<td colspan="2"><p>The name to give the new report option.</p></td>
</tr>
<tr>
<td><p><code>overwrite?</code></p></td>
<td><p>true / false</p></td>
<td colspan="2"><p>If true, any report option that has the same label is replaced. If false or omitted, any report option with the same label will not be replaced.</p></td>
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

In this example, we create new options for the sample report named Cascading_multi_select_report:

http://\<host\>:\<port\>/jasperserver\[-pro\]/rest_v2/reports/reports/samples/Cascading_multi_select_report/options?label=MyReportOption

With the following request body:

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

When successful, the server responds with a JSON object that describes the new report options, for example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;uri&quot;</span><span class="fu">:</span><span class="st">&quot;/reports/samples/MyReportOption&quot;</span><span class="fu">,</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;id&quot;</span><span class="fu">:</span><span class="st">&quot;MyReportOption&quot;</span><span class="fu">,</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;label&quot;</span><span class="fu">:</span><span class="st">&quot;MyReportOption&quot;</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
</tbody>
</table>
