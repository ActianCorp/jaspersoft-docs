---
title: JRXML Sources and Jasper Files
description: "JasperReports defines a report with an jrdax file. A jrxml file is composed of a set of sections:"
---

# JRXML Sources and Jasper Files

JasperReports defines a report with an jrdax file. A `jrxml` file is composed of a set of sections:

- some concerned with the report’s physical characteristics (such as the dimensions of the page, positioning of the fields, and height of the bands).

- some concerned with the logical characteristics (such as the declaration of the parameters and variables and the definition of a query for data selection).

## The Report Lifecycle

The life cycle of a JasperReport is divided into two phases:

- Report development: designing and planning the report, creating a JRXML file, and compiling a Jasper file from the JRXML.
- Report execution: loading the Jasper file, filling the report, and exporting the output (a Jasper print object) in a final format.

Jaspersoft Studio is primarily focused on report development, though it is able to preview the results and export it in all the supported formats. Jaspersoft Studio supports a wide range of data sources and allows users to create custom data sources, thereby becoming a complete environment for report development and testing.

When you design a report, you specify where the data comes from, how it is positioned on the page, and additional functionality, such as parameters for input controls or complex formulas to perform calculations. The result is a template, similar to a form containing blank space that is filled with data when the report is run. The template is stored in a JRXML file, which is an XML document that contains the definition of the report layout and design.

Before running a report, the JRXML must be compiled in a binary object called a Jasper file. Jasper files are what you need to include your application to run the reports.

Report execution is performed by passing a Jasper file and a data source to JasperReports. There are many data source types. You can fill a Jasper file from an SQL query, an jrdax file, a .csv file, an HQL (Hibernate Query Language) query, a collection of JavaBeans, and others. If you do not have a suitable data source, JasperReports allows you to write your own custom data source. With a Jasper file and a data source, JasperReports is able to generate the final document in the format you want.

Jaspersoft Studio also lets you configure data sources and use them to test your reports. In many cases, data-driven wizards can help you design your reports much quicker. Jaspersoft Studio includes the JasperReports engine itself to let you preview your report output, test, and refine your reports.

The following table shows sample report source code.

