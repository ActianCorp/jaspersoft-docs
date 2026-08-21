---
title: Managing External Users
description: "The following table describes the impact on JasperReports Server when managing users in the external authority:"
---

# Managing External Users

The following table describes the impact on JasperReports Server when managing users in the external authority:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>Action in External<br />
Authority</p></th>
<th><p>Impact on JasperReports Server</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Creating a new user</p></td>
<td><p>JasperReports Server automatically creates the new external user account when the user first accesses the server. As long as the user relies on existing roles in an existing organization, no server changes are required. If the user is associated with new roles, see <a href="managing-external-role-definitions.md">Managing External Role Definitions</a>.</p></td>
</tr>
<tr>
<td><p>Updating a password</p></td>
<td><p>JasperReports Server doesn't store the passwords of external users, and is not affected by changes to user passwords or policies on the external authority.</p></td>
</tr>
<tr>
<td><p>Updating personal information</p></td>
<td><p>With the default mapping of external users, only the login name is stored in an external user account. If you configure role mapping based on personal information in the external user entry, you need to account for any possible change in the content or structure of the external authority. For example, if a role is based on a user’s <code>department</code> attribute, make sure the user can't modify this attribute in the external authority. Otherwise, the user could inadvertently or maliciously change his or her roles within JasperReports Server.</p></td>
</tr>
<tr>
<td><p>Changing group or role membership</p></td>
<td><p>Described in <a href="managing-external-role-definitions.md">Managing External Role Definitions</a>.</p></td>
</tr>
<tr>
<td><p>Changing organization membership</p></td>
<td><p>When organizations represent departments within a company, a user may change organizations, as mapped from the external authority. From JasperReports Server’s point of view, this is the same as deleting a user in the old organization and creating a user in another organization.</p></td>
</tr>
<tr>
<td><p>Disabling or deleting a user</p></td>
<td><p>When the user can no longer authenticate with the external authority, he can’t access JasperReports Server. Even though the external user account remains in the internal database, it can't be used for logging in. The defunct user account has no impact on the server; you can safely delete it.</p>
<p>An external user can be disabled in JasperReports Server.</p></td>
</tr>
</tbody>
</table>
