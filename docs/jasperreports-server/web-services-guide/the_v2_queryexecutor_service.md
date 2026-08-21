---
title: The v2/queryExecutor Service
description: "In addition to running reports, JasperReports Server exposes queries that you can run through the restv2/queryExecutor service. In release 5.1, the only resource that supports queries is a Domain."
---

# 1.1 The v2/queryExecutor Service

In addition to running reports, JasperReports Server exposes queries that you can run through the rest_v2/queryExecutor service. In release 5.1, the only resource that supports queries is a Domain.

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/<span>rest_v2/queryExecutor/</span>path/to/Domain/?q=&lt;query&gt;</p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p>q</p></td>
<td><p>Required String</p></td>
<td colspan="2"><p>The query string is a special format that references the fields and measures exposed by the Domain. To write this query, you must have knowledge of the Domain schema that is not available through the REST services. See below.</p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p>accept: application/xml (default)</p>
<p>accept: application/json</p>
<p>Accept-Language: &lt;locale&gt;, &lt;relativeQualityFactor&gt;; for example en_US, q=0.8;</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The body contains the data that is the result of the query. See the format of the data below.</p></td>
<td><p>404 Not Found – When the specified Domain does not exist.</p></td>
</tr>
</tbody>
</table>

If the query is too large to fit in the argument in the URL, use the POST method to send it as request content:

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
<td><p>POST</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/<span>rest_v2/queryExecutor/</span>path/to/Domain/</p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p>application/xml</p></td>
<td colspan="2"><p>The query string is a special format that references the fields and measures exposed by the Domain. To write this query, you must have knowledge of the Domain schema that is not available through the REST services. See below.</p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p>accept: application/xml (default)</p>
<p>accept: application/json</p>
<p>Accept-Language: &lt;locale&gt;, &lt;relativeQualityFactor&gt;; for example en_US, q=0.8;</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The body contains the data that is the result of the query. See the format of the data below.</p></td>
<td><p>404 Not Found – When the specified Domain does not exist.</p></td>
</tr>
</tbody>
</table>

The following example show the format of a query in XML:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">query</span>&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">queryFields</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">queryField</span> <span class="ot">id=</span><span class="st">&quot;expense_join_store.ej_store_store_city&quot;</span>/&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">queryField</span> <span class="ot">id=</span><span class="st">&quot;expense_join_store.ej_store_store_country&quot;</span>/&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">queryField</span> <span class="ot">id=</span><span class="st">&quot;expense_join_store.ej_store_store_name&quot;</span>/&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">queryField</span> <span class="ot">id=</span><span class="st">&quot;expense_join_store.ej_store_store_state&quot;</span>/&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">queryField</span> <span class="ot">id=</span><span class="st">&quot;expense_join_store.ej_store_store_street_address&quot;</span>/&gt;</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">queryFields</span>&gt;</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">queryFilterString</span>&gt;expense_join_store.ej_store_store_country == &#39;USA&#39;</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>                     and expense_join_store.ej_store_store_state == &#39;CA&#39;</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">queryFilterString</span>&gt;</span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">query</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

