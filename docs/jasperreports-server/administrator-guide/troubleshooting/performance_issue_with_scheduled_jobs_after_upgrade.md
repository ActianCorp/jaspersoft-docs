---
title: Performance Issue with Scheduled Jobs After Upgrade
description: "When upgrading from JasperReports Server 7.5 to 8.0, the scheduled jobs take longer to run. The report query is run less than a minute but it takes hours for the report engine to render the output..."
---

# Performance Issue with Scheduled Jobs After Upgrade

When upgrading from JasperReports Server 7.5 to 8.0, the scheduled jobs take longer to run. The report query is run less than a minute but it takes hours for the report engine to render the output file. This is because starting JasperReports Server 7.8, the instance name for the scheduler has changed from `quartzScheduler` to `JasperServerScheduler`. As a result, after upgrading to JasperReports Server 8.0, you may observe that scheduled jobs for the same report are duplicated in the system. This duplication occurs because each job is associated with both the old and new scheduler names within the Quartz tables.

To handle this, a new property `remove.duplicate.quartz.instance` is added in the `js.quartz.properties` file. This property can be set to either `true` or `false` depending on the requirement. By default, this property is set to `remove.duplicate.quartz.instance=false`.

<table>
<tbody>
<tr>
<td><p>Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><code>false</code></td>
<td colspan="2"><p>Scheduler shall start normally without checking for multiple instances resulting in duplicate jobs.</p></td>
</tr>
<tr>
<td><code>true</code></td>
<td colspan="2">System checks for duplicate scheduler instances. When multiple instances are found, existing jobs are moved to the instance specified in the <code>js.quartz.base.properties</code> file.</td>
</tr>
</tbody>
</table>
