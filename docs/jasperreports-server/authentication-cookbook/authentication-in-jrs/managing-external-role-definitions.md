---
title: Managing External Role Definitions
description: "Roles can be mapped from a variety of structures that depend on the external authority: LDAP authentication maps roles dynamically from groups, and CAS authentication extracts roles from an external..."
---

# Managing External Role Definitions

Roles can be mapped from a variety of structures that depend on the external authority: LDAP authentication maps roles dynamically from groups, and CAS authentication extracts roles from an external data source or specifies them statically in the configuration file. Because each external authority may define roles differently, this guide refers to those structures collectively as role definitions.

In practice, you'll find that only a subset of the role definitions in your external authority are applicable to JasperReports Server. Of those, some may also be used by other applications, and others may be created specifically for managing users in JasperReports Server. You should identify the maintenance procedures on your enterprise-wide user authority that impact JasperReports Server and document additional procedures for keeping JasperReports Server in sync.

The following table describes the impact on JasperReports Server when modifying role definitions in the external authority:

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
<td><p>Creating a new role</p></td>
<td><p>Role definitions are not directly mapped to JasperReports Server; only roles that are assigned to users who log in are mapped. When you create a new role and assign it to a user who accesses JasperReports Server, determine which case applies:</p>
<ul>
<li>The role is significant to access control within JasperReports Server. You must initialize this role in the server with a test user and define all necessary repository authorization rules to secure your data before you deploy this role to real users, as described in <a href="synchronization-roles.md">Synchronization of Roles</a>.</li>
<li>The role is not significant to users within JasperReports Server. Synchronization automatically creates the role and assigns it to users according to their mapping, but with no authorization rules based on the role, it has no impact.</li>
</ul></td>
</tr>
<tr>
<td><p>Modifying role membership</p></td>
<td><p>Changes in role membership are reflected the next time a role member starts a new session in JasperReports Server, as described in <a href="synchronization-users.md">Synchronization of External Users</a>. Roles that were previously unknown to the server are treated as new roles as described above, and roles that are no longer assigned to a user are deleted as described below.</p></td>
</tr>
<tr>
<td><p>Deleting a role</p></td>
<td><p>External users no longer have the role, and it is removed from each external user by synchronization upon the next login. The role remains in the internal database, and permissions that reference the role remain in the repository. The role may still be assigned to external users who have not logged in since the role was removed.</p>
<ul>
<li>If the role definition in the external authority was mapped to an external role in JasperReports Server, it has no impact on the server and you can safely delete it.</li>
<li>If the role definition is mapped to an internally defined role in JasperReports Server, you can delete the role or modify the configuration file to remove the mapping. If you remove the mapping, the internal role can be assigned manually by an administrator. If you do not modify the configuration file and you attempt to assign the internal role manually to a user in JasperReports Server, the role is automatically removed during synchronization.</li>
</ul></td>
</tr>
</tbody>
</table>

# Modifying Role Mappings

Once you've set up external authentication with your JasperReports Server instance, you add new role mappings by editing the applicationContext-externalAuth-\*.xml file. You need to restart the server for these changes to take effect.

Be careful changing or removing role mappings. When a role mapping is removed or changed, synchronization no longer updates the target role in JasperReports Server. This means users assigned a deleted external role still have that role in JasperReports Server. You can work around this by creating a mapping from a non-existing role definition in the external authority to the target role you want to remove.

!!! warning

    When you want to change the target role for an existing role mapping, you should create a dummy mapping that maps a non-existent role definition to the JasperReports Server role you no longer want to use.

For example, suppose you have **Sales Manager** as a role in your external authority, and you initially map it to ROLE_ADMINISTRATOR in JasperReports Server.

**Sales Manager** Mandy logs into JasperReports Server and is assigned ROLE_ADMINISTRATOR.

You then create a new role in JasperReports Server, ROLE_SALES_MANAGER, and modify your role mapping so **Sales Manager** in the external authority is now mapped to ROLE_SALES_MANAGER in JasperReports Server. You then restart the server.

By default, the next time Mandy logs in, she's assigned ROLE_SALES_MANAGER. But because ROLE_ADMINISTRATOR no longer appears in your application context file, synchronization doesn't check for it and remove it. Mandy now has two roles: ROLE_ADMINISTRATOR and ROLE_SALES_MANAGER.

You can remove ROLE_ADMINISTRATOR from Mandy's account by creating a dummy mapping with ROLE_ADMINISTRATOR as the target. For example, if no one in your external authority has the role definition **No Such Role**, you can add a mapping in your application context file from **No Such Role** to ROLE_ADMINISTRATOR then restart the server. The next time Mandy logs in, the synchronizer finds that she doesn't have the **No Such Role** role definition and removes ROLE_ADMINISTRATOR.

!!! note

    It is possible for a role in JasperReports Server to be the target of more than one role mapping. If multiple role definitions map to the same role in JasperReports Server, users who have any one of the role definitions will receive the role in JasperReports Server.
