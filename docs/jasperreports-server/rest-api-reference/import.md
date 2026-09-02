---
title: The import Service
description: "Use the restv2/import service to upload a catalog as a zip file and import it into the repository with the given options. The service has two forms, depending on whether called from an application or..."
---

# The import Service

Use the rest_v2/import service to upload a catalog as a zip file and import it into the repository with the given options. The service has two forms, depending on whether called from an application or from a web page. This operation is Asynchronous. You must poll the state of the import to make sure it succeeds, or otherwise read an error code and retry the operation with different options.

This chapter includes the following sections:

-   [Launching an Import Operation](#launching-an-import-operation)
-   [Polling the Import Status](#polling-the-import-status)
-   [Import Errors](#import-errors)
-   [Restarting an Import Operation](#restarting-an-import-operation)
-   [Canceling an Import Operation](#canceling-an-import-operation)
-   [Importing from a Web Form](#importing-from-a-web-form)

## Launching an Import Operation

Typically, an application uses the rest_v2/import service to upload a catalog zip file as an attachment. Your application can specify import options as URL arguments in the format &lt;argument&gt;=true. Options that are omitted are assumed to be false. To import into root, you must be authenticated as the system admin (`superuser`), but organization admins (`jasperadmin`) may import into their organizations or suborganizations.

!!! warning

    As of JasperReports Server 7.5, import operations must specify a key to decrypt any passwords in the import catalog. Use either the secret-key or the secretUri parameter. For more information about import and export keys, see the JasperReports Server Security Guide.

The import operation is asynchronous. Your application should poll the status of the operation to determine when it finishes or has an error. In case of an error, you can restart the operation with new options or cancel it. The next sections of this chapter explain how to do this.

It is also possible to invoke the import service from a web page, as explained in [Importing from a Web Form](#importing-from-a-web-form).

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>POST</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/import</span>?&lt;arguments&gt;</span></p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><span>update?</span></p></td>
<td><p><span>true</span></p></td>
<td colspan="2"><p>Resources in the catalog replace those in the repository if their URIs and types match.</p></td>
</tr>
<tr>
<td><p><span>skipUserUpdate?</span></p></td>
<td><p><span>true</span></p></td>
<td colspan="2"><p>When used with <span>update=true</span>, users in the catalog are not imported or updated. Use this option to import catalogs without overwriting currently defined users.</p></td>
</tr>
<tr>
<td><p><span>broken<br />
Dependencies?</span></p></td>
<td><p><span>skip</span><br />
<span>include</span><br />
<span>fail</span></p></td>
<td colspan="2"><p>Defines the strategy when importing a resource with broken dependencies. The default value is fail.</p>
<ul>
<li><span>skip</span> –The resource with broken dependency is not imported, but the import operation continues.</li>
<li><span>include</span> – Attempts to import the resource by resolving dependencies with local resources. If unsuccessful, this resource is skipped.</li>
<li><span>fail</span> - The import operation stops and shows an error.</li>
</ul></td>
</tr>
<tr>
<td><p><span>organization?</span></p></td>
<td><p><span>orgID</span></p></td>
<td colspan="2"><p>Destination organization for importing. The file being imported must have been exported from an organization, not the root of the server. If this argument is not specified, the organization of the user performing the operation is used.</p></td>
</tr>
<tr>
<td><p><span>merge<br />
Organization?</span></p></td>
<td><p><span>true</span></p></td>
<td colspan="2"><p>When importing from one organization into a different organization, specify this argument. The resulting organization takes its ID from the import file. If the organization IDs of import and destination do not match, and this argument is not specified, the operation stops with an error.</p></td>
</tr>
<tr>
<td><p><span>skipThemes?</span></p></td>
<td><p><span>true</span></p></td>
<td colspan="2"><p>When this argument is specified, any themes in the import other than the default theme is ignored. Use this argument when importing catalogs from other JasperReports Server versions that used themes incompatible with your version.</p></td>
</tr>
<tr>
<td><p><span>includeAccess<br />
Events?</span></p></td>
<td><p><span>true</span></p></td>
<td colspan="2"><p>Restores the date, time, and user name of the last modification if they are included in the catalog to import.</p></td>
</tr>
<tr>
<td><p><span>includeAudit<br />
Events?</span></p></td>
<td><p><span>true</span></p></td>
<td colspan="2"><p>Imports audit events if they are included in the catalog.</p></td>
</tr>
<tr>
<td><p><span>includeMonitoring<br />
Events?</span></p></td>
<td><p><span>true</span></p></td>
<td colspan="2"><p>Imports monitoring events if they are included in the catalog.</p></td>
</tr>
<tr>
<td><p><span>includeServer<br />
Setting?</span></p></td>
<td><p><span>true</span></p></td>
<td colspan="2"><p>Imports server settings if they are included in the catalog.</p></td>
</tr>
<tr>
<td><p><span>keyAlias</span></p></td>
<td><p>key</p></td>
<td colspan="2"><p>Specify the alias of the key (for example "productionServerKey") associated with the import catalog. This is the key that was used to encrypt any passwords in the catalog when it was exported. The alias must correspond to a custom key in the importing server's keystore. When not specified, the server uses its own import-export key. In this case, the catalog must have been exported from this server, unless this key has been shared with another server.</p>
<p>For a list of available keys, see <a href="keys.md">“The keys Service” on page 1</a>. For more information about import and export keys, see the <span>JasperReports Server Security Guide</span>.</p></td>
</tr>
<tr>
<td><p><span>secret-key</span></p>
<p><span>secretUri</span></p></td>
<td></td>
<td colspan="2"><p>Deprecated for security reasons. See the Content-Type below.</p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>multipart/form-data</span></p></td>
<td colspan="2"><p>You must send the secret-key or secret-uri as form-data. See <a href="#importing-from-a-web-form">Importing from a Web Form</a>:</p>
<ul>
<li><p>secret-key: Specify the encryption key in hexadecimal format (for example "0x1c 0x40 0xb9 0xf6 0xe2 0xd3 0xf9 0xd0 0x5a 0xab 0x84 0xe6 0xd4 0xe8 0x5f 0xed") associated with the import catalog. You can obtain the key in hexadecimal format when exporting the catalog from the source server.</p></li>
<li><p>secret-uri: Specify the encryption key as the URI of a secure file resource in the repository. This must be the same key used when exporting the catalog from the source server.</p></li>
</ul></td>
</tr>
<tr>
<td colspan="2"><p><span>application/zip</span></p></td>
<td colspan="2"><p>The catalog file to import. Jaspersoft does not recommend uploading files greater than 2 gigabytes.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK - Returns a JSON object that indicates the import has been started. See sections on polling and error messages below.</p></td>
<td><p>401 Unauthorized - Import is available only to administrators (superuser or jasperadmin).</p></td>
</tr>
</tbody>
</table>

The body of the response contains the ID of the import operation needed to check its status:

``` text
{
    id:"aad78989-dasds32-dasdsd"
    phase: "inprogress",
    message: "Import in progress"
}
```

See the following sections to manage the asynchronous import operation.

## Polling the Import Status

To check the status of the import, use its ID in the following method:

<table>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>GET</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/import</span>/&lt;import-id&gt;/<span>state</span></span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK - The body of the response gives the current state of the import operation.</p></td>
<td><p>404 Not Found - When the specified import ID is not found.</p></td>
</tr>
</tbody>
</table>

As with the initial import request, the body of the response contains the state of the import operation, including its current phase and corresponding message:

``` text
{
    id:"aad78989-dasds32-dasdsd"
    phase: "inprogress",
    message: "Import in progress"
}
```

The following table describes the possible phases of the import operation:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>Import Phase</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><span>in progress</span></p></td>
<td><p>Import has begun and is still running.</p></td>
</tr>
<tr>
<td><p><span>finished</span></p></td>
<td><p>The import has been completed.</p></td>
</tr>
<tr>
<td><p><span>failed</span></p></td>
<td><p>The import had an error and was not completed.</p></td>
</tr>
<tr>
<td><p><span>pending</span></p></td>
<td><p>The import cannot run because of an error, but it can be restarted with new options. Pending happens if the import operation stopped with the following error codes:</p>
<ul>
<li>import.organizations.not.match</li>
<li>import.broken.dependencies</li>
</ul></td>
</tr>
</tbody>
</table>

## Import Errors

In the case of warnings or errors, the GET method returns a JSON structure that includes an error message and code. Some errors also have parameters given as a list of values, for example a list of resource URIs with broken dependencies.

``` text
{
    id:"aad78989-dasds32-dasdsd"
    phase: "pending",
    message: "Import is pending",
    error: {
       code: "import.broken.dependencies",
       parameters: [errorParams]
    }
}
```

The following tables list the most common warnings and errors, along with an array of parameters, if any. When there is more than one parameter, its position in the array determines its meaning. Some warnings have more than one form with different numbers of parameters:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th><p>Warning Code</p></th>
<th><p>Parameters</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><span>import.resource.uri.too.long</span></p></td>
<td><p><span>0=resourceURI</span></p></td>
<td><p>The URI given by the parameter is too long.</p></td>
</tr>
<tr>
<td><p><span>import.resource.uri.too.long</span></p></td>
<td><p><span>0=resourceURI</span><br />
<span>1=length</span></p></td>
<td><p>The URI given by the first parameter is too long. The second parameter is the maximum length.</p></td>
</tr>
<tr>
<td><p><span>import.access.denied</span></p></td>
<td><p><span>0=resourceURI</span></p></td>
<td><p>Access was denied when trying to import the resource with the given URI.</p></td>
</tr>
<tr>
<td><p><span>import.resource.not.found</span></p></td>
<td><p><span>0=resourceURI</span></p></td>
<td><p>The resource with the given URI cannot be found.</p></td>
</tr>
<tr>
<td><p><span>import.resource.different.type.</span><br />
<span>already.exists</span></p></td>
<td><p><span>0=resourceURI</span></p></td>
<td><p>The target of the given resource URI has a different type than the one being imported. The resource is not updated.</p></td>
</tr>
<tr>
<td><p><span>import.resource.uri.not.valid</span></p></td>
<td><p><span>0=resourceURI</span></p></td>
<td><p>The resource with the given URI is attached to an organization that is not valid in the target.</p></td>
</tr>
<tr>
<td><p><span>import.resource.data.missing</span></p></td>
<td><p><span>0=resourceURI</span></p></td>
<td><p>The resource with the given URI is missing from the catalog and is skipped.</p></td>
</tr>
<tr>
<td><p><span>import.reference.resource.not.found</span></p></td>
<td><p><span>0=resourceURI</span></p></td>
<td><p>The resource with the given URI has dependent resources that are not in the import catalog.</p></td>
</tr>
<tr>
<td><p><span>import.reference.resource.not.found</span></p></td>
<td><p><span>0=resourceURI</span><br />
<span>1=dependentURI</span></p></td>
<td><p>The resource with the first URI has a dependent resource with the second URI that is not in the import catalog.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th><p>Error Code</p></th>
<th><p>Parameters</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><span>import.organizations.not.match</span></p></td>
<td><p><span>0=catalogOrganization</span><br />
<span>1=targetOrganization</span></p></td>
<td><p>The organization ID contained in the import catalog does not match the target organization. Use the mergeOrganizations option.</p></td>
</tr>
<tr>
<td><p><span>import.broken.dependencies</span></p></td>
<td><p><span>0=resourceURI</span><br />
<span>1=resourceURI</span><br />
...</p></td>
<td><p>The resources in the list have broken dependencies in the import catalog.</p></td>
</tr>
<tr>
<td><p><span>import.organization.into.root.not.allowed</span></p></td>
<td><p><span>0=catalogOrganization</span></p></td>
<td><p>You cannot import the organization into the root.</p></td>
</tr>
<tr>
<td><p><span>import.root.into.organization.not.allowed</span></p></td>
<td><p><span>0=targetOrganization</span></p></td>
<td><p>The import catalog contains root resources that cannot be imported into the target organization.</p></td>
</tr>
<tr>
<td><p><span>import.failed</span></p></td>
<td><p><span>0=message</span></p></td>
<td><p>The import failed for the reason in the message.</p></td>
</tr>
<tr>
<td><p><span>import.failed.zip.error</span></p></td>
<td><p>none</p></td>
<td><p>The server cannot read the zip file.</p></td>
</tr>
<tr>
<td><p><span>import.failed.content.error</span></p></td>
<td><p>none</p></td>
<td><p>The zip file is not a valid import catalog.</p></td>
</tr>
</tbody>
</table>

## Restarting an Import Operation

When an import is in the pending state, you can try to restart it. To see the import options that led to the pending state, use the GET method with the import ID.

<table>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>GET</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/import</span>/&lt;import-id&gt;</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK - Returns a JSON object that contains the options of the import operation.</p></td>
<td><p>404 Not Found – When the specified import ID is not found.</p></td>
</tr>
</tbody>
</table>

The response contains a JSON structure that lists all options specified for this import operation:

``` json
{
   "brokenDependencies": "fail",
   "organization" : "organization_1",
   "parameters" : ["role-users", "repository-permissions"]
}
```

Once you know which options blocked the import operation, use the PUT method of the import service to send new options and restart the operation.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>PUT</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/import</span>/&lt;import-id&gt;</span></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/json</span></p></td>
<td colspan="2"><p>A JSON object that contains the new import options, for example:</p>
<div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>   <span class="dt">&quot;brokenDependencies&quot;</span><span class="fu">:</span> <span class="st">&quot;include&quot;</span><span class="fu">,</span>  </span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>   <span class="dt">&quot;organization&quot;</span> <span class="fu">:</span> <span class="st">&quot;organization_1&quot;</span><span class="fu">,</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>   <span class="dt">&quot;parameters&quot;</span> <span class="fu">:</span> <span class="ot">[</span><span class="st">&quot;role-users&quot;</span><span class="ot">,</span> <span class="st">&quot;repository-permissions&quot;</span><span class="ot">]</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK - The body of the response is shown below.</p></td>
<td><p>404 Not Found - When the specified import ID is not found.</p></td>
</tr>
</tbody>
</table>

The body of the response shows the import options that were applied:

``` json
{
   "brokenDependencies": "include",
   "organization" : "organization_1",
   "parameters" : ["role-users", "repository-permissions"]
}
```

## Canceling an Import Operation

To cancel an import operation that you have started, send a DELETE request with the ID of the operation.

<table>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>DELETE</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/import</span>/&lt;import-id&gt;</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>204 No Content - The specified export operation was canceled.</p></td>
<td><p>404 Not Found - When the specified import ID is not found.</p></td>
</tr>
</tbody>
</table>

## Importing from a Web Form

Alternatively, you can call the `import` service directly from a web page with `form` and `input` tags. Use inputs from the Import options checkbox to submit the import options and a file input to upload the catalog zip file.

Submitting an import catalog through an HTML form is also an Asynchronous operation. However, web pages are not practical for receiving the ID and polling the status of the import operation. Therefore, you are limited in knowing whether the import succeeded as you cannot restart the import service if needed.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>POST</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/import</span></span></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>multipart/form-data</span></p></td>
<td colspan="2"><p>The form data is sent by the browser when you submit a page with <code>input</code> tags. For example:</p>
<div class="language-text highlight"><pre><code>form-data; name=&quot;file-name&quot;,
form-data; name=&quot;include-access-events&quot;,
form-data; name=&quot;update&quot;,
...</code></pre></div></td>
</tr>
<tr>
<td colspan="2"><p><span>application/zip</span></p></td>
<td colspan="2"><p>The catalog file to import. Jaspersoft does not recommend uploading files greater than 2 gigabytes.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – Returns a JSON object that indicates the import has been started.</p></td>
<td><p>401 Unauthorized – Import is available only to administrators (superuser or jasperadmin).</p></td>
</tr>
</tbody>
</table>

The form data options are similar to the arguments in the other import format. When you select a form data option, the option is set to true. Otherwise, the option is set to false by default.

When an option name is submitted in the form data with any value, then the form data options are considered true for the operation.

!!! note

    If you do not want to enable any of the import options, then do not specify those option names in the import request when submitting the form.

The following table describes the options that you can submit in the import request:

| Import Web Form Options | Description |
|----|----|
| update | When the catalog contains resources with the same path and type as existing resources in the repository, then those in the repository is overwritten. Roles and users in an organization are also overwritten with any in the catalog. |
| skip-user-update | When update is specified, you can also specify this option to avoid overwriting any user profiles. |
| merge-organization | In commercial releases with organizations, specify this option if the catalog is exported from one organization and imported into a different one. If this option is not specified, and the catalog is sourced from a different organization than the destination, and the import fails. |
| skip-themes | In commercial releases, specify this option to ignore any themes in the catalog. Otherwise, any themes in the catalog are imported into the repository. |
| include-access-events | When specified, the timestamps for resource creation and modification of each resource are imported into the repository. |
| include-audit-events | When this option is specified, any audit event logs in the catalog are imported into the server's audit event logs. |
| include-alerts | Includes data alert when importing the report. |
| include-monitoring-events | When this option is specified, any monitoring event logs in the catalog are imported into the server's monitoring event logs. |
| include-server-settings | When this option is specified, any global server settings in the catalog are imported into the server. |

The following HTML example shows how the `import` service can be invoked from a web page:

``` xml
<form method="post"
      action="http://example.com:8090/jasperserver-pro/rest_v2/import"
      enctype="multipart/form-data">
    Import a catalog file to JasperReports Server:
    <input type="file" name="file-name" required="true" accept="application/zip">
    <fieldset>
        <legend>Options:</legend>
        <input type="checkbox" name="update">Overwrite resources of the same name<br>
          <input type="checkbox" name="skip-user-update">But do not overwrite users<br>
        <input type="checkbox" name="merge-organization">Import into a different organization<br>
        <input type="checkbox" name="skip-themes">Do not import themes<br>
        <input type="checkbox" name="include-access-events">Import created/modified timestamps<br>
        <input type="checkbox" name="include-audit-events">Import audit event logs<br>
        <input type="checkbox" name="include-monitoring-events">Import monitoring event logs<br>
        <input type="checkbox" name="include-server-settings">Import global server settings<br>
    </fieldset>
    <input type="submit" value="Submit">
</form>
```
