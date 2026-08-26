---
title: 1.0.0.1 Adding or Updating an Exclusion Calendar
description: "This method creates a named exclusion calendar that you can use when scheduling reports. If the calendar already exists, you have the option of replacing it and updating all the jobs that used it."
---

# 1.0.0.1 Adding or Updating an Exclusion Calendar

This method creates a named exclusion calendar that you can use when scheduling reports. If the calendar already exists, you have the option of replacing it and updating all the jobs that used it.

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/jobs/calendars</span>/&lt;calendarName&gt;?&lt;arguments&gt;</p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p>replace?</p></td>
<td><p>true / false</p></td>
<td colspan="2"><p>If true, any calendar existing in the JobStore with the same name is overwritten. When this argument is omitted, it is false by default.</p></td>
</tr>
<tr>
<td><p>update<br />
Triggers?</p></td>
<td><p>true / false</p></td>
<td colspan="2"><p>Whether or not to update existing triggers that referenced the already existing calendar so that they are based on the new trigger.</p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p>application/xml</p></td>
<td colspan="2"><p>A well-formed XML calendar descriptor (see examples below).</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK –</p></td>
<td><p>404 Not Found – When the specified calendar name does not exist.</p></td>
</tr>
</tbody>
</table>

The following examples show the types of exclusion calendars that you can add to the scheduler:

-   Base calendar.

    <table>
    <colgroup>
    <col style="width: 100%" />
    </colgroup>
    <tbody>
    <tr>
    <td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">&lt;?xml</span> <span class="ot">version=</span><span class="st">&quot;1.0&quot;</span> <span class="ot">encoding=</span><span class="st">&quot;UTF-8&quot;</span> <span class="ot">standalone=</span><span class="st">&quot;yes&quot;</span><span class="fu">?&gt;</span></span>
    <span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">reportJobCalendar</span>&gt;</span>
    <span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">calendarType</span>&gt;base&lt;/<span class="kw">calendarType</span>&gt;</span>
    <span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">description</span>&gt;Base calendar description&lt;/<span class="kw">description</span>&gt;</span>
    <span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">timeZone</span>&gt;GMT+03:00&lt;/<span class="kw">timeZone</span>&gt;</span>
    <span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">reportJobCalendar</span>&gt;</span></code></pre></div></td>
    </tr>
    </tbody>
    </table>

-   Annual calendar – A list of days that you want to exclude every year.

    <table>
    <colgroup>
    <col style="width: 100%" />
    </colgroup>
    <tbody>
    <tr>
    <td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">&lt;?xml</span> <span class="ot">version=</span><span class="st">&quot;1.0&quot;</span> <span class="ot">encoding=</span><span class="st">&quot;UTF-8&quot;</span> <span class="ot">standalone=</span><span class="st">&quot;yes&quot;</span><span class="fu">?&gt;</span></span>
    <span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">reportJobCalendar</span>&gt;</span>
    <span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">calendarType</span>&gt;annual&lt;/<span class="kw">calendarType</span>&gt;</span>
    <span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">description</span>&gt;Annual calendar description&lt;/<span class="kw">description</span>&gt;</span>
    <span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">timeZone</span>&gt;GMT+03:00&lt;/<span class="kw">timeZone</span>&gt;</span></code></pre></div></td>
    </tr>
    <tr>
    <td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">excludeDays</span>&gt;</span>
    <span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDay</span>&gt;2012-03-20&lt;/<span class="kw">excludeDay</span>&gt;</span>
    <span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDay</span>&gt;2012-03-21&lt;/<span class="kw">excludeDay</span>&gt;</span>
    <span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDay</span>&gt;2012-03-22&lt;/<span class="kw">excludeDay</span>&gt;</span>
    <span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">excludeDays</span>&gt;</span>
    <span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">reportJobCalendar</span>&gt;</span></code></pre></div></td>
    </tr>
    </tbody>
    </table>

-   Cron calendar – Defines the days and times to exclude as a cron expression.

    <table>
    <colgroup>
    <col style="width: 100%" />
    </colgroup>
    <tbody>
    <tr>
    <td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">&lt;?xml</span> <span class="ot">version=</span><span class="st">&quot;1.0&quot;</span> <span class="ot">encoding=</span><span class="st">&quot;UTF-8&quot;</span> <span class="ot">standalone=</span><span class="st">&quot;yes&quot;</span><span class="fu">?&gt;</span></span>
    <span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">reportJobCalendar</span>&gt;</span>
    <span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">calendarType</span>&gt;cron&lt;/<span class="kw">calendarType</span>&gt;</span>
    <span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">description</span>&gt;Cron format description&lt;/<span class="kw">description</span>&gt;</span>
    <span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">cronExpression</span>&gt;0 30 10-13 ? * WED,FRI&lt;/<span class="kw">cronExpression</span>&gt;</span>
    <span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">timeZone</span>&gt;GMT+03:00&lt;/<span class="kw">timeZone</span>&gt;</span>
    <span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">reportJobCalendar</span>&gt;</span></code></pre></div></td>
    </tr>
    </tbody>
    </table>

