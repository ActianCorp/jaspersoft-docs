---
title: Viewing a Job Definition
description: The GET method for the job service retrieves the information about a scheduled job.
---

# 1.0.1 Viewing a Job Definition

The GET method for the job service retrieves the information about a scheduled job.

<table>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>GET</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest/job</span>/&lt;jobID&gt;/</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The body contains XML that describes all the job properties</p></td>
<td><p>404 Not Found – When the specified job is not found in the server.</p></td>
</tr>
</tbody>
</table>

The GET method returns a `job` element that gives the output, scheduling, and parameter details, if any, for the job:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">job</span>&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">baseOutputFilename</span>&gt;AllAccounts&lt;/<span class="kw">baseOutputFilename</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">description</span>&gt;Sample job&lt;/<span class="kw">description</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">id</span>&gt;22164&lt;/<span class="kw">id</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">label</span>&gt;MyJob&lt;/<span class="kw">label</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">mailNotification</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">id</span>&gt;22163&lt;/<span class="kw">id</span>&gt;</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">messageText</span>&gt;&lt;/<span class="kw">messageText</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resultSendType</span>&gt;&lt;<span class="kw">value</span>&gt;SEND&lt;/<span class="kw">value</span>&gt;&lt;/<span class="kw">resultSendType</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">skipEmptyReports</span>&gt;false&lt;/<span class="kw">skipEmptyReports</span>&gt;</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">subject</span>&gt;Scheduled AllAccounts report&lt;/<span class="kw">subject</span>&gt;</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">toAddresses</span>&gt;example@example.com&lt;/<span class="kw">toAddresses</span>&gt;</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">version</span>&gt;2&lt;/<span class="kw">version</span>&gt;</span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">mailNotification</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td><div class="sourceCode" id="cb3"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">outputFormats</span>&gt;PDF&lt;/<span class="kw">outputFormats</span>&gt;</span>
<span id="cb3-2"><a href="#cb3-2" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">outputFormats</span>&gt;HTML&lt;/<span class="kw">outputFormats</span>&gt;</span>
<span id="cb3-3"><a href="#cb3-3" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">outputLocale</span>&gt;&lt;/<span class="kw">outputLocale</span>&gt;</span>
<span id="cb3-4"><a href="#cb3-4" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">reportUnitURI</span>&gt;/reports/samples/AllAccounts&lt;/<span class="kw">reportUnitURI</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td><div class="sourceCode" id="cb4"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb4-1"><a href="#cb4-1" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">repositoryDestination</span>&gt;</span>
<span id="cb4-2"><a href="#cb4-2" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">folderURI</span>&gt;/reports/samples&lt;/<span class="kw">folderURI</span>&gt;</span>
<span id="cb4-3"><a href="#cb4-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">id</span>&gt;22162&lt;/<span class="kw">id</span>&gt;</span>
<span id="cb4-4"><a href="#cb4-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">outputDescription</span>&gt;&lt;/<span class="kw">outputDescription</span>&gt;</span>
<span id="cb4-5"><a href="#cb4-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">overwriteFiles</span>&gt;false&lt;/<span class="kw">overwriteFiles</span>&gt;</span>
<span id="cb4-6"><a href="#cb4-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">sequentialFilenames</span>&gt;false&lt;/<span class="kw">sequentialFilenames</span>&gt;</span>
<span id="cb4-7"><a href="#cb4-7" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">version</span>&gt;0&lt;/<span class="kw">version</span>&gt;</span>
<span id="cb4-8"><a href="#cb4-8" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">repositoryDestination</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td><div class="sourceCode" id="cb5"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb5-1"><a href="#cb5-1" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">simpleTrigger</span>&gt;</span>
<span id="cb5-2"><a href="#cb5-2" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">id</span>&gt;22161&lt;/<span class="kw">id</span>&gt;</span>
<span id="cb5-3"><a href="#cb5-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">startDate</span>&gt;2011-11-11T11:11:11-08:00&lt;/<span class="kw">startDate</span>&gt;</span>
<span id="cb5-4"><a href="#cb5-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">timezone</span>&gt;America/Los_Angeles&lt;/<span class="kw">timezone</span>&gt;</span>
<span id="cb5-5"><a href="#cb5-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">version</span>&gt;0&lt;/<span class="kw">version</span>&gt;</span>
<span id="cb5-6"><a href="#cb5-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">occurrenceCount</span>&gt;1&lt;/<span class="kw">occurrenceCount</span>&gt;</span>
<span id="cb5-7"><a href="#cb5-7" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">simpleTrigger</span>&gt;</span>
<span id="cb5-8"><a href="#cb5-8" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">version</span>&gt;0&lt;/<span class="kw">version</span>&gt;</span>
<span id="cb5-9"><a href="#cb5-9" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">job</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>
