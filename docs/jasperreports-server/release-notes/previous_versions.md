---
title: Changes In Previous Versions
description: "This section describes new features introduced in the Jaspersoft BI Suite Version 7.1.0 to 7.8.0 releases. For information regarding features added to Version 6 releases, see the latest 6.4.x release..."
---

# Changes In Previous Versions

This section describes new features introduced in the Jaspersoft BI Suite Version 7.1.0 to 7.8.0 releases. For information regarding features added to Version 6 releases, see the latest 6.4.x release notes.

## Version 7.8.0

JasperReports Server 7.8.0 adds these improvements

-   Updated user interface. This release includes new visual changes on several pages:

    -   The Search Results page has new expand and collapse controls for the filters column on the left.
    -   The Repository page, Library page, Schedules page, Schedules editor, and Management pages have a new look.
    -   Ad Hoc Editor has usability improvements, including the ability to drag measurements and fields directly to the canvas to start building your visualization.
    -   The Visualization Selector now has a new panel describing the selected visualization, including the requirements, and a new Apply and Close button.
    -   The Dashboard Designer has usability improvements, including a new toolbar button to switch between editing and viewing a dashboard. The Designer now opens an embedded Ad Hoc Editor when creating and editing charts, crosstabs, and tables.

-   Cryptography improvements. Import and export operations now allow the administrator to specify the encryption key. When importing through the server UI, a list of possible keys is displayed.

-   New Chromium JavaScript engine. JasperReports Server Version 7.8 uses the Chromium JavaScript engine to generate graphical reports. The binary installer for JasperReports Server will display a message asking if you want to use the engine and then prompt you to enter the path to Chrome or Chromium on your machine. If you want to use Microsoft Edge as your main web browser, you will need to install JasperReports Server using the stand-alone WAR file distribution. For instructions on installing the Chromium JavaScript engine, see the JasperReports Server Installation Guide.

-   Chromium replacing PhantomJS. JasperReports Server Version 7.8 replaces PhantomJS with the Chromium JavaScript engine to generate graphical reports that are run in the background or scheduled. You can use Chrome, Chromium, or any other browser based on Chromium like Microsoft Edge. For information on the compatible versions of browsers, see the TIBCO Jaspersoft Platform Support Guide.

-   Visualize.js updates. Dashboard export support has been added to Visualize.js. Supported formats include .PDF, .PNG, .DOCX, .PPTX, and .ODT. Plus, client-server communication has been migrated from using EasyXDM library to cross-origin resource sharing.

-   New TIBCO JasperReports® Server Data Management Using Domains Guide. A new guide on working with domains in JasperReports Server. The guide includes instructions for using the Domain Designer, localizing domains, securing your data, and more.

-   New Domain Designer Security tab. The Domain Designer has a new Security tab where you enter and view rules that restrict access to the data in a Domain, based on a user's roles and attributes. Rules are stored in an XML file that works together with the Domain's XML design file to identify what data you want to expose to each user.

-   Input controls client-server pagination implemented for Report Viewer, Report Options, and Scheduler. This functional change improves performance when running reports with big number of values in single-select and multi-select input controls.

-   New platforms. This release adds support for several new third-party platforms:

    -   Operating systems:

        -   Red Hat Enterprise Linux 7.8, 8.0
        -   MacOS 10.15

    -   Application servers:

        -   Tomcat 8.5.54, 8.5.57, 9.0.34, 9.0.37
        -   Wildfly 18, 19
        -   WebSphere 9.0.0.11, 9.0.5.1

    -   Database servers:

        -   DB2 11.5
        -   MySQL 8.0
        -   SQL Server 2019

    -   JDBC connectors:

        -   Elasticsearch

        -   Google BigQuery

        -   Neo4j

        -   TIBCO Data Virtualization

        -   MongoDB 4.2.6 Schemafilter option

        -   Cassandra 3.10, 3.11

            Jaspersoft Studio 7.8.0 adds these improvements

-   New jasperQL query language. Jaspersoft Studio supports a new query language that provides more options to aggregate and sort data in Domain-based reports (JasperReports Server Professional Edition only). For example, with jasperQL you can use `Order By`, `Group By`, and `Limit` in your queries. The domain query language is still supported.

-   **JasperReports Library 6.14.0 support**. Jaspersoft Studio now provides full support for JasperReports Library 6.14.0.

