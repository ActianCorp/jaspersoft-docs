---
title: 1.0.0.1 Viewing an Exclusion Calendar
description: "The following method takes the name of an exclusion calendar and returns the definition of the calendar:"
---

# 1.0.0.1 Viewing an Exclusion Calendar

The following method takes the name of an exclusion calendar and returns the definition of the calendar:

<table>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>GET</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/jobs/calendars</span>/&lt;calendarName&gt;/</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – Body is XML that contains the requested calendar.</p></td>
<td><p>404 Not Found – When the specified calendar name does not exist.</p></td>
</tr>
</tbody>
</table>

The calendar descriptor in the result has the following XML format:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">&lt;?xml</span> <span class="ot">version=</span><span class="st">&quot;1.0&quot;</span> <span class="ot">encoding=</span><span class="st">&quot;UTF-8&quot;</span> <span class="ot">standalone=</span><span class="st">&quot;yes&quot;</span><span class="fu">?&gt;</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">reportJobCalendar</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">baseCalendar</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">calendarType</span>&gt;base&lt;/<span class="kw">calendarType</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDates</span>/&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">description</span>&gt;Base calendar description&lt;/<span class="kw">description</span>&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDays</span>/&gt;</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">timeZone</span>&gt;GMT+03:00&lt;/<span class="kw">timeZone</span>&gt;</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">baseCalendar</span>&gt;</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">calendarType</span>&gt;daily&lt;/<span class="kw">calendarType</span>&gt;</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">excludeDates</span>/&gt;</span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">description</span>&gt;Main calendar description&lt;/<span class="kw">description</span>&gt;</span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">excludeDays</span>/&gt;</span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">invertTimeRange</span>&gt;false&lt;/<span class="kw">invertTimeRange</span>&gt;</span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">rangeEndingCalendar</span><span class="er"> </span> &gt;2012-03-20T14:44:37.353+03:00&lt;/<span class="kw">rangeEndingCalendar</span>&gt;</span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">rangeStartingCalendar</span>&gt;2012-03-20T14:43:37.353+03:00&lt;/<span class="kw">rangeStartingCalendar</span>&gt;</span>
<span id="cb1-17"><a href="#cb1-17" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">timeZone</span>&gt;GMT+03:00&lt;/<span class="kw">timeZone</span>&gt;</span>
<span id="cb1-18"><a href="#cb1-18" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">reportJobCalendar</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>
