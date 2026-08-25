---
title: The reportExecutions Service
description: "As described in The reports Service, synchronous report execution blocks the client waiting for the response. Synchronous report execution slows down or uses many threads, each waiting for a report,..."
---

# The reportExecutions Service

As described in [The reports Service](reports.md), [](reports.md) synchronous report execution blocks the client waiting for the response. Synchronous report execution slows down or uses many threads, each waiting for a report, when:

- Managing large reports that may take minutes to complete

- Running a large number of reports simultaneously

The rest_v2/reportExecutions service provides asynchronous report execution, so that the client does not need to wait for report output. Instead, the client obtains a request ID to check the status of the report periodically. This is also called polling. When the report is finished, the client downloads the output. Alternatively, the client can check when specific pages are finished and download available pages. The client can also send an asynchronous request for other export formats (PDF, Excel, and others) of the same report. Again the client can check the status of the export and download the result when the export has been completed.

Reports scheduled on the server also run asynchronously. reportExecutions allows you to access jobs triggered by the scheduler. Finally, the reportExecutions service allows the client to stop and remove any report execution or job that has been triggered.

This chapter includes the following sections:

- Running a Report Asynchronously
- Polling Report Execution
- Requesting Page Status
- Requesting Report Execution Details
- Requesting Report Output
- Requesting Report Bookmarks
- Exporting a Report Asynchronously
- Modifying Report Parameters
- Polling Export Execution
- Finding Running Reports and Jobs
- Stopping Running Reports and Jobs
- Removing a Report Execution

## Running a Report Asynchronously

To run a report asynchronously, the reportExecutions service provides a method to specify all the parameters needed to open a report. Report parameters are all sent as a `reportExecutionRequest` object. The response from the server contains the request ID needed to track the execution until completion.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>POST</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/reportExecutions</span></span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jrio/<span>rest_v2/reportExecutions</span></span></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/xml</span></p>
<p><span>application/json</span></p></td>
<td colspan="2"><p><span>A complete <code>ReportExecutionRequest</code> in either XML or JSON format. See the example and table below for an explanation of its properties.</span></p>
<p><span>A complete <code>ReportExecutionRequest</code> in JSON format. See the example and table below for an explanation of its properties.</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The content contains a <span>ReportExecution</span> descriptor. See below for an example</p></td>
<td><p>403 Forbidden–When the logged-in user does not have permission to access the report in the request.</p>
<p>404 Not Found – When the report URI specified in the request does not exist.</p></td>
</tr>
</tbody>
</table>

The following example shows the structure of the `ReportExecutionRequest`:

``` xml
<reportExecutionRequest>
    <reportUnitUri>/supermart/details/CustomerDetailReport</reportUnitUri>
    <async>true</async>
    <reportContainerWidth>900</reportContainerWidth>
    <freshData>false</freshData>
    <saveDataSnapshot>false</saveDataSnapshot>
    <outputFormat>html</outputFormat>
    <interactive>true</interactive>
    <ignorePagination>false</ignorePagination>
    <pages>1-5</pages>
    <parameters>
        <reportParameter name="someParameterName">
            <value>value 1</value>
            <value>value 2</value>
        </reportParameter>
        <reportParameter name="someAnotherParameterName">
            <value>another value</value>
        </reportParameter>
    </parameters>
</reportExecutionRequest>
{
    "reportUnitUri":"/samples/reports/chartthemes/ChartThemesReport",
    "async":true,
    "interactive":true,
    "pages":"1-5",
    "attachmentsPrefix":"/jrio/rest_v2/reportExecutions/
        {reportExecutionId}/exports/{exportExecutionId}/attachments/",
    "baseUrl":"/jrio",
    "parameters":
    {
        "reportParameter":
        [
            {"name":"chartTheme","value":["aegean"]},
            {"name":"anotherParamName","value":["value 1","value 2"]}
        ]
    }
}
```

