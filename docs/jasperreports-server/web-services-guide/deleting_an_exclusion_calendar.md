---
title: 1.0.0.1 Deleting an Exclusion Calendar
description: Use the following method to delete a calendar by name.
---

# 1.0.0.1 Deleting an Exclusion Calendar

Use the following method to delete a calendar by name.

<table>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>DELETE</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/jobs/calendars</span>/&lt;calendarName&gt;/</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK</p></td>
<td><p>404 Not Found – When the specified calendar name does not exist.</p></td>
</tr>
</tbody>
</table>
