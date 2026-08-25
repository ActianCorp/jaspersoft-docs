---
title: The v2/domains/metadata Service
description: "This section describes functionality that can be restricted by the software license for JasperReports Server. If you don’t see some of the options described in this section, your license may prohibit..."
---

# 1.1 The v2/domains/metadata Service

!!! info "Important"

    This section describes functionality that can be restricted by the software license for JasperReports Server. If you don’t see some of the options described in this section, your license may prohibit you from using them. To find out what you're licensed to use, or to upgrade your license, contact Jaspersoft.

The REST v2/domains/metadata service gives access to the sets and items exposed by a Domain for use in Ad Hoc reports. Items are database fields exposed by the Domain, after all joins, filters, and calculated fields have been applied to the database tables selected in the Domain. Sets are groups of items, arranged by the Domain creator for use by report creators.

!!! note

    A limitation of the v2/domains/metadata service only allows it to operate on Domains with a single data island. A data island is a group of fields that are all related by joins between the database tables in the Domain. Fields that belong to tables that are not joined in the Domain belong to separate data islands.

If your Domain contains localization bundles you can specify a locale and an optional alternate locale and preference (called q-value, a decimal between 0 and 1).

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/domains</span>/path/to/Domain/<span>metadata</span></p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p>Accept-Language: &lt;locale&gt;[, &lt;alt-locale&gt;;q=0.8]</p>
<p>Accept: application/xml (default)</p>
<p>Accept: application/json</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The body is XML containing the list of resourceDescriptors.</p></td>
<td><p>404 Not Found – The specified Domain URI is not found in the repository. This service also returns an XML <code>errorDescriptor</code> giving a human-readable error message.</p></td>
</tr>
</tbody>
</table>

The response of the v2/domains/metadata service is an XML or JSON structure that describes the sets and items available in the selected Domain. This metadata includes the localized labels for the sets and items, as well as the datatypes of the items. The `resourceId` of the sets and items are internal to the Domain and not meaningful or otherwise useable.

For more information about Domains, refer to the JasperReports® Server User Guide.

The following example shows the JSON response for a Domain with:

- A set named expense containing:

  - An item named Exp Date of type Date
  - An item named Amount of type BigDecimal

