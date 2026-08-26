---
title: Configuring User Authentication and Authorization via Database Queries
description: "To authenticate a user, JasperReports Server first queries the external database to retrieve the user by username and organization. After authentication, a second query is executed to retrieve user..."
---

# Configuring User Authentication and Authorization via Database Queries

To authenticate a user, JasperReports Server first queries the external database to retrieve the user by username and organization. After authentication, a second query is executed to retrieve user roles. These queries are configured in the `externalUserTenantDetailsService` bean. The results are used to map users, roles, and organizations.

The `externalUserTenantDetailsService` bean configures this bean to define the queries needed to retrieve user, organization, and roles from the external database. This bean has the following properties:

-   `dataSource` property: References the `externalDataSource` bean, which configures the JDBC connection to the database. The `externalDataSource` bean is defined later in the file.
-   `usersByUsernameAndTenantNameQuery`: Property that takes as input a single `username` parameter and returns a username, encrypted password, and an organization ID. Configure this property with a database query that retrieves the information that authenticates the user, that is, username, encrypted password, and organization.
-   `authoritiesByUsernameQuery`: Property that takes as input a single `username` parameter and returns one or more records of `username`, `rolename` tuples. Configure this property with a database query that retrieves the user and roles from the external database.

The following example shows how to set up the `externalUserTenantDetailsService` bean queries:

``` xml
<bean id="externalUserTenantDetailsService" class="com.jaspersoft.jasperserver.
        multipleTenancy.security.externalAuth.db.MTExternalJDBCUserDetailsService">
    <property name="dataSource" ref="externalDataSource"/>
    <property name="usersByUsernameAndTenantNameQuery" value="SELECT u.username,
      u.password, t.tenantId FROM jiuser u, jitenant t WHERE u.tenantId = t.id and
      username = ?"/>
    <property name="authoritiesByUsernameQuery" value="SELECT u.username, r.rolename
      FROM jiuser u, jiuserrole ur, jirole r WHERE u.id = ur.userId and ur.roleId=r.id and
      u.username = ?"/>
    <property name="multiTenancyConfiguration"><ref bean="multiTenancyConfiguration"/></property>
</bean>
```

!!! note

    The semantics, order, and number of the columns in each tuple is fixed. Changing the order or number of the columns requires customization, which is beyond the scope of this manual.
