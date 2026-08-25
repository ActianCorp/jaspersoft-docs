---
title: The getDomainMetaData Operation
description: "The getDomainMetaDataoperation takes these parameters:"
---

# 1.0.1 The getDomainMetaData Operation

The `getDomainMetaData`operation takes these parameters:

- `domainUri` - a string containing the path to the Domain on the server, for example `/domains/John/ExpenseDomain`.
- `localeStr` - a string giving the user locale, for example `en`, `en_US`, or `es_ES_Traditional_WIN`.

The operation returns the tree structure of item sets and items in the requested Domain. The tree structure consists of levels that represent the nested sets and items that represent the items in the Domain. Levels may contain sub-levels, items, or both, thus modelling the hierarchical structure of the Domain.

The following object types are combined to create the tree structure in the return value:

- `SimpleMetaData`. Encapsulates all the item sets and items in a Domain structure:

  - `rootLevel`. The `SimpleMetaLevel` object that is the root of the Domain tree structure.
  - `properties`.Tthere are currently no properties on this object.

- `SimpleMetaLevel`. Represents an item set in the Domain. It has the following attributes:

  - `id` and `label`. Unique identifier and label string for this item set.
  - `items`. An array of `SimpleMetaItem` objects representing the items in this set.
  - `subLevels`. An array of `SimpleMetaLevel` objects representing the sub-sets of this set.
  - `properties`. The `resourceId` key indicates the resource identifier of this item set.

- `SimpleMetaItem`. An item in the Domain. It has the following attributes:

  - `id` and `label`. Unique identifier and label string for this item.
  - `javaType`. The Java class name of this item, for example `java.lang.String`.
  - `properties`. The `javaType` key is identical to the `javaType` attribute, and the `resourceId` key indicates the resource identifier of this item.

!!! note

    A resource identifier is an internal property that identifies the data resource that the set or item references. Web applications do not need to process or return this value.

This is the full SOAP request for a `getDomainMetaData` operation:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><p><code>&lt;?xml version="1.0" encoding="utf-8"?&gt;</code></p>
<div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">soapenv:Envelope</span>&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">soapenv:Body</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">ns1:getDomainMetaData</span> <span class="ot">soapenv:encodingStyle=</span><span class="st">&quot;http://schemas.xmlsoap.org/soap/</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="st">      encoding/&quot;</span> <span class="ot">xmlns:ns1=</span><span class="st">&quot;http://www.jasperforge.org/jasperserver/ws&quot;</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">domainUri</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;/Domains/examples/SampleDomain&lt;/<span class="kw">domainUri</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">localeStr</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;US&lt;/<span class="kw">localeStr</span>&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">ns1:getDomainMetaData</span>&gt;</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">soapenv:Body</span>&gt;</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">soapenv:Envelope</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

