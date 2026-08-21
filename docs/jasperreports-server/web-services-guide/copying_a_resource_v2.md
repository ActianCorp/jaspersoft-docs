---
title: Copying a Resource
description: "Copying a resource uses the Content-Location HTTP header to specify the source of the copy operation. If any resource descriptor is sent in the request, it is ignored."
---

# 1.1.9 Copying a Resource

Copying a resource uses the Content-Location HTTP header to specify the source of the copy operation. If any resource descriptor is sent in the request, it is ignored.

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/resources</span>/path/to/folder<br />
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
<td colspan="2"><p>When true, the target resource given in the URL is overwritten even if it is a different type than the resource descriptor in the content. The default is false.</p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p>Content-Location: {resourceSourceUri} - Specifies the resource to be copied.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>201 Created – The request was successful and, for confirmation, the response contains the full descriptor of the resource that was just copied.</p></td>
<td><p>404 Not Found – When the {resourceSourceUri} is not valid.</p></td>
</tr>
</tbody>
</table>
