---
title: Uploading File Resources
description: There are several ways of uploading file contents to create file resources. The simplest way is to POST a file descriptor containing the file in base64 encoding.
---

# 1.0.1 Uploading File Resources

There are several ways of uploading file contents to create file resources. The simplest way is to POST a file descriptor containing the file in base64 encoding.

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
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p>application/repository.file+json</p>
<p>application/repository.file+xml</p></td>
<td colspan="2"><p>A well defined file resource descriptor, as described in <a href="v2_resource_descriptor_types.md">1.0.1.14, “File,” on page 1</a>. The contents of the file are base64 encoded in the <code>content</code> attribute of the descriptor.</p></td>
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

You can also create a file resource with a multipart form request. The request parameters contain information that becomes the name and description of the new file resource.

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
<td colspan="2"><p>The request should include the following parameters:</p>
<ul>
<li>"label" containing the name of the file resource</li>
<li>"description" containing a description for the resource</li>
<li>"type" containing a file type shown in <span>Table 1-1</span></li>
<li>"data" containing the file contents</li>
</ul></td>
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

Another form allows you to create a file resource by direct streaming, without needing to create it first as a descriptor object. In this case, the required fields of the file descriptor are specified in HTTP headers.

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
<td colspan="2"><p>The MIME type from <span>Table 1-1</span> that corresponds to the desired file type. The body of the request then contains the binary data representation of that file format.</p></td>
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

When using MIME types, you must specify the MIME type that corresponds with the desired file type, as shown in the following table.

*Table 1-1 File Types and MIME Types*

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>File Types</p></th>
<th><p>Corresponding MIME Types</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>pdf</p></td>
<td><p>application/pdf</p></td>
</tr>
<tr>
<td><p>html</p></td>
<td><p>text/html</p></td>
</tr>
<tr>
<td><p>xls</p></td>
<td><p>application/xls</p></td>
</tr>
<tr>
<td><p>rtf</p></td>
<td><p>application/rtf</p></td>
</tr>
<tr>
<td><p>csv</p></td>
<td><p>text/csv</p></td>
</tr>
<tr>
<td><p>ods</p></td>
<td><p>application/vnd.oasis.opendocument.spreadsheet</p></td>
</tr>
<tr>
<td><p>odt</p></td>
<td><p>application/vnd.oasis.opendocument.text</p></td>
</tr>
<tr>
<td><p>txt</p></td>
<td><p>text/plain</p></td>
</tr>
<tr>
<td><p>docx</p></td>
<td><p>application/vnd.openxmlformats-officedocument.wordprocessingml.<br />
document</p></td>
</tr>
<tr>
<td><p>xlsx</p></td>
<td><p>application/vnd.openxmlformats-officedocument.spreadsheetml.sheet</p></td>
</tr>
<tr>
<td><p>font</p></td>
<td><p>font/*</p></td>
</tr>
<tr>
<td><p>img</p></td>
<td><p>image/*</p></td>
</tr>
<tr>
<td><p>jrxml</p></td>
<td><p>application/jrxml</p></td>
</tr>
<tr>
<td><p>jar</p></td>
<td><p>application/zip</p></td>
</tr>
<tr>
<td><p>prop</p></td>
<td><p>application/properties</p></td>
</tr>
<tr>
<td><p>jrtx</p></td>
<td><p>application/jrtx</p></td>
</tr>
<tr>
<td><p>xml</p></td>
<td><p>application/xml</p></td>
</tr>
<tr>
<td><p>css</p></td>
<td><p>text/css</p></td>
</tr>
<tr>
<td><p>accessGrantSchema</p></td>
<td><p>application/accessGrantSchema</p></td>
</tr>
<tr>
<td><p>olapMondrianSchema</p></td>
<td><p>application/olapMondrianSchema</p></td>
</tr>
</tbody>
</table>

You can cusomize this list of MIME types in the server by editing the `contentTypeMapping` map in the file .../WEB-INF/applicationContext-rest-services.xml. You can change MIME types for predefined types, add MIME types, or add custom types.
