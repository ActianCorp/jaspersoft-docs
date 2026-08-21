---
title: Initialization of JasperReports Server for External Users
description: "Knowing how external users are synchronized, the system administrator must initialize JasperReports Server and set the permissions in the repository to provide needed authorization."
---

# Initialization of JasperReports Server for External Users

Knowing how external users are synchronized, the system administrator must initialize JasperReports Server and set the permissions in the repository to provide needed authorization.

Your deployment procedure must include the following steps:

1.  Configure the mapping of usernames, roles, and possibly organization IDs from your external authority to JasperReports Server. The mapping depends on external authentication, as described in the chapter for each process. Optionally configure an admin user to be created in each external organization. The sample configuration files create a `jasperadmin` user by default.

2.  Create test users in the external authority for every organization and with every role that you expect in your production environment.

3.  If you're mapping external users to multiple organizations, log into JasperReports Server as the system administrator and prepare your organization templates and, possibly, themes for those organizations.

4.  Log into JasperReports Server as each of the test users. Doing so validates your configuration of the external authentication and mapping beans. When successful, it also creates the external roles and organizations you need.

5.  Log into JasperReports Server as the system administrator and:

    1.  Ensure that mapping and synchronization created the external users, roles, and organizations you expect.
    2.  In every organization, change the password of each automatically created administrator.

6.  Initialize your repository:
    1.  If you're using organizations, create additional repository resources, like data sources and shared reports, within each organization folder.
    2.  Define all your repository permissions using the external roles that were created.

This procedure is necessary because the external roles must exist in the internal database before you can create permissions for them. If you're using organizations, roles must be defined within organizations, so the organizations must exist as well. Optionally, you can use the administrative pages to create all the organizations your externally authenticated users need. This allows you some additional control over the creation of the organizations, but you must ensure that their IDs exactly match the values and hierarchies determined by the mapping.

When your JasperReports Server is in production, the external user accounts will be populated by the synchronization process as users log in. When the mapping is correct and consistent, the user population will have the same roles and organizations as those in your external authority, and you won't need to manually import users or roles into the server. And as role membership is updated in the external authority, external users are automatically synchronized in JasperReports Server.
