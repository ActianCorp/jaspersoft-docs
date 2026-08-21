---
title: Viewing Job Status
description: "The following method returns the current runtime state of a job:"
---

# 1.0.1 Viewing Job Status

The following method returns the current runtime state of a job:

<table>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>GET</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/jobs/</span>&lt;jobID&gt;<span>/state/</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – Body contains the status descriptor.</p></td>
<td><p>404 Not Found – When the specified &lt;jobID&gt; does not exist.</p></td>
</tr>
</tbody>
</table>
