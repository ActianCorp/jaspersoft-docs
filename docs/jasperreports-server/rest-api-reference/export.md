---
title: The export Service
description: "The restv2/export service works asynchronously: first you request the export with the desired options, then you monitor the state of the export, and finally you request the output file. Each step..."
---

# The export Service

The rest_v2/export service works asynchronously: first you request the export with the desired options, then you monitor the state of the export, and finally you request the output file. Each step requires a different service call.

You must be authenticated as the system admin (`superuser`) for the export services.

This chapter includes the following sections:

- Requesting an Export
- Polling the Export Status
- Fetching the Export Output
- Canceling an Export Operation

## Requesting an Export

Use the following method to specify the export options for your export request:

<table>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>POST</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/export</span>/</span></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/json</span></p></td>
<td colspan="2"><p>A JSON object that describes the export options.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – Returns a JSON object that gives the ID of the running export operation.</p></td>
<td><p>401 Unauthorized – Export is available only to the system admin user (superuser).</p></td>
</tr>
</tbody>
</table>

The content to send describes the export options, for example:

``` json
{
  "roles": ["ROLE_USER","ROLE_MANAGER|organization_1"],
  "users": ["superuser","joeuser|organization_1"],
  "uris":  ["/public/Samples/Reports/AllAccounts",
            "/organizations/organization_1/reports/Survey/Survey_Data"],
  "parameters": ["role-users", "repository-permissions"]
}
```

As shown above, commercial editions must use the organization syntax for all roles, users, and URIs.

The following table describes the options you can list in the request.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>Export Options</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><span>roles</span></p></td>
<td><p>A list of role names to export. Specify the role-users parameter to also export all users who have these roles.</p></td>
</tr>
<tr>
<td><p><span>users</span></p></td>
<td><p>A list of user names to export.</p></td>
</tr>
<tr>
<td><p><span>uris</span></p></td>
<td><p>A list of resources or folders to export, specified as repository URIs. When a folder is specified, all its contents and all its subfolders recursively are included. To export all resources in the repository or in an organization, specify "/" (root) in this list. When you specify an organization ID below, the URIs in this list are all relative to the organization.</p></td>
</tr>
<tr>
<td><p><span>scheduledJobs</span></p></td>
<td><p>A list of report URIs for which all scheduled jobs are exported. If you specify a folder URIs, the scheduled jobs for all reports in the folder, recursively, are exported.</p></td>
</tr>
<tr>
<td><p><span>resourceTypes</span></p></td>
<td><p>A list of resource types that filters any selected resources for export. When omitted, all resources specified by URI or folder URI are exported. When specified, only the resource types in this list are exported.</p></td>
</tr>
<tr>
<td><p><span>organization</span></p></td>
<td><p>A single organization ID that determines a branch of the repository for export. When this option is specified, this organization becomes the root for all roles, users, and URIS to be listed for export.</p></td>
</tr>
<tr>
<td><p><span>parameters</span></p></td>
<td><p>A list of parameters that act as flags: if specified, the corresponding action is taken, if omitted they have no effect. The export parameters are listed in the following table.</p></td>
</tr>
<tr>
<td><p><span>keyAlias</span></p></td>
<td><p>Specify the alias of the key (for example "productionServerKey") to use when encrypting passwords in the export catalog. The alias must correspond to a custom key in the importing server's keystore. When not specified, the server uses its own import-export key, and unless this key is shared with another server, the catalog may only be imported back into the same server.</p>
<p>For a list of available keys, see <a href="keys.md">“The keys Service” on page 1</a>. This key must also be available on the server that imports the catalog. For more information about import and export keys, see the <span>JasperReports Server Security Guide</span>.</p></td>
</tr>
<tr>
<td><span>scheduledAlerts</span></td>
<td>A list of report URIs for which all scheduled alerts are exported. If you specify a folder URIs, the scheduled alerts for all reports in the folder, recursively, are exported.</td>
</tr>
</tbody>
</table>

The following table describes the export parameters that can be specified in the parameters option:

