---
title: Get Operation
description: "The get operation is used to obtain information about a resource. In the case of file resources, such as images, fonts, JRXML files, and JAR files, the resource file is attached to the response..."
---

# 1.1 Get Operation

The `get` operation is used to obtain information about a resource. In the case of file resources, such as images, fonts, JRXML files, and JAR files, the resource file is attached to the response message.

This method’s behavior differs according to the type of object specified:

- Generally, a simple resource descriptor is returned.
- If you get a resource file, the file content is attached to the response; if you do not want the server to attach files to the response, set the request’s `NO_ATTACHMENT` argument to `true`.
- If you get a report unit, all the related resources are added as child resource descriptors to the report unit descriptor.
- To get an input control that is based on a query, you must set the IC_GET_QUERY_DATA argument to the valid URI of a datasource for the control, or you can handle the NONE condition as in the sample code java-webapp-sample.

If you set the datasource in the input control, that datasource is used to execute the query and populate the resource descriptor. This can be useful when the input control must be rendered (for example, on a web page) in order to capture a value to pass when executing a report.

- You can use parameters in the input control to select query values, including the datasource. See the examples starting on [](runreport_operation.md).

The following sample request gets a file resource:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">request</span> <span class="ot">operationName=</span><span class="st">&quot;get&quot;</span> <span class="ot">locale=</span><span class="st">&quot;en&quot;</span>&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceDescriptor</span> <span class="ot">name=</span><span class="st">&quot;JRLogo&quot;</span> <span class="ot">wsType=</span><span class="st">&quot;img&quot;</span> <span class="ot">uriString=</span><span class="st">&quot;/images/JRLogo&quot;</span> <span class="ot">isNew=</span><span class="st">&quot;false&quot;</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">label</span>&gt;JR logo&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">description</span>&gt;JR logo&lt;/<span class="kw">description</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceDescriptor</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">request</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

The service only uses the `uriString` to identify the resource to get and check for access permissions. This means that other information present in the resource description (such as resource properties, label, and description) are not actually used or required.

If a file is attached to the response, the returned resource descriptor has the `PROP_HAS_DATA` property set to `true`. By default, the attachments format is MIME. You can use DIME attachments by specifying the `USE_DIME_ATTACHMENTS` argument in the request.

A `get` call always returns a resource descriptor. If the specified resource is not found, or the specified user cannot access it, an error with code 2 is returned.

Java sample:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><pre class="text"><code>String imgUri = &quot;/images/JRLogo&quot;;
ResourceDescriptor rdis = new ResourceDescriptor();
rdis.setParentFolder(&quot;/images&quot;);
rdis.setUriString(imgUri);
ResourceDescriptor result = wsclient.get(rdis, null);</code></pre></td>
</tr>
</tbody>
</table>

PHP sample:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode bash"><code class="sourceCode bash"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="va">$result</span> = ws_get<span class="er">(</span><span class="va">$someInputControlUri</span><span class="ex">,</span> array<span class="er">(</span> <span class="ex">IC_GET_QUERY_DATA</span> =<span class="op">&gt;</span> </span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a><span class="va">$someDatasourceUri</span> <span class="kw">)</span> <span class="kw">);</span></span></code></pre></div></td>
</tr>
</tbody>
</table>

