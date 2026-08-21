---
title: Updating File Resources
description: "For an existing file resource, you can update its name, description or file contents in several ways."
---

# 1.0.1 Updating File Resources

For an existing file resource, you can update its name, description or file contents in several ways.

The simplest way is to PUT a file descriptor containing the new file in base64 encoding. This new definition of the file resource overwrites the previous one.

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/resources</span>/path/to/resource</p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p>application/repository.file+json</p>
<p>application/repository.file+xml</p></td>
<td colspan="2"><p>A well defined file resource descriptor, as described in <a href="v2_resource_descriptor_types.md">1.0.1.14, “File,” on page 1</a>. The new contents of the file are base64 encoded in the <code>content</code> attribute of the descriptor.</p></td>
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

The second method allows you to update a file resource by direct streaming. You can specify the Content-Description and Content-Disposition headers to update the resource description or name, respectively.

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/resources</span>/path/to/resource</p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p>Content-Description: &lt;file-description&gt; - Becomes the description field of the created file resource</p>
<p>Content-Disposition: attachment; filename=&lt;filename&gt; - Becomes the name of the file resource</p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p>{MIME type}</p></td>
<td colspan="2"><p>The MIME type from <a href="uploading_file_resources.md">Table 1-1, “File Types and MIME Types,” on page 1</a> that corresponds to the desired file type. The body of the request then contains the binary data representation of that file format.</p></td>
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
