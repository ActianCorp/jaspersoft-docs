---
title: Requesting Report Execution Details
description: "Once the report is ready, your client must determine the names of the files to download by requesting the reportExecution descriptor again. Specify the requestID in the URL as follows:"
---

# 1.0.1 Requesting Report Execution Details

Once the report is ready, your client must determine the names of the files to download by requesting the `reportExecution` descriptor again. Specify the requestID in the URL as follows:

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/report</span><strong>Executions/</strong>requestID</p></td>
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
<td colspan="3"><p>200 OK – The content contains a ReportExecution descriptor. See below for an example.</p></td>
<td><p>404 Not Found – When the request ID specified in the request does not exist.</p></td>
</tr>
</tbody>
</table>

The report execution descriptor now contains the list of exports for the report, including the report output itself and any other file attachments. File attachments such as images and JavaScript occur only with HTML export.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;status&quot;</span><span class="fu">:</span> <span class="st">&quot;ready&quot;</span><span class="fu">,</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;totalPages&quot;</span><span class="fu">:</span> <span class="dv">47</span><span class="fu">,</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;requestId&quot;</span><span class="fu">:</span> <span class="st">&quot;b487a05a-4989-8b53-b2b9-b54752f998c4&quot;</span><span class="fu">,</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;reportURI&quot;</span><span class="fu">:</span> <span class="st">&quot;/reports/samples/AllAccounts&quot;</span><span class="fu">,</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;exports&quot;</span><span class="fu">:</span> <span class="ot">[</span><span class="fu">{</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;id&quot;</span><span class="fu">:</span> <span class="st">&quot;195a65cb-1762-450a-be2b-1196a02bb625&quot;</span><span class="fu">,</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;options&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;outputFormat&quot;</span><span class="fu">:</span> <span class="st">&quot;html&quot;</span><span class="fu">,</span></span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;attachmentsPrefix&quot;</span><span class="fu">:</span> <span class="st">&quot;./images/&quot;</span><span class="fu">,</span></span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;allowInlineScripts&quot;</span><span class="fu">:</span> <span class="kw">false</span></span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>        <span class="fu">},</span></span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;status&quot;</span><span class="fu">:</span> <span class="st">&quot;ready&quot;</span><span class="fu">,</span></span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;outputResource&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;contentType&quot;</span><span class="fu">:</span> <span class="st">&quot;text/html&quot;</span></span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a>        <span class="fu">},</span></span>
<span id="cb1-17"><a href="#cb1-17" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;attachments&quot;</span><span class="fu">:</span> <span class="ot">[</span><span class="fu">{</span></span>
<span id="cb1-18"><a href="#cb1-18" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;contentType&quot;</span><span class="fu">:</span> <span class="st">&quot;image/png&quot;</span><span class="fu">,</span></span>
<span id="cb1-19"><a href="#cb1-19" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;fileName&quot;</span><span class="fu">:</span> <span class="st">&quot;img_0_46_0&quot;</span></span>
<span id="cb1-20"><a href="#cb1-20" aria-hidden="true" tabindex="-1"></a>        <span class="fu">}</span><span class="ot">,</span></span>
<span id="cb1-21"><a href="#cb1-21" aria-hidden="true" tabindex="-1"></a>        <span class="fu">{</span></span>
<span id="cb1-22"><a href="#cb1-22" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;contentType&quot;</span><span class="fu">:</span> <span class="st">&quot;image/png&quot;</span><span class="fu">,</span></span>
<span id="cb1-23"><a href="#cb1-23" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;fileName&quot;</span><span class="fu">:</span> <span class="st">&quot;img_0_0_0&quot;</span></span>
<span id="cb1-24"><a href="#cb1-24" aria-hidden="true" tabindex="-1"></a>        <span class="fu">}</span><span class="ot">,</span></span>
<span id="cb1-25"><a href="#cb1-25" aria-hidden="true" tabindex="-1"></a>        <span class="fu">{</span></span>
<span id="cb1-26"><a href="#cb1-26" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;contentType&quot;</span><span class="fu">:</span> <span class="st">&quot;image/jpeg&quot;</span><span class="fu">,</span></span>
<span id="cb1-27"><a href="#cb1-27" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;fileName&quot;</span><span class="fu">:</span> <span class="st">&quot;img_0_46_1&quot;</span></span>
<span id="cb1-28"><a href="#cb1-28" aria-hidden="true" tabindex="-1"></a>        <span class="fu">}</span><span class="ot">]</span></span>
<span id="cb1-29"><a href="#cb1-29" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span><span class="ot">,</span></span>
<span id="cb1-30"><a href="#cb1-30" aria-hidden="true" tabindex="-1"></a>    <span class="fu">{</span></span>
<span id="cb1-31"><a href="#cb1-31" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;id&quot;</span><span class="fu">:</span> <span class="st">&quot;4bac4889-0e63-4f09-bbe8-9593674f0700&quot;</span><span class="fu">,</span></span>
<span id="cb1-32"><a href="#cb1-32" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;options&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb1-33"><a href="#cb1-33" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;outputFormat&quot;</span><span class="fu">:</span> <span class="st">&quot;html&quot;</span><span class="fu">,</span></span>
<span id="cb1-34"><a href="#cb1-34" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;attachmentsPrefix&quot;</span><span class="fu">:</span> <span class="st">&quot;{contextPath}/rest_v2/reportExecutions/{reportExecutionId}/exports/{exportExecutionId}/attachments/&quot;</span><span class="fu">,</span></span>
<span id="cb1-35"><a href="#cb1-35" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;baseUrl&quot;</span><span class="fu">:</span> <span class="st">&quot;http://localhost:8080/jasperserver-pro&quot;</span><span class="fu">,</span></span>
<span id="cb1-36"><a href="#cb1-36" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;allowInlineScripts&quot;</span><span class="fu">:</span> <span class="kw">true</span></span>
<span id="cb1-37"><a href="#cb1-37" aria-hidden="true" tabindex="-1"></a>        <span class="fu">},</span></span>
<span id="cb1-38"><a href="#cb1-38" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;status&quot;</span><span class="fu">:</span> <span class="st">&quot;ready&quot;</span><span class="fu">,</span></span>
<span id="cb1-39"><a href="#cb1-39" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;outputResource&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb1-40"><a href="#cb1-40" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;contentType&quot;</span><span class="fu">:</span> <span class="st">&quot;text/html&quot;</span></span>
<span id="cb1-41"><a href="#cb1-41" aria-hidden="true" tabindex="-1"></a>        <span class="fu">},</span></span>
<span id="cb1-42"><a href="#cb1-42" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;attachments&quot;</span><span class="fu">:</span> <span class="ot">[</span><span class="fu">{</span></span>
<span id="cb1-43"><a href="#cb1-43" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;contentType&quot;</span><span class="fu">:</span> <span class="st">&quot;image/png&quot;</span><span class="fu">,</span></span>
<span id="cb1-44"><a href="#cb1-44" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;fileName&quot;</span><span class="fu">:</span> <span class="st">&quot;img_0_0_0&quot;</span></span>
<span id="cb1-45"><a href="#cb1-45" aria-hidden="true" tabindex="-1"></a>        <span class="fu">}</span><span class="ot">]</span></span>
<span id="cb1-46"><a href="#cb1-46" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span><span class="ot">]</span></span>
<span id="cb1-47"><a href="#cb1-47" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
</tbody>
</table>
