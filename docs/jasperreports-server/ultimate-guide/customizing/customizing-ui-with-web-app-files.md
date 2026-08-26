---
title: Customizing the UI With Web App Files
description: "Many components of the UI are created from the source code. The entire process from designing the UI in source files to displaying the UI in the server is very complex, with several interacting..."
---

# Customizing the UI With Web App Files

Many components of the UI are created from the source code. The entire process from designing the UI in source files to displaying the UI in the server is very complex, with several interacting components. JasperReports Server uses the Spring Framework based on compiled Java beans, but the layout of the UI is also controlled by Java Server Pages (JSP files), the SiteMesh framework that decorates pages, and the CSS files seen in the previous section. Some of these components use additional XML files for configuration.

Several kinds of files are involved in creating the UI:

-   Interpreted files such as JSP, XML, and CSS that the server processes in order to generate the UI. The advantage of interpreted files is that you can modify them in a running instance and have them take effect immediately (as with CSS), or after restarting the server (as with JSP). Much of the UI can be customized with interpreted files.

-   Compiled Java files that define the underlying behavior of the server, for example, what happens when you click a button to run a report. These are Java beans used in the Spring framework, where they're also called Spring beans.

To change the behavior of a Java file, you must recompile it, rebuild the server, and redeploy it in an application server. Therefore, to change UI features controlled by Java files, you must have the source code distribution and a testing environment to build and deploy the server. For more information, see [Working With Source Code Files](customizing-java-classes.md).
