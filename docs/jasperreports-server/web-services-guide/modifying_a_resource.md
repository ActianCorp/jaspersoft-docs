---
title: Modifying a Resource
description: "The POST method on the resource service is used to modify a resource. If the resource has one or more file resources, they must be provided using a multipart request. A POST operates on the URL of an..."
---

# 1.0.1 Modifying a Resource

The POST method on the resource service is used to modify a resource. If the resource has one or more file resources, they must be provided using a multipart request. A POST operates on the URL of an existing resource, otherwise it is identical to the PUT method for a new resource.

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest/resource</span>/path/to/resource/</p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p>Resource<br />
Descriptor</p></td>
<td><p>String</p></td>
<td colspan="2"><p>This parameter identifies the part with an XML resource descriptor in a multipart request. This is a required argument when using multipart requests.</p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p>multipart/form-data</p>
<p>text/plain (in the first part)</p>
<p>application/octet-stream (for files)</p></td>
<td colspan="2"><p>A well-formed XML resourceDescriptor that fully describes the modified resource, including any locally defined resources. File resources are uploaded in separate parts.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>201 Created – The body is XML containing the resourceDescriptor of the resource just modified.</p></td>
<td><p>An error if the resource cannot be modified for some reason.</p></td>
</tr>
</tbody>
</table>