The following table describes the properties that you can specify in the `ReportExecutionRequest`:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th><p>Property</p></th>
<th><p>Required or Default</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><span>reportUnitUri</span></p></td>
<td><p>Required</p></td>
<td><p>Repository path (URI) of the report to run. For commercial editions with organizations, the URI is relative to the logged-in user’s organization.</p>
<p>Repository path (URI) of the report to run.</p></td>
</tr>
<tr>
<td><p><span>outputFormat</span></p></td>
<td><p>Required</p></td>
<td><p>Specifies the desired output format: <span>pdf</span>, <span>html</span>, <span>xlsx</span>, <span>rtf</span>, <span>csv</span>, <span>xml</span>, <span>docx</span>, <span>odt</span>, <span>ods</span>, <span>jrprint</span>.</p>
<p>As of JasperReports Server 6.0, it is also possible to specify <span>json</span> if your reports are designed for data export. For more information, see the JasperReports Library samples documentation.</p>
<p>Specifies the desired output format:</p>
<ul>
<li>Regular output:</li>
</ul>
<p>html, pdf, csv, docx, pptx, xlsx, rtf, odt, ods, xml</p>
<ul>
<li>Metadata output:</li>
</ul>
<p>data_csv, data_xlsx, data_json</p></td>
</tr>
<tr>
<td><p><span>freshData</span></p></td>
<td><p>false</p></td>
<td><p>When data snapshots are enabled, it specifies whether the report should get fresh data by querying the data source. If false, use a previously saved data snapshot (if any). By default, if a saved data snapshot exists for the report it is used when running the report.</p></td>
</tr>
<tr>
<td><p><span>saveDataSnapshot</span></p></td>
<td><p>false</p></td>
<td><p>When data snapshots are enabled, it specifies whether the data snapshot for the report should be written (or overwritten) with data from the report execution.</p></td>
</tr>
<tr>
<td><p><span>interactive</span></p></td>
<td><p>true</p></td>
<td><p>In a commercial edition of the server where Highcharts are used in the report, this property determines whether the required JavaScript is generated. It is returned as an attachment when exported to HTML. If false, the chart is generated as a non-interactive image file (also as an attachment).</p></td>
</tr>
<tr>
<td><p><span>allowInlineScripts</span></p></td>
<td>true</td>
<td>Affects HTML export only. If true, then inline scripts are allowed, otherwise no inline script is included in the HTML output.</td>
</tr>
<tr>
<td><p><span>ignorePagination</span></p></td>
<td><p>Optional</p></td>
<td><p>When set to true, the report is generated as a single long page. This can be used with HTML output to avoid pagination. When omitted, the <span>ignorePagination</span> property on the JRXML, if any, is used.</p></td>
</tr>
<tr>
<td><p><span>pages</span></p></td>
<td><p>Optional</p></td>
<td><p>Specify a page range to generate a partial report. The format is:<br />
<span>&lt;startPageNumber&gt;-&lt;endPageNumber&gt;</span></p></td>
</tr>
<tr>
<td><p><span>async</span></p></td>
<td><p>false</p></td>
<td><p>Determines whether <span>reportExecution</span> is synchronous or asynchronous. When set to true, the response is provided immediately and the client must poll the report status. They can download the results when ready. By default, this property is false and the operation pauses until the report execution is complete. The client must wait but can download the report immediately after the response.</p></td>
</tr>
<tr>
<td><p><span>transformerKey</span></p></td>
<td><p>Optional</p></td>
<td><p>Advanced property used when requesting a report as a <span>JasperPrint</span> object. This property can specify a JasperReports Library generic print element transformer of the class <span>net.sf.jasperreports.engine.export.GenericElementTransformer</span>. These transformers are pluggable as JasperReports Library extensions.</p></td>
</tr>
<tr>
<td><p><span>attachmentsPrefix</span></p></td>
<td><p>attachments</p></td>
<td><p>For HTML output, this property specifies the URL path to use for downloading the attachment files (JavaScript and images). The full path of the default value is:</p>
<p><span>{contextPath}/rest_v2/reportExecutions/{reportExecutionId}/exports/{exportExecutionId}/attachments/</span></p>
<p>You can specify a different URL path using the placeholders <span>{contextPath}</span>, <span>{reportExecutionId}</span>, and <span>{exportExecutionId}</span>.</p></td>
</tr>
<tr>
<td><p><span>baseUrl</span></p></td>
<td>String</td>
<td><p><span>Specifies the base URL that the report uses to load static resources such as JavaScript files. You can also set the <span>deploy.base.url</span> property in the <span>.../WEB-INF/js.config.properties</span> file to set this value permanently. If both are set, the <span>baseUrl</span> parameter in this request takes precedence.</span></p>
<p>Specifies the base URL that the report uses to load static resources such as JavaScript files.</p></td>
</tr>
<tr>
<td><p><span>parameters</span></p></td>
<td><p><span>See example</span></p></td>
<td><p>A list of input control parameters and their values.</p>
<p>By default, the parameter values are case-sensitive. To change them to case insensitive, set <code>inputControl.handler.values.caseSensitive=false</code> in the <code>jasperserver-pro/WEB-INF/js.config.properties</code> file.</p></td>
</tr>
<tr>
<td><p><span>reportContainerWidth</span></p></td>
<td>Optional</td>
<td>This property specifies the width of the report container. A report specifying this parameter with integer values receives the current screen size width when the report is run.</td>
</tr>
</tbody>
</table>