The resource descriptor of an input control that includes data obtained by setting the `IC_GET_QUERY_DATA` argument to `true` would be similar to the following XML:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">resourceDescriptor</span> <span class="ot">name=</span><span class="st">&quot;TEST_LIST&quot;</span> <span class="ot">wsType=</span><span class="st">&quot;inputControl&quot;</span> <span class="ot">uriString=</span>  <span class="st">&quot;/MyInputControls/TEST_LIST&quot;</span> <span class="ot">isNew=</span><span class="st">&quot;false&quot;</span>&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">label</span>&gt;My test list&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">description</span>&gt;My test list&lt;/<span class="kw">description</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_RESOURCE_TYPE&quot;</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;com.jaspersoft.jasperserver.api.metadata.common.domain.InputControl<span class="er">&lt;</span>/</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>      value&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_PARENT_FOLDER&quot;</span>&gt;</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;/MyInputControls&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_VERSION&quot;</span>&gt;</span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;6&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_HAS_DATA&quot;</span>&gt;</span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;false&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-17"><a href="#cb1-17" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_IS_REFERENCE&quot;</span>&gt;</span>
<span id="cb1-18"><a href="#cb1-18" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;false&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-19"><a href="#cb1-19" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-20"><a href="#cb1-20" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_INPUTCONTROL_IS_MANDATORY&quot;</span>&gt;</span>
<span id="cb1-21"><a href="#cb1-21" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;true&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-22"><a href="#cb1-22" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-23"><a href="#cb1-23" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_INPUTCONTROL_IS_READONLY&quot;</span>&gt;</span>
<span id="cb1-24"><a href="#cb1-24" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;false&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-25"><a href="#cb1-25" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-26"><a href="#cb1-26" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_INPUTCONTROL_TYPE&quot;</span>&gt;</span>
<span id="cb1-27"><a href="#cb1-27" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;7&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-28"><a href="#cb1-28" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_QUERY_VALUE_COLUMN&quot;</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;name&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_QUERY_VISIBLE_COLUMNS&quot;</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_QUERY_VISIBLE_COLUMN_NAME&quot;</span>&gt;</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;name&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_QUERY_VISIBLE_COLUMN_NAME&quot;</span>&gt;</span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;phone_office&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb2-11"><a href="#cb2-11" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_QUERY_VISIBLE_COLUMN_NAME&quot;</span>&gt;</span>
<span id="cb2-12"><a href="#cb2-12" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;billing_address_city&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-13"><a href="#cb2-13" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb2-14"><a href="#cb2-14" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb2-15"><a href="#cb2-15" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_QUERY_DATA&quot;</span>&gt;</span>
<span id="cb2-16"><a href="#cb2-16" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_QUERY_DATA_ROW&quot;</span>&gt;</span>
<span id="cb2-17"><a href="#cb2-17" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;A <span class="dv">&amp;amp;</span> L Powers Engineering, Inc&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-18"><a href="#cb2-18" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_QUERY_DATA_ROW_COLUMN&quot;</span>&gt;</span>
<span id="cb2-19"><a href="#cb2-19" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">value</span>&gt;A <span class="dv">&amp;amp;</span> L Powers Engineering, Inc&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-20"><a href="#cb2-20" aria-hidden="true" tabindex="-1"></a>      &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb2-21"><a href="#cb2-21" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_QUERY_DATA_ROW_COLUMN&quot;</span>&gt;</span>
<span id="cb2-22"><a href="#cb2-22" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">value</span>&gt;738-555-3283&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-23"><a href="#cb2-23" aria-hidden="true" tabindex="-1"></a>      &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb2-24"><a href="#cb2-24" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_QUERY_DATA_ROW_COLUMN&quot;</span>&gt;</span>
<span id="cb2-25"><a href="#cb2-25" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">value</span>&gt;Haney&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-26"><a href="#cb2-26" aria-hidden="true" tabindex="-1"></a>      &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb2-27"><a href="#cb2-27" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb2-28"><a href="#cb2-28" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_QUERY_DATA_ROW&quot;</span>&gt;</span>
<span id="cb2-29"><a href="#cb2-29" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;A <span class="dv">&amp;amp;</span> U Jaramillo Telecommunications, Inc&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-30"><a href="#cb2-30" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_QUERY_DATA_ROW_COLUMN&quot;</span>&gt;</span>
<span id="cb2-31"><a href="#cb2-31" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">value</span>&gt;A <span class="dv">&amp;amp;</span> U Jaramillo Telecommunications, Inc&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-32"><a href="#cb2-32" aria-hidden="true" tabindex="-1"></a>      &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb2-33"><a href="#cb2-33" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_QUERY_DATA_ROW_COLUMN&quot;</span>&gt;</span>
<span id="cb2-34"><a href="#cb2-34" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">value</span>&gt;564-555-6913&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-35"><a href="#cb2-35" aria-hidden="true" tabindex="-1"></a>      &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb2-36"><a href="#cb2-36" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_QUERY_DATA_ROW_COLUMN&quot;</span>&gt;</span>
<span id="cb2-37"><a href="#cb2-37" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">value</span>&gt;Walla Walla&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-38"><a href="#cb2-38" aria-hidden="true" tabindex="-1"></a>      &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb2-39"><a href="#cb2-39" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb2-40"><a href="#cb2-40" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_QUERY_DATA_ROW&quot;</span>&gt;</span>
<span id="cb2-41"><a href="#cb2-41" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;A <span class="dv">&amp;amp;</span> U Stalker Telecommunications, Inc&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-42"><a href="#cb2-42" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_QUERY_DATA_ROW_COLUMN&quot;</span>&gt;</span>
<span id="cb2-43"><a href="#cb2-43" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">value</span>&gt;A <span class="dv">&amp;amp;</span> U Stalker Telecommunications, Inc&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-44"><a href="#cb2-44" aria-hidden="true" tabindex="-1"></a>      &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb2-45"><a href="#cb2-45" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_QUERY_DATA_ROW_COLUMN&quot;</span>&gt;</span>
<span id="cb2-46"><a href="#cb2-46" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">value</span>&gt;323-555-1226&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-47"><a href="#cb2-47" aria-hidden="true" tabindex="-1"></a>      &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb2-48"><a href="#cb2-48" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_QUERY_DATA_ROW_COLUMN&quot;</span>&gt;</span>
<span id="cb2-49"><a href="#cb2-49" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">value</span>&gt;Mill Valley&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-50"><a href="#cb2-50" aria-hidden="true" tabindex="-1"></a>      &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb2-51"><a href="#cb2-51" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td><div class="sourceCode" id="cb3"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_QUERY_DATA_ROW&quot;</span>&gt;</span>
<span id="cb3-2"><a href="#cb3-2" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;A <span class="dv">&amp;amp;</span> X Caravello Engineering, Inc&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb3-3"><a href="#cb3-3" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_QUERY_DATA_ROW_COLUMN&quot;</span>&gt;</span>
<span id="cb3-4"><a href="#cb3-4" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">value</span>&gt;A <span class="dv">&amp;amp;</span> X Caravello Engineering, Inc&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb3-5"><a href="#cb3-5" aria-hidden="true" tabindex="-1"></a>      &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb3-6"><a href="#cb3-6" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_QUERY_DATA_ROW_COLUMN&quot;</span>&gt;</span>
<span id="cb3-7"><a href="#cb3-7" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">value</span>&gt;958-555-5890&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb3-8"><a href="#cb3-8" aria-hidden="true" tabindex="-1"></a>      &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb3-9"><a href="#cb3-9" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_QUERY_DATA_ROW_COLUMN&quot;</span>&gt;</span>
<span id="cb3-10"><a href="#cb3-10" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">value</span>&gt;Tlaxiaco&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb3-11"><a href="#cb3-11" aria-hidden="true" tabindex="-1"></a>      &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb3-12"><a href="#cb3-12" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb3-13"><a href="#cb3-13" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb3-14"><a href="#cb3-14" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceDescriptor</span> <span class="ot">name=</span><span class="st">&quot;query&quot;</span> <span class="ot">wsType=</span><span class="st">&quot;query&quot;</span> <span class="ot">uriString=</span><span class="st">&quot;/MyInputControls/</span></span>
<span id="cb3-15"><a href="#cb3-15" aria-hidden="true" tabindex="-1"></a><span class="st">    TEST_LIST_files/query&quot;</span> <span class="ot">isNew=</span><span class="st">&quot;false&quot;</span>&gt;</span>
<span id="cb3-16"><a href="#cb3-16" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">label</span>&gt;query&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb3-17"><a href="#cb3-17" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">description</span>&gt;query&lt;/<span class="kw">description</span>&gt;</span>
<span id="cb3-18"><a href="#cb3-18" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_RESOURCE_TYPE&quot;</span>&gt;</span>
<span id="cb3-19"><a href="#cb3-19" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;com.jaspersoft.jasperserver.api.metadata.common.domain.Query&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb3-20"><a href="#cb3-20" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb3-21"><a href="#cb3-21" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_PARENT_FOLDER&quot;</span>&gt;</span>
<span id="cb3-22"><a href="#cb3-22" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;/MyInputControls/TEST_LIST_files&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb3-23"><a href="#cb3-23" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb3-24"><a href="#cb3-24" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_VERSION&quot;</span>&gt;</span>
<span id="cb3-25"><a href="#cb3-25" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;1&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb3-26"><a href="#cb3-26" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb3-27"><a href="#cb3-27" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_HAS_DATA&quot;</span>&gt;</span>
<span id="cb3-28"><a href="#cb3-28" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;false&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb3-29"><a href="#cb3-29" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb3-30"><a href="#cb3-30" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_IS_REFERENCE&quot;</span>&gt;</span>
<span id="cb3-31"><a href="#cb3-31" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;false&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb3-32"><a href="#cb3-32" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb3-33"><a href="#cb3-33" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_QUERY&quot;</span>&gt;</span>
<span id="cb3-34"><a href="#cb3-34" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;SELECT name, phone_office, billing_address_city FROM accounts order by </span>
<span id="cb3-35"><a href="#cb3-35" aria-hidden="true" tabindex="-1"></a>      name&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb3-36"><a href="#cb3-36" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb3-37"><a href="#cb3-37" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_QUERY_LANGUAGE&quot;</span>&gt;</span>
<span id="cb3-38"><a href="#cb3-38" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;sql&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb3-39"><a href="#cb3-39" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb3-40"><a href="#cb3-40" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceDescriptor</span> <span class="ot">name=</span><span class="st">&quot;&quot;</span> <span class="ot">wsType=</span><span class="st">&quot;datasource&quot;</span> <span class="ot">uriString=</span><span class="st">&quot;&quot;</span> <span class="ot">isNew=</span><span class="st">&quot;false&quot;</span>&gt;</span>
<span id="cb3-41"><a href="#cb3-41" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">label</span>&gt;null&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb3-42"><a href="#cb3-42" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_REFERENCE_URI&quot;</span>&gt;</span>
<span id="cb3-43"><a href="#cb3-43" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">value</span>&gt;/datasources/JServerJdbcDS&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb3-44"><a href="#cb3-44" aria-hidden="true" tabindex="-1"></a>      &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb3-45"><a href="#cb3-45" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_IS_REFERENCE&quot;</span>&gt;</span>
<span id="cb3-46"><a href="#cb3-46" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">value</span>&gt;true&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb3-47"><a href="#cb3-47" aria-hidden="true" tabindex="-1"></a>      &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb3-48"><a href="#cb3-48" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceDescriptor</span>&gt;</span>
<span id="cb3-49"><a href="#cb3-49" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceDescriptor</span>&gt;</span>
<span id="cb3-50"><a href="#cb3-50" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">resourceDescriptor</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

