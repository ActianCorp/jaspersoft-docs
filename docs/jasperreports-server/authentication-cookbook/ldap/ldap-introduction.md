---
title: LDAP Authentication
description: "Lightweight Directory Access Protocol (LDAP) is one of the most popular architectures for enterprise directories. By centralizing all user management in an LDAP directory, applications across the..."
---

# LDAP Authentication

Lightweight Directory Access Protocol (LDAP) is one of the most popular architectures for enterprise directories. By centralizing all user management in an LDAP directory, applications across the enterprise can share the same user database, and administrators don't need to duplicate user accounts.

This chapter shows how JasperReports Server can be configured to perform external authentication with LDAP. As part of the authentication process, JasperReports Server also synchronizes the external user information, such as roles and organization ID, between LDAP and the JasperReports Server internal database.

LDAP authentication does not provide single sign-on (SSO) functionality. You must implement that separately and configure it for use within JasperReports Server. Enabling SSO with LDAP is beyond the scope of this guide. For more information, see [Advanced Topics](../advanced-topics/advanced-topics.md).

This chapter assumes you're familiar with LDAP servers and the structure of the data they contain, in particular the format of distinguished names (DNs) and relative distinguished names (RDNs) that create structure and identify entries in LDAP. For more information about LDAP in Spring Security, see the LDAP sample in the [Spring Security reference documentation](https://docs.spring.io/spring-security/reference/6.5/index.html) for 6.5. [<br>
](https://docs.spring.io/spring-security/site/docs/5.3.13.RELEASE/reference/html5/)

This chapter contains the following sections:

-   [Overview of External LDAP Authentication](ldap-authentication-steps.md)

-   [Configuring JasperReports Server for LDAP Authentication](configuring-jrs-for-ldap.md)

-   [Overview of LDAP Beans](ldap-beans.md)

-   [Setting the LDAP Connection Parameters](ldap-setting-connection-parameters.md)

-   [Performing LDAP User Search](ldap-user-search.md)

-   [Mapping the User Roles](ldap-user-role-mapping.md)

-   [Mapping the User Organization](ldap-setting-user-organization.md)

-   [Mapping Roles to System Roles](ldap-mapping-system-roles.md)

-   [Setting Up Multiple Providers](multiple-providers.md)

-   [Troubleshooting LDAP Configurations](ldap-troubleshooting.md)

-   [Adding a Custom Processor](ldap-custom.md)

-   [Restarting](ldap-jrs-restart.md)