When successful, the reply from the server contains the `reportExecution` descriptor. This descriptor contains the request ID and status needed for the client to request the output. There are two statuses, one for the report execution itself, and one for the chosen output format.

The following descriptor shows that the report is still running (\<status\>execution\</status\>).

The following descriptor shows that the report was placed in the report execution queue ("status":"queued"):

``` xml
<reportExecution>
    <currentPage>1</currentPage>
    <exports>
        <export>
            <id>html</id>
            <status>queued</status>
        </export>
    </exports>
    <reportURI>/supermart/details/CustomerDetailReport</reportURI>
    <requestId>f3a9805a-4089-4b53-b9e9-b54752f91586</requestId>
    <status>execution</status>
</reportExecution>
{
    "requestId":"9ecf5c6f-b70d-4170-8a3b-b305db4c2253",
    "reportURI":"/samples/reports/chartthemes/ChartThemesReport",
    "status":"queued"
}
```

The value of `async` in the request determines if the report output is available after receiving a response. Your client should implement either synchronous or asynchronous processing of the response depending on the value you set for the `async` property.

Set the `async` property.

## Polling Report Execution

When requesting reports asynchronously, use the following method to poll the status of the report execution. The request ID in the URL is the one returned in the `reportExecution` descriptor.

This service supports the extended status value that includes an appropriate message.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>GET</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/reportExecutions/</span>requestID/<span>status</span>/</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jrio/<span>rest_v2/reportExecutions/</span>requestID/<span>status</span>/</span></p></td>
</tr>
<tr>
<td colspan="2"><p>Options</p></td>
<td colspan="2">Sample Return Value</td>
</tr>
<tr>
<td colspan="2"><p><span>accept: application/xml</span> (default)</p></td>
<td colspan="2"><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">status</span>&gt;ready&lt;/<span class="kw">status</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td colspan="2"><p><span>accept: application/status+xml</span></p></td>
<td colspan="2"><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">status</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">errorDescriptor</span>&gt;</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">errorCode</span>&gt;input.controls.validation.error&lt;/<span class="kw">errorCode</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">message</span>&gt;Input controls validation failure&lt;/<span class="kw">message</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">parameters</span>&gt;</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">parameter</span>&gt;Specify a valid value for type Integer.</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>            &lt;/<span class="kw">parameter</span>&gt;</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">parameters</span>&gt;</span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">errorDescriptor</span>&gt;</span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;failed&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-11"><a href="#cb2-11" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">status</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td colspan="2"><p><span>accept: application/json</span></p></td>
<td colspan="2"><div class="sourceCode" id="cb3"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span> <span class="dt">&quot;value&quot;</span><span class="fu">:</span> <span class="st">&quot;ready&quot;</span> <span class="fu">}</span></span></code></pre></div></td>
</tr>
<tr>
<td colspan="2"><p><span>accept: application/status+json</span></p></td>
<td colspan="2"><div class="sourceCode" id="cb4"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb4-1"><a href="#cb4-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb4-2"><a href="#cb4-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;value&quot;</span><span class="fu">:</span> <span class="st">&quot;failed&quot;</span><span class="fu">,</span></span>
<span id="cb4-3"><a href="#cb4-3" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;errorDescriptor&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb4-4"><a href="#cb4-4" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;message&quot;</span><span class="fu">:</span> <span class="st">&quot;Input controls validation failure&quot;</span><span class="fu">,</span></span>
<span id="cb4-5"><a href="#cb4-5" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;errorCode&quot;</span><span class="fu">:</span> <span class="st">&quot;input.controls.validation.error&quot;</span><span class="fu">,</span></span>
<span id="cb4-6"><a href="#cb4-6" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;parameters&quot;</span><span class="fu">:</span> <span class="ot">[</span><span class="st">&quot;Specify a valid value for type Integer.&quot;</span><span class="ot">]</span></span>
<span id="cb4-7"><a href="#cb4-7" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span></span>
<span id="cb4-8"><a href="#cb4-8" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The content contains the report status, as shown above. In the extended format, error reports contain error messages suitable for display.</p></td>
<td><p>404 Not Found – When the specified <span>requestID</span> does not exist.</p></td>
</tr>
</tbody>
</table>

## Requesting Page Status

When requesting reports asynchronously, you can also poll the status of a specific page during the report execution. The request ID in the URL is the one returned in the `reportExecution` descriptor.

