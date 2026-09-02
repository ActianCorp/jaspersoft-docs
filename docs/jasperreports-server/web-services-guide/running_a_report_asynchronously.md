---
title: Running a Report Asynchronously
description: "In order to run a report asynchronously, the v2/reportExecutions service provides a method to specify all the parameters needed to launch a report. Report parameters are all sent as a..."
---

# Running a Report Asynchronously

In order to run a report asynchronously, the v2/reportExecutions service provides a method to specify all the parameters needed to launch a report. Report parameters are all sent as a `reportExecutionRequest` object. The response from the server contains the request ID needed to track the execution until completion.

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/report</span><strong>Executions</strong></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p>application/xml</p>
<p>application/json</p></td>
<td colspan="2"><p>A complete <code>ReportExecutionRequest</code> in either XML or JSON format. See the example and table below for an explanation of its properties.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The content contains a ReportExecution descriptor. See below for an example</p></td>
<td><p>403 Forbidden – When the logged-in user does not have permission to access the report in the request.</p>
<p>404 Not Found – When the report URI specified in the request does not exist.</p></td>
</tr>
</tbody>
</table>

The following example shows the structure of the `ReportExecutionRequest`:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">reportExecutionRequest</span>&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">reportUnitUri</span>&gt;/supermart/details/CustomerDetailReport&lt;/<span class="kw">reportUnitUri</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">async</span>&gt;true&lt;/<span class="kw">async</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">freshData</span>&gt;false&lt;/<span class="kw">freshData</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">saveDataSnapshot</span>&gt;false&lt;/<span class="kw">saveDataSnapshot</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">outputFormat</span>&gt;html&lt;/<span class="kw">outputFormat</span>&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">interactive</span>&gt;true&lt;/<span class="kw">interactive</span>&gt;</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">ignorePagination</span>&gt;false&lt;/<span class="kw">ignorePagination</span>&gt;</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">pages</span>&gt;1-5&lt;/<span class="kw">pages</span>&gt;</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">parameters</span>&gt;</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">reportParameter</span> <span class="ot">name=</span><span class="st">&quot;someParameterName&quot;</span>&gt;</span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">value</span>&gt;value 1&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">value</span>&gt;value 2&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">reportParameter</span>&gt;</span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">reportParameter</span> <span class="ot">name=</span><span class="st">&quot;someAnotherParameterName&quot;</span>&gt;</span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">value</span>&gt;another value&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-17"><a href="#cb1-17" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">reportParameter</span>&gt;</span>
<span id="cb1-18"><a href="#cb1-18" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">parameters</span>&gt;</span>
<span id="cb1-19"><a href="#cb1-19" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">reportExecutionRequest</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

The following table describes the properties you can specify in the `ReportExecutionRequest`:

