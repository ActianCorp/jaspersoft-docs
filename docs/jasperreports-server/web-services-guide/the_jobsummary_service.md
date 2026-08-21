---
title: The jobsummary Service
description: The rest/jobsummary service is superseded by The v2/jobs Service.
---

# 1.1 The jobsummary Service

!!! note

    The rest/jobsummary service is superseded by [The v2/jobs Service](the_v2_jobs_service.md).

In order to schedule reports and interact with jobs that are created to run a report at a later time, the REST API provides two services:

- The jobsummary service lists all currently defined jobs on a given report.
- The job service lets you create, modify, and delete a specific job.

The jobsummary service is a read only service. Requests for PUT, POST, and DELETE operations receive the error 405, method not allowed.

<table>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>GET</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest/jobsummary</span>/path/to/report/</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The body contains XML that describes all the active jobs</p></td>
<td><p>404 Not Found – When the specified report is not found in the server.</p></td>
</tr>
</tbody>
</table>

The jobs are described in `jobsummary` elements such as the following example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">jobs</span>&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">jobsummary</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">id</span>&gt;22164&lt;/<span class="kw">id</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">label</span>&gt;MyJob&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">nextFireTime</span>&gt;2011-11-11T11:11:11-08:00&lt;/<span class="kw">nextFireTime</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">reportUnitURI</span>&gt;/organizations/organization_1/reports/samples/AllAccounts</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>      &lt;/<span class="kw">reportUnitURI</span>&gt;</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">state</span>&gt;</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;NORMAL&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">state</span>&gt;</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">version</span>&gt;0&lt;/<span class="kw">version</span>&gt;</span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">jobsummary</span>&gt;</span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">jobsummary</span>&gt;</span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>  ...</span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">jobsummary</span>&gt;</span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">jobs</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

The job summary gives the ID of the job that you need to interact with it using the job service. It also gives the next occurrence (“fire time”) of the job, and its status that would indicate any errors.
