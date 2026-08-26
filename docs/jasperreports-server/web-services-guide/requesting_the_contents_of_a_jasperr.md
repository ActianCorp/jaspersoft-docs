---
title: Requesting the Contents of a JasperReport
description: "A JasperReport is a complex resource that contains many parts such as a data source, input controls, and file resources. These can be either references to other resources in the repository or..."
---

# 1.0.1 Requesting the Contents of a JasperReport

A JasperReport is a complex resource that contains many parts such as a data source, input controls, and file resources. These can be either references to other resources in the repository or resources that are fully defined internally to the report.

In the following example, a simple request gives the contents of a JasperReport:

GET http://localhost:8080/jasperserver/rest/resource/reports/samples/AllAccounts

The following response in this example shows the content of the AllAccounts report:

-   The reportUnit, which is the container for all the resources of the report.
-   The data source, which is an external link to a data source in the repository.
-   The main JRXML, which is a file defined internally to this resource.
-   Two image files, one of which is defined internally to this resource, the other references a file resource in the repository.

The structure of the JasperReport is defined through nested `resourceDescriptor` tags in XML. In the nested descriptor for each file that is part of the JasperReport, we can find its URI and use `fileData=true` to retrieve that file:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">resourceDescriptor</span> <span class="ot">name=</span><span class="st">&quot;AllAccounts&quot;</span> <span class="ot">wsType=</span><span class="st">&quot;reportUnit&quot;</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>                    <span class="ot">uriString=</span><span class="st">&quot;/reports/samples/AllAccounts&quot;</span> <span class="ot">isNew=</span><span class="st">&quot;false&quot;</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">label</span>&gt;Accounts Report&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">description</span>&gt;All Accounts Report&lt;/<span class="kw">description</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">creationDate</span>&gt;1302268918000&lt;/<span class="kw">creationDate</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_RESOURCE_TYPE&quot;</span>&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;com.jaspersoft.jasperserver.api.metadata.jasperreports.domain.</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>           ReportUnit&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_PARENT_FOLDER&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;/reports/samples&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_VERSION&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;2&lt;/<span class="kw">value</span>&gt;&lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_RU_ALWAYS_PROPMT_CONTROLS&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;false&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_RU_CONTROLS_LAYOUT&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;1&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceDescriptor</span> <span class="ot">name=</span><span class="st">&quot;&quot;</span> <span class="ot">wsType=</span><span class="st">&quot;datasource&quot;</span> <span class="ot">uriString=</span><span class="st">&quot;&quot;</span> <span class="ot">isNew=</span><span class="st">&quot;false&quot;</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">label</span>&gt;null&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_REFERENCE_URI&quot;</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;/datasources/JServerJNDIDS&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_IS_REFERENCE&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;true&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceDescriptor</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td><div class="sourceCode" id="cb3"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceDescriptor</span> <span class="ot">name=</span><span class="st">&quot;AllAccountsReport&quot;</span> <span class="ot">wsType=</span><span class="st">&quot;jrxml&quot;</span> <span class="ot">uriString=</span><span class="st">&quot;/reports/</span></span>
<span id="cb3-2"><a href="#cb3-2" aria-hidden="true" tabindex="-1"></a><span class="st">samples/AllAccounts_files/AllAccountsReport&quot;</span> <span class="ot">isNew=</span><span class="st">&quot;false&quot;</span>&gt;</span>
<span id="cb3-3"><a href="#cb3-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">label</span>&gt;All Accounts Jasper Report&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb3-4"><a href="#cb3-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">description</span>&gt;All Accounts Jasper Report&lt;/<span class="kw">description</span>&gt;</span>
<span id="cb3-5"><a href="#cb3-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">creationDate</span>&gt;1302268918000&lt;/<span class="kw">creationDate</span>&gt;</span>
<span id="cb3-6"><a href="#cb3-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_RESOURCE_TYPE&quot;</span>&gt;</span>
<span id="cb3-7"><a href="#cb3-7" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;com.jaspersoft.jasperserver.api.metadata.common.domain.FileResource</span>
<span id="cb3-8"><a href="#cb3-8" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb3-9"><a href="#cb3-9" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb3-10"><a href="#cb3-10" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_PARENT_FOLDER&quot;</span>&gt;</span>
<span id="cb3-11"><a href="#cb3-11" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;/reports/samples/AllAccounts_files&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb3-12"><a href="#cb3-12" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb3-13"><a href="#cb3-13" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_VERSION&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;2&lt;/<span class="kw">value</span>&gt;&lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb3-14"><a href="#cb3-14" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_IS_REFERENCE&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;false&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb3-15"><a href="#cb3-15" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb3-16"><a href="#cb3-16" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_HAS_DATA&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;true&lt;/<span class="kw">value</span>&gt;&lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb3-17"><a href="#cb3-17" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_ATTACHMENT_ID&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;attachment&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb3-18"><a href="#cb3-18" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb3-19"><a href="#cb3-19" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_RU_IS_MAIN_REPORT&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;true&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb3-20"><a href="#cb3-20" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb3-21"><a href="#cb3-21" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceDescriptor</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td><div class="sourceCode" id="cb4"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb4-1"><a href="#cb4-1" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceDescriptor</span> <span class="ot">name=</span><span class="st">&quot;AllAccounts_Res2&quot;</span> <span class="ot">wsType=</span><span class="st">&quot;img&quot;</span> <span class="ot">uriString=</span><span class="st">&quot;/reports/</span></span>
<span id="cb4-2"><a href="#cb4-2" aria-hidden="true" tabindex="-1"></a><span class="st">samples/AllAccounts_files/AllAccounts_Res2&quot;</span> <span class="ot">isNew=</span><span class="st">&quot;false&quot;</span>&gt;</span>
<span id="cb4-3"><a href="#cb4-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">label</span>&gt;AllAccounts_Res2&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb4-4"><a href="#cb4-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">description</span>&gt;AllAccounts_Res2&lt;/<span class="kw">description</span>&gt;</span>
<span id="cb4-5"><a href="#cb4-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">creationDate</span>&gt;1302268918000&lt;/<span class="kw">creationDate</span>&gt;</span>
<span id="cb4-6"><a href="#cb4-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_RESOURCE_TYPE&quot;</span>&gt;</span>
<span id="cb4-7"><a href="#cb4-7" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;com.jaspersoft.jasperserver.api.metadata.common.domain.FileResource</span>
<span id="cb4-8"><a href="#cb4-8" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb4-9"><a href="#cb4-9" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb4-10"><a href="#cb4-10" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_PARENT_FOLDER&quot;</span>&gt;</span>
<span id="cb4-11"><a href="#cb4-11" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;/reports/samples/AllAccounts_files&lt;/<span class="kw">value</span>&gt;&lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb4-12"><a href="#cb4-12" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_VERSION&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;0&lt;/<span class="kw">value</span>&gt;&lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb4-13"><a href="#cb4-13" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_IS_REFERENCE&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;false&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb4-14"><a href="#cb4-14" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb4-15"><a href="#cb4-15" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_HAS_DATA&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;true&lt;/<span class="kw">value</span>&gt;&lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb4-16"><a href="#cb4-16" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_ATTACHMENT_ID&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;attachment&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb4-17"><a href="#cb4-17" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb4-18"><a href="#cb4-18" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceDescriptor</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td><div class="sourceCode" id="cb5"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb5-1"><a href="#cb5-1" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceDescriptor</span> <span class="ot">name=</span><span class="st">&quot;AllAccounts_Res3&quot;</span> <span class="ot">wsType=</span><span class="st">&quot;img&quot;</span> <span class="ot">uriString=</span><span class="st">&quot;/reports/</span></span>
<span id="cb5-2"><a href="#cb5-2" aria-hidden="true" tabindex="-1"></a><span class="st">samples/AllAccounts_files/AllAccounts_Res3&quot;</span> <span class="ot">isNew=</span><span class="st">&quot;false&quot;</span>&gt;</span>
<span id="cb5-3"><a href="#cb5-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">label</span>&gt;AllAccounts_Res3&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb5-4"><a href="#cb5-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">description</span>&gt;AllAccounts_Res3&lt;/<span class="kw">description</span>&gt;</span>
<span id="cb5-5"><a href="#cb5-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">creationDate</span>&gt;1302268918000&lt;/<span class="kw">creationDate</span>&gt;</span>
<span id="cb5-6"><a href="#cb5-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_RESOURCE_TYPE&quot;</span>&gt;</span>
<span id="cb5-7"><a href="#cb5-7" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;com.jaspersoft.jasperserver.api.metadata.common.domain.FileResource</span>
<span id="cb5-8"><a href="#cb5-8" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">value</span>&gt;&lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb5-9"><a href="#cb5-9" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_PARENT_FOLDER&quot;</span>&gt;</span>
<span id="cb5-10"><a href="#cb5-10" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;/reports/samples/AllAccounts_files&lt;/<span class="kw">value</span>&gt;&lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb5-11"><a href="#cb5-11" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_VERSION&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;0&lt;/<span class="kw">value</span>&gt;&lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb5-12"><a href="#cb5-12" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_IS_REFERENCE&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;false&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb5-13"><a href="#cb5-13" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb5-14"><a href="#cb5-14" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_HAS_DATA&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;true&lt;/<span class="kw">value</span>&gt;&lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb5-15"><a href="#cb5-15" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_ATTACHMENT_ID&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;attachment&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb5-16"><a href="#cb5-16" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb5-17"><a href="#cb5-17" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceDescriptor</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td><div class="sourceCode" id="cb6"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb6-1"><a href="#cb6-1" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceDescriptor</span> <span class="ot">name=</span><span class="st">&quot;LogoLink&quot;</span> <span class="ot">wsType=</span><span class="st">&quot;reference&quot;</span> <span class="ot">uriString=</span><span class="st">&quot;/reports/</span></span>
<span id="cb6-2"><a href="#cb6-2" aria-hidden="true" tabindex="-1"></a><span class="st">                      samples/AllAccounts_files/LogoLink&quot;</span> <span class="ot">isNew=</span><span class="st">&quot;false&quot;</span>&gt;</span>
<span id="cb6-3"><a href="#cb6-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">label</span>&gt;LogoLink_label&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb6-4"><a href="#cb6-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">description</span>&gt;LogoLink description&lt;/<span class="kw">description</span>&gt;</span>
<span id="cb6-5"><a href="#cb6-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">creationDate</span>&gt;1302268918000&lt;/<span class="kw">creationDate</span>&gt;</span>
<span id="cb6-6"><a href="#cb6-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_RESOURCE_TYPE&quot;</span>&gt;</span>
<span id="cb6-7"><a href="#cb6-7" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;com.jaspersoft.jasperserver.api.metadata.common.domain.FileResource</span>
<span id="cb6-8"><a href="#cb6-8" aria-hidden="true" tabindex="-1"></a>      &lt;/<span class="kw">value</span>&gt;&lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb6-9"><a href="#cb6-9" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_PARENT_FOLDER&quot;</span>&gt;</span>
<span id="cb6-10"><a href="#cb6-10" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;/reports/samples/AllAccounts_files&lt;/<span class="kw">value</span>&gt;&lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb6-11"><a href="#cb6-11" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_VERSION&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;0&lt;/<span class="kw">value</span>&gt;&lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb6-12"><a href="#cb6-12" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_IS_REFERENCE&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;true&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb6-13"><a href="#cb6-13" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb6-14"><a href="#cb6-14" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_REFERENCE_URI&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;/images/JRLogo&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb6-15"><a href="#cb6-15" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td><div class="sourceCode" id="cb7"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb7-1"><a href="#cb7-1" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_HAS_DATA&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;true&lt;/<span class="kw">value</span>&gt;&lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb7-2"><a href="#cb7-2" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_ATTACHMENT_ID&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;attachment&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb7-3"><a href="#cb7-3" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb7-4"><a href="#cb7-4" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceDescriptor</span>&gt;</span>
<span id="cb7-5"><a href="#cb7-5" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">resourceDescriptor</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>
