---
title: Defining Static Roles
description: "If you're mapping all your external users to a single organization, you can assign static roles to users. This lets you specify a list of administrative users and roles, and a list of roles for..."
---

# Defining Static Roles

If you're mapping all your external users to a single organization, you can assign static roles to users. This lets you specify a list of administrative users and roles, and a list of roles for non-administrative users. To define static roles, use the `externalUserSetupProcessor` or `mtExternalUserSetupProcessor` bean. To set up static roles, locate the version of the bean used in your sample file and configure the following properties:

-   `adminUserNames` property: A list of usernames granted internal administrator privileges in JasperReports Server. The username values must exactly match the usernames authenticated and returned by the external authority.
-   `defaultAdminRoles` property: A list of JasperReports Server internal roles. These are assigned to every user in the list of administrators.
-   `defaultInternalRoles` property: A list of JasperReports Server roles assigned to every user not in the list of administrators.

The following example shows how to use the `mtExternalUserSetupProcessor` bean to define static roles. The configuration for `externalUserSetupProcessor` is similar:

``` xml
<bean id="mtExternalUserSetupProcessor" class="com.jaspersoft.jasperserver.multipleTenancy.security.
    externalAuth.processors.MTExternalUserSetupProcessor"
    parent="abstractExternalProcessor">
    ...
  <property name="adminUsernames">
    <list>
      <value>myorgadmin</value>
    </list>
  </property><property name="defaultAdminRoles">
    <list>
      <value>ROLE_USER</value>
      <value>ROLE_ADMINISTRATOR</value>
    </list>
  </property>
  <property name="defaultInternalRoles">
    <list>
      <value>ROLE_USER</value>
    </list>
  </property>...
```
