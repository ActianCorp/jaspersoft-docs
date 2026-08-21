---
title: Delete Operation
description: "This operation deletes resources from the repository. If the specified resource is located in a report unit, you must set the request’s MODIFYREPORTUNITURI argument to the URI of the report unit you..."
---

# 1.1 Delete Operation

This operation deletes resources from the repository. If the specified resource is located in a report unit, you must set the request’s `MODIFY_REPORTUNIT_URI` argument to the URI of the report unit you want to modify.

If you are deleting a folder, all its content is removed recursively. There is no way to recover a deleted resource or folder, so use caution when calling this service.

The following sample request deletes a resource from a report unit:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">request</span> <span class="ot">operationName=</span><span class="st">&quot;delete&quot;</span> <span class="ot">locale=</span><span class="st">&quot;en&quot;</span>&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">argument</span> <span class="ot">name=</span><span class="st">&quot;MODIFY_REPORTUNIT_URI&quot;</span>&gt;/reports/JD_New_report&lt;/<span class="kw">argument</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">resourceDescriptor</span> <span class="ot">name=</span><span class="st">&quot;test_img&quot;</span> <span class="ot">wsType=</span><span class="st">&quot;img&quot;</span> <span class="ot">uriString=</span><span class="st">&quot;/reports/JD_New_report_files/test_img&quot;</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">label</span>&gt;test image&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">description</span>&gt;test image&lt;/<span class="kw">description</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">resourceDescriptor</span>&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">request</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>
