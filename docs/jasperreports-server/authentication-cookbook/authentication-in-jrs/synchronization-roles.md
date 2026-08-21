---
title: Synchronization of Roles
description: "Role synchronization is a complex process because roles need to be updated every time an external user logs in. Like users and organizations, roles are synchronized in two phases: mapping the roles..."
---

# Synchronization of Roles

Role synchronization is a complex process because roles need to be updated every time an external user logs in. Like users and organizations, roles are synchronized in two phases: mapping the roles from the external authority to roles in JasperReports Server, then assigning them to the user.

External authentication in JasperReports Server involves three role types:

- External: The synchronization process assigns and removes external roles in users' accounts according to the roles defined in the external authority. These roles are flagged in the UI, because they're not meant to be managed by administrators.
- Internal: JasperReports Server administrators create internal roles. To assign internal roles to external users, set up synchronization to map external roles to internal roles. Do not manually assign internal roles to external users. External role mapping takes precedence over manually-assigned roles. So synchronization may remove manually-assigned roles from users' accounts.
- System: JasperReports Server creates system roles like `ROLE_DEMO` during installation. System roles are handled exactly like internal roles above.

In the first phase of synchronization, the principal object has a set of role names derived from role definitions in the external authority. The goal is a JasperReports Server role for each of the mapped role names.

- If you're using organizations, all target roles are created within the user's mapped organization.
- If a role with the target name is already defined in JasperReports Server, that role is assigned to the user. Otherwise a new external role with this name is created and assigned.
- By default, roles are mapped to external roles, even if an internal role has the same name. If an external role name conflicts with an existing internal role in the target organization, a suffix like `_EXT` is added to the role name.
- You must explicitly map external roles to internal roles. If you're mapping a role to an internal role, you can specify whether to assign the internal role at the organization level or at the system (root) level. Roles mapped at the organization level have no administrative privileges. Roles at the system administrative privileges and access to the repositories of all organizations. To map to an internal role at the organization level, append \|\* to the name of the internal role. To map to an internal role at the system level, do not modify the internal role name.

The goal of the second phase of synchronization is to update the user with the set of roles mapped from the external authority. The origin of a role determines how the synchronizer assigns and removes the role from an external user account:

- All of roles identified or created in the first phase — internal, external, and system — are assigned to the external user. Any role not yet in the user's account, is assigned by the synchronization process.
- External roles that are assigned to the user — but not among those mapped and identified in the first phase — are removed from the user. This way, roles removed from the external authority are also removed from the user's JasperReports Server account.
- Internal and system roles created by synchronization during a previous login — but no longer mapped and identified from the external authority — are removed from the user. If an internal role that was assigned or removed by an administrator appears in the mapping configuration, the mapping from the external role takes precedence. This means that a manually assigned role may be added or removed based on the state of the external database. Therefore, to ensure that synchronization automatically makes all roles reflect those in the external authority, you should not manually assign internal roles.