The query result is a set of rows that represents the full set of possible values for the input control. For each row, the repository web service returns the value that `runReport` expects for that particular option in the input control. Each row also includes the column values that should be displayed in the input control when prompting users.

![7 2](assets/images/7_2.jpg)

*Figure 1-1 Query Results*

This figure shows input controls based on queries, as they are rendered by the iReport Designer plugin for JasperReports Server. When the web services run report units, the rendering of input controls is left to the client application. The best way to proceed is:

- Get the report unit.
- Check for query-based input controls by looking at the `PROP_INPUTCONTROL_TYPE` resource property or each child resource descriptor where `wsType` is equal to `inputControl`.
- Get each query-based input control by setting the `IC_GET_QUERY_DATA` argument to true.
- Render the input controls (if used in the report unit), being mindful of the input control properties (such as read only and mandatory).
- Call the runReport service and pass the user-selected values.

The rows are stored in the `PROP_QUERY_DATA` resource property: for each row, a child resource property named `PROP_QUERY_DATA_ROW` contains the value and a set of children that contain the column values; these last resource properties are named `PROP_QUERY_DATA_ROW_COLUMN`.

The following schema may elucidate the whole data structure:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><pre class="text"><code>PROP_QUERY_DATA
  (
  PROP_QUERY_DATA_ROW, value
    (
    PROP_QUERY_DATA_ROW_COLUMN, value
    PROP_QUERY_DATA_ROW_COLUMN, value
    ...
    )
  PROP_QUERY_DATA_ROW, value
    (
    PROP_QUERY_DATA_ROW_COLUMN, value
    PROP_QUERY_DATA_ROW_COLUMN, value
    ...
    )</code></pre></td>
</tr>
<tr>
<td><pre class="text"><code>  PROP_QUERY_DATA_ROW, value
    (
    PROP_QUERY_DATA_ROW_COLUMN, value
    PROP_QUERY_DATA_ROW_COLUMN, value
    ...
    )
  )</code></pre></td>
</tr>
</tbody>
</table>

In Java, to simplify response processing, the `resourceDescriptor` class provides the `getQueryData()` method that returns a list of `InputControlQueryDataRow`, which is a convenient class containing all the row information (row and column values).
