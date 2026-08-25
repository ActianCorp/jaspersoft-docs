---
title: Ad Hoc Filter With All Values Causing Error
description: "When using filters in the Ad Hoc Editor, your browser sends lists of values to the server with a POST operation. If you filter a field with tens or hundreds of thousands of distinct values, and then..."
---

# Ad Hoc Filter With All Values Causing Error

When using filters in the Ad Hoc Editor, your browser sends lists of values to the server with a `POST` operation. If you filter a field with tens or hundreds of thousands of distinct values, and then select all values, your browser sends megabytes of data in the `POST` operation. Some application servers are configured to reject such large inputs by default.

For example, if you select 100,000 values in an Ad Hoc filter on a default installation on Tomcat, Tomcat logs an error and redirect the user to the JasperReports Server home page. The Tomcat error log may contain the following entry:

``` text
2013-09-30 15:12:33,847 ERROR errorPage_jsp,http-8080-6:559 - stack trace of
exception that redirected to errorPage.jsp
java.lang.NullPointerException
```

If you apply filters to fields with large numbers of distinct values, make sure that your app server is configured to accept large input. The following table shows how to configure the Apache Tomcat. For other app servers, refer to your app server's documentation about `POST` operations.

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
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>           <span class="ot">maxPostSize=</span><span class="st">&quot;0&quot;</span> /&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>or         maxPostSize=&quot;-1&quot; /&gt;</span></code></pre></div></td>
<td colspan="2"><p>Add the <code>maxPostSize</code> parameter to set the number of bytes accepted by the app server.</p>
<p>For Tomcat 8 and 9, "-1" indicates that there is no limit (<a href="http://tomcat.apache.org/tomcat-9.0-doc/config/ajp.html">Tomcat 9 documentation</a>).</p></td>
</tr>
</tbody>
</table>
