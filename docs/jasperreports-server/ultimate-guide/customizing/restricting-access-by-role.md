---
title: Restricting Access by Role
description: "You can use role-based customizations to control access to many user interface components, including menus, Java Server Pages, and web flows. This example shows how to control access to existing UI..."
---

# Restricting Access by Role

You can use role-based customizations to control access to many user interface components, including menus, Java Server Pages, and web flows. This example shows how to control access to existing UI components; the same techniques work with your custom components.

In this example, suppose end users haven’t had training in creating reports with the Ad Hoc Editor, and you want to hide it from users, but make it accessible to administrators. To hide access to the Ad Hoc Editor, you need to customize the UI in three ways:

- Customize the **Create** menu to restrict access to Ad Hoc creation to administrators only

- Customize the JSP content on the home page to hide the **Create Ad Hoc View** button from non-administrative users.

- Customize the Ad Hoc web flow to restrict access to administrators only.

The following sections show how to perform each of these actions.

!!! warning

    Be very careful when editing the JSP or XML files that define the UI. Simple typos or bugs such as unclosed tags can cause the server to appear in an incorrect state, or make it impossible to log in. After fixing a problem, you may need to restart the app server; reloading the web app doesn’t always resolve the issue.

## Restricting a Menu Item by Role

1.  Edit the file `<js-webapp>/WEB-INF/actionModel-navigation.xml`. The actionModel for ****Create \> Ad Hoc View**** is near the end of the file.

``` text
...
<context name="main_create_mutton" test="isProVersion">
  <condition test="!banUserRole">
    <condition test="!isMainFeaturesDisabled">
      <selectAction labelKey="NAV_005_CREATE">
        <condition test="isAvailableProFeature" testArgs="AHD">
          <condition test="checkAuthenticationRoles" testArgs="ROLE_ADMINISTRATOR">
          <option labelKey="NAV_051_ADHOC_REPORT"
          action="primaryNavModule.navigationOption"
          actionArgs="designer"/>
          </condition>
        </condition>
 ...
      </selectAction>
    </condition>
  </condition>
</context>
```

1.  Following the pattern of conditions for other administrator-only functionality, insert the `condition` tag for checking role authentication around the `option` tag to display the Ad Hoc menu item, as shown in the code sample above.

!!! note

    In commercial editions, you must specify the role’s organization ID when restricting access to roles defined in an organization. Use one of these methods:

    - `ORG_ROLE|orgID`: Explicitly specify a role belonging to an organization.

    - `SYSTEM_ROLE`: Explicitly specify a role defined at the root or system level, such as `ROLE_ADMINISTRATOR`.

!!! note

    If you want to hide an entire menu, follow the pattern of the Manage menu, which is hidden from non-administrators. In this case, add the `test` and `testArgs` attributes to the `context` tag that displays the menu, as shown in the following sample:

``` text
...
<!-- The Manage menu is displayed only to administrators -->
<context name="main_manage_mutton"
         test="checkAuthenticationRoles" testArgs="ROLE_ADMINISTRATOR">
  <selectAction labelKey="menu.administration">
  </selectAction>
</context>
...
```

## Restricting a Section of a JSP File by Role

You can use Spring Security’s authorization tags to set up access control on JSP pages. See the example below for how this tag is used. As described in the Spring documentation, the `authz:authorize` tag supports the following attributes:

- `hasRole`: All the listed roles must be granted for the tag to output its body.

- `hasAnyRole`: Any of the listed roles must be granted for the tag to output its body.

- `!hasAnyRole`: None of the listed roles must be granted for the tag to output its body.

The attributes take roles as values. To list multiple roles in an attribute, separate the roles using a comma.

To use the authorization tags in a JSP file:

1.  Make sure the line to import the Spring `authz` tag is near the beginning of the file. This line is necessary in any JSP file that implements access control:

`<%@ taglib uri="http://www.springframework.org/security/tags" prefix="authz"%>`

``` text
...
<%@ taglib prefix="t" uri="http://tiles.apache.org/tags-tiles" %>
<%@ taglib prefix="authz" uri="http://www.springframework.org/security/tags"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jstl/core_rt" %>
<%@ taglib uri="/spring" prefix="spring"%>
...

<authz:authorize access="hasRole('ROLE_ADMINISTRATOR')">
    <a id="createReports" class="button action jumbo up"><span
      class="wrap"><spring:message code="home.create" javaScriptEscape="true"/>
      </span><span class="icon"></span></a>
</authz:authorize>

...
```

1.  Insert the `authz:authorize` tag for checking role authentication before the element you want to restrict, as shown in the code sample above.

