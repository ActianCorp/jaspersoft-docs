---
title: Undefined DataType
description: "By default, JasperReports Server treats \"undefined\" fields in domains as strings. If your data includes \"undefined\" fields that are a different data type, set the following option for your database."
---

# Undefined DataType

By default, JasperReports Server treats "undefined" fields in domains as strings. If your data includes "undefined" fields that are a different data type, set the following option for your database.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>Undefined Data Type</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><span>.../WEB-INF/applicationContext-jdbc-metadata.xml</span></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Bean</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>jdbc2JavaType Mapping</code></p></td>
<td><p><code>jdbcMeta Configuration</code></p></td>
<td><p>This property contains a map of database field types to Java types. Find the line for the undefined data type</p>
<div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">entry</span> <span class="ot">key=</span><span class="st">&quot;undefined&quot;</span> <span class="ot">value=</span><span class="st">&quot;java.lang.String&quot;</span>&gt;</span></code></pre></div>
<p>Change the value to the correct data type for your undefined fields.</p></td>
</tr>
</tbody>
</table>