-   **Updated Drivers**. The following drivers are updated:

    -   Progress DB2 driver updated from version 5.14 to 5.1.4.000288
    -   Progress Salesforce driver updated from version 5.14 to 6.0.0.000724
    -   Progress MSSQL Server driver updated from version 5.1.4.000242 to 6.0.0.000249
    -   Progress Spark driver updated from version 6.0.2 to 6.0.1.000081
    -   Progress MongoDB driver updated from version 6.0.2.404 to 6.0.2.000510

-   **New Drivers**. The following drivers are added:

    -   Progress Google BigQuery driver version 6.0.0.000279
    -   Simba Google BigQuery driver version 1.0.5.1006
    -   Elasticsearch driver version 7.6.0
    -   TIBCO Data Virtualization driver version 8.2.0

-   **Updated Bouncycastle bundle**. Updated to version 1.64.0.jdk15on

    JasperReports Library 7.8.0 adds these improvements

-   Introduced a secure report execution infrastructure that allows filtering of classes used in expressions. The allowed classes are specified in a configurable whitelist.

-   Improvements in expression bytecode generation and expression evaluation. Simple expressions containing only parameter, field, or variable references are evaluated directly.

-   New built-in function ORIGINAL_DATA_SOURCE gives access the original data source when the data is sorted using sort field declarations in the dataset.

-   New built-in function SUB_DATA_SOURCE creates a JSON or XML sub data source when the data is sorted using sort field declarations in the dataset.

-   Added functionality to automatically increase the frame element width if its contents stretch horizontally.

-   Added support for dynamic bookmark levels based on expressions.

-   Added support for PDF forms to the core library. Custom properties at the report element level convert report elements into editable text fields, lists, check boxes, or radio buttons when the report is exported to PDF.

-   The JasperReports Web Framework providing the embeddable report viewer APIs has been removed from the JasperReports Library as it is now available as part of other products such as JasperReports Server, Jaspersoft Studio, and JasperReports IO. All Javascript, CSS, HTML templates, images files, and servlets that make up this framework have been removed from the core library JAR. The related /demo/samples/webapp-repo sample has been removed from the project distribution. The former /demo/samples/webapp sample continues to provide an example for using the JasperReports Library in Java web applications, for delivering static/non-interactive reports in all supported export formats.

-   Fixed an issue with the virtualization of large unpaginated reports containing large frame elements.

-   Improved justified alignment for paragraphs that are cut through by page or column breaks.

-   Added support for Java Generics in the class attribute of parameters, fields, and variables.

## Version 7.5.0

JasperReports Server 7.5.0 adds these improvements:

-   Updated user interface. This release includes a new look and feel that is crisp and easy to navigate. It keeps the familiar layout and provides updated icons, styling, and colors throughout the application:

    -   The home page has a simpler layout with all BI tools in a single column and introduces a color-coding of features that is consistent throughout the application. For example, the green icon for finding reports on the home page matches the green icon for adding a report in the Dashboard Designer.
    -   The pages for creating data sources have been streamlined and color-coded.
    -   The Domain Designer has new icons for tables, fields, joins, sets, and others throughout.
    -   The Report Viewer, Ad Hoc Designer, and Dashboard Designer are all updated with new icons, color-coding, and matching styles so that viewing data is clearer and creating visualizations is simpler.

-   Three new visualizations. The new gauge types are the circular gauge, the multi-level gauge, and the arc gauge. These gauges have formatting properties to set minimum and maximum values, colors for value ranges, whether the value is displayed, and if so the number of decimal places and a suffix string such as the % sign.

-   Ad Hoc visualization selector. This UI element has been updated to choose or switch between visualizations more easily. The visualization selector now lets you choose crosstab or table, and the chart selection includes a sidebar for chart categories. In addition, the visualization mode toolbar drop-list is replaced with a visualization selector button.

-   New color picker dialog. The Ad Hoc Designer and Dashboard Designer have a new color picker interface for specifying colors to match any palette where visualizations are embedded. The default color selections are expanded, and custom colors may be specified precisely with HEX or RGB entry options.

-   Colors in Ad Hoc charts. There are several new features in the Ad Hoc Designer that allow greater customization of chart colors. New UI properties allow the user to set the series color, the plot color, and the background color in charts that allow it.

