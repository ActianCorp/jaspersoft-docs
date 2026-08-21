---
title: Requesting the Values of a Query-Based Input Control
description: "A newer service is available to interact with input controls, including query-based input controls. See section The v2/inputControls Service."
---

# 1.0.1 Requesting the Values of a Query-Based Input Control

!!! note

    A newer service is available to interact with input controls, including query-based input controls. See section [The v2/inputControls Service](the_v2_inputcontrols_service.md).

The following sample request specifies a resource that is a query-based input control, and by specifying the appropriate parameters, we can receive the current values. In this case, one of the parameters to the query is a list of two values, USA and Mexico:

GET http://localhost:8080/jasperserver/rest/resource/reports/samples/Cascading_multi_select_report_files/<br>
Cascading_state_multi_select?IC_GET_QUERY_DATA=/datasources/JServerJNDIDS&<br>
PL_Country_multi_select=USA&PL_Country_multi_select=Mexico

The following response shows the resource descriptor for the requested input control, and it contains extra properties that give all the values that are the results of the query. You can see they are from Mexico and USA. The resource descriptor also includes the nested descriptor for the query that is part of the input control.

!!! note

    If a selection-type input control has a null value, it is given as `~NULL~`. If no selection is made, its value is given as `~NOTHING~`.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">resourceDescriptor</span> <span class="ot">name=</span><span class="st">&quot;Cascading_state_multi_select&quot;</span> <span class="ot">wsType=</span><span class="st">&quot;inputControl&quot;</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>                    <span class="ot">uriString=</span><span class="st">&quot;/reports/samples/Cascading_multi_select_report_files/</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a><span class="st">                    Cascading_state_multi_select&quot;</span> <span class="ot">isNew=</span><span class="st">&quot;false&quot;</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">label</span>&gt;Cascading state multi select control&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">description</span>&gt;Cascading state multi select control&lt;/<span class="kw">description</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">creationDate</span>&gt;1302268918000&lt;/<span class="kw">creationDate</span>&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_RESOURCE_TYPE&quot;</span>&gt;</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;com.jaspersoft.jasperserver.api.metadata.common.domain.InputControl</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_PARENT_FOLDER&quot;</span>&gt;</span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;/reports/samples/Cascading_multi_select_report_files&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_VERSION&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;0&lt;/<span class="kw">value</span>&gt;&lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_HAS_DATA&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;false&lt;/<span class="kw">value</span>&gt;&lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_IS_REFERENCE&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;false&lt;/<span class="kw">value</span>&gt;&lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-17"><a href="#cb1-17" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_INPUTCONTROL_IS_MANDATORY&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;true&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-18"><a href="#cb1-18" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-19"><a href="#cb1-19" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_INPUTCONTROL_IS_READONLY&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;false&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-20"><a href="#cb1-20" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-21"><a href="#cb1-21" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_INPUTCONTROL_IS_VISIBLE&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;true&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-22"><a href="#cb1-22" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-23"><a href="#cb1-23" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_INPUTCONTROL_TYPE&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;7&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-24"><a href="#cb1-24" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-25"><a href="#cb1-25" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_QUERY_VALUE_COLUMN&quot;</span>&gt;</span>
