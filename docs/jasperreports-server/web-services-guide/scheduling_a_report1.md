---
title: Scheduling a Report
description: "To schedule a report, create its job descriptor similar to the one returned by the GET method, and use the PUT method of the V2/jobs service. Specify the report being scheduled inside the job..."
---

# 1.0.1 Scheduling a Report

To schedule a report, create its job descriptor similar to the one returned by the GET method, and use the PUT method of the V2/jobs service. Specify the report being scheduled inside the job descriptor. You do not need to specify any job IDs in the descriptor, because the server will assign them.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>PUT</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/jobs/</span></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p>application/xml</p>
<p>application/job+json</p></td>
<td colspan="2"><p>A well-formed XML or JSON job descriptor such as the one shown in <a href="viewing_a_job_definition1.md">“Viewing a Job Definition” on page 1</a>.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>201 Created – The body contains the XML job descriptor of the newly created job. It is similar to the one that was sent but now contains the jobID for the new job.</p></td>
<td><p>404 Not Found – When the report specified in the job descriptor is not found in the server.</p></td>
</tr>
</tbody>
</table>
