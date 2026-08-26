---
title: Beans to Configure
description: The sample-applicationContext-externalAuth-CAS.xml files contain the beans needed to enable and perform CAS authentication. This section summarizes the beans you need to modify to configure...
---

# Beans to Configure

The sample-applicationContext-externalAuth-CAS\*.xml files contain the beans needed to enable and perform CAS authentication. This section summarizes the beans you need to modify to configure JasperReports Server to work with your CAS provider.

-   `externalAuthProperties`: Configure this bean to specify the external authentication properties needed by the JasperReports Server API, including the HTTPS URL where tickets are validated on the CAS server and the login and logout URLs for external users. See [Configuring externalAuthProperties](cas-with-externalauthproperties.md) for more information.
-   `casServiceProperties`: Configure this bean to specify the Spring CAS API properties, such as the service parameter (the JasperReports Server URL to which CAS redirects after successful authentication) and whether to disregard the TGT (`sendRenew`).
-   `externalUserSetupProcessor`: Configure this bean to specify how to synchronize external users and roles with the internal `jasperserver` database.
-   `externalDataSource` (optional): Configure this bean to specify an external data source for `casJDBCUserDetailsService` to query for user details. External details can be obtained from other data sources, such as LDAP. To enable an external data source, you must implement the `ExternalUserDetailsService` interface and substitute it in the `externalDataSynchronizer` bean.
-   `casJDBCUserDetailsService` (optional): Configure this bean with the SQL queries to extract external user information from the data source specified in the `externalDataSource` bean.
