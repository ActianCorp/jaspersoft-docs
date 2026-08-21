---
title: Enabling Compression in Tomcat
description: The Tomcat app server can be configured to compress web content sent to browsers in order to reduce bandwidth usage and reduce loading times. Tomcat compression has been tested with JasperReports...
---

# Enabling Compression in Tomcat

The Tomcat app server can be configured to compress web content sent to browsers in order to reduce bandwidth usage and reduce loading times. Tomcat compression has been tested with JasperReports Server and found to reduce transferred data to about one third of the original size. For example, the login page and its scripts and images are about 3 MB normally and 1 MB compressed; the Domain designer page and scripts are 6.2 MB normally and 1.7 MB compressed. Large reports with lots of data may compress even more.

The performance benefit of compression depends upon the content and your client's connection. For small pages on a local network, the data transfer time is minimal, and the overhead of decompression may actually cause pages to load a few milliseconds longer. For large pages on a local network, compression can help load a few milliseconds faster. However, compression can improve loading times noticeably on networks with low latency or bandwidth, for example if you access reports on the server from a mobile device. In this case, loading time can be reduced by seconds, for example from 10 to 5 seconds.

Compression can also be enabled on cloud or hosted services to reduce bandwidth usage and costs.

Compression is a configuration on the Tomcat app server that is off by default. To enable compression, shut down your Tomcat instance and modify the following file:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th colspan="2"><p>Compression in Tomcat</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="2"><p><code>.../apache-tomcat/conf/server.xml</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">Connector</span> <span class="ot">compressibleMimeType=</span><span class="st">&quot;text/html,text/xml,text/css,</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a><span class="st">    text/javascript,application/javascript,application/json&quot;</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a><span class="ot">compression=</span><span class="st">&quot;on&quot;</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="ot">compressionMinSize=</span><span class="st">&quot;128&quot;</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a><span class="ot">connectionTimeout=</span><span class="st">&quot;20000&quot;</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a><span class="ot">noCompressionUserAgents=</span><span class="st">&quot;gozilla, traviata&quot;</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a><span class="ot">port=</span><span class="st">&quot;8080&quot;</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a><span class="ot">redirectPort=</span><span class="st">&quot;8443&quot;</span> <span class="ot">protocol=</span><span class="st">&quot;HTTP/1.1&quot;</span> /&gt;</span></code></pre></div></td>
<td><p>Add this connector to the Catalina service. You can modify the settings as needed, but these default values have been tested to work.</p></td>
</tr>
</tbody>
</table>

Restart the Tomcat app server after saving the file.

Compression is not compatible with the use of `sendfile` to reduce processor load in Tomcat. If you specify the `useSendFile` parameter, it takes precedence and content will not be compressed. For more information, see the [Tomcat documentation](https://tomcat.apache.org/tomcat-8.5-doc/config/http.html#Standard_Implementation).
