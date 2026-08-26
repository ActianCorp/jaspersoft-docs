---
title: Protection Domain Infrastructure in Tomcat
description: "Legitimate code can be used to introduce harmful measures into the web application. For instance, calls for disk access and calls to System.Exit can be hidden in classpaths. An effective measure..."
---

# Protection Domain Infrastructure in Tomcat

Legitimate code can be used to introduce harmful measures into the web application. For instance, calls for disk access and calls to `System.Exit` can be hidden in classpaths. An effective measure against such intrusions is to implement a protection domain. In Tomcat, you have to enable the Tomcat Security Manager then edit its parameters according to the requirements of your server environment.

The `ProtectionDomain` class encloses a group of classes whose instances have the same permissions, public keys, and URI. A given class can belong to only one ProtectionDomain. For more information on `ProtectionDomain`, see the [Java documentation](http://download.oracle.com/javase/6/docs/api/java/security/ProtectionDomain.html).

## Enabling the JVM Security Manager

The Security Manager restricts permissions at the application server level. By default, no permissions are disallowed at that level, so legitimate permissions must be specifically added. Add permissions for JasperReports Server. Doing so does not interfere with server operations because JasperReports Server security restrictions occur on other levels.

Add the enabling code for the Security Manager in the file `<apache-tomcat>/conf/catalina.policy`. ProtectionDomains can be enabled, as defined in `<js-webapp>/WEB-INF/applicationContext.xml`, `reportsProtectionDomainProvider` bean.

To enable the Security Manager and give JasperReports Server full permissions there, add the following code fragment at the end of `catalina.policy`.

``` text
// These permissions apply to the JasperReports Server application
grant codeBase "file:${catalina.home}/webapps/jasperserver[-pro]/-" {
      permission java.security.AllPermission;
};

grant codeBase "file:/groovy/script" {  permission java.io.FilePermission "${catalina.home}${file.separator}webapps${file.separator}jasperserver[-pro]${file.separator}WEB-INF${file.separator}classes${file.separator}-", "read";
  permission java.io.FilePermission
 "${catalina.home}${file.separator}webapps${file.separator}jasperserver[-pro]${file.separator}WEB-INF${file.separator}lib${file.separator}*", "read";
     permission java.util.PropertyPermission "groovy.use.classvalue", "read";
};
```

After enabling the manager in catalina.policy, you should limit the packages that the JasperReports Library can access. To do so, edit `<apache-tomcat>/conf/catalina.policy`, locate the `package.access` property, and add the names of the packages that JasperReports Library should be prevented from accessing. We recommend that you block these packages:

-   `com.jaspersoft.jasperserver`
-   `org.springframework`

After editing, it should be similar to:

``` properties
package.access=sun.,org.apache.catalina.,org.apache.coyote.,org.apache.jasper.,
org.apache.tomcat.,com.jaspersoft.jasperserver.,org.springframework.
```

After enabling the manager, you should add the security parameter to your Tomcat startup command. For example:

`<apache-tomcat>\bin\startup -security`

If you did not add the permissions properly, you receive errors like the following:

``` text
Feb 9, 2010 12:34:05 PM org.apache.catalina.core.StandardContext listenerStart
SEVERE: Exception sending context initialized event to listener instance of class org.springframework.web.context.ContextLoaderListener
java.security.AccessControlException: access denied (java.lang.RuntimePermission accessDeclaredMembers)
  at java.security.AccessControlContext.checkPermission(Unknown Source)
  at java.security.AccessController.checkPermission(Unknown Source)
  at java.lang.SecurityManager.checkPermission(Unknown Source)
  at java.lang.SecurityManager.checkMemberAccess(Unknown Source)
  at java.lang.Class.checkMemberAccess(Unknown Source)
  at java.lang.Class.getDeclaredMethods(Unknown Source)
...
```

## Restoring Disallowed Permissions

The file `<js-webapp>/WEB-INF/applicationContext.xml` defines the permissions allowed for `java.security.Class`. You might have to use the file to add permissions disallowed by enabling the Security Manager. On the application level, only specified permissions are granted now, so any application-level permissions you were using have been disallowed. Write code that restores them.

Refer to this commented sample `applicationContext.xml` file when you restore necessary permissions.

For instance, to add permission for read/write access to the `/temp` and JasperReport resources folders, add the `java.io.FilePermission` beans to the `permissions` property of `reportsProtectionDomainProvider`:

``` xml
<bean id="reportsProtectionDomainProvider" class="com.jaspersoft.jasperserver.api.engine.jasperreports.util.
PermissionsListProtectionDomainProvider">
   <property name="permissions">
          <list>
             <bean class="java.io.FilePermission">
                <constructor-arg value="${java.io.tmpdir}${file.separator}*"/>
                <constructor-arg value="read,write"/>
             </bean>

             <bean class="java.io.FilePermission">
                <constructor-arg value="${catalina.home}${file.separator}webapps${file.separator}
               jasperserver[-pro]${file.separator}WEB-INF${file.separator}classes${file.separator}-"/>
                <constructor-arg value="read"/>
             </bean>

             <bean class="java.io.FilePermission">
                 <constructor-arg value="${catalina.home}${file.separator}webapps${file.separator}
                 jasperserver[-pro]${file.separator}WEB-INF${file.separator}lib${file.separator}*"/>
                 <constructor-arg value="read"/>
              </bean>
          </list>
   </property>
</bean>
```
