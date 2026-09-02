---
title: Mapping the User Organization
description: Organizations are a feature of JasperReports Server commercial editions. Skip this section if you have JasperReports Server community edition.
---

# Mapping the User Organization

!!! note

    Organizations are a feature of JasperReports Server commercial editions. Skip this section if you have JasperReports Server community edition.

In implementation that supports multiple organizations, all users and roles except for system administrators and system roles belong to organizations. In turn, each organization determines the folders that its users can access in the repository. So the final part of mapping is to determine an organization ID for the external user and roles, based on the user’s RDN in the directory.

If your JasperReports Server supports multiple organizations, you have two ways to set the user organization for external users:

-   Create a mapping from RDNs in your LDAP server to organizations in JasperReports Server, as described in [Mapping to Multiple Organizations](#mapping-to-multiple-organizations).
-   If you want all users to be in just one of your organizations, use the `externalTenantSetupProcessor` bean to specify the organization, as described in [Mapping to a Single Organization](#mapping-to-a-single-organization).

If your JasperReports Server deployment supports only a single organization (all community deployments and some professional editions), you do not need to set organization information.

## Mapping to Multiple Organizations

LDAP is well suited to mapping users into organizations, because LDAP itself has a hierarchical structure of user entries that's often used to represent separate organizations, such as the internal departments of a company. The LDAP tree structure is reflected in the elements of the RDN of each user entry, and the server maps this RDN into an organization or hierarchy of organizations for the external user. For example, the users `uid=jack,ou=audit,ou=finance,dc=example,dc=com` and `uid=jill,ou=accounting,ou=finance,dc=example,dc=com` could be mapped to the organizations `audit` and `accounting`, respectively, both of which are sub-organizations of `finance`.

In order to ensure consistency, the server must create the organization of any external user if the organization does not already exist. The server also creates any organization that does not exist in the hierarchy of organizations mapped from the user RDN. To avoid “stray” organizations outside of your intended hierarchy, test your mapping against all potential user DNs in your LDAP directory.

Organizations created during external user login have an administrator with a default password. The admin username and password is configurable. See [Setting Up Default Admins for Organizations](#setting-up-default-admins-for-organizations) for more information. For security reasons, you should change the default password of any organization admin created. See [Initialization of JasperReports Server for External Users](../authentication-in-jrs/initializing-external-users-in-jrs.md) for a process to initialize the server, including organization admins, before going into production with external authentication.

### Setting Up Organization Mapping

Specify the following information in the `ldapExternalTenantProcessor` bean to map the RDN of the user to a hierarchy of organizations in JasperReports Server:

-   `excludeRootDn` property: Property that specifies whether the base DN, also called root DN, should be mapped along with the RDN. For example, if the property list for `organizationRDNs` contains `dc` and you don't exclude the base DN of `dc=example,dc=com`, the base DN maps to the following: the organization ID `example` nested inside the organization ID `com` nested inside the specified root organization. The base DN is part of the LDAP URL specified in [Setting the LDAP Connection Parameters](ldap-setting-connection-parameters.md).
-   `organizationRDNs` property: A list of attribute names that determines which RDN values should be mapped to organization names. The names in this list determine the RDNs that creates a hierarchy of organizations in JasperReports Server. For example, if you specify the value `ou`, each RDN with `ou=<name>` creates a level in the hierarchy of mapped organizations. If this list is blank or none of the attributes match the RDN of the user entry, the `defaultOrganization` property determines the organization name.
-   `rootOrganizationId` property: The ID of an organization under which any mapped organizations are created as sub-organizations. If the root organization ID is absent or blank (`""`), the server creates the organization(s) mapped in `organizationRDNs` as children of the default organization shipped with JasperReports Server.
-   `defaultOrganization` property (optional): The ID of an organization assigned to users that would otherwise be mapped to a null organization ID.

!!! warning

    If `excludeRootDn = true`, `defaultOrganization = ""` or is absent, and no `organizationRDNs` match in the DN of the user, the user will have a null organization ID. The null organization ID is usually reserved for special users like the system administrator and allows access the repository folder of all other organizations. To avoid this mapping, specify a value for `defaultOrganization` or ensure that every user has one of the `organizationRDNs`.

The following example shows the syntax of the `ldapExternalTenantProcessor` bean and its properties:

``` xml
<bean id="ldapExternalTenantProcessor" class="com.jaspersoft.jasperserver.multipleTenancy.security.
      externalAuth.processors.ldap.LdapExternalTenantProcessor" parent="abstractExternalProcessor">
  <property name="ldapContextSource" ref="ldapContextSource" />
  <property name="multiTenancyService">
    <ref bean="internalMultiTenancyService"/></property>
  <property name="excludeRootDn" value="false"/>
  <!-- only following RDNs matter in creating the organization hierarchy -->
  <property name="organizationRDNs">
    <list>
      <value>o</value>
      <value>ou</value>
    </list>
  </property>
  <property name="rootOrganizationId" value="organization_1"/>
  <property name="defaultOrganization" value="#{configurationBean.tenantIdNotSupportedSymbols}"/>
...
</bean>
```

For example, given the `ldapExternalTenantProcessor` bean configuration above, an LDAP user with the DN `uid=jack,ou=audit,ou=finance, dc=example,dc=com` is placed in a organization named `audit` which is a child of an organization named `finance`, which in turn is a child of `organization_1`. This example illustrates that it's not possible to map only one of the two RDN components if they have the same attribute. In other words, the mapping mechanism does not let you choose to create only the `audit` or the `finance` organization; both are created if you specify `ou` in the list of `organizationRDNs`.

!!! note

    By default, the sample-applicationContext-externalAuth-LDAP-mt.xml file maps users to multiple organizations. If you want to map all users to a single organization, see [Mapping to a Single Organization.](ldap-setting-user-organization.md)

### Setting Up Default Admins for Organizations

In a multi-organization deployment, JasperReports Server creates a `jasperadmin` user whenever you create a new organization. The `jasperadmin` user is also given a standard default password. When creating multiple organizations using external authentication, you can set a different default password for jasperadmin, remove the jasperadmin user, and/or create additional default users in each new organization created by external authentication. Optionally, you can encrypt the password in the configuration files. See the JasperReports Server Security Guide for more information on default users in every organization.

!!! warning

    For security reasons, you should change the default password of any organization admin. See [Initialization of JasperReports Server for External Users](../authentication-in-jrs/initializing-external-users-in-jrs.md) for a process to initialize the server, including organization admins, before going into production with external authentication.

To set up admin users

1.  Open your sample-applicationContext-xxx-externalAuth.xml file in a text editor.

2.  Locate the `externalTenantSetupUsers` property in the `ldapExternalTenantProcessor``externalTenantSetupProcessor` bean.

3.  The sample contains a bean of class `ExternalTenantSetupUser` already configured for `jasperadmin`.

    ``` xml
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

4.  To create additional admin users for each external organization, create a bean of class `ExternalTenantSetupUser` for each admin user you want.

    ``` xml
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

5.  The ${...} syntax above references values configured in the following file:

    &lt;js-install&gt;\\buildomatic\\conf_source\\iePro\\js.config.properties file.

    To set these values, open &lt;js-install&gt;\\buildomatic\\conf_source\\iePro\\js.config.properties and edit the entries there.

    ``` properties
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

6.  If you want to obfuscate the default passwords in the js.config.properties files, encrypt them as described in the JasperReports Server Security Guide. Obfuscation must be implemented before you install the server.

7.  If you don't want to obfuscate default passwords, you can eliminate the reference to js.config.properties and instead configure the values directly in the `externalTenantSetupUsers` property in the applicationContext-externalAuth-xxx.xml file. For example:

``` xml
      <property name="username" value="anotheradmin"/>
      <property name="fullName" value="Another Admin"/>
      <property name="password" value="anotherpassword"/>
      <property name="emailAddress" value=""/>
```

### Mapping Organization Names

You have the option to use the `organizationMap` property in the `externalTenantSetupProcessor``ldapExternalTenantProcessor` bean to map organization names extracted from your external authority to organization names in JasperReports Server. To do this, create a key/value pair for each organization you want to map, specifying the external organization name as the key and the organization name in JasperReports Server as the value. When mapping organizations, the server determines the mapped name and uses it as the name, ID, and description of the organization.

For example, the following would map users in External_Org_1 in the external authority to JRS_Org_1 in JasperReports Server and users in External_Org_2 in the external authority to JRS_Org_2 in JasperReports Server:

``` xml
    <property name="organizationMap">
        <map>
            <entry key="External_Org_1" value="JRS_Org_1" />
            <entry key="External_Org_2" value="JRS_Org_2" />
        </map>
    </property>
```

The `organizationMap` property is optional. Any organization in your external authority that is not listed in `organizationMap` is mapped to an organization of the same name in JasperReports Server. However, if an organization in your external authority contains unsupported characters, each sequence of unsupported characters is replaced with a single underscore. For example, Human Resources maps to Human_Resources.

The `tenantIdNotSupportedSymbols` property of the `configurationBean` bean in the applicationContext.xml file lists the unsupported characters, including spaces and the following characters: `|`, `&`, `*`, `?`, `<`, `>`, `/`, `\`, `~`, `!`, `#`, `$`, `%`, `^`, `[`, `]`, or a space. If you want to list additional characters that should be replaced with an underscore, you can add them in this bean. However, we do not recommend removing any of the pre-defined characters, as JasperReports Server may not handle them correctly.

## Mapping to a Single Organization

If you have a commercial version of JasperReports Server, you can choose to map all external users to a single organization, for example, in the following cases:

-   You have a commercial JasperReports Server deployment that does not implement multiple organizations, but instead uses the default organization. This includes commercial versions licensed for a single organization. In this case, externally authenticated users must be mapped to the default organization.
-   You have multiple organizations in JasperReports Server, but still want all external users to be placed in a single organization.

The following steps show how to map all external users to a single organization using the sample-applicationContext-externalAuth-LDAP-mt.xml file:

1.  In sample-applicationContext-externalAuth-LDAP-mt.xml, locate the first instance of the `ldapExternalTenantProcessor` bean and comment the bean out.
2.  Locate the second instance of the `ldapExternalTenantProcessor` bean and uncomment it.
3.  Set the `defaultOrganization` property to the organization you want assigned to all external LDAP users.

!!! note

    `ldapExternalTenantProcessor` is an example of a processor. For more information about processors, see [Creating a Custom Processor](../advanced-topics/creating-custom-processor.md).

    The `ldapExternalTenantProcessor` bean is not available in the community edition. You don't need to set the organization in the community edition.

The following example places all external users in the default organization, `organization_1`.

``` xml
<bean id="ldapExternalTenantProcessor"
        class="com.jaspersoft.jasperserver.multipleTenancy.security.
              externalAuth.processors.ldap.LdapExternalTenantProcessor"
        parent="abstractExternalProcessor">
  <property name="ldapContextSource" ref="ldapContextSource"/>
  <property name="multiTenancyService"><ref bean="internalMultiTenancyService"/></property>
  <property name="excludeRootDn" value="true"/>
  <property name="defaultOrganization" value="organization_1"/>
</bean>
```

!!! warning

    Make sure you specify a value for the `defaultOrganization`. If `defaultOrganization` is left empty, users may be mapped to the null organization id. This is usually reserved for special users like the system administrator and allows access to the repository folder of all other organizations.
