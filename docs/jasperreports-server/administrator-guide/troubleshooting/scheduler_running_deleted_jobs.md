---
title: Scheduler Running Deleted Jobs
description: "In some cases, old versions of JasperReports Server did not delete the scheduled jobs when deleting a report. These jobs cause errors when the scheduler tries to run them, but you can't remove the..."
---

# Scheduler Running Deleted Jobs

In some cases, old versions of JasperReports Server did not delete the scheduled jobs when deleting a report. These jobs cause errors when the scheduler tries to run them, but you can't remove the jobs through the user interface. The server no longer creates such `orphan` jobs, but they may appear again when you upgrade or import a catalog that contains them.

If you accidentally imported orphan jobs, make the configuration change shown below and restart your server.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>Automatically Deleting Orphan Jobs</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>.../WEB-INF/applicationContext-report-scheduling.xml</code></p></td>
</tr>
<tr>
<td><p>Entry</p></td>
<td><p>Bean</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>autoDeleteBroken</code><br />
<code>UriReportJob</code><br />
</p></td>
<td><p><code>quartz</code><br />
<code>Scheduler</code><br />
</p></td>
<td><p>Change this property from <code>false</code> (the default) to <code>true</code>. Orphan jobs are detected and deleted just before they run, so all orphan jobs will be deleted gradually over time.</p></td>
</tr>
</tbody>
</table>