The response of the request contains the tree structure of the Domain:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">&lt;?xml</span> <span class="ot">version=</span><span class="st">&quot;1.0&quot;</span> <span class="ot">encoding=</span><span class="st">&quot;UTF-8&quot;</span><span class="fu">?&gt;</span>&lt;<span class="kw">soapenv:Envelope</span>&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">soapenv:Body</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">ns1:getDomainMetaDataResponse</span> <span class="ot">soapenv:encodingStyle=</span><span class="st">&quot;http://schemas.xmlsoap.org/</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="st">      soap/encoding/&quot;</span> <span class="ot">xmlns:ns1=</span><span class="st">&quot;http://www.jasperforge.org/jasperserver/ws&quot;</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">getDomainMetaDataReturn</span> <span class="ot">xsi:type=</span><span class="st">&quot;ns1:SimpleMetaData&quot;</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">rootLevel</span> <span class="ot">xsi:type=</span><span class="st">&quot;ns1:SimpleMetaLevel&quot;</span>&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">id</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;root&lt;/<span class="kw">id</span>&gt;</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">label</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span> <span class="ot">xsi:nil=</span><span class="st">&quot;true&quot;</span>/&gt;</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">properties</span> <span class="ot">soapenc:arrayType=</span><span class="st">&quot;ns1:SimpleProperty[0]&quot;</span> <span class="ot">xsi:type=</span><span class="st">&quot;soapenc:Array&quot;</span>/&gt;</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">items</span> <span class="ot">soapenc:arrayType=</span><span class="st">&quot;ns1:SimpleMetaItem[0]&quot;</span> <span class="ot">xsi:type=</span><span class="st">&quot;soapenc:Array&quot;</span>/&gt;</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">subLevels</span> <span class="ot">soapenc:arrayType=</span><span class="st">&quot;ns1:SimpleMetaLevel[7]&quot;</span> <span class="ot">xsi:type=</span><span class="st">&quot;soapenc:Array&quot;</span>&gt;</span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">subLevels</span> <span class="ot">xsi:type=</span><span class="st">&quot;ns1:SimpleMetaLevel&quot;</span>&gt;</span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>              &lt;<span class="kw">id</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;expense_join&lt;/<span class="kw">id</span>&gt;</span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>              &lt;<span class="kw">label</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;expense&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>              &lt;<span class="kw">properties</span> <span class="ot">soapenc:arrayType=</span><span class="st">&quot;ns1:SimpleProperty[1]&quot;</span> <span class="ot">xsi:type=</span></span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a>                <span class="st">&quot;soapenc:Array&quot;</span>&gt;</span>
<span id="cb1-17"><a href="#cb1-17" aria-hidden="true" tabindex="-1"></a>                &lt;<span class="kw">properties</span> <span class="ot">xsi:type=</span><span class="st">&quot;ns1:SimpleProperty&quot;</span>&gt;</span>
<span id="cb1-18"><a href="#cb1-18" aria-hidden="true" tabindex="-1"></a>                  &lt;<span class="kw">key</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;resourceId&lt;/<span class="kw">key</span>&gt;</span>
<span id="cb1-19"><a href="#cb1-19" aria-hidden="true" tabindex="-1"></a>                  &lt;<span class="kw">value</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;expense_join&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-20"><a href="#cb1-20" aria-hidden="true" tabindex="-1"></a>                &lt;/<span class="kw">properties</span>&gt;</span>
<span id="cb1-21"><a href="#cb1-21" aria-hidden="true" tabindex="-1"></a>              &lt;/<span class="kw">properties</span>&gt;</span>
<span id="cb1-22"><a href="#cb1-22" aria-hidden="true" tabindex="-1"></a>              &lt;<span class="kw">items</span> <span class="ot">soapenc:arrayType=</span><span class="st">&quot;ns1:SimpleMetaItem[2]&quot;</span> <span class="ot">xsi:type=</span><span class="st">&quot;soapenc:Array&quot;</span>&gt;</span>
<span id="cb1-23"><a href="#cb1-23" aria-hidden="true" tabindex="-1"></a>                &lt;<span class="kw">items</span> <span class="ot">xsi:type=</span><span class="st">&quot;ns1:SimpleMetaItem&quot;</span>&gt;</span>
<span id="cb1-24"><a href="#cb1-24" aria-hidden="true" tabindex="-1"></a>                  &lt;<span class="kw">id</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;ej_expense_fact_exp_date&lt;/<span class="kw">id</span>&gt;</span>
<span id="cb1-25"><a href="#cb1-25" aria-hidden="true" tabindex="-1"></a>                  &lt;<span class="kw">label</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;Exp Date&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb1-26"><a href="#cb1-26" aria-hidden="true" tabindex="-1"></a>                  &lt;<span class="kw">javaType</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;java.sql.Date&lt;/<span class="kw">javaType</span>&gt;</span>
<span id="cb1-27"><a href="#cb1-27" aria-hidden="true" tabindex="-1"></a>                  &lt;<span class="kw">properties</span> <span class="ot">soapenc:arrayType=</span><span class="st">&quot;ns1:SimpleProperty[2]&quot;</span> <span class="ot">xsi:type=</span></span>
<span id="cb1-28"><a href="#cb1-28" aria-hidden="true" tabindex="-1"></a>                    <span class="st">&quot;soapenc:Array&quot;</span>&gt;</span>
<span id="cb1-29"><a href="#cb1-29" aria-hidden="true" tabindex="-1"></a>                    &lt;<span class="kw">properties</span> <span class="ot">xsi:type=</span><span class="st">&quot;ns1:SimpleProperty&quot;</span>&gt;</span>
<span id="cb1-30"><a href="#cb1-30" aria-hidden="true" tabindex="-1"></a>                      &lt;<span class="kw">key</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;JavaType&lt;/<span class="kw">key</span>&gt;</span>
<span id="cb1-31"><a href="#cb1-31" aria-hidden="true" tabindex="-1"></a>                      &lt;<span class="kw">value</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;java.sql.Date&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-32"><a href="#cb1-32" aria-hidden="true" tabindex="-1"></a>                    &lt;/<span class="kw">properties</span>&gt;</span>
<span id="cb1-33"><a href="#cb1-33" aria-hidden="true" tabindex="-1"></a>                    &lt;<span class="kw">properties</span> <span class="ot">xsi:type=</span><span class="st">&quot;ns1:SimpleProperty&quot;</span>&gt;</span>
<span id="cb1-34"><a href="#cb1-34" aria-hidden="true" tabindex="-1"></a>                      &lt;<span class="kw">key</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;resourceId&lt;/<span class="kw">key</span>&gt;</span>
<span id="cb1-35"><a href="#cb1-35" aria-hidden="true" tabindex="-1"></a>                      &lt;<span class="kw">value</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;expense_join.e.exp_date&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-36"><a href="#cb1-36" aria-hidden="true" tabindex="-1"></a>                    &lt;/<span class="kw">properties</span>&gt;</span>
<span id="cb1-37"><a href="#cb1-37" aria-hidden="true" tabindex="-1"></a>                  &lt;/<span class="kw">properties</span>&gt;</span>
<span id="cb1-38"><a href="#cb1-38" aria-hidden="true" tabindex="-1"></a>                &lt;/<span class="kw">items</span>&gt;</span>
<span id="cb1-39"><a href="#cb1-39" aria-hidden="true" tabindex="-1"></a>                &lt;<span class="kw">items</span> <span class="ot">xsi:type=</span><span class="st">&quot;ns1:SimpleMetaItem&quot;</span>&gt;</span>
<span id="cb1-40"><a href="#cb1-40" aria-hidden="true" tabindex="-1"></a>                  &lt;<span class="kw">id</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;ej_expense_fact_amount&lt;/<span class="kw">id</span>&gt;</span>
<span id="cb1-41"><a href="#cb1-41" aria-hidden="true" tabindex="-1"></a>                  &lt;<span class="kw">label</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;Amount&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb1-42"><a href="#cb1-42" aria-hidden="true" tabindex="-1"></a>                  &lt;<span class="kw">javaType</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;java.math.BigDecimal&lt;/<span class="kw">javaType</span>&gt;</span>
<span id="cb1-43"><a href="#cb1-43" aria-hidden="true" tabindex="-1"></a>                  &lt;<span class="kw">properties</span> <span class="ot">soapenc:arrayType=</span><span class="st">&quot;ns1:SimpleProperty[2]&quot;</span> <span class="ot">xsi:type=</span></span>
<span id="cb1-44"><a href="#cb1-44" aria-hidden="true" tabindex="-1"></a>                    <span class="st">&quot;soapenc:Array&quot;</span>&gt;</span>
<span id="cb1-45"><a href="#cb1-45" aria-hidden="true" tabindex="-1"></a>                    &lt;<span class="kw">properties</span> <span class="ot">xsi:type=</span><span class="st">&quot;ns1:SimpleProperty&quot;</span>&gt;</span>
<span id="cb1-46"><a href="#cb1-46" aria-hidden="true" tabindex="-1"></a>                      &lt;<span class="kw">key</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;JavaType&lt;/<span class="kw">key</span>&gt;</span>
<span id="cb1-47"><a href="#cb1-47" aria-hidden="true" tabindex="-1"></a>                      &lt;<span class="kw">value</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;java.math.BigDecimal&lt;/<span class="kw">value</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td><div class="language-text highlight"><pre><code>                    &lt;/properties&gt;
                    &lt;properties xsi:type=&quot;ns1:SimpleProperty&quot;&gt;
                      &lt;key xsi:type=&quot;xsd:string&quot;&gt;resourceId&lt;/key&gt;
                      &lt;value xsi:type=&quot;xsd:string&quot;&gt;expense_join.e.amount&lt;/value&gt;
                    &lt;/properties&gt;
                  &lt;/properties&gt;
                &lt;/items&gt;
              &lt;/items&gt;
              &lt;subLevels soapenc:arrayType=&quot;ns1:SimpleMetaLevel[0]&quot; xsi:type=
                &quot;soapenc:Array&quot;/&gt;
            &lt;/subLevels&gt;
            &lt;subLevels xsi:type=&quot;ns1:SimpleMetaLevel&quot;&gt;
              &lt;id xsi:type=&quot;xsd:string&quot;&gt;expense_join_store&lt;/id&gt;
              &lt;label xsi:type=&quot;xsd:string&quot;&gt;store&lt;/label&gt;
              &lt;properties soapenc:arrayType=&quot;ns1:SimpleProperty[1]&quot; xsi:type=
                &quot;soapenc:Array&quot;&gt;
                &lt;properties xsi:type=&quot;ns1:SimpleProperty&quot;&gt;
                  &lt;key xsi:type=&quot;xsd:string&quot;&gt;resourceId&lt;/key&gt;
                  &lt;value xsi:type=&quot;xsd:string&quot;&gt;expense_join&lt;/value&gt;
                &lt;/properties&gt;
              &lt;/properties&gt;
              &lt;items soapenc:arrayType=&quot;ns1:SimpleMetaItem[24]&quot; xsi:type=
                &quot;soapenc:Array&quot;&gt;
                &lt;items xsi:type=&quot;ns1:SimpleMetaItem&quot;&gt;
                  &lt;id xsi:type=&quot;xsd:string&quot;&gt;ej_store_store_type&lt;/id&gt;
                  &lt;label xsi:type=&quot;xsd:string&quot;&gt;Store Type&lt;/label&gt;
                  &lt;javaType xsi:type=&quot;xsd:string&quot;&gt;java.lang.String&lt;/javaType&gt;
                  &lt;properties soapenc:arrayType=&quot;ns1:SimpleProperty[2]&quot; xsi:type=
                    &quot;soapenc:Array&quot;&gt;
                    &lt;properties xsi:type=&quot;ns1:SimpleProperty&quot;&gt;
                      &lt;key xsi:type=&quot;xsd:string&quot;&gt;JavaType&lt;/key&gt;
                      &lt;value xsi:type=&quot;xsd:string&quot;&gt;java.lang.String&lt;/value&gt;
                    &lt;/properties&gt;
                    &lt;properties xsi:type=&quot;ns1:SimpleProperty&quot;&gt;
                      &lt;key xsi:type=&quot;xsd:string&quot;&gt;resourceId&lt;/key&gt;
                      &lt;value xsi:type=&quot;xsd:string&quot;&gt;expense_join.s.store_type&lt;/value&gt;
                    &lt;/properties&gt;
                  &lt;/properties&gt;
                &lt;/items&gt;
                ...
              &lt;/items&gt;
              &lt;subLevels soapenc:arrayType=&quot;ns1:SimpleMetaLevel[0]&quot; xsi:type=
                &quot;soapenc:Array&quot;/&gt;
            &lt;/subLevels&gt;
          &lt;/subLevels&gt;
        &lt;/rootLevel&gt;
        &lt;properties soapenc:arrayType=&quot;ns1:SimpleProperty[0]&quot; xsi:type=&quot;soapenc:Array&quot;/&gt;
      &lt;/getDomainMetaDataReturn&gt;
    &lt;/ns1:getDomainMetaDataResponse&gt;
  &lt;/soapenv:Body&gt;
&lt;/soapenv:Envelope&gt;</code></pre></div></td>
</tr>
</tbody>
</table>
