---
title: Removing a Menu Item
description: "In this example, suppose neither users nor administrators have been trained to work with Domains, and to prevent users from accidentally creating Domain resources, system administrators decide to..."
---

# Removing a Menu Item

In this example, suppose neither users nor administrators have been trained to work with Domains, and to prevent users from accidentally creating Domain resources, system administrators decide to remove any reference to Domains in the UI.

!!! note

    Removing Domains from the menu hides Domains but does not disable them. Users can still access Domains by entering the URI of the Domain webflow. See [Working With Source Code Files](customizing-java-classes.md) for information on how to restrict a webflow.

To remove the Domain menu items

1.  Edit the file `<js-webapp>/WEB-INF/actionModel-navigation.xml`. This file defines the main menu visible by default on all pages of the server. The XML that defines the actionModel, contains many condition tests that determine when each menu and menu item should be displayed.

    ``` text
    ...
    <context name="main_create_mutton" test="isProVersion">
      <condition test="!banUserRole">
        <condition test="!isMainFeaturesDisabled">
          <selectAction labelKey="NAV_005_CREATE">
            <condition test="isAvailableProFeature" testArgs="AHD">
              <option labelKey="NAV_051_ADHOC_REPORT"
                      action="primaryNavModule.navigationOption"
                      actionArgs="designer"/>
            </condition>
            <condition test="isAvailableProFeature" testArgs="DB">
              <option labelKey="NAV_050_DASHBOARD"
                      action="primaryNavModule.navigationOption"
                      actionArgs="dashboard"/>
            </condition>
    <!--
            <condition test="isAvailableProFeature" testArgs="AHD">
              <condition test="checkAuthenticationRoles" testArgs="ROLE_ADMINISTRATOR">
                <option labelKey="NAV_056_DOMAIN"
                        action="primaryNavModule.navigationOption"
                        actionArgs="domain"/>
              </condition>
            </condition>
    -->
          </selectAction>
        </condition>
      </condition>
    </context>
    ```

    !!! note

        “Mutton” is a term that means menu-button, and designates a button that creates a drop-down menu.

2.  Find the section at the end for the **Create** menu and insert comments to remove the last menu item, as shown in the code sample above.

3.  Edit the file `<js-webapp>/WEB-INF/actionModel-search.xml`. This file defines the context menu items visible when users right-click folders and resources in repository listings.

    ``` xml
    <?xml version="1.0" encoding="UTF-8"?>
    <actions>
    <context name="folder_mutton">
      <simpleAction labelKey="SEARCH_CREATE_FOLDER" action="invokeFolderAction"
                    actionArgs="CreateFolder" clientTest="canCreateFolder"
                    className="up"/>
      <condition test="checkAuthenticationRoles"
                 testArgs="ROLE_USER,ROLE_ADMINISTRATOR">
        <selectAction labelKey="SEARCH_CREATE_RESOURCE"
                      clientTest="canResourceBeCreated" className="flyout">
          <condition test="checkAuthenticationRoles" testArgs="ROLE_ADMINISTRATOR">
          <option labelKey="RM_NEW_RESOURCE_DATA_SOURCE" action="invokeCreate"
                  actionArgs="ReportDataSource" clientTest="canResourceBeCreated"
                  clientTestArgs="ReportDataSource" className="up"/>
          <option labelKey="RM_NEW_RESOURCE_DATATYPE" action="invokeCreate"
                  actionArgs="DataType" clientTest="canResourceBeCreated"
                  clientTestArgs="DataType" className="up"/>
    <!--
          <condition test="isProVersion">
            <option labelKey="RM_NEW_DOMAIN" action="invokeCreate"
                    actionArgs="SemanticLayerDataSource"
                    clientTest="canResourceBeCreated"
                    clientTestArgs="SemanticLayerDataSource" className="up"/>
          </condition>
    -->
    ```

4.  Find the section at the top of the file that creates the Add Resources sub-menu. Then add comments to remove the lines that define the ****Add Resources &gt; Domain**** menu item, as shown in the code sample above.

5.  Save the modified files and reload the web app in the app server to see the changes (see [1.0.1, “Reloading the JasperReports Server Web App,” on page 1](reloading-jrs-webapp.md)).

6.  When the web app has reloaded, log into JasperReports Server as jasperadmin. Click the **Create** menu and right-click a folder in the repository. In both cases, the menu item for Domain is no longer available.

!!! note

    When you remove a menu item, it is removed for all users, even administrators. It's often preferable to prevent only non-administrators from viewing a menu item, as shown in the next section.
