---
title: REST API Overview
description: The JasperReports Server REST API is an Application Programming Interface that follows the guidelines of REpresentational State Transfer design to allow client application to interact with the server...
---

# REST API Overview

The JasperReports Server REST API is an Application Programming Interface that follows the guidelines of REpresentational State Transfer design to allow client application to interact with the server through the HTTP protocol. With a few exceptions, the REST API allows clients to interact with all features of the server, such as running, exporting, and scheduling reports, reading and writing resources in the repository, and managing organizations, roles, and users. The REST API requires credentials for every operation and enforces the same permissions and administrator restrictions as the server's user interface.

Client applications send requests to named URLs that are called services. A service provides several operations on a feature, for example the roles service lists the roles in an organization, gives the properties and members of a role, writes new roles, updates existing roles, and deletes roles. This chapter lists all the services of the current REST API. The other chapters of this API Reference each describe one of the services.

In order to describe resources and objects in the server, the REST API sends and receives data structures called descriptors. Most services support descriptors in both XML (eXtensible Markup Language) and JSON (JavaScript Object Notation). The descriptors are specific to each service, and are defined in the corresponding chapter of this reference. Descriptors are usually sent and received in the body of HTTP requests and responses, so your client application usually relies on further APIs to handle the HTTP communications.

Historically, the REST API is considered a web service, and JasperReports Server provided several other web services. The current REST API is the second version and all services use the rest_v2/ prefix. The first REST API with the rest/ prefix and the earlier SOAP API (Simple Object Access Protocol) are deprecated and no longer maintained. Although the server might still respond to deprecated services, they are not updated for new features of the server and are never garanteed to succeed or be accurate. For completeness, the deprecated service names are listed at the end of this chapter.

This chapter includes the following sections:

-   List of Services
-   Sending REST Requests from a Browser
-   HTTP Response Codes
-   Deprecated Web Services

## List of Services

The REST API of JasperReports Server responds to HTTP requests from client applications, in particular the following methods (sometimes called verbs):

-   GET to list, search and acquire information about server resources.

-   POST to create new resources and execute reports.

-   PUT to modify existing resources.

-   DELETE to remove resources.

    As with any RESTful service, not all methods (GET, PUT, POST, and DELETE) are supported on every service. The URLs usually include a path to the resource being acted upon, as well as any parameters that are accepted by the method. For example, to search for input control resources in the repository, your application would send the following HTTP request:

    GET http://&lt;host&gt;:&lt;port&gt;/jasperserver\[-pro\]/rest_v2/resources?type=inputControl

    In all URLs in this API Reference:

-   `<host>` is the name of the computer hosting JasperReports Server

-   `<port>` is the port you specified during installation

-   `jasperserver[-pro]` indicates that the service is available in both Community and Commercial editions.

-   `jasperserver-pro` indicates that the service is available only in Commercial editions.

-   The context name (by default jasperserver or jasperserver-pro) may be customized in your specific installation of JasperReports Server

The REST services are available at the following URLs:

<table>
<caption><p>REST API Services and URLs</p></caption>
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
<td><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/login</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/logout.html</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/serverInfo</span></p></td>
</tr>
<tr>
<td><p>Repository</p></td>
<td><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/resources</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/rest_v2/domains/.../metadata</span> *</p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/permissions</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/export</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/import</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/keys</span></p></td>
</tr>
<tr>
<td><p>Reports</p></td>
<td><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/reports</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/reportExecutions</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/reports/.../inputControls</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/reports/.../options</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/jobs</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/alerts</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/alerts/{alertId}</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/alerts?id={ID_1}&amp;id={ID_2}&amp;...&amp;id={ID_n)</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/alerts/pause/</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/alerts/resume/</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/alerts/restart/</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/alerts/calendars</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/rest_v2/queryExecutor</span> *</p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/rest_v2/caches/vds</span> *</p></td>
</tr>
<tr>
<td><p>Administration<br />
without<br />
organizations</p></td>
<td><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/users</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/users/.../attributes</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/roles</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/attributes</span></p></td>
</tr>
<tr>
<td><p>Administration<br />
with<br />
organizations *</p></td>
<td><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/rest_v2/organizations</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/rest_v2/organizations/.../attributes</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/rest_v2/organizations/.../users</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/rest_v2/organizations/.../users/.../attributes</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/rest_v2/organizations/.../roles</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/rest_v2/attributes</span></p></td>
</tr>
<tr>
<td colspan="2"><p>* Available only in commercial editions of JasperReports Server.</p></td>
</tr>
</tbody>
</table>

