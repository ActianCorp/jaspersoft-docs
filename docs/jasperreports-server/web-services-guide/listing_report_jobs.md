---
title: Listing Report Jobs
description: "Use the following method to list jobs, either all jobs managed by the scheduler or the jobs for a specific report:"
---

# 1.0.1 Listing Report Jobs

Use the following method to list jobs, either all jobs managed by the scheduler or the jobs for a specific report:

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/jobs</span></p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/jobs</span>/path/to/report</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The body contains XML that describes jobs in the scheduler.</p></td>
<td><p>404 Not Found – When no job is not found in the server.</p></td>
</tr>
</tbody>
</table>

The jobs are described in the `jobsummary` element such as the following example:

!!! note

    The jobsummary XML element returned by the rest_v2/jobs service has a different structure than the element with the same name returned by the rest/jobsummary service.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">&lt;?xml</span> <span class="ot">version=</span><span class="st">&quot;1.0&quot;</span> <span class="ot">encoding=</span><span class="st">&quot;UTF-8&quot;</span> <span class="ot">standalone=</span><span class="st">&quot;yes&quot;</span><span class="fu">?&gt;</span> </span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">jobs</span>&gt; </span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>   &lt;<span class="kw">jobsummary</span>&gt; </span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">id</span>&gt;2042&lt;/<span class="kw">id</span>&gt; </span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">label</span>&gt;JUnit_Job_New&lt;/<span class="kw">label</span>&gt; </span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">reportUnitURI</span>&gt;/organizations/organization_1/reports/samples/AllAccounts</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>      &lt;/<span class="kw">reportUnitURI</span>&gt; </span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">state</span>&gt; </span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">nextFireTime</span>&gt;2222-02-04T13:47:00+02:00&lt;/<span class="kw">nextFireTime</span>&gt; </span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;NORMAL&lt;/<span class="kw">value</span>&gt; </span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">state</span>&gt; </span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">version</span>&gt;1&lt;/<span class="kw">version</span>&gt; </span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">jobsummary</span>&gt; </span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">jobs</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>
