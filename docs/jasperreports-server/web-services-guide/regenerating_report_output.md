---
title: Regenerating Report Output
description: "To export a report in a different format after its first execution, or to export a specific page, use the POST method of the report service. For example, it is possible to download the report one..."
---

# 1.0.1 Regenerating Report Output

To export a report in a different format after its first execution, or to export a specific page, use the POST method of the report service. For example, it is possible to download the report one page at a time by repeatedly sending the appropriate POST and GET requests.

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest/report</span>/&lt;UUID&gt;?&lt;arguments&gt; (see example below)</p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><pre class="text"><code>RUN_OUTPUT_FORMAT?</code></pre></td>
<td><p>OutputType</p></td>
<td colspan="2"><p>The format of the report output. Possible values: PDF, HTML, XLS, RTF, CSV, XML, JRPRINT. The Default is PDF.</p></td>
</tr>
<tr>
<td><pre class="text"><code>IMAGES_URI?</code></pre></td>
<td><p>String</p></td>
<td colspan="2"><p>The uri prefix used for images when exporting in HTML. The default is <code>images</code>.</p></td>
</tr>
<tr>
<td><pre class="text"><code>PAGE?</code></pre></td>
<td><p>Integer &gt; 0</p></td>
<td colspan="2"><p>An integer value used to export a specific page.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The new details of the report. The old files produces are discarded and replaced with new ones.</p></td>
<td><p>404 Not Found – When the specified UUID is not found in the user’s session.</p></td>
</tr>
</tbody>
</table>

For example, the following request exports page 10 of the PDF report:

POST http://host/rest/report/d7bf6c9-9077-41f7-a2d4-8682e74b637e?PAGE=10&RUN_OUTPUT_FORMAT=PDF

You then need to take the file name from the return value and create a GET request for it.
