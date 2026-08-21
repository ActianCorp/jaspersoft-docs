---
title: Print View Not Displaying in Dashboards
description: "If you cannot display the Print view for a dashboard, there might be an issue with the size of the input control values. Input control values are passed as URL parameters on this page, and the..."
---

# Print View Not Displaying in Dashboards

If you cannot display the Print view for a dashboard, there might be an issue with the size of the input control values. Input control values are passed as URL parameters on this page, and the application server can limit the length of the URL that includes the parameters.

To avoid this limit and allow large numbers of input control values in dashboard print view, edit the following configuration file or the equivalent in your application server.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>Configure Apache Tomcat to Accept Large Filter Values</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>&lt;tomcat&gt;/conf/server.xml</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">Connector</span> <span class="ot">port=</span><span class="st">&quot;8080&quot;</span> <span class="ot">protocol=</span><span class="st">&quot;HTTP/1.1&quot;</span> </span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>           <span class="ot">connectionTimeout=</span><span class="st">&quot;20000&quot;</span> </span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>           <span class="ot">redirectPort=</span><span class="st">&quot;8443&quot;</span> </span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>           <span class="ot">URIEncoding=</span><span class="st">&quot;UTF-8&quot;</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>           <span class="ot">maxPostSize=</span><span class="st">&quot;0&quot;</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>           <span class="ot">maxHttpHeaderSize=</span><span class="er">65535</span> /&gt;</span></code></pre></div></td>
<td colspan="2"><p>Add the <code>maxHttpHeaderSize</code> parameter to set the number of bytes accepted in the URL by the app server; <code>"65535"</code> is equivalent to 64 KB. For more information, see the <a href="https://tomcat.apache.org/tomcat-9.0-doc/config/http.html">Tomcat documentation</a>.</p></td>
</tr>
</tbody>
</table>
