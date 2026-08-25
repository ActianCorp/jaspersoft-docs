---
title: Changes in 7.2 That May Affect Your Upgrade
description: "JasperReports Server 7.2 removes support for legacy dashboards, created in JasperReports Server version 5.6.2 and earlier. If your JasperReports Server repository contains any legacy dashboards, a..."
---

# Changes in 7.2 That May Affect Your Upgrade

## Removal of Legacy Dashboards

JasperReports Server 7.2 removes support for legacy dashboards, created in JasperReports Server version 5.6.2 and earlier. If your JasperReports Server repository contains any legacy dashboards, a warning message appears during the upgrade. If you continue with the upgrade, your legacy dashboards are permanently deleted. You cannot roll back this operation after it is done.

If you have any legacy dashboards you want to keep, you should recreate them as new dashboards before upgrading. For information on creating dashboards using the Dashboard Designer, see the JasperReports Server User Guide.

## Changes to the Login Page

The layout of the login page changed in JasperReports Server 7.2. There were no changes to the CSS classes, but some default values were changed. If you have customized the login page, test your customizations to ensure they have the desired effect in 7.2, and make any necessary changes. If you have not customized the login page, this change does not affect you.

## Spring Security Upgrade

JasperReports Server uses the Spring Security framework to implement security throughout the product. In JasperReports Server 7.2, the Spring Security framework was updated to Spring Security 4.2. For many users, this upgrade has no impact. However, you may need to make some changes if you have implemented the following:

- External authentication–If you have implemented external authentication or Single Sign-on in your server implementation, you need to update your implementation:

  - If you implemented external authentication using one of the sample files included in the project, you need to reimplement your changes in the updated sample files included in JasperReports Server 7.2.
  - If you have implemented a custom external authentication solution, you need to migrate your solution to the new framework.

- Customizations–If you have customized the server using Spring Security classes, you need to migrate your solution to the new framework.

### Migrating External Authentication Sample Files

If you have implemented external authentication using one of the sample-applicationContext-\<customName\>.xml files located in the \<js‑install\>/samples/externalAuth-sample-config directory, migrate your changes to JasperReports Server 7.2 as follows:

1.  Prior to upgrade, back up your existing applicationContext-\<customName\>.xml (for example, applicationContext-externalAuth-LDAP.xml), located in the \<js-webapp\>/WEB-INF directory of your previous version of JasperReports Server.

2.  Update your server installation to JasperReports Server 7.2, as described in the JasperReports Server Upgrade Guide.

3.  In the new installation, locate the sample file that corresponds to the file you implemented previously. For example, if you implemented applicationContext-externalAuth-LDAP.xml, locate \<js‑install-7.2\>/samples/externalAuth-sample-config/sample-applicationContext-externalAuth-LDAP.xml.

4.  Rename the JasperReports Server 7.2 sample file to remove the sample- prefix. For example, rename sample-applicationContext-externalAuth-LDAP.xml to applicationContext-externalAuth-LDAP.xml.

5.  Configure the properties in the new sample file to match the properties in your existing sample file. To do this:

    1.  Locate each bean that you have modified in the previous version.

    2.  Find the same bean in the JasperReports Server 7.2 sample. The names of the beans have not changed between versions.

    3.  Copy or reenter the properties you need for your server, taking care not to copy over class names or class packages.

        !!! warning

            Although the bean names are the same in the JasperReports Server 7.2 sample files, the name and package of the class in many bean definitions have changed. Make sure not to overwrite the new names with the old ones.

    4.  Save the JasperReports Server 7.2 sample file.

    5.  Rename the JasperReports Server 7.2 sample file to remove the sample- prefix. For example, rename sample-applicationContext-externalAuth-LDAP.xml to applicationContext-externalAuth-LDAP.xml.

    6.  Place the modified file in the \<js-webapp-7.2\>/WEB-INF directory.

### Migrating Customizations

The Spring Security codebase was significantly restructured from 3.x to 4.x. Many classnames have changed and other classes were moved to different packages. In addition, many classes were deprecated. At a minimum, you need to update the names and paths of the Spring Security classes you reference in any customizations you have made to JasperReports Server For information on updating your customizations, see the *Spring Security migration guide*:

<https://docs.spring.io/spring-security/site/migrate/current/3-to-4/html5/migrate-3-to-4-xml.html>

For specific information about migrating from deprecated classes in 4.x, see the [Deprecations](https://docs.spring.io/spring-security/site/migrate/current/3-to-4/html5/migrate-3-to-4-xml.html#m3to4-deprecations) topic in the same document.
