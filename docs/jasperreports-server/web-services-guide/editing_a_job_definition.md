---
title: Editing a Job Definition
description: "To modify an existing job definition, use the GET method to read its job descriptor, modify the descriptor as required, and use the POST method of the job service. The POST method replaces the..."
---

# 1.0.1 Editing a Job Definition

To modify an existing job definition, use the GET method to read its job descriptor, modify the descriptor as required, and use the POST method of the job service. The POST method replaces the definition of the job with the given job ID.

<table>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>POST</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest/job</span>/&lt;jobID&gt;/</p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p>text/plain</p></td>
<td colspan="2"><p>A well-formed XML job descriptor.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK</p></td>
<td><p>404 Not Found – When the specified job is not found in the server.</p></td>
</tr>
</tbody>
</table>
