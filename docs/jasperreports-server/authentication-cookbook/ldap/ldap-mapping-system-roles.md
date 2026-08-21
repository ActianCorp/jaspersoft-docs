---
title: Mapping Roles to System Roles
description: "When the organization mapping is complete, synchronization invokes mtExternalUserSetupProcessor commercial editions) or externalUserSetupProcessor (community edition) to create the external user and..."
---

# Mapping Roles to System Roles

When the organization mapping is complete, synchronization invokes `mtExternalUserSetupProcessor` commercial editions) or `externalUserSetupProcessor` (community edition) to create the external user and roles in that organization. JasperReports Server includes an additional mapping of roles to system roles so you can grant administrator privileges to your external users. Using this feature, LDAP entries belonging to custom groups can be granted system or organization admin roles in JasperReports Server.

Depending on your deployment, you can map roles to system roles in one of two ways:

- Configure the `mtExternalUserSetupProcessor` or `externalUserSetupProcessor` bean with `organizationRoleMap` to map between external and internal roles. The processor checks if the user has an external role as a map entry key. If the user has the role, the processor assigns the user the internal role in the map entry value instead of the external role in the key.
- Map user roles statically using the `mtExternalUserSetupProcessor` or `externalUserSetupProcessor` bean.

One practical consequence of external administrator role mapping is that external authentication can be used exclusively. When properly set up, you can have external users who are system or organization administrators. Then you don't need to have the superuser and jasperadmin users. However, you must ensure that every organization has an external user mapped to the organization with the correct attributes to have organization admin privileges.

!!! note

    Administrators of your LDAP server cannot log into JasperReports Server using their LDAP administrator credentials.

    In most LDAP servers, users and administrators are stored in different base DNs. For example, you might store user entries in dc=example,dc=com, but administrators are stored under cn=Administrators,cn=config or ou=system. The mechanism for locating users during authentication can only search in a single base DN, so administrators in a different one cannot be found.

## organizationRoleMap

System and organization admin privileges are determined by the `ROLE_SUPERUSER` and `ROLE_ADMINISTRATOR` system roles at the root level. Using the `organizationRoleMap` property, you can assign these system roles to LDAP entries based on custom group membership. This property can be used in addition to the properties that map group names to organization roles.

Whether you map users and roles to a single organization or multiple organizations, you can define this additional mapping between any role name that your mapping creates and any system role. You specify role mapping via the `organizationRoleMap` property of the `mtExternalUserSetupProcessor` bean (commercial editions) or `externalUserSetupProcessor` (community edition).

The `organizationRoleMap` property provides a list of key/value pairs that maps external role names to internal ones. The key should be a role name that your mapping creates, after adding the prefix and capitalization as configured in `JSDefaultLdapAuthoritiesPopulator`. For commercial JasperReports Server deployments, you need to choose the level at which the role is assigned:

- To map to an internal role at the organization level, append `|*` to the name of the internal role, for example, `ROLE_EXTERNAL_USER|*`. Roles mapped at the organization level do not have administrative privileges.
- To map to an internal role at the system (null) level, do not modify the internal role name, for example, ROLE_EXTERNAL_ADMINISTRATOR. Roles at the system level are usually reserved for special users like the system administrator and allow access to the repository folder of all other organizations.

For example, if your LDAP user belongs to a group named `jrsadmin` that's mapped to the name `ROLE_ADMIN_EXTERNAL_ORGANIZATION`, the following code example would assign that user the `ROLE_ADMINISTRATOR` system role that makes the user an organization admin. This example shows how to create this system role mapping in a single organization configuration for commercial editions:

```
<bean id="mtExternalUserSetupProcessor" class="com.jaspersoft.jasperserver.multipleTenancy.security.
        externalAuth.processors.MTExternalUserSetupProcessor" parent="abstractExternalProcessor">
  <property name="userAuthorityService">
    <ref bean="${bean.internalUserAuthorityService}"/>
  </property>
  <property name="defaultInternalRoles">
    <list>
      <value>ROLE_USER</value>
    </list>
  </property>
  <property name="organizationRoleMap">
    <map>
      <entry>
        <key>
          <value>ROLE_ADMIN_EXTERNAL_ORGANIZATION</value>
        </key>
        <value>ROLE_ADMINISTRATOR</value>
      </entry>
    </map>
  </property>
</bean>
```

If the value `ROLE_ADMINISTRATOR` in the key value pair had ended with \|\* (`ROLE_ADMINISTRATOR|*`), the user would have been assigned `ROLE_ADMINISTRATOR` at the organization level.

Roles not mapped to system roles are created and synchronized in the mapped organization, as described in [Synchronization of Roles](../authentication-in-jrs/synchronization-roles.md). In particular, if the name `ROLE_ADMINISTRATOR` or `ROLE_SUPERUSER` are mapped from the LDAP groups, but not mapped to system roles, they're created as organization roles and assigned to the user. As organization roles, they don't grant any access permissions, which can be very confusing for administrators. Avoid LDAP groups and role mappings that create these names as organization roles.

## Defining User Roles Statically

If you're mapping all your external users to a single organization, you can assign static roles to users. This lets you specify a list of administrative users and roles, and a list of roles for non-administrative users. To define static roles, use the `externalUserSetupProcessor` or `mtExternalUserSetupProcessor` bean. To set up static roles, locate the version of the bean used in your sample file and configure the following properties:

- `adminUserNames` property: A list of usernames granted internal administrator privileges in JasperReports Server. The username values must exactly match the usernames authenticated and returned by the external authority.
- `defaultAdminRoles` property: A list of JasperReports Server internal roles. These are assigned to every user in the list of administrators.
- `defaultInternalRoles` property: A list of JasperReports Server roles assigned to every user not in the list of administrators.

The following example shows how to use the `mtExternalUserSetupProcessor` bean to define static roles. The configuration for `externalUserSetupProcessor` is similar:

```
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
