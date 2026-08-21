---
title: Updating Jobs in Bulk
description: The POST method also supports other parameters to perform bulk updates on scheduled jobs.
---

# 1.0.1 Updating Jobs in Bulk

The POST method also supports other parameters to perform bulk updates on scheduled jobs.

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/jobs</span>?&lt;arguments&gt;</p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p>id?</p></td>
<td><p>jobID string</p></td>
<td colspan="2"><p>Can be used multiple times to create a list of jobIDs to update</p></td>
</tr>
<tr>
<td><p>replace<br />
Trigger<br />
IgnoreType</p></td>
<td><p>true / false</p></td>
<td colspan="2"><p>When true, the trigger is replaced from the content being sent and the trigger type is ignored. When false or omitted, the trigger is updated automatically by the scheduler.</p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p>application/xml</p></td>
<td colspan="2"><p>A well-formed XML jobModel descriptor. The jobModel is a fragment of a job descriptor containing only the fields to be updated. See example below.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – Body empty.</p></td>
<td><p>404 Not Found – When the specified job is not found in the server.</p></td>
</tr>
</tbody>
</table>

For example, the following request will update the job description in several jobs:

POST request: http://localhost:8080/jasperserver-pro/rest_v2/jobs?id=3798&id=3799&id=3800

And the body of the request contains:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">jobModel</span>&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">description</span>&gt;This description updated in bulk&lt;/<span class="kw">description</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">jobModel</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>
