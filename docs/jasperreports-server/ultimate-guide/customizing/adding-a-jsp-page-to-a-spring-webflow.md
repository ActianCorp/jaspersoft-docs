---
title: Adding a Custom JSP Page in a Spring Web Flow
description: "The flexibility of JasperReports Server lets you create your own JSP pages that integrate into the UI. In order for the SiteMesh decorator to process a custom JSP page, you must integrate it into the..."
---

# Adding a Custom JSP Page in a Spring Web Flow

The flexibility of JasperReports Server lets you create your own JSP pages that integrate into the UI. In order for the SiteMesh decorator to process a custom JSP page, you must integrate it into the Spring Web Flow framework. A flow is a sequence of related pages for which you define states and transitions in relation to your own business logic. This example shows how to add a single page, but you could integrate a series of pages and the navigation among them.

To further integrate your pages with the server, you should use the CSS building blocks provided in themes to replicate the menu and column layout of the server. You can then apply the default theme of the UI or design your own style in a custom theme.

Spring Web Flow relies on the Spring MVC (Model, View, and Controller) module to implement the web interface, where the controller is a Java class. As a result, adding business logic to a web flow involves creating Java methods to implement the logic. In general, the server UI contains most of the functionality in action class code that can be associated with one or more JSP pages. The JSP files have minimal functionality because JSP code logic can become very cluttered and hard to follow. The action classes are pure Java and easier to organize. In this example, the Java method simply returns `success` whenever it's invoked.