- A set named store containing:

  - An item named Store Type of type String
  - ...

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;rootLevel&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;id&quot;</span><span class="fu">:</span><span class="st">&quot;root&quot;</span><span class="fu">,</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;subLevels&quot;</span><span class="fu">:</span><span class="ot">[</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>            <span class="fu">{</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>                <span class="dt">&quot;id&quot;</span><span class="fu">:</span><span class="st">&quot;expense_join&quot;</span><span class="fu">,</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>                <span class="dt">&quot;label&quot;</span><span class="fu">:</span><span class="st">&quot;expense&quot;</span><span class="fu">,</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>                <span class="dt">&quot;properties&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>                        <span class="dt">&quot;resourceId&quot;</span><span class="fu">:</span> <span class="st">&quot;expense_join&quot;</span></span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>                <span class="fu">},</span></span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>                <span class="dt">&quot;items&quot;</span><span class="fu">:</span><span class="ot">[</span></span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>                    <span class="fu">{</span></span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>                        <span class="dt">&quot;id&quot;</span><span class="fu">:</span><span class="st">&quot;ej_expense_fact_exp_date&quot;</span><span class="fu">,</span></span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>                        <span class="dt">&quot;label&quot;</span><span class="fu">:</span><span class="st">&quot;Exp Date&quot;</span><span class="fu">,</span></span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>                        <span class="dt">&quot;properties&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a>                                <span class="dt">&quot;JavaType&quot;</span><span class="fu">:</span> <span class="st">&quot;java.sql.Date&quot;</span><span class="fu">,</span></span>
<span id="cb1-17"><a href="#cb1-17" aria-hidden="true" tabindex="-1"></a>                                <span class="dt">&quot;resourceId&quot;</span><span class="fu">:</span> <span class="st">&quot;expense_join.e.exp_date&quot;</span></span>
<span id="cb1-18"><a href="#cb1-18" aria-hidden="true" tabindex="-1"></a>                        <span class="fu">}</span></span>
<span id="cb1-19"><a href="#cb1-19" aria-hidden="true" tabindex="-1"></a>                    <span class="fu">}</span><span class="ot">,</span></span>
<span id="cb1-20"><a href="#cb1-20" aria-hidden="true" tabindex="-1"></a>                    <span class="fu">{</span></span>
<span id="cb1-21"><a href="#cb1-21" aria-hidden="true" tabindex="-1"></a>                        <span class="dt">&quot;id&quot;</span><span class="fu">:</span><span class="st">&quot;ej_expense_fact_amount&quot;</span><span class="fu">,</span></span>
<span id="cb1-22"><a href="#cb1-22" aria-hidden="true" tabindex="-1"></a>                        <span class="dt">&quot;label&quot;</span><span class="fu">:</span><span class="st">&quot;Amount&quot;</span><span class="fu">,</span></span>
<span id="cb1-23"><a href="#cb1-23" aria-hidden="true" tabindex="-1"></a>                        <span class="dt">&quot;properties&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb1-24"><a href="#cb1-24" aria-hidden="true" tabindex="-1"></a>                                <span class="dt">&quot;JavaType&quot;</span><span class="fu">:</span> <span class="st">&quot;java.math.BigDecimal&quot;</span><span class="fu">,</span></span>
<span id="cb1-25"><a href="#cb1-25" aria-hidden="true" tabindex="-1"></a>                                <span class="dt">&quot;resourceId&quot;</span><span class="fu">:</span> <span class="st">&quot;expense_join.e.amount&quot;</span></span>
<span id="cb1-26"><a href="#cb1-26" aria-hidden="true" tabindex="-1"></a>                        <span class="fu">}</span></span>
<span id="cb1-27"><a href="#cb1-27" aria-hidden="true" tabindex="-1"></a>                    <span class="fu">}</span></span>
<span id="cb1-28"><a href="#cb1-28" aria-hidden="true" tabindex="-1"></a>                <span class="ot">]</span></span>
<span id="cb1-29"><a href="#cb1-29" aria-hidden="true" tabindex="-1"></a>            <span class="fu">}</span><span class="ot">,</span></span>
<span id="cb1-30"><a href="#cb1-30" aria-hidden="true" tabindex="-1"></a>            <span class="fu">{</span></span>
<span id="cb1-31"><a href="#cb1-31" aria-hidden="true" tabindex="-1"></a>                <span class="dt">&quot;id&quot;</span><span class="fu">:</span><span class="st">&quot;expense_join_store&quot;</span><span class="fu">,</span></span>
<span id="cb1-32"><a href="#cb1-32" aria-hidden="true" tabindex="-1"></a>                <span class="dt">&quot;label&quot;</span><span class="fu">:</span><span class="st">&quot;store&quot;</span><span class="fu">,</span></span>
<span id="cb1-33"><a href="#cb1-33" aria-hidden="true" tabindex="-1"></a>                <span class="dt">&quot;properties&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb1-34"><a href="#cb1-34" aria-hidden="true" tabindex="-1"></a>                        <span class="dt">&quot;resourceId&quot;</span><span class="fu">:</span><span class="st">&quot;expense_join&quot;</span></span>
<span id="cb1-35"><a href="#cb1-35" aria-hidden="true" tabindex="-1"></a>                <span class="fu">},</span></span>
<span id="cb1-36"><a href="#cb1-36" aria-hidden="true" tabindex="-1"></a>                <span class="dt">&quot;items&quot;</span><span class="fu">:</span><span class="ot">[</span></span>
<span id="cb1-37"><a href="#cb1-37" aria-hidden="true" tabindex="-1"></a>                    <span class="fu">{</span></span>
<span id="cb1-38"><a href="#cb1-38" aria-hidden="true" tabindex="-1"></a>                        <span class="dt">&quot;id&quot;</span><span class="fu">:</span><span class="st">&quot;ej_store_store_type&quot;</span><span class="fu">,</span></span>
<span id="cb1-39"><a href="#cb1-39" aria-hidden="true" tabindex="-1"></a>                        <span class="dt">&quot;label&quot;</span><span class="fu">:</span><span class="st">&quot;Store Type&quot;</span><span class="fu">,</span></span>
<span id="cb1-40"><a href="#cb1-40" aria-hidden="true" tabindex="-1"></a>                        <span class="dt">&quot;properties&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb1-41"><a href="#cb1-41" aria-hidden="true" tabindex="-1"></a>                                <span class="dt">&quot;JavaType&quot;</span><span class="fu">:</span> <span class="st">&quot;java.lang.String&quot;</span><span class="fu">,</span></span>
<span id="cb1-42"><a href="#cb1-42" aria-hidden="true" tabindex="-1"></a>                                <span class="dt">&quot;resourceId&quot;</span><span class="fu">:</span> <span class="st">&quot;expense_join.s.store_type&quot;</span></span>
<span id="cb1-43"><a href="#cb1-43" aria-hidden="true" tabindex="-1"></a>                        <span class="fu">}</span></span>
<span id="cb1-44"><a href="#cb1-44" aria-hidden="true" tabindex="-1"></a>                    <span class="fu">}</span><span class="ot">,</span></span>
<span id="cb1-45"><a href="#cb1-45" aria-hidden="true" tabindex="-1"></a>                    <span class="er">...</span></span>
<span id="cb1-46"><a href="#cb1-46" aria-hidden="true" tabindex="-1"></a>                <span class="ot">]</span></span>
<span id="cb1-47"><a href="#cb1-47" aria-hidden="true" tabindex="-1"></a>            <span class="fu">}</span></span>
<span id="cb1-48"><a href="#cb1-48" aria-hidden="true" tabindex="-1"></a>        <span class="ot">]</span></span>
<span id="cb1-49"><a href="#cb1-49" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span></span>
<span id="cb1-50"><a href="#cb1-50" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
</tbody>
</table>

