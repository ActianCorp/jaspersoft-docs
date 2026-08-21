---
title: REST Web Services Overview
description: "The RESTful interface of JasperReports Server responds to HTTP requests from client applications, in particular the following methods (sometimes called verbs):"
---

# 1.1 REST Web Services Overview

The RESTful interface of JasperReports Server responds to HTTP requests from client applications, in particular the following methods (sometimes called verbs):

- GET to list, search and acquire information about repository resources.
- POST to create new resources and execute reports.
- PUT to modify resources (note that PUT and POST were reversed in the v1 REST API).
- DELETE to remove resources.

In order to introduce new features and keep backwards compatibility, Jaspersoft® has introduced a second RESTful API using the rest_v2 URL.

By default, the REST web services are available at the following URLs, where `<host>` is the name of the computer hosting JasperReports Server and `<port>` is the port you specified during installation. By default, the context name is `jasperserver` for the Community Project and `jasperserver-pro` for commercial editions. The context name may also be customized on your specific installation of JasperReports® Server.

<table>
<caption><p><em>Table 1-1 REST v2 - Web Services and URLs</em></p></caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>Web Service</p></th>
<th><p>URLs</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Login (optional)</p></td>
<td><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest/GetEncryptionKey</p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest/login</p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/j_spring_security_check</p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/logout.html</p></td>
</tr>
<tr>
<td><p>Repository</p></td>
<td><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/resources</p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/rest_v2/domains/.../metadata *</p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/permissions</p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/export</p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/import</p></td>
</tr>
<tr>
<td><p>Reports</p></td>
<td><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/reports</p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/reportExecutions</p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/reports/.../inputControls</p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/reports/.../options</p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/jobs</p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/rest_v2/queryExecutor *</p></td>
</tr>
<tr>
<td><p>Administration<br />
without<br />
organizations</p></td>
<td><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/users</p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/users/.../attributes</p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/roles</p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/attributes</p></td>
</tr>
<tr>
<td><p>Administration<br />
with<br />
organizations *</p></td>
<td><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/rest_v2/organizations</p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/rest_v2/organizations/.../attributes</p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/rest_v2/organizations/.../users</p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/rest_v2/organizations/.../users/.../attributes</p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/rest_v2/organizations/.../roles</p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/rest_v2/attributes</p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/rest_v2/serverInfo</p></td>
</tr>
<tr>
<td colspan="2"><p>* Available only in commercial editions of JasperReports® Server.</p></td>
</tr>
</tbody>
</table>

Applications may receive the machine-readable XML description of all supported REST v2 services in Web Application Desciption Language (WADL) at the following URL:

http://\<host\>:\<port\>/jasperserver\[-pro\]/rest_v2/application.wadl

The original REST (now called v1) API is being deprecated. These services are still supported but no longer include the latest features of the server.

<table>
<caption><p><em>Table 1-2 REST v1 - Deprecated Web Services and URLs</em></p></caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>Web Service</p></th>
<th><p>URLs</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Repository</p></td>
<td><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest/resources</p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest/resource</p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest/permission</p></td>
</tr>
<tr>
<td><p>Reports</p></td>
<td><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest/report</p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest/jobsummary</p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest/job</p></td>
</tr>
<tr>
<td><p>Administration<br />
without<br />
organizations</p></td>
<td><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest/user</p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest/attribute</p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest/role</p></td>
</tr>
<tr>
<td><p>Administration<br />
with<br />
organizations *</p></td>
<td><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/rest/organization</p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/rest/user</p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/rest/attribute</p>
<p>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/rest/role</p></td>
</tr>
<tr>
<td colspan="2"><p>* Available only in commercial editions of JasperReports® Server.</p></td>
</tr>
</tbody>
</table>

As with any RESTful service, not all methods (GET, PUT, POST, and DELETE) are supported on every service. The URLs usually include a path to the resource being acted upon, as well as any paramters that are accepted by the method. For example, to search for input control resources in the repository, your application would send the following HTTP request:

GET http://\<host\>:\<port\>/jasperserver-pro/rest_v2/resources?type=inputControl

The reference chapters in this book give the full description of the methods supported by each URL, the path or resource expected for each method, and the parameters that are required or optional. The description of each method includes a sample of the return value.

