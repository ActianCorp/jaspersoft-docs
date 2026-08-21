---
title: The resources Service
description: "The resources service lets you browse or search the repository. When used without arguments, it gives the list of resources in the folder specified in the URL. With the arguments, you can search for..."
---

# 1.1 The resources Service

The resources service lets you browse or search the repository. When used without arguments, it gives the list of resources in the folder specified in the URL. With the arguments, you can search for terms in the resource names or descriptions, search for all resources of a given type, and specify whether to search in subfolders. This service is similar to the `list` operation in the SOAP web services.

The resources service is a read only service. Requests for PUT, POST, and DELETE operations receive the error 405, method not allowed.

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest/resources</span>/path/to/folder/</p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p>q?</p></td>
<td><p>String</p></td>
<td colspan="2"><p>Match only resources having the specified text in the name or description. Note that the search string does not match in the ID of resources.</p></td>
</tr>
<tr>
<td><p>type?</p></td>
<td><p>wsType</p></td>
<td colspan="2"><p>Match only resources of the given type. Valid types are listed in <a href="wstype_attribute.md">Values for wsType</a>, for example: datasource, reportUnit, img, folder.</p>
<p>Searching by type does not always yield the expected results when using newer versions of the server (5.0 and later). New repository types may appear unexpectedly in the results. The v2/resources service resolves this issue, but the (v1) resources service is deprecated and will no longer be updated.</p></td>
</tr>
<tr>
<td><p>recursive?</p></td>
<td><p>0 | 1</p></td>
<td colspan="2"><p>Search for resources recursively and not only in the specified folder. This parameter is used only when a search criteria is specified (either q or type). When not specified, the default is 0, meaning only in the specified folder.</p>
<p>Note that searching recursively in the whole repository may cause performance issues, because the number of resources returned may be huge.</p></td>
</tr>
<tr>
<td><p>limit?</p></td>
<td><p>Integer &gt;= 0</p></td>
<td colspan="2"><p>Maximum number of items returned to the client. The default is 0, meaning no limit.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The body is XML containing the list of resourceDescriptors.</p></td>
<td><p>404 Not Found – The specified URI is not found in the repository.</p></td>
</tr>
</tbody>
</table>

The XML content in the result consists of resourceDescriptors described in section [Syntax of resourceDescriptor](syntax_of_resourcedescriptor.md). However, the list may be empty in the following conditions:

- If the specified URI is a resource instead of a folder.
- If the folder is empty or the search returns no results.

The following example shows the request to list the resources in the /reports folder:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><pre class="text"><code>GET /jasperserver/rest/resources/reports HTTP/1.1
User-Agent: Jakarta Commons-HttpClient/3.1
Authorization: Basic amFzcGVyYWRtaW46amFzcGVyYWRtaW4=
Host: localhost:8080
Cookie: $Version=0; JSESSIONID=6854BF45EC89F3D3CE3E6F4FD6FF1BBD; $Path=/jasperserver</code></pre></td>
</tr>
</tbody>
</table>

Because the example is not a recursive search, it simply returns the contents of the folder, in this case a subfolder and a report:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><pre class="text"><code>HTTP/1.1 200 OK
Server: Apache-Coyote/1.1
Pragma: No-cache
Cache-Control: no-cache
Expires: Thu, 01 Jan 1970 01:00:00 CET
Content-Length: 1518
Date: Fri, 24 Jun 2011 12:09:45 GMT</code></pre></td>
</tr>
<tr>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">resourceDescriptors</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceDescriptor</span> <span class="ot">name=</span><span class="st">&quot;samples&quot;</span> <span class="ot">wsType=</span><span class="st">&quot;folder&quot;</span> <span class="ot">uriString=</span><span class="st">&quot;/reports/samples&quot;</span></span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>                      <span class="ot">isNew=</span><span class="st">&quot;false&quot;</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">label</span>&gt;Samples&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">description</span>&gt;Samples&lt;/<span class="kw">description</span>&gt;</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">creationDate</span>&gt;1302268917000&lt;/<span class="kw">creationDate</span>&gt;</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_HAS_DATA&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;false&lt;/<span class="kw">value</span>&gt;&lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_RESOURCE_TYPE&quot;</span>&gt;</span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;com.jaspersoft.jasperserver.api.metadata.common.domain.Folder&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb2-11"><a href="#cb2-11" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_PARENT_FOLDER&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;/reports&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-12"><a href="#cb2-12" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb2-13"><a href="#cb2-13" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_SECURITY_PERMISSION_MASK&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;31&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-14"><a href="#cb2-14" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb2-15"><a href="#cb2-15" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_VERSION&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;0&lt;/<span class="kw">value</span>&gt;&lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb2-16"><a href="#cb2-16" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceDescriptor</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td><div class="sourceCode" id="cb3"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceDescriptor</span> <span class="ot">name=</span><span class="st">&quot;test&quot;</span> <span class="ot">wsType=</span><span class="st">&quot;reportUnit&quot;</span> <span class="ot">uriString=</span><span class="st">&quot;/reports/test&quot;</span></span>
<span id="cb3-2"><a href="#cb3-2" aria-hidden="true" tabindex="-1"></a>                      <span class="ot">isNew=</span><span class="st">&quot;false&quot;</span>&gt;</span>
<span id="cb3-3"><a href="#cb3-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">label</span>&gt;A test&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb3-4"><a href="#cb3-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">creationDate</span>&gt;1303206124000&lt;/<span class="kw">creationDate</span>&gt;</span>
<span id="cb3-5"><a href="#cb3-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_RESOURCE_TYPE&quot;</span>&gt;</span>
<span id="cb3-6"><a href="#cb3-6" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;com.jaspersoft.jasperserver.api.metadata.jasperreports.domain.</span>
<span id="cb3-7"><a href="#cb3-7" aria-hidden="true" tabindex="-1"></a>             ReportUnit&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb3-8"><a href="#cb3-8" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb3-9"><a href="#cb3-9" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_PARENT_FOLDER&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;/reports&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb3-10"><a href="#cb3-10" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb3-11"><a href="#cb3-11" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_SECURITY_PERMISSION_MASK&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;31&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb3-12"><a href="#cb3-12" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb3-13"><a href="#cb3-13" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_VERSION&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;19&lt;/<span class="kw">value</span>&gt;&lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb3-14"><a href="#cb3-14" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_RU_ALWAYS_PROPMT_CONTROLS&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;true&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb3-15"><a href="#cb3-15" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb3-16"><a href="#cb3-16" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_RU_CONTROLS_LAYOUT&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;1&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb3-17"><a href="#cb3-17" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb3-18"><a href="#cb3-18" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceDescriptor</span>&gt;</span>
<span id="cb3-19"><a href="#cb3-19" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">resourceDescriptors</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

The following sample request is intended to list all the reports available in the /reports folder and subfolders. The result, not shown, is a long list of resourceDescriptors for reports in the designated folders.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><pre class="text"><code>GET /jasperserver/rest/resources/reports?type=reportUnit&amp;recursive=1 HTTP/1.1
User-Agent: Jakarta Commons-HttpClient/3.1
Authorization: Basic amFzcGVyYWRtaW46amFzcGVyYWRtaW4=
Host: localhost:8080
Cookie: $Version=0; JSESSIONID=60B573BDC47098E6379FC867B24C5C0E; $Path=/jasperserver</code></pre></td>
</tr>
</tbody>
</table>
