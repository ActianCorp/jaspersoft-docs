---
title: Mapping the User Roles
description: "An external user's roles in JasperReports Server are based on the groups to which that user belongs in LDAP. The server does a second search in the LDAP directory to determine any user roles. The..."
---

# Mapping the User Roles

An external user's roles in JasperReports Server are based on the groups to which that user belongs in LDAP. The server does a second search in the LDAP directory to determine any user roles. The mapping defines the location of the group definitions in LDAP, how to find the user's groups, and any transformation of the group name for use in the server as a role name.

## Configuring the User Role Mapping

The mapping for user roles is configured in a bean of the `JSDefaultLdapAuthoritiesPopulator` class, a Jaspersoft wrapper class that is itself part of the configuration of the `ldapAuthenticationProvider` bean.

!!! note

    Some LDAP servers support other user-grouping mechanisms, like `nsrole` in the Sun Directory Server. These can be mapped into JasperReports Server roles through the configuration parameters below, by extending the `JSDefaultLdapAuthoritiesPopulator` class, or a combination of both. Such configurations are beyond the scope of this guide.

To configure the mapping for user roles in sample-applicationContext-externalAuth-LDAP\[-mt\].xml, locate the bean of the `JSDefaultLdapAuthoritiesPopulator` class, the second constructor argument of `ldapAuthenticationProvider`, and specify the following information:

- `constructor-arg index="1"`: An optional branch DN where group entries are located. If not specified, the search covers your entire LDAP directory starting from the base DN.
- `groupRoleAttribute` property: The attribute whose value is mapped to the name of the JasperReports Server role. Often, this is the `cn` attribute that gives the name of the role in the RDN of the group entry. But it can be any attribute, for example a custom attribute named `Jaspersoft Role Name` defined by a custom LDAP schema.
- `groupSearchFilter` property: A group search filter that locates entries representing groups to which the user belongs. For static groups, this filter should detect entries with the `groupofuniquenames` object class and with a `uniqueMember` value that matches the DN found by the user search. You can use the following parameters:
  - `{0}` represents the full DN of the user entry.
  - `{1}` represents the username.
- `searchSubtree` property: Whether or not the search should extend to all subtrees beneath the branch DN, or beneath the base DN when no branch DN is specified.

`JSDefaultLdapAuthoritiesPopulator` is a wrapper class of the Spring Security `DefaultLdapAuthoritiesPopulator` class. Spring Security supports additional properties; see the [Spring Security documentation](https://docs.spring.io/spring-security/reference/6.5/index.html) for more information.

!!! note

    All internal and external users are assigned `ROLE_USER` by default. So you never need to create or map this role in your LDAP directory.

The following shows an example syntax of the constructor arguments and properties that uses `groupofuniquenames`:

```
<bean id="ldapAuthenticationProvider"  class="com.jaspersoft.jasperserver.api.security.
       externalAuth.wrappers.spring.ldap.JSLdapAuthenticationProvider">
  <constructor-arg> ...
  </constructor-arg>
  <constructor-arg>
    <bean class="com.jaspersoft.jasperserver.api.security.externalAuth.wrappers.
                 spring.ldap.JSDefaultLdapAuthoritiesPopulator">
      <constructor-arg index="0"><ref bean="ldapContextSource"/></constructor-arg>
      <!-- optional branch DN for roles -->
      <constructor-arg index="1"><value></value></constructor-arg>
      <property name="groupRoleAttribute"><value>cn</value></property>
      <property name="groupSearchFilter"><value>
        (&amp;(uniqueMember={0})(objectclass=groupofuniquenames))</value></property>
      <property name="searchSubtree"><value>true</value></property>
    </bean>
  </constructor-arg>
</bean>
```

Be careful when defining the properties for mapping user roles. The search for groups in the LDAP directory must not cause an error, otherwise the entire login will fail. For example, if you specify a branch DN that doesn't exist, the search will cause an error, and users will be unable to log in. A successful search that returns no results will allow users to log in, but without having the intended roles.

After the mapping has determined the role names given to the external user in JasperReports Server:

- In the community edition, which doesn't have the organization architecture, the roles are synchronized with existing roles and assigned to the user.
- In commercial editions, which have the organization architecture, the external user and roles are assigned to an organization that's either the default single organization or an organization mapped from the DN of the LDAP user. Organization mapping is described in [Mapping the User Organization](ldap-setting-user-organization.md).

If you intend for one of the mapped roles to provide administrator privileges, you must explicitly map it to the system roles, as described in [Mapping Roles to System Roles](ldap-mapping-system-roles.md). Otherwise, all mapped roles are created in the mapped organization.

!!! note

    Synchronization creates roles in JasperReports Server if they don’t exist, as described in [Synchronization of Roles](../authentication-in-jrs/synchronization-roles.md).
