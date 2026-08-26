---
title: Overview of JasperReports Server Security
description: "JasperReports® Server ensures that people can access only the data they are allowed to see. The settings that define organizations, users, roles, and repository resources work together to provide..."
---

# Overview of JasperReports Server Security

JasperReports® Server ensures that people can access only the data they are allowed to see. The settings that define organizations, users, roles, and repository resources work together to provide complete access control that includes:

-   Authentication – Restricts access to identified users and protects that access with passwords. Defines roles for grouping users and assigning permissions.
-   Authorization – Controls access to repository objects, pages, and menus based on users and roles.
-   Data level security (commercial version only) – Defines row and column level permissions to access your data. Row and column level permissions can be defined and enforced in Domains.

Administrators must keep security in mind at all times when managing organizations, users, roles, and resources, because the security settings behind each of these rely on the others.

!!! warning "Caution"

    The bundled installer is not meant for use in either production environments or security testing. It is only intended for evaluation purposes. The application server provided in that package has been configured with minimal security. We recommend that production environments use the WAR package deployed to an application server configured to your security standards.

!!! warning "Caution"

    This guide focuses on security concerns specific to JasperReports Server. However, you should consider other security precautions in your environment. For example, an end user can potentially exploit JasperReports Server's **Test Connection** option when scheduling reports to an FTP server. If this is a concern, you can secure the port (by default, port 21) at the operating system level.

!!! note

    The chapter on data-level security for Domains has been moved from this guide to the new document JasperReports Server Data Management Using Domains. That guide covers all aspects of Domains, including creating the security file.

This chapter contains the following sections:

-   Authentication

-   Authorization Overview

## Authentication

The first part of security is to define user accounts and secure them with passwords to give each user an identity within the JasperReports® Server. The server stores user definitions, including encrypted passwords, in a private database. Administrators create, modify, and delete user accounts through the administrator pages, as described in the JasperReports Server Administrator Guide.

JasperReports® Server also implements roles for creating groups or classes of users with similar permissions. A user can belong to any number of roles and have the privileges of each. The server stores the role definition in its private database, and administrators create, modify, and delete roles through the administrator pages, as described in the JasperReports Server Administrator Guide.

JasperReports® Server relies on the open source Spring security framework. It has many configurable options for:

-   External authentication services such as LDAP (used by Microsoft Active Directory and Novell eDirectory)
-   Single Sign-on using JA-SIG's Central Authentication Service (CAS)
-   Java Authentication and Authorization Service (JAAS)
-   Container security (Tomcat, Jetty)
-   SiteMinder
-   Anonymous user access (disabled by default)

JasperReports® Server also supports these encryption and authentication standards:

-   HTTPS, including requiring HTTPS
-   HTTP Basic
-   HTTP Digest
-   X509

The Spring framework is readily extensible to integrate with custom and commercial authentication services and transports.

Authentication occurs by default through the web user interface, forcing login, and/or through HTTP Basic authentication for web services, such as Jaspersoft® Studio and for XML/A traffic. The server can automatically synchronize with an external authentication service. External users don’t need to be created manually in the server first. Both users and roles are created automatically in the server from their definitions in an external authentication service. For an overview of the authentication system and details about external authentication, see the JasperReports® Server External Authentication Cookbook.

## Authorization Overview

With a user’s identity and roles established, JasperReports® Server controls the user’s access in these ways:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td><p>Menu options and pages</p></td>
<td><p>The menus appear in the JasperReports® Server UI depending on the user’s roles. For example, only users with the administrator role can see the <strong>Manage</strong> menu and access the administrator pages. By modifying the server’s configuration, you can modify access to menus, menu items, and individual pages. See the JasperReports® Server Source Build Guide and <span>JasperReports Server Ultimate Guide</span> for more information.<br />
</p></td>
</tr>
<tr>
<td><p>Organization scope</p></td>
<td><p>Users belong to organizations and are restricted to resources within their organizations. Organizations have their own administrators who each see only the users, roles, and resources of their own organization. When the JasperReports® Server is configured with multiple organizations, those organizations are effectively isolated from each other, although the system administrator can share resources through the Public folder. For more information, see the JasperReports Server Administrator Guide.<br />
</p></td>
</tr>
<tr>
<td><p>Resource permissions</p></td>
<td><p>Administrators can define access permissions on every folder and resource in the repository. You can define permissions for every role and every user, or leave them undefined to be inherited from the parent folder. For example, a user may have read-write access to a folder where they create reports, but the administrator can also create shared reports in the same folder that are set to read-only. The possible permissions are: no access, execute only, read-only, read-delete, read-write-delete, and administer (see "Repository Administration" in the JasperReports Server Administrator Guide).</p>
<p>Permissions are enforced when accessing any resource whether directly through the repository interface, indirectly when called from a report, or programmatically through the web services. A user's access to resources is limited by the permissions defined in the user's roles.<br />
</p></td>
</tr>
<tr>
<td><p>Administrator privileges</p></td>
<td><p>JasperReports® Server distinguishes between reading or writing a resource in the repository and viewing or editing the internal definition of a resource. For security purposes, granting a user read or write permission on a resource does not allow viewing or editing the resource definition. For example, users need execute or read permission on a data source to run the reports that use it, but they cannot view the data source’s definition, which includes a database password. Also, only administrators can interact with theme folders to upload, download, and activate CSS files that control the UI's appearance.<br />
</p></td>
</tr>
<tr>
<td><p>Data-level security</p></td>
<td><p>Data-level security determines the data that can be retrieved and viewed in a report, based on the username and roles of the user running the report. For example, a management report could allow any user to see the management hierarchy, managers would see the salary information for their direct employees, and only human resource managers would see all salary values.</p>
<p>Data-level security in Domains is explained in the new JasperReports Server Data Management Using Domains.</p>
<p>**Note** <div> This type of security is available only in the commercial edition of JasperReports® Server. </div></p></td>
</tr>
<tr>
<td><p>User attributes</p></td>
<td><p>User attributes are name-value pairs associated with a user, organization, or server.</p>
<p>User attributes provide additional information about the user and can also be used to restrict a user's access to data through Domain security files and OLAP schemas. For information on defining user attributes, see "Editing User Attributes" in the JasperReports Server Administrator Guide.</p>
<p>User, organization, and server attributes can be used to customize the definition of a data source or as parameters of a report. See "Attributes in Data Source Definitions" and "Attribute-Based Parameters for Queries and Reports" in the JasperReports Server Administrator Guide</p></td>
</tr>
</tbody>
</table>
