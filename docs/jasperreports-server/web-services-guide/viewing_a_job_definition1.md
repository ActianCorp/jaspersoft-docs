---
title: Viewing a Job Definition
description: The GET method with a specific job ID retrieves the detailed information about that scheduled job.
---

# Viewing a Job Definition

The GET method with a specific job ID retrieves the detailed information about that scheduled job.

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/jobs</span>/&lt;jobID&gt;/</p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p>accept: application/xml (default)</p>
<p>accept: application/job+json (provides advanced features, as described below)</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The body contains XML that describes all the job properties.</p></td>
<td><p>404 Not Found – When the specified job is not found in the server.</p></td>
</tr>
</tbody>
</table>

The GET method returns a `job` element that gives the output, scheduling, and parameter details, if any, for the job.

!!! note

    The job XML element returned by the rest_v2/jobs service has a different structure than the element with the same name returned by the rest/job service.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">&lt;?xml</span> <span class="ot">version=</span><span class="st">&quot;1.0&quot;</span> <span class="ot">encoding=</span><span class="st">&quot;UTF-8&quot;</span> <span class="ot">standalone=</span><span class="st">&quot;yes&quot;</span><span class="fu">?&gt;</span> </span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">job</span>&gt; </span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">baseOutputFilename</span>&gt;AllAccounts&lt;/<span class="kw">baseOutputFilename</span>&gt; </span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">repositoryDestination</span>&gt; </span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">folderURI</span>&gt;/reports/samples&lt;/<span class="kw">folderURI</span>&gt; </span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">id</span>&gt;2041&lt;/<span class="kw">id</span>&gt; </span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">outputDescription</span>/&gt; </span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">overwriteFiles</span>&gt;false&lt;/<span class="kw">overwriteFiles</span>&gt; </span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">sequentialFilenames</span>&gt;false&lt;/<span class="kw">sequentialFilenames</span>&gt; </span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">version</span>&gt;0&lt;/<span class="kw">version</span>&gt; </span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">repositoryDestination</span>&gt; </span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">description</span>/&gt; </span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">id</span>&gt;2042&lt;/<span class="kw">id</span>&gt; </span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">label</span>&gt;MyNewJob&lt;/<span class="kw">label</span>&gt; </span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">mailNotification</span>&gt;</span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">bccAddresses</span>/&gt;</span>
