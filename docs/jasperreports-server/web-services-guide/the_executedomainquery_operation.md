---
title: The executeDomainQuery Operation
description: "The executeDomainQueryoperation takes these parameters:"
---

# 1.0.1 The executeDomainQuery Operation

The `executeDomainQuery`operation takes these parameters:

- `domainUri` - a string containing the path to the Domain on the server, for example `/domains/John/ExpenseDomain`.
- `queryStr` - a string containing the Domain query composed of fields and a filter expression (see below for the syntax).
- `localeStr` - a string giving the user locale, for example `en`, `en_US`, or `es_ES_Traditional_WIN`.
- `dateFormatStr` - a string giving the date format desired in date fields, for example `MM/dd/yyyy` or `h:mm a`.

!!! note

    Be sure the format has date and time portions if you expect to have both date and time fields, for example `yyyy.MM.dd G 'at' HH:mm:ss z`

The query string is composed of the following elements that create a syntax for the Domain query:

- `<query>` - encapsulates the whole query.
- `<queryFields>` - contains a sequence of `<queryField>` elements. The order of fields will be preserved in the results.
- `<queryField id="<fullyQualifiedID>" />`- an empty element where `<fullyQualifiedID>` gives the unique identifier of an item you want to appear as a column in the results. The identifier must be fully qualified, which means it includes the identifiers of the set and super-sets to which the item belongs. The fully qualified identifier is similar to the path of the item in the Domain, using a period (`.`) to separate each set identifier.
- `<queryFilterString>` - the filter string for the query uses an application-specific syntax called Domain Expression Language (DomEL).

The following example shows a filter string that must match two values:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">query</span>&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">queryFields</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">queryField</span> <span class="ot">id=</span><span class="st">&quot;expense_join_store.ej_store_store_city&quot;</span> /&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">queryField</span> <span class="ot">id=</span><span class="st">&quot;expense_join_store.ej_store_store_country&quot;</span> /&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">queryField</span> <span class="ot">id=</span><span class="st">&quot;expense_join_store.ej_store_store_name&quot;</span> /&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">queryField</span> <span class="ot">id=</span><span class="st">&quot;expense_join_store.ej_store_store_state&quot;</span> /&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">queryField</span> <span class="ot">id=</span><span class="st">&quot;expense_join_store.ej_store_store_street_address&quot;</span> /&gt;</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">queryFields</span>&gt;</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">queryFilterString</span>&gt;expense_join_store.ej_store_store_country == &#39;USA&#39; and </span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>    expense_join_store.ej_store_store_state == &#39;CA&#39;&lt;/<span class="kw">queryFilterString</span>&gt;</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">query</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

Note that when the query string appears in the SOAP example below, special characters such as `<` and `>` are converted to their corresponding character entities, `&lt;` and `&gt;` respectively.

The `executeDomainQuery`operation returns results in the following objects:

- `ResultSetData`. Encapsulates the results of the Domain query. It contains column names and rows of data:

  - `names`. Array of column names in the result set. These names match the order and items in the query fields.
  - `data`. An array of data rows.

- `DataRow`. Represents a record and contains values for each column in a row:

  - `data`. An array of strings, one for the value in each column, in the same order as the names array.

!!! note

    Note that all values are given in string format.

