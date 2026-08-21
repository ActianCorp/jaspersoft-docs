---
title: Creating a Resource
description: "The PUT method on the resource service is used to create a new resource. If the resource has one or more file resources, they must be provided using a multipart request."
---

# 1.0.1 Creating a Resource

The PUT method on the resource service is used to create a new resource. If the resource has one or more file resources, they must be provided using a multipart request.

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
<td colspan="2"><p>A well-formed XML resourceDescriptor that fully describes the resource, including any locally defined resources. File resources are uploaded in separate parts.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>201 Created – The body is XML containing the resourceDescriptor of the resource just created.</p></td>
<td><p>An error if the resource cannot be created for some reason. If you have very large files, see section <a href="setting_the_temporary_upload_directo.md">Setting the Temporary Upload Directory</a>.</p></td>
</tr>
</tbody>
</table>

In the following sample request, the URI is the location where we want to create the resource, in this case / (the root), and the content includes the resource descriptor for a new folder called myfolder.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><pre class="text"><code>PUT /jasperserver/rest/resource/ HTTP/1.1
Content-Length: 473
Content-Type: multipart/form-data; boundary=1afdzzMUQLfSOmu0Pgb2F-nmEnTwWuPf3
Host: localhost:8080
User-Agent: Apache-HttpClient/4.1.1 (java 1.5)
Cookie: JSESSIONID=3370EC843B09363C0A8DD09A2D1F21E3
Cookie2: $Version=1
--1afdzzMUQLfSOmu0Pgb2F-nmEnTwWuPf3
Content-Disposition: form-data; name=&quot;ResourceDescriptor&quot;
Content-Type: text/plain; charset=US-ASCII
Content-Transfer-Encoding: 8bit
&lt;resourceDescriptor name=&quot;myfolder&quot; wsType=&quot;folder&quot; uriString=&quot;/myfolder&quot;
                    isNew=&quot;false&quot;&gt;
  &lt;label&gt;REST created folder&lt;/label&gt;
  &lt;resourceProperty name=&quot;PROP_PARENT_FOLDER&quot;&gt;
    &lt;value&gt;/&lt;/value&gt;
  &lt;/resourceProperty&gt;
&lt;/resourceDescriptor&gt;
--1afdzzMUQLfSOmu0Pgb2F-nmEnTwWuPf3--</code></pre></td>
</tr>
</tbody>
</table>

Also, the example above shows a multi-part request even though it is only sending the plain-text resource descriptor and not a binary file. Usually, such requests could be sent without multiple parts, and multiple parts are used to send a binary file, for example when creating a report.

!!! note

    When the ResourceDescriptor contains the ResourceProperty `PROP_PARENT_FOLDER`, that property overrides the path/to/resource given as the URL and determines the location of the new resource.

The response to the PUT request is the complete resource descriptor for the new folder:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><pre class="text"><code>HTTP/1.1 201 Created
Server: Apache-Coyote/1.1
Cache-Control: no-cache
Content-Length: 648
Date: Mon, 01 Aug 2011 14:44:05 GMT
&lt;resourceDescriptor name=&quot;myfolder&quot; wsType=&quot;folder&quot; uriString=&quot;/myfolder&quot;
                    isNew=&quot;false&quot;&gt;
  &lt;label&gt;REST created folder&lt;/label&gt;
  &lt;creationDate&gt;1312209845000&lt;/creationDate&gt;
  &lt;resourceProperty name=&quot;PROP_RESOURCE_TYPE&quot;&gt;
    &lt;value&gt;com.jaspersoft.jasperserver.api.metadata.common.domain.Folder&lt;/value&gt;
  &lt;/resourceProperty&gt;
  &lt;resourceProperty name=&quot;PROP_PARENT_FOLDER&quot;&gt;
    &lt;value&gt;/&lt;/value&gt;
  &lt;/resourceProperty&gt;
  &lt;resourceProperty name=&quot;PROP_VERSION&quot;&gt;
    &lt;value&gt;0&lt;/value&gt;
  &lt;/resourceProperty&gt;
  &lt;resourceProperty name=&quot;PROP_HAS_DATA&quot;&gt;
    &lt;value&gt;false&lt;/value&gt;
  &lt;/resourceProperty&gt;
&lt;/resourceDescriptor&gt;</code></pre></td>
</tr>
</tbody>
</table>
