---
title: Overview of Users and Roles
description: "User accounts and role membership provide authentication and authorization for access control in JasperReports Server. When logging in, users enter their username and password to access the server...."
---

# Overview of Users and Roles

User accounts and role membership provide authentication and authorization for access control in JasperReports Server. When logging in, users enter their username and password to access the server. In a server with multiple organizations, users must also enter their organization ID. Administrators assign named roles to users and then create role-based permissions to further control access to the repository.

Users and roles are associated with the organizations in which they are defined. Users and roles defined in an organization can be granted or denied access to any repository folder or object in the organization or its suborganizations. However, a suborganization administrator has no access to the roles and users in the parent organization, even if they are used in access permission within the suborganization.

User names and role names are unique within an organization, but not necessarily among suborganizations or across all organizations in the server. For example, the default organization administrator is called `jasperadmin` in every organization. Because login credentials include the organization and user name, JasperReports Server can distinguish each user. In some cases such as web services, a user is identified by the unique string `username|organization_ID`.

Administrators define permissions directly on the resources and folders in the repository. You can define a level of access, such as read-write, read-only, or no access, and assign each permission based on either a username or a role.

## Administering Users and Roles

Administrators perform the following actions to manage users in their organization:

- Create, modify, and delete users.
- Set user account properties such as name, email, and attributes.
- Reset a user password. However, no administrator can ever view a user's existing password.
- Login as any user to test permissions.
- Create, modify, and delete roles.
- Assign roles to users.
- Set access permissions on repository folders and resources.

The system admin (`superuser`) can perform these actions for any user or any role in any organization in the server. An organization admin (`jasperadmin`) can perform these actions for users and roles in the same organization or its suborganizations.

## Delegated Administration

JasperReports Server enables three levels of delegated administration:

- With multiple organizations, administrators in each organization are limited to actions within their organization.
- The Administer permission allows a user to view and set permissions on a folder or resource. This can allow a power-user to manage a section of the repository, but not to create or manage users.
- Granting `ROLE_ADMINISTRATOR`, `ROLE_SUPERUSER`, or both allows a user to see the management interface and create users and roles. This is true delegated administration, whereby a user other than `jasperadmin` or `superuser` has administration abilities.

In the case of true delegated administration, three factors determine the scope of a user's administrative privileges:

- `ROLE_ADMINISTRATOR` – JasperReports Server confers the organization-level privileges to any user with this role. This includes managing users, roles, and permissions, as well as creating resources in the repository. When a user with this role logs in, the server displays the additional menus to access the admin pages and manage repository resources. Any administrator can assign this role to any other user.
- `ROLE_SUPERUSER` – When a user already has `ROLE_ADMINISTRATOR`, this additional role grants access to the system configuration functions. Only a system admin can assign this role to another user.

In a multi-organization environment, `ROLE_SUPERUSER` should not be given to organization admins or organization users, because this allows access to the Ad Hoc cache shared by all organizations. In the case of a single organization such as in the default installation, you may assign this role to the organization admins to grant access to system settings without granting privileges to create top-level organizations or other system administrators.

- The user's organization – Regardless of roles, an administrator is always limited in scope to the organization in which the user account is created, including any suborganizations thereof. In no case can a user, even with the `ROLE_SUPERUSER`, ever view or modify any organization, user, role, or folder outside of the organization to which that user belongs.

Any administrator can grant `ROLE_ADMINISTRATOR` to any user. That user then becomes equivalent to an organization admin of the organization in which he belongs. In order to delegate system administration, the existing system admin must first create other users at the root level, outside of any organization. The system admin can then assign both `ROLE_ADMINISTRATOR` and `ROLE_SUPERUSER` to grant them system admin privileges. For further information about these roles, see [Repository Permissions](../repository/permissions.md).
