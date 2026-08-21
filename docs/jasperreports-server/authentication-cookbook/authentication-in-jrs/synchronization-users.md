---
title: Synchronization of External Users
description: "When a user is authenticated by an external authority, JasperReports Server initializes its session principal object, which contains the username, role names, and organization ID, if applicable. The..."
---

# Synchronization of External Users

When a user is authenticated by an external authority, JasperReports Server initializes its session principal object, which contains the username, role names, and organization ID, if applicable. The `ExternalDataSynchronizer` uses this information to automatically update or create corresponding structures in the internal database:

- If the internal database has no organization with the user's organization ID, JasperReports Server creates it with the templates currently defined in the repository. For LDAP authentication, organization hierarchies are created for users.
- Roles can be mapped to external or internal roles.
  - When mapping a role to an external role, the role name is compared to existing external roles. If the role doesn't exist, it's created as an external role. See [Synchronization of Roles](synchronization-roles.md) for details about role creation.
  - When mapping a role to an internal role, the role name is compared to existing internal roles. If the role doesn't exist, it's created as an internal role. You can also create a role at the root level, which gives administrative permissions, or at the organization level, which restricts access to the organization. See [Synchronization of Roles](synchronization-roles.md) for details about role creation.
- The user ID is compared to existing user accounts in the internal database. If an organization ID is specified, only the user IDs in that organization are checked.
  - If the user ID matches an account in the internal database, its list of assigned roles is synchronized as described in [Synchronization of Roles](synchronization-roles.md). The user ID can match either a previously synchronized external user or an internal user created by an administrator. If the external user ID matches an existing internal user, authentication fails; an administrative user has to resolve the situation manually.
  - If the user ID does not match an account in the internal database, an external user account is created. If an organization ID is specified, the account is created within that organization. Finally, all of the external roles along with any configurable default internal roles are assigned to the new user account.

For more information about organizations, roles, and user accounts see the JasperReports Server Administrator Guide.

A user account created for an external user has the same structure as an internal user account but differs in the following ways:

- A database flag marks it as externally defined.
- The full name of the user is the same as the user ID, which is always the same as the login name entered by the user.
- The external user account does not store the password.
- It does not have any values for optional user properties, such as the user's email or profile attributes. The default implementation of external authentication does not include these properties. An administrator can manually include these properties.

!!! note

    An external authority such as LDAP contains information like the user’s full name, email address, and profile attributes, which can be mapped into the external user account. However, this requires customizing the mapping and synchronization beans. See [Advanced Topics](../advanced-topics/advanced-topics.md).

After synchronization, the external user fits in cohesively with all the structures and mechanisms of JasperReports Server, especially those required for authorization. But the JasperReports Server administrator's management of an external account is limited to the ability to disable the account and prevent the external user from logging in.

An external user cannot log in when the external authority is offline; external accounts do not store the password and are not meant for failover. Once external authentication is configured, only the information in the external authority determines who can log in and what roles they have. However, administrators may view external organizations, users, and roles to determine if all mappings from the external authority are correct.