**Report Execution Properties**

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th><p>Property</p></th>
<th><p>Required or Default</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="language-text highlight"><pre><code>reportUnitUri</code></pre></div></td>
<td><p>Required</p></td>
<td><p>Repository path (URI) of the report to run. For commercial editions with organizations, the URI is relative the the logged-in user’s organization.</p></td>
</tr>
<tr>
<td><div class="language-text highlight"><pre><code>outputFormat</code></pre></div></td>
<td><p>Required</p></td>
<td><p>Specifies the desired output format: pdf, html, xls, xlsx, rtf, csv, xml, docx, odt, ods, jrprint.</p>
<p>As of JasperReports® Server 6.0, it is also possible to specify json if your reports are designed for data export. For more information, see the JasperReports® Library samples documentation.</p></td>
</tr>
<tr>
<td><div class="language-text highlight"><pre><code>freshData</code></pre></div></td>
<td><p>false</p></td>
<td><p>When data snapshots are enabled, specifies whether the report should get fresh data by querying the data source or if false, use a previously saved data snapshot (if any). By default, if a saved data snapshot exists for the report it will be used when running the report.</p></td>
</tr>
<tr>
<td><div class="language-text highlight"><pre><code>saveDataSnapshot</code></pre></div></td>
<td><p>false</p></td>
<td><p>When data snapshots are enabled, specifies whether the data snapshot for the report should be written or overwritten with the new data from this execution of the report.</p></td>
</tr>
<tr>
<td><div class="language-text highlight"><pre><code>interactive</code></pre></div></td>
<td><p>true</p></td>
<td><p>In a commercial editions of the server where HighCharts are used in the report, this property determines whether the JavaScript necessary for interaction is generated and returned as an attachment when exporting to HTML. If false, the chart is generated as a non-interactive image file (also as an attachment).</p></td>
</tr>
<tr>
<td><div class="language-text highlight"><pre><code>allowInlineScripts</code></pre></div></td>
<td>true</td>
<td>Affects HTML export only. If true, then inline scripts are allowed, otherwise no inline script is included in the HTML output.</td>
</tr>
<tr>
<td><div class="language-text highlight"><pre><code>ignorePagination</code></pre></div></td>
<td><p>Optional</p></td>
<td><p>When set to true, the report is generated as a single long page. This can be used with HTML output to avoid pagination. When omitted, the ignorePagination property on the JRXML, if any, is used.</p></td>
</tr>
<tr>
<td><div class="language-text highlight"><pre><code>pages</code></pre></div></td>
<td><p>Optional</p></td>
<td><p>Specify a page range to generate a partial report. The format is &lt;startPageNumber&gt;-&lt;endPageNumber&gt;</p></td>
</tr>
<tr>
<td><div class="language-text highlight"><pre><code>async</code></pre></div></td>
<td><p>false</p></td>
<td><p>Determines whether reportExecution is synchronous or asynchronous. When set to true, the response is sent immediately and the client must poll the report status and later download the result when ready. By default, this property is false and the operation will wait until the report execution is complete, forcing the client to wait as well, but allowing the client to download the report immediately after the response.</p></td>
</tr>
<tr>
<td><div class="language-text highlight"><pre><code>transformerKey</code></pre></div></td>
<td><p>Optional</p></td>
<td><p>Advanced property used when requesting a report as a JasperPrint object. This property can specify a JasperReports Library generic print element transformers of class net.sf.jasperreports.engine.export. GenericElementTransformer. These transformers are pluggable as JasperReports. extensions</p></td>
</tr>
<tr>
<td><div class="language-text highlight"><pre><code>attachmentsPrefix</code></pre></div></td>
<td><p>attachments</p></td>
<td><p>For HTML output, this property specifies the URL path to use fo downloading the attachment files (JavaScript and images). The full path of the default value is:</p>
<p>{contextPath}/rest_v2/reportExecutions/{reportExecutionId}/exports/{exportExecutionId}/attachments/</p>
<p>You can specify a different URL path using the placeholders {contextPath}, {reportExecutionId} and {exportExecutionId}.</p></td>
</tr>
<tr>
<td><div class="language-text highlight"><pre><code>baseURL</code></pre></div></td>
<td>String</td>
<td>Specifies the base URL that the report will use to load static resources such as JavaScript files. You can also set the deploy.base.url property in the WEB-INF/js.config.properties file to set this value permanently. If both are set, the baseUrl parameter in this request takes precedence.</td>
</tr>
<tr>
<td><div class="language-text highlight"><pre><code>parameters</code></pre></div></td>
<td></td>
<td><p>A list of input control parameters and their values.</p></td>
</tr>
</tbody>
</table>

When successful, the reply from the server contains the `reportExecution` descriptor. This descriptor contains the request ID and status needed in order for the client to request the output. There are two statuses, one for the report execution itself, and one for the chosen output format. The following descriptor shows that the report is still executing (&lt;status&gt;execution&lt;/status&gt;).

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">reportExecution</span>&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">currentPage</span>&gt;1&lt;/<span class="kw">currentPage</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">exports</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">export</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">id</span>&gt;html&lt;/<span class="kw">id</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">status</span>&gt;queued&lt;/<span class="kw">status</span>&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">export</span>&gt;</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">exports</span>&gt;</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">reportURI</span>&gt;/supermart/details/CustomerDetailReport&lt;/<span class="kw">reportURI</span>&gt;</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">requestId</span>&gt;f3a9805a-4089-4b53-b9e9-b54752f91586&lt;/<span class="kw">requestId</span>&gt;</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">status</span>&gt;execution&lt;/<span class="kw">status</span>&gt;</span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">reportExecution</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

The value of the `async` property in the request determines whether or not the report output is available when the response is received. Your client should implement either synchronous or asynchronous processing of the response depending on the value you set for the `async` property.
