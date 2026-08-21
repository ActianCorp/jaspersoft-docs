---
title: Report Output
description: "The files produced are attached to the response. Specify the final format of the report by setting the request RUNOUTPUTFORMAT argument. Its possible values are: PDF, JRPRINT, HTML, XLS, XML, CSV and..."
---

# 1.0.1 Report Output

The files produced are attached to the response. Specify the final format of the report by setting the request `RUN_OUTPUT_FORMAT` argument. Its possible values are: `PDF`, `JRPRINT`, `HTML`, `XLS`, `XML`, `CSV` and `RTF.` The default is `PDF`.

If the final format is set to `JRPRINT`, the data attached to the response contains a serialized instance of a JasperPrint object. This is the best format to use for clients in Java environments, because it provides the Java client with access to all of JasperReports’ export options, and only relies on the server to fill the report.

The following Java code shows how to access the serialized object and get the JasperPrint object:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><pre class="text"><code>FileContent content = null;
if (attachments != null &amp;&amp; !attachments.isEmpty()) {
content = (FileContent)(attachments.values().toArray()[0]);
}
if (content == null) {
throw new Exception(&quot;No JasperPrint&quot;);
}</code></pre></td>
</tr>
<tr>
<td><pre class="text"><code>InputStream is = new ByteArrayInputStream(content.getData());
JasperPrint print = (JasperPrint) JRLoader.loadObject(is);</code></pre></td>
</tr>
</tbody>
</table>

If the specified output format is HTML, the URI for images can be set using the `RUN_OUTPUT_IMAGES_URI` argument: the default value is `images/`. If images are found, they are attached to the response.

If only a single page should be printed, use the `RUN_OUTPUT_PAGE` argument, which must contain the index of page to fill.
