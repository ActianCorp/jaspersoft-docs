---
title: Working with Domains
description: "The repository services can also be used to read and write Domains. Like JasperReport resources, Domains are complex resources that contain other files. The files that make up a Domain are its Domain..."
---

# 1.1 Working with Domains

The repository services can also be used to read and write Domains. Like JasperReport resources, Domains are complex resources that contain other files. The files that make up a Domain are its Domain schema, its optional security files, and its optional language bundles. You can find the name and location of these files by requesting the Domain itself. For example, the following request shows the contents of the Supermart Domain:

GET http://localhost:8080/jasperserver-pro/rest/resource/Domains/supermartDomain

!!! note

    All repository URIs sent and received are relative the organization of the user ID that performs the REST operation. The URIs in this section assume the user is an organization admin such as jasperadmin.

Looking carefully through the resulting descriptor, we find the relevant information:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">resourceDescriptor</span> <span class="ot">name=</span><span class="st">&quot;supermartDomain&quot;</span> <span class="ot">wsType=</span><span class="st">&quot;domain&quot;</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  <span class="ot">uriString=</span><span class="st">&quot;/Domains/supermartDomain&quot;</span> <span class="ot">isNew=</span><span class="st">&quot;false&quot;</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">label</span>&gt;Supermart Domain&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">description</span>&gt;Comprehensive example of Domain (pre-joined table sets for complex reporting, custom query based dataset, column and row security, I18n bundles)&lt;/<span class="kw">description</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_RESOURCE_TYPE&quot;</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;com.jaspersoft.commons.semantic.datasource.SemanticLayerDataSource</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>  ...</span></code></pre></div></td>
</tr>
<tr>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceDescriptor</span> <span class="ot">name=</span><span class="st">&quot;supermartDomain_schema&quot;</span> <span class="ot">wsType=</span><span class="st">&quot;xml&quot;</span></span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    <span class="ot">uriString=</span><span class="st">&quot;/Domains/supermartDomain_files/supermartDomain_schema&quot;</span> <span class="ot">isNew=</span><span class="st">&quot;false&quot;</span>&gt;</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">label</span>&gt;supermartDomain_schema&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">description</span>&gt;supermartDomain_schema&lt;/<span class="kw">description</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_RESOURCE_TYPE&quot;</span>&gt;</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;com.jaspersoft.jasperserver.api.metadata.common.domain.FileResource</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>    ...</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceDescriptor</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td><div class="sourceCode" id="cb3"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceDescriptor</span> <span class="ot">name=</span><span class="st">&quot;supermart_domain.properties&quot;</span> <span class="ot">wsType=</span><span class="st">&quot;prop&quot;</span></span>
<span id="cb3-2"><a href="#cb3-2" aria-hidden="true" tabindex="-1"></a>    <span class="ot">uriString=</span><span class="st">&quot;/Domains/supermartDomain_files/supermart_domain.properties&quot;</span></span>
<span id="cb3-3"><a href="#cb3-3" aria-hidden="true" tabindex="-1"></a>    <span class="ot">isNew=</span><span class="st">&quot;false&quot;</span>&gt;</span>
<span id="cb3-4"><a href="#cb3-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">label</span>&gt;supermart_domain.properties&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb3-5"><a href="#cb3-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_RESOURCE_TYPE&quot;</span>&gt;</span>
<span id="cb3-6"><a href="#cb3-6" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;com.jaspersoft.jasperserver.api.metadata.common.domain.FileResource</span>
<span id="cb3-7"><a href="#cb3-7" aria-hidden="true" tabindex="-1"></a>    ...</span>
<span id="cb3-8"><a href="#cb3-8" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceDescriptor</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td><div class="sourceCode" id="cb4"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb4-1"><a href="#cb4-1" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceDescriptor</span> <span class="ot">name=</span><span class="st">&quot;supermart_domain_en_US.properties&quot;</span> <span class="ot">wsType=</span><span class="st">&quot;prop&quot;</span></span>
<span id="cb4-2"><a href="#cb4-2" aria-hidden="true" tabindex="-1"></a>    <span class="ot">uriString=</span><span class="st">&quot;/Domains/supermartDomain_files/supermart_domain_en_US.properties&quot;</span> </span>
<span id="cb4-3"><a href="#cb4-3" aria-hidden="true" tabindex="-1"></a>    <span class="ot">isNew=</span><span class="st">&quot;false&quot;</span>&gt;</span>
<span id="cb4-4"><a href="#cb4-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">label</span>&gt;supermart_domain_en_US.properties&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb4-5"><a href="#cb4-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_RESOURCE_TYPE&quot;</span>&gt;</span>
<span id="cb4-6"><a href="#cb4-6" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;com.jaspersoft.jasperserver.api.metadata.common.domain.FileResource</span>
<span id="cb4-7"><a href="#cb4-7" aria-hidden="true" tabindex="-1"></a>    ...</span>
<span id="cb4-8"><a href="#cb4-8" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceDescriptor</span>&gt;</span>
<span id="cb4-9"><a href="#cb4-9" aria-hidden="true" tabindex="-1"></a>  ...</span></code></pre></div></td>
</tr>
<tr>
<td><div class="sourceCode" id="cb5"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb5-1"><a href="#cb5-1" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceDescriptor</span> <span class="ot">name=</span><span class="st">&quot;supermartDomain_domain_security&quot;</span> <span class="ot">wsType=</span><span class="st">&quot;xml&quot;</span></span>
<span id="cb5-2"><a href="#cb5-2" aria-hidden="true" tabindex="-1"></a>    <span class="ot">uriString=</span><span class="st">&quot;/Domains/supermartDomain_files/supermartDomain_domain_security&quot;</span></span>
<span id="cb5-3"><a href="#cb5-3" aria-hidden="true" tabindex="-1"></a>    <span class="ot">isNew=</span><span class="st">&quot;false&quot;</span>&gt;</span>
<span id="cb5-4"><a href="#cb5-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">label</span>&gt;supermartDomain_domain_security&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb5-5"><a href="#cb5-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">description</span>&gt;supermartDomain_domain_security&lt;/<span class="kw">description</span>&gt;</span>
<span id="cb5-6"><a href="#cb5-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_RESOURCE_TYPE&quot;</span>&gt;</span>
<span id="cb5-7"><a href="#cb5-7" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;com.jaspersoft.jasperserver.api.metadata.common.domain.FileResource</span>
<span id="cb5-8"><a href="#cb5-8" aria-hidden="true" tabindex="-1"></a>    ...</span>
<span id="cb5-9"><a href="#cb5-9" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_SECURITY_BUNDLE&quot;</span>&gt;</span>
<span id="cb5-10"><a href="#cb5-10" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;true&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb5-11"><a href="#cb5-11" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb5-12"><a href="#cb5-12" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceDescriptor</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td><div class="sourceCode" id="cb6"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb6-1"><a href="#cb6-1" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceDescriptor</span> <span class="ot">name=</span><span class="st">&quot;dsFoodMart&quot;</span> <span class="ot">wsType=</span><span class="st">&quot;reference&quot;</span> <span class="ot">referenceType=</span><span class="st">&quot;jndi&quot;</span></span>
<span id="cb6-2"><a href="#cb6-2" aria-hidden="true" tabindex="-1"></a>    <span class="ot">uriString=</span><span class="st">&quot;/analysis/datasources/FoodmartDataSourceJNDI&quot;</span> <span class="ot">isNew=</span><span class="st">&quot;false&quot;</span>&gt;</span>
<span id="cb6-3"><a href="#cb6-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_REFERENCE_URI&quot;</span>&gt;</span>
<span id="cb6-4"><a href="#cb6-4" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;/analysis/datasources/FoodmartDataSourceJNDI&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb6-5"><a href="#cb6-5" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb6-6"><a href="#cb6-6" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceDescriptor</span>&gt;</span>
<span id="cb6-7"><a href="#cb6-7" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">resourceDescriptor</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

