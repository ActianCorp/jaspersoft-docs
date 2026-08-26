---
title: Beans to Configure
description: The sample-applicationContext-externalAuth-db-mt.xml file contains the beans needed to enable and perform authentication to an external database. This section summarizes the most important beans in...
---

# Beans to Configure

The sample-applicationContext-externalAuth-db-mt.xml file contains the beans needed to enable and perform authentication to an external database. This section summarizes the most important beans in this file, including the beans you need to configure to make the samples work with your deployment.

-   `proxyAuthenticationProcessingFilter`: Filter bean that enables external authentication of web application requests. When `proxyAuthenticationProcessingFilter` is present in the application context, that is, when it appears in an applicationContext-&lt;customName&gt;.xml file in the &lt;js‑webapp&gt;/WEB-INF directory, the Spring Security filter chain processes the authentication via the proxy definitions instead of the default internal filter found in applicationContext-security-web.xml. You don't need to configure this bean.

-   `dbAuthenticationManager`: Lists the available authentication providers. The providers in the list are invoked in the order they appear in the configuration file until one of them authenticates the user. When one of the providers successfully authenticates the user, the rest of the providers are skipped. The final provider in the list, `${bean.daoAuthenticationProvider}` authenticates to the `jasperserver` internal database. You can customize authentication by adding more providers to this bean.

    -   `externalDaoAuthenticationProvider`: Custom authentication provider for external database authentication.

-   `externalUserTenantDetailsService`: Configure this bean to define the query necessary to retrieve user, role, and organization information from the external database, as described in [Configuring User Authentication and Authorization via Database Queries](external-db-authentication-queries.md).

-   `passwordValidator`: Bean that specifies a key for encoding user passwords. First, import the same cryptographic key that is used for passwords in your database. Then configure this bean with the key's alias and password, as described in [Setting the Password Encryption](external-db-password-encryption.md) .

-   `externalDataSynchronizer`: Bean whose class creates a mirror image of the external user in the internal jasperserver database. The sample includes the following processors:

    -   `externalTenantSetupProcessor`: Bean that sets up external organizations in the `jasperserver` database. For multi-organization JasperReports Server deployments, configure this bean to specify the mapping between fields and field values retrieved from the database and JasperReports Server organizations, as described in [Setting the User Organization](external-db-setting-user-organization.md).
    -   `mtExternalUserSetupProcessor`: Bean that creates and configures the internal user corresponding to a successfully authenticated external user. Configure this bean to specify the default internal role given to the external users in JasperReports Server and to map external user roles to internal JasperReports Server roles if needed, as described in [Mapping User Roles](external-db-mapping-roles.md). Optionally, you can assign administrative roles to specific users.
    -   `externalUserFolderProcessor`: Bean that creates a user folder as an example of additional post-authentication processing. Post-authentication processing is described in [Authentication Based on Request](../advanced-topics/header-based-authentication.md).

-   `externalDataSource`: Configure this bean with the JDBC connection information to the external database to which users are authenticated, as described in [Setting the Database Connection Parameters](external-db-setting-connection-parameters.md).

-   `externalAuthProperties`: This bean stores properties necessary to configure JasperReports Server for external authentication. For multi-organization deployments of JasperReports Server, configure this bean to require an organization ID on the login form, as described in [Configuring the Login Page for a Single-Organization Deployment](external-db-single-org-login.md)
