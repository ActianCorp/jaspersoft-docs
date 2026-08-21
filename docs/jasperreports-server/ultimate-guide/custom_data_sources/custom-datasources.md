---
title: Custom Data Sources
description: "JasperReports Server provides out-of-the-box support for many commonly used data sources, such as JDBC, JNDI, cloud-based databases, and several types of big data, as described in the JasperReports..."
---

# Custom Data Sources

JasperReports Server provides out-of-the-box support for many commonly used data sources, such as JDBC, JNDI, cloud-based databases, and several types of big data, as described in the JasperReports Server Administrator Guide. In some cases, however, you may want to connect to a data source that is not supported by default or to a custom data source that you have created. To do this, you need to extend JasperReports Server by adding certain executable libraries and editing files in your server's configuration.

This chapter explains how to add new data source types from several different origins:

- Pre-installed data sources: The libraries for these are installed by default, but you need to change the configuration to make them visible in the user interface.

- Custom data source examples: The source code for these is installed by default, but you must run the included scripts to compile the libraries, copy them to the correct location, and configure the server.

- Your own custom data sources: You must write Java classes and compile them into JAR files, or download them from the community website, then copy them to the correct location and configure the server.

All three use the same mechanisms and files to be configured in the server. After following the appropriate steps, your custom data source types show up in the New Data Source dialog, and users can create instances of your custom data source and use them to access data. For example, the JSON and XML file data source types added in JasperReports Server 6.1 are implemented using the same patterns as for custom data source types.

!!! note

    This chapter explains how to configure JasperReports Server to support an existing JasperReports Library data source (`JRDataSource`). For this, you must write additional code to implement further interfaces (`ReportDataSourceService` and optionally others).

    To develop your own custom data source (`JRDataSource`), see the source code for the examples mentioned in this chapter. For further information, see the JasperReports Library Ultimate Guide.

This chapter contains the following sections:

- [Pre-installed Custom Data Source Types](pre-installed-data-sources.md)

- [Custom Data Source Examples](custom-data-source-examples.md)

- [Custom Data Source Architecture](custom-data-source-architecture.md)

- [Creating a Custom Data Source](custom-data-source-creation.md)
