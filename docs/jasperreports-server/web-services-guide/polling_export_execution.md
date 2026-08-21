---
title: Polling Export Execution
description: "As with the execution of the main report, you can also poll the execution of the export process. As of JasperReports® Server 5.6, this service supports the extended status value that includes an..."
---

# 1.0.1 Polling Export Execution

As with the execution of the main report, you can also poll the execution of the export process. As of JasperReports® Server 5.6, this service supports the extended status value that includes an appropriate message.

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/report</span><strong>Executions/</strong>requestID/<strong>exports</strong>/<br />
exportID/<strong>status</strong></p></td>
</tr>
<tr>
<td colspan="2"><p>Options</p></td>
<td colspan="2">Sample Return Value</td>
</tr>
<tr>
<td colspan="2"><p>accept: application/xml (default)</p></td>
<td colspan="2"><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">status</span>&gt;ready&lt;/<span class="kw">status</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td colspan="2"><p>accept: application/status+xml</p></td>
<td colspan="2"><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">status</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">errorDescriptor</span>&gt;</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">errorCode</span>&gt;input.controls.validation.error&lt;/<span class="kw">errorCode</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">message</span>&gt;Input controls validation failure&lt;/<span class="kw">message</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">parameters</span>&gt;</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">parameter</span>&gt;Specify a valid value for type Integer.&lt;/<span class="kw">parameter</span>&gt;</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">parameters</span>&gt;</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">errorDescriptor</span>&gt;</span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;failed&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">status</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td colspan="2"><p>accept: application/json</p></td>
<td colspan="2"><div class="sourceCode" id="cb3"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span> <span class="dt">&quot;value&quot;</span><span class="fu">:</span> <span class="st">&quot;ready&quot;</span> <span class="fu">}</span></span></code></pre></div></td>
</tr>
<tr>
<td colspan="2"><p>accept: application/status+json</p></td>
<td colspan="2"><div class="sourceCode" id="cb4"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb4-1"><a href="#cb4-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb4-2"><a href="#cb4-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;value&quot;</span><span class="fu">:</span> <span class="st">&quot;failed&quot;</span><span class="fu">,</span></span>
<span id="cb4-3"><a href="#cb4-3" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;errorDescriptor&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb4-4"><a href="#cb4-4" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;message&quot;</span><span class="fu">:</span> <span class="st">&quot;Input controls validation failure&quot;</span><span class="fu">,</span></span>
<span id="cb4-5"><a href="#cb4-5" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;errorCode&quot;</span><span class="fu">:</span> <span class="st">&quot;input.controls.validation.error&quot;</span><span class="fu">,</span></span>
<span id="cb4-6"><a href="#cb4-6" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;parameters&quot;</span><span class="fu">:</span> <span class="ot">[</span><span class="st">&quot;Specify a valid value for type Integer.&quot;</span><span class="ot">]</span></span>
<span id="cb4-7"><a href="#cb4-7" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span></span>
<span id="cb4-8"><a href="#cb4-8" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The content contains the export status, as shown above. In the extened format, error reports contain error messages suitable for display.</p></td>
<td><p>404 Not Found – When the specified request ID does not exist.</p></td>
</tr>
</tbody>
</table>

For example, to get the status of the HTML export in the previous example, use the following URL:

GET http://localhost:8080/jasperserver-pro/rest_v2/reportExecutions/912382875_1366638024956_2/exports/html/status

When the status is “ready” your client can download the new export output and any attachments as described in section [Requesting Report Output](requesting_report_output.md). For example:

GET http://localhost:8080/jasperserver-pro/rest_v2/reportExecutions/912382875_1366638024956_2/exports/html/outputResource

GET http://localhost:8080/jasperserver-pro/rest_v2/reportExecutions/912382875_1366638024956_2/exports/html/images/img_0_46_0
