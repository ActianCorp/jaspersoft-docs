---
title: Data Sources
description: "A data source is a resource in the repository that specifies how and where to obtain the data displayed by reports, Domains, Ad Hoc views, and OLAP views. Administrators must define data sources..."
---

# Data Sources

A data source is a resource in the repository that specifies how and where to obtain the data displayed by reports, Domains, Ad Hoc views, and OLAP views. Administrators must define data sources before uploading reports that rely on them. Typically, a data source specifies the URI of the database server and the details you need to access it, such as a username and password.

JasperReports Server provides data source types for relational databases, most flavors of big data, and for specialized data such as Amazon Web Services and JavaBean data. Virtual data sources allow you to combine several data sources into one.

JasperReports Server can access any relational database that supports the SQL query language through the JDBC (Java DataBase Connectivity) API. In this case, you can configure two types of data sources in the repository:

- JDBC data source: Establishes a direct connection to the database server using its JDBC driver. After installation, JasperReports Server includes JDBC drivers to access the most popular databases: MySQL, PostgreSQL, Oracle, SQL Server, DB2, Salesforce. The server also includes a JDBC driver that can access Hadoop-Hive, MongoDB, Cassandra, TIBCO Data Virtualization, Google BigQuery, and more. If you want to install drivers for other databases, or if you want to use alternate drivers, the system administrator can upload and manage JDBC drivers through the UI. With JDBC data sources, JasperReports Server configures and manages the connections to the database. By default, the maximum number of simultaneous connections for each data source is 20.

- JNDI data source: Relies on the JNDI (Java Naming and Directory Interface) service of your application server to access a database connection. First configure your application server to install its JDBC drivers and configure its database connections. With JNDI data sources, the configuration of the application server determines the number of shared connections. Note that the application server connects to the database using JDBC, meaning that JNDI data sources are available for all databases that support JDBC.

!!! note

    For the list of certified data sources, refer the Jaspersoft Platform Support Guide.

JasperReports Server also supports some specialized data sources:

- Amazon Web Services (AWS) data source: Accesses data stored in your AWS data store using JasperReports Server, either on-premises or in the cloud.
- Microsoft Azure SQL data source: Allows you to access data stored in your Azure SQL Server database.
- Virtual data source: Allows you to combine multiple data sources into a single data source and join them within a Domain. You can also wrap a data source for big data to be used in a Domain.
- MongoDB: This custom data source for MongoDB supports Jaspersoft's own MongoDB Query Language. A MongoDB JDBC driver is also available.
- XLS and XLSX data sources: Allows you to generate reports based on data in the XLS and XLSX formats.
- File data source: Allows you to generate reports based on data in XML and JSON formats.
- Bean data source - Allows you to access data encapsulated in JavaBeans.
- Internal diagnostic data source: A custom data source for the server's own diagnostic data. The diagnostic information is available only to system admins (`superuser` by default). For more information, see [Using the Diagnostic Data in Reports](../diagnostics/using_the_diagnostic_data_in_reports.md).

In the case of analysis data, JasperReports Server supports OLAP data sources (such as Mondrian and XML/A connections). For information about analysis data sources, see the Jaspersoft OLAP Ultimate Guide.

!!! note

    You can extend JasperReports Server to support any custom data source. Custom data sources consist of Java implementation classes, a message catalog, and a Spring bean definition. For more information about custom data sources, see the JasperReports Server Ultimate Guide.

This chapter contains the following sections:

- [Attributes in Data Source Definitions](attributes_in_data_source_definitions.md)

- [JDBC Data Sources](jdbc_data_sources.md)

- [Managing JDBC Drivers](managing_jdbc_drivers.md)

- [JNDI Data Sources](jndi_data_sources.md)

- [AWS Data Sources](aws_data_sources.md)

- [Azure SQL Data Sources](azure_data_sources.md)

- [Snowflake Data Sources](snowflake_data_sources.md)

- [Hadoop-Hive Data Sources](hadoop-hive_data_sources.md)

- [MongoDB Data Sources](mongodb_data_sources.md)

- [Virtual Data Sources](virtual_data_sources.md)

- [TIBCO Data Virtualization](tibco_data_virtualization.md)

- [XLS and XLSX Data Sources](xls_xlsx_data_sources.md)

- [File Data Sources](file_data_sources.md)

- [Bean Data Sources](bean_data_sources.md)
