---
title: Project Folder Types and Report Execution Contexts
description: "When a report is run in Jaspersoft Studio, it is run within a \"report execution context.\" This context is defined by custom Java code and JasperReports Library configuration properties that direct..."
---

# Project Folder Types and Report Execution Contexts

When a report is run in Jaspersoft Studio, it is run within a "report execution context." This context is defined by custom Java code and JasperReports Library configuration properties that direct the behavior of the reporting engine.

At execution time, a report might need a number of resources, such as data sources or adapters, subreports, style templates, images, and fonts, as well as any custom code in the form of compiled Java classes. The way these resources are organized and loaded can differ when you deploy a report to one of the following:

- JasperReports Library (default)

- JasperReports Server

Each context approximates how reports work in their target environment, affecting the repository root, JasperReports Library properties, strategy for java class loaders, resource loading, and default report preview for reports. There may be some differences from the actual production environment, particularly for JasperReports Server.

Programmers familiar with Java and Eclipse can add their own contexts.

## Available Execution Contexts

### JasperReports Library Context

The JasperReports Library context is the default. Use it if you are deploying to your own JasperReports Library implementation. Selecting this context sets the environment as follows:

- The repository root is set to the root of the project folder.

- The report classpath is taken from the project.

- The project uses the JasperReports Library properties set in **Window \> Preferences \> Jaspersoft Studio \> Properties** and in **Mac \> Preferences \> Jaspersoft Studio \> Properties**.

- The report can access global (repository explorer) data adapters. See [To create a global data adapter](data-adapters/data-adapters-creating.md) for more information.

- Report preview defaults to Java.

### JasperReports Server Context

The JasperReports Server context emulates the functionality of a generic JasperReports Server. It is not able to detect custom classes or other customizations of a particular JasperReports Server instance.

If you have a folder connected to a JasperReports Server instance with a JasperReports Server context configured, the environment is set as follows:

- The repository root is set to the root of the server.

- The report classpath attempts to emulate the classpath for a JasperReports Server instance.

- The project uses the default JasperReports Library properties.

- The report can only access local data adapters.

- Report preview defaults to HTML.

See [Configuring a Project for JasperReports Server](jrs-server/jrs-context.md) for more information on configuring a JasperReports Server context.

## Choosing Project Folder Type

The report execution context is set on a project folder basis. By default, the report execution context of a project folder inherits from its parent project up to the root folder of the repository. The root folder is set to the JasperReports Library context by default.

To set the context of a project:

1.  Right-click the project folder in the Repository Explorer.
2.  Select **Report Repository Type** from the context menu and select one of the following options:

- **Reset to Parent** (default): Sets the project to inherit context type directly from its parent folder or the root folder of the repository.
- **JasperReports Library**
- **JasperReports Server**

For the JasperReports Server contexts, there may be additional steps necessary to configure the project fully. See [Setting the Context for JasperReports Server](jrs-server/jrs-context.md) for more information.