When requesting reports asynchronously, you can also poll the status of a specific page during the report execution. The `executionId` in the URL is the one returned in the `reportExecution` descriptor. This service returns a response containing `reportStatus`, `pageFinal`, and `pageTimestamp` attributes.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>GET</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/reportExecutions/</span>requestID/<span>pages/</span>pageNumber/<span>status</span></span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jrio/<span>rest_v2/reportExecutions/</span>&lt;executionId&gt;/<span>pages/</span>&lt;pageNumber&gt;/<span>status</span></span></p></td>
</tr>
<tr>
<td colspan="2"><p>Options</p></td>
<td colspan="2"><p>Sample Response Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>accept: application/status+json</span></p></td>
<td colspan="2"><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;reportStatus&quot;</span><span class="fu">:</span> <span class="st">&quot;ready&quot;</span><span class="fu">,</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;pageTimestamp&quot;</span><span class="fu">:</span> <span class="st">&quot;0&quot;</span><span class="fu">,</span> </span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;pageFinal&quot;</span><span class="fu">:</span> <span class="st">&quot;true&quot;</span> </span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The content contains the page status, as shown above.</p></td>
<td><p>404 Not Found – When the request ID specified in the request does not exist.</p></td>
</tr>
</tbody>
</table>

## Requesting Report Execution Details

Once the report is ready, your client must determine the names of the files to download by requesting the `reportExecution` descriptor again. Specify the requestID in the URL as follows:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>GET</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/reportExecutions/</span>requestID</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jrio/<span>rest_v2/reportExecutions/</span>requestID</span></p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p><span>accept: application/xml</span></p>
<p><span>accept: application/json</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The content contains a <code>ReportExecution</code> descriptor. See below for an example.</p></td>
<td><p>404 Not Found – When the request ID specified in the request does not exist.</p></td>
</tr>
</tbody>
</table>

The `reportExecution` descriptor now contains the list of exports for the report, including the report output itself and any other file attachments. File attachments such as images and JavaScript occur only with HTML export.

``` json
{
    "status": "ready",
    "totalPages": 47,
    "requestId": "cce63cba-1685-4708-ba4f-b70f277a1cd5",
    "reportURI": "/public/Samples/Reports/AllAccounts",
    "exports": [
        {
        "status": "ready",
        "outputResource": {
            "contentType": "text/html,"
            "output final": true,
            "outputTimestamp": 0
        },
        "id": "db9acf02-8add-4196-9ab5-ce86844bfc2e",
        "attachments": [

        {
                "contentType": "image/png",
                "fileName": "img_0_0_0"
            }
        ]
    }
{
    "status": "ready",
    "totalPages": 47,
    "requestId": "b487a05a-4989-8b53-b2b9-b54752f998c4",
    "reportURI": "/reports/samples/AllAccounts",
    "exports": [{
        "id": "195a65cb-1762-450a-be2b-1196a02bb625",
        "options": {
            "outputFormat": "html",
            "attachmentsPrefix": "./images/",
            "allowInlineScripts": false
        },
        "status": "ready",
        "outputResource": {
            "contentType": "text/html"
        },
        "attachments": [{
            "contentType": "image/png",
            "fileName": "img_0_46_0"
        },
        {
            "contentType": "image/png",
            "fileName": "img_0_0_0"
        },
        {
            "contentType": "image/jpeg",
            "fileName": "img_0_46_1"
        }]
    },
    {
        "id": "4bac4889-0e63-4f09-bbe8-9593674f0700",
        "options": {
            "outputFormat": "html",
            "attachmentsPrefix": "{contextPath}/rest_v2/reportExecutions/{reportExecutionId}/exports/{exportExecutionId}/attachments/",
            "baseUrl": "http://localhost:8080/jrio",
            "allowInlineScripts": true
        },
        "status": "ready",
        "outputResource": {
            "contentType": "text/html"
        },
        "attachments": [{
            "contentType": "image/png",
            "fileName": "img_0_0_0"
        }]
    }]
}
```

When exporting a chart report to HTML, the image produced for the chart is a part of HTML, and can be in two formats - JavaScript or SVG:

- When "interactive" is set to *true*, it is embedded as JavaScript in HTML that uses Highcharts js to render the chart.
- When "interactive" is set to *false*, the chart image is embedded as SVG as part of HTML.

When the option *net.sf.jasperreports.force.html.embed.image=false in WEB-INF/classes/jasperreports.properties* in combination with *interactive=false*, this puts the SVG images into attachments instead of HTML.

## Requesting Report Output

After requesting a report execution and waiting synchronously or asynchronously for it to finish, your client is ready to download the report output.