JasperReports Server REST services return standard HTTP status codes. In case of an error, a detailed message may be present in the body in form of plain text. Client error codes are of type 4xx, while server errors are of type 5xx. The following table lists all the standard HTTP codes.

<table>
<caption><p><em>Table 1-2 REST - HTTP Return Codes</em></p></caption>
<thead>
<tr>
<th colspan="2"><p>Success Messages</p></th>
<th colspan="2"><p>Client Error</p></th>
<th colspan="2"><p>Server Errors</p></th>
</tr>
<tr>
<th><p>Code</p></th>
<th><p>Message</p></th>
<th><p>Code</p></th>
<th><p>Message</p></th>
<th><p>Code</p></th>
<th><p>Message</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>100</p></td>
<td><p>Continue</p></td>
<td><p>400</p></td>
<td><p>Bad Request</p></td>
<td><p>500</p></td>
<td><p>Internal Server Error</p></td>
</tr>
<tr>
<td><p>101</p></td>
<td><p>Switching Protocols</p></td>
<td><p>401</p></td>
<td><p>Unauthorized</p></td>
<td><p>501</p></td>
<td><p>Not Implemented</p></td>
</tr>
<tr>
<td><p>200</p></td>
<td><p>OK</p></td>
<td><p>402</p></td>
<td><p>Payment Required</p></td>
<td><p>502</p></td>
<td><p>Bad Gateway</p></td>
</tr>
<tr>
<td><p>201</p></td>
<td><p>Created</p></td>
<td><p>403</p></td>
<td><p>Forbidden</p></td>
<td><p>503</p></td>
<td><p>Service Unavailable</p></td>
</tr>
<tr>
<td><p>202</p></td>
<td><p>Accepted</p></td>
<td><p>404</p></td>
<td><p>Not Found</p></td>
<td><p>504</p></td>
<td><p>Gateway Time-out</p></td>
</tr>
<tr>
<td><p>203</p></td>
<td><p>Non-Authoritative Information</p></td>
<td><p>405</p></td>
<td><p>Method Not Allowed</p></td>
<td><p>505</p></td>
<td><p>HTTP Version Not Supported</p></td>
</tr>
<tr>
<td><p>204</p></td>
<td><p>No Content</p></td>
<td><p>406</p></td>
<td><p>Not Acceptable</p></td>
<td colspan="2" rowspan="8"></td>
</tr>
<tr>
<td><p>205</p></td>
<td><p>Reset Content</p></td>
<td><p>407</p></td>
<td><p>Proxy Authentication Required</p></td>
</tr>
<tr>
<td><p>206</p></td>
<td><p>Partial Content</p></td>
<td><p>408</p></td>
<td><p>Request Time-out</p></td>
</tr>
<tr>
<td><p>300</p></td>
<td><p>Multiple Choices</p></td>
<td><p>409</p></td>
<td><p>Conflict</p></td>
</tr>
<tr>
<td><p>301</p></td>
<td><p>Moved Permanently</p></td>
<td><p>410</p></td>
<td><p>Gone</p></td>
</tr>
<tr>
<td><p>302</p></td>
<td><p>Found</p></td>
<td><p>411</p></td>
<td><p>Length Required</p></td>
</tr>
<tr>
<td><p>303</p></td>
<td><p>See Other</p></td>
<td><p>412</p></td>
<td><p>Precondition Failed</p></td>
</tr>
<tr>
<td><p>304</p></td>
<td><p>Not Modified</p></td>
<td><p>413</p></td>
<td><p>Request Entity Too Large</p></td>
</tr>
<tr>
<td><p>305</p></td>
<td><p>Use Proxy</p></td>
<td><p>414</p></td>
<td><p>Request-URI Too Large</p></td>
<td colspan="2" rowspan="4"></td>
</tr>
<tr>
<td><p>307</p></td>
<td><p>Temporary Redirect</p></td>
<td><p>415</p></td>
<td><p>Unsupported Media Type</p></td>
</tr>
<tr>
<td colspan="2" rowspan="2"></td>
<td><p>416</p></td>
<td><p>Requested Range Not Satisfiable</p></td>
</tr>
<tr>
<td><p>417</p></td>
<td><p>Expectation Failed</p></td>
</tr>
</tbody>
</table>
