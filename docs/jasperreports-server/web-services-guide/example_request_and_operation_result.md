---
title: Example Request and Operation Result
description: "This is the full SOAP request for a scheduleJob operation that creates a job with four report parameters:"
---

# 1.0.1 Example Request and Operation Result

This is the full SOAP request for a `scheduleJob` operation that creates a job with four report parameters:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">&lt;?xml</span> <span class="ot">version=</span><span class="st">&quot;1.0&quot;</span> <span class="ot">encoding=</span><span class="st">&quot;UTF-8&quot;</span><span class="fu">?&gt;</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">soapenv:Envelope</span> <span class="ot">xmlns:soapenv=</span><span class="st">&quot;http://schemas.xmlsoap.org/soap/envelope/&quot;</span> <span class="ot">xmlns:xsd=</span><span class="st">&quot;http://www.w3.org/2001/XMLSchema&quot;</span> <span class="ot">xmlns:xsi=</span><span class="st">&quot;http://www.w3.org/2001/XMLSchema-instance&quot;</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">soapenv:Body</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">ns1:scheduleJob</span> <span class="ot">soapenv:encodingStyle=</span><span class="st">&quot;http://schemas.xmlsoap.org/soap/encoding/</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a><span class="st">      &quot;</span> <span class="ot">xmlns:ns1=</span><span class="st">&quot;http://www.jasperforge.org/jasperserver/ws&quot;</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">job</span> <span class="ot">xsi:type=</span><span class="st">&quot;ns1:Job&quot;</span>&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">reportUnitURI</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;/reports/samples/SalesByMonth</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">reportUnitURI</span>&gt;</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">username</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span> <span class="ot">xsi:nil=</span><span class="st">&quot;true&quot;</span>/&gt;</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">label</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;Label 3&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">description</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;Description 3&lt;/<span class="kw">description</span>&gt;</span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">simpleTrigger</span> <span class="ot">xsi:type=</span><span class="st">&quot;ns1:JobSimpleTrigger&quot;</span>&gt;</span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">timezone</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span> <span class="ot">xsi:nil=</span><span class="st">&quot;true&quot;</span>/&gt;</span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">startDate</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:dateTime&quot;</span>&gt;2008-10-09T09:25:00.000Z&lt;/<span class="kw">startDate</span>&gt;</span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">endDate</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:dateTime&quot;</span> <span class="ot">xsi:nil=</span><span class="st">&quot;true&quot;</span>/&gt;</span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">occurrenceCount</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:int&quot;</span>&gt;1&lt;/<span class="kw">occurrenceCount</span>&gt;</span>
<span id="cb1-17"><a href="#cb1-17" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">recurrenceInterval</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:int&quot;</span> <span class="ot">xsi:nil=</span><span class="st">&quot;true&quot;</span>/&gt;</span>
<span id="cb1-18"><a href="#cb1-18" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">recurrenceIntervalUnit</span> <span class="ot">xsi:type=</span><span class="st">&quot;ns1:IntervalUnit&quot;</span> <span class="ot">xsi:nil=</span><span class="st">&quot;true&quot;</span>/&gt;</span>
<span id="cb1-19"><a href="#cb1-19" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">simpleTrigger</span>&gt;</span>
<span id="cb1-20"><a href="#cb1-20" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">calendarTrigger</span> <span class="ot">xsi:type=</span><span class="st">&quot;ns1:JobCalendarTrigger&quot;</span> <span class="ot">xsi:nil=</span><span class="st">&quot;true&quot;</span>/&gt;</span>
<span id="cb1-21"><a href="#cb1-21" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">parameters</span> <span class="ot">soapenc:arrayType=</span><span class="st">&quot;ns1:JobParameter[4]&quot;</span> <span class="ot">xsi:type=</span><span class="st">&quot;soapenc:Array&quot;</span></span>
<span id="cb1-22"><a href="#cb1-22" aria-hidden="true" tabindex="-1"></a>          <span class="ot">xmlns:soapenc=</span><span class="st">&quot;http://schemas.xmlsoap.org/soap/encoding/&quot;</span>&gt;</span>
<span id="cb1-23"><a href="#cb1-23" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">parameters</span> <span class="ot">xsi:type=</span><span class="st">&quot;ns1:JobParameter&quot;</span>&gt;</span>
<span id="cb1-24"><a href="#cb1-24" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">name</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;TextInput&lt;/<span class="kw">name</span>&gt;</span>
<span id="cb1-25"><a href="#cb1-25" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">value</span> <span class="ot">xsi:type=</span><span class="st">&quot;soapenc:int&quot;</span>&gt;22&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-26"><a href="#cb1-26" aria-hidden="true" tabindex="-1"></a>          &lt;/<span class="kw">parameters</span>&gt;</span>
<span id="cb1-27"><a href="#cb1-27" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">parameters</span> <span class="ot">xsi:type=</span><span class="st">&quot;ns1:JobParameter&quot;</span>&gt;</span>
<span id="cb1-28"><a href="#cb1-28" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">name</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;CheckboxInput&lt;/<span class="kw">name</span>&gt;</span>
<span id="cb1-29"><a href="#cb1-29" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">value</span> <span class="ot">xsi:type=</span><span class="st">&quot;soapenc:boolean&quot;</span>&gt;true&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-30"><a href="#cb1-30" aria-hidden="true" tabindex="-1"></a>          &lt;/<span class="kw">parameters</span>&gt;</span>
<span id="cb1-31"><a href="#cb1-31" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">parameters</span> <span class="ot">xsi:type=</span><span class="st">&quot;ns1:JobParameter&quot;</span>&gt;</span>
<span id="cb1-32"><a href="#cb1-32" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">name</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;ListInput&lt;/<span class="kw">name</span>&gt;</span>
<span id="cb1-33"><a href="#cb1-33" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">value</span> <span class="ot">xsi:type=</span><span class="st">&quot;soapenc:string&quot;</span>&gt;2&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-34"><a href="#cb1-34" aria-hidden="true" tabindex="-1"></a>          &lt;/<span class="kw">parameters</span>&gt;</span>
<span id="cb1-35"><a href="#cb1-35" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">parameters</span> <span class="ot">xsi:type=</span><span class="st">&quot;ns1:JobParameter&quot;</span>&gt;</span>
<span id="cb1-36"><a href="#cb1-36" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">name</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;DateInput&lt;/<span class="kw">name</span>&gt;</span>
<span id="cb1-37"><a href="#cb1-37" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">value</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:dateTime&quot;</span>&gt;2007-10-09T09:00:00.000Z&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-38"><a href="#cb1-38" aria-hidden="true" tabindex="-1"></a>          &lt;/<span class="kw">parameters</span>&gt;</span>
<span id="cb1-39"><a href="#cb1-39" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">parameters</span>&gt;</span>
<span id="cb1-40"><a href="#cb1-40" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">baseOutputFilename</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;Sales3&lt;/<span class="kw">baseOutputFilename</span>&gt;</span>
<span id="cb1-41"><a href="#cb1-41" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">outputFormats</span> <span class="ot">soapenc:arrayType=</span><span class="st">&quot;xsd:string[1]&quot;</span> <span class="ot">xsi:type=</span></span>
<span id="cb1-42"><a href="#cb1-42" aria-hidden="true" tabindex="-1"></a>          <span class="st">&quot;soapenc:Array&quot;</span> <span class="ot">xmlns:soapenc=</span><span class="st">&quot;http://schemas.xmlsoap.org/soap/</span></span>
<span id="cb1-43"><a href="#cb1-43" aria-hidden="true" tabindex="-1"></a><span class="st">          encoding/&quot;</span>&gt;</span>
<span id="cb1-44"><a href="#cb1-44" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">outputFormats</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;PDF&lt;/<span class="kw">outputFormats</span>&gt;</span>
<span id="cb1-45"><a href="#cb1-45" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">outputFormats</span>&gt;</span>
<span id="cb1-46"><a href="#cb1-46" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">outputLocale</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span> <span class="ot">xsi:nil=</span><span class="st">&quot;true&quot;</span>/&gt;</span></code></pre></div></td>
</tr>
<tr>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">repositoryDestination</span> <span class="ot">xsi:type=</span><span class="st">&quot;ns1:JobRepositoryDestination&quot;</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">folderURI</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;/ContentFiles&lt;/<span class="kw">folderURI</span>&gt;</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">sequentialFilenames</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:boolean&quot;</span>&gt;false</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>          &lt;/<span class="kw">sequentialFilenames</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">overwriteFiles</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:boolean&quot;</span>&gt;false&lt;/<span class="kw">overwriteFiles</span>&gt;</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">repositoryDestination</span>&gt;</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">mailNotification</span> <span class="ot">xsi:type=</span><span class="st">&quot;ns1:JobMailNotification&quot;</span> <span class="ot">xsi:nil=</span><span class="st">&quot;true&quot;</span>/&gt;</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>      &lt;/<span class="kw">job</span>&gt;</span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">ns1:scheduleJob</span>&gt;</span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">soapenv:Body</span>&gt;</span>
<span id="cb2-11"><a href="#cb2-11" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">soapenv:Envelope</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

