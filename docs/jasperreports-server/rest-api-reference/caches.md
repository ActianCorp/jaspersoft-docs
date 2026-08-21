---
title: The caches Service
description: "The restv2/caches service allows you to clear the caches used by virtual data sources. Virtual data sources use the Teiid engine that lets you combine data from several data sources such as JDBC,..."
---

# The caches Service

The rest_v2/caches service allows you to clear the caches used by virtual data sources. Virtual data sources use the Teiid engine that lets you combine data from several data sources such as JDBC, JNDI, and several flavors of big data. To join the data, the Teiid engine uses an internal cache to store data. You can use this service to clear this cache, for example after updating your data sources.

For now, this service provides only cache deletion for virtual data sources.

<table>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>DELETE</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/<span>rest_v2/caches/vds</span>/</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>204 No Content - There is nothing to return.</p></td>
<td><p>404 Not Found - When the specified cache does not exist.</p></td>
</tr>
</tbody>
</table>