The following example shows the same Domain as returned by the v2/domains/metadata service in XML format:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">&lt;?xml</span> <span class="ot">version=</span><span class="st">&quot;1.0&quot;</span> <span class="ot">encoding=</span><span class="st">&quot;UTF-8&quot;</span><span class="fu">?&gt;</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">domainMetadata</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">rootLevel</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">id</span>&gt;root&lt;/<span class="kw">id</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">subLevels</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">subLevel</span>&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>                &lt;<span class="kw">id</span>&gt;expense_join&lt;/<span class="kw">id</span>&gt;</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>                &lt;<span class="kw">label</span>&gt;expense&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>                &lt;<span class="kw">properties</span>&gt;</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>                    &lt;<span class="kw">entry</span>&gt;</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>                        &lt;<span class="kw">key</span>&gt;resourceId&lt;/<span class="kw">key</span>&gt;</span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>                        &lt;<span class="kw">value</span>&gt;expense_join&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>                    &lt;/<span class="kw">entry</span>&gt;</span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>                &lt;/<span class="kw">properties</span>&gt;</span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>                &lt;<span class="kw">items</span>&gt;</span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a>                    &lt;<span class="kw">item</span>&gt;</span>
<span id="cb1-17"><a href="#cb1-17" aria-hidden="true" tabindex="-1"></a>                        &lt;<span class="kw">id</span>&gt;ej_expense_fact_exp_date&lt;/<span class="kw">id</span>&gt;</span>
<span id="cb1-18"><a href="#cb1-18" aria-hidden="true" tabindex="-1"></a>                        &lt;<span class="kw">label</span>&gt;Exp Date&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb1-19"><a href="#cb1-19" aria-hidden="true" tabindex="-1"></a>                        &lt;<span class="kw">properties</span>&gt;</span>
<span id="cb1-20"><a href="#cb1-20" aria-hidden="true" tabindex="-1"></a>                            &lt;<span class="kw">entry</span>&gt;</span>
<span id="cb1-21"><a href="#cb1-21" aria-hidden="true" tabindex="-1"></a>                                &lt;<span class="kw">key</span>&gt;JavaType&lt;/<span class="kw">key</span>&gt;</span>
<span id="cb1-22"><a href="#cb1-22" aria-hidden="true" tabindex="-1"></a>                                &lt;<span class="kw">value</span>&gt;java.sql.Date&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-23"><a href="#cb1-23" aria-hidden="true" tabindex="-1"></a>                            &lt;/<span class="kw">entry</span>&gt;</span>
<span id="cb1-24"><a href="#cb1-24" aria-hidden="true" tabindex="-1"></a>                            &lt;<span class="kw">entry</span>&gt;</span>
<span id="cb1-25"><a href="#cb1-25" aria-hidden="true" tabindex="-1"></a>                                &lt;<span class="kw">key</span>&gt;resourceId&lt;/<span class="kw">key</span>&gt;</span>
<span id="cb1-26"><a href="#cb1-26" aria-hidden="true" tabindex="-1"></a>                                &lt;<span class="kw">value</span>&gt;expense_join.e.exp_date&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-27"><a href="#cb1-27" aria-hidden="true" tabindex="-1"></a>                            &lt;/<span class="kw">entry</span>&gt;</span>
<span id="cb1-28"><a href="#cb1-28" aria-hidden="true" tabindex="-1"></a>                        &lt;/<span class="kw">properties</span>&gt;</span>
<span id="cb1-29"><a href="#cb1-29" aria-hidden="true" tabindex="-1"></a>                    &lt;/<span class="kw">item</span>&gt;</span>
<span id="cb1-30"><a href="#cb1-30" aria-hidden="true" tabindex="-1"></a>                    &lt;<span class="kw">item</span>&gt;</span>
<span id="cb1-31"><a href="#cb1-31" aria-hidden="true" tabindex="-1"></a>                        &lt;<span class="kw">id</span>&gt;ej_expense_fact_amount&lt;/<span class="kw">id</span>&gt;</span>
<span id="cb1-32"><a href="#cb1-32" aria-hidden="true" tabindex="-1"></a>                        &lt;<span class="kw">label</span>&gt;Amount&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb1-33"><a href="#cb1-33" aria-hidden="true" tabindex="-1"></a>                        &lt;<span class="kw">properties</span>&gt;</span>
<span id="cb1-34"><a href="#cb1-34" aria-hidden="true" tabindex="-1"></a>                            &lt;<span class="kw">entry</span>&gt;</span>
<span id="cb1-35"><a href="#cb1-35" aria-hidden="true" tabindex="-1"></a>                                &lt;<span class="kw">key</span>&gt;JavaType&lt;/<span class="kw">key</span>&gt;</span>
<span id="cb1-36"><a href="#cb1-36" aria-hidden="true" tabindex="-1"></a>                                &lt;<span class="kw">value</span>&gt;java.math.BigDecimal&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-37"><a href="#cb1-37" aria-hidden="true" tabindex="-1"></a>                            &lt;/<span class="kw">entry</span>&gt;</span>
<span id="cb1-38"><a href="#cb1-38" aria-hidden="true" tabindex="-1"></a>                            &lt;<span class="kw">entry</span>&gt;</span>
<span id="cb1-39"><a href="#cb1-39" aria-hidden="true" tabindex="-1"></a>                                &lt;<span class="kw">key</span>&gt;resourceId&lt;/<span class="kw">key</span>&gt;</span>
<span id="cb1-40"><a href="#cb1-40" aria-hidden="true" tabindex="-1"></a>                                &lt;<span class="kw">value</span>&gt;expense_join.e.amount&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-41"><a href="#cb1-41" aria-hidden="true" tabindex="-1"></a>                            &lt;/<span class="kw">entry</span>&gt;</span>
<span id="cb1-42"><a href="#cb1-42" aria-hidden="true" tabindex="-1"></a>                        &lt;/<span class="kw">properties</span>&gt;</span>
<span id="cb1-43"><a href="#cb1-43" aria-hidden="true" tabindex="-1"></a>                    &lt;/<span class="kw">item</span>&gt;</span>
<span id="cb1-44"><a href="#cb1-44" aria-hidden="true" tabindex="-1"></a>                &lt;/<span class="kw">items</span>&gt;</span>
<span id="cb1-45"><a href="#cb1-45" aria-hidden="true" tabindex="-1"></a>            &lt;/<span class="kw">subLevel</span>&gt;</span>
<span id="cb1-46"><a href="#cb1-46" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">subLevel</span>&gt;</span>
<span id="cb1-47"><a href="#cb1-47" aria-hidden="true" tabindex="-1"></a>                &lt;<span class="kw">id</span>&gt;expense_join_store&lt;/<span class="kw">id</span>&gt;</span>
<span id="cb1-48"><a href="#cb1-48" aria-hidden="true" tabindex="-1"></a>                &lt;<span class="kw">label</span>&gt;store&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb1-49"><a href="#cb1-49" aria-hidden="true" tabindex="-1"></a>                &lt;<span class="kw">properties</span>&gt;</span>
<span id="cb1-50"><a href="#cb1-50" aria-hidden="true" tabindex="-1"></a>                    &lt;<span class="kw">entry</span>&gt;</span>
<span id="cb1-51"><a href="#cb1-51" aria-hidden="true" tabindex="-1"></a>                        &lt;<span class="kw">key</span>&gt;resourceId&lt;/<span class="kw">key</span>&gt;</span>
<span id="cb1-52"><a href="#cb1-52" aria-hidden="true" tabindex="-1"></a>                        &lt;<span class="kw">value</span>&gt;expense_join&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-53"><a href="#cb1-53" aria-hidden="true" tabindex="-1"></a>                    &lt;/<span class="kw">entry</span>&gt;</span>
<span id="cb1-54"><a href="#cb1-54" aria-hidden="true" tabindex="-1"></a>                &lt;/<span class="kw">properties</span>&gt;</span>
<span id="cb1-55"><a href="#cb1-55" aria-hidden="true" tabindex="-1"></a>                &lt;<span class="kw">items</span>&gt;</span>
<span id="cb1-56"><a href="#cb1-56" aria-hidden="true" tabindex="-1"></a>                    &lt;<span class="kw">item</span>&gt;</span>
<span id="cb1-57"><a href="#cb1-57" aria-hidden="true" tabindex="-1"></a>                        &lt;<span class="kw">id</span>&gt;ej_store_store_type&lt;/<span class="kw">id</span>&gt;</span>
<span id="cb1-58"><a href="#cb1-58" aria-hidden="true" tabindex="-1"></a>                        &lt;<span class="kw">label</span>&gt;Store Type&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb1-59"><a href="#cb1-59" aria-hidden="true" tabindex="-1"></a>                        &lt;<span class="kw">properties</span>&gt;</span>
<span id="cb1-60"><a href="#cb1-60" aria-hidden="true" tabindex="-1"></a>                            &lt;<span class="kw">entry</span>&gt;</span>
<span id="cb1-61"><a href="#cb1-61" aria-hidden="true" tabindex="-1"></a>                                &lt;<span class="kw">key</span>&gt;JavaType&lt;/<span class="kw">key</span>&gt;</span>
<span id="cb1-62"><a href="#cb1-62" aria-hidden="true" tabindex="-1"></a>                                &lt;<span class="kw">value</span>&gt;java.lang.String&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-63"><a href="#cb1-63" aria-hidden="true" tabindex="-1"></a>                            &lt;/<span class="kw">entry</span>&gt;</span>
<span id="cb1-64"><a href="#cb1-64" aria-hidden="true" tabindex="-1"></a>                            &lt;<span class="kw">entry</span>&gt;</span>
<span id="cb1-65"><a href="#cb1-65" aria-hidden="true" tabindex="-1"></a>                                &lt;<span class="kw">key</span>&gt;resourceId&lt;/<span class="kw">key</span>&gt;</span>
<span id="cb1-66"><a href="#cb1-66" aria-hidden="true" tabindex="-1"></a>                                &lt;<span class="kw">value</span>&gt;expense_join.s.store_type&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-67"><a href="#cb1-67" aria-hidden="true" tabindex="-1"></a>                            &lt;/<span class="kw">entry</span>&gt;</span>
<span id="cb1-68"><a href="#cb1-68" aria-hidden="true" tabindex="-1"></a>                        &lt;/<span class="kw">properties</span>&gt;</span>
<span id="cb1-69"><a href="#cb1-69" aria-hidden="true" tabindex="-1"></a>                    &lt;/<span class="kw">item</span>&gt;</span>
<span id="cb1-70"><a href="#cb1-70" aria-hidden="true" tabindex="-1"></a>                    ...</span>
<span id="cb1-71"><a href="#cb1-71" aria-hidden="true" tabindex="-1"></a>                &lt;/<span class="kw">items</span>&gt;</span>
<span id="cb1-72"><a href="#cb1-72" aria-hidden="true" tabindex="-1"></a>            &lt;/<span class="kw">subLevel</span>&gt;</span>
<span id="cb1-73"><a href="#cb1-73" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">subLevels</span>&gt;</span>
<span id="cb1-74"><a href="#cb1-74" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">rootLevel</span>&gt;</span>
<span id="cb1-75"><a href="#cb1-75" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">domainMetadata</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

.

## 1.1.1 Working with Domain Schemas

The v2/domains/metadata service returns only the display information about a Domain, not its internal definition. The fields, joins, filters, and calculated fields that define the internal structure of a Domain make up the Domain design. The XML representation of a Domain design is called the Domain schema.

Currently, there is no REST service to interact with Domain schemas, but you can use the v2/resources service to retrieve the raw schema. First, retrieve the resource descriptor for the Domain. For example, to view the descriptor for the Supermart Domain, use the following request (when logged in as jasperadmin):

GET http://\<host\>:\<port\>/jasperserver-pro/rest_v2/resources/Domains/supermartDomain

This descriptor contains the Domain schema as an internal resource:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">&lt;?xml</span> <span class="ot">version=</span><span class="st">&quot;1.0&quot;</span> <span class="ot">encoding=</span><span class="st">&quot;UTF-8&quot;</span> <span class="ot">standalone=</span><span class="st">&quot;yes&quot;</span><span class="fu">?&gt;</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">semanticLayerDataSource</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">creationDate</span>&gt;2013-10-10T15:30:31&lt;/<span class="kw">creationDate</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">description</span>&gt;Comprehensive example of Domain (pre-joined table sets for complex reporting, custom query based dataset, column and row security, I18n bundles)&lt;/<span class="kw">description</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">label</span>&gt;Supermart Domain&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">permissionMask</span>&gt;1&lt;/<span class="kw">permissionMask</span>&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">updateDate</span>&gt;2013-10-10T15:30:31&lt;/<span class="kw">updateDate</span>&gt;</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">uri</span>&gt;/organizations/organization_1/Domains/supermartDomain&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">version</span>&gt;1&lt;/<span class="kw">version</span>&gt;</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">dataSourceReference</span>&gt;</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">uri</span>&gt;/organizations/organization_1/analysis/datasources/FoodmartDataSourceJNDI&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">dataSourceReference</span>&gt;</span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">bundles</span>&gt;</span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">bundle</span>&gt;</span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">fileReference</span>&gt;&lt;<span class="kw">uri</span>&gt;/organizations/organization_1/Domains/supermartDomain_files/supermart_domain.properties&lt;/<span class="kw">uri</span>&gt;&lt;/<span class="kw">fileReference</span>&gt;</span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">locale</span>&gt;&lt;/<span class="kw">locale</span>&gt;</span>
<span id="cb1-17"><a href="#cb1-17" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">bundle</span>&gt;</span>
<span id="cb1-18"><a href="#cb1-18" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">bundle</span>&gt;</span>
<span id="cb1-19"><a href="#cb1-19" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">fileReference</span>&gt;&lt;<span class="kw">uri</span>&gt;/organizations/organization_1/Domains/supermartDomain_files/supermart_domain_en_US.properties&lt;/<span class="kw">uri</span>&gt;&lt;/<span class="kw">fileReference</span>&gt;</span>
<span id="cb1-20"><a href="#cb1-20" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">locale</span>&gt;en_US&lt;/<span class="kw">locale</span>&gt;</span>
<span id="cb1-21"><a href="#cb1-21" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">bundle</span>&gt;</span>
<span id="cb1-22"><a href="#cb1-22" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">bundle</span>&gt;</span>
<span id="cb1-23"><a href="#cb1-23" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">fileReference</span>&gt;&lt;<span class="kw">uri</span>&gt;/organizations/organization_1/Domains/supermartDomain_files/supermart_domain_de.properties&lt;/<span class="kw">uri</span>&gt;&lt;/<span class="kw">fileReference</span>&gt;</span>
<span id="cb1-24"><a href="#cb1-24" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">locale</span>&gt;de&lt;/<span class="kw">locale</span>&gt;</span>
<span id="cb1-25"><a href="#cb1-25" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">bundle</span>&gt;</span>
<span id="cb1-26"><a href="#cb1-26" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">bundle</span>&gt;</span>
<span id="cb1-27"><a href="#cb1-27" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">fileReference</span>&gt;&lt;<span class="kw">uri</span>&gt;/organizations/organization_1/Domains/supermartDomain_files/supermart_domain_fr.properties&lt;/<span class="kw">uri</span>&gt;&lt;/<span class="kw">fileReference</span>&gt;</span>
<span id="cb1-28"><a href="#cb1-28" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">locale</span>&gt;fr&lt;/<span class="kw">locale</span>&gt;</span>
<span id="cb1-29"><a href="#cb1-29" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">bundle</span>&gt;</span>
<span id="cb1-30"><a href="#cb1-30" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">bundle</span>&gt;</span>
<span id="cb1-31"><a href="#cb1-31" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">fileReference</span>&gt;&lt;<span class="kw">uri</span>&gt;/organizations/organization_1/Domains/supermartDomain_files/supermart_domain_es.properties&lt;/<span class="kw">uri</span>&gt;&lt;/<span class="kw">fileReference</span>&gt;</span>
<span id="cb1-32"><a href="#cb1-32" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">locale</span>&gt;es&lt;/<span class="kw">locale</span>&gt;</span>
<span id="cb1-33"><a href="#cb1-33" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">bundle</span>&gt;</span>
<span id="cb1-34"><a href="#cb1-34" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">bundle</span>&gt;</span>
<span id="cb1-35"><a href="#cb1-35" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">fileReference</span>&gt;&lt;<span class="kw">uri</span>&gt;/organizations/organization_1/Domains/supermartDomain_files/supermart_domain_ja.properties&lt;/<span class="kw">uri</span>&gt;&lt;/<span class="kw">fileReference</span>&gt;</span>
<span id="cb1-36"><a href="#cb1-36" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">locale</span>&gt;ja&lt;/<span class="kw">locale</span>&gt;</span>
<span id="cb1-37"><a href="#cb1-37" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">bundle</span>&gt;</span>
<span id="cb1-38"><a href="#cb1-38" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">bundle</span>&gt;</span>
<span id="cb1-39"><a href="#cb1-39" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">fileReference</span>&gt;&lt;<span class="kw">uri</span>&gt;/organizations/organization_1/Domains/supermartDomain_files/supermart_domain_zh_CN.properties&lt;/<span class="kw">uri</span>&gt;&lt;/<span class="kw">fileReference</span>&gt;</span>
<span id="cb1-40"><a href="#cb1-40" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">locale</span>&gt;zh_CN&lt;/<span class="kw">locale</span>&gt;</span>
<span id="cb1-41"><a href="#cb1-41" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">bundle</span>&gt;</span>
<span id="cb1-42"><a href="#cb1-42" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">bundles</span>&gt;</span>
<span id="cb1-43"><a href="#cb1-43" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">schemaFileReference</span>&gt;</span>
<span id="cb1-44"><a href="#cb1-44" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">uri</span>&gt;/organizations/organization_1/Domains/supermartDomain_files/supermartDomain_schema&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb1-45"><a href="#cb1-45" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">schemaFileReference</span>&gt;</span>
<span id="cb1-46"><a href="#cb1-46" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">securityFileReference</span>&gt;</span>
<span id="cb1-47"><a href="#cb1-47" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">uri</span>&gt;/organizations/organization_1/Domains/supermartDomain_files/supermartDomain_domain_security&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb1-48"><a href="#cb1-48" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">securityFileReference</span>&gt;</span>
<span id="cb1-49"><a href="#cb1-49" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">semanticLayerDataSource</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

