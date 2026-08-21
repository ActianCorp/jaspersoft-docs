---
title: Running a Report
description: The PUT request for the report service runs the report and generates the specified output. The response contains the ID of the saved output for downloading later with a GET request.
---

# 1.0.1 Running a Report

The PUT request for the report service runs the report and generates the specified output. The response contains the ID of the saved output for downloading later with a GET request.

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
<td><p>PUT</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest/report</span>/path/to/report</p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><code>RUN_OUTPUT_FORMAT?</code></p></td>
<td><p>OutputType</p></td>
<td colspan="2"><p>The format of the report output. The possible values are: PDF, HTML, XLS, XLSX, RTF, CSV, XML, DOCX, ODT, ODS, JRPRINT. The Default is PDF.</p></td>
</tr>
<tr>
<td><p>&lt;Resource<br />
Descriptor&gt;</p></td>
<td><p>String</p></td>
<td colspan="2"><p>Argument used to pass a transformer key to be used when running a report using JRPRINT as output format. The transformer key will be used to transform generic elements in the generated report as per net.sf.jasperreports.engine. export.GenericElementReportTransformer. This is a required argument when using multipart requests.</p></td>
</tr>
<tr>
<td><pre class="text"><code>interactive?</code></pre></td>
<td><p>Boolean</p></td>
<td colspan="2"><p>In a commercial editions of the server where HighCharts are used in the report, this property determines whether the JavaScript necessary for interaction is generated when exporting to HTML. By default it is true. If set to false, the chart is generated as a non-interactive image file.</p></td>
</tr>
<tr>
<td><pre class="text"><code>IMAGES_URI?</code></pre></td>
<td><p>String</p></td>
<td colspan="2"><p>The uri prefix used for images when exporting in HTML. The default is <code>images</code>.</p></td>
</tr>
<tr>
<td><pre class="text"><code>X-Method-Override?</code></pre></td>
<td><p>POST</p></td>
<td colspan="2"><p>This method can be used to perform a POST instead of a PUT.</p></td>
</tr>
<tr>
<td><pre class="text"><code>PAGE?</code></pre></td>
<td><p>Integer &gt; 0</p></td>
<td colspan="2"><p>An integer value used to export a specific page</p></td>
</tr>
<tr>
<td><pre class="text"><code>ignorePagination</code></pre></td>
<td><p>Boolean</p></td>
<td colspan="2"><p>When true, the report output will be generated on a single page in all export formats. When false or omitted, all export formats will be paginated.</p></td>
</tr>
<tr>
<td><p><code>onePagePerSheet</code><br />
</p></td>
<td><p>Boolean</p></td>
<td colspan="2"><p>Valid only for the XLS format. When true, each page of the report is on a separate spreadsheet. When false or omitted, the entire report is on a single spreadsheet. If your reports are very long, set this argument to true, otherwise the report will not fit on a single spreadsheet and cause an error.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The body is XML containing a summary of the report execution (UUID, pages, generated files, etc...). See sample return below.</p></td>
<td><p>404 Not Found – When the specified report URI is not found in the repository.</p></td>
</tr>
</tbody>
</table>

The body of the PUT request should contain a resource descriptor of type `reportUnit` with the URI of the report unit to run. The resource descriptor can contain one or more parameter tags to specify parameters. Lists can be passed using parameters with the same name and the `isListItem` attribute set to true.

The arguments can be placed in the URL of the request or by encoding them in the multipart request. However, some application servers such as Apache Tomcat do not process arguments that are www-url-encoded in the request when sent to a PUT method, so be sure you are using a multipart request or you are using the GET style parameters when using this method.

The return value of the PUT request provides the UUID of the report output in this session and the ID of the files.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">report</span>&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">uuid</span>&gt;d7bf6c9-9077-41f7-a2d4-8682e74b637e&lt;/<span class="kw">uuid</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">originalUri</span>&gt;/reports/samples/AllAccounts&lt;/<span class="kw">originalUri</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">totalPages</span>&gt;43&lt;/<span class="kw">totalPages</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">startPage</span>&gt;1&lt;/<span class="kw">startPage</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">endPage</span>&gt;43&lt;/<span class="kw">endPage</span>&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">file</span> <span class="ot">type=</span><span class="st">&quot;image/png&quot;</span>&gt;img_0_0_0&lt;/<span class="kw">file</span>&gt;</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">file</span> <span class="ot">type=</span><span class="st">&quot;image/gif&quot;</span>&gt;px&lt;/<span class="kw">file</span>&gt;</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">file</span> <span class="ot">type=</span><span class="st">&quot;text/html&quot;</span>&gt;report&lt;/<span class="kw">file</span>&gt;</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">file</span> <span class="ot">type=</span><span class="st">&quot;image/jpeg&quot;</span>&gt;img_0_42_27&lt;/<span class="kw">file</span>&gt;</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">file</span> <span class="ot">type=</span><span class="st">&quot;image/png&quot;</span>&gt;img_0_42_26&lt;/<span class="kw">file</span>&gt;</span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">report</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>
