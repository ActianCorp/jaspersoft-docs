---
title: Finding Running Reports
description: "The new v2/reports service provides functionality to stop reports that are running. Reports can be running from user interaction, web service calls, or scheduling. The following method provides..."
---

# Finding Running Reports

The new v2/reports service provides functionality to stop reports that are running. Reports can be running from user interaction, web service calls, or scheduling. The following method provides several ways to find reports that are currently running, in case the client wants to stop them.

!!! note

    This syntax of the v2/reports service is deprecated. See [The v2/reportExecutions Service](the_v2_reportexecutions_service.md).

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/reports</span>/path/to/report/</p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/reports</span>?&lt;arguments&gt;</p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><code>jobID?</code></p></td>
<td><p>String</p></td>
<td colspan="2"><p>Find the running report based on its jobID in the scheduler.</p></td>
</tr>
<tr>
<td><p><code>jobLabel?</code></p></td>
<td><p>String</p></td>
<td colspan="2"><p>Find the running report based on its jobLabel in the scheduler.</p></td>
</tr>
<tr>
<td><p><code>userName?</code></p></td>
<td><p>String</p></td>
<td colspan="2"><p>Name of user who has scheduled a report, in the format &lt;username&gt;%7C&lt;organizationID&gt;. The |&lt;organizationID&gt; is required for all users except system admins (superuser).</p></td>
</tr>
<tr>
<td><p>fireTime<br />
From?</p></td>
<td><p>date/time</p></td>
<td colspan="2" rowspan="2"><p>Date and time in the following pattern: yyyy-MM-dd'T'HH:mmZ. Together, these arguments create a time range to find when the running report was started. Both of the range limits are inclusive. Either argument may be null to signify an open-ended range.</p></td>
</tr>
<tr>
<td><p>fireTimeTo?</p></td>
<td><p>date/time</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The content is a list of execution IDs that can be used for cancellation.</p></td>
<td><p>404 Not Found – When the specified report URI is not found in the repository.</p></td>
</tr>
</tbody>
</table>

For security purposes, the search for running reports is has the following restrictions:

- The system administrator (`superuser`) can see and cancel any report running on the server.
- An organization admin (`jasperadmin`) can see every running report, but can cancel only the reports that were started by a user of the same organization or one of its child organizations.
- A regular user can see every running report, but can cancel only the reports that he initiated.
