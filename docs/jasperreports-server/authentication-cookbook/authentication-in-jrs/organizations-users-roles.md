---
title: Organizations and Users
description: "When performing external authentication, JasperReports Server obtains all the information about a user from the external authority. In order to create and enforce permissions, JasperReports Server..."
---

# Organizations and Users

When performing external authentication, JasperReports Server obtains all the information about a user from the external authority. In order to create and enforce permissions, JasperReports Server must store the information about users, roles, and organizations in the internal database. So for each externally-defined user, role, and organization, the server creates a local user account, role definitions, and organization folders. This process is called synchronization.

The users and roles defined through external authentication appear in the management interface, but are labeled as “external.” Administrators can view and delete the external users and roles, but the synchronization will re-create the necessary users and roles as long as external authentication is configured. External user accounts and roles are placeholders for use by the synchronization and permissions mechanisms. Administrators can disable specific external users in JasperReports Server to prevent those external users from logging into JasperReports Server.

There are three important aspects to managing external users, roles, and organizations:

-   The synchronization of external users, roles, and organizations with the internal database is automatic once external authentication is configured. This is done by the `ExternalDataSynchronizer` bean. For more information, see [Advanced Topics](../advanced-topics/advanced-topics.md).
-   Permissions in the repository must be initialized manually for the external roles after their creation.
-   Maintenance of the external users is necessary only when creating or deleting roles, when creating new organizations from an external authority, or when disabling external users in JasperReports Server.

When you deploy JasperReports Server in a production environment, you need to set up role permissions before your users access the server. However, you cannot create external roles or organizations directly; you can create them only by logging in as an external user with the desired roles and permissions. To set up role permissions, you must understand the synchronization process. For maintenance, you must be aware of how changes in the external authority impact permissions in JasperReports Server. These processes are explained in the following sections.