-   Daily calendar – Defines a time range to exclude every day.

    <table>
    <colgroup>
    <col style="width: 100%" />
    </colgroup>
    <tbody>
    <tr>
    <td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">&lt;?xml</span> <span class="ot">version=</span><span class="st">&quot;1.0&quot;</span> <span class="ot">encoding=</span><span class="st">&quot;UTF-8&quot;</span> <span class="ot">standalone=</span><span class="st">&quot;yes&quot;</span><span class="fu">?&gt;</span></span>
    <span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">reportJobCalendar</span>&gt;</span>
    <span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">calendarType</span>&gt;daily&lt;/<span class="kw">calendarType</span>&gt;</span>
    <span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">description</span>&gt;Daily calendar description&lt;/<span class="kw">description</span>&gt;</span>
    <span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">invertTimeRange</span>&gt;false&lt;/<span class="kw">invertTimeRange</span>&gt;</span>
    <span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">rangeEndingCalendar</span>&gt;2012-03-20T14:44:37.353+03:00&lt;/<span class="kw">rangeEndingCalendar</span>&gt;</span>
    <span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">rangeStartingCalendar</span>&gt;2012-03-20T14:43:37.353+03:00&lt;/<span class="kw">rangeStartingCalendar</span>&gt;</span>
    <span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">timeZone</span>&gt;GMT+03:00&lt;/<span class="kw">timeZone</span>&gt;</span>
    <span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">reportJobCalendar</span>&gt;</span></code></pre></div></td>
    </tr>
    </tbody>
    </table>

-   Holiday calendar – Defines a set of days to exclude that can be updated every year.

    <table>
    <colgroup>
    <col style="width: 100%" />
    </colgroup>
    <tbody>
    <tr>
    <td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">&lt;?xml</span> <span class="ot">version=</span><span class="st">&quot;1.0&quot;</span> <span class="ot">encoding=</span><span class="st">&quot;UTF-8&quot;</span> <span class="ot">standalone=</span><span class="st">&quot;yes&quot;</span><span class="fu">?&gt;</span></span>
    <span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">reportJobCalendar</span>&gt;</span>
    <span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">calendarType</span>&gt;holiday&lt;/<span class="kw">calendarType</span>&gt;</span>
    <span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">description</span>&gt;Holiday calendar description&lt;/<span class="kw">description</span>&gt;</span>
    <span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">excludeDays</span>&gt;</span>
    <span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDay</span>&gt;2012-03-20&lt;/<span class="kw">excludeDay</span>&gt;</span>
    <span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDay</span>&gt;2012-03-21&lt;/<span class="kw">excludeDay</span>&gt;</span>
    <span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDay</span>&gt;2012-03-22&lt;/<span class="kw">excludeDay</span>&gt;</span>
    <span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">excludeDays</span>&gt;</span>
    <span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">timeZone</span>&gt;GMT+03:00&lt;/<span class="kw">timeZone</span>&gt;</span>
    <span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">reportJobCalendar</span>&gt;</span></code></pre></div></td>
    </tr>
    </tbody>
    </table>

