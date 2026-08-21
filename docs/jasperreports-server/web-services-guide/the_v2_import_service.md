---
title: The v2/import Service
description: "Use the following service to upload a catalog as a zip file and import it with the given options. Specify options as arguments in the format <argument>=true. Arguments that are omitted are assumed to..."
---

# 1.1 The v2/import Service

Use the following service to upload a catalog as a zip file and import it with the given options. Specify options as arguments in the format \<argument\>=true. Arguments that are omitted are assumed to be false. You must be authenticated as the system admin (superuser) to import into root, but organization admins may import into their organizations or suborganizations.

Jaspersoft does not recommend uploading files greater than 2 gigabytes.

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
<td><p>POST</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/import</span>?&lt;arguments&gt;</p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p>update?</p></td>
<td><p>true</p></td>
<td colspan="2"><p>Resources in the catalog replace those in the repository if their URIs and types match.</p></td>
</tr>
<tr>
<td><p>skipUserUpdate?</p></td>
<td><p>true</p></td>
<td colspan="2"><p>When used with update=true, users in the catalog are not imported or updated. Use this option to import catalogs without overwriting currently defined users.</p></td>
</tr>
<tr>
<td><p>broken<br />
Dependencies?</p></td>
<td><p>skip<br />
include<br />
fail</p></td>
<td colspan="2"><p>Defines the strategy when importing a resource with broken dependencies. The default value is fail.</p>
<p>skip - The resource with broken dependency won't be imported, but the import operation will continue.</p>
<p>include - Attempts to import the resource by resolving dependencies with local resources. If unsuccessful, this resource is skipped.</p>
<p>fail - The import operation will stop and return an error.</p></td>
</tr>
<tr>
<td><p>organization?</p></td>
<td><p>orgID</p></td>
<td colspan="2"><p>Destination organization for importing. The file being imported must have been exported from an organization, not the root of the server. If this argument is not specified, the organization of the user performing the operation is used.</p></td>
</tr>
<tr>
<td><p>merge<br />
Organization?</p></td>
<td><p>true</p></td>
<td colspan="2"><p>When importing from one organization into a different organization, specify this argument. The resulting organization takes its ID from the import file. If organization IDs of import and destination do not match, and this argument is not specified, the operation stops with an error.</p></td>
</tr>
<tr>
<td><p>skipThemes?</p></td>
<td><p>true</p></td>
<td colspan="2"><p>When this argument is specified, any themes in the import other than the default theme is ignored. Use this argument when importing catalogs from servers before release 5.5 whose themes are incompatible.</p></td>
</tr>
<tr>
<td><p>includeAccess<br />
Events?</p></td>
<td><p>true</p></td>
<td colspan="2"><p>Restores the date, time, and user name of last modification if they are included in the catalog to import.</p></td>
</tr>
<tr>
<td><p>includeAudit<br />
Events?</p></td>
<td><p>true</p></td>
<td colspan="2"><p>Imports audit events if they are included in the catalog.</p></td>
</tr>
<tr>
<td><p>includeMonitoring<br />
Events?</p></td>
<td><p>true</p></td>
<td colspan="2"><p>Imports audit events if they are included in the catalog.</p></td>
</tr>
<tr>
<td><p>includeServer<br />
Setting?</p></td>
<td><p>true</p></td>
<td colspan="2"><p>Imports server settings if they are included in the catalog.</p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p>application/zip</p></td>
<td colspan="2"><p>The catalog file to import.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – Returns a JSON object that indicates the import was a success.</p></td>
<td><p>401 Unauthorized – Import is available only to the system admin user (superuser).</p></td>
</tr>
</tbody>
</table>

The body of the response contains the ID of the import operation needed to check its status:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">state</span>&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">id</span>&gt;2cc871ee-4645-4be0-b5b4-7d7c45c561cb&lt;/<span class="kw">id</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">message</span>&gt;Import in progress.&lt;/<span class="kw">message</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">phase</span>&gt;inprogress&lt;/<span class="kw">phase</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">state</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

To check the status of the import, use its ID in the following method:

<table>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>GET</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/import</span>/&lt;import-id&gt;/<span>state</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The body of the response gives the current state of the export operation.</p></td>
<td><p>404 Not Found – When the specified import ID is not found.</p></td>
</tr>
</tbody>
</table>
