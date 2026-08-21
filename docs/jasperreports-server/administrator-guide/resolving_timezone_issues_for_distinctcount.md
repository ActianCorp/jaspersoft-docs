---
title: Ad Hoc Not Displaying Data Due To Timezone Issues
description: "When the database and JasperReports Server operate in different timezones, it can lead to inaccurate calculations for distinct counts on timestamp data, which can result in ad hoc not displaying data..."
---

# Ad Hoc Not Displaying Data Due To Timezone Issues

When the database and JasperReports Server operate in different timezones, it can lead to inaccurate calculations for distinct counts on timestamp data, which can result in ad hoc not displaying data for some date/time interval. To resolve this, the processing for distinct counts must be forced to occur entirely within JasperReports Server, ensuring a consistent timezone is used for all calculations.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>Configuration for Distinct Count Calculation Method</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>WEB-INF/applicationContext-adhoc-dataStrategy.xml</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">bean</span> <span class="ot">class=</span><span class="st">&quot;com.jaspersoft.ji.adhoc.strategy.AggregateConfig&quot;</span>&gt;&lt;<span class="kw">property</span> <span class="ot">name=</span><span class="st">&quot;name&quot;</span> <span class="ot">value=</span><span class="st">&quot;CountDistinct&quot;</span>/&gt;&lt;<span class="kw">property</span> <span class="ot">name=</span><span class="st">&quot;functionName&quot;</span> <span class="ot">value=</span><span class="st">&quot;CountDistinct&quot;</span>/&gt;<span class="co">&lt;!-- distinct count not currently mapped directly to sql func --&gt;</span>&lt;<span class="kw">property</span> <span class="ot">name=</span><span class="st">&quot;calcMethod&quot;</span> <span class="ot">value=</span><span class="st">&quot;sqlGroupBy&quot;</span>/&gt;&lt;/<span class="kw">bean</span>&gt;</span></code></pre></div></td>
<td colspan="2"><p>To enforce server-side processing for distinct counts, you must modify the <code>AggregateConfig</code> bean for <code>CountDistinct</code>. This involves changing the value of the <code>calcMethod</code> property from <code>sqlUnionAll</code> to <code>sqlGroupBy</code>.</p></td>
</tr>
</tbody>
</table>
