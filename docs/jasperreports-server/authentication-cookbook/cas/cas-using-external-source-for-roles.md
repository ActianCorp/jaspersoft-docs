---
title: Retrieving User Roles from an External Data Source
description: "If the static configuration available with CAS is insufficient, you can import external user information, like roles and organization ID, from an external data source. Imported roles are stored in..."
---

# Retrieving User Roles from an External Data Source

If the static configuration available with CAS is insufficient, you can import external user information, like roles and organization ID, from an external data source. Imported roles are stored in the internal `jasperserver` database (synchronization); they can be mapped to internal JasperReports Server roles or created as new external roles.

To retrieve external roles, the `externalUserDetailsService` property in the `externalDataSynchronizer` bean needs to point to an `ExternalUserDetailsService` implementation. The sample file includes `CasJDBCUserDetailsService`, which connects to an external MySQL database. `externalUserDetailsService` then makes the external data available to `externalUserSetupProcessor` or `mtExternalUserSetupProcessor`, which is responsible for mapping the external information and synchronizing it with the database.

The `casJDBCUserDetailsService` bean is configured with the following properties:

- `dataSource` property: Points to external database to query user details
- `usersByUsernameQuery` property: SQL query returning a list of user properties for the user name to be processed by `externalUserSetupProcessor` or `mtExternalUserSetupProcessor`. The result is returned as a map where keys are the column names in the query.
- `authoritiesByUsernameQuery` property: SQL query returning a list of user roles for the user name.

The `externalUserSetupProcessor` or `mtExternalUserSetupProcessor` bean has the following properties:

- `defaultInternalRoles` property: A list of internal roles assigned to the external user by default.
- `organizationRoleMap` property: A list of key/value pairs that map external role names to internal ones. For a commercial JasperReports Server deployment, you need to choose the level at which the role is assigned:
  - To map to an internal role at the organization level, append \|\* to the name of the internal role, for example, ROLE_EXTERNAL_USER\|\*. Roles mapped at the organization level do not have administrative privileges.
  - To map to an internal role at the system (null) level, do not modify the internal role name, for example, ROLE_EXTERNAL_ADMINISTRATOR. Roles at the system level are usually reserved for special users like the system administrator and allow access to the repository folders of all organizations.

The following shows how you might configure the `externalUserSetupProcessor` bean:

```
<bean id="mtExternalUserSetupProcessor" class="com.jaspersoft.jasperserver.multipleTenancy.security.
    externalAuth.processors.MTExternalUserSetupProcessor"  parent="abstractExternalProcessor">
<property name="organizationRoleMap">
   <map>
    <!-- Example of mapping customer roles to JRS roles -->
    <entry>
      <key>
        <value>ROLE_ADMIN_EXTERNAL_ORGANIZATION</value>
      </key>
      <!-- JRS role that the <key> external role is mapped to-->
      <value>ROLE_ADMINISTRATOR</value>
    </entry>
  </map>
</property>
```
