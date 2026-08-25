---
title: Setting the Home Page
description: The home page is the first page a user sees when logging in to JasperReports Server. You can set the home page to a specified flow based on user role.
---

# Setting the Home Page

The home page is the first page a user sees when logging in to JasperReports Server. You can set the home page to a specified flow based on user role.

**Setting the Library as the Home Page**

The following example shows how to set the library page as the home page of a non-administrative user:

1.  Open the file `<js-webapp>\WEB-INF\jasperserver-servlet-pro.xml` (commercial editions) or `jasperserver-servlet.xml` (community edition) for editing.

2.  Locate the home page bean:

    `proHomePageByRole` (commercial editions)

    `homePageByRole` (community edition)

3.  Locate the line under this bean for `ROLE_USER` and modify it to direct to the library page:

    ``` xml
    <bean id="proHomePageByRole" class="java.util.ArrayList">
    <constructor-arg>
    <list>
    <value>ROLE_ADMINISTRATOR|redirect:/flow.html?_flowId=homeFlow</value>
    <value>ROLE_USER|redirect:/flow.html?_flowId=searchFlow&amp;mode=library</value>
    </list>
    </constructor-arg>
    </bean>
    ```

    !!! note

        For a user with multiple roles, the `proHomePageByRole` bean redirects the user to the page specified by the first matching role on the list. For example, for an administrator with ROLE_ADMINISTRATOR and ROLE_USER roles, the `ROLE_ADMINSTRATOR` redirect is applied because it appears first in the bean. When adding your own roles to this bean, insert them in the order that works for you.

4.  Save the modified file and reload the web app in the app server to see the changes (see [1.0.1, “Reloading the JasperReports Server Web App,” on page 1](reloading-jrs-webapp.md)).

5.  Log into JasperReports Server as joeuser. The library page is displayed.

!!! note

    You can use this method for dashboards. For example:

    `<value>ROLE_ADMINISTRATOR|redirect:/dashboard/viewer.html#/public/Samples/Dashboards/1._Supermart_Dashboard</value>`

    This method does not work with `viewReportFlow`.

Setting a report as the home page

The following example shows how to set a report as the home page based on a role. This example uses the 01. Geographic Results by Segment Report.

!!! note

    All roles should start with the prefix 'ROLE\_'.

    For example:

    `'ROLE_MANAGER_DIME'`

1.  First, set up the role and create a sample user:

    1.  Create the role you want to use, for example, `ROLE_REPORT_HOME`.
    2.  Create a user HomeUser and add `ROLE_REPORT_HOME` to HomeUser.

2.  Open the file `<js-webapp>\WEB-INF\jsp\modules\home\home.jsp` in an editor and add the following lines:

    ``` xml
    <authz:authorize access="hasRole('ROLE_REPORT_HOME')">
    <c:redirect
            url="http://localhost:8080/jasperserver-pro-601/flow.html?_flowId=viewReportFlow
            &standAlone=true&_flowId=viewReportFlow&ParentFolderUri=%2Fpublic%2FSamples%2FReports&
            reportUnit=%2Fpublic%2FSamples%2FReports%2F01._Geographic_Results_by_Segment_Report"/>
    </authz:authorize>
    ```

    !!! note

        To find the URI for the report you want to use, open the report in the repository and copy the URI.

3.  Save the modified file and restart the application server to see changes.

4.  Log into JasperReports Server as HomeUser. The report is displayed.