For progammers creating a client application, the reference chapters in this guide give the full description of the methods supported by each REST service, the path or resource expected for each method, and the parameters that are required or optional in the URL. The description of each method includes an example of the descriptors it uses and a sample of the return value.

For tools that can parse the Web Application Description Language (WADL), the following URL gives a machine-readable XML description of all supported REST v2 services:

http://&lt;host&gt;:&lt;port&gt;/jasperserver\[-pro\]/rest_v2/application.wadl

## Sending REST Requests from a Browser

Normally, you program your client application to send REST requests to your instance of JasperReports Server. You may also want to test certain requests or examine the response from the server, and some browsers have plug-ins to send a REST request and view the response.

However, the server includes cross-session request forgery (CSRF) protection that does not allow requests, including REST, from a browser in a different domain. Sending POST, PUT, or DELETE requests from a browser will often fail for this reason. REST requests from REST-client applications are secure and are not stopped by CSRF protection.

To allow testing of the REST API through a browser, configure your browser REST client to include the following header in every request:

`X-REMOTE-DOMAIN: 1`

## HTTP Response Codes

JasperReports Server REST services return standard HTTP status codes. In case of an error, a detailed message may be present in the body as plain text. Client error codes are of type 4xx, while server errors are of type 5xx. The following table lists all the standard HTTP codes. Each service returns typical success and error messages that are given in the reference chapter for that service.

<table>
<caption><p>HTTP Response Codes</p></caption>
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
<td colspan="2" rowspan="12"></td>
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
<td><p>Request URI Too Large</p></td>
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

## Deprecated Web Services

The server's first REST API (now called v1) is deprecated. These services are no longer supported, do not work with the latest features of the server, and are never guaranteed to succeed. Note that meanings of PUT and POST were reversed in the REST v1 API.

<table>
<caption><p>Deprecated REST v1 Services</p></caption>
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
<td><p>Login</p></td>
<td><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest/login</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/j_spring_security_check</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/GetEncryptionKey</span></p></td>
</tr>
<tr>
<td><p>Repository</p></td>
<td><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest/resources</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest/resource</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest/permission</span></p></td>
</tr>
<tr>
<td><p>Reports</p></td>
<td><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest/report</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest/jobsummary</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest/job</span></p></td>
</tr>
<tr>
<td><p>Administration<br />
without<br />
organizations</p></td>
<td><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest/user</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest/attribute</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest/role</span></p></td>
</tr>
<tr>
<td><p>Administration<br />
with<br />
organizations *</p></td>
<td><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/rest/organization</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/rest/user</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/rest/attribute</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/rest/role</span></p></td>
</tr>
<tr>
<td colspan="2"><p>* Available only in commercial editions of JasperReports Server.</p></td>
</tr>
</tbody>
</table>

The original SOAP web services at the following URLs are also deprecated and no longer supported. The SOAP web services will no longer be maintained or updated to work with new features of the server. In particular, the SOAP web services do not support interactive charts or interactive HTML5 tables. Though the server may still respond to these methods, they are never guaranteed to work.

The SOAP web services often refer to the http://www.jasperforge.org/jasperserver/ws namespace. This namespace is only an identifier; it is not intended to be a valid URL.

<table>
<caption><p>Deprecated SOAP Web Services</p></caption>
<thead>
<tr>
<th><p>Edition</p></th>
<th><p>Web Service</p></th>
<th><p>URL</p></th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="3"><p>Community Project</p></td>
<td><p>Repository</p></td>
<td><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver/services/repository</span></p></td>
</tr>
<tr>
<td><p>Scheduling</p></td>
<td><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver/services/ReportScheduler</span></p></td>
</tr>
<tr>
<td><p>Administration</p></td>
<td><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver/services/UserAndRoleManagementService</span></p></td>
</tr>
<tr>
<td rowspan="4"><p>Commercial Editions</p></td>
<td><p>Repository</p></td>
<td><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/services/repository</span></p></td>
</tr>
<tr>
<td><p>Scheduling</p></td>
<td><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/services/ReportScheduler</span></p></td>
</tr>
<tr>
<td><p>Domains</p></td>
<td><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/services/DomainServices</span></p></td>
</tr>
<tr>
<td><p>Administration</p></td>
<td><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/services/UserAndRoleManagementService</span></p></td>
</tr>
</tbody>
</table>
