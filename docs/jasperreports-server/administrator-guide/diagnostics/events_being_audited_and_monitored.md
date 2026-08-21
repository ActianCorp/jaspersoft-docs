---
title: Auditing and Monitoring Events
description: "Whereas logs capture messages from the internal code of JasperReports Server, the auditing and monitoring systems capture user events. This gives an operational picture of how users interact with the..."
---

# Auditing and Monitoring Events

Whereas logs capture messages from the internal code of JasperReports Server, the auditing and monitoring systems capture user events. This gives an operational picture of how users interact with the server and what resources they use. Auditing and monitoring can help you see who is using the server, and what resources are the most in demand. This can help you locate bottlenecks and optimize your reports.

In broad terms, an audit event is any atomic operation that can be recorded by the audit system. Event properties and attributes are features of the event; they can be defined internally or in custom code. Auditing and monitoring rely on the same record of events, so the audit events are also available in monitoring data sources, Domains, and reports.

The following table lists the defined audit events and the information collected about them. For every recorded event, JasperReports Server logs the time it occurred and the user who initiated it. See the configuration file `applicationContext-audit.xml` for complete specification of the events.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>Event</p></th>
<th><p>Information Collected</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Log in or log out</p></td>
<td><p>Time and user ID (recorded for every event)</p></td>
</tr>
<tr>
<td><p>Log in as</p></td>
<td><p>User logged in as</p></td>
</tr>
<tr>
<td><p>Run report or run a subreport within any other report</p></td>
<td><ul>
<li>Report referenced</li>
<li>Data source referenced</li>
<li>Report parameters and values</li>
<li>Report queries (such as SQL, Domain, HQL, generated SQL)</li>
<li>Execution start, end</li>
<li>Query execution time (in milliseconds)</li>
<li>Report rendering time (in milliseconds)</li>
<li>Caching parameters</li>
<li>Errors that occurred</li>
</ul></td>
</tr>
<tr>
<td><p>Report schedule created, deleted, or updated</p></td>
<td><ul>
<li>Report referenced</li>
<li>Scheduling parameters and values</li>
</ul></td>
</tr>
<tr>
<td><p>Scheduled report run</p></td>
<td><ul>
<li>Report output</li>
<li>Report delivery parameters (such as email)</li>
<li>Same parameters as when report is run</li>
</ul></td>
</tr>
<tr>
<td><p>Creating report in Ad Hoc Editor</p></td>
<td><ul>
<li>Field added as a column</li>
<li>Field added as a group</li>
</ul></td>
</tr>
<tr>
<td><p>Resource accessed for any reason (such as view, used in report, etc.)</p></td>
<td><ul>
<li>Resource referenced</li>
<li>Resource type</li>
</ul></td>
</tr>
<tr>
<td><p>Resource added or updated</p></td>
<td><ul>
<li>Resource referenced</li>
<li>Resource type</li>
</ul></td>
</tr>
<tr>
<td><p>Resource or folder deleted</p></td>
<td><p>Resource or folder referenced</p></td>
</tr>
<tr>
<td>Resource or folder moved</td>
<td><p>Resource or folder referenced</p>
<p>**Note** When a resource or folder is moved, the logged URI is no longer valid. Also, when resources are moved, access events are updated in the queue, and the Home Page list of frequently accessed resources will be updated with new URIs after some delay.</p></td>
</tr>
<tr>
<td><p>Permissions added, updated, or deleted</p></td>
<td><ul>
<li>Resource or folder referenced</li>
<li>Previous permissions (before update)</li>
</ul></td>
</tr>
<tr>
<td><p>User added, updated, or deleted, also user password change</p></td>
<td><ul>
<li>User ID</li>
<li>User name</li>
<li>Email</li>
<li>Enabled flag</li>
<li>External flag</li>
<li>User attributes</li>
</ul></td>
</tr>
<tr>
<td><p>Role added, updated, or deleted</p></td>
<td><ul>
<li>Role ID</li>
<li>Role name</li>
<li>Role organization</li>
</ul></td>
</tr>
<tr>
<td><p>Organization added, updated, or deleted</p></td>
<td><ul>
<li>Organization ID</li>
<li>Organization description</li>
</ul></td>
</tr>
</tbody>
</table>
