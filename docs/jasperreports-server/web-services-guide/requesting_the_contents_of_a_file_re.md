---
title: Requesting the Contents of a File Resource
description: "In order to retrieve the contents of a file, first retrieve the descriptor of its enclosing resource to find the resource URI. The resource can either be internal to the report, or referenced from..."
---

# 1.0.1 Requesting the Contents of a File Resource

In order to retrieve the contents of a file, first retrieve the descriptor of its enclosing resource to find the resource URI. The resource can either be internal to the report, or referenced from the repository. In either case it has a URI in the repository that we can extract from the parent resource.

In the previous sample, we see the attachments that are internal to the AllAccounts report. There is an image named AllAccounts_Res3 that is not a reference and has data. To download the image, we create the following request to the resource service, giving it the internal URI of the image and `fileData=true`.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><pre class="text"><code>GET /jasperserver/rest/resource/reports/samples/AllAccounts_files/AllAccounts_Res3?
fileData=true HTTP/1.1
User-Agent: Jakarta Commons-HttpClient/3.1
Authorization: Basic amFzcGVyYWRtaW46amFzcGVyYWRtaW4=
Host: localhost:8080
Cookie: $Version=0; JSESSIONID=6854BF45EC89F3D3CE3E6F4FD6FF1BBD; $Path=/jasperserver</code></pre></td>
</tr>
</tbody>
</table>

!!! note

    Notice that the URI to the file includes the path AllAccounts_files. This is a local path that exists to access the local resources of the report, not a folder that exists in the repository.

In the case of a resource that is referenced in the repository, you can download the contents of the file in the same way. From the resource descriptor in the previous section, we see there is another resource where `PROP_IS_REFERENCE` is `true`. We can extract the repository URI from the `PROP_REFERENCE_URI` property and use that with `fileData=true` to obtain the image:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><pre class="text"><code>GET /jasperserver-pro/rest/resource/images/JRLogo?fileData=true HTTP/1.1
User-Agent: Jakarta Commons-HttpClient/3.1
Authorization: Basic amFzcGVyYWRtaW46amFzcGVyYWRtaW4=
Host: localhost:8080
Cookie: $Version=0; JSESSIONID=6854BF45EC89F3D3CE3E6F4FD6FF1BBD; $Path=/jasperserver</code></pre></td>
</tr>
</tbody>
</table>

In both cases, the response contains the binary contents of the file. The response header contains the information to decode it:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">Content-Disposition</span><span class="kw">:</span><span class="at"> attachment; filename=JRLogo</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a><span class="fu">Content-Type</span><span class="kw">:</span><span class="at"> application/octet-stream</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a><span class="fu">Content-Length</span><span class="kw">:</span><span class="at"> </span><span class="dv">1491</span></span></code></pre></div></td>
</tr>
</tbody>
</table>

!!! note

    The descriptor does not store the extension nor the format of a file resource. Jaspersoft recommends using the filename with the file extension as the resource ID when creating file resources so that the extension is available when downloading the file.
