---
title: Finding Running Reports and Jobs
description: "The v2/reportExecutions service provides a method to search for reports that are running on the server, including report jobs triggered by the scheduler."
---

# Finding Running Reports and Jobs

The v2/reportExecutions service provides a method to search for reports that are running on the server, including report jobs triggered by the scheduler.

To search for running reports, use the search arguments with the following URL:

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/report</span><strong>Executions</strong>?&lt;arguments&gt;</p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><code>reportURI</code></p></td>
<td><p>Optional String</p></td>
<td colspan="2"><p>This string matches the repository URI of the running report, relative the currently logged-in user’s organization.</p></td>
</tr>
<tr>
<td><p><code>jobID</code></p></td>
<td><p>Optional String</p></td>
<td colspan="2"><p>For scheduler jobs, this argument matches the ID of the job that triggered the running repot.</p></td>
</tr>
<tr>
<td><p><code>jobLabel</code></p></td>
<td><p>Optional String</p></td>
<td colspan="2"><p>For scheduler jobs, this argument matches the name of the job that triggered the running repot.</p></td>
</tr>
<tr>
<td><p><code>userName</code></p></td>
<td><p>Optional String</p></td>
<td colspan="2"><p>For scheduler jobs, this argument matches the user ID that created the job.</p></td>
</tr>
<tr>
<td><p>fireTimeFrom</p></td>
<td rowspan="2"><p>Optional<br />
Date/Time</p></td>
<td colspan="2" rowspan="2"><p>For scheduler jobs, the fire time arguments define a range of time that matches if the job that is currently running was triggered during this time. You can specify either or both of the arguments. Specify the date and time in the following pattern: yyyy-MM-dd'T'HH:mmZ.</p></td>
</tr>
<tr>
<td><p>fireTimeTo</p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p>accept: application/xml (default)</p>
<p>accept: application/json</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The content is a descriptor for each of the matching results.</p>
<p>204 No Content – When the search results are empty.</p></td>
<td></td>
</tr>
</tbody>
</table>

The response contains a list of summary `reportExecution` descriptors, for example in XML:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">reportExecutions</span>&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">reportExecution</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">reportURI</span>&gt;repo:/supermart/details/CustomerDetailReport&lt;/<span class="kw">reportURI</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">requestId</span>&gt;2071593484_1355224559918_5&lt;/<span class="kw">requestId</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">reportExecution</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">reportExecutions</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

Given the request ID, you can obtain more information about each result by downloading the full `reportExecution` descriptor, as described in section [Requesting Report Execution Details](requesting_report_execution_details.md).

For security purposes, the search for running reports is has the following restrictions:

-   The system administrator (`superuser`) can see and cancel any report running on the server.
-   An organization admin (`jasperadmin`) can see every running report, but can cancel only the reports that were started by a user of the same organization or one of its child organizations.
-   A regular user can see every running report, but can cancel only the reports that he initiated.
