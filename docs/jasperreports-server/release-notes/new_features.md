---
title: New Features
description: This section describes new features introduced in the Jaspersoft BI Suite Version 10.1 release.
---

# New Features

This section describes new features introduced in the Jaspersoft BI Suite Version 10.1 release.

To view the Release Notes of version 10.0.0, see [JasperReports® Server Release Notes v10.0.0](https://community.jaspersoft.com/documentation/jasperreports-server/tibco-jasperreports-server-release-notes/v1000/relnotesbody-_-overview/).

To view the new features added to the various products of Jaspersoft BI Suite, refer to the following list:

- JasperReports® Server 10.1.0
- Jaspersoft® Studio 10.1.0
- JasperReports® Web Studio 10.1.0

## JasperReports® Server 10.1.0

For JasperReports® Server 10.1.0, the following improvements have been added:

- **Centralized Scheduler Dashboard**

  Enhance operational oversight with the new Scheduler Dashboard. This centralized Admin Console provides real-time visibility into your entire scheduled report landscape.

  - Comprehensive Monitoring: Track job states in real-time, from queued to completed.

  - Enhanced Admin Controls: Restart individual job executions or view detailed historical data for finished triggers using new dedicated action buttons.

  - Actionable Insights: Administrators gain full access to execution history, while standard users can monitor success and failure counts at a glance.

- **Password History Validation**

  Strengthen your enterprise security and simplify compliance with our new Password History Validation. This feature prevents users from recycling their last *n* passwords during the reset process, defending against unauthorized access and aligning your environment with modern security best practices.

  This feature is turned off by default. To implement password recycling restrictions, you must explicitly enable the corresponding configuration property.

  For more information, see JasperReports® Server Security Guide.

- **Modernized Password Storage**

  Upgrade your security posture with our state-of-the-art password storage system. We have introduced industry-leading, one-way hashing algorithms that provide superior protection against unauthorized access. This update ensures a more robust defense while maintaining seamless backward compatibility for all existing users.

  For more information, see JasperReports® Server Security Guide.

- **Migration to Jackson**

  We have successfully migrated JasperReports® Server’s data binding and serialization framework from legacy Castor to the industry-leading Jackson library. This architectural upgrade delivers faster response times and significantly improved system stability. While this represents a major technical leap forward, the transition is entirely seamless. Users will enjoy a faster, more reliable experience with no manual configuration required.

  <div class="admonition note">
  <p class="admonition-title">Note</p>

                      <p>Resources exported from version 10.1.0  cannot be imported into older versions of the application.</p>

  </div>

  For more information, see JasperReports® Server Upgrade Guide.

- **Retired Apache Tiles**

  We have streamlined the JasperReports® Server core by migrating from legacy Apache Tiles to standard JSP Tag Files. By eliminating complex external dependencies and adopting a sleek, native framework (now located in `WEB-INF/tags/templates/`), we have built a reliable foundation.

  This is an internal architectural upgrade. The user interface and public APIs remain unchanged. If you use custom JSP overlays, update your references from `tiles:insertTemplate` to the new `<tmpl:*>` tag files to align with this modernization.

  For more information, see JasperReports® Server Upgrade Guide.

## Jaspersoft® Studio 10.1.0

For Jaspersoft® Studio 10.1.0, the following improvements have been added:

- **Intuitive report design**

  The JasperReports Library PDF exporter now supports Section 508, PDF/UA, and WCAG standards by embedding semantic tags for screen reader navigation. Our goal is to ensure reports pass validation in tools like PAC, VeraPDF, and Adobe Professional.

  True accessibility is a partnership between the software and the report designer. While the exporter provides the technical tagging, report designers must still prioritize accessible layouts, such as high color contrast and simple table structures, to ensure true readability.

  <div class="admonition note">
  <p class="admonition-title">Note</p>

                      <p>Starting release 10.1.0, accessibility features have been removed from all future Community Edition releases. When upgrading to or embedding library version 10.1.0, reports will throw a <code>Tag PDF not supported</code> exception on the first run due to the removal of accessibility features from the Community Edition. </p>
                      <p>For more information, see <a href="https://community.jaspersoft.com/knowledgebase/getting-started/jasperreports-library-pdf-accessibility-feature-r5060/">JasperReports Library PDF Accessibility Feature</a>.</p>

  </div>

- **Single Sign On (Browser) option**

  Jaspersoft® Studio now features enhanced SSO support via an embedded browser widget, simplifying connections to JasperReports® Server instances secured by external identity providers (such as Okta).

  You select the new **Single Sign-On (Browser)** option in the **Server Profile Wizard** to log in via an in-app browser window. Upon successful authentication, you can capture the active `JSESSIONID` session cookie to securely unlock repository browsing, report publishing, and resource management without storing corporate credentials.

- **Improved Eclipse IO Console appender**

  This release introduces key improvements to our logging capabilities. We have enhanced the Eclipse IO Console appender and added two new JVM properties:

  - `jss.logging.tmpdir`, can be configured in your `.ini` file for use in the `log4J2.xml` file appender.

  - `jss.logging.redirectSystemStreams` (defaults to `false`), allows you to intercept and redirect `System.out` and `System.err` streams when enabled.

## JasperReports® Web Studio 10.1.0

For JasperReports® Web Studio 10.1.0, the following improvements have been added:

- **Drag-and-drop query building**

  Accelerate query design by dragging nodes directly from the **Metadata** panel into the query editor. This streamlined workflow eliminates manual coding errors and simplifies the construction of complex queries.

- **Composite elements**

  Accelerate report creation with new Composite elements. Effortlessly drag and drop preconfigured components, such as dynamic timestamps and automatic page numbering, into your canvas to streamline complex workflows and save development time.

- **Contextual "maximize" action**

  Maximize your design workspace with the new "Maximize Band" action. Simply select any report band and click the button to instantly expand it to fill the available space, streamlining your layout workflow and eliminating manual resizing.

- **Manual parameter reordering**

  Manage the resolution sequence of your datasets precisely by using a simple drag-and-drop interface. By grabbing the new handle icon to the left of any parameter name, you can reorder your list to ensure that dependent variables resolve in the correct sequence for your query, eliminating manual configuration errors and streamlining dataset logic.

- **Enhanced pattern editor**

  Configuring numeric and date-time formats is now more intuitive with the enhanced Pattern Editor. Clicking the ellipsis (...) button opens a new dialog featuring a comprehensive library of common presets. Simply select a predefined pattern and use the built-in controls to fine-tune the formatting to your specific requirements, ensuring precision with minimal effort.

- **Automated aggregate calculations**

  Dragging fields into summary or group bands now triggers the "Smart Calculation" dialog, automating the setup of aggregate data. Simply choose your desired calculation, such as sum, average, or count, and the system instantly generates the necessary variables and expressions. For numeric fields, additional advanced aggregation options are available to further accelerate your report design.

- **JDBC scalability improvements**

  Experience significantly faster performance when working with large database schemas. Our new lazy-loading logic eliminates timeouts by fetching metadata in smaller, on-demand increments, ensuring a smooth and responsive design experience even when connecting to the most complex data environments.

- **Streamlined repository access**

  Simplify your onboarding. Report repositories and owners are now generated automatically. Upon login, the interface directs you straight to your personal repository, eliminating manual configuration and providing a seamless start-to-finish experience.

- **Cross-Site Request Forgery (CSRF) protection**

  implemented CSRF security filters across the entire application. This critical security update prevents unauthorized commands from being executed on behalf of authenticated users, significantly strengthening the platform's defense against malicious exploits and ensuring a more secure environment for your data.

- **Advanced Query Designer**

  Our new JavaScript-based query editor is a powerful tool designed to bridge the gap between complex design and actionable data. This powerhouse editor offers an intuitive interface that combines visual drag-and-drop building with a professional text-based environment, allowing you to master datasets using standard `SELECT, FROM, WHERE`, and `ORDER BY` components. With integrated metadata insights and high-fidelity result previews, you can build sophisticated queries featuring conditional logic, dynamic expressions, and nested subqueries with confidence. Every design is backed by intelligent real-time validation, ensuring flawless accuracy and peak performance for your most demanding reports.

- **Modernized Repository UI**

  Experience a professional-grade file management interface designed for speed and precision. This comprehensive refactor introduces visual versatility, allowing you to tailor your workspace with customizable view modes, and precision control through multi-select functionality and hover-triggered shortcuts. We have also optimized file handling to ensure folder creation. Data transfers are faster and more reliable. Additionally, you can now gain priority access to your most important resources via the new **Favorites** section, putting your go-to reports just one click away.
