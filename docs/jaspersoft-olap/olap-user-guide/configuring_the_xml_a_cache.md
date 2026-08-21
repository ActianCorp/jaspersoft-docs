---
title: Configuring the XML/A Cache
description: "When JasperReports Server connects to an XML/A provider to retrieve data that populate views and reports, it relies on a cache to improve performance. When data is first requested from the XML/A..."
---

# Configuring the XML/A Cache

When JasperReports Server connects to an XML/A provider to retrieve data that populate views and reports, it relies on a cache to improve performance. When data is first requested from the XML/A provider, it is retrieved and cached. Subsequent requests for the data are then fulfilled from the cache until it is refreshed. You can configure the frequency and behavior of the cache’s refresh mechanism by editing a properties file, as shown in the following table.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>XML/A Cache Configuration</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>…\WEB-INF\applicationContext-olap-connection.xml</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Value</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>OLAP4J_CACHE</code></p></td>
<td><p><code>org.olap4j.driver.xmla.cache. XmlaOlap4jNamedMemoryCache</code><br />
<br />
</p></td>
<td><p>Do not change this value.</p></td>
</tr>
<tr>
<td><p><code>OLAP4J_CACHE_NAME</code></p></td>
<td><p><code>org.olap4j.driver.xmla.cache. XmlaOlap4jNamedMemoryCache</code><br />
<br />
</p></td>
<td><p>Do not change this value.</p></td>
</tr>
<tr>
<td><p><code>OLAP4J_CACHE_MODE</code></p></td>
<td><p><code>LFU</code></p></td>
<td><p>Specifies the eviction policy to use when determining what data to evict from the cache. Valid values are:</p>
<ul>
<li><code>LIFO</code>: Last In First Out</li>
<li><code>FIFO</code>: First In First Out</li>
<li><code>LFU</code>: Least Frequently Used</li>
<li><code>MFU</code>: Most Frequently Used</li>
</ul></td>
</tr>
<tr>
<td><p><code>OLAP4J_CACHE_SIZE</code></p></td>
<td><p>Commercial Editions: <code>10000</code></p>
<p>Community Project: <code>1000</code></p></td>
<td><p>The number of cache entries to maintain. The number of entries generated is determined by the number of queries sent to the XML/A provider via SOAP.</p></td>
</tr>
<tr>
<td><p><code>OLAP4J_CACHE_TIMEOUT</code></p></td>
<td><p>Commercial Editions: <code>3600</code></p>
<p>Community Project: <code>600</code></p></td>
<td><p>The length of time, expressed in seconds, to keep an entry in the cache. The default is one hour in commercial editions and ten minutes in the community project.</p></td>
</tr>
</tbody>
</table>
