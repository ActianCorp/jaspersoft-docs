---
title: Creating a Custom Processor
description: "To create custom code to run on the server after the user has been authenticated, you can create a custom processor and add it to the processors list for the externalUserProcessors property of the..."
---

# Creating a Custom Processor

To create custom code to run on the server after the user has been authenticated, you can create a custom processor and add it to the processors list for the `externalUserProcessors` property of the `externalDataSynchronizer` bean. To create a custom processor, extend the `AbstractExternalSetupProcessor` class or `MTAbstractExternalProcessor` class, which provide access to all the JasperReports Server service classes like the repository and user management. For example, to create a folder, you must use `HibernateRepositoryService` and `ObjectPermissionService`. See the description of Java APIs in the chapter “JasperReports Server APIs” in the JasperReports Server Ultimate Guide for more information on the available JasperReports Server services.

The processors for user setup and tenant mapping in the sample configuration files, like `externalUserProcessors` or `ldapExternalTenantProcessor`, are themselves examples of processor implementation. These processors are described in detail in the sections for each authentication mechanism, for example, [“Mapping to Multiple Organizations” on page 1](../ldap/ldap-setting-user-organization.md).

In addition, many of the sample application context files include an `externalUserFolderProcessor` bean that calls code to automatically create a user home folder for the authenticated user. The following example shows how to add `externalUserFolderProcessor` to the `externalUserProcessors` property of the `ExternalDataSynchronizer` bean:

``` xml
<bean id="externalDataSynchronizer"      class="com.jaspersoft.jasperserver.api.security.externalAuth.ExternalDataSynchronizerImpl">
<property name="externalUserProcessors">
    <list>
      <ref local="externalUserSetupProcessor"/>
      <ref local="externalUserFolderProcessor"/>
    </list>
 </property>
</bean>
```

The following code block shows how you might configure an `externalUserFolderProcessor` bean in your applicationContext-externalAuth-xxx.xml configuration file:

``` xml
<bean id="externalUserFolderProcessor"
      class="com.jaspersoft.jasperserver.api.security.externalAuth.processors.
      ExternalUserFolderProcessor"
      parent="abstractExternalProcessor">
  <property name="repositoryService" ref="${bean.unsecureRepositoryService}"/>
</bean>
```

To write a processor, extend `AbstractExternalUserProcessor` and overwrite the process method with your java code. This gives you access to the following services:

- `RepositoryService`
- `UserAuthorityService`
- `TenantService`
- `ProfileAttributeService`
- `ObjectPermissionService`

If you extend `MTAbstractExternalProcessor`, you can access the following `multiTenancyService` service:
