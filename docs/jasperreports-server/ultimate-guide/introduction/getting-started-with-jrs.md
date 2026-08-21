---
title: Getting Started
description: "JasperReports Server must be installed and configured before you can use it. For information, see the JasperReports Server Installation Guide for your product edition."
---

# Getting Started

JasperReports Server must be installed and configured before you can use it. For information, see the JasperReports Server Installation Guide for your product edition.

The directory where JasperReports Server is installed is referred to as \<js-install\> in this guide. The default installation directory is:

|          |                                              |
|----------|----------------------------------------------|
| Windows: | `C:\Program Files\jasperreports-server-`10.1 |
| Linux:   | `<USER_HOME>/jasperreports-server-`10.1      |
| Mac:     | `/Applications/jasperreports-server-`10.1    |

To connect to JasperReports Server, make sure your database and application server are running, then enter the corresponding URL in a supported browser:

Commercial Editions: `http://<hostname>:<port>/jasperserver-pro/login.html`

Community Project: `http://<hostname>:<port>/jasperserver/login.html`

Where:

`<hostname>` is the name of the computer hosting the application server where JasperReports Server is installed.

`<port>` is the number of the port specified when the application server was installed.

For example, if you installed the Jaspersoft BI Suite evaluation software, the default URL is:

`http://localhost:8080/jasperserver-pro/login.html`

If JasperReports Server is secured using Secure Socket Layer (SSL) encryption, both the protocol and the port differ. For example, a typical SSL-secured URL for JasperReports Server Professional follows this format:

`https://localhost:443/jasperserver-pro/login.html`

On the JasperReports Server Login page, enter a user ID and password and click **Login**. The following table lists the credentials for the evaluation server:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th><p>User ID</p></th>
<th><p>Password</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>superuser</code></p></td>
<td><p>superuser</p></td>
<td><p>System-wide administrator (commercial editions only)</p></td>
</tr>
<tr>
<td><p><code>jasperadmin</code></p></td>
<td><p>jasperadmin</p></td>
<td><p>Administrator for the default organization (commercial editions)</p>
<p>System-wide administrator (community project)</p></td>
</tr>
<tr>
<td><p><code>joeuser</code></p></td>
<td><p>joeuser</p></td>
<td><p>Sample end-user</p></td>
</tr>
<tr>
<td><p><code>demo</code></p></td>
<td><p>demo</p></td>
<td><p>Sample end-user for the SuperMart Dashboard demonstration</p></td>
</tr>
</tbody>
</table>

!!! note

    Depending on the configuration of your system, the Login page may also enable you to change your password. If there is a **Change password** link, click the link to enter a new password. If there is no link, only your system administrator can change the password.
