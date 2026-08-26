---
title: Setting Default Roles
description: You can assign roles to all users using the defaultInternalRoles property of externalUserSetupProcessor or mtExternalUserSetupProcessor. The following example shows how to use this property in...
---

# Setting Default Roles

You can assign roles to all users using the `defaultInternalRoles` property of `externalUserSetupProcessor` or `mtExternalUserSetupProcessor`. The following example shows how to use this property in `externalUserSetupProcessor` to assign `ROLE_USER` to all users, in addition to the roles assigned by mapping:

``` xml
  <property name="defaultInternalRoles">
    <list>
      <value>ROLE_USER</value>
    </list>
  </property>
```

# Avoiding Role Collisions

If an external role has the same name as an internal role at the same organization level, JasperReports Server adds a suffix such as \_EXT to the external role name to avoid collisions. For example, a user with the externally defined role ROLE_ADMINISTRATOR is assigned the role ROLE_ADMINISTRATOR_EXT in the JasperReports Server database. This ensures that internal administrator accounts like jasperadmin and superuser can still log in as internal administrators with the associated permissions.

You can set the extension in the `conflictingExternalInternalRoleNameSuffix` property in the `externalUserSetupProcessor` or `mtExternalUserSetupProcessor` bean. If the property doesn't appear in the bean, the extension is still implemented but defaults to \_EXT. The following example shows how to configure this property:

``` xml
<bean id="mtExternalUserSetupProcessor" class="com.jaspersoft.jasperserver.multipleTenancy.security.
    externalAuth.processors.MTExternalUserSetupProcessor"
    parent="abstractExternalProcessor">
  <property name="conflictingExternalInternalRoleNameSuffix"
        value="_EXTERNAL"/>
  <property name="organizationRoleMap">
      ...
     <!-- Example of mapping customer roles to JRS roles -->
      ...
  </property>
```

# Restricting the Mapping to Whitelisted Roles

You may not want every role in your external authority to appear as a role in JasperReports Server. Use the `permittedRolesRegex` property of the `externalUserSetupProcessor` bean or `mtExternalUserSetupProcessor` bean to specify which external roles become roles in JasperReports Server. You can use regular expressions to specify multiple roles that match the expression.

For example, to restrict the roles you create in JasperReports Server to roles that begin with JRS\_ or EXT\_ in your external authority, you would configure `permittedRolesRegex` in a way similar to the following:

``` xml
        <property name="permittedRolesRegex">
            <list>
                <value>JRS_.*</value>
                <value>EXT_.*</value>
            </list>
        </property>
```

To allow all roles, use .\* or comment out the property. If the property is omitted, all roles in the external authority are synchronized with roles in JasperReports Server.

# Supporting Additional Characters in Role Names

The default mapping from attributes in your external authentication server to roles in JasperReports Server supports only alphanumeric characters and underscores. If a role in your external authority contains unsupported characters, each sequence of unsupported characters is replaced with a single underscore. For example, ROLE$-DEMO)EXT maps to ROLE_DEMO_EXT.

You can extend the supported character set by modifying the `permittedExternalRoleNameRegex` property of the `externalUserSetupProcessor` bean or `mtExternalUserSetupProcessor` bean. Check the sample configuration file for your deployment to determine which bean to modify.

The default value of the `permittedExternalRoleNameRegex` property is the regular expression \[A-Za-z0-9\_\]+. Edit this expression to add supported characters. For example, the following syntax allows alphanumeric characters, underscores, and the Cyrillic letter Я (Unicode 042F):

``` xml
<bean id="mtExternalUserSetupProcessor"  class="com.jaspersoft.jasperserver.api.security.
        externalAuth.processors.MTExternalUserSetupProcessor"
    parent="abstractExternalProcessor">
 <property name="userAuthorityService">
   <ref bean="${bean.internalUserAuthorityService}"/>
 </property>
  .....
 <property name="permittedExternalRoleNameRegex"
     value="[A-Za-z0-9_\u042F]+">
</bean>
```

!!! warning

    Do not allow the following in role names: spaces, periods or \|, \[ \], \`, ", ', \~, !, #, $, %, \^, &, \[,\], \*, +, =, ;, :, ?, &lt;, &gt;, }, {, ), (, \], \[, /, or \\. Adding these characters in the `permittedExternalRoleNameRegex` property may cause unexpected behavior, such as the inability to delete or edit roles containing those characters.