Use the following request to access the Domain schema file inside the Domain resource:

GET http://\<host\>:\<port\>/jasperserver-pro/rest_v2/resources/Domains/supermartDomain_files/supermartDomain_schema

The Domain schema is an XML file with a structure explained in the JasperReports® Server User Guide. If you wish to modify the schema programmatically, you must write your own parser to access its fields and definitions. You can then replace the schema file in the Domain with one of the file updating methods described in [“Uploading File Resources” on page 1](uploading_file_resources.md).

## 1.1.2 Accessing Domain Bundles and Security Files

Once you have the descriptor of a Domain resource as shown in the previous section, you can access the other files that help define a Domain. For example, you can access the language bundles of the Supermart Domain with the following request:

GET http://\<host\>:\<port\>/jasperserver-pro/rest_v2/resources/Domains/supermartDomain_files/supermart_domain\_\<locale\>.properties

Language bundles are Java properties files that follow the language bundle naming convention, and that contain the names of the sets and fields in the language of the locale in the filename.

You can also retrieve the localized set and item names by specifying Accept-Language when using the v2/domains/metadat service. However, by accessing the language bundles through the Domain descriptor, you read the default bundle to see the pattern of keys and values, and then create a bundle for a new locale.

Domains may also contain a security file that is also stored as an internal resource of the Domain descriptor. Use the following example to request the security file of the Supermart Domain in the sample data:

GET http://\<host\>:\<port\>/jasperserver-pro/rest_v2/resources/Domains/supermartDomain_files/supermart_domain_security

A security file defines a complex set of access permissions to the data in the rows and columns returned by the Domain, based on the username, roles, or profile attributes of the user running a Domain-based report. As with the Domain schema file, you must write your own parser to interpret this file and modify it.

You can then upload an updated language bundle or security file for the Domain with one of the methods described in .

For more information about language bundles and security files in Domains, see the JasperReports® Server User Guide.
