---
title: Downloading File Resources
description: "There are two operations on file resources:"
---

# 1.1.6 Downloading File Resources

There are two operations on file resources:

-   Viewing the file resource details to determine the file format
-   Downloading the binary file contents

To view the file resource details, specify the URL and the file descriptor type as follows:

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
<td><p>GET</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/resources</span>/path/to/file/resource</p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p>accept: application/repository.file+json</p>
<p>accept: application/repository.file+xml</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The response will the the file resource descriptor.</p></td>
<td><p>404 Not Found – The specified resource is not found in the repository.</p></td>
</tr>
</tbody>
</table>

The type attribute of the file resource descriptor indicates the format of the contents. However, you can also download the binary file contents directly, with the format indicated by the MIME content-type of the response:

<table>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>GET</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/resources</span>/path/to/file/resource</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The response content-type will indicate the MIME type of the binary contents. See for the list of MIME types that correspond to file resource types.</p></td>
<td><p>404 Not Found – The specified resource is not found in the repository.</p></td>
</tr>
</tbody>
</table>