Every export format of the report has an ID that is used to retrieve it. For example, the HTML export in the previous example has the ID 195a65cb-1762-450a-be2b-1196a02bb625. To download the main report output, specify this export ID in the following method:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>GET</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/reportExecutions/</span>requestID/<span>exports</span>/ exportID/<span>outputResource</span></span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jrio/<span>rest_v2/reportExecutions/</span>requestID/<span>exports</span>/ exportID/<span>outputResource</span></span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The content is the main output of the report. The format specified by the <code>contentType</code> property of the <code>outputResource</code> descriptor. For example: <code>text/html</code></p></td>
<td><p>400 Bad Request – When invalid values are provided for export options in the request body.</p>
<p>404 Not Found – When the request ID specified in the request does not exist.</p></td>
</tr>
</tbody>
</table>

For example, to download the main HTML of the report execution response above, use the following URL:

GET http://localhost:8080/jasperserver-pro/rest_v2/reportExecutions/b487a05a-4989-8b53-b2b9-b54752f998c4/exports/195a65cb-1762-450a-be2b-1196a02bb625/outputResource

GET http://localhost:8080/jrio/rest_v2/reportExecutions/b487a05a-4989-8b53-b2b9-b54752f998c4/exports/195a65cb-1762-450a-be2b-1196a02bb625/outputResource

!!! note

    JasperReports Server does not support exporting Highcharts charts with background images to PDF, ODT, DOCX, or RTF formats. When exporting or downloading reports with Highcharts that have background images to these formats, the background image is removed from the chart. The data in the chart is not affected.

!!! note

    JasperReports IO does not support exporting Highcharts charts with background images to PDF, ODT, DOCX, or RTF formats. When exporting or downloading reports with Highcharts that have background images to these formats, the background image is removed from the chart. The data in the chart is not affected.

To download file attachments for HTML output, use the following method. Download all attachments to display the HTML content properly. The given URL is the default path, but it can be modified with the `attachmentsPrefix` property in the `reportExecutionRequest`, as described in Running a Report Asynchronously.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>GET</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/reportExecutions/</span>requestID/<span>exports</span>/exportID/<span>attachments</span>/fileName</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jrio/<span>rest_v2/reportExecutions/</span>requestID/<span>exports</span>/exportID/<span>attachments</span>/fileName</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The content is the attachment in the format specified in the <code>contentType</code> property of the <code>attachment</code> descriptor, for example:</p>
<p><span>image/png</span></p></td>
<td><p>404 Not Found – When the request ID specified in the request does not exist.</p></td>
</tr>
</tbody>
</table>

For example, to download the one of the images for the HTML report execution response above, use the following URL:

GET http://localhost:8080/jasperserver-pro/rest_v2/reportExecutions/912382875_1366638024956_2/exports/html/attachments/img_0_46_0

GET http://localhost:8080/jrio/rest_v2/reportExecutions/912382875_1366638024956_2/exports/html/attachments/img_0_46_0

## Requesting Report Bookmarks

Some reports have additional meta-information associated with them, such as bookmarks and indexes of report sections or parts. Clients can use this information to create a table of contents for the report. The table of contents contains the links to the bookmarks and the parts defined in the report. After running a report, you can request this information using the same request ID.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>GET</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/reportExecutions/</span>requestID/<span>info</span></span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jrio/<span>rest_v2/reportExecutions/</span>{executionId}/<span>info</span></span></p></td>
</tr>
<tr>
<td colspan="2"><p>Options</p></td>
<td colspan="2"><p>Sample Response Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>accept: application/json</span></p>
<p><span>accept: application/xml</span></p></td>
<td colspan="2"><p>A structure that contains bookmarks and report parts, as shown below.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The content contains the report meta-information, as shown below.</p></td>
<td><p>404 Not Found – When the request ID specified in the request does not exist.</p></td>
</tr>
</tbody>
</table>

Example of a request URL:

``` text
https://localhost:8080/jasperserver[-pro]/rest_v2/reportExecutions/70b9b169-1c0e-431c-b8bc-a6f49328bc75/info
```

JSON:

``` json
{
  "bookmarks": {
    "id": "bkmrk_1058907116",
    "type": "bookmarks",
    "bookmarks": [
      {
        "label": "USA shipments",
        "pageIndex": 22,
        "elementAddress": "0",
        "bookmarks": [
          {
            "label": "Albuquerque",
            "pageIndex": 22,
            "elementAddress": "4",
            "bookmarks": null
          },
          {
            "label": "Anchorage",
            "pageIndex": 23,
            "elementAddress": "116",
            "bookmarks": null
          },
          ...
        ]
      }
    ]
  },

  "parts": {
    "id": "parts_533304192",
    "type": "reportparts",
    "parts": [
      {
        "idx": 0,
        "name": "Table of Contents"
      },
      {
        "idx": 3,
        "name": "Overview"
      },
      {
        "idx": 22,
        "name": "USA shipments"
      }
    ]
  }
}
```

