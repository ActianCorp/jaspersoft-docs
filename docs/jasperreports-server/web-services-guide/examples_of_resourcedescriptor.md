---
title: Examples of resourceDescriptor
description: "The following resourceDescriptor sample contains a set of simple properties that describe a JDBC connection resource:"
---

# 1.0.1 Examples of resourceDescriptor

The following `resourceDescriptor` sample contains a set of simple properties that describe a JDBC connection resource:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">resourceDescriptor</span> <span class="ot">name=</span><span class="st">&quot;JServerJdbcDS&quot;</span> <span class="ot">wsType=</span><span class="st">&quot;jdbc&quot;</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>                    <span class="ot">uriString=</span><span class="st">&quot;/datasources/JServerJdbcDS&quot;</span> <span class="ot">isNew=</span><span class="st">&quot;false&quot;</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">label</span>&gt;JServer Jdbc data source&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">description</span>&gt;JServer Jdbc data source&lt;/<span class="kw">description</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_PARENT_FOLDER&quot;</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;/datasources&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_VERSION&quot;</span>&gt;</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;0&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_DATASOURCE_DRIVER_CLASS&quot;</span>&gt;</span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;com.mysql.jdbc.Driver&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_DATASOURCE_CONNECTION_URL&quot;</span>&gt;</span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;jdbc:mysql://localhost/test?autoReconnect=true&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_DATASOURCE_USERNAME&quot;</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;username&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_DATASOURCE_PASSWORD&quot;</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;password&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">resourceDescriptor</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

Some properties cannot be represented by a simple value. To accommodate more complicated properties, a resourceProperty can recursively contain other resourceProperties. This is the case for a List of Values type resource (used to define input controls for report parameters); the list values are contained in the `resourceProperty` named `PROP_LOV` and are represented by sub-resourceProperties. For example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">resourceDescriptor</span> <span class="ot">name=</span><span class="st">&quot;SampleLOV&quot;</span> <span class="ot">wsType=</span><span class="st">&quot;lov&quot;</span> <span class="ot">uriString=</span><span class="st">&quot;/datatypes/SampleLOV&quot;</span> <span class="ot">isNew=</span><span class="st">&quot;false&quot;</span>&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">label</span>&gt;Sample List of Values&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_RESOURCE_TYPE&quot;</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;com.jaspersoft.jasperserver.api.metadata.common.domain.ListOfValues</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_PARENT_FOLDER&quot;</span>&gt;</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;/datatypes&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_VERSION&quot;</span>&gt;</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;-1&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_HAS_DATA&quot;</span>&gt;</span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;false&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_IS_REFERENCE&quot;</span>&gt;</span>
<span id="cb1-17"><a href="#cb1-17" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;false&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-18"><a href="#cb1-18" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_LOV&quot;</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;US&quot;</span>&gt;</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;United States&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;CA&quot;</span>&gt;</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;Canada&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;      &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;IN&quot;</span>&gt;</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;India&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;IT&quot;</span>&gt;</span>
<span id="cb2-11"><a href="#cb2-11" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;Italy&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-12"><a href="#cb2-12" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb2-13"><a href="#cb2-13" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;DE&quot;</span>&gt;</span>
<span id="cb2-14"><a href="#cb2-14" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;Germany&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-15"><a href="#cb2-15" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb2-16"><a href="#cb2-16" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;RO&quot;</span>&gt;</span>
<span id="cb2-17"><a href="#cb2-17" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;Romania&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-18"><a href="#cb2-18" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb2-19"><a href="#cb2-19" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb2-20"><a href="#cb2-20" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">resourceDescriptor</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

This example defined a list of countries. Notice that, for each list item, the `resourceProperty` name represents the item value, and the `resourceProperty` value contains the item label.
