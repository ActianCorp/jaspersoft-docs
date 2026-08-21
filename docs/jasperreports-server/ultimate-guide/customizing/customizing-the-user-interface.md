---
title: Customizing the User Interface
description: "JasperReports Server is highly customizable because it's built on the Spring Framework and uses web standards such as Cascading Style Sheets (CSS) and JavaServer Pages (JSP). When the server is..."
---

# Customizing the User Interface

JasperReports Server is highly customizable because it's built on the Spring Framework and uses web standards such as Cascading Style Sheets (CSS) and JavaServer Pages (JSP). When the server is embedded in a web application or portal, its user interface (UI) can be customized to extend functionality and better reflect the parent application.

As with any large web application, the logic to generate the JasperReports Server UI is complex and relies on several mechanisms, listed here from simplest to most complex.

- Themes: The themes expose the CSS of the UI through the repository. This makes it easy for administrators change to the appearance of the UI, such as images, colors, font size, spacing, and even the general layout. Themes are described in detail in the JasperReports Server Administrator Guide. Refer to that document first.
- SiteMesh: The SiteMesh decorator creates the header and footer for every page of the server. Decorators provide a quick way to edit the overall appearance of the web app, such as branding and copyright.
- Java Server Pages (JSP) and JavaScript: These are the templates and logic, respectively, that generate the pages of JasperReports Server. Edit these files to change the content of individual pages or the way a page is generated. This chapter assumes you're familiar with JSP and JavaScript syntax.
- Action Model: This provides a simple way to edit any menu in JasperReports Server. The simple XML syntax lets you remove default menu items, restrict their visibility based on roles, and add new menu items if you have implemented an action.
- Spring MVC (Model, View, and Controller) and Spring Web Flow are frameworks for creating states and transitions that represent a business process in a web application. By creating custom flows, you can add your own sequence of pages that integrate with the server.

You can modify themes in a running server and changes will be seen immediately by all users. For all other types of customization, you need to edit the files deployed in the web app. If you're modifying files in the web application, you then need to redeploy the web app in the app server. In some cases, you need to modify source code, in which case you must re-compile the source code and redeploy the web app in the app server.

This chapter includes the following sections:

- [Changing the UI With Themes](customizing-ui-with-themes.md)

- [Customizing the UI With Web App Files](customizing-ui-with-web-app-files.md)

- [Customizing the Branding with SiteMesh](customizing-ui-with-sitemesh.md)

- [Customizing JSP and JavaScript for the Login Page](customizing-login-page.md)

- [Setting the Home Page](setting-home-page-flow.md)

- [Adding View List Buttons to the Getting Started Page](configuring_homepage_workboxes.md)

- [Restricting Access to a Location in the Repository](restricting-access.md)

- [Customizing JasperReports Wizard Repository Trees](repository-lazy-loading.md)

- [Customizing Menus](customizing-menus.md)

- [Customizing the Report Rendering Page](customizing-report-viewer.md)

- [Working With Custom Java Classes](customizing-java-classes.md)

- [Adding a Custom JSP Page in a Spring Web Flow](adding-a-jsp-page-to-a-spring-webflow.md)

- [Customizing the Scheduler Pages](customizing-scheduler.md)

- [Upgrading With UI Customizations](ui-customizations-and-upgrade.md)