The response of the request contains the job details as saved by the server:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">&lt;?xml</span> <span class="ot">version=</span><span class="st">&quot;1.0&quot;</span> <span class="ot">encoding=</span><span class="st">&quot;utf-8&quot;</span><span class="fu">?&gt;</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">soapenv:Envelope</span> <span class="ot">xmlns:soapenv=</span><span class="st">&quot;http://schemas.xmlsoap.org/soap/envelope/&quot;</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  <span class="ot">xmlns:xsd=</span><span class="st">&quot;http://www.w3.org/2001/XMLSchema&quot;</span> <span class="ot">xmlns:xsi=</span><span class="st">&quot;http://www.w3.org/2001/</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="st">  XMLSchema-instance&quot;</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">soapenv:Body</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">ns1:scheduleJobResponse</span> <span class="ot">soapenv:encodingStyle=</span><span class="st">&quot;http://schemas.xmlsoap.org/soap/</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a><span class="st">      encoding/&quot;</span> <span class="ot">xmlns:ns1=</span><span class="st">&quot;http://www.jasperforge.org/jasperserver/ws&quot;</span>&gt;</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">scheduleJobReturn</span> <span class="ot">xsi:type=</span><span class="st">&quot;ns1:job&quot;</span>&gt;</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">id</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:long&quot;</span>&gt;7&lt;/<span class="kw">id</span>&gt;</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">version</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:int&quot;</span>&gt;0&lt;/<span class="kw">version</span>&gt;</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">reportUnitURI</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;/reports/samples/SalesByMonth<span class="er">&lt;</span>/</span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>          reportUnitURI&gt;</span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">username</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;tomcat&lt;/<span class="kw">username</span>&gt;</span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">label</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;Label 3&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">description</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;Description 3&lt;/<span class="kw">description</span>&gt;</span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">simpleTrigger</span> <span class="ot">xsi:type=</span><span class="st">&quot;ns1:jobSimpleTrigger&quot;</span>&gt;</span>
<span id="cb1-17"><a href="#cb1-17" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">id</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:long&quot;</span>&gt;7&lt;/<span class="kw">id</span>&gt;</span>
<span id="cb1-18"><a href="#cb1-18" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">version</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:int&quot;</span>&gt;0&lt;/<span class="kw">version</span>&gt;</span>
<span id="cb1-19"><a href="#cb1-19" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">timezone</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;Europe/Minsk&lt;/<span class="kw">timezone</span>&gt;</span>
<span id="cb1-20"><a href="#cb1-20" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">startDate</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:dateTime&quot;</span>&gt;2008-10-09T09:25:00.000Z&lt;/<span class="kw">startDate</span>&gt;</span>
<span id="cb1-21"><a href="#cb1-21" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">endDate</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:dateTime&quot;</span> <span class="ot">xsi:nil=</span><span class="st">&quot;true&quot;</span>/&gt;</span>
<span id="cb1-22"><a href="#cb1-22" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">occurrenceCount</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:int&quot;</span>&gt;1&lt;/<span class="kw">occurrenceCount</span>&gt;</span>
<span id="cb1-23"><a href="#cb1-23" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">recurrenceInterval</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:int&quot;</span> <span class="ot">xsi:nil=</span><span class="st">&quot;true&quot;</span>/&gt;</span>
<span id="cb1-24"><a href="#cb1-24" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">recurrenceIntervalUnit</span> <span class="ot">xsi:type=</span><span class="st">&quot;ns1:IntervalUnit&quot;</span> <span class="ot">xsi:nil=</span><span class="st">&quot;true&quot;</span>/&gt;</span>
<span id="cb1-25"><a href="#cb1-25" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">simpleTrigger</span>&gt;</span></code></pre></div>
<p><code> &lt;calendarTrigger xsi:type="ns1:JobCalendarTrigger" xsi:nil="true"/&gt;</code></p>
<div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">parameters</span> <span class="ot">soapenc:arrayType=</span><span class="st">&quot;ns1:JobParameter[4]&quot;</span> <span class="ot">xsi:type=</span><span class="st">&quot;soapenc:Array&quot;</span> </span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>          <span class="ot">xmlns:soapenc=</span><span class="st">&quot;http://schemas.xmlsoap.org/soap/encoding/&quot;</span>&gt;</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">parameters</span> <span class="ot">xsi:type=</span><span class="st">&quot;ns1:jobParameter&quot;</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">name</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;CheckboxInput&lt;/<span class="kw">name</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">value</span> <span class="ot">xsi:type=</span><span class="st">&quot;soapenc:boolean&quot;</span>&gt;true&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>          &lt;/<span class="kw">parameters</span>&gt;</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">parameters</span> <span class="ot">xsi:type=</span><span class="st">&quot;ns1:jobParameter&quot;</span>&gt;</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">name</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;TextInput&lt;/<span class="kw">name</span>&gt;</span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">value</span> <span class="ot">xsi:type=</span><span class="st">&quot;soapenc:int&quot;</span>&gt;22&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a>          &lt;/<span class="kw">parameters</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td><div class="sourceCode" id="cb3"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">parameters</span> <span class="ot">xsi:type=</span><span class="st">&quot;ns1:jobParameter&quot;</span>&gt;</span>
<span id="cb3-2"><a href="#cb3-2" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">name</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;DateInput&lt;/<span class="kw">name</span>&gt;</span>
<span id="cb3-3"><a href="#cb3-3" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">value</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:dateTime&quot;</span>&gt;2007-10-09T09:00:00.000Z&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb3-4"><a href="#cb3-4" aria-hidden="true" tabindex="-1"></a>          &lt;/<span class="kw">parameters</span>&gt;</span>
<span id="cb3-5"><a href="#cb3-5" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">parameters</span> <span class="ot">xsi:type=</span><span class="st">&quot;ns1:jobParameter&quot;</span>&gt;</span>
<span id="cb3-6"><a href="#cb3-6" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">name</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;ListInput&lt;/<span class="kw">name</span>&gt;</span>
<span id="cb3-7"><a href="#cb3-7" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">value</span> <span class="ot">xsi:type=</span><span class="st">&quot;soapenc:string&quot;</span>&gt;2&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb3-8"><a href="#cb3-8" aria-hidden="true" tabindex="-1"></a>          &lt;/<span class="kw">parameters</span>&gt;</span>
<span id="cb3-9"><a href="#cb3-9" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">parameters</span>&gt;</span>
<span id="cb3-10"><a href="#cb3-10" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">baseOutputFilename</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;Sales3&lt;/<span class="kw">baseOutputFilename</span>&gt;</span>
<span id="cb3-11"><a href="#cb3-11" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">outputFormats</span> <span class="ot">soapenc:arrayType=</span><span class="st">&quot;xsd:string[1]&quot;</span> <span class="ot">xsi:type=</span><span class="st">&quot;soapenc:Array&quot;</span> </span>
<span id="cb3-12"><a href="#cb3-12" aria-hidden="true" tabindex="-1"></a>          <span class="ot">xmlns:soapenc=</span><span class="st">&quot;http://schemas.xmlsoap.org/soap/encoding/&quot;</span>&gt;</span>
<span id="cb3-13"><a href="#cb3-13" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">outputFormats</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;PDF&lt;/<span class="kw">outputFormats</span>&gt;</span>
<span id="cb3-14"><a href="#cb3-14" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">outputFormats</span>&gt;</span>
<span id="cb3-15"><a href="#cb3-15" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">outputLocale</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span> <span class="ot">xsi:nil=</span><span class="st">&quot;true&quot;</span>/&gt;</span>
<span id="cb3-16"><a href="#cb3-16" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">repositoryDestination</span> <span class="ot">xsi:type=</span><span class="st">&quot;ns1:jobRepositoryDestination&quot;</span>&gt;</span>
<span id="cb3-17"><a href="#cb3-17" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">id</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:long&quot;</span>&gt;7&lt;/<span class="kw">id</span>&gt;</span>
<span id="cb3-18"><a href="#cb3-18" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">version</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:int&quot;</span>&gt;0&lt;/<span class="kw">version</span>&gt;</span>
<span id="cb3-19"><a href="#cb3-19" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">folderURI</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:string&quot;</span>&gt;/ContentFiles&lt;/<span class="kw">folderURI</span>&gt;</span>
<span id="cb3-20"><a href="#cb3-20" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">sequentialFilenames</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:boolean&quot;</span>&gt;false&lt;/<span class="kw">sequentialFilenames</span>&gt;</span>
<span id="cb3-21"><a href="#cb3-21" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">overwriteFiles</span> <span class="ot">xsi:type=</span><span class="st">&quot;xsd:boolean&quot;</span>&gt;false&lt;/<span class="kw">overwriteFiles</span>&gt;</span>
<span id="cb3-22"><a href="#cb3-22" aria-hidden="true" tabindex="-1"></a>          &lt;/<span class="kw">repositoryDestination</span>&gt; </span>
<span id="cb3-23"><a href="#cb3-23" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">mailNotification</span> <span class="ot">xsi:type=</span><span class="st">&quot;ns1:JobMailNotification&quot;</span> <span class="ot">xsi:nil=</span><span class="st">&quot;true&quot;</span>/&gt;</span>
<span id="cb3-24"><a href="#cb3-24" aria-hidden="true" tabindex="-1"></a>      &lt;/<span class="kw">scheduleJobReturn</span>&gt;</span>
<span id="cb3-25"><a href="#cb3-25" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">ns1:scheduleJobResponse</span>&gt;</span>
<span id="cb3-26"><a href="#cb3-26" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">soapenv:Body</span>&gt;</span>
<span id="cb3-27"><a href="#cb3-27" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">soapenv:Envelope</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>