For more information, refer to the [Spring documentation](https://docs.spring.io/spring-framework/docs/5.3.29/reference/html/) for flows and MVC.

This example requires you to work with the JasperReports Server source code, as explained in [Working With Source Code Files](customizing-java-classes.md).

This example is divided into several tasks:

1.  Adding a custom JSP file integrated into the server as a web flow.
2.  Creating an action and adding it to the web flow.
3.  Adding the web flow to a menu.

**Example of adding a custom JSP file integrated into the server as a web flow**

1.  Create a subdirectory named sampleFlow for the JSP files in your flow module in `<js-src>/jasperserver-pro/jasperserver-war/src/main/webapp/WEB-INF/jsp/`. For example:

    `cd <js-src>/jasperserver-pro/jasperserver-war/src/main/webapp/WEB-INF/jsp/`

    `mkdir sampleFlow`

2.  Create the following JSP file and save it as `sampleView.jsp` in `<js-src>/jasperserver-pro/jasperserver-war/src/main/webapp/WEB-INF/jsp/sampleFlow`:

    ``` html
    <html>
    <head><title>Sample Page</title>
    </head>
    <body class="oneColumn primary column">
    <h1 class="textAccent">Hello World!</h1>
    </body>
    </html>
    ```

    !!! note

        Design the layout of your custom content based on the UI components in the server. The UI components are defined in the CSS files in the `<js-src>/jasperserver/jasperserver-war/src/main/webapp/themes/default/` directory.

        This example uses a one-column layout and the `textAccent` font.

3.  Create the following XML file with a `flow` container element and an empty `view-state` element. In a later step, you will add an action state:

    ``` xml
    <?xml version="1.0" encoding="UTF-8"?>
    <flow xmlns="http://www.springframework.org/schema/webflow"
           xmlns:ns0="http://www.w3.org/2001/XMLSchema-instance"
           ns0:schemaLocation="http://www.springframework.org/schema/webflow
           http://www.springframework.org/schema/webflow/spring-webflow-2.0.xsd"
           start-state="sampleView">

        <view-state id="sampleView" view="modules/sampleFlow/sampleView">
        </view-state>

        <end-state id="done"/>

    </flow>
    ```

4.  Name the file `docSampleFlow.xml` and save it in the `<js-src>/jasperserver/jasperserver-war/src/main/webapp/WEB-INF/flows` directory.

    **Example of setting flow permissions**

5.  Set permissions for your flow:

    1.  Edit the file `<js-src>/jasperserver/common/shared-config/applicationContext-security.xml`.

    2.  Locate the `flowVoter` bean. This bean sets the permissions for flows.

    3.  Add a line for your flow and set the permissions to `ROLE_ADMINISTRATOR`.

        ``` xml
        <bean id="flowVoter"
                  class="com.jaspersoft.jasperserver.api.security.FlowRoleAccessVoter">
            <property name="flowAccessAttribute" value="FLOW_ACCESS"/>
            <property name="flowDefinitionSource">
              <value>
                repoAdminFlow=ROLE_ADMINISTRATOR
                ...
                docSampleFlow=ROLE_ADMINISTRATOR
                <!--objectPermissionToUserFlow=ROLE_ADMINISTRATOR-->
                searchFlow=ROLE_USER,ROLE_ADMINISTRATOR
                *=ROLE_USER,ROLE_ADMINISTRATOR
              </value>
            </property>
        </bean>
        ```

        !!! note

            The final entry in the `flowVoter` bean, `*=ROLE_USER,ROLE_ADMINISTRATOR`, sets the default permissions for all flows not specified directly. If you don't create an entry for your flow, these permissions apply.

    **Example of creating an action and adding it to the flow**

6.  Create a java class that defines the controller in the Spring MVC framework. In this example, this file always returns `success` when invoked.

    1.  Go to the `<js-src>/jasperserver/jasperserver-war-jar/src/main/java/com/jaspersoft/ji/war/` directory. This is where the JasperReports Server source looks for java files used by the Spring web flow framework.

    2.  Create a subdirectory for your flow package, `<js-src>/jasperserver/jasperserver-war-jar/src/main/java/com/jaspersoft/ji/war/sampleFlow/`

    3.  Create a java file and save it as `<js-src>/jasperserver/jasperserver-war-jar/src/main/java/com/jaspersoft/ji/war/sampleFlow/SampleAction.java`

        ``` java
        package com.jaspersoft.ji.war.sampleFlow;

        import org.springframework.webflow.action.MultiAction;
        import org.springframework.webflow.execution.Event;
        import org.springframework.webflow.execution.RequestContext;

        public class SampleAction extends MultiAction {
            public Event start(RequestContext context) throws Exception{

                // implement some logic

                return success();
            }

        }
        ```

7.  Create a bean for the `SampleAction` class that you created. To this, create the following file and save it as `<js-src>/jasperserver/jasperserver-war/src/main/webapp/WEB-INF/flows/docSampleBeans.xml`:

    ``` xml
    <beans xmlns="http://www.springframework.org/schema/beans"
          xsi:schemaLocation="http://www.springframework.org/schema/beans
          http://www.springframework.org/schema/beans/spring-beans-3.1.xsd
          http://www.springframework.org/schema/util
          http://www.springframework.org/schema/util/spring-util-3.1.xsd">
     <bean id="sampleAction" class="com.jaspersoft.ji.war.sampleFlow.SampleAction">
     </bean>
    </beans>
    ```

8.  Modify `docSampleFlow.xml` to start with an action state that calls the `SampleAction` class you created:

    1.  Change the start-state to `start`.

    2.  Create an action state `start` that calls `sampleAction` and transitions to the view-state `sampleView` on success. Insert this state before `sampleView`.

    3.  At the end of the flow, import `docSampleBeans.xml` as a resource.

        ``` xml
        <?xml version="1.0" encoding="UTF-8"?>
        <flow xmlns="http://www.springframework.org/schema/webflow"
            xmlns:ns0="http://www.w3.org/2001/XMLSchema-instance"
            ns0:schemaLocation="http://www.springframework.org/schema/webflow
            http://www.springframework.org/schema/webflow/spring-webflow-2.0.xsd"
                start-state="start">

          <action-state id="start">
            <evaluate expression="sampleAction"/>
              <transition on="success" to="sampleView"/>
             </action-state>

        <view-state id="sampleView" view="modules/sampleFlow/sampleView">
        </view-state>

        <view-state id="errorPage" view="modules/system/errorPage"/>

        <end-state id="done"/>

        <global-transitions>
          <transition on="backFromErrorPage" to="backFromError"/>
          <transition on-exception="java.lang.Throwable" to="errorPage"/>
        </global-transitions>

        <!-- end exceptions handling -->

        <bean-import resource="docSampleBeans.xml"/>

        </flow>
        ```

9.  Add error handling as shown in the code sample above:

    1.  Add a view-state `errorPage` to your flow. In this example, you add it immediately after `sampleView`.
    2.  Add a global-transitions state that handles Java exceptions by displaying `errorPage`.

10. (Optional) If you want, you can rebuild the source code and view your page:

    -   Rebuild the source code and redeploy the web application according to the instructions in the Building JasperReports Server section in the JasperReports Server Source Build Guide within your distribution. See [Working With Source Code Files](customizing-java-classes.md) for an overview of this process.

    -   Log in to your JasperReports Server.

    -   Navigate to the page you created using this URL:

        `http://<hostname>:<port>/jasperserver-pro/flow.html?_flowId=docSampleFlow`

        Example:

        `http://localhost:8080/jasperserver-pro/flow.html?_flowId=docSampleFlow`

    **Example of creating a menu item to call your flow**

    Now you can add a menu item to call the flow you created. The process is similar to the one described in [Adding an Item to the Main Menu](adding-an-item-to-a-menu.md), but because you're modifying the source, the file locations are different in this example.

    !!! note

        Because the commercial source code includes the community source, most modifications to the menu are made in the community source files.

11. Edit the file `<js-src>/jasperserver/common/shared-config/actionModel-navigation.xml`. Locate the `actionModel` for the **View** menu in the file.

12. Add an `option` tag for the menu item, as shown in the following code sample. The `option` tag has attributes to specify the label key and the name of the action to perform.

    ``` html
    <!--context for view option on primary menu-->
    <context name="main_view_mutton" test="!banUserRole">
      <selectAction labelKey="menu.repository">
        ...
        <condition test="checkAuthenticationRoles" testArgs="ROLE_ADMINISTRATOR">
          <separator/>
          <option labelKey="menu.samples" clientTest="!isIPad"
            action="primaryNavModule.navigationOption" actionArgs="samples"/>
        </condition>

        <separator/>
        <condition test="checkAuthenticationRoles" testArgs="ROLE_ADMINISTRATOR"><option labelKey="NAV_028_DOC_SAMPLE" action="primaryNavModule.navigationOption"actionArgs="docSample"/></condition>
      </selectAction>
    </context>
    ```

13. Add a `condition` tag for the menu item, as shown in the code sample above.

    !!! note

        The condition tag prevents the menu item from being displayed to users without the specified permissions. However, to ensure the flow can't be accessed via URL, set flow permissions as shown in step 5.

14. Add the label key to the file `<js-src>/jasperserver-pro/jasperserver-war/src/main/webapp/WEB-INF/bundles/pro_nav_messages.properties`, as shown in the following code sample:

    ``` properties
    NAV_001_HOME=Home
    ...
    NAV_027_SEARCH=Search Results
    NAV_028_DOC_SAMPLE=Hello World
    NAV_031_USERS=Users
    ...
    ```

15. Create a working directory where you can edit and build JavaScript source code, as described in [1.0.1, “Customizing JavaScript Files,” on page 1](customizing-javascript.md).

16. In a text editor, open your working copy of the file `<js-src>/jasperserver/jasperserver-war/src/main/webapp/scripts/actionModel.primaryNavigation.js`, and locate the `navigationPaths` section. Add a line that specifies the accounts flow to begin when the menu item is selected. If you are adding your line at the end of the section, make sure to add a comma to the previous line.

    ``` javascript
    var primaryNavModule = {
    ...
       navigationPaths : {
         ...
         logSettings : {url : "log_settings.html"},
         docSample : {url : "flow.html", params : "_flowId=docSampleFlow"}
      },
    ```

17. Create a file "`sampleFlowMain.js`" at "`jasperserver-ui/ce/jrs-ui/src/sampleFlow/sampleFlowMain.js`", as shown in the following code sample:

    ``` text
    import '../util/webpackPublicPathSetup';
    const importStartup = import('../util/mainPagesStartup')
    const importCommonModule = () => import('../commons/commons.main')

    importStartup.then(({default: startup}) => startup({
    importCommonModule
    }))
    ```

18. Add the following file entry to "`jasperserver-ui/ce/jrs-ui/webpack.config.js`"

    ``` text
    'system/systemErrorMain': "./src/system/systemErrorMain",
    'system/errorMain': "./src/system/errorMain",
    *'sampleFlow/sampleFlowMain': './src/sampleFlow/sampleFlowMain'*
    ```

19. (For JasperReports Server Professional edition only) Create a file "`sampleFlowMain.js`" at "`jasperserver-ui/pro/jrs-ui-pro/src/sampleFlow/sampleFlowMain.js`", as shown in the following code sample:

    ``` text
    import 'jrs-ui/src/util/webpackPublicPathSetup';
    const importStartup = import('jrs-ui/src/util/mainPagesStartup')
    const importCommonModule = () => import('../commons/commons.main')

    importStartup.then(({default: startup}) => startup({
    importCommonModule
    }))
    ```

    Then update the JSP file mentioned in step 2 to:

    ``` html
    <html>
    <head><title>Sample Page</title>
    <script type="text/javascript" src="${pageContext.request.contextPath}/runtime/${jsOptimizationProperties.runtimeHash}/JavaScriptServlet"></script>
         <script src="${pageContext.request.contextPath}/runtime/${jsOptimizationProperties.runtimeHash}/scripts/sampleFlow/sampleFlowMain.js" defer></script>

    </head>
    <body class="oneColumn primary column">
    <h1 class="textAccent">Hello World!</h1>
    </body>
    </html>
    ```

    **Compile code and view changes**

20. Build the JavaScript source code in your working directory and copy the output back to JasperReports Server as described in [1.0.1, “Customizing JavaScript Files,” on page 1](customizing-javascript.md).

21. Rebuild the source code and redeploy the web application according to the instructions in the JasperReports Server Source Build Guide within your distribution. See [Working With Source Code Files](customizing-java-classes.md) for an overview of this process.

22. Log in as an administrator. If your changes were successful, this example displays the ****View &gt; MyCompany Accounts**** menu item to users, and selecting it displays the custom page defined in the `sampleView.jsp` file:

23. The page uses the single column layout and the orange text is the `textAccent` class in CSS.