## Exporting a Report Asynchronously

After running a report and downloading its content in a given format, you can request the same report in other formats. As with exporting report formats through the user interface, the report does not run again because the export process is independent of the report.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>POST</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/reportExecutions/</span>requestID/<span>exports</span>/</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jrio/<span>rest_v2/reportExecutions/</span>requestID/<span>exports</span>/</span></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/xml</span></p>
<p><span>application/json</span></p></td>
<td colspan="2"><p>Send an <code>export</code> descriptor in either XML or JSON format to specify the format and details of your request. For example:</p>
<div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">export</span>&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">outputFormat</span>&gt;html&lt;/<span class="kw">outputFormat</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">pages</span>&gt;10-20&lt;/<span class="kw">pages</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">attachmentsPrefix</span>&gt;./images/&lt;/<span class="kw">attachmentsPrefix</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">export</span>&gt;</span></code></pre></div>
<p>Send an <code>export</code> descriptor in JSON format to specify the format and details of your request. For example:</p>
<div class="sourceCode" id="cb2"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;outputFormat&quot;</span><span class="fu">:</span> <span class="st">&quot;html&quot;</span><span class="fu">,</span></span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;pages&quot;</span><span class="fu">:</span> <span class="st">&quot;10-20&quot;</span><span class="fu">,</span></span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;attachmentsPrefix&quot;</span><span class="fu">:</span> <span class="st">&quot;./images/&quot;</span></span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p><span><span>accept: application/xml</span> (default)</span></p>
<p><span>accept: application/json</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The content contains an <code>exportExecution</code> descriptor. See below for an example.</p></td>
<td><p>404 Not Found – When the request ID specified in the request does not exist.</p></td>
</tr>
</tbody>
</table>

The following example shows the `exportExecution` descriptor that the server sends in response to the export request:

``` json
{
    "id":"6b7ce8fa-f1d7-4d53-9af6-4569edb05d1b",
    "status":"queued"
}
<exportExecution>
    <id>html;attachmentsPrefix=./images/</id>
    <status>ready</status>
    <outputResource>
        <contentType>text/html</contentType>
    </outputResource>
</exportExecution>
```

## Modifying Report Parameters

You can update the report parameters, also known as input controls, through a separate method before running a report execution again. For more operations with input controls, see [The inputControls Service](../../../jasperreports-server/rest-api-reference/jasperreports-server-rest-api-reference/inputcontrols.md).

