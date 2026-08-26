---
title: runReport Operation
description: This operation executes a report on the server then returns the report’s results in the specified format. The client application is responsible for prompting users for values to pass to any input...
---

# 1.1 runReport Operation

This operation executes a report on the server then returns the report’s results in the specified format. The client application is responsible for prompting users for values to pass to any input controls referenced by the report, as shown in the following sample request XML:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">request</span> <span class="ot">operationName=</span><span class="st">&quot;runReport&quot;</span> <span class="ot">locale=</span><span class="st">&quot;en&quot;</span>&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">argument</span> <span class="ot">name=</span><span class="st">&quot;RUN_OUTPUT_FORMAT&quot;</span>&gt;JRPRINT&lt;/<span class="kw">argument</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">resourceDescriptor</span> <span class="ot">name=</span><span class="st">&quot;&quot;</span> <span class="ot">wsType=</span><span class="st">&quot;&quot;</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="ot">uriString=</span><span class="st">&quot;/reports/samples/EmployeeAccounts&quot;</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a><span class="ot">isNew=</span><span class="st">&quot;false&quot;</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">label</span>&gt;null&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">parameter</span> <span class="ot">name=</span><span class="st">&quot;EmployeeID&quot;</span>&gt;emil_id&lt;/<span class="kw">parameter</span>&gt;</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">parameter</span> <span class="ot">name=</span><span class="st">&quot;TEST_LIST&quot;</span> <span class="ot">isListItem=</span><span class="st">&quot;true&quot;</span>&gt;A <span class="dv">&amp;amp;</span> L Powers Engineering, Inc&lt;/<span class="kw">parameter</span>&gt;</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">parameter</span> <span class="ot">name=</span><span class="st">&quot;TEST_LIST&quot;</span> <span class="ot">isListItem=</span><span class="st">&quot;true&quot;</span>&gt;A <span class="dv">&amp;amp;</span> U Jaramillo Telecom, Inc&lt;/<span class="kw">parameter</span>&gt;</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">parameter</span> <span class="ot">name=</span><span class="st">&quot;TEST_LIST&quot;</span> <span class="ot">isListItem=</span><span class="st">&quot;true&quot;</span>&gt;A <span class="dv">&amp;amp;</span> U Stalker Telecom, Inc&lt;/<span class="kw">parameter</span>&gt;</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">resourceDescriptor</span>&gt;</span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">request</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

This example shows a parameter tag:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="language-text highlight"><pre><code>&lt;!ELEMENT parameter (#PCDATA)&gt;
&lt;!ATTLIST parameter
name CDATA #REQUIRED
isListItem ( true | false ) false</code></pre></div></td>
</tr>
</tbody>
</table>

In the example, `name` is the input control to set. If the input control is of type `multi-select`, the list of selected values is composed of a set of parameter tags that have the same names and have the `isListItem` attribute set to true, indicating that the parameter is part of a list.

The next example shows the `getInputControlValues` call for a cascading multi-select input control:

1.  The IC_GET_QUERY_DATA argument gets the data from the data source.
2.  The RU_REF_URI argument points to the report in which the input control is used.
3.  Parameter tags under `resourceDescriptor` supply the parameters for the input control. The parameters’ specifics are derived from the `ReportUnit` resource properties ([](api-constants.md)).

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="language-text highlight"><pre><code>ResourceDescriptor rd = new ResourceDescriptor();
rd.setUriString(&quot;/reports/samples/Cascading_multi_select_report_files/                 Cascading_state_multi_select&quot;);
rd.setResourceProperty(rd.PROP_QUERY_DATA, null);
ListItem li1 = new ListItem(&quot;Country_multi_select&quot;, &quot;USA&quot;);
li1.setIsListItem(true);
rd.getParameters().add(li1);
ListItem li2 = new ListItem(&quot;Country_multi_select&quot;, &quot;Mexico&quot;);
li2.setIsListItem(true);
rd.getParameters().add(li2);
java.util.List args = new java.util.ArrayList();
args.add(new Argument( Argument.IC_GET_QUERY_DATA, &quot;&quot;));
args.add(new Argument( Argument.RU_REF_URI,                       &quot;/reports/samples/Cascading_multi_select_report&quot;));
ResourceDescriptor rd2 = wsclnt.get(rd, null, args);</code></pre></div></td>
</tr>
<tr>
<td><div class="language-text highlight"><pre><code>if (rd2.getQueryData() != null) {
  List l = (List) rd2.getQueryData();
  for (Object dr : l) {
    InputControlQueryDataRow icdr = (InputControlQueryDataRow) dr;
    for (Object cv : icdr.getColumnValues()) {
      System.out.print(cv + &quot; | &quot;);
    }
    System.out.println();
  }
}</code></pre></div></td>
</tr>
</tbody>
</table>

!!! note

    Note the following conventions for parameter values:

    -   All parameter values are treated as strings; only number, string, and date/time values are allowed.
    -   Numbers cannot include punctuation for the digit grouping symbol (thousands separator) and must use a period (.) as the decimal separator (if the relative parameter is not an integer).
    -   Dates and date/times must be represented as the number of milliseconds since January 1, 1970, 00:00:00 GMT.
