---
title: The v2/export Service
description: "The export service works asynchronously: first you request the export with the desired options, then you monitor the state of the export, and finally you request the output file. Each step requires a..."
---

# 1.1 The v2/export Service

The export service works asynchronously: first you request the export with the desired options, then you monitor the state of the export, and finally you request the output file. Each step requires a different service call. You must be authenticated as the system admin (superuser) for the export services.

<table>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>POST</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/export</span>/</p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p>application/json</p></td>
<td colspan="2"><p>A JSON object that describes the export options.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – Returns a JSON object that gives the ID of the started export operation.</p></td>
<td><p>401 Unauthorized – Export is available only to the system admin user (superuser).</p></td>
</tr>
</tbody>
</table>

The content to send describes the export options, for example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><pre class="text"><code>{
  roles: [&quot;ROLE_USER&quot;,&quot;ROLE_MANAGER|organization_1&quot;],
  users: [&quot;superuser&quot;,&quot;joeuser|organization_1&quot;],
  uris: [&quot;/public/Samples/Reports/AllAccounts&quot;,
         &quot;/organizations/organization_1/reports/Survey/Survey_Data&quot;]
  parameters: [&quot;role-users&quot;, &quot;repository-permissions&quot;]
}</code></pre></td>
</tr>
</tbody>
</table>

As shown above, commercial editions must use the organization syntax for all roles, users, and URIs.

The following table describes the options you can list in the request.

<table>
<thead>
<tr>
<th colspan="2">Export Options</th>
</tr>
</thead>
<tbody>
<tr>
<td>roles</td>
<td>A list of role names to export. Specify the role-users parameter to also export all users who have these roles.</td>
</tr>
<tr>
<td>users</td>
<td>A list of user names to export.</td>
</tr>
<tr>
<td>uris</td>
<td>A list of resoures or folders to export, specified as repository URIs. When a folder is specified, all its contents and all its subfolders recursively are included. To export all resources in the repository or in an organization, specify "/" (root) in this list. When you specify an organization ID below, the URIs in this list are all relative to the organization.</td>
</tr>
<tr>
<td>scheduledJobs</td>
<td>A list of report URIs for which all scheduled jobs are exported. If you specify a folder URIs, the scheduled jobs for all reports in the folder, recursively, are exported.</td>
</tr>
<tr>
<td>resourceTypes</td>
<td>A list of resource types that filters any selected resources for export. When omitted, all resources specified by URI or folder URI are exported. When specified, only the resource types in this list are exported.</td>
</tr>
<tr>
<td>organization</td>
<td>A single organization ID that determines a branch of the repository for export. When this option is specified, this organization becomes the root for all roles, users, and uris to be listed for export.</td>
</tr>
<tr>
<td>parameters</td>
<td>A list of parameters that act as flags: if specified, the corresponding action is taken, if omitted they have no effect. The the following table.</td>
</tr>
</tbody>
</table>

The following table describes the export parameters:

| Export Parameters |  |
|----|----|
| everything | Export everything except audit and monitoring: all repository resources, permissions, report jobs, users, roles, and server settings. |
| role-users | When specified, each role export triggers the export of all users belonging to the role. This option should only be used if roles are specified |
| repository-permissions | When specified, repository permissions are exported along with each exported folder and resource. This option should only be used if uris are specified. |
| skip-dependent-resources | When specified, only the resources specified by URIs are exported, no dependent resources such as data sources, queries, or files included by reference are exported. This will create broken dependencies during import unless the the same dependencies already exist in the same relative locations in the destination. |
| skip-suborganizations | When specified, the export will omit all the items such as roles, users, and resources that belong to suborganizations, even they are directly specified using the corresponding options. When no organization ID is specified, this flag applies to the root such that no top-level organizations are included in the export, only the contents of the root. |
| include-attributes | Includes all attributes that are associated with a item being exported, such as a user, an organization, or the root. |
| skip-attribute-values | When specified with include-attributes, only attribute names are exported with null values. Use this to prevent applying attributes that are specific to one server or one organization. |
| include-server-settings | When specified, the configuration and security settings on the server are exported. When imported into another server, these settings will take effect immediately. |
| include-access-events | When specified, access events (date, time, and user name of last modification) are exported along with each exported folder and resource. This option should only be used if uris are specified. |
| include-audit-events | Include audit data for all resources and users in the export. The audit feature must be enabled in the server configuration. |
| include-monitoring-events | Include monitoring events. The monitoring feature must be enabled in the server configuration. |

The body of the response contains the ID of the export operation needed to check its status and later download the file:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><pre class="text"><code>{
  id: &quot;njkhfs8374&quot;,
  phase: &quot;inprogress&quot;,
  message: &quot;Progress...&quot;
}</code></pre></td>
</tr>
</tbody>
</table>

The response may also warn you of any broken dependencies in the export that may affect a future import operation:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><pre class="text"><code>{
  id: &quot;njkhfs8374&quot;,
  phase: &quot;inprogress&quot;,
  message: &quot;Progress...&quot;
  &quot;warnings&quot;: [
    {
      &quot;code&quot;: &quot;export.broken.dependency&quot;,
      &quot;message&quot;:&quot;Resource with broken dependencies&quot;,
      &quot;parameters&quot;: [
        &quot;path_to_broken_resource&quot;]
    }, ...
  ]
}</code></pre></td>
</tr>
</tbody>
</table>