-   Weekly calendar – Defines a set of days to be excluded each week.

    <table>
    <colgroup>
    <col style="width: 100%" />
    </colgroup>
    <tbody>
    <tr>
    <td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">&lt;?xml</span> <span class="ot">version=</span><span class="st">&quot;1.0&quot;</span> <span class="ot">encoding=</span><span class="st">&quot;UTF-8&quot;</span> <span class="ot">standalone=</span><span class="st">&quot;yes&quot;</span><span class="fu">?&gt;</span></span>
    <span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">reportJobCalendar</span>&gt;</span>
    <span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">calendarType</span>&gt;weekly&lt;/<span class="kw">calendarType</span>&gt;</span>
    <span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">description</span>&gt;test description&lt;/<span class="kw">description</span>&gt;</span>
    <span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">excludeDaysFlags</span>&gt;</span>
    <span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDayFlag</span>&gt;false&lt;/<span class="kw">excludeDayFlag</span>&gt; <span class="co">&lt;!--SUNDAY</span><span class="er">-</span><span class="co">--&gt;</span></span>
    <span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDayFlag</span>&gt;true&lt;/<span class="kw">excludeDayFlag</span>&gt;  <span class="co">&lt;!--MONDAY</span><span class="er">-</span><span class="co">--&gt;</span></span>
    <span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDayFlag</span>&gt;false&lt;/<span class="kw">excludeDayFlag</span>&gt;  <span class="co">&lt;!--TUESDAY</span><span class="er">-</span><span class="co">--&gt;</span></span>
    <span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDayFlag</span>&gt;true&lt;/<span class="kw">excludeDayFlag</span>&gt;  <span class="co">&lt;!--WEDNESDAY</span><span class="er">-</span><span class="co">--&gt;</span></span>
    <span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDayFlag</span>&gt;false&lt;/<span class="kw">excludeDayFlag</span>&gt;  <span class="co">&lt;!--THURSDAY</span><span class="er">-</span><span class="co">--&gt;</span></span>
    <span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDayFlag</span>&gt;true&lt;/<span class="kw">excludeDayFlag</span>&gt;  <span class="co">&lt;!--FRIDAY</span><span class="er">-</span><span class="co">--&gt;</span></span>
    <span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDayFlag</span>&gt;false&lt;/<span class="kw">excludeDayFlag</span>&gt;  <span class="co">&lt;!--SATURDAY</span><span class="er">-</span><span class="co">--&gt;</span></span>
    <span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">excludeDaysFlags</span>&gt;</span>
    <span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">timeZone</span>&gt;GMT+03:00&lt;/<span class="kw">timeZone</span>&gt;</span>
    <span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">reportJobCalendar</span>&gt;</span></code></pre></div></td>
    </tr>
    </tbody>
    </table>