And the following sample shows the result of query. In order to optimize the size of the response, rows are presented as sets of values without the column names repeated for each row. The column IDs appear at the top of the result, as shown in the following example. As with the query, the result requires knowledge of the Domain schema to identify the human-readable column names.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">queryResult</span>&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">names</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">name</span>&gt;expense_join_account.ej_account_account_description&lt;/<span class="kw">name</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">name</span>&gt;expense_join_account.ej_expense_fact_account_id&lt;/<span class="kw">name</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">name</span>&gt;expense_join_account.ej_account_account_parent&lt;/<span class="kw">name</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">name</span>&gt;expense_join_account.ej_account_account_rollup&lt;/<span class="kw">name</span>&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">name</span>&gt;expense_join_account.ej_account_account_type&lt;/<span class="kw">name</span>&gt;</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">name</span>&gt;expense_join_account.ej_account_Custom_Members&lt;/<span class="kw">name</span>&gt;</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">name</span>&gt;expense_join.ej_expense_fact_amount&lt;/<span class="kw">name</span>&gt;</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">name</span>&gt;expense_join_store.ej_store_store_type&lt;/<span class="kw">name</span>&gt;</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">name</span>&gt;expense_join_store.ej_store_store_street_address&lt;/<span class="kw">name</span>&gt;</span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">name</span>&gt;expense_join_store.ej_store_store_city&lt;/<span class="kw">name</span>&gt;</span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">name</span>&gt;expense_join_store.ej_store_store_state&lt;/<span class="kw">name</span>&gt;</span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">name</span>&gt;expense_join_store.ej_store_store_postal_code&lt;/<span class="kw">name</span>&gt;</span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">name</span>&gt;expense_join_store.sample_time&lt;/<span class="kw">name</span>&gt;</span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">names</span>&gt;</span>
<span id="cb1-17"><a href="#cb1-17" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">values</span>&gt;</span>
<span id="cb1-18"><a href="#cb1-18" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">row</span>&gt;</span>
<span id="cb1-19"><a href="#cb1-19" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span> <span class="ot">xsi:type=</span><span class="st">&quot;xs:string&quot;</span>&gt;Marketing&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-20"><a href="#cb1-20" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span> <span class="ot">xsi:type=</span><span class="st">&quot;xs:int&quot;</span>&gt;4300&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-21"><a href="#cb1-21" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span> <span class="ot">xsi:type=</span><span class="st">&quot;xs:int&quot;</span>&gt;4000&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-22"><a href="#cb1-22" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span> <span class="ot">xsi:type=</span><span class="st">&quot;xs:string&quot;</span>&gt;+&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-23"><a href="#cb1-23" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span> <span class="ot">xsi:type=</span><span class="st">&quot;xs:string&quot;</span>&gt;Expense&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-24"><a href="#cb1-24" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span> <span class="ot">xsi:nil=</span><span class="st">&quot;true&quot;</span>/&gt;</span>
<span id="cb1-25"><a href="#cb1-25" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span> <span class="ot">xsi:type=</span><span class="st">&quot;xs:double&quot;</span>&gt;1884.0000&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-26"><a href="#cb1-26" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span> <span class="ot">xsi:type=</span><span class="st">&quot;xs:dateTime&quot;</span>&gt;1997-01-01T04:05:06+02:00&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-27"><a href="#cb1-27" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span> <span class="ot">xsi:type=</span><span class="st">&quot;xs:string&quot;</span>&gt;HeadQuarters&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-28"><a href="#cb1-28" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span> <span class="ot">xsi:type=</span><span class="st">&quot;xs:string&quot;</span>&gt;1 Alameda Way&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-29"><a href="#cb1-29" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span> <span class="ot">xsi:type=</span><span class="st">&quot;xs:string&quot;</span>&gt;Alameda&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-30"><a href="#cb1-30" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span> <span class="ot">xsi:type=</span><span class="st">&quot;xs:string&quot;</span>&gt;CA&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-31"><a href="#cb1-31" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span> <span class="ot">xsi:type=</span><span class="st">&quot;xs:int&quot;</span>&gt;94502&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-32"><a href="#cb1-32" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span> <span class="ot">xsi:type=</span><span class="st">&quot;xs:string&quot;</span>&gt;USA&lt;/<span class="kw">value</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span> <span class="ot">xsi:type=</span><span class="st">&quot;xs:time&quot;</span>&gt;04:05:06+02:00&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">row</span>&gt;</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>     ...</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">values</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">queryResult</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

!!! note

    Both date-only and timestamp fields are given in the ISO date-time format such as 1997-01-01T04:05:06+02:00.

    For database columns that store a time and date that includes a time zone, such as “timestamp with time zone” in PostgreSQL, the result is not guaranteed to be in the same timezone as stored in the database. These dates and times are converted to the server’s time zone.
