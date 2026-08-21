---
title: Report Locales
description: Reports that have resource bundles for localization can be generated in a specific languages when the locale is passed using the REPORTLOCALE built-in report parameter. If this parameter is not...
---

# 1.0.1 Report Locales

Reports that have resource bundles for localization can be generated in a specific languages when the locale is passed using the `REPORT_LOCALE` built-in report parameter. If this parameter is not specified in the web service request, the report locale defaults to the request's locale. If no locale was specified for the request, the report is generated in the server's default locale.

The following XML shows a request to run a report in the Italian locale, which is passed as the value of the `REPORT_LOCALE` built-in report parameter:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">request</span> <span class="ot">operationName=</span><span class="st">&quot;runReport&quot;</span> <span class="ot">locale=</span><span class="st">&quot;fr&quot;</span>&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">argument</span> <span class="ot">name=</span><span class="st">&quot;RUN_OUTPUT_FORMAT&quot;</span>&gt;JRPRINT&lt;/<span class="kw">argument</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">resourceDescriptor</span> <span class="ot">name=</span><span class="st">&quot;&quot;</span> <span class="ot">wsType=</span><span class="st">&quot;&quot;</span> <span class="ot">uriString=</span><span class="st">&quot;/reports/samples/EmployeeAccounts&quot;</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>                    <span class="ot">isNew=</span><span class="st">&quot;false&quot;</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">label</span>&gt;null&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">parameter</span> <span class="ot">name=</span><span class="st">&quot;REPORT_LOCALE&quot;</span>&gt;it&lt;/<span class="kw">parameter</span>&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">parameter</span> <span class="ot">name=</span><span class="st">&quot;EmployeeID&quot;</span>&gt;emil_id&lt;/<span class="kw">parameter</span>&gt;</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">resourceDescriptor</span>&gt;</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">request</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

If the built-in report parameter is removed from this request, the report is generated in French, based on the locale attribute of the request.
