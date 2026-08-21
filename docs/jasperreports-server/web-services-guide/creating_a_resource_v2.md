---
title: Creating a Resource
description: The POST and PUT methods offer alternative ways to create resources. Both take a resource descriptor but each handles the URL differently.
---

# Creating a Resource

The POST and PUT methods offer alternative ways to create resources. Both take a resource descriptor but each handles the URL differently.

With the POST method, specify a folder in the URL, and the new resource ID is created automatically from the label attribute in its descriptor.

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/resources</span>/path/to/folder?&lt;param&gt;</p></td>
</tr>
<tr>
<td><p>Parameter</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p>create<br />
Folders</p></td>
<td><p>true|false</p></td>
<td colspan="2"><p>By default, this is true, and the service will create all parent folders if they don't already exist. When set to false, the folders specified in the URL must all exist, otherwise the service returns an error.</p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p>application/repository.</p>
<p>&lt;resourceType&gt;+json</p>
<p>application/repository.</p>
<p>&lt;resourceType&gt;+xml</p></td>
<td colspan="2"><p>A well defined descriptor of the specified type and format. See <a href="v2_resource_descriptor_types.md">V2 Resource Descriptor Types</a></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>201 Created – The request was successful and, for confirmation, the response contains the full descriptor of the resource that was just created.</p></td>
<td><p>400 Bad Request – Mismatch between the content-type and the fields or syntax of the actual descriptor.</p></td>
</tr>
</tbody>
</table>

With the PUT method, specify a unique new resource ID as part of the URL. For more information, see [Resource IDs](the_v2_resources_service.md).

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
<td><p>PUT</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/resources</span>/path/to/resource<br />
?&lt;parameters&gt;</p></td>
</tr>
<tr>
<td><p>Parameters</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p>create<br />
Folders</p></td>
<td><p>true|false</p></td>
<td colspan="2"><p>True by default, and the service will create all parent folders if they don't already exist. When set to false, the folders specified in the URL must all exist, otherwise the service returns an error.</p></td>
</tr>
<tr>
<td><p>overwrite</p></td>
<td><p>true|false</p></td>
<td colspan="2"><p>When true, the resource given in the URL is overwritten even if it is a different type than the resource descriptor in the content. The default is false.</p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p>application/repository.</p>
<p>&lt;resourceType&gt;+json</p>
<p>application/repository.</p>
<p>&lt;resourceType&gt;+xml</p></td>
<td colspan="2"><p>A well defined descriptor of the specified type and format. See <a href="v2_resource_descriptor_types.md">V2 Resource Descriptor Types</a></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>201 Created – The request was successful and, for confirmation, the response contains the full descriptor of the resource that was just created.</p></td>
<td><p>400 Bad Request – Mismatch between the content-type and the fields or syntax of the actual descriptor.</p></td>
</tr>
</tbody>
</table>

The POST method also supports a way to create complex resources and their nested resources in a single multipart request.

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/resources</span>/path/to/folder</p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p>multipart/form-data</p></td>
<td colspan="2"><p>Root resource multipart item name: resource</p>
<p>Root resource multipart Content-type and corresponding item names:</p>
<ul>
<li>mondrianConnection:</li>
</ul>
<p>- schema: mondrian schema XML file</p>
<ul>
<li>secureMondrianConnection:</li>
</ul>
<p>- schema: mondrian schema XML file</p>
<p>- accessGrantSchemas.accessGrantSchema[{itemIndex}]: XML file</p>
<ul>
<li>semanticLayerDataSource:</li>
</ul>
<p>- schema: domain schema XML file</p>
<p>- securityFile: security file XML</p>
<p>- bundles.bundle[{bundleIndex}]: i18n properties file</p>
<ul>
<li>reportUnit</li>
</ul>
<p>- jrxml: report unit JRXML file</p>
<p>- files.{fileName}: report unit attached resource file (e.g. images)</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>201 Created – The request was successful and, for confirmation, the response contains the full descriptor of the resource that was just created.</p></td>
<td><p>400 Bad Request – Mismatch between the content-type and the fields or syntax of the actual descriptor.</p></td>
</tr>
</tbody>
</table>
