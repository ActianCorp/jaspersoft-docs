---
title: Configuring Auditing and Monitoring
description: "The auditing and monitoring features both rely on the same subsystem in JasperReports Server. The settings are located in the .../WEB-INF/applicationContext-audit.xml file, but their values are set..."
---

# Configuring Auditing and Monitoring

The auditing and monitoring features both rely on the same subsystem in JasperReports Server. The settings are located in the `.../WEB-INF/applicationContext-audit.xml` file, but their values are set in the `.../WEB-INF/js.config.properties` file. The beans and properties of these files are used to enable auditing and monitoring, set the archive options, and select the events to be logged.

!!! note

    You must enable CLOB fields on your JasperReports Server before enabling audits if you want to use audit Domains for your data. See [Enabling CLOB Fields](../configuration/configuring_domains.md) for instructions on enabling CLOB fields.

## Enabling Auditing and Monitoring

Because auditing and monitoring share the same subsystem, there is a master configuration setting to turn on the subsystem, and individual settings for auditing and monitoring. This allows you to turn on each feature independently, or turn off the whole subsystem to avoid any overhead from an unused feature.

By default, the auditing and monitoring subsystem is off.

<table>
<thead>
<tr>
<th colspan="2"><p>Enabling Auditing and Monitoring Options</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="2"><p><code>.../WEB-INF/js.config.properties</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>feature.audit_monitoring.enabled</code></p></td>
<td><p>Set this property to <code>true</code> to enable the auditing and monitoring subsystem. You must also turn on audit and/or monitoring records independently with the following two properties. If you do not need auditing or monitoring, set this property to false to avoid any performance overhead.</p></td>
</tr>
<tr>
<td><p><code>audit.records.enabled</code></p></td>
<td><p>Once <code>feature.audit_monitoring.enabled=true</code>, set this property to <code>true</code> to enable auditing. This setting controls the logging of events in the tables used by the audit reports.</p></td>
</tr>
<tr>
<td><p><code>monitoring.records.enabled</code></p></td>
<td><p>Once <code>feature.audit_monitoring.enabled=true</code>, set this property to <code>true</code> to enable monitoring. This setting controls the logging of events in the tables used by the monitoring Domain.</p></td>
</tr>
</tbody>
</table>

## Auditing Archive Options

Archiving automatically moves audit data to separate database tables, called the audit archive, after a certain time. For example if you create reports for weekly server usage based on the audit Domain, you'll never see audit data older than a month by default. Because audit data can be quite large, the old data can increase the time needed to write new data and query data for your report. If you want to create reports on audit archive tables, there is a separate Domain to access the archived audit data. You can also configure the audit feature to delete old archive data if you no longer need it.

You should set the archiving interval to a level that balances your need to record and access audit data with your server's performance on large audit tables. Use the following configuration settings to change the archiving behavior.

Archiving and deleting (or purging) of audit data happens once per day, by default in the early morning hours. You can also set the time and frequency of these operations.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>Auditing Archive Options</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>.../WEB-INF/applicationContext-audit.xml</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Bean</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>maxAudit</code><br />
<code>EventAge</code><br />
<code>ToArchive</code></p></td>
<td><p><code>auditService</code></p></td>
<td><p>The number of days to keep audit data in the active audit tables. The default is 30. Older data is moved to the archive.</p></td>
</tr>
<tr>
<td><p><code>maxAudit</code><br />
<code>EventAge</code></p></td>
<td><p><code>auditService</code></p></td>
<td><p>The total number of days to keep any audit data. Older data is deleted from either the active or the archive tables. If this value is non-zero but less than the <code>maxAuditEventAgeToArchive</code>, the audit data will be deleted before it is ever archived (this may be useful if you don't want to use the archive). The default is 0 (zero), meaning that old data is never deleted.</p></td>
</tr>
<tr>
<td><p><code>cronExpression</code></p></td>
<td><p><code>auditEvent</code><br />
<code>ArchiverTrigger</code></p></td>
<td><p>Defines the frequency of the archiving job as a <code>cron</code> expression. The default <code>0 0 5* * ?</code> is every day at 5 A.M.</p></td>
</tr>
<tr>
<td><p><code>cronExpression</code></p></td>
<td><p><code>auditEvent</code><br />
<code>PurgerTrigger</code></p></td>
<td><p>Defines the frequency of the audit delete (purge) job as a <code>cron</code> expression. The default <code>0 0 3 * * ?</code> is every day at 3 A.M.</p></td>
</tr>
</tbody>
</table>

The `cronExpression` properties use a [Quartz scheduler cron expression](http://www.quartz-scheduler.org/documentation/quartz-1.x/tutorials/crontrigger) that specifies the repeating trigger as seconds, minutes, hour, day of month, month, day of week, respectively.

## Disabling Events and Properties

By default, all events and properties are logged. To enable or disable logging of a given event or property, use the `applicationContext-audit.xml` configuration file. Events that are logged are used by both the audit and monitoring subsystems, therefore disabling an event makes it unavailable for both auditing and monitoring.

In the file, event types and their properties are listed under `<util:map id="enabledEventsMapping">`. The map has three parts:

-   `WEB_SERVICES`: Event types related to accessing JasperReports Server through a web service.

-   `GUI`: Event types for access through the user interface.

-   `INTERNAL`: Event types used by the server itself, such as when running a scheduled report.

To disable an event, comment it out. For example:

`<!-- <entry key="createFolder" value="folderName,folderLabel,folderDescription" /> -->`

To disable a property, use any of these measures:

-   Delete the property. For example, remove `folderDescription`, resulting in:<br>
    `<entry key="createFolder" value="folderName,folderLabel,exception" />`
-   Disable it with the `|` syntax. For example:<br>
    `<entry key="createFolder" value="folderName,folderLabel,|folderDescription,exception" />`
-   Use the "all except" `*|` syntax to specify only the disabled property. All others are recorded. For example:<br>
    `<entry key="createFolder" value="*|folderDescription" />`
