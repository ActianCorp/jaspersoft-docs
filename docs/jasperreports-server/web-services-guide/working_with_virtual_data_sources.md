---
title: Working with Virtual Data Sources
description: "Data sources define a connection to a database or other source of data for running reports. Data sources are resources in the repository that can be created, modified, and deleted with the repository..."
---

# 1.1 Working with Virtual Data Sources

Data sources define a connection to a database or other source of data for running reports. Data sources are resources in the repository that can be created, modified, and deleted with the repository service.

As with all descriptors, the descriptors for data sources contain properties and values that define the data source. Different types of data sources have different properties, but all are self-explanatory. For example, the following call returns the descriptor for a virtual data source in the sample data:

GET http://localhost:8080/jasperserver/rest/resource/datasources/SugarFoodmartVDS

The resource descriptor is shown below. The data sources that make up the virtual data source are given as children descriptors of type generic datasource. Each child descriptor has an ID within the virtual data source (PROP_DATASOURCE_SUB_DS \_ID) and a repository URI (PROP_REFERENCE_URI):

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">resourceDescriptor</span> <span class="ot">name=</span><span class="st">&quot;SugarFoodmartVDS&quot;</span> <span class="ot">wsType=</span><span class="st">&quot;virtual&quot;</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="ot">uriString=</span><span class="st">&quot;/datasources/SugarFoodmartVDS&quot;</span> <span class="ot">isNew=</span><span class="st">&quot;false&quot;</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">label</span>&gt;SugarCRM-Foodmart Virtual Data Source&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">description</span>&gt;Virtual Data Source Combining SugarCRM and Foodmart&lt;/<span class="kw">description</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">creationDate</span>&gt;1366267873303&lt;/<span class="kw">creationDate</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_RESOURCE_TYPE&quot;</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;com.jaspersoft.jasperserver.api.metadata.jasperreports.domain.</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>           VirtualReportDataSource&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_PARENT_FOLDER&quot;</span>&gt;</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;/datasources&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_VERSION&quot;</span>&gt;</span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;0&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb2-11"><a href="#cb2-11" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_SECURITY_PERMISSION_MASK&quot;</span>&gt;</span>
<span id="cb2-12"><a href="#cb2-12" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;33&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-13"><a href="#cb2-13" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb2-14"><a href="#cb2-14" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceDescriptor</span> <span class="ot">wsType=</span><span class="st">&quot;datasource&quot;</span> <span class="ot">isNew=</span><span class="st">&quot;false&quot;</span>&gt;</span>
<span id="cb2-15"><a href="#cb2-15" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_REFERENCE_URI&quot;</span>&gt;</span>
<span id="cb2-16"><a href="#cb2-16" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;/analysis/datasources/SugarCRMDataSourceJNDI&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-17"><a href="#cb2-17" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb2-18"><a href="#cb2-18" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_IS_REFERENCE&quot;</span>&gt;</span>
<span id="cb2-19"><a href="#cb2-19" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;true&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-20"><a href="#cb2-20" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb2-21"><a href="#cb2-21" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_DATASOURCE_SUB_DS_ID&quot;</span>&gt;</span>
<span id="cb2-22"><a href="#cb2-22" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;SugarCRMDataSource&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-23"><a href="#cb2-23" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb2-24"><a href="#cb2-24" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceDescriptor</span>&gt;</span>
<span id="cb2-25"><a href="#cb2-25" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceDescriptor</span> <span class="ot">wsType=</span><span class="st">&quot;datasource&quot;</span> <span class="ot">isNew=</span><span class="st">&quot;false&quot;</span>&gt;</span>
<span id="cb2-26"><a href="#cb2-26" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_REFERENCE_URI&quot;</span>&gt;</span>
<span id="cb2-27"><a href="#cb2-27" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;/analysis/datasources/FoodmartDataSourceJNDI&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-28"><a href="#cb2-28" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb2-29"><a href="#cb2-29" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_IS_REFERENCE&quot;</span>&gt;</span>
<span id="cb2-30"><a href="#cb2-30" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;true&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-31"><a href="#cb2-31" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb2-32"><a href="#cb2-32" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_DATASOURCE_SUB_DS_ID&quot;</span>&gt;</span>
<span id="cb2-33"><a href="#cb2-33" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;FoodmartDataSource&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-34"><a href="#cb2-34" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb2-35"><a href="#cb2-35" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceDescriptor</span>&gt;</span>
<span id="cb2-36"><a href="#cb2-36" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">resourceDescriptor</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

If you wanted more information about the child data sources, use the resource service again to request their descriptors, for example:

GET http://localhost:8080/jasperserver/rest/resource/analysis/datasources/FoodmartDataSourceJNDI