<span id="cb1-17"><a href="#cb1-17" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">ccAddresses</span>/&gt;</span>
<span id="cb1-18"><a href="#cb1-18" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">id</span>&gt;2007&lt;/<span class="kw">id</span>&gt;</span>
<span id="cb1-19"><a href="#cb1-19" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">includingStackTraceWhenJobFails</span>&gt;false&lt;/<span class="kw">includingStackTraceWhenJobFails</span>&gt;</span>
<span id="cb1-20"><a href="#cb1-20" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">messageText</span>&gt;Body of message&lt;/<span class="kw">messageText</span>&gt;<span class="er">&lt;</span></span>
<span id="cb1-21"><a href="#cb1-21" aria-hidden="true" tabindex="-1"></a>    resultSendType&gt;SEND_ATTACHMENT&lt;/<span class="kw">resultSendType</span>&gt;</span>
<span id="cb1-22"><a href="#cb1-22" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">skipEmptyReports</span>&gt;true&lt;/<span class="kw">skipEmptyReports</span>&gt;</span>
<span id="cb1-23"><a href="#cb1-23" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">skipNotificationWhenJobFails</span>&gt;false&lt;/<span class="kw">skipNotificationWhenJobFails</span>&gt;</span>
<span id="cb1-24"><a href="#cb1-24" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">subject</span>&gt;Subject of message&lt;/<span class="kw">subject</span>&gt;</span>
<span id="cb1-25"><a href="#cb1-25" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">toAddresses</span>&gt;&lt;<span class="kw">address</span>&gt;name@example.com&lt;/<span class="kw">address</span>&gt;&lt;/<span class="kw">toAddresses</span>&gt;</span>
<span id="cb1-26"><a href="#cb1-26" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">version</span>&gt;0&lt;/<span class="kw">version</span>&gt;</span>
<span id="cb1-27"><a href="#cb1-27" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">mailNotification</span>&gt;</span>
<span id="cb1-28"><a href="#cb1-28" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">outputFormats</span>&gt;</span>
<span id="cb1-29"><a href="#cb1-29" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">outputFormat</span>&gt;XLS&lt;/<span class="kw">outputFormat</span>&gt;</span>
<span id="cb1-30"><a href="#cb1-30" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">outputFormat</span>&gt;CSV&lt;/<span class="kw">outputFormat</span>&gt;</span>
<span id="cb1-31"><a href="#cb1-31" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">outputFormat</span>&gt;PDF&lt;/<span class="kw">outputFormat</span>&gt;</span>
<span id="cb1-32"><a href="#cb1-32" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">outputFormat</span>&gt;HTML&lt;/<span class="kw">outputFormat</span>&gt;</span>
<span id="cb1-33"><a href="#cb1-33" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">outputFormat</span>&gt;DOCX&lt;/<span class="kw">outputFormat</span>&gt;</span>
<span id="cb1-34"><a href="#cb1-34" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">outputFormats</span>&gt;</span>
<span id="cb1-35"><a href="#cb1-35" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">outputLocale</span>/&gt; </span>
<span id="cb1-36"><a href="#cb1-36" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">reportUnitURI</span>&gt;/reports/samples/AllAccounts&lt;/<span class="kw">reportUnitURI</span>&gt; </span>
<span id="cb1-37"><a href="#cb1-37" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">simpleTrigger</span>&gt; </span>
<span id="cb1-38"><a href="#cb1-38" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">id</span>&gt;2040&lt;/<span class="kw">id</span>&gt; </span>
<span id="cb1-39"><a href="#cb1-39" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">startDate</span>&gt;2222-02-04T03:47:00+02:00&lt;/<span class="kw">startDate</span>&gt; </span>
<span id="cb1-40"><a href="#cb1-40" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">timezone</span>&gt;America/Los_Angeles&lt;/<span class="kw">timezone</span>&gt; </span>
<span id="cb1-41"><a href="#cb1-41" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">version</span>&gt;0&lt;/<span class="kw">version</span>&gt; </span>
<span id="cb1-42"><a href="#cb1-42" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">occurrenceCount</span>&gt;1&lt;/<span class="kw">occurrenceCount</span>&gt; </span>
<span id="cb1-43"><a href="#cb1-43" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">simpleTrigger</span>&gt; </span>
<span id="cb1-44"><a href="#cb1-44" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">version</span>&gt;1&lt;/<span class="kw">version</span>&gt; </span>
<span id="cb1-45"><a href="#cb1-45" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">job</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

