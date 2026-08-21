---
title: Copy Operation
description: This operation creates a copy of an existing resource or folder. The operation exposes the repository service copyResource and copyFolder API methods.
---

# 1.1 Copy Operation

This operation creates a copy of an existing resource or folder. The operation exposes the repository service `copyResource` and `copyFolder` API methods.

The resource or folder to be copied is sent as the resource descriptor of the request; the caller does not need to provide the full resource information; just the information required to locate the resource is required.

The full location of the copy must be provided as the value of the `DESTINATION_URI` request argument. If this location already exists in the repository at the moment the operation is called, the server automatically changes the name part of the destination URI and saves the resource or folder copy at the new URI.

The copy operation response includes a descriptor for the saved resource or folder copy. The response descriptor is particularly useful in determining whether the copy has been created at the specified destination URI or at a different/generated URI.

When a folder is being copied, all its subfolders and contained resources are copied recursively.

The following request copies the report unit located at /Reports/NewReport to /MyReports/NewReportCopy:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">request</span> <span class="ot">operationName=</span><span class="st">&quot;copy&quot;</span> <span class="ot">locale=</span><span class="st">&quot;en&quot;</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a><span class="er">&lt;argument</span> <span class="ot">name=</span><span class="st">&quot;DESTINATION_URI&quot;</span>&gt;/MyReports/NewReportCopy&lt;/<span class="kw">argument</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">resourceDescriptor</span> <span class="ot">name=</span><span class="st">&quot;NewReport&quot;</span> <span class="ot">wsType=</span><span class="st">&quot;reportUnit&quot;</span> <span class="ot">uriString=</span><span class="st">&quot;/Reports/NewReport&quot;</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">resourceDescriptor</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">request</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>