The files contained in this Domain are:

-   /Domains/supermartDomain_files/supermartDomain_schema
-   /Domains/supermartDomain_files/supermartDomain_domain_security
-   /Domains/supermartDomain_files/supermart_domain.properties
-   /Domains/supermartDomain_files/supermart_domain_en_US.properties
-   `...`

To download these files, use the same syntax as for downloading file resource contents:

GET http://localhost:8080/jasperserver-pro/rest/resource/Domains/supermartDomain_files/<br>
supermartDomain_schema?fileData=true

Domain schema files, security files, and language bundles have a special syntax described in the JasperReports® Server User Guide. To process these files automatically, you would need to write your own parser.

If you have valid schema files, security files, and language bundles, you can also create Domain resources in the repository using the PUT method described in section [Creating a Resource](creating_a_resource.md). The following procedure outlines the step required to create a Domain resource programmatically through the REST API:

1.  Create the resource descriptor for the Domain using the descriptor shown above as an example. Make sure the files are referenced correctly in the descriptor.
2.  Create the PUT request to the resource service using the resource descriptor created in the previous step.
3.  Add the files to the request as multi-part request. For example use the class `org.apache.http.entity.mime. MultipartEntity` to build a multi-part request. Add each file as a separate part to the request.
4.  Send the multi-part request to JasperReports Server.
5.  Process the response to verify the request was successful.