As of JasperReports® Server 5.5, the v2/jobs service also supports the extended application/job+json syntax. This format allows you to specify the scheduler features introduced in release 5.5, such as alert messages:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;id&quot;</span><span class="fu">:</span> <span class="dv">3819</span><span class="fu">,</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;version&quot;</span><span class="fu">:</span> <span class="dv">0</span><span class="fu">,</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;username&quot;</span><span class="fu">:</span> <span class="st">&quot;superuser&quot;</span><span class="fu">,</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;label&quot;</span><span class="fu">:</span> <span class="st">&quot;test&quot;</span><span class="fu">,</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;description&quot;</span><span class="fu">:</span> <span class="st">&quot;&quot;</span><span class="fu">,</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;creationDate&quot;</span><span class="fu">:</span> <span class="st">&quot;2013-08-30T02:02:40.382+03:00&quot;</span><span class="fu">,</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;trigger&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;simpleTrigger&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;id&quot;</span><span class="fu">:</span> <span class="dv">3816</span><span class="fu">,</span></span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;version&quot;</span><span class="fu">:</span> <span class="dv">0</span><span class="fu">,</span></span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;timezone&quot;</span><span class="fu">:</span> <span class="st">&quot;America/Los_Angeles&quot;</span><span class="fu">,</span></span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;calendarName&quot;</span><span class="fu">:</span> <span class="kw">null</span><span class="fu">,</span></span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;startType&quot;</span><span class="fu">:</span> <span class="dv">2</span><span class="fu">,</span></span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>            <span class="er">//</span> <span class="er">startDate</span> <span class="er">format</span> <span class="er">is</span> <span class="er">yyyy-MM-dd</span> <span class="er">HH</span><span class="fu">:</span><span class="er">mm</span></span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a>            <span class="er">//</span> <span class="er">time</span> <span class="er">zone</span> <span class="er">specified</span> <span class="er">in</span> <span class="er">a</span> <span class="er">&#39;timezone&#39;</span> <span class="er">filed</span> <span class="er">getting</span> <span class="er">applied</span> <span class="er">on</span> <span class="er">a</span> <span class="er">server</span></span>
<span id="cb1-17"><a href="#cb1-17" aria-hidden="true" tabindex="-1"></a>            <span class="st">&quot;startDate&quot;</span><span class="er">:</span> <span class="st">&quot;2013-09-26 10:00&quot;</span><span class="fu">,</span></span>
<span id="cb1-18"><a href="#cb1-18" aria-hidden="true" tabindex="-1"></a>            <span class="er">//</span> <span class="er">endDate</span> <span class="er">format</span> <span class="er">is</span> <span class="er">yyyy-MM-dd</span> <span class="er">HH</span><span class="fu">:</span><span class="er">mm</span></span>
<span id="cb1-19"><a href="#cb1-19" aria-hidden="true" tabindex="-1"></a>            <span class="er">//</span> <span class="er">time</span> <span class="er">zone</span> <span class="er">specified</span> <span class="er">in</span> <span class="er">a</span> <span class="er">&#39;timezone&#39;</span> <span class="er">filed</span> <span class="er">getting</span> <span class="er">applied</span> <span class="er">on</span> <span class="er">a</span> <span class="er">server</span></span>
<span id="cb1-20"><a href="#cb1-20" aria-hidden="true" tabindex="-1"></a>            <span class="st">&quot;endDate&quot;</span><span class="er">:</span> <span class="kw">null</span><span class="fu">,</span></span>
<span id="cb1-21"><a href="#cb1-21" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;misfireInstruction&quot;</span><span class="fu">:</span> <span class="dv">0</span><span class="fu">,</span></span>
<span id="cb1-22"><a href="#cb1-22" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;occurrenceCount&quot;</span><span class="fu">:</span> <span class="dv">1</span><span class="fu">,</span></span>
<span id="cb1-23"><a href="#cb1-23" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;recurrenceInterval&quot;</span><span class="fu">:</span> <span class="kw">null</span></span>
<span id="cb1-24"><a href="#cb1-24" aria-hidden="true" tabindex="-1"></a>        <span class="fu">}</span></span>
<span id="cb1-25"><a href="#cb1-25" aria-hidden="true" tabindex="-1"></a>    <span class="fu">},</span></span>
<span id="cb1-26"><a href="#cb1-26" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;source&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb1-27"><a href="#cb1-27" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;reportUnitURI&quot;</span><span class="fu">:</span> <span class="st">&quot;/organizations/organization_1/reports/samples/Cascading_multi_select_report&quot;</span><span class="fu">,</span></span>
<span id="cb1-28"><a href="#cb1-28" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;parameters&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb1-29"><a href="#cb1-29" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;parameterValues&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb1-30"><a href="#cb1-30" aria-hidden="true" tabindex="-1"></a>                <span class="dt">&quot;Country_multi_select&quot;</span><span class="fu">:</span> <span class="ot">[</span><span class="st">&quot;Mexico&quot;</span><span class="ot">]</span><span class="fu">,</span></span>
<span id="cb1-31"><a href="#cb1-31" aria-hidden="true" tabindex="-1"></a>                <span class="dt">&quot;Cascading_name_single_select&quot;</span><span class="fu">:</span> <span class="ot">[</span><span class="st">&quot;Chin-Lovell Engineering Associates&quot;</span><span class="ot">]</span><span class="fu">,</span></span>
<span id="cb1-32"><a href="#cb1-32" aria-hidden="true" tabindex="-1"></a>                <span class="dt">&quot;Cascading_state_multi_select&quot;</span><span class="fu">:</span> <span class="ot">[</span><span class="st">&quot;DF&quot;</span><span class="ot">,</span><span class="st">&quot;Jalisco&quot;</span><span class="ot">,</span><span class="st">&quot;Mexico&quot;</span><span class="ot">]</span></span>
<span id="cb1-33"><a href="#cb1-33" aria-hidden="true" tabindex="-1"></a>            <span class="fu">}</span></span>
<span id="cb1-34"><a href="#cb1-34" aria-hidden="true" tabindex="-1"></a>        <span class="fu">}</span></span>
<span id="cb1-35"><a href="#cb1-35" aria-hidden="true" tabindex="-1"></a>    <span class="fu">},</span></span>
<span id="cb1-36"><a href="#cb1-36" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;baseOutputFilename&quot;</span><span class="fu">:</span> <span class="st">&quot;Cascading_multi_select_report&quot;</span><span class="fu">,</span></span>
<span id="cb1-37"><a href="#cb1-37" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;outputLocale&quot;</span><span class="fu">:</span> <span class="st">&quot;&quot;</span><span class="fu">,</span></span>
<span id="cb1-38"><a href="#cb1-38" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;mailNotification&quot;</span><span class="fu">:</span> <span class="kw">null</span><span class="fu">,</span></span>
<span id="cb1-39"><a href="#cb1-39" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;alert&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb1-40"><a href="#cb1-40" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;id&quot;</span><span class="fu">:</span> <span class="dv">0</span><span class="fu">,</span></span>
<span id="cb1-41"><a href="#cb1-41" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;version&quot;</span><span class="fu">:</span> <span class="dv">-1</span><span class="fu">,</span></span>
<span id="cb1-42"><a href="#cb1-42" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;recipient&quot;</span><span class="fu">:</span> <span class="st">&quot;OWNER_AND_ADMIN&quot;</span><span class="fu">,</span></span>
<span id="cb1-43"><a href="#cb1-43" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;toAddresses&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb1-44"><a href="#cb1-44" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;address&quot;</span><span class="fu">:</span> <span class="ot">[]</span></span>
<span id="cb1-45"><a href="#cb1-45" aria-hidden="true" tabindex="-1"></a>        <span class="fu">},</span></span>
<span id="cb1-46"><a href="#cb1-46" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;jobState&quot;</span><span class="fu">:</span> <span class="st">&quot;FAIL_ONLY&quot;</span><span class="fu">,</span></span>
<span id="cb1-47"><a href="#cb1-47" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;messageText&quot;</span><span class="fu">:</span> <span class="kw">null</span><span class="fu">,</span></span>
<span id="cb1-48"><a href="#cb1-48" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;messageTextWhenJobFails&quot;</span><span class="fu">:</span> <span class="kw">null</span><span class="fu">,</span></span>
<span id="cb1-49"><a href="#cb1-49" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;subject&quot;</span><span class="fu">:</span> <span class="kw">null</span><span class="fu">,</span></span>
<span id="cb1-50"><a href="#cb1-50" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;includingStackTrace&quot;</span><span class="fu">:</span> <span class="kw">true</span><span class="fu">,</span></span>
<span id="cb1-51"><a href="#cb1-51" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;includingReportJobInfo&quot;</span><span class="fu">:</span> <span class="kw">true</span></span>
<span id="cb1-52"><a href="#cb1-52" aria-hidden="true" tabindex="-1"></a>    <span class="fu">},</span></span>
<span id="cb1-53"><a href="#cb1-53" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;outputTimeZone&quot;</span><span class="fu">:</span> <span class="st">&quot;America/Los_Angeles&quot;</span><span class="fu">,</span></span>
<span id="cb1-54"><a href="#cb1-54" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;repositoryDestination&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb1-55"><a href="#cb1-55" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;id&quot;</span><span class="fu">:</span> <span class="dv">3817</span><span class="fu">,</span></span>
<span id="cb1-56"><a href="#cb1-56" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;version&quot;</span><span class="fu">:</span> <span class="dv">0</span><span class="fu">,</span></span>
<span id="cb1-57"><a href="#cb1-57" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;folderURI&quot;</span><span class="fu">:</span> <span class="st">&quot;/organizations/organization_1/reports/samples&quot;</span><span class="fu">,</span></span>
<span id="cb1-58"><a href="#cb1-58" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;sequentialFilenames&quot;</span><span class="fu">:</span> <span class="kw">false</span><span class="fu">,</span></span>
<span id="cb1-59"><a href="#cb1-59" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;overwriteFiles&quot;</span><span class="fu">:</span> <span class="kw">false</span><span class="fu">,</span></span>
<span id="cb1-60"><a href="#cb1-60" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;outputDescription&quot;</span><span class="fu">:</span> <span class="st">&quot;&quot;</span><span class="fu">,</span></span>
<span id="cb1-61"><a href="#cb1-61" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;timestampPattern&quot;</span><span class="fu">:</span> <span class="kw">null</span><span class="fu">,</span></span>
<span id="cb1-62"><a href="#cb1-62" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;saveToRepository&quot;</span><span class="fu">:</span> <span class="kw">true</span><span class="fu">,</span></span>
<span id="cb1-63"><a href="#cb1-63" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;defaultReportOutputFolderURI&quot;</span><span class="fu">:</span> <span class="kw">null</span><span class="fu">,</span></span>
<span id="cb1-64"><a href="#cb1-64" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;usingDefaultReportOutputFolderURI&quot;</span><span class="fu">:</span> <span class="kw">false</span><span class="fu">,</span></span>
<span id="cb1-65"><a href="#cb1-65" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;outputLocalFolder&quot;</span><span class="fu">:</span> <span class="kw">null</span><span class="fu">,</span></span>
<span id="cb1-66"><a href="#cb1-66" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;outputFTPInfo&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb1-67"><a href="#cb1-67" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;userName&quot;</span><span class="fu">:</span> <span class="kw">null</span><span class="fu">,</span></span>
<span id="cb1-68"><a href="#cb1-68" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;password&quot;</span><span class="fu">:</span> <span class="kw">null</span><span class="fu">,</span></span>
<span id="cb1-69"><a href="#cb1-69" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;folderPath&quot;</span><span class="fu">:</span> <span class="kw">null</span><span class="fu">,</span></span>
<span id="cb1-70"><a href="#cb1-70" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;serverName&quot;</span><span class="fu">:</span> <span class="kw">null</span></span>
<span id="cb1-71"><a href="#cb1-71" aria-hidden="true" tabindex="-1"></a>        <span class="fu">}</span></span>
<span id="cb1-72"><a href="#cb1-72" aria-hidden="true" tabindex="-1"></a>    <span class="fu">},</span></span>
<span id="cb1-73"><a href="#cb1-73" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;outputFormats&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb1-74"><a href="#cb1-74" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;outputFormat&quot;</span><span class="fu">:</span> <span class="ot">[</span><span class="st">&quot;PDF&quot;</span><span class="ot">]</span></span>
<span id="cb1-75"><a href="#cb1-75" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span></span>
<span id="cb1-76"><a href="#cb1-76" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
</tbody>
</table>