The following example shows the full SOAP request for an `executeDomainQuery` operation on a sample Domain:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">&lt;?xml</span> <span class="ot">version=</span><span class="st">&quot;1.0&quot;</span> <span class="ot">encoding=</span><span class="st">&quot;utf-8&quot;</span><span class="fu">?&gt;</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">soapenv:Envelope</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">soapenv:Body</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">ns1:executeDomainQuery</span> <span class="ot">soapenv:encodingStyle=</span><span class="st">&quot;http://schemas.xmlsoap.org/soap/</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a><span class="st">      encoding/&quot;</span> <span class="ot">xmlns:ns1=</span><span class="st">&quot;http://www.jasperforge.org/jasperserver/ws&quot;</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">domainUri</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;/Domains/examples/SampleDomain&lt;/<span class="kw">domainUri</span>&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">queryStr</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;<span class="dv">&amp;lt;</span>query<span class="dv">&amp;gt;</span>  <span class="dv">&amp;lt;</span>queryFields<span class="dv">&amp;gt;</span>    <span class="dv">&amp;lt;</span>queryField id=<span class="dv">&amp;quot;</span>expense_join_account.ej_account_account_description<span class="dv">&amp;quot;</span>/<span class="dv">&amp;gt;&amp;lt;</span>queryField id=<span class="dv">&amp;quot;</span>expense_join_account.ej_expense_fact_account_id<span class="dv">&amp;quot;</span> /<span class="dv">&amp;gt;</span>    <span class="dv">&amp;lt;</span>queryField id=<span class="dv">&amp;quot;</span>expense_join_account.ej_account_account_parent<span class="dv">&amp;quot;</span> /<span class="dv">&amp;gt;</span>    <span class="dv">&amp;lt;</span>queryField id=<span class="dv">&amp;quot;</span>expense_join_account.ej_account_account_rollup<span class="dv">&amp;quot;</span> /<span class="dv">&amp;gt;</span>    <span class="dv">&amp;lt;</span>queryField id=<span class="dv">&amp;quot;</span>expense_join_account.ej_account_account_type<span class="dv">&amp;quot;</span> /<span class="dv">&amp;gt;</span>    <span class="dv">&amp;lt;</span>queryField id=<span class="dv">&amp;quot;</span>expense_join_account.ej_account_Custom_Members<span class="dv">&amp;quot;</span> /<span class="dv">&amp;gt;</span>    <span class="dv">&amp;lt;</span>queryField id=<span class="dv">&amp;quot;</span>expense_join.ej_expense_fact_amount<span class="dv">&amp;quot;</span> /<span class="dv">&amp;gt;</span>    <span class="dv">&amp;lt;</span>queryField id=<span class="dv">&amp;quot;</span>expense_join.ej_expense_fact_exp_date<span class="dv">&amp;quot;</span> /<span class="dv">&amp;gt;</span> <span class="dv">&amp;lt;</span>queryField id=<span class="dv">&amp;quot;</span>expense_join_store.ej_store_store_type<span class="dv">&amp;quot;</span> /<span class="dv">&amp;gt;&amp;lt;</span>queryField id=<span class="dv">&amp;quot;</span>expense_join_store.ej_store_store_street_address<span class="dv">&amp;quot;</span> /<span class="dv">&amp;gt;</span> <span class="dv">&amp;lt;</span>queryField id=<span class="dv">&amp;quot;</span>expense_join_store.ej_store_store_city<span class="dv">&amp;quot;</span> /<span class="dv">&amp;gt;</span> <span class="dv">&amp;lt;</span>queryField id=<span class="dv">&amp;quot;</span>expense_join_store.ej_store_store_state<span class="dv">&amp;quot;</span> /<span class="dv">&amp;gt;&amp;lt;</span>queryField id=<span class="dv">&amp;quot;</span>expense_join_store.ej_store_store_postal_code<span class="dv">&amp;quot;</span> /<span class="dv">&amp;gt;</span> <span class="dv">&amp;lt;</span>queryField id=<span class="dv">&amp;quot;</span>expense_join_store.ej_store_store_country<span class="dv">&amp;quot;</span> /<span class="dv">&amp;gt;</span> <span class="dv">&amp;lt;</span>queryFields<span class="dv">&amp;gt;</span>  <span class="dv">&amp;lt;</span>queryFilterString<span class="dv">&amp;gt;</span>expense_join_account.ej_account_account_description == &#39;Marketing&#39;<span class="dv">&amp;lt;</span>/queryFilterString<span class="dv">&amp;gt;&amp;lt;</span>/query<span class="dv">&amp;gt;</span>&lt;/<span class="kw">queryStr</span>&gt;</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">localeStr</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;US&lt;/<span class="kw">localeStr</span>&gt;</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">dateFormatStr</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;MM/dd/yyyy&lt;/<span class="kw">dateFormatStr</span>&gt;</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">ns1:executeDomainQuery</span>&gt;</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">soapenv:Body</span>&gt;</span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">soapenv:Envelope</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

