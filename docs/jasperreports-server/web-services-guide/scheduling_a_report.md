---
title: Scheduling a Report
description: "To schedule a report, create its job descriptor and use the PUT method of the job service. Specify the report being scheduled inside the job descriptor. You do not need to specify any job IDs in the..."
---

# 1.0.1 Scheduling a Report

To schedule a report, create its job descriptor and use the PUT method of the job service. Specify the report being scheduled inside the job descriptor. You do not need to specify any job IDs in the descriptor, because the server will assign them.

<table>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>PUT</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest/job/</span></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p>text/plain</p></td>
<td colspan="2"><p>A well-formed XML job descriptor.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>201 Created – The body contains XML Job descriptor. This is the only case where a descriptor returns for a put request and that id due to the fact that the job id (the job handle) is created in the server.</p></td>
<td><p>404 Not Found – When the report specified in the job descriptor is not found in the server.</p></td>
</tr>
</tbody>
</table>

The output formats are those supported by JasperReports server, as given by the following values:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td><ul>
<li>PDF</li>
</ul></td>
<td><ul>
<li>XLS</li>
</ul></td>
<td><ul>
<li>DOCX</li>
</ul></td>
</tr>
<tr>
<td><ul>
<li>HTML</li>
</ul></td>
<td><ul>
<li>XLS_NOPAG</li>
</ul></td>
<td><ul>
<li>RTF</li>
</ul></td>
</tr>
<tr>
<td><ul>
<li>CSV</li>
</ul></td>
<td><ul>
<li>XLSX</li>
</ul></td>
<td><ul>
<li>ODT</li>
</ul></td>
</tr>
<tr>
<td><ul>
<li>ODS</li>
</ul></td>
<td><ul>
<li>XLSX_NOPAG</li>
</ul></td>
<td></td>
</tr>
</tbody>
</table>

The recurrence can be defined as follows:

- No recurrence (single run), for example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">simpleTrigger</span>&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">startDate</span>&gt;2011-11-11T11:11:11-08:00&lt;/<span class="kw">startDate</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">timezone</span>&gt;America/Los_Angeles&lt;/<span class="kw">timezone</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">version</span>&gt;0&lt;/<span class="kw">version</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">occurrenceCount</span>&gt;1&lt;/<span class="kw">occurrenceCount</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">simpleTrigger</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

- Simple recurrence, for example every day until a given date:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">simpleTrigger</span>&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">endDate</span>&gt;2011-11-11T11:11:11-08:00&lt;/<span class="kw">endDate</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">startDate</span>&gt;2012-12-12T12:12:12-08:00&lt;/<span class="kw">startDate</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">timezone</span>&gt;America/Los_Angeles&lt;/<span class="kw">timezone</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">version</span>&gt;0&lt;/<span class="kw">version</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">occurrenceCount</span>&gt;-1&lt;/<span class="kw">occurrenceCount</span>&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">recurrenceInterval</span>&gt;1&lt;/<span class="kw">recurrenceInterval</span>&gt;</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">recurrenceIntervalUnit</span>&gt;</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;DAY&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">recurrenceIntervalUnit</span>&gt;</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">simpleTrigger</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

- Calendar recurrence, for example every Tuesday and Thursday in February, April, and June until next year:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="language-text highlight"><pre><code>&lt; &lt;calendarTrigger&gt;
    &lt;endDate&gt;2012-12-12T12:12:12-08:00&lt;/endDate&gt;
    &lt;timezone&gt;America/Los_Angeles&lt;/timezone&gt;
    &lt;version&gt;0&lt;/version&gt;
    &lt;daysType&gt;&lt;value&gt;WEEK&lt;/value&gt;&lt;/daysType&gt;
    &lt;hours&gt;0&lt;/hours&gt;
    &lt;minutes&gt;0&lt;/minutes&gt;
    &lt;monthDays&gt;&lt;/monthDays&gt;
    &lt;months&gt;2&lt;/months&gt;
    &lt;months&gt;4&lt;/months&gt;
    &lt;months&gt;6&lt;/months&gt;
    &lt;weekDays&gt;3&lt;/weekDays&gt;
    &lt;weekDays&gt;5&lt;/weekDays&gt;
  &lt;/calendarTrigger&gt;</code></pre></div></td>
</tr>
</tbody>
</table>