-   Distinct values in Ad Hoc tables. Tables often contain columns that have duplicate values in many rows, making it difficult to find relevant data. The new distinct values selector in the Ad Hoc Designer hides the duplicate rows and makes tables shorter and easier to read. Note that tables with a totals row will not recalculate the total values when duplicate rows are hidden.

-   Referential Integrity for Domains. New configuration settings let you adjust how strictly Ad Hoc views and reports are checked against their underlying Domain. By default, fields and measures in a view or report that do not exist in the Domain will cause an error upon opening. Administrators can adjust the level of referential integrity to allow opening views and reports when Domain security causes missing items.

-   Security. This release of JasperReports Server updates its use of cryptographic keys, for example to encrypt user passwords internally. All keys are now generated and managed in a single keystore for consistency. Keys used for encrypting export catalogs from older versions of the server have new procedures and user interface for importing into this version of the server. For more details, see the JasperReports Server Security Guide.

-   Update to Log4j 2. The logging service now relies on the updated Apache Log4j 2. This upgrade provides higher performance of the loggers and thus less overhead for JasperReports Server. If you have custom loggers, you will need to update their definitions using the new syntax.

-   Java 11. JasperReports Server runs with Java 8 and Java 11 for certain platforms, see the Platform Support document for more details.

## Version 7.2

JasperReports Server 7.2 added these features:

-   New Domain Designer. We improved and rebuilt the Domain designer's presentation and functionality with:

    -   All New User Experience. Our modern web UI with streamlined workflows helps you quickly define and manage Domains, including these helpful usability features:

        -   Support for searching across the Domain designer helps you manage large Domains efficiently.
        -   **Undo**, **Redo**, and **Undo All** buttons.
        -   One single **Save** button (**Save and Submit** is removed).
        -   Context-based designer space.
        -   Support for profile attributes as schema names, derived tables, calculated fields, and pre-filters.

    -   Improved Special Character Handling. We added support for many characters in schema, table, and field names.

    -   Improved Joins Support. New features and UI improvements include:

        -   New drag and drop interaction helps you create join trees and expressions; you can view the overall logical data model and expand into each join tree.
        -   The abilities to rename join trees, use more join operators, and create constant joins.
        -   Support for advanced joins that use either a Full or Minimum join path. With Minimum paths, you can assign join weights and force tables to always be included in your overall join expression.

    -   Redesigned Presentation including:

        -   A single element can now be part of multiple sets (your no longer need to duplicate fields).
        -   Sets and items belonging to a single join tree are neatly organized under data islands, providing a clear view of their relationships.
        -   Improved presentation shows the properties of sets and items directly on the **Presentation** tab.
        -   Inline editing of properties without the need to click an **Edit** button.
        -   Similar items and their properties can be compared using search.

    -   Validation and performance improvements, including:

        -   The new model checks the validity of the Domain with every action, and provides real-time feedback in the form of useful icons, helping you maintain the Domain's validity and save without losing changes.
        -   Better interface components, paginated loading, and refined client-side rendering all improve the performance of Domains; the new designer handles thousands of tables.

-   New platforms. This release adds several new third-party platforms:

    -   Application servers:

        -   Tomcat versions 9.0.1 through 9.0.17
        -   WildFly 13, 14, 15, and 16
        -   JBoss EAP 7.1
        -   Oracle WebLogic 12.2.1.3
        -   IBM WebSphere 8.5.5.14

    -   Database Servers:

        -   PostgreSQL 10.5
        -   Microsoft SQL Server 2017
        -   Oracle Database 12c Release 2 12.2.0.1

-   **Legacy Dashboards End of Life**. With this release, legacy dashboards are no longer available to view or edit. These older objects are no longer supported. Legacy Dashboards refers to those developed with the JasperReports Server dashboard designer in versions earlier than 6. These dashboards utilized older architecture that we deprecated. If your installation still includes dashboards in the legacy dashboard format, please recreate them in the new Dashboard designer before migrating to this release.

-   Accessibility Support. To help visually impaired users, we improved keyboard and screen-reader support in the report viewer. You can now navigate the main report viewer menu structure using the keyboard and hear interface descriptions using JAWS-enabled screen readers.

-   JasperReports Library. This new version provides dynamic control of page numbers.

-   Jaspersoft Studio 7.3. This new version supports Spotfire 7.11 and higher.

