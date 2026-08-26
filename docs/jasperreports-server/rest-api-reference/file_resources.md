---
title: Working With File Resources
description: "This chapter includes the following sections:"
---

# Working With File Resources

This chapter includes the following sections:

-   MIME Types
-   Downloading File Resources
-   Uploading File Resources
-   Updating File Resources

## MIME Types

When downloading or uploading file contents, you must specify the MIME type (Multi-Purpose Internet Mail Extensions) that corresponds with the desired file type, as shown in the following table.

You can customize this list of MIME types in the server by editing the `contentTypeMapping` map in the file .../WEB-INF/applicationContext-rest-services.xml. You can change MIME types for predefined types, add MIME types, or add custom types.

<table>
<caption><p>MIME Types for File Contents</p></caption>
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
<td><p><span>pdf</span></p></td>
<td><p><span>application/pdf</span></p></td>
</tr>
<tr>
<td><p><span>html</span></p></td>
<td><p><span>text/html</span></p></td>
</tr>
<tr>
<td><p><span>xls</span></p></td>
<td><p><span>application/xls</span></p></td>
</tr>
<tr>
<td><p><span>rtf</span></p></td>
<td><p><span>application/rtf</span></p></td>
</tr>
<tr>
<td><p><span>csv</span></p></td>
<td><p><span>text/csv</span></p></td>
</tr>
<tr>
<td><p><span>ods</span></p></td>
<td><p><span>application/vnd.oasis.opendocument.spreadsheet</span></p></td>
</tr>
<tr>
<td><p><span>odt</span></p></td>
<td><p><span>application/vnd.oasis.opendocument.text</span></p></td>
</tr>
<tr>
<td><p><span>txt</span></p></td>
<td><p><span>text/plain</span></p></td>
</tr>
<tr>
<td><p><span>docx</span></p></td>
<td><p><span>application/vnd.openxmlformats-officedocument.wordprocessingml.<br />
document</span></p></td>
</tr>
<tr>
<td><p><span>xlsx</span></p></td>
<td><p><span>application/vnd.openxmlformats-officedocument.spreadsheetml.sheet</span></p></td>
</tr>
<tr>
<td><p><span>font</span></p></td>
<td><p><span>font/*</span> <sup>*</sup></p></td>
</tr>
<tr>
<td><p><span>img</span></p></td>
<td><p><span>image/*</span> <sup>*</sup></p></td>
</tr>
<tr>
<td><p><span>jrxml</span></p></td>
<td><p><span>application/jrxml</span></p></td>
</tr>
<tr>
<td><p><span>jar</span></p></td>
<td><p><span>application/zip</span></p></td>
</tr>
<tr>
<td><p><span>prop</span></p></td>
<td><p><span>application/properties</span></p></td>
</tr>
<tr>
<td><p><span>jrtx</span></p></td>
<td><p><span>application/jrtx</span></p></td>
</tr>
<tr>
<td><p><span>xml</span></p></td>
<td><p><span>application/xml</span></p></td>
</tr>
<tr>
<td><p><span>css</span></p></td>
<td><p><span>text/css</span></p></td>
</tr>
<tr>
<td><p><span>accessGrantSchema</span></p></td>
<td><p><span>application/accessGrantSchema</span></p></td>
</tr>
<tr>
<td><p><span>olapMondrianSchema</span></p></td>
<td><p><span>application/olapMondrianSchema</span></p></td>
</tr>
</tbody>
</table>

^\*^ For the font and img file types when using the HTTP URL, MIME types of font/\* and image/\* respectively continues to work. However, for the HTTPS URL the MIME type must be explicitly specified based on the type of font or image file used. For example, font/ttf, image/png.

## Downloading File Resources

There are two read operations on file resources:

-   Viewing the file resource details to determine the file format.
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
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>GET</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/resources</span>/path/to/file/resource</span></p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p><span>accept: application/repository.file+json</span></p>
<p><span>accept: application/repository.file+xml</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK - The response contains the file resource descriptor.</p></td>
<td><p>404 Not Found - The specified resource is not found in the repository.</p></td>
</tr>
</tbody>
</table>

The type attribute of the file resource descriptor indicates the format of the contents. However, you can also download the binary file contents directly, with the format indicated by the MIME content-type of the response:

<table>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>GET</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/resources</span>/path/to/file/resource</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK - The response content-type indicates the MIME type of the binary contents. See <span>Table 1-1, “MIME Types for File Contents,” on page 1</span> for the list of MIME types that correspond to file resource types.</p></td>
<td><p>404 Not Found - The specified resource is not found in the repository.</p></td>
</tr>
</tbody>
</table>

## Uploading File Resources

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
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>POST</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/resources</span>/path/to/folder?&lt;argument&gt;</span></p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><span>create<br />
Folders</span></p></td>
<td><p>true|false</p></td>
<td colspan="2"><p>True by default, and the service creates all parent folders if they do not already exist. When set to false, the folders specified in the URL must all exist, otherwise the service returns an error.</p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/repository.file+json</span></p>
<p><span>application/repository.file+xml</span></p></td>
<td colspan="2"><p>A well-defined file resource descriptor, as described in <a href="resource_descriptors.md">1.14, “File,” on page 1</a>. The contents of the file are base64-encoded in the <code>content</code> attribute of the descriptor.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>201 Created - The request was successful and, for confirmation, the response contains the full descriptor of the resource that was just created.</p></td>
<td><p>400 Bad Request - Mismatch between the content-type and the fields or syntax of the actual descriptor.</p></td>
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
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>POST</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/resources</span>/path/to/folder</span></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>multipart/form-data</span></p></td>
<td colspan="2"><p>The request should include the following parameters:</p>
<ul>
<li><span>label</span> - contains the name of the file resource</li>
<li><span>description</span> - contains a description for the resource</li>
<li><span>type</span> - contains a file type shown in <span>Table 1-1, “MIME Types for File Contents,” on page 1</span></li>
<li><span>data</span> - contains the file contents</li>
</ul></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>201 Created - The request was successful and, for confirmation, the response contains the full descriptor of the resource that was just created.</p></td>
<td><p>400 Bad Request - Mismatch between the content-type and the fields or syntax of the actual descriptor.</p></td>
</tr>
</tbody>
</table>

Another form allows you to create a file resource by direct streaming, without needing to create it first as a descriptor object. In this case, the required fields of the file descriptor are specified in the HTTP headers.

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
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/resources</span>/path/to/folder</span></p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p><span>Content-Description: &lt;file-description&gt;</span> – Becomes the description field of the created file resource</p>
<p><span>Content-Disposition: attachment; filename=&lt;filename&gt;</span> – Becomes the name of the file resource</p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>{MIME type}</span></p></td>
<td colspan="2"><p>The MIME type from <span>Table 1-1, “MIME Types for File Contents,” on page 1</span> that corresponds to the desired file type. The body of the request then contains the binary data representation of that file format.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>201 Created - The request was successful and, for confirmation, the response contains the full descriptor of the resource that was just created.</p></td>
<td><p>400 Bad Request - Mismatch between the content-type and the fields or syntax of the actual descriptor.</p></td>
</tr>
</tbody>
</table>

## Updating File Resources

For an existing file resource, you can update its name, description, or file contents in several ways.

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
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>PUT</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/resources</span>/path/to/resource</span></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/repository.file+json</span></p>
<p><span>application/repository.file+xml</span></p></td>
<td colspan="2"><p>A well-defined file resource descriptor, as described in <a href="resource_descriptors.md">1.14, “File,” on page 1</a>. The new contents of the file are base64-encoded in the <code>content</code> attribute of the descriptor.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>201 Created - The request was successful and, for confirmation, the response contains the full descriptor of the resource that was just created.</p></td>
<td><p>400 Bad Request - Mismatch between the content-type and the fields or syntax of the actual descriptor.</p></td>
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
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>PUT</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/resources</span>/path/to/resource</span></p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p><span>Content-Description: &lt;file-description&gt;</span> - Becomes the description field of the created file resource</p>
<p><span>Content-Disposition: attachment; filename=&lt;filename&gt;</span> -Becomes the name of the file resource</p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>{MIME type}</span></p></td>
<td colspan="2"><p>The MIME type from <span>Table 1-1, “MIME Types for File Contents,” on page 1</span> that corresponds to the desired file type. The body of the request then contains the binary data representation of that file format.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>201 Created - The request was successful and, for confirmation, the response contains the full descriptor of the resource that was just created.</p></td>
<td><p>400 Bad Request - Mismatch between the content-type and the fields or syntax of the actual descriptor.</p></td>
</tr>
</tbody>
</table>
