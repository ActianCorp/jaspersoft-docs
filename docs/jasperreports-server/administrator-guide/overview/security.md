---
title: Overview of Security
description: "JasperReports Server ensures that people can access only the data they are allowed to see. The mechanisms that define organizations, users, roles, and repository resources work together to provide..."
---

# Overview of Security

JasperReports Server ensures that people can access only the data they are allowed to see. The mechanisms that define organizations, users, roles, and repository resources work together to provide complete access control. Security has many facets covered in this guide and other guides:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td>Authentication</td>
<td><p>Authentication is the process of restricting access to identified users. Users must log in with their user ID and password so that they have an identity in JasperReports Server. The server stores user definitions, including encrypted passwords, in a private database. Administrators create, modify, and delete user accounts through the administrator pages, as described in <a href="../management/managing_users.md">Managing Users</a>.</p></td>
</tr>
<tr>
<td>Password policies</td>
<td><p>Every company must establish a password policy that weighs its security risks against the convenience of its users. JasperReports Server supports many different password policies such as password expiration, reuse, and strong patterns. This configuration is described in the <span>JasperReports Server Security Guide</span>.</p></td>
</tr>
<tr>
<td>External authentication</td>
<td><p>External authentication uses centralized identity services such as LDAP (used by Microsoft Active Directory and Novell eDirectory), Central Authentication Service (CAS), or Java Authentication and Authorization Service (JAAS). For more information, see the <span>JasperReports Server External Authentication Cookbook</span>.</p></td>
</tr>
<tr>
<td>Application Security</td>
<td><p>System admins who install and maintain enterprise software know they must protect their servers against hackers. JasperReports Server protects your data against intruders with many protocols and tools, such as HTTPS, encryption, CSRF prevention, and input validation against cross-site scripting and SQL injection. For these topics and others, see the <span>JasperReports Server Security Guide</span>.</p></td>
</tr>
<tr>
<td>Organizations</td>
<td><p>Users belong to organizations and are restricted to seeing resources within their organization. Organizations have their own administrators, but they see only the users, roles, and resources from their organization. When JasperReports Server is configured with multiple organizations, they are effectively isolated from each other, although the system admin can share resources through the Public folder. For more information, see <a href="../repository/multiple_organizations.md">Multiple Organizations in the Repository</a>.</p></td>
</tr>
<tr>
<td>Roles</td>
<td><p>JasperReports Server also implements roles that can be assigned to any number of users. Roles let administrators create groups or classes of users that are granted similar permissions. A user may belong to any number of roles and receive the privileges from each of them. Administrators create, modify, and delete roles through the administrator pages, as described in <a href="../management/managing_roles.md">Managing Roles</a>.</p></td>
</tr>
<tr>
<td>Resource permissions</td>
<td><p>Administrators can define access permissions on every folder and resource in the repository. Permissions are enforced when accessing any resource either directly through the repository interface, indirectly when called from a report, or programmatically through the web services.</p>
<p>Permissions can be defined for every role and every user, or they can be left undefined so they are inherited from the parent folder. To restrict access or hide resources such as database connections, the administrator can set no-access or execute-only permission. For more information, see <a href="../repository/permissions.md">Repository Permissions</a>.</p></td>
</tr>
<tr>
<td>Administrator privileges</td>
<td><p>JasperReports Server distinguishes between administrators and users. Administrators are granted access to the UI for permissions, user management, and sensitive resources such as database connections. Administrators also set the UI appearance with themes<span> and monitor server activity with diagnostics</span>. Regular users are restricted to the folders, reports, and dashboards that admins allow them to access. Most of the features in this guide are not accessible to regular users. See <a href="users_and_roles.md">Delegated Administration</a>.<br />
</p></td>
</tr>
<tr>
<td>Menus and pages</td>
<td><p>The menus that appear in JasperReports Server depend on the user's roles. For example, only users with the administrator role can see the <strong>Manage</strong> menu and access the administrator pages. By modifying the server's configuration, you can modify access to menus, menu items, and individual pages. Refer to the <span>JasperReports Server Source Build Guide</span> and <span>JasperReports Server Ultimate Guide</span> for more information.</p></td>
</tr>
<tr>
<td>Attributes</td>
<td><p>Attributes are name-value pairs associated with a user, organization, or server. Attributes can be used to restrict or enable a user's access to data in several ways. See <a href="../management/managing_attributes.md">Managing Attributes</a>.</p></td>
</tr>
</tbody>
</table>

Administrators must keep security in mind at all times when managing organizations, user, roles, and resources, because effective security relies on all of them working together.
