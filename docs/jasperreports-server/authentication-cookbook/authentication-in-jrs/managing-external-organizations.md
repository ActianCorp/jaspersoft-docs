---
title: 1.0.0.1 Managing External Organizations
description: "The following table describes the impact on JasperReports Server when modifying organizations defined in the external authority:"
---

# 1.0.0.1 Managing External Organizations

The following table describes the impact on JasperReports Server when modifying organizations defined in the external authority:

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
<td><p>Adding an organization</p></td>
<td><p>Organizations are not directly mapped to JasperReports Server, rather a new organization ID is mapped when synchronizing the first user in the organization that accesses the server. At that time, synchronization creates the organization and the user within it, along with any roles assigned to the user. Determine which of the following cases applies:</p>
<ul>
<li>Your organization definitions and mappings create the same role names in every organization. You should configure the organization folder templates so the default contents and permissions work with the known role names. Your external organization definitions should then map to organizations that work as soon as the first user logs in.</li>
<li>Each of your externally defined organizations has different role names or requires specific repository contents. You should create test users in the new organizations first, so you can configure the new organization folder, synchronize external roles, and assign repository permissions before actual users have access. See the procedure in <a href="initializing-external-users-in-jrs.md">Initialization of JasperReports Server for External Users</a>.</li>
</ul></td>
</tr>
<tr>
<td><p>Modifying an organization</p></td>
<td><p>Changing the users or roles in organizations defined in the external authority is the same as adding users or roles to one organization and removing them from the other. See the corresponding actions in <a href="managing-external-users.md">Managing External Users</a> and <a href="managing-external-role-definitions.md">Managing External Role Definitions</a>.</p></td>
</tr>
<tr>
<td><p>Deleting an organization</p></td>
<td><p>Because organization definitions are not mapped directly, deleting an organization has the same effect as removing each of its users. The organization remains in the internal database and repository, along with the external roles and users who last accessed it. The unused organization has no impact on the server. You can safely delete it.</p></td>
</tr>
<tr>
<td>Changing the default admin users of organizations</td>
<td>Default admin users are created only when the organization is created. Therefore, changes to the default admin users appear only in organizations created after the changes were made. In particular, if you add or delete default admin users, your changes affect only new organizations.</td>
</tr>
</tbody>
</table>
