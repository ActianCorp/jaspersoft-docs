---
title: Deleting Jobs
description: Use the DELETE method to remove jobs from the scheduler. There are two forms to specify a single job or multiple jobs to delete.
---

# Deleting Jobs

Use the DELETE method to remove jobs from the scheduler. There are two forms to specify a single job or multiple jobs to delete.

<table>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>DELETE</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/jobs</span>/&lt;jobID&gt;/</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The body contains the deleted job ID.</p></td>
<td>404 Not Found – When the specified job is not found in the server.</td>
</tr>
</tbody>
</table>

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
<td><p>DELETE</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/jobs</span>?&lt;arguments&gt;</p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><code>id</code></p></td>
<td><p>Multiple String</p></td>
<td colspan="2"><p>Enter as many job IDs as you want to delete, for example:</p>
<p>?id=5594&amp;id=5645&amp;id=5761</p></td>
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
<td colspan="3"><p>200 OK – The content is a list of deleted jobs.</p></td>
<td></td>
</tr>
</tbody>
</table>

The list of deleted jobs in the response has the following structure:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">JSON</span><span class="kw">:</span><span class="at"> </span><span class="kw">{</span><span class="st">&quot;jobId&quot;</span><span class="at">:[5594</span><span class="kw">,</span><span class="at">5645]</span><span class="kw">}</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a><span class="fu">XML</span><span class="kw">:</span><span class="at"> &lt;jobIdList&gt;</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="at">         &lt;jobId&gt;5594&lt;/jobId&gt;</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a><span class="at">         &lt;jobId&gt;5645&lt;/jobId&gt;</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a><span class="at">     &lt;/jobIdList&gt;</span></span></code></pre></div></td>
</tr>
</tbody>
</table>