| Export Parameters | Description |
|----|----|
| everything | Export everything except audit and monitoring: all repository resources, permissions, report jobs, users, roles, and server settings. |
| role-users | When this option is present, each role export triggers the export of all users belonging to that role. This option should only be used if roles are specified. |
| repository-permissions | When this option is present, repository permissions are exported along with each exported folder and resource. This option should only be used if URIs are specified. |
| skip-dependent-resources | When specified, only the resources specified by URIs or resource types are exported, no dependent resources such as data sources, queries, or files included by reference are exported. For example, you can use this parameter to export a single report. The export catalog created with this parameter will cause broken dependencies during import unless the same dependencies already exist in the same relative locations in the destination. |
| skip-suborganizations | When specified, the export will omit all the items such as roles, users, and resources that belong to suborganizations, even if they are directly specified using the corresponding options. When no organization ID is specified, this flag applies to the root such that no top-level organizations are included in the export, only the contents of the root. |
| skip-favorite-resources | When specified, the resources added to Favorites are not exported. |
| include-attributes | Includes all attributes that are associated with a item being exported, such as a user, an organization, or the root. |
| skip-attribute-values | When specified with include-attributes, only attribute names are exported with null values. Use this to prevent applying attributes that are specific to one server or one organization. |
| include-server-settings | When specified, the configuration and security settings on the server are exported. When imported into another server, these settings will take effect immediately. |
| include-access-events | When this option is present, access events (date, time, and user name of last modification) are exported along with each exported folder and resource. This option should only be used if URIs are specified. |
| include-audit-events | Include audit data for all resources and users in the export. The audit feature must be enabled in the server configuration. |
| include-monitoring-events | Include monitoring events. The monitoring feature must be enabled in the server configuration. |

The body of the response contains the ID of the export operation needed to check its status and later download the file:

``` json
{
  "id": "njkhfs8374",
  "phase": "inprogress",
  "message": "Export in progress."
}
```

The response may also warn you of any broken dependencies in the export that may affect a future import operation:

``` json
{
  "id": "njkhfs8374",
  "phase": "inprogress",
  "message": "Export in progress."
  "warnings": [
    {
      "code": "export.broken.dependency",
      "message":"Resource with broken dependencies",
      "parameters": [
        "path_to_broken_resource"]
    }, ...
  ]
}
```

## Polling the Export Status

After receiving the export ID in the response to the export request, you can check the state of the export operation. The server takes up to several seconds to generate the export catalog, depending on the size of the requested resources and the load on the server.

<table>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>GET</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/export</span>/&lt;export-id&gt;/<span>state</span></span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – Returns a JSON object that gives the current state of the export operation.</p></td>
<td><p>404 Not Found – When the specified export ID is not found.</p></td>
</tr>
</tbody>
</table>

The body of the response contains the current state of the export operation:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;phase&quot;</span><span class="fu">:</span> <span class="st">&quot;inprogress&quot;</span><span class="fu">,</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;message&quot;</span><span class="fu">:</span><span class="st">&quot;Export in progress.&quot;</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;phase&quot;</span><span class="fu">:</span> <span class="st">&quot;finished&quot;</span><span class="fu">,</span></span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;message&quot;</span><span class="fu">:</span> <span class="st">&quot;Export succeeded.&quot;</span></span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
<td><div class="sourceCode" id="cb3"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb3-2"><a href="#cb3-2" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;phase&quot;</span><span class="fu">:</span> <span class="st">&quot;failed&quot;</span><span class="fu">,</span></span>
<span id="cb3-3"><a href="#cb3-3" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;message&quot;</span><span class="fu">:</span> <span class="st">&quot;Export failed.&quot;</span></span>
<span id="cb3-4"><a href="#cb3-4" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
</tbody>
</table>

## Fetching the Export Output

When the export state is `finished`, you can download the zip file containing the export catalog.

<table>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>GET</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/export</span>/&lt;export-id&gt;/&lt;fileName&gt;</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – Returns the exported catalog as a zip file with the given <span>&lt;fileName&gt;</span>.</p></td>
<td><p>404 Not Found – When the specified export ID is not found.</p></td>
</tr>
</tbody>
</table>

## Canceling an Export Operation

To cancel an export operation that you have started, send a DELETE request with the ID of the export operation.

<table>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>DELETE</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/export</span>/&lt;export-id&gt;</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>204 No Content – The specified export operation was canceled.</p></td>
<td><p>404 Not Found – When the specified export ID is not found.</p></td>
</tr>
</tbody>
</table>