<span id="cb1-26"><a href="#cb1-26" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;billing_address_state&lt;/<span class="kw">value</span>&gt;&lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-27"><a href="#cb1-27" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_QUERY_VISIBLE_COLUMNS&quot;</span>&gt;</span>
<span id="cb1-28"><a href="#cb1-28" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_QUERY_VISIBLE_COLUMN_NAME&quot;</span>&gt;</span>
<span id="cb1-29"><a href="#cb1-29" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;billing_address_country&lt;/<span class="kw">value</span>&gt;&lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-30"><a href="#cb1-30" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_QUERY_VISIBLE_COLUMN_NAME&quot;</span>&gt;</span>
<span id="cb1-31"><a href="#cb1-31" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;billing_address_state&lt;/<span class="kw">value</span>&gt;&lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-32"><a href="#cb1-32" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-33"><a href="#cb1-33" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_QUERY_DATA&quot;</span>&gt;</span>
<span id="cb1-34"><a href="#cb1-34" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_QUERY_DATA_ROW&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;DF&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-35"><a href="#cb1-35" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_QUERY_DATA_ROW_COLUMN&quot;</span>&gt;</span>
<span id="cb1-36"><a href="#cb1-36" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">value</span>&gt;Mexico&lt;/<span class="kw">value</span>&gt;&lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-37"><a href="#cb1-37" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_QUERY_DATA_ROW_COLUMN&quot;</span>&gt;</span>
<span id="cb1-38"><a href="#cb1-38" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">value</span>&gt;DF&lt;/<span class="kw">value</span>&gt;&lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-39"><a href="#cb1-39" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td><pre class="text"><code>    ...
    &lt;resourceProperty name=&quot;PROP_QUERY_DATA_ROW&quot;&gt;&lt;value&gt;Zacatecas&lt;/value&gt;
      &lt;resourceProperty name=&quot;PROP_QUERY_DATA_ROW_COLUMN&quot;&gt;
        &lt;value&gt;Mexico&lt;/value&gt;&lt;/resourceProperty&gt;
      &lt;resourceProperty name=&quot;PROP_QUERY_DATA_ROW_COLUMN&quot;&gt;
        &lt;value&gt;Zacatecas&lt;/value&gt;&lt;/resourceProperty&gt;
    &lt;/resourceProperty&gt;
    &lt;resourceProperty name=&quot;PROP_QUERY_DATA_ROW&quot;&gt;&lt;value&gt;CA&lt;/value&gt;
      &lt;resourceProperty name=&quot;PROP_QUERY_DATA_ROW_COLUMN&quot;&gt;
        &lt;value&gt;USA&lt;/value&gt;&lt;/resourceProperty&gt;
      &lt;resourceProperty name=&quot;PROP_QUERY_DATA_ROW_COLUMN&quot;&gt;
        &lt;value&gt;CA&lt;/value&gt;&lt;/resourceProperty&gt;
    &lt;/resourceProperty&gt;
    ...
    &lt;resourceProperty name=&quot;PROP_QUERY_DATA_ROW&quot;&gt;&lt;value&gt;WA&lt;/value&gt;
      &lt;resourceProperty name=&quot;PROP_QUERY_DATA_ROW_COLUMN&quot;&gt;
        &lt;value&gt;USA&lt;/value&gt;&lt;/resourceProperty&gt;
      &lt;resourceProperty name=&quot;PROP_QUERY_DATA_ROW_COLUMN&quot;&gt;
        &lt;value&gt;WA&lt;/value&gt;&lt;/resourceProperty&gt;
    &lt;/resourceProperty&gt;
  &lt;/resourceProperty&gt;
  &lt;resourceDescriptor name=&quot;Cascading_state_query&quot; wsType=&quot;query&quot; uriString=&quot;/
                      reports/samples/Cascading_multi_select_report_files/
                      Cascading_state_multi_select_files/Cascading_state_query&quot;
                      isNew=&quot;false&quot;&gt;
    &lt;label&gt;Cascading state query&lt;/label&gt;
    &lt;creationDate&gt;1302268918000&lt;/creationDate&gt;
    &lt;resourceProperty name=&quot;PROP_RESOURCE_TYPE&quot;&gt;
      &lt;value&gt;com.jaspersoft.jasperserver.api.metadata.common.domain.Query&lt;/value&gt;
    &lt;/resourceProperty&gt;
    &lt;resourceProperty name=&quot;PROP_PARENT_FOLDER&quot;&gt;
      &lt;value&gt;/reports/samples/Cascading_multi_select_report_files/
             Cascading_state_multi_select_files&lt;/value&gt;&lt;/resourceProperty&gt;
    &lt;resourceProperty name=&quot;PROP_VERSION&quot;&gt;&lt;value&gt;0&lt;/value&gt;&lt;/resourceProperty&gt;
    &lt;resourceProperty name=&quot;PROP_HAS_DATA&quot;&gt;&lt;value&gt;false&lt;/value&gt;&lt;/resourceProperty&gt;
    &lt;resourceProperty name=&quot;PROP_IS_REFERENCE&quot;&gt;&lt;value&gt;false&lt;/value&gt;
    &lt;/resourceProperty&gt;
    &lt;resourceProperty name=&quot;PROP_QUERY&quot;&gt;
      &lt;value&gt;select distinct billing_address_state, billing_address_country
             from accounts where $X{IN, billing_address_country,
             Country_multi_select} order by billing_address_country,
             billing_address_state&lt;/value&gt;
    &lt;/resourceProperty&gt;
    &lt;resourceProperty name=&quot;PROP_QUERY_LANGUAGE&quot;&gt;&lt;value&gt;sql&lt;/value&gt;
    &lt;/resourceProperty&gt;
    &lt;resourceDescriptor name=&quot;&quot; wsType=&quot;datasource&quot; uriString=&quot;&quot; isNew=&quot;false&quot;&gt;
      &lt;label&gt;null&lt;/label&gt;
      &lt;resourceProperty name=&quot;PROP_REFERENCE_URI&quot;&gt;
        &lt;value&gt;/datasources/JServerJNDIDS&lt;/value&gt;&lt;/resourceProperty&gt;
      &lt;resourceProperty name=&quot;PROP_IS_REFERENCE&quot;&gt;&lt;value&gt;true&lt;/value&gt;
      &lt;/resourceProperty&gt;</code></pre></td>
</tr>
<tr>
<td><pre class="text"><code>    &lt;/resourceDescriptor&gt;
  &lt;/resourceDescriptor&gt;
&lt;/resourceDescriptor&gt;</code></pre></td>
</tr>
</tbody>
</table>