You can update the report parameters, also known as input controls, through a separate method before running an existing report execution again. Use the following method to rerun the report with a different set of parameter values:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>POST</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/reportExecutions</span>/requestID/<span>parameters</span></span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jrio/<span>rest_v2/reportExecutions</span>/requestID/<span>parameters</span></span></p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><span>freshData</span></p></td>
<td><p><span>true</span></p></td>
<td colspan="2"><p>When data snapshots are enabled, you must set this to true to force the server to get fresh data when you change parameters. This overrides the default value of false, as explained in the table of properties in <span>Running a Report Asynchronously</span>.</p></td>
</tr>
<tr>
<td colspan="2">Media-Type</td>
<td colspan="2">Content</td>
</tr>
<tr>
<td colspan="2"><p><span>application/json</span></p></td>
<td colspan="2"><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="ot">[</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="fu">{</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;name&quot;</span><span class="fu">:</span><span class="st">&quot;someParameterName&quot;</span><span class="fu">,</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;value&quot;</span><span class="fu">:</span><span class="ot">[</span><span class="st">&quot;value 1&quot;</span><span class="ot">,</span> <span class="st">&quot;value 2&quot;</span><span class="ot">]</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span><span class="ot">,</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    <span class="fu">{</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;name&quot;</span><span class="fu">:</span><span class="st">&quot;someAnotherParameterName&quot;</span><span class="fu">,</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;value&quot;</span><span class="fu">:</span><span class="ot">[</span><span class="st">&quot;another value&quot;</span><span class="ot">]</span></span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span></span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a><span class="ot">]</span></span></code></pre></div></td>
</tr>
<tr>
<td colspan="2"><span>application/xml</span></td>
<td colspan="2"><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">reportParameters</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">reportParameter</span> <span class="ot">name=</span><span class="st">&quot;Country_multi_select&quot;</span>&gt;</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">value</span>&gt;Mexico&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">reportParameter</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>     &lt;<span class="kw">reportParameter</span> <span class="ot">name=</span><span class="st">&quot;Cascading_state_multi_select&quot;</span>&gt;</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">value</span>&gt;Guerrero&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">value</span>&gt;Sinaloa&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">reportParameter</span>&gt;</span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">reportParameters</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>204 No Content–There is no content to return.</p></td>
<td><p>404 Not Found – When the request ID specified in the request does not exist.</p></td>
</tr>
</tbody>
</table>

## Polling Export Execution

As with the execution of the main report, you can also poll the execution of the export process. This service supports the extended status value that includes an appropriate message.

As with the execution of the main report, you can also poll the execution of the export process. This service supports the extended status value that includes an appropriate message.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>GET</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/reportExecutions/</span>requestID/<span>exports</span>/<br />
exportID/<span>status</span></span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jrio/<span>rest_v2/reportExecutions/</span>requestID/<span>exports</span>/<br />
exportID/<span>status</span></span></p></td>
</tr>
<tr>
<td colspan="2"><p>Options</p></td>
<td colspan="2">Sample Return Value</td>
</tr>
<tr>
<td colspan="2"><p><span>accept: application/xml</span> (default)</p></td>
<td colspan="2"><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">status</span>&gt;ready&lt;/<span class="kw">status</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td colspan="2"><p><span>accept: application/status+xml</span></p></td>
<td colspan="2"><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">status</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">errorDescriptor</span>&gt;</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">errorCode</span>&gt;input.controls.validation.error&lt;/<span class="kw">errorCode</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">message</span>&gt;Input controls validation failure&lt;/<span class="kw">message</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">parameters</span>&gt;</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">parameter</span>&gt;Specify a valid value for type Integer.&lt;/<span class="kw">parameter</span>&gt;</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">parameters</span>&gt;</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">errorDescriptor</span>&gt;</span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;failed&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">status</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td colspan="2"><p><span>accept: application/json</span></p></td>
<td colspan="2"><div class="sourceCode" id="cb3"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span> <span class="dt">&quot;value&quot;</span><span class="fu">:</span> <span class="st">&quot;ready&quot;</span> <span class="fu">}</span></span></code></pre></div></td>
</tr>
<tr>
<td colspan="2"><p><span>accept: application/status+json</span></p></td>
<td colspan="2"><div class="sourceCode" id="cb4"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb4-1"><a href="#cb4-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb4-2"><a href="#cb4-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;value&quot;</span><span class="fu">:</span> <span class="st">&quot;failed&quot;</span><span class="fu">,</span></span>
<span id="cb4-3"><a href="#cb4-3" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;errorDescriptor&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb4-4"><a href="#cb4-4" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;message&quot;</span><span class="fu">:</span> <span class="st">&quot;Input controls validation failure&quot;</span><span class="fu">,</span></span>
<span id="cb4-5"><a href="#cb4-5" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;errorCode&quot;</span><span class="fu">:</span> <span class="st">&quot;input.controls.validation.error&quot;</span><span class="fu">,</span></span>
<span id="cb4-6"><a href="#cb4-6" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;parameters&quot;</span><span class="fu">:</span> <span class="ot">[</span><span class="st">&quot;Specify a valid value for type Integer.&quot;</span><span class="ot">]</span></span>
<span id="cb4-7"><a href="#cb4-7" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span></span>
<span id="cb4-8"><a href="#cb4-8" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The content contains the export status, as shown above. In the extended format, error reports contain error messages suitable for display.</p></td>
<td><p>404 Not Found – When the specified request ID does not exist.</p></td>
</tr>
</tbody>
</table>

For example, to get the status of the HTML export in the previous example, use the following URL:

GET http://localhost:8080/jasperserver-pro/rest_v2/reportExecutions/912382875_1366638024956_2/exports/195a65cb-1762-450a-be2b-1196a02bb625/status

GET http://localhost:8080/jrio/rest_v2/reportExecutions/912382875_1366638024956_2/exports/195a65cb-1762-450a-be2b-1196a02bb625/status

When the status is "ready", the client can download the new export output and any attachments as described in Requesting Report Output. For example:

GET http://localhost:8080/jasperserver-pro/rest_v2/reportExecutions/912382875_1366638024956_2/exports/195a65cb-1762-450a-be2b-1196a02bb625/outputResource

GET http://localhost:8080/jasperserver-pro/rest_v2/reportExecutions/912382875_1366638024956_2/exports/195a65cb-1762-450a-be2b-1196a02bb625/images/img_0_46_0

GET http://localhost:8080/jrio/rest_v2/reportExecutions/912382875_1366638024956_2/exports/195a65cb-1762-450a-be2b-1196a02bb625/outputResource

GET http://localhost:8080/jrio/rest_v2/reportExecutions/912382875_1366638024956_2/exports/195a65cb-1762-450a-be2b-1196a02bb625/images/img_0_46_0

## Finding Running Reports and Jobs

The reportExecutions service provides a method to search for reports that are running on the server. It includes asynchronous reports that are still running and those that are finished but in cache and available by their request ID.

The search for reports also includes report jobs triggered by the scheduler, both running and finished but still in the cache.

To search for running or finished reports, use the search arguments with the following URL:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>GET</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/reportExecutions</span>?&lt;arguments&gt;</span></p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><span>reportURI</span></p></td>
<td><p>Optional String</p></td>
<td colspan="2"><p>This string matches the repository URI of the running report, relative to the currently logged-in user’s organization.</p></td>
</tr>
<tr>
<td><p><span>jobID</span></p></td>
<td><p>Optional String</p></td>
<td colspan="2"><p>For scheduler jobs, this argument matches the ID of the job that triggered the running report.</p></td>
</tr>
<tr>
<td><p><span>jobLabel</span></p></td>
<td><p>Optional String</p></td>
<td colspan="2"><p>For scheduler jobs, this argument matches the name of the job that triggered the running report.</p></td>
</tr>
<tr>
<td><p><span>userName</span></p></td>
<td><p>Optional String</p></td>
<td colspan="2"><p>For scheduler jobs, this argument matches the user ID that created the job.</p></td>
</tr>
<tr>
<td><p><span>fireTimeFrom</span></p></td>
<td rowspan="2"><p>Optional<br />
<span>Date/Time</span></p></td>
<td colspan="2" rowspan="2"><p>For scheduler jobs, the fire time arguments define a range of time. You can check if the current job was triggered during this time. You can specify either or both of the arguments. Specify the date and time in the following pattern: <span>yyyy-MM-dd'T'HH:mmZ</span>.</p></td>
</tr>
<tr>
<td><p><span>fireTimeTo</span></p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p><span>accept: application/xml</span> (default)</p>
<p><span>accept: application/json</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The content is a descriptor for each of the matching results.</p></td>
<td><p>204 No Content – When the search results are empty.</p></td>
</tr>
</tbody>
</table>

The response contains a list of summary `reportExecution` descriptors, for example in XML:

``` xml
<reportExecutions>
    <reportExecution>
        <reportURI>repo:/supermart/details/CustomerDetailReport</reportURI>
        <requestId>2071593484_1355224559918_5</requestId>
    </reportExecution>
</reportExecutions>
```

Given the request ID, you can obtain more information about each result by downloading the full `reportExecution` descriptor, as described in Requesting Report Execution Details.

For security purposes, the search for running reports has the following restrictions:

- The system administrator (`superuser`) can see and cancel any report running on the server.
- An organization admin (`jasperadmin`) can see every running report, but can cancel only the reports that were started by a user from the same or child organization.
- A regular user can see every running report, but can cancel only the reports that he initiated.

## Stopping Running Reports and Jobs

To stop a running report and cancel its output, use the PUT method and set the `status` as `cancelled`.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>PUT</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/reportExecutions/</span>requestID/<span>status</span>/</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jrio]/<span>rest_v2/reportExecutions/</span>requestID/<span>status</span>/</span></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/xml</span></p>
<p><span>application/json</span></p></td>
<td colspan="2"><p>Send a <code>status</code> descriptor in JSON format with the value <code>cancelled</code>. For example:</p>
<p>Send a <code>status</code> descriptor in either XML or JSON format with the value <code>cancelled</code>. For example:</p>
<p>XML: <code>&lt;status&gt;cancelled&lt;/status&gt;</code></p>
<p>JSON: <code>{ "value": "cancelled" }</code></p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p><span>accept: application/xml</span> (default)</p>
<p><span>accept: application/json</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – When the report execution was successfully stopped, the server replies with the same status:</p>
<p>XML: <code>&lt;status&gt;cancelled&lt;/status&gt;</code></p>
<p>JSON: <code>{ "value": "cancelled" }</code></p>
<p>{ "value": "cancelled" }</p>
<p>204 No Content – When the report specified by the request ID is not running, either because it finished running, failed, or was stopped by another process.</p></td>
<td><p>404 Not Found – When the request ID specified in the request does not exist.</p></td>
</tr>
</tbody>
</table>

## Removing a Report Execution

Deleting a report that has run removes it from the cache and makes its output no longer available. If the report execution is still running, it is stopped automatically then removed.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>DELETE</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/reportExecutions/</span>requestID</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jrio/<span>rest_v2/reportExecutions/</span>&lt;executionID&gt;</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>204 No Content – The report execution was successfully removed.</p></td>
<td><p>404 Not Found – When the request ID specified in the request does not exist.</p></td>
</tr>
</tbody>
</table>