The response to the request contains the current values in the specified Domain:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">&lt;?xml</span> <span class="ot">version=</span><span class="st">&quot;1.0&quot;</span> <span class="ot">encoding=</span><span class="st">&quot;UTF-8&quot;</span><span class="fu">?&gt;</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">soapenv:Envelope</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">soapenv:Body</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">ns1:executeDomainQueryResponse</span> <span class="ot">soapenv:encodingStyle=</span><span class="st">&quot;http://schemas.xmlsoap.org/</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a><span class="st">      soap/encoding/&quot;</span> <span class="ot">xmlns:ns1=</span><span class="st">&quot;http://www.jasperforge.org/jasperserver/ws&quot;</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">executeDomainQueryReturn</span> <span class="ot">xsi:type=</span><span class="st">&quot;ns1:ResultSetData&quot;</span>&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">names</span> <span class="ot">soapenc:arrayType=</span><span class="st">&quot;xsd:string[31]&quot;</span> <span class="ot">xsi:type=</span><span class="st">&quot;soapenc:Array&quot;</span>&gt;</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">names</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;expense_join_account.ej_account_account_</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>            description/&gt;</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">names</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;expense_join_account.ej_expense_fact_</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>            account_id/&gt;</span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">names</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;expense_join_account.ej_account_account_parent/&gt;</span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">names</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;expense_join_account.ej_account_account_rollup/&gt;</span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">names</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;expense_join_account.ej_account_account_type/&gt;</span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">names</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;expense_join_account.ej_account_Custom_Members/&gt;</span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">names</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;expense_join.ej_expense_fact_amount/&gt;</span></code></pre></div></td>
</tr>
<tr>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">names</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;expense_join_store.ej_store_store_type/&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">names</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;expense_join_store.ej_store_store_street_</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>            address/&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">names</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;expense_join_store.ej_store_store_city/&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">names</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;expense_join_store.ej_store_store_state/&gt;</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">names</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;expense_join_store.ej_store_store_postal_code/&gt;</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">names</span>&gt;</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">data</span> <span class="ot">soapenc:arrayType=</span><span class="st">&quot;ns1:DataRow[600]&quot;</span> <span class="ot">xsi:type=</span><span class="st">&quot;soapenc:Array&quot;</span>&gt;</span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">data</span> <span class="ot">xsi:type=</span><span class="st">&quot;ns1:DataRow&quot;</span>&gt;</span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">data</span> <span class="ot">soapenc:arrayType=</span><span class="st">&quot;xsd:string[31]&quot;</span> <span class="ot">xsi:type=</span><span class="st">&quot;soapenc:Array&quot;</span>&gt;</span>
<span id="cb2-11"><a href="#cb2-11" aria-hidden="true" tabindex="-1"></a>              &lt;<span class="kw">data</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;Marketing&lt;/<span class="kw">data</span>&gt;</span>
<span id="cb2-12"><a href="#cb2-12" aria-hidden="true" tabindex="-1"></a>              &lt;<span class="kw">data</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;4300&lt;/<span class="kw">data</span>&gt;</span>
<span id="cb2-13"><a href="#cb2-13" aria-hidden="true" tabindex="-1"></a>              &lt;<span class="kw">data</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;4000&lt;/<span class="kw">data</span>&gt;</span>
<span id="cb2-14"><a href="#cb2-14" aria-hidden="true" tabindex="-1"></a>              &lt;<span class="kw">data</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;+&lt;/<span class="kw">data</span>&gt;</span>
<span id="cb2-15"><a href="#cb2-15" aria-hidden="true" tabindex="-1"></a>              &lt;<span class="kw">data</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;Expense&lt;/<span class="kw">data</span>&gt;</span>
<span id="cb2-16"><a href="#cb2-16" aria-hidden="true" tabindex="-1"></a>              &lt;<span class="kw">data</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span> <span class="ot">xsi:nil=</span><span class="st">&quot;true&quot;</span>/&gt;</span>
<span id="cb2-17"><a href="#cb2-17" aria-hidden="true" tabindex="-1"></a>              &lt;<span class="kw">data</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;1884.0000&lt;/<span class="kw">data</span>&gt;</span>
<span id="cb2-18"><a href="#cb2-18" aria-hidden="true" tabindex="-1"></a>              &lt;<span class="kw">data</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;01/01/1997&lt;/<span class="kw">data</span>&gt;</span>
<span id="cb2-19"><a href="#cb2-19" aria-hidden="true" tabindex="-1"></a>              &lt;<span class="kw">data</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;HeadQuarters&lt;/<span class="kw">data</span>&gt;</span>
<span id="cb2-20"><a href="#cb2-20" aria-hidden="true" tabindex="-1"></a>              &lt;<span class="kw">data</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;1 Alameda Way&lt;/<span class="kw">data</span>&gt;</span>
<span id="cb2-21"><a href="#cb2-21" aria-hidden="true" tabindex="-1"></a>              &lt;<span class="kw">data</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;Alameda&lt;/<span class="kw">data</span>&gt;</span>
<span id="cb2-22"><a href="#cb2-22" aria-hidden="true" tabindex="-1"></a>              &lt;<span class="kw">data</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;CA&lt;/<span class="kw">data</span>&gt;</span>
<span id="cb2-23"><a href="#cb2-23" aria-hidden="true" tabindex="-1"></a>              &lt;<span class="kw">data</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;94502&lt;/<span class="kw">data</span>&gt;</span>
<span id="cb2-24"><a href="#cb2-24" aria-hidden="true" tabindex="-1"></a>              &lt;<span class="kw">data</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;USA&lt;/<span class="kw">data</span>&gt;</span>
<span id="cb2-25"><a href="#cb2-25" aria-hidden="true" tabindex="-1"></a>            &lt;/<span class="kw">data</span>&gt;</span>
<span id="cb2-26"><a href="#cb2-26" aria-hidden="true" tabindex="-1"></a>          &lt;/<span class="kw">data</span>&gt;</span>
<span id="cb2-27"><a href="#cb2-27" aria-hidden="true" tabindex="-1"></a>...</span>
<span id="cb2-28"><a href="#cb2-28" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">data</span>&gt;</span>
<span id="cb2-29"><a href="#cb2-29" aria-hidden="true" tabindex="-1"></a>      &lt;/<span class="kw">executeDomainQueryReturn</span>&gt;</span>
<span id="cb2-30"><a href="#cb2-30" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">ns1:executeDomainQueryResponse</span>&gt;</span>
<span id="cb2-31"><a href="#cb2-31" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">soapenv:Body</span>&gt;</span>
<span id="cb2-32"><a href="#cb2-32" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">soapenv:Envelope</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>
