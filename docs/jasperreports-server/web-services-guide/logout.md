---
title: Logout
description: "While REST calls are often stateless, JasperReports® Server uses a session to hold some information such as generated reports. The session and its report data take up space in memory and it's good..."
---

# Logout

While REST calls are often stateless, JasperReports® Server uses a session to hold some information such as generated reports. The session and its report data take up space in memory and it's good practice to explicitly close the session when it is no longer needed. This allows the server to free up and reuse resources much faster.

To close a session and free its resources, invoke the logout page and include the JSESSIONID cookie in the request.

<table>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
<td></td>
</tr>
<tr>
<td><p>GET</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>/logout.htm</span></p></td>
<td></td>
</tr>
<tr>
<td colspan="4">Header</td>
<td> </td>
</tr>
<tr>
<td colspan="4">Cookie: $Version=0; JSESSIONID=52E79BCEE51381DF32637EC69AD698AE; $Path=/jasperserver</td>
<td> </td>
</tr>
</tbody>
</table>