-   Monthly calendar – Defines the dates to exclude every month.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">&lt;?xml</span> <span class="ot">version=</span><span class="st">&quot;1.0&quot;</span> <span class="ot">encoding=</span><span class="st">&quot;UTF-8&quot;</span> <span class="ot">standalone=</span><span class="st">&quot;yes&quot;</span><span class="fu">?&gt;</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">reportJobCalendar</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">calendarType</span>&gt;monthly&lt;/<span class="kw">calendarType</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">description</span>&gt;Monthly calendar description&lt;/<span class="kw">description</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">excludeDaysFlags</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDayFlag</span>&gt;true&lt;/<span class="kw">excludeDayFlag</span>&gt; <span class="co">&lt;!--01</span><span class="er">-</span><span class="co">--&gt;</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDayFlag</span>&gt;false&lt;/<span class="kw">excludeDayFlag</span>&gt; <span class="co">&lt;!--02</span><span class="er">-</span><span class="co">--&gt;</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDayFlag</span>&gt;true&lt;/<span class="kw">excludeDayFlag</span>&gt; <span class="co">&lt;!--03</span><span class="er">-</span><span class="co">--&gt;</span></span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDayFlag</span>&gt;false&lt;/<span class="kw">excludeDayFlag</span>&gt; <span class="co">&lt;!--04</span><span class="er">-</span><span class="co">--&gt;</span></span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDayFlag</span>&gt;true&lt;/<span class="kw">excludeDayFlag</span>&gt; <span class="co">&lt;!--05</span><span class="er">-</span><span class="co">--&gt;</span></span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDayFlag</span>&gt;false&lt;/<span class="kw">excludeDayFlag</span>&gt; <span class="co">&lt;!--06</span><span class="er">-</span><span class="co">--&gt;</span></span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDayFlag</span>&gt;true&lt;/<span class="kw">excludeDayFlag</span>&gt; <span class="co">&lt;!--07</span><span class="er">-</span><span class="co">--&gt;</span></span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDayFlag</span>&gt;false&lt;/<span class="kw">excludeDayFlag</span>&gt; <span class="co">&lt;!--08</span><span class="er">-</span><span class="co">--&gt;</span></span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDayFlag</span>&gt;true&lt;/<span class="kw">excludeDayFlag</span>&gt; <span class="co">&lt;!--09</span><span class="er">-</span><span class="co">--&gt;</span></span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDayFlag</span>&gt;false&lt;/<span class="kw">excludeDayFlag</span>&gt; <span class="co">&lt;!--10</span><span class="er">-</span><span class="co">--&gt;</span></span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDayFlag</span>&gt;true&lt;/<span class="kw">excludeDayFlag</span>&gt; <span class="co">&lt;!--11</span><span class="er">-</span><span class="co">--&gt;</span></span>
<span id="cb1-17"><a href="#cb1-17" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDayFlag</span>&gt;false&lt;/<span class="kw">excludeDayFlag</span>&gt; <span class="co">&lt;!--12</span><span class="er">-</span><span class="co">--&gt;</span></span>
<span id="cb1-18"><a href="#cb1-18" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDayFlag</span>&gt;false&lt;/<span class="kw">excludeDayFlag</span>&gt; <span class="co">&lt;!--13</span><span class="er">-</span><span class="co">--&gt;</span></span>
<span id="cb1-19"><a href="#cb1-19" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDayFlag</span>&gt;true&lt;/<span class="kw">excludeDayFlag</span>&gt; <span class="co">&lt;!--14</span><span class="er">-</span><span class="co">--&gt;</span></span>
<span id="cb1-20"><a href="#cb1-20" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDayFlag</span>&gt;false&lt;/<span class="kw">excludeDayFlag</span>&gt; <span class="co">&lt;!--15</span><span class="er">-</span><span class="co">--&gt;</span></span>
<span id="cb1-21"><a href="#cb1-21" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDayFlag</span>&gt;false&lt;/<span class="kw">excludeDayFlag</span>&gt; <span class="co">&lt;!--16</span><span class="er">-</span><span class="co">--&gt;</span></span>
<span id="cb1-22"><a href="#cb1-22" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDayFlag</span>&gt;false&lt;/<span class="kw">excludeDayFlag</span>&gt; <span class="co">&lt;!--17</span><span class="er">-</span><span class="co">--&gt;</span></span>
<span id="cb1-23"><a href="#cb1-23" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDayFlag</span>&gt;false&lt;/<span class="kw">excludeDayFlag</span>&gt; <span class="co">&lt;!--18</span><span class="er">-</span><span class="co">--&gt;</span></span>
<span id="cb1-24"><a href="#cb1-24" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDayFlag</span>&gt;false&lt;/<span class="kw">excludeDayFlag</span>&gt; <span class="co">&lt;!--19</span><span class="er">-</span><span class="co">--&gt;</span></span>
<span id="cb1-25"><a href="#cb1-25" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDayFlag</span>&gt;false&lt;/<span class="kw">excludeDayFlag</span>&gt; <span class="co">&lt;!--20</span><span class="er">-</span><span class="co">--&gt;</span></span>
<span id="cb1-26"><a href="#cb1-26" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDayFlag</span>&gt;false&lt;/<span class="kw">excludeDayFlag</span>&gt; <span class="co">&lt;!--21</span><span class="er">-</span><span class="co">--&gt;</span></span>
<span id="cb1-27"><a href="#cb1-27" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDayFlag</span>&gt;false&lt;/<span class="kw">excludeDayFlag</span>&gt; <span class="co">&lt;!--22</span><span class="er">-</span><span class="co">--&gt;</span></span>
<span id="cb1-28"><a href="#cb1-28" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDayFlag</span>&gt;false&lt;/<span class="kw">excludeDayFlag</span>&gt; <span class="co">&lt;!--23</span><span class="er">-</span><span class="co">--&gt;</span></span>
<span id="cb1-29"><a href="#cb1-29" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDayFlag</span>&gt;false&lt;/<span class="kw">excludeDayFlag</span>&gt; <span class="co">&lt;!--24</span><span class="er">-</span><span class="co">--&gt;</span></span>
<span id="cb1-30"><a href="#cb1-30" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDayFlag</span>&gt;false&lt;/<span class="kw">excludeDayFlag</span>&gt; <span class="co">&lt;!--25</span><span class="er">-</span><span class="co">--&gt;</span></span></code></pre></div></td>
</tr>
<tr>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDayFlag</span>&gt;false&lt;/<span class="kw">excludeDayFlag</span>&gt; <span class="co">&lt;!--26</span><span class="er">-</span><span class="co">--&gt;</span></span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDayFlag</span>&gt;false&lt;/<span class="kw">excludeDayFlag</span>&gt; <span class="co">&lt;!--27</span><span class="er">-</span><span class="co">--&gt;</span></span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDayFlag</span>&gt;false&lt;/<span class="kw">excludeDayFlag</span>&gt; <span class="co">&lt;!--28</span><span class="er">-</span><span class="co">--&gt;</span></span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDayFlag</span>&gt;false&lt;/<span class="kw">excludeDayFlag</span>&gt; <span class="co">&lt;!--29</span><span class="er">-</span><span class="co">--&gt;</span></span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDayFlag</span>&gt;false&lt;/<span class="kw">excludeDayFlag</span>&gt; <span class="co">&lt;!--30</span><span class="er">-</span><span class="co">--&gt;</span></span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">excludeDayFlag</span>&gt;false&lt;/<span class="kw">excludeDayFlag</span>&gt; <span class="co">&lt;!--31</span><span class="er">-</span><span class="co">--&gt;</span></span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">excludeDaysFlags</span>&gt;</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">timeZone</span>&gt;GMT+03:00&lt;/<span class="kw">timeZone</span>&gt;</span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">reportJobCalendar</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>
