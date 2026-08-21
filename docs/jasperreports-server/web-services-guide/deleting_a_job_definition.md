---
title: Deleting a Job Definition
description: Use the DELETE method to delete a job identified by its jobID. Use the jobsummary service to see the job IDs for a given report.
---

# 1.0.1 Deleting a Job Definition

Use the DELETE method to delete a job identified by its jobID. Use the jobsummary service to see the job IDs for a given report.

<table>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>DELETE</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest/job</span>/&lt;jobID&gt;/</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK</p></td>
<td><p>404 Not Found – When the specified job is not found in the server.</p></td>
</tr>
</tbody>
</table>
