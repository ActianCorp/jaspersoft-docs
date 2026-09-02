---
title: SOAP Web Services Overview
description: "With the completion of the REST v2 API in JasperReports® Server 5.5, Jaspersoft® announces the end of life of the SOAP web services. The SOAP web services will no longer be maintained or updated to..."
---

# 1.1 SOAP Web Services Overview

!!! warning

    With the completion of the REST v2 API in JasperReports® Server 5.5, Jaspersoft® announces the end of life of the SOAP web services. The SOAP web services will no longer be maintained or updated to support new features of the server. In particular, the SOAP web services do not support interactive charts or interactive HTML5 tables.

For now, the SOAP web services are still available at the following URLs, where `<host>` is the name of the computer hosting JasperReports Server and `<port>` is the port you specified during installation:

**SOAP - Deprecated Web Services and URLs**

<table>
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
<td><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver/services/repository</p></td>
</tr>
<tr>
<td><p>Scheduling</p></td>
<td><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver/services/ReportScheduler</p></td>
</tr>
<tr>
<td><p>Administration</p></td>
<td><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver/services/UserAndRoleManagementService</p></td>
</tr>
<tr>
<td rowspan="4"><p>Commercial Editions</p></td>
<td><p>Repository</p></td>
<td><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/services/repository</p></td>
</tr>
<tr>
<td><p>Scheduling</p></td>
<td><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/services/ReportScheduler</p></td>
</tr>
<tr>
<td><p>Domains</p></td>
<td><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/services/DomainServices</p></td>
</tr>
<tr>
<td><p>Administration</p></td>
<td><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/services/UserAndRoleManagementService</p></td>
</tr>
</tbody>
</table>

!!! note

    The context name (by default jasperserver or jasperserver-pro) may also depend on the specific installation of JasperReports Server.

The web services take as input an XML document (the request) and return another XML document (the operation result). Because they use XML, the web services provide easy, natural integration with the most common programming languages and environments.

Jaspersoft provides two complete sample applications that demonstrate the SOAP web service: a simple J2EE (Java 2 Enterprise Edition) web application and the same application written in PHP (PHP Hypertext Preprocessor).

The SOAP web services often refer a namespace with the value of `http://www.jasperforge.org/jasperserver/ws` namespace. This namespace is only an identifier; it is not intended to be a valid URL.