!!! note

    In commercial editions, you must also use the authz:authorize tag and specify the role’s organization ID when restricting access to roles defined in an organization. For example:

    `<authz:authorize access="hasRole('ORG_ROLE|OrgID')">...</authz:authorize>`

    You can use the `ORG_ROLE|OrgID` or `SYSTEM_ROLE` syntax, as described in [“Restricting a Menu Item by Role” on page 1](restricting-access-by-role.md).

See the [Spring Security Reference Documentation](https://docs.spring.io/spring-framework/docs/5.3.29/reference/html/) for more information.

## Controlling Access to Web Flows

JasperReports Server uses Spring Web Flow to define and control its UI flow. A Spring flow is a sequence of related pages for which you define states and transitions in relation to your own business logic. In addition to controlling users’ access to items on the menus, you can control their access to functionality by setting permissions on web flows.

!!! warning

    Be very careful when setting access to existing web flows. UI components that depend on a web flow may not work properly if access to the web flow has been modified.

In this example, suppose you want to ensure users cannot access the Ad Hoc Editor through its URI. To do this, restrict the Ad Hoc web flow to administrative users:

1.  Navigate to the Ad Hoc Editor by clicking the **Create Ad Hoc View** button on the home page. You see the URI for the flow in the navigation bar:

`http://localhost:8080/jasperserver-pro/flow.html?_flowId=adhocFlow`

This tells you that the URI for the Ad Hoc Editor flow is `adhocFlow`.

1.  Open the file `<js-webapp>/WEB-INF/applicationContext-security.xml` for editing.
2.  Locate the `flowVoter` bean.

This bean sets the permissions for flows. It contains a number of flows set to `ROLE_ADMINISTRATOR`. Note that `adhocFlow` does not appear explicitly. However, there is an entry `*=ROLE_USER,ROLE_ADMINISTRATOR`. This setting determines access for all flows that are not specifically mentioned.

``` xml
<bean id="flowVoter"
  class="com.jaspersoft.jasperserver.api.security.FlowRoleAccessVoter">
  <property name="flowAccessAttribute" value="FLOW_ACCESS"/>
  <property name="flowDefinitionSource">
     <value>
      repoAdminFlow=ROLE_ADMINISTRATOR
      ...
      searchFlow=ROLE_USER,ROLE_ADMINISTRATOR
      *=ROLE_USER,ROLE_ADMINISTRATOR
      <!--custom flow permissions -->
         adhocFlow=ROLE_ADMINISTRATOR
    </value>
  </property>
</bean>
```

1.  Set access for the Ad Hoc flow by adding an entry to restrict access to `ROLE_ADMINISTRATOR` as shown in the code sample above.

## Controlling Access to the Scheduler and Dashboards UI

Restricting the Scheduler or Dashboards UI to an administrator requires editing a different file.

To restrict Scheduler or Dashboards to administrative users:

1.  Open the file `<js-webapp>/WEB-INF/applicationContext-security-web.xml`.

!!! note

    1.  For commercial versions of JasperReports Server, you will also need to edit a second file, `<js-webapp>``/WEB-INF/applicationContext-security-pro-web.xml`, to restrict the Dashboards UI. The `applicationContext-security-web.xml` file only controls dashboards for the Community Project version.

1.  Locate the `filterInvocationInterceptor` bean.

The entries for the intercept-URL patterns `/scheduler/main.html` and `/dashboard/viewer.html` determine the access for Scheduler and Dashboards.

``` xml
 <bean id="filterInvocationInterceptor"
  class="org.springframework.security.web.access.intercept.FilterSecurityInterceptor">
  <property name="securityMetadataSource">
    <security:filter-security-metadata-source lowercase-comparisons="true"
     path-type="ant" request-matcher="ant">
      ...
      <!--scheduler-->
      <security:intercept-url pattern="/scheduler/main.html"access="ROLE_USER,ROLE_ADMINISTRATOR" />
      ...
      <!--dashboard-->
      <security:intercept-url pattern="/dashboard/viewer.html" access="ROLE_USER,ROLE_ADMINISTRATOR" />
    </security:filter-security-metadata-source>
  </property>
</bean>
```

1.  Set access for Scheduler and Dashboards by removing `ROLE_USER`.
2.  For commercial versions of JasperReports Server, open the file `<js-webapp>/WEB-INF/applicationContext-security-pro-web.xml`.
3.  Locate the entry for the intercept-URL pattern for `/dashboard/viewer.html`.
4.  Set access for Dashboards by removing `ROLE_USER`.

## Loading Your Changes

1.  Save the modified files and reload the web app in the app server to see the changes (see [1.0.1, “Reloading the JasperReports Server Web App,” on page 1](reloading-jrs-webapp.md)).
2.  When the web app has reloaded, log into JasperReports Server as `joeuser`. You'll see that the button for creating a report is removed, and there's no ****Create \> Create Ad Hoc Report**** menu item. Log out and log back in as `jasperadmin`. Both the button and the menu item are visible to administrators.
