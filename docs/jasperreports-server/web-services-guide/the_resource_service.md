---
title: The resource Service
description: "The resource service supports several HTTP methods to view, download, create, and modify resources in the repository."
---

# 1.1 The resource Service

The resource service supports several HTTP methods to view, download, create, and modify resources in the repository.

GET is used to show the information about a specific resource. Getting a resource can serve several purposes:

- In the case of JasperReports, also known as report units, this service returns the structure of the JasperReport, including resourceDescriptors for any linked resources.
- For resources that contain files, specifying the `fileData=true` argument downloads the file content.
- Specifying a query-based input control with arguments for running the query returns the dynamic values for the control.

!!! note

    A new service is also available to interact with report options. See [“The v2/options Service” on page 1](the_v2_options_service.md).

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest/resource</span>/path/to/resource/?&lt;arguments&gt;</p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p>fileData?</p></td>
<td><p>Boolean</p></td>
<td colspan="2"><p>For resources that contain a file, set this argument to true to download the file. When not specified, this argument is false by default and the method returns the description of the resource.</p></td>
</tr>
<tr>
<td><p>IC_GET_QUERY_DATA?</p></td>
<td><p>String</p></td>
<td colspan="2"><p>Used to get the items to fill an input control which subtend a query resource. The value of this parameter must be the URI of the data source to use to execute the query. Set the null string to use the default data source.</p></td>
</tr>
<tr>
<td><p>P_&lt;param name&gt;?</p></td>
<td><p>String</p></td>
<td colspan="2" rowspan="2"><p>If the IC_GET_QUERY_DATA is specified, one or more parameters can be specified to be used in the query:</p>
<ul>
<li>Use the "P_" prefix for single values.</li>
<li>Use the "PL_" prefix for list of values.</li>
</ul></td>
</tr>
<tr>
<td><p>PL_&lt;param name&gt;?</p></td>
<td><p>String</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The body is either:</p>
<ul>
<li>XML giving the resourceDescriptors that make up the resource, including nested descriptors.</li>
<li>The native content of the specified file.</li>
</ul></td>
<td><p>404 Not Found – When the specified resource URI is not found in the repository</p></td>
</tr>
</tbody>
</table>

The GET method returns the structure and definition of resources in the repository, and using that information can be used to download any files attached to the resources. Resources are defined through `resourceDescriptor` tags in XML.

The following example shows the resource descriptor of a folder:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">resourceDescriptor</span> <span class="ot">name=</span><span class="st">&quot;datasources&quot;</span> <span class="ot">wsType=</span><span class="st">&quot;folder&quot;</span> <span class="ot">uriString=</span><span class="st">&quot;/datasources&quot;</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>                    <span class="ot">isNew=</span><span class="st">&quot;false&quot;</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">label</span>&gt;Data Sources&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">description</span>&gt;Data Sources used by reports&lt;/<span class="kw">description</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">creationDate</span>&gt;1317838605320&lt;/<span class="kw">creationDate</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_RESOURCE_TYPE&quot;</span>&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;com.jaspersoft.jasperserver.api.metadata.common.domain.Folder&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_PARENT_FOLDER&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;/&lt;/<span class="kw">value</span>&gt;&lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_VERSION&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;0&lt;/<span class="kw">value</span>&gt;&lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_HAS_DATA&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;false&lt;/<span class="kw">value</span>&gt;&lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">resourceDescriptor</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

The following example shows the resource descriptor of a data source. The various `resourceProperty` tags define the properties of the data source, specific to the JNDI type:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">resourceDescriptor</span> <span class="ot">name=</span><span class="st">&quot;SugarCRMDataSourceJNDI&quot;</span> <span class="ot">wsType=</span><span class="st">&quot;jndi&quot;</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  <span class="ot">uriString=</span><span class="st">&quot;/analysis/datasources/SugarCRMDataSourceJNDI&quot;</span> <span class="ot">isNew=</span><span class="st">&quot;false&quot;</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">label</span>&gt;SugarCRM Data Source JNDI&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">description</span>&gt;SugarCRM Data Source JNDI&lt;/<span class="kw">description</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">creationDate</span>&gt;1318380229907&lt;/<span class="kw">creationDate</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_RESOURCE_TYPE&quot;</span>&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;com.jaspersoft.jasperserver.api.metadata.jasperreports.domain.</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>           JndiJdbcReportDataSource&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_PARENT_FOLDER&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;/analysis/datasources&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_VERSION&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;0&lt;/<span class="kw">value</span>&gt;&lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_DATASOURCE_JNDI_NAME&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;jdbc/sugarcrm&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">resourceDescriptor</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

The following example shows the resource descriptor of a query resource, with properties for the query string and query language:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">resourceDescriptor</span> <span class="ot">name=</span><span class="st">&quot;CustomerCityQuery&quot;</span> <span class="ot">wsType=</span><span class="st">&quot;query&quot;</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  <span class="ot">uriString=</span><span class="st">&quot;/datatypes/CustomerCityQuery&quot;</span> <span class="ot">isNew=</span><span class="st">&quot;false&quot;</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">label</span>&gt;Customer City Query&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">description</span>&gt;Retrieves names of all customers&#39; home cities&lt;/<span class="kw">description</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">creationDate</span>&gt;1318380317602&lt;/<span class="kw">creationDate</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_RESOURCE_TYPE&quot;</span>&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;com.jaspersoft.jasperserver.api.metadata.common.domain.Query&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;&lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_PARENT_FOLDER&quot;</span>&gt;</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;/JUNIT_NEW_FOLDER&lt;/<span class="kw">value</span>&gt;&lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_VERSION&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;0&lt;/<span class="kw">value</span>&gt;&lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_HAS_DATA&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;false&lt;/<span class="kw">value</span>&gt;&lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_IS_REFERENCE&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;false&lt;/<span class="kw">value</span>&gt;&lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_QUERY&quot;</span>&gt;</span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;select distinct customer.city from customer&lt;/<span class="kw">value</span>&gt;&lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_QUERY_LANGUAGE&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;sql&lt;/<span class="kw">value</span>&gt;&lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">resourceDescriptor</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>