<table>
<caption><p>A simple JRMXL file example</p></caption>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">&lt;?xml</span> <span class="ot">version=</span><span class="st">&quot;1.0&quot;</span> <span class="ot">encoding=</span><span class="st">&quot;UTF-8&quot;</span><span class="fu">?&gt;</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">jasperReport</span> <span class="ot">xmlns=</span><span class="st">&quot;http://jasperreports.sourceforge.net/jasperreports&quot;</span> </span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>      <span class="ot">xsi:schemaLocation=</span><span class="st">&quot;http://jasperreports.sourceforge.net/jasperreports </span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="st">        http://jasperreports.sourceforge.net/xsd/jasperreport.xsd&quot;</span> </span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>      <span class="ot">name=</span><span class="st">&quot;My first report&quot;</span> <span class="ot">pageWidth=</span><span class="st">&quot;595&quot;</span> <span class="ot">pageHeight=</span><span class="st">&quot;842&quot;</span> <span class="ot">columnWidth=</span><span class="st">&quot;535&quot;</span> </span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>      <span class="ot">leftMargin=</span><span class="st">&quot;20&quot;</span> <span class="ot">rightMargin=</span><span class="st">&quot;20&quot;</span> <span class="ot">topMargin=</span><span class="st">&quot;20&quot;</span> <span class="ot">bottomMargin=</span><span class="st">&quot;20&quot;</span>&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">queryString</span> <span class="ot">language=</span><span class="st">&quot;SQL&quot;</span>&gt;</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    <span class="bn">&lt;![CDATA[</span>select * from address order by city<span class="bn">]]&gt;</span></span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">queryString</span>&gt;</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">field</span> <span class="ot">name=</span><span class="st">&quot;ID&quot;</span> <span class="ot">class=</span><span class="st">&quot;java.lang.Integer&quot;</span>&gt;</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">fieldDescription</span>&gt;<span class="bn">&lt;![CDATA[]]&gt;</span>&lt;/<span class="kw">fieldDescription</span>&gt;</span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">field</span>&gt;</span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">field</span> <span class="ot">name=</span><span class="st">&quot;FIRSTNAME&quot;</span> <span class="ot">class=</span><span class="st">&quot;java.lang.String&quot;</span>&gt;</span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">fieldDescription</span>&gt;<span class="bn">&lt;![CDATA[]]&gt;</span>&lt;/<span class="kw">fieldDescription</span>&gt;</span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">field</span>&gt;</span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">field</span> <span class="ot">name=</span><span class="st">&quot;LASTNAME&quot;</span> <span class="ot">class=</span><span class="st">&quot;java.lang.String&quot;</span>&gt;</span>
<span id="cb1-17"><a href="#cb1-17" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">fieldDescription</span>&gt;<span class="bn">&lt;![CDATA[]]&gt;</span>&lt;/<span class="kw">fieldDescription</span>&gt;</span>
<span id="cb1-18"><a href="#cb1-18" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">field</span>&gt;    </span>
<span id="cb1-19"><a href="#cb1-19" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">field</span> <span class="ot">name=</span><span class="st">&quot;STREET&quot;</span> <span class="ot">class=</span><span class="st">&quot;java.lang.String&quot;</span>&gt;</span>
<span id="cb1-20"><a href="#cb1-20" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">fieldDescription</span>&gt;<span class="bn">&lt;![CDATA[]]&gt;</span>&lt;/<span class="kw">fieldDescription</span>&gt;</span>
<span id="cb1-21"><a href="#cb1-21" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">field</span>&gt;</span>
<span id="cb1-22"><a href="#cb1-22" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">field</span> <span class="ot">name=</span><span class="st">&quot;CITY&quot;</span> <span class="ot">class=</span><span class="st">&quot;java.lang.String&quot;</span>&gt;</span>
<span id="cb1-23"><a href="#cb1-23" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">fieldDescription</span>&gt;<span class="bn">&lt;![CDATA[]]&gt;</span>&lt;/<span class="kw">fieldDescription</span>&gt;</span>
<span id="cb1-24"><a href="#cb1-24" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">field</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">group</span> <span class="ot">name=</span><span class="st">&quot;CITY&quot;</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">groupExpression</span>&gt;<span class="bn">&lt;![CDATA[</span>$F{CITY}<span class="bn">]]&gt;</span>&lt;/<span class="kw">groupExpression</span>&gt;</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">groupHeader</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">band</span> <span class="ot">height=</span><span class="st">&quot;27&quot;</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">staticText</span>&gt;</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">reportElement</span> <span class="ot">mode=</span><span class="st">&quot;Opaque&quot;</span> <span class="ot">x=</span><span class="st">&quot;0&quot;</span> <span class="ot">y=</span><span class="st">&quot;0&quot;</span> <span class="ot">width=</span><span class="st">&quot;139&quot;</span> <span class="ot">height=</span><span class="st">&quot;27&quot;</span> </span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>          <span class="ot">forecolor=</span><span class="st">&quot;#FFFFFF&quot;</span> <span class="ot">backcolor=</span><span class="st">&quot;#000000&quot;</span>/&gt;</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">textElement</span>&gt;</span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">font</span> <span class="ot">size=</span><span class="st">&quot;18&quot;</span>/&gt;</span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a>          &lt;/<span class="kw">textElement</span>&gt;</span>
<span id="cb2-11"><a href="#cb2-11" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">text</span>&gt;<span class="bn">&lt;![CDATA[</span>CITY<span class="bn">]]&gt;</span>&lt;/<span class="kw">text</span>&gt;</span>
<span id="cb2-12"><a href="#cb2-12" aria-hidden="true" tabindex="-1"></a>      &lt;/<span class="kw">staticText</span>&gt;</span>
<span id="cb2-13"><a href="#cb2-13" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb2-14"><a href="#cb2-14" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">textField</span> <span class="ot">hyperlinkType=</span><span class="st">&quot;None&quot;</span>&gt;</span>
<span id="cb2-15"><a href="#cb2-15" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">reportElement</span> <span class="ot">mode=</span><span class="st">&quot;Opaque&quot;</span> <span class="ot">x=</span><span class="st">&quot;139&quot;</span> <span class="ot">y=</span><span class="st">&quot;0&quot;</span> <span class="ot">width=</span><span class="st">&quot;416&quot;</span> <span class="ot">height=</span><span class="st">&quot;27&quot;</span> </span>
<span id="cb2-16"><a href="#cb2-16" aria-hidden="true" tabindex="-1"></a>        <span class="ot">forecolor=</span><span class="st">&quot;#FFFFFF&quot;</span> <span class="ot">backcolor=</span><span class="st">&quot;#000000&quot;</span>/&gt;</span>
<span id="cb2-17"><a href="#cb2-17" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">textElement</span>&gt;</span>
<span id="cb2-18"><a href="#cb2-18" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">font</span> <span class="ot">size=</span><span class="st">&quot;18&quot;</span> <span class="ot">isBold=</span><span class="st">&quot;true&quot;</span>/&gt;</span>
<span id="cb2-19"><a href="#cb2-19" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">textElement</span>&gt;</span>
<span id="cb2-20"><a href="#cb2-20" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">textFieldExpression</span> <span class="ot">class=</span><span class="st">&quot;java.lang.String&quot;</span>&gt;<span class="bn">&lt;![CDATA[</span>$F{CITY}<span class="bn">]]&gt;</span></span>
<span id="cb2-21"><a href="#cb2-21" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">textFieldExpression</span>&gt;</span>
<span id="cb2-22"><a href="#cb2-22" aria-hidden="true" tabindex="-1"></a>      &lt;/<span class="kw">textField</span>&gt;</span>
<span id="cb2-23"><a href="#cb2-23" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">band</span>&gt;</span>
<span id="cb2-24"><a href="#cb2-24" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">groupHeader</span>&gt;</span>
<span id="cb2-25"><a href="#cb2-25" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">groupFooter</span>&gt;</span>
<span id="cb2-26"><a href="#cb2-26" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">band</span> <span class="ot">height=</span><span class="st">&quot;8&quot;</span>&gt;</span>
<span id="cb2-27"><a href="#cb2-27" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">line</span> <span class="ot">direction=</span><span class="st">&quot;BottomUp&quot;</span>&gt;</span>
<span id="cb2-28"><a href="#cb2-28" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">reportElement</span> <span class="ot">key=</span><span class="st">&quot;line&quot;</span> <span class="ot">x=</span><span class="st">&quot;1&quot;</span> <span class="ot">y=</span><span class="st">&quot;4&quot;</span> <span class="ot">width=</span><span class="st">&quot;554&quot;</span> <span class="ot">height=</span><span class="st">&quot;1&quot;</span>/&gt;</span>
<span id="cb2-29"><a href="#cb2-29" aria-hidden="true" tabindex="-1"></a>      &lt;/<span class="kw">line</span>&gt;</span>
<span id="cb2-30"><a href="#cb2-30" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">band</span>&gt;</span>
<span id="cb2-31"><a href="#cb2-31" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">groupFooter</span>&gt;</span>
<span id="cb2-32"><a href="#cb2-32" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">group</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td><div class="sourceCode" id="cb3"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">background</span>&gt;</span>
<span id="cb3-2"><a href="#cb3-2" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">band</span>/&gt;</span>
<span id="cb3-3"><a href="#cb3-3" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">background</span>&gt;</span>
<span id="cb3-4"><a href="#cb3-4" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">title</span>&gt;</span>
<span id="cb3-5"><a href="#cb3-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">band</span> <span class="ot">height=</span><span class="st">&quot;58&quot;</span>&gt;</span>
<span id="cb3-6"><a href="#cb3-6" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">line</span>&gt;</span>
<span id="cb3-7"><a href="#cb3-7" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">reportElement</span> <span class="ot">x=</span><span class="st">&quot;0&quot;</span> <span class="ot">y=</span><span class="st">&quot;8&quot;</span> <span class="ot">width=</span><span class="st">&quot;555&quot;</span> <span class="ot">height=</span><span class="st">&quot;1&quot;</span>/&gt;</span>
<span id="cb3-8"><a href="#cb3-8" aria-hidden="true" tabindex="-1"></a>      &lt;/<span class="kw">line</span>&gt;</span>
<span id="cb3-9"><a href="#cb3-9" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">line</span>&gt;</span>
<span id="cb3-10"><a href="#cb3-10" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">reportElement</span> <span class="ot">positionType=</span><span class="st">&quot;FixRelativeToBottom&quot;</span> <span class="ot">x=</span><span class="st">&quot;0&quot;</span> <span class="ot">y=</span><span class="st">&quot;51&quot;</span> <span class="ot">width=</span><span class="st">&quot;555&quot;</span> </span>
<span id="cb3-11"><a href="#cb3-11" aria-hidden="true" tabindex="-1"></a>             <span class="ot">height=</span><span class="st">&quot;1&quot;</span>/&gt;</span>
<span id="cb3-12"><a href="#cb3-12" aria-hidden="true" tabindex="-1"></a>      &lt;/<span class="kw">line</span>&gt;</span>
<span id="cb3-13"><a href="#cb3-13" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb3-14"><a href="#cb3-14" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">staticText</span>&gt;</span>
<span id="cb3-15"><a href="#cb3-15" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">reportElement</span> <span class="ot">x=</span><span class="er">”65</span>” y=”13” width ”424” height=”35”/&gt;</span>
<span id="cb3-16"><a href="#cb3-16" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">textElement</span> <span class="ot">textAlignment=</span><span class="er">”Center</span>”&gt;</span>
<span id="cb3-17"><a href="#cb3-17" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">font</span> <span class="ot">size=</span><span class="er">”26</span>” isBold=”true”/&gt;</span>
<span id="cb3-18"><a href="#cb3-18" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">textElement</span>&gt;</span>
<span id="cb3-19"><a href="#cb3-19" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">text</span>&gt;<span class="bn">&lt;![CDATA[</span>Classic template<span class="bn">]]&gt;</span> &lt;/<span class="kw">text</span>&gt;</span>
<span id="cb3-20"><a href="#cb3-20" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">staticText</span>&gt;</span>
<span id="cb3-21"><a href="#cb3-21" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">band</span>&gt;</span>
<span id="cb3-22"><a href="#cb3-22" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">title</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td><div class="sourceCode" id="cb4"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb4-1"><a href="#cb4-1" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">pageHeader</span>&gt;</span>
<span id="cb4-2"><a href="#cb4-2" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">band</span>/&gt;</span>
<span id="cb4-3"><a href="#cb4-3" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">pageHeader</span>&gt;</span>
<span id="cb4-4"><a href="#cb4-4" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">columnHeader</span>&gt;</span>
<span id="cb4-5"><a href="#cb4-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">band</span> <span class="ot">height=</span><span class="st">&quot;18&quot;</span>&gt;</span>
<span id="cb4-6"><a href="#cb4-6" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">staticText</span>&gt;</span>
<span id="cb4-7"><a href="#cb4-7" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">reportElement</span> <span class="ot">mode=</span><span class="st">&quot;Opaque&quot;</span> <span class="ot">x=</span><span class="st">&quot;0&quot;</span> <span class="ot">y=</span><span class="st">&quot;0&quot;</span> <span class="ot">width=</span><span class="st">&quot;138&quot;</span> <span class="ot">height=</span><span class="st">&quot;18&quot;</span> </span>
<span id="cb4-8"><a href="#cb4-8" aria-hidden="true" tabindex="-1"></a>        <span class="ot">forecolor=</span><span class="st">&quot;#FFFFFF&quot;</span> <span class="ot">backcolor=</span><span class="st">&quot;#999999&quot;</span>/&gt;</span>
<span id="cb4-9"><a href="#cb4-9" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">textElement</span>&gt;</span>
<span id="cb4-10"><a href="#cb4-10" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">font</span> <span class="ot">size=</span><span class="st">&quot;12&quot;</span>/&gt;</span>
<span id="cb4-11"><a href="#cb4-11" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">textElement</span>&gt;</span>
<span id="cb4-12"><a href="#cb4-12" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">text</span>&gt;<span class="bn">&lt;![CDATA[</span>ID<span class="bn">]]&gt;</span>&lt;/<span class="kw">text</span>&gt;</span>
<span id="cb4-13"><a href="#cb4-13" aria-hidden="true" tabindex="-1"></a>      &lt;/<span class="kw">staticText</span>&gt;</span>
<span id="cb4-14"><a href="#cb4-14" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">staticText</span>&gt;</span>
<span id="cb4-15"><a href="#cb4-15" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">reportElement</span> <span class="ot">mode=</span><span class="st">&quot;Opaque&quot;</span> <span class="ot">x=</span><span class="st">&quot;138&quot;</span> <span class="ot">y=</span><span class="st">&quot;0&quot;</span> <span class="ot">width=</span><span class="st">&quot;138&quot;</span> <span class="ot">height=</span><span class="st">&quot;18&quot;</span> </span>
<span id="cb4-16"><a href="#cb4-16" aria-hidden="true" tabindex="-1"></a>        <span class="ot">forecolor=</span><span class="st">&quot;#FFFFFF&quot;</span> <span class="ot">backcolor=</span><span class="st">&quot;#999999&quot;</span>/&gt;</span>
<span id="cb4-17"><a href="#cb4-17" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">textElement</span>&gt;</span>
<span id="cb4-18"><a href="#cb4-18" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">font</span> <span class="ot">size=</span><span class="st">&quot;12&quot;</span>/&gt;</span>
<span id="cb4-19"><a href="#cb4-19" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">textElement</span>&gt;</span>
<span id="cb4-20"><a href="#cb4-20" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">text</span>&gt;<span class="bn">&lt;![CDATA[</span>FIRSTNAME<span class="bn">]]&gt;</span>&lt;/<span class="kw">text</span>&gt;</span>
<span id="cb4-21"><a href="#cb4-21" aria-hidden="true" tabindex="-1"></a>      &lt;/<span class="kw">staticText</span>&gt;</span>
<span id="cb4-22"><a href="#cb4-22" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">staticText</span>&gt;</span>
<span id="cb4-23"><a href="#cb4-23" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">reportElement</span> <span class="ot">mode=</span><span class="st">&quot;Opaque&quot;</span> <span class="ot">x=</span><span class="st">&quot;276&quot;</span> <span class="ot">y=</span><span class="st">&quot;0&quot;</span> <span class="ot">width=</span><span class="st">&quot;138&quot;</span> <span class="ot">height=</span><span class="st">&quot;18&quot;</span> </span>
<span id="cb4-24"><a href="#cb4-24" aria-hidden="true" tabindex="-1"></a>        <span class="ot">forecolor=</span><span class="st">&quot;#FFFFFF&quot;</span> <span class="ot">backcolor=</span><span class="st">&quot;#999999&quot;</span>/&gt;</span>
<span id="cb4-25"><a href="#cb4-25" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">textElement</span>&gt;</span>
<span id="cb4-26"><a href="#cb4-26" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">font</span> <span class="ot">size=</span><span class="st">&quot;12&quot;</span>/&gt;</span>
<span id="cb4-27"><a href="#cb4-27" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">textElement</span>&gt;</span>
<span id="cb4-28"><a href="#cb4-28" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">text</span>&gt;<span class="bn">&lt;![CDATA[</span>LASTNAME<span class="bn">]]&gt;</span>&lt;/<span class="kw">text</span>&gt;</span>
<span id="cb4-29"><a href="#cb4-29" aria-hidden="true" tabindex="-1"></a>      &lt;/<span class="kw">staticText</span>&gt;</span>
<span id="cb4-30"><a href="#cb4-30" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">staticText</span>&gt;</span>
<span id="cb4-31"><a href="#cb4-31" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">reportElement</span> <span class="ot">mode=</span><span class="st">&quot;Opaque&quot;</span> <span class="ot">x=</span><span class="st">&quot;414&quot;</span> <span class="ot">y=</span><span class="st">&quot;0&quot;</span> <span class="ot">width=</span><span class="st">&quot;138&quot;</span> <span class="ot">height=</span><span class="st">&quot;18&quot;</span> </span>
<span id="cb4-32"><a href="#cb4-32" aria-hidden="true" tabindex="-1"></a>        <span class="ot">forecolor=</span><span class="st">&quot;#FFFFFF&quot;</span> <span class="ot">backcolor=</span><span class="st">&quot;#999999&quot;</span>/&gt;</span>
<span id="cb4-33"><a href="#cb4-33" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">textElement</span>&gt;</span>
<span id="cb4-34"><a href="#cb4-34" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">font</span> <span class="ot">size=</span><span class="st">&quot;12&quot;</span>/&gt;</span>
<span id="cb4-35"><a href="#cb4-35" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">textElement</span>&gt;</span>
<span id="cb4-36"><a href="#cb4-36" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">text</span>&gt;<span class="bn">&lt;![CDATA[</span>STREET<span class="bn">]]&gt;</span>&lt;/<span class="kw">text</span>&gt;</span>
<span id="cb4-37"><a href="#cb4-37" aria-hidden="true" tabindex="-1"></a>      &lt;/<span class="kw">staticText</span>&gt;</span>
<span id="cb4-38"><a href="#cb4-38" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">band</span>&gt;</span>
<span id="cb4-39"><a href="#cb4-39" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">columnHeader</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td><div class="sourceCode" id="cb5"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb5-1"><a href="#cb5-1" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">detail</span>&gt;</span>
<span id="cb5-2"><a href="#cb5-2" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">band</span> <span class="ot">height=</span><span class="st">&quot;20&quot;</span>&gt;</span>
<span id="cb5-3"><a href="#cb5-3" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">textField</span> <span class="ot">hyperlinkType=</span><span class="st">&quot;None&quot;</span>&gt;</span>
<span id="cb5-4"><a href="#cb5-4" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">reportElement</span> <span class="ot">x=</span><span class="st">&quot;0&quot;</span> <span class="ot">y=</span><span class="st">&quot;0&quot;</span> <span class="ot">width=</span><span class="st">&quot;138&quot;</span> <span class="ot">height=</span><span class="st">&quot;20&quot;</span>/&gt;</span>
<span id="cb5-5"><a href="#cb5-5" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">textElement</span>&gt;</span>
<span id="cb5-6"><a href="#cb5-6" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">font</span> <span class="ot">size=</span><span class="st">&quot;12&quot;</span>/&gt;</span>
<span id="cb5-7"><a href="#cb5-7" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">textElement</span>&gt;</span>
<span id="cb5-8"><a href="#cb5-8" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">textFieldExpression</span> <span class="ot">class=</span><span class="st">&quot;java.lang.Integer&quot;</span>&gt;<span class="bn">&lt;![CDATA[</span>$F{ID}<span class="bn">]]&gt;</span></span>
<span id="cb5-9"><a href="#cb5-9" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">textFieldExpression</span>&gt;</span>
<span id="cb5-10"><a href="#cb5-10" aria-hidden="true" tabindex="-1"></a>      &lt;/<span class="kw">textField</span>&gt;</span>
<span id="cb5-11"><a href="#cb5-11" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">textField</span> <span class="ot">hyperlinkType=</span><span class="st">&quot;None&quot;</span>&gt;</span>
<span id="cb5-12"><a href="#cb5-12" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">reportElement</span> <span class="ot">x=</span><span class="st">&quot;138&quot;</span> <span class="ot">y=</span><span class="st">&quot;0&quot;</span> <span class="ot">width=</span><span class="st">&quot;138&quot;</span> <span class="ot">height=</span><span class="st">&quot;20&quot;</span>/&gt;</span>
<span id="cb5-13"><a href="#cb5-13" aria-hidden="true" tabindex="-1"></a>      &lt;/<span class="kw">textField</span>&gt;</span>
<span id="cb5-14"><a href="#cb5-14" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">textElement</span>&gt;</span>
<span id="cb5-15"><a href="#cb5-15" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">font</span> <span class="ot">size=</span><span class="st">&quot;12&quot;</span>/&gt;</span>
<span id="cb5-16"><a href="#cb5-16" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">textElement</span>&gt;</span>
<span id="cb5-17"><a href="#cb5-17" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">textFieldExpression</span> <span class="ot">class=</span><span class="st">&quot;java.lang.String&quot;</span>&gt;<span class="bn">&lt;![CDATA[</span>$F{FIRSTNAME}<span class="bn">]]&gt;</span></span>
<span id="cb5-18"><a href="#cb5-18" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">textFieldExpression</span>&gt;</span>
<span id="cb5-19"><a href="#cb5-19" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">textField</span> <span class="ot">hyperlinkType=</span><span class="st">&quot;None&quot;</span>&gt;</span>
<span id="cb5-20"><a href="#cb5-20" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">reportElement</span> <span class="ot">x=</span><span class="st">&quot;276&quot;</span> <span class="ot">y=</span><span class="st">&quot;0&quot;</span> <span class="ot">width=</span><span class="st">&quot;138&quot;</span> <span class="ot">height=</span><span class="st">&quot;20&quot;</span>/&gt;</span>
<span id="cb5-21"><a href="#cb5-21" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">textElement</span>&gt;</span>
<span id="cb5-22"><a href="#cb5-22" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">font</span> <span class="ot">size=</span><span class="st">&quot;12&quot;</span>/&gt;</span>
<span id="cb5-23"><a href="#cb5-23" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">textElement</span>&gt;</span>
<span id="cb5-24"><a href="#cb5-24" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">textFieldExpression</span> <span class="ot">class=</span><span class="st">&quot;java.lang.String&quot;</span>&gt;<span class="bn">&lt;![CDATA[</span>$F{LASTNAME}<span class="bn">]]&gt;</span></span>
<span id="cb5-25"><a href="#cb5-25" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">textFieldExpression</span>&gt;</span>
<span id="cb5-26"><a href="#cb5-26" aria-hidden="true" tabindex="-1"></a>      &lt;/<span class="kw">textField</span>&gt;</span>
<span id="cb5-27"><a href="#cb5-27" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">textField</span> <span class="ot">hyperlinkType=</span><span class="st">&quot;None&quot;</span>&gt;</span>
<span id="cb5-28"><a href="#cb5-28" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">reportElement</span> <span class="ot">x=</span><span class="st">&quot;414&quot;</span> <span class="ot">y=</span><span class="st">&quot;0&quot;</span> <span class="ot">width=</span><span class="st">&quot;138&quot;</span> <span class="ot">height=</span><span class="st">&quot;20&quot;</span>/&gt;</span>
<span id="cb5-29"><a href="#cb5-29" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">textElement</span>&gt;</span>
<span id="cb5-30"><a href="#cb5-30" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">font</span> <span class="ot">size=</span><span class="st">&quot;12&quot;</span>/&gt;</span>
<span id="cb5-31"><a href="#cb5-31" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">textElement</span>&gt;</span>
<span id="cb5-32"><a href="#cb5-32" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">textFieldExpression</span> <span class="ot">class=</span><span class="st">&quot;java.lang.String&quot;</span>&gt;<span class="bn">&lt;![CDATA[</span>$F{STREET}<span class="bn">]]&gt;</span></span>
<span id="cb5-33"><a href="#cb5-33" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">textFieldExpression</span>&gt;</span>
<span id="cb5-34"><a href="#cb5-34" aria-hidden="true" tabindex="-1"></a>      &lt;/<span class="kw">textField</span>&gt;</span>
<span id="cb5-35"><a href="#cb5-35" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">band</span>&gt;</span>
<span id="cb5-36"><a href="#cb5-36" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">detail</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td><div class="sourceCode" id="cb6"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb6-1"><a href="#cb6-1" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">columnFooter</span>&gt;</span>
<span id="cb6-2"><a href="#cb6-2" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">band</span>/&gt;</span>
<span id="cb6-3"><a href="#cb6-3" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">columnFooter</span>&gt;</span>
<span id="cb6-4"><a href="#cb6-4" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">pageFooter</span>&gt;</span>
<span id="cb6-5"><a href="#cb6-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">band</span> <span class="ot">height=</span><span class="st">&quot;26&quot;</span>&gt;</span>
<span id="cb6-6"><a href="#cb6-6" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">textField</span> <span class="ot">evaluationTime=</span><span class="st">&quot;Report&quot;</span> <span class="ot">pattern=</span><span class="st">&quot;&quot;</span> <span class="ot">isBlankWhenNull=</span><span class="st">&quot;false&quot;</span> </span>
<span id="cb6-7"><a href="#cb6-7" aria-hidden="true" tabindex="-1"></a>      <span class="ot">hyperlinkType=</span><span class="st">&quot;None&quot;</span>&gt;</span>
<span id="cb6-8"><a href="#cb6-8" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">reportElement</span> <span class="ot">key=</span><span class="st">&quot;textField&quot;</span> <span class="ot">x=</span><span class="st">&quot;516&quot;</span> <span class="ot">y=</span><span class="st">&quot;6&quot;</span> <span class="ot">width=</span><span class="st">&quot;36&quot;</span> <span class="ot">height=</span><span class="st">&quot;19&quot;</span> </span>
<span id="cb6-9"><a href="#cb6-9" aria-hidden="true" tabindex="-1"></a>        <span class="ot">forecolor=</span><span class="st">&quot;#000000&quot;</span> <span class="ot">backcolor=</span><span class="st">&quot;#FFFFFF&quot;</span>/&gt;</span>
<span id="cb6-10"><a href="#cb6-10" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">textElement</span>&gt;</span>
<span id="cb6-11"><a href="#cb6-11" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">font</span> <span class="ot">size=</span><span class="st">&quot;10&quot;</span>/&gt;</span>
<span id="cb6-12"><a href="#cb6-12" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">textElement</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td><div class="sourceCode" id="cb7"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb7-1"><a href="#cb7-1" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">textFieldExpression</span> <span class="ot">class=</span><span class="st">&quot;java.lang.String&quot;</span>&gt;<span class="bn">&lt;![CDATA[</span>&quot;&quot; + </span>
<span id="cb7-2"><a href="#cb7-2" aria-hidden="true" tabindex="-1"></a>        $V{PAGE_NUMBER}<span class="bn">]]&gt;</span>&lt;/<span class="kw">textFieldExpression</span>&gt;</span>
<span id="cb7-3"><a href="#cb7-3" aria-hidden="true" tabindex="-1"></a>      &lt;/<span class="kw">textField</span>&gt;</span>
<span id="cb7-4"><a href="#cb7-4" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">textField</span> <span class="ot">pattern=</span><span class="st">&quot;&quot;</span> <span class="ot">isBlankWhenNull=</span><span class="st">&quot;false&quot;</span> <span class="ot">hyperlinkType=</span><span class="st">&quot;None&quot;</span>&gt;</span>
<span id="cb7-5"><a href="#cb7-5" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">reportElement</span> <span class="ot">key=</span><span class="st">&quot;textField&quot;</span> <span class="ot">x=</span><span class="st">&quot;342&quot;</span> <span class="ot">y=</span><span class="st">&quot;6&quot;</span> <span class="ot">width=</span><span class="st">&quot;170&quot;</span> <span class="ot">height=</span><span class="st">&quot;19&quot;</span> </span>
<span id="cb7-6"><a href="#cb7-6" aria-hidden="true" tabindex="-1"></a>        <span class="ot">forecolor=</span><span class="st">&quot;#000000&quot;</span> <span class="ot">backcolor=</span><span class="st">&quot;#FFFFFF&quot;</span>/&gt;</span>
<span id="cb7-7"><a href="#cb7-7" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">box</span>&gt;</span>
<span id="cb7-8"><a href="#cb7-8" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">topPen</span> <span class="ot">lineWidth=</span><span class="st">&quot;0.0&quot;</span> <span class="ot">lineStyle=</span><span class="st">&quot;Solid&quot;</span> <span class="ot">lineColor=</span><span class="st">&quot;#000000&quot;</span>/&gt;</span>
<span id="cb7-9"><a href="#cb7-9" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">leftPen</span> <span class="ot">lineWidth=</span><span class="st">&quot;0.0&quot;</span> <span class="ot">lineStyle=</span><span class="st">&quot;Solid&quot;</span> <span class="ot">lineColor=</span><span class="st">&quot;#000000&quot;</span>/&gt;</span>
<span id="cb7-10"><a href="#cb7-10" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">bottomPen</span> <span class="ot">lineWidth=</span><span class="st">&quot;0.0&quot;</span> <span class="ot">lineStyle=</span><span class="st">&quot;Solid&quot;</span> <span class="ot">lineColor=</span><span class="st">&quot;#000000&quot;</span>/&gt;</span>
<span id="cb7-11"><a href="#cb7-11" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">rightPen</span> <span class="ot">lineWidth=</span><span class="st">&quot;0.0&quot;</span> <span class="ot">lineStyle=</span><span class="st">&quot;Solid&quot;</span> <span class="ot">lineColor=</span><span class="st">&quot;#000000&quot;</span>/&gt;</span>
<span id="cb7-12"><a href="#cb7-12" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">box</span>&gt;</span>
<span id="cb7-13"><a href="#cb7-13" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">textElement</span> <span class="ot">textAlignment=</span><span class="st">&quot;Right&quot;</span>&gt;</span>
<span id="cb7-14"><a href="#cb7-14" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">font</span> <span class="ot">size=</span><span class="st">&quot;10&quot;</span>/&gt;</span>
<span id="cb7-15"><a href="#cb7-15" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">textElement</span>&gt;</span>
<span id="cb7-16"><a href="#cb7-16" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">textFieldExpression</span> <span class="ot">class=</span><span class="st">&quot;java.lang.String&quot;</span>&gt;<span class="bn">&lt;![CDATA[</span>&quot;Page &quot; + </span>
<span id="cb7-17"><a href="#cb7-17" aria-hidden="true" tabindex="-1"></a>        $V{PAGE_NUMBER} + &quot; of &quot;<span class="bn">]]&gt;</span>&lt;/<span class="kw">textFieldExpression</span>&gt;</span>
<span id="cb7-18"><a href="#cb7-18" aria-hidden="true" tabindex="-1"></a>      &lt;/<span class="kw">textField</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td rowspan="2"><div class="sourceCode" id="cb8"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb8-1"><a href="#cb8-1" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">textField</span> <span class="ot">pattern=</span><span class="st">&quot;&quot;</span> <span class="ot">isBlankWhenNull=</span><span class="st">&quot;false&quot;</span> <span class="ot">hyperlinkType=</span><span class="st">&quot;None&quot;</span>&gt;</span>
<span id="cb8-2"><a href="#cb8-2" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">reportElement</span> <span class="ot">key=</span><span class="st">&quot;textField&quot;</span> <span class="ot">x=</span><span class="st">&quot;1&quot;</span> <span class="ot">y=</span><span class="st">&quot;6&quot;</span> <span class="ot">width=</span><span class="st">&quot;209&quot;</span> <span class="ot">height=</span><span class="st">&quot;19&quot;</span> </span>
<span id="cb8-3"><a href="#cb8-3" aria-hidden="true" tabindex="-1"></a>        <span class="ot">forecolor=</span><span class="st">&quot;#000000&quot;</span> <span class="ot">backcolor=</span><span class="st">&quot;#FFFFFF&quot;</span>/&gt;</span>
<span id="cb8-4"><a href="#cb8-4" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">box</span>&gt;</span>
<span id="cb8-5"><a href="#cb8-5" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">topPen</span> <span class="ot">lineWidth=</span><span class="st">&quot;0.0&quot;</span> <span class="ot">lineStyle=</span><span class="st">&quot;Solid&quot;</span> <span class="ot">lineColor=</span><span class="st">&quot;#000000&quot;</span>/&gt;</span>
<span id="cb8-6"><a href="#cb8-6" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">leftPen</span> <span class="ot">lineWidth=</span><span class="st">&quot;0.0&quot;</span> <span class="ot">lineStyle=</span><span class="st">&quot;Solid&quot;</span> <span class="ot">lineColor=</span><span class="st">&quot;#000000&quot;</span>/&gt;</span>
<span id="cb8-7"><a href="#cb8-7" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">bottomPen</span> <span class="ot">lineWidth=</span><span class="st">&quot;0.0&quot;</span> <span class="ot">lineStyle=</span><span class="st">&quot;Solid&quot;</span> <span class="ot">lineColor=</span><span class="st">&quot;#000000&quot;</span>/&gt;</span>
<span id="cb8-8"><a href="#cb8-8" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">rightPen</span> <span class="ot">lineWidth=</span><span class="st">&quot;0.0&quot;</span> <span class="ot">lineStyle=</span><span class="st">&quot;Solid&quot;</span> <span class="ot">lineColor=</span><span class="st">&quot;#000000&quot;</span>/&gt;</span>
<span id="cb8-9"><a href="#cb8-9" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">box</span>&gt;</span>
<span id="cb8-10"><a href="#cb8-10" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">textElement</span>&gt;</span>
<span id="cb8-11"><a href="#cb8-11" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">font</span> <span class="ot">size=</span><span class="st">&quot;10&quot;</span>/&gt;</span>
<span id="cb8-12"><a href="#cb8-12" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">textElement</span>&gt;</span>
<span id="cb8-13"><a href="#cb8-13" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">textFieldExpression</span> <span class="ot">class=</span><span class="st">&quot;java.util.Date&quot;</span>&gt;<span class="bn">&lt;![CDATA[</span>new Date()<span class="bn">]]&gt;</span></span>
<span id="cb8-14"><a href="#cb8-14" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">textFieldExpression</span>&gt;</span>
<span id="cb8-15"><a href="#cb8-15" aria-hidden="true" tabindex="-1"></a>      &lt;/<span class="kw">textField</span>&gt;</span>
<span id="cb8-16"><a href="#cb8-16" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">band</span>&gt;</span>
<span id="cb8-17"><a href="#cb8-17" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">pageFooter</span>&gt;</span>
<span id="cb8-18"><a href="#cb8-18" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">summary</span>&gt;</span>
<span id="cb8-19"><a href="#cb8-19" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">band</span>/&gt;</span>
<span id="cb8-20"><a href="#cb8-20" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">summary</span>&gt;</span>
<span id="cb8-21"><a href="#cb8-21" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">jasperReport</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
</tr>
</tbody>
</table>

During compilation of the `jrxml` file (using some JasperReports classes) the jrdax is parsed and loaded in a JasperDesign object, which is a rich data structure that allows you to represent the exact jrdax contents in memory. Regardless of the language used for expressions inside the `jrxml`, JasperReports creates a special Java class that represents the whole report. The report is then compiled, instanced, and serialized in a `jasper` file, ready for loading at any time.

JasperReports' speedy operation is due to all of a report’s formulas being compiled into Java-native bytecode and the report structure being verified during compilation instead of at run time. The `jasper` file contains no extraneous resources, such as images used in the report, resource bundles to run the report in different languages, or extra scriptlets and external style definitions. All these resources must be provided by the host application and at run time.
