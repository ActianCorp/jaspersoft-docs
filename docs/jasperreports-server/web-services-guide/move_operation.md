---
title: Move Operation
description: This operation moves a repository folder or resource to a different folder in the repository. The operation exposes the API repository service moveResource and moveFolder methods.
---

# 1.1 Move Operation

This operation moves a repository folder or resource to a different folder in the repository. The operation exposes the API repository service `moveResource` and `moveFolder` methods.

The operation expects (as part of the request) a resource descriptor that identifies the resource or folder to be moved. The new location of the resource or folder must be provided as the value of the `DESTINATION_URI` request argument. The destination URI must resolve to an existing repository folder.

The following request moves the report unit located at /Reports/NewReport to /MyReports:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">request</span> <span class="ot">operationName=</span><span class="st">&quot;move&quot;</span> <span class="ot">locale=</span><span class="st">&quot;en&quot;</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a><span class="er">&lt;argument</span> <span class="ot">name=</span><span class="st">&quot;DESTINATION_URI&quot;</span>&gt;/MyReports&lt;/<span class="kw">argument</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">resourceDescriptor</span> <span class="ot">name=</span><span class="st">&quot;NewReport&quot;</span> <span class="ot">wsType=</span><span class="st">&quot;reportUnit&quot;</span> <span class="ot">uriString=</span><span class="st">&quot;/Reports/NewReport&quot;</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">resourceDescriptor</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">request</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>
