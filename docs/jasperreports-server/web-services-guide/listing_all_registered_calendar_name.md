---
title: 1.0.0.1 Listing All Registered Calendar Names
description: The following method returns the list of all calendar names that were added to the scheduler.
---

# 1.0.0.1 Listing All Registered Calendar Names

The following method returns the list of all calendar names that were added to the scheduler.

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/jobs/calendars/</span>?&lt;parameter&gt;</p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p>calendar<br />
Type</p></td>
<td><p>optional string</p></td>
<td colspan="2"><p>A type of calendar to return: annual, base, cron, daily, holiday, monthly, or weekly. See <a href="adding_or_updating_an_exclusion_cale.md">Adding or Updating an Exclusion Calendar</a> for a description of the various types. You may specify only one calendarType parameter. When calendarType isn't specified, then all calendars names are returned. If calendarType has an invalid value, then an empty collection is returned.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – Body is XML that contains a list of calendar names.</p></td>
<td><p>401 Unauthorized</p></td>
</tr>
</tbody>
</table>

The list of calendar names in the result has the following XML format:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">calendarNameList</span>&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">calendarName</span>&gt;name1&lt;/<span class="kw">calendarName</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">calendarName</span>&gt;name2&lt;/<span class="kw">calendarName</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">calendarNameList</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>
