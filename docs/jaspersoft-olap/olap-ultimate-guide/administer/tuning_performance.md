---
title: Tuning Performance
description: This section provides a framework for performance tuning of Jaspersoft OLAP for the technically skilled reader who understands the basics of SQL and RDBMS tuning and has used the Jaspersoft OLAP...
---

# Tuning Performance

## Understand Jaspersoft OLAP Performance

This section provides a framework for performance tuning of Jaspersoft OLAP for the technically skilled reader who understands the basics of SQL and RDBMS tuning and has used the Jaspersoft OLAP interface to perform some queries.

The first step is to gain a high-level understanding of the common performance bottlenecks in a typical installation of Jaspersoft OLAP. The user submits an MDX query, either through the MDX query editor or implicitly by taking an action in the navigation table, such as drilling-down, expanding, and doing cross-joins. This MDX query is passed to the OLAP engine, with either a local Mondrian connection, or over a network using XML/A. The OLAP engine then processes the query, retrieving whatever it can from its memory cache and generating SQL queries to look up anything else from the database. These SQL queries are then executed on the database server, and the results are returned to the OLAP engine and may be cached in its memory space. The OLAP engine further processes the data to assemble the SQL and cache lookups into an OLAP Result object. The result is then returned to the front-end by the same means that it received the request: either locally in-memory or using XML/A. The front-end server does further processing to layout the new view.

The following table described the complete round trip MDX request and response in Jaspersoft OLAP, along with commentary on which computing resources are most relevant for bottleneck analysis.

Steps in an MDX Query and Response

<table>
<thead>
<tr>
<th colspan="2"><p>Step</p></th>
<th><p>Resources Relevant to Bottleneck Analysis</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>1</p></td>
<td><p>MDX is generated</p></td>
<td rowspan="2"><p>CPU and memory of front-end negligible</p></td>
</tr>
<tr>
<td rowspan="2"><p>2</p></td>
<td><p>MDX is passed to the local OLAP engine</p></td>
</tr>
<tr>
<td><p>MDX is passed remotely using XML/A</p></td>
<td><p>Network latency between front-end and OLAP engine</p></td>
</tr>
<tr>
<td><p>3</p></td>
<td><p>MDX is processed by the OLAP engine</p></td>
<td><p>CPU and memory of OLAP engine</p></td>
</tr>
<tr>
<td><p>4</p></td>
<td><p>SQL sent to database server</p></td>
<td><p>Network latency between OLAP engine and database</p></td>
</tr>
<tr>
<td><p>5</p></td>
<td><p>SQL queries executed by database</p></td>
<td><p>Disk <span> I/O</span>, CPU, memory of database server</p></td>
</tr>
<tr>
<td rowspan="2"><p>6</p></td>
<td><p>SQL results returned to OLAP engine</p></td>
<td><p>Network latency and bandwidth between OLAP and database</p></td>
</tr>
<tr>
<td><p>OLAP Result object constructed</p></td>
<td><p>CPU and memory of OLAP engine</p></td>
</tr>
<tr>
<td rowspan="2"><p>7</p></td>
<td><p>Result passed to local front-end</p></td>
<td><p>Memory of <span>engine/front-end</span></p></td>
</tr>
<tr>
<td><p>Result returned using XML/A</p></td>
<td><p>Network latency and bandwidth between OLAP and UI</p></td>
</tr>
<tr>
<td><p>8</p></td>
<td><p>Result is processed and displayed</p></td>
<td><p>CPU and memory of front-end</p></td>
</tr>
</tbody>
</table>

One question about performance that may come up here regards the difference between local Mondrian connections and XML/A. With Mondrian connections, the front-end and OLAP engine routines run in the same application server, sharing the same memory and CPU resources. While this happens serially for each single request, the requests of multiple users occur in parallel. So, in multi-user installations, there is a performance gain to be made by separating the front-end server from the OLAP engine server using XML/A. XML/A incurs the additional processing overhead of converting requests and responses to XML, and then transmitting them through HTTP, but this is quickly outweighed by the performance benefits of parallelism when there are multiple simultaneous users. Another advantage of XML/A in performance and scalability optimization is that a front-end can have its request load balanced using HTTP to one of the many OLAP engines in a cluster. See [Load Balancing](jaspersoft_olap_tuning_process_and_o.md).
