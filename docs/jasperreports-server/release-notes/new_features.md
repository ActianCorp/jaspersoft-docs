---
title: New Features
description: This section describes new features introduced in the Jaspersoft BI Suite Version 10.1 release.
---

# New Features

This section describes new features introduced in the Jaspersoft BI Suite Version 10.1 release.

To view the Release Notes of version 9.0.0, see [JasperReports® Server Release Notes v9.0.0](https://community.jaspersoft.com/documentation/jasperreports-server/tibco-jasperreports-server-release-notes/v900/relnotesbody-_-overview/).

To view the new features added to the various products of Jaspersoft BI Suite, refer to the following list:

- JasperReports® Server10.1.0
- Jaspersoft® Studio 10.1.0
- JasperReports® Web Studio 10.1.0

## JasperReports® Server 10.1.0

For JasperReports® Server 10.1.0, the following improvements have been added:

- **Jakarta Upgrade**

  The Jakarta upgrade represents a significant stride towards modernizing our platform and ensuring its compatibility with evolving technologies. By enabling JasperReports® Server to run on Apache Tomcat 10.1.24 onwards, we are embracing the latest advancements in the Jakarta EE 10 specifications. This transition involves:

  - Updating the codebase to align with the new Jakarta namespace, guaranteeing a seamless and future-proof experience for our users.

  - Upgrading the Spring and Commons DBCP libraries to ensure compatibility with the evolving Java enterprise ecosystem to be used effectively in Jakarta EE environments.

  - moving from ehcache2 to JCache API implementation. Currently, Infinispan is the only verified JCache implementation.

- **Hibernate Upgrade**

  The application now leverages Hibernate version 6. This involved replacing the older, XML-based (.hbm.xml) object-relational mappings with modern JPA annotation-based @Entity classes.

- **Enhanced Tooltip for Fields and Measures**

  Gain valuable insights at a glance with our enhanced tooltip. It now provides comprehensive field information, including **Field Path, Original Name, Formula, Description, Data Type, Field Type**, and **Default Summary Function**. The details are available for all available fields/measures, selected fields/measures, and fields/measures used in filters, empowering you to make informed decisions and optimize your reports.

  For more information, see JasperReports® Server User Guide.

- **Ad Hoc UX Panel (Layout Band)**

  The Layout Band has been completely redesigned to provide a more intuitive and user-friendly experience when creating visualizations. It now dynamically adapts to each visualization type, presenting specific areas for fields and measures that directly correspond to how the visualization is constructed. This update improves the user experience and simplifies the visualization building process.

  Informative tooltips are added to guide you on where to drag and drop fields and measures to achieve the perfect layout for your visualizations.

  For more information, see JasperReports® Server User Guide.

- **Print Functionality**

  Now you can easily print your reports, dashboards, and Ad Hoc designs with a single click. Our new print function, integrated directly into the toolbars, instantly generates a PDF and opens your system's **Print** dialogue. For dashboards, you have even more control with configurable visibility for the print button (both for the entire dashboard and individual dashlets), offering "screenshot" or "detailed" print options to perfectly capture your data.

  For more information, see JasperReports® Server User Guide.

- **Visual indicator of filters/dashlets**

  Unlock deeper insights with enhanced dashboard interactivity. Our latest update visually clarifies data relationships, highlighting affected dashlets when you select a filter. Gain a more intuitive understanding of your data at a glance.

  For more information, see JasperReports® Server User Guide.

- **Editing external Ad Hoc view from Dashboard**

  Unlock seamless, in-dashboard editing. This powerful enhancement lets you modify existing Ad Hoc views directly from within your dashboard. Simply enter edit mode, right-click any dashlet, and select **Edit** to instantly access and fine-tune the underlying data view. Save your changes, close the view, and watch your dashboard update dynamically—all without leaving your workflow.

  For more information, see JasperReports® Server User Guide.

- **Disabling Alert**

  Take complete control of the **Alert** feature visibility. Easily disable system alerts by setting the `isAlertEnabled` flag to `false` ( `true` by default) and simply restart the server.

  For more information, see JasperReports® Server User Guide.

- **Accessibility Changes**

  With the accessibility changes, the usability and precision for users is enhanced. There are improvements in some areas of the Ad Hoc designer and the Input Controls dialog providing smoother navigation, clearer interface and wider compatibility.

- **New License Manager**

  A new in-house license manager/validator is added in JasperReports® Server 10.1.0. The name of the license file is now changed to `jaspersoft.jrs.license`, while the application's functionality remains the same regardless of the license. Correct permissions must be set on this new file.

  For more information, see JasperReports® Server Installation Guide.

- **Telemetry**

  We have significantly upgraded our telemetry and license management to improve compliance and deliver greater customer value. This expanded data collection provides increased visibility into usage patterns, enabling our teams to generate actionable insights for product and sales development. Key focuses include compliance monitoring (tracking user counts and feature limits to prevent violations) and onboarding improvement (tracking initial user actions to reduce drop-off). This new mechanism efficiently aggregates all crucial data, providing a single, comprehensive view of each customer's deployments in the Diagnostic Report.

  For more information, see JasperReports® Server Administrator Guide.

- **HTML Pro Component**

  With the new HTML Pro component, you can embed the HTML content (including layout, tables, and images) into JasperReports. While the support for basic HTML formatting using HTML as the markup language for text fields is already available, it is limited and does not support images, tables, and custom CSS-based formatting. The HTML PRO component leverages the Microsoft Playwright library version 1.50.0 to provide enhanced HTML report generation capabilities.

  For more information, see the JasperReports® Server User Guide.

- **Sending Emails Using SendGrid API**

  You can configure the scheduler to utilize SendGrid API for sending and receiving emails.

  For more information, see JasperReports® Server Administrator Guide and JasperReports® Server Installation Guide.

- **Custom Input Controls**

  Custom Input Controls for JasperReports Server empower you to transform your reports and dashboards from generic displays into highly intuitive, sophisticated interfaces. You now have the flexibility to use custom expressions to **Enable/Disable** and **Show/Hide** Input Control. You can also update the Input Control title using custom expressions. This precision gives every user the exact controls they need, resulting in smarter, faster filtering and a truly intuitive experience for complex data analysis.

  For more information, see JasperReports® Server User Guide and JasperReports® Server Administrator Guide.

- **Show or Hide Columns in Interactive Tables**

  JIVE action of show/hide columns in report viewer is now enhanced to provide more control over which columns to display. You can now show or hide single/multiple columns.

  For more information, see JasperReports® Server Administrator Guide.

## Jaspersoft® Studio 10.1.0

For Jaspersoft® Studio 10.1.0, the following improvements have been added:

- **Eclipse 4.36 and Java 21 Upgrade**

  The Eclipse 4.36 and Java 21 upgrade is a significant modernization of the core platform used to build and run Jaspersoft® Studio. With this upgrade, Jaspersoft® Studio runs on a more modern, stable, and feature-rich foundation, ensuring better compatibility and a more responsive user interface. The Eclipse 4.36 platform requires a more recent version of the Java runtime to function correctly, forcing the minimum Java version requirement to move up. Moving the minimum requirement to Java 21 is a substantial jump, as Java 21 is one of the latest versions.

  This combined upgrade represents a major technological shift aimed at modernizing the application's core. It replaces older software dependencies with modern, performance-optimized, and more secure components (Eclipse 4.36 and Java 21), ensuring the platform remains current and viable for future development.

- **HTML Pro Component**

The new HTML Pro component is exclusively available for Jaspersoft® Studio Professional users. The HTML Pro component allows the embedding of HTML content (including layout, tables, and images) into JasperReports. While the support for basic HTML formatting using HTML as the markup language for text fields is already available, it is limited and does not support images, tables, and custom CSS-based formatting. The HTML PRO component leverages the Microsoft Playwright library version 1.50.0 to provide enhanced HTML report generation capabilities.

For more information, see the Jaspersoft® Studio User Guide.

- **New License Manager**

A new in-house license manager/validator is added in Jaspersoft Studio 10.1.0. The name of the license file is now changed to `jaspersoft.jss.license`, while the application's functionality remains the same regardless of the license.

For more information, see the Jaspersoft® Studio User Guide.

- **New JRXML 7 Model**

With the introduction of the new JRXML 7 model, a warning message will now appear when publishing reports to JasperReports® Server. You can modify the compatibility settings, such as the JasperReports® Library version, as needed.

For more information, see the Jaspersoft® Studio User Guide.

- **Alternative Login Method**

A secondary, smartphone-based activation method to Jaspersoft® Studio Community is offered to improve the activation experience for users with limited or no internet connectivity. In case of network limitations, Jaspersoft® Studio generates a QR code containing encrypted installation details. Users can scan this code with their smart phones, log in to the Jaspersoft® community, and receive a unique activation code. Entering this code into Jaspersoft® Studio completes the registration process. This enables offline usage and allows installation tracking.

## JasperReports® Web Studio 10.1.0

For JasperReports® Web Studio 10.1.0, the following improvements have been added:

- **Wizard for Table Creation**

  Instantly build powerful, data-rich reports with the Table Wizard. This essential tool is designed to drastically streamline table creation, transforming complex setup into a smooth, step-by-step process. The Wizard guides you through everything—from selecting or defining your datasets to configuring data adapters—ensuring a fast, efficient workflow so you can publish your reports sooner.

- **Crosstab Wizard**

  The enhanced crosstab creation feature is designed to give you a clearer, more intuitive understanding of complex data relationships. We have completely streamlined the process: the new Crosstab Wizard makes adding sophisticated crosstabs to your reports easier than ever, guiding you effortlessly to better data insights.

- **Report Wizard**

  Generate powerful reports effortlessly with our intuitive Report Wizard. We have taken the complexity out of report creation by guiding you through a clear, step-by-step process. Simply follow the wizard to select your data adapter, define your query, choose fields, and apply precise grouping and sorting. It’s the easiest way to ensure a seamless workflow and instantly create the reports you need.

- **Refactor Home page**

  The application's default login page allows users to connect to various repositories like JasperReports Server, Google Drive, and GitHub via the upper-right menu. Users can switch between these repositories and set a default login page from server settings.

- **Effortless Table Editing**

  Take full control of your tables by effortlessly adding, deleting, or reordering columns. Populate your table with data and use the intuitive contextual menu or mini toolbar to seamlessly perform any action. With the enhanced table editor, you can effortlessly add or delete sections, such as table headers, and merge or split cells to achieve your desired layout.

- **Intuitive Contextual Menu**

  Streamline your workflow with the convenient contextual menu. Select elements from the Outline and effortlessly align or resize them within the Designing Area. Simply right-click the element and choose from the context-sensitive menu options to achieve precise positioning and sizing.

- **Enhanced Design Experience**

  Experience a new level of report design with our improved layout designer.

  - **Snap to Geometry**: Achieve pixel-perfect alignment of elements within the Designing Area. Select one or more elements and effortlessly move, resize, or align them together.

  - **Image Preview**: Add images to your design and instantly preview them. Easily edit and adjust display settings to achieve the perfect visual impact.

  - **Inline Text Element Editing**: Edit text elements directly within the design canvas. Double-click any text field or static text element to conveniently modify the expression or text. Personalize element properties such as color and font with ease.

  - **Column Support**: Create tables with multiple columns effortlessly. Specify the desired number of columns in the Properties view to evenly divide the Designing Area.

  - **Expression Editor**: Simplify expression editing by double-clicking the field to replace the text with the corresponding field expression.
