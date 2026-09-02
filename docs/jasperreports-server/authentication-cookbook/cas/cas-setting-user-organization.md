---
title: Setting the User Organization
description: Organizations are a feature of JasperReports Server commercial editions. Skip this section if you have JasperReports Server community edition.
---

# Setting the User Organization

!!! note

    Organizations are a feature of JasperReports Server commercial editions. Skip this section if you have JasperReports Server community edition.

Spring’s default CAS configuration supports only user authentication. However, you can extend this to set organizations in one of two ways:

-   Extract organization data with an additional technology, such as LDAP or a JDBC database. See [Mapping to Multiple Organizations](#mapping-to-multiple-organizations).
-   Use the `defaultOrganization` property of the `externalTenantSetupProcessor` bean to set a single organization assigned to all external users. See [Mapping to a Single Organization](#mapping-to-a-single-organization).

## Mapping to Multiple Organizations

To assign your external CAS users to multiple organizations in JasperReports Server, you need an additional technology like LDAP or JDBC to supply the user’s organization data. We provide sample files that show how to extract the organization data from a third-party technology and integrate it with CAS authentication. These files are described briefly; an in-depth discussion is beyond the scope of this guide.

### Setting Multiple Organizations Using LDAP

You can configure your connection to the LDAP server in one of two ways:

-   Configure the connection during installation of JasperReports Server by configuring the `external.ldapUrl`, `external.ldapDn`, and/or `external.ldapPassword` properties in default_master.properties. You have the option to encrypt any of the LDAP connection parameters. This is the preferred method for setting the LDAP connection parameters. See the JasperReports Server Security Guide for more information.
-   If you have an existing JasperReports Server and can't reinstall it for some reason, you can configure the connection properties directly in your sample-applicationContext-externalAuth-CAS-mt.xml file. In this case, the properties, including the password, can't be encrypted. See [Setting the LDAP Connection Parameters](../ldap/ldap-setting-connection-parameters.md)for more information.

The following file gives an example of how to assign users to multiple organizations by integrating CAS with LDAP:

&lt;js-install&gt;/samples/externalAuth-sample-config/sample-applicationContext-externalAuth-CAS-LDAP-mt.xml

This sample uses the `ldapExternalTenantProcessor` bean to extract an organization hierarchy from the user’s distinguished name. For more information about the `ldapExternalTenantProcessor` bean, see [Mapping to Multiple Organizations](../ldap/ldap-setting-user-organization.md) in [LDAP Authentication](../ldap/ldap-introduction.md).

### Setting Multiple Organizations Using JDBC

You can configure your connection to the database in one of two ways:

-   Configure the connection during installation of JasperReports Server by configuring the `external.jdbc.driverClassName`, `external.jdbc.url`, `external.jdbc.username`, and/or `external.jdbc.Password` properties in default_master.properties. You have the option to encrypt any of the LDAP connection parameters. This is the preferred method for setting the database connection parameters. See the JasperReports Server Security Guide for more information.
-   If you have an existing JasperReports Server and can't reinstall it for some reason, you can configure the connection properties directly in your sample-applicationContext-externalAuth-CAS-db-mt.xml file. In this case, the properties, including the password, can't be encrypted. See [Setting the Database Connection Parameters](../external-db/external-db-setting-connection-parameters.md) for more information.

The following file gives an example of how to assign users to multiple organizations by integrating CAS with a JDBC database:

&lt;js-install&gt;/samples/externalAuth-sample-config/sample-applicationContext-externalAuth-CAS-db-mt.xml

This sample uses the `detailsQuery` property of the `casJDBCUserDetailsService` bean to extract `tenantId` from an external database using an appropriate SQL query. Note that the `tenantId` column name has to be returned by the SQL query in order for `externalTenantSetupProcessor` to catch and process it correctly. In cases where the external database column has a different name, cast the column name as `tenantId`, as in the following example:

``` sql
SELECT organizationId AS tenantId from org_table
```

## Mapping to a Single Organization

If you have multiple organizations in your deployment, you can use the `externalTenantSetupProcessor``ldapExternalTenantProcessor` bean to specify a single organization assigned to all external users. To do this, set `externalTenantSetupProcessor``ldapExternalTenantProcessor`’s `defaultOrganization` property to the organization ID of the selected organization. If an organization with that ID already exists, all external users are assigned to that organization. If the organization does not exist, it's created when the first external user authenticates correctly.

When specifying the `defaultOrganization` value, the organization ID must not contain the following characters: \|, &, \*, ?, &lt;, &gt;, /, \\, \~, !, #, $, %, \^, \[, or \].

The following example shows how to configure `externalTenantSetupProcessor``ldapExternalTenantProcessor` to assign all users to organization_1:

``` xml
<bean id="externalTenantSetupProcessorldapExternalTenantProcessor" class="com.jaspersoft.jasperserver.multipleTenancy.
    security.externalAuth.processors.MTExternalTenantSetupProcessorLdapExternalTenantProcessor"     parent="abstractExternalProcessor">
  <property name="multiTenancyService">
    <ref bean="internalMultiTenancyService"/>
  </property>
  <property name="defaultOrganization" value="organization_1"/>
</bean>
```

!!! warning

    Do not specify a null value for the `defaultOrganization` property. The null organization ID is usually reserved for special users like the system administrator and allows access to the repository folder of all other organizations.

Organizations created during external user login have an administrator with the default password. For security reasons, you should change the default password of any organization admin. See [Initialization of JasperReports Server for External Users](../authentication-in-jrs/initializing-external-users-in-jrs.md) for a process to initialize JasperReports Server, including organization administrators, before going into production with external authentication.