This release also includes enhancements and fixes requested by our customers. For more information, see [Closed Issues](closed_issues.md).

!!! note

    The configuration of the `ResourceForwardingServlet` servlet has changed since Release 6. For more information, refer to the New Configuration in [Version 7.1.0](#version-710), below.

## Version 7.1.1

Version 7.1.1 was a maintenance release that included improvements requested by customers. For information about the status of specific cases, please visit [TIBCO Jaspersoft Technical Support](https://support.tibco.com/) (http://support.tibco.com). In addition, we updated the version of Tomcat: Apache Tomcat 8.5.34.

## Version 7.1.0

JasperReports Server 7.1.0 added these improvements:

-   Visualize.js Ad Hoc View Support. Visualize.js provides new building blocks to embed Ad Hoc views, helping application developers build modern, immersive experiences. This release includes:

    -   A frozen heading pane and infinite scrolling for table and crosstab components; this can greatly improve performance when viewing large result sets.

    -   CSS inheritance can define crosstab and table styling.

    -   The ability to capture attributes about table, crosstab, and chart components for use in hyperlinks.

    -   Object properties that help developers build their own user interfaces for selecting visualization types.

    -   Parameter and parameter value calls that enable dynamic view updates and custom filter controls in the surrounding application.

        !!! note

            OLAP Data Sources are not supported by Ad Hoc views in Visualize.js.

-   Ad Hoc Views. Ad Hoc views and reports now offer:

    -   Ad Hoc View Referential Integrity. When items from a Domain are used in a dependent Ad Hoc view, removing the items from the Domain now returns an error message when editing the Ad Hoc view. You're given the option to remove the missing items from the Ad Hoc view to continue using it. The removed items no longer appear in the Data Source Selection panel.

    -   Time Balance Calculations. The ability to define basic Time Balance properties on measures, providing greater control of time series aggregate data.

        By default, all data are aggregated by summing time series values. New options let you calculate aggregate time values by taking the first or last values of a time series. This benefits cases where opening and ending balance values (such as Inventory and Cash Balances) are measured. These options can change the totals to the sum of the numeric data for a period of time, as well as an average of the numeric values, the first numeric value entered for the period, and the last numeric value entered for the period.

    -   Grouping by Day of the Week. There is a new option for grouping time series data by Day of Week.

-   Jaspersoft Studio. Several new features are available in our report designer:

    -   Spotfire (Version 7.5+) Infolink support. The data adapter for connecting to a Spotfire instance uses the latest public Spotfire API. Report developers can create content from Spotfire data.

    -   Support for properties in datasets and query executers. Better support for fields and parameters in the Dataset and Query dialog, including support for field properties on the **Fields** tab and show and hide built-in parameters, and the ability to display, create, and edit parameter properties on the Parameters tab. This lets you configure your fields and parameters directly in the Dataset and Query dialog.

    -   Data adapters that connect to a web service. You can now create data adapters that connect to a web service. You configure these data adapters in the data adapter dialog. When you use this type of data adapter in a report, you can access it in the Dataset and Query dialog: you can auto-discover fields from a node you enter in the query dialogs and view and manage HTTP parameters on the Data Adapter tab.

    -   Enhanced Properties UI. The advanced properties dialog now displays a searchable list of available properties. You can create expressions, toggle the view to the old Properties dialog, and add properties for your custom classes. Most elements now support expressions in properties.

    -   Support for Data Snapshots. Jaspersoft Studio now lets you create a JasperReports data snapshot, which contains a sample dataset that contains all sample data necessary to run the report. Storing the data for a report makes it easier to develop reports while offline or to share a functional report with other developers.

        You can still create reports and connect to the latest JasperReports Server with previous versions of Jaspersoft Studio.

-   New Platforms. Components included in the installer have been updated to:

    -   PostgreSQL 9.3.20
    -   Tomcat 8.5.34
    -   Oracle JDK 8 version 1.8.0_201 (8u201)
    -   Spring Framework 3.2.18

-   New Third-party Software Support. This release adds support for Oracle 12c as a host for the JasperReports Server repository and WebLogic 12.2.1 as the application server.

-   Security Improvement. JasperReports Server implements a new mechanism to protect against clickjacking attacks. To enable this mechanism, edit a configuration file.

    <table>
    <colgroup>
    <col style="width: 100%" />
    </colgroup>
    <tbody>
    <tr>
    <td><ol>
    <li>Using a text editor, open the applicationContext-security-web.xml file (found in &lt;js-install&gt;\apache-tomcat\webapps\jasperserver-pro\WEB-INF).</li>
    <li>Locate the <code>antiClickJackingEnabled</code> property in the <code>webAppSecurityFilter</code> bean, and set it to true. Setting this property to true instructs JasperReports Server to include an X-Frame-Options header in every response.</li>
    <li>You can also set the <code>antiClickJackingOption</code> property to control the header value. Valid values are:</li>
    </ol>
    <ul>
    <li><p><code>DENY</code> - JasperReports Server doesn't load into any <span>iframe</span>.</p>
    <ul>
    <li><code>SAMEORIGIN</code> - JasperReports Server only loads into an <span>iframe</span> on a page in the same domain as JasperReports Server.</li>
    <li><code>ALLOW-FROM</code> - JasperReports Server only loads in a frame on a page specified in <code>antiClickJackingUri</code> property.</li>
    </ul></li>
    </ul>
    <ol>
    <li>If you set the <span>antiClickJackingOption</span> property to <code>ALLOW-FROM</code>, also be sure to set the <code>antiClickJackingUri</code> property to a valid URI.</li>
    <li>Save the file and restart the server.</li>
    </ol></td>
    </tr>
    </tbody>
    </table>

    |  |  |
    |----|----|
    | ![note icon ns](assets/images/note-icon-ns.png) | If you use iframes to embed JasperReports Server (including use of Visualize.js), set the `antiClickJackingOption` to either `SAMEORIGIN` (if the embedding host is on the same domain as JasperReports Server) or `ALLOW-FROM` (if the embedding host is on a different domain than JasperReports Server). If you use `ALLOW-FROM`, also set the `antiClickJackingUri` property. |
    |   | Clickjack protection doesn't support cases in which multiple domains embed JasperReports Server. |

-   Directory Access Control. A new option controls access to resources in the file system of the JasperReports Server host using the `ResourceForwardingServlet` servlet. The servlet forwards requests to handle browser caching. For example, when it receives calls to `/runtime/<hex-code>/<my-resource>`, it forwards them to `/<my-resource>`.

The servlet controls access using a whitelist that can include both resource and directory names; for simplicity here, we use the term directories.The whitelist defines the directories to which access is granted; access to other directories is denied. By default, it lists all the directories that JasperReports Server requires.

New Configuration

!!! warning

    Note that this approach differs from the previous implementation, and requires intervention in fewer cases. In general, you don't need to change it. We recommend that any additions you make to the whitelist be considered carefully and tested thoroughly.

    We advise against removing the default values from the list, as this would impair functionality.

To configure this list, edit the `forwardWhitelist` parameter of the `ResourceForwardingServlet` servlet in the web.xml file.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><ol>
<li>Using a text editor, open the web.xml file (found in &lt;js-install&gt;\apache-tomcat\webapps\jasperserver-<span>pro</span> \WEB-INF).</li>
<li>Locate the <code>init-param</code> section of the <code>ResourceForwardingServlet</code> servlet.</li>
<li>In the <code>param-value</code> section of the <code>forwardWhitelist</code> parameter, review the comma-separated list of directories that JasperReports Server users should be able to access. This parameter can only list directories under the jasperserver-<span>pro</span> deployment directory.</li>
<li>If you make changes, save the file, restart the server, and test the application thoroughly.</li>
</ol></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td><p><img src="assets/images/note-icon-ns.png" alt="note icon ns" /></p></td>
<td><p>In a previous version, access to the application's resources was controlled by a blacklist. The blacklist has been removed in favor of this whitelist.</p></td>
</tr>
<tr>
<td> </td>
<td><p>The previous approach sometimes required additional steps. For example, if you restricted access using the <code>security-constraint</code> tag in web.xml, you may have also restricted that access using the <code>ResourceForwardingServlet</code> servlet. This step is no longer necessary, since access is now denied by default.</p>
<p>If a high-priority case requires you to customize the <code>ResourceForwardingServlet</code> servlet and use JasperReports Server to cache a third-party resource, you might consider editing this list and making further customizations; we advise against such changes due to the security risks they might pose.</p></td>
</tr>
</tbody>
</table>
