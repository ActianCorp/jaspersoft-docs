---
title: Setting the User Organization
description: Organizations are a feature of JasperReports Server commercial editions. Skip this section if you have JasperReports Server community edition.
---

# Setting the User Organization

!!! note

    Organizations are a feature of JasperReports Server commercial editions. Skip this section if you have JasperReports Server community edition.

In the sample-applicationContext-externalAuth-db-mt.xml file, the `tenantId` is returned within the field `usersByUsernameAndTenantNameQuery` in `externalUserTenantDetailsService`. This query provides the required information to the tenant processor, so no additional configuration is needed.

Organizations created during external user login have an administrator with a default password. The admin username and password are configurable. See Setting Up Default Admins for Organizations. For security reasons, you should change the default password of any organization admin. See [Initialization of JasperReports Server for External Users](../authentication-in-jrs/initializing-external-users-in-jrs.md) for a process to initialize the server, including organization admins, before going into production with external authentication.

## Setting Up Default Admins for Organizations

In a multi-organization deployment, JasperReports Server creates a `jasperadmin` user whenever you create a new organization. The `jasperadmin` user is also given a standard default password. When creating multiple organizations using external authentication, you can set a different default password for jasperadmin, remove the jasperadmin user, and/or create additional default users in each new organization created by external authentication. Optionally, you can encrypt the password in the configuration files. See the JasperReports Server Security Guide for more information on default users in every organization.

!!! warning

    For security reasons, you should change the default password of any organization admin. See [Initialization of JasperReports Server for External Users](../authentication-in-jrs/initializing-external-users-in-jrs.md) for a process to initialize the server, including organization admins, before going into production with external authentication.

To set up admin users

1.  Open your sample-applicationContext-xxx-externalAuth.xml file in a text editor.
2.  Locate the `externalTenantSetupUsers` property in the `ldapExternalTenantProcessor``externalTenantSetupProcessor` bean.
3.  The sample contains a bean of class `ExternalTenantSetupUser` already configured for `jasperadmin`.

```
<property name="externalTenantSetupUsers">
  <list>
    <bean class="com.jaspersoft.jasperserver.multipleTenancy.security.
                 externalAuth.processors.MTAbstractExternalProcessor.ExternalTenantSetupUser">
      <property name="username" value="${new.tenant.user.name.1}"/>
      <property name="fullName" value="${new.tenant.user.fullname.1}"/>
      <property name="password" value="${new.tenant.user.password.1}"/>
      <property name="emailAddress" value="${new.tenant.user.email.1}"/>
      <property name="roleSet">
        <set>
          <value>ROLE_ADMINISTRATOR</value>
          <value>ROLE_USER</value>
        </set>
      </property>
    </bean>
  </list>
</property>
```

1.  To create additional admin users for each external organization, create a bean of class `ExternalTenantSetupUser` for each admin user you want.

```
<bean class="com.jaspersoft.jasperserver.multipleTenancy.security.
                 externalAuth.processors.MTAbstractExternalProcessor.ExternalTenantSetupUser">
      <property name="username" value="${new.tenant.user.name.2}"/>
      <property name="fullName" value="${new.tenant.user.fullname.2}"/>
      <property name="password" value="${new.tenant.user.password.2}"/>
      <property name="emailAddress" value="${new.tenant.user.email.2}"/>
 <property name="roleSet">
        <set>
          <value>ROLE_ADMINISTRATOR</value>
          <value>ROLE_USER</value>
        </set>
      </property>
    </bean>
```

1.  The \${...} syntax above references values configured in the following file:

\<js-install\>\buildomatic\conf_source\iePro\js.config.properties file.

To set these values, open \<js-install\>\buildomatic\conf_source\iePro\js.config.properties and edit the entries there.

```
new.tenant.user.name.1=jasperadmin
new.tenant.user.fullname.1=jasperadmin
new.tenant.user.password.1=mynewpassword
new.tenant.user.email.1=
new.tenant.user.name.2=anotheradmin
new.tenant.user.fullname.2=Another Admin
new.tenant.user.password.2=anotherpassword
new.tenant.user.email.2=
```

!!! note

    The property names, for example, `new.tenant.user.name.1`, are arbitrary. You can use any name for each property as long as the name in the applicationContext-externalAuth-xxx.xml file matches the name in the js.config.properties file.

1.  If you want to obfuscate the default passwords in the js.config.properties files, encrypt them as described in the JasperReports Server Security Guide. Obfuscation must be implemented before you install the server.
2.  If you don't want to obfuscate default passwords, you can eliminate the reference to js.config.properties and instead configure the values directly in the `externalTenantSetupUsers` property in the applicationContext-externalAuth-xxx.xml file. For example:

```
      <property name="username" value="anotheradmin"/>
      <property name="fullName" value="Another Admin"/>
      <property name="password" value="anotherpassword"/>
      <property name="emailAddress" value=""/>
```

## Mapping Organization Names

You have the option to use the `organizationMap` property in the `externalTenantSetupProcessor``ldapExternalTenantProcessor` bean to map organization names extracted from your external authority to organization names in JasperReports Server. To do this, create a key/value pair for each organization you want to map, specifying the external organization name as the key and the organization name in JasperReports Server as the value. When mapping organizations, the server determines the mapped name and uses it as the name, ID, and description of the organization.

For example, the following would map users in External_Org_1 in the external authority to JRS_Org_1 in JasperReports Server and users in External_Org_2 in the external authority to JRS_Org_2 in JasperReports Server:

```
    <property name="organizationMap">
        <map>
            <entry key="External_Org_1" value="JRS_Org_1" />
            <entry key="External_Org_2" value="JRS_Org_2" />
        </map>
    </property>
```

The `organizationMap` property is optional. Any organization in your external authority that is not listed in `organizationMap` is mapped to an organization of the same name in JasperReports Server. However, if an organization in your external authority contains unsupported characters, each sequence of unsupported characters is replaced with a single underscore. For example, Human Resources maps to Human_Resources.

The `tenantIdNotSupportedSymbols` property of the `configurationBean` bean in the applicationContext.xml file lists the unsupported characters, including spaces and the following characters: `|`, `&`, `*`, `?`, `<`, `>`, `/`, `\`, `~`, `!`, `#`, `$`, `%`, `^`, `[`, `]`, or a space. If you want to list additional characters that should be replaced with an underscore, you can add them in this bean. However, we do not recommend removing any of the pre-defined characters, as JasperReports Server may not handle them correctly.

## Specifying a Single Organization

If you have multiple organizations in your deployment, you can use the `externalTenantSetupProcessor``ldapExternalTenantProcessor` bean to specify a single organization assigned to all external users. To do this, set `externalTenantSetupProcessor``ldapExternalTenantProcessor`’s `defaultOrganization` property to the organization ID of the selected organization. If an organization with that ID already exists, all external users are assigned to that organization. If the organization does not exist, it's created when the first external user authenticates correctly.

When specifying the `defaultOrganization` value, the organization ID must not contain the following characters: \|, &, \*, ?, \<, \>, /, \\ ~, !, \#, \$, %, ^, \[, or \].

The following example shows how to configure `externalTenantSetupProcessor``ldapExternalTenantProcessor` to assign all users to organization_1:

```
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
