---
title: Changes in Functionality
description: This section describes changes in functionality in the Jaspersoft BI Suite Version 10.1 release.
---

# Changes in Functionality

This section describes changes in functionality in the Jaspersoft BI Suite Version 10.1 release.

For information about changes in functionality in version 9.0.0, see [JasperReports® Server Release Notes v9.0.0](https://community.jaspersoft.com/documentation/jasperreports-server/tibco-jasperreports-server-release-notes/v900/relnotesbody-_-overview/).

## JasperReports® Server 10.1.0

!!! note

    The JasperReports® Server 10.1.0 release doesn't support binary installer.

Following are the list of changes in JasperReports® Server10.1.0:

- **Ad Hoc UX Panel (Layout Band)**

  The Layout Band has been completely redesigned to provide a more intuitive experience when creating visualizations. It now dynamically adapts to each visualization type, presenting specific areas for fields and measures that directly correspond to how the visualization is constructed. This update dramatically improves the user experience and simplifies the visualization building process. For more information, see the JasperReports® Server User Guide.

- **Database Connectors Certification**

  The following native connectors are certified:

  - Elasticsearch

  - Neo4j

  - MongoDB

  - Apache Hive

  - Impala

  - Cassandra

  - Spark SQL

  - Apache Spark

  - Snowflake

  - Mongo DB native

  - Azure SQL

  - Google BigQuery

  - Autonomous REST JDBC

  - AWS Athena

  For more information, see JasperReports® Server Administrator Guide.

- **csrfguard Library Upgrade**

  With the csrfguard library upgraded from version 3.1.0 to 4.3.0, it was observed that all server requests were rejected.

  This is because in the original OWASP library version 4.3.0, the `org.owasp.csrfguard.TokenPerPage` property is set to `true` by default and cannot be set to `false`. The said library does not support changing the property value for better security. When this property is set to `true` new tokens are created per API URL within a valid session time.

  For more information, see JasperReports® Server Administrator Guide.

- **Library changes**:

  The library changes include:

  - Hibernate upgraded to version 6.6.x

  - Spring upgraded to version 6.2.x

  - Spring-security upgrade to 6.5.x

  - React upgraded to version 18

  - Material UI upgraded to version 6

  - Node Js upgraded to version 20

  - Highcharts upgraded to version 11.1.0

  - commons-dbcp upgraded to 2.12.0

  - Lucene library upgraded to version 9.0

## Jaspersoft® Studio 10.1.0

Following are the list of changes in Jaspersoft® Studio 10.1.0:

- **MongoDB Connector, Google Maps and Custom Visualization Component**

  The MongoDB Connector, Google Maps and Custom Visualization Component are now exclusively available in Jaspersoft® Studio Professional.

  For more information, see the Jaspersoft® Studio User Guide.

- **Removal of JasperReports® IO**

  JasperReports® IO is no longer bundled with Jaspersoft® Studio Professional. For more information, see the Jaspersoft® Studio User Guide.

- JasperReports® Library **Compatibility**

  The JRXML model is has been upgraded from version 6.x to 7.

  With the new JRXML 7, the users must ensure they do not publish reports using the older JasperReports® Server instances. The user should correctly set the project's compatibility settings and/or the JasperReports® Server advanced properties (required library version).

  For more information, see the Jaspersoft® Studio User Guide.

- **SOAP Protocol**

  The SOAP protocol is no longer supported for publishing reports from Jaspersoft® Studio to JasperReports® Server. The RESTv2 protocol is used instead.

  For more information, see the Jaspersoft® Studio User Guide.

- **Revised Logging System**

  Jaspersoft® Studio now uses a revised, centralized logging mechanism based on Apache Log4j2. The new architecture unifies all application and underlying Java framework logging output. All logging behavior is now controlled by a single, easily modifiable file, `log4j2.xml` in the installation folder.

  You can access all your logging information instantly with the new, dedicated Console view integrated directly into the Jaspersoft® Studio user interface.

  For more information, see the Jaspersoft® Studio User Guide.

- **Library changes**:

  The library changes include:

  - D3.js version 7.9 library

  - Highcharts and Highmaps upgraded to version 11.1.0

  - Mongo Java driver upgraded to version 3.12.14

  - PostgreSQL driver upgraded to version 42.7.3

  - H2 driver upgraded to version 2.3.232

  - Jersey library upgraded to version 3.1.10

  - Spring library upgraded to version 6.2.11

  - Jackson library upgraded to version 2.18.2

  - Apache Batik library upgraded to version 1.19.0

  - OpenPDF library upgraded to version 1.3.43

  - Apache POI library upgraded to version 5.4.1

  - Apache Log4J2 library upgraded to version 2.24.3

  - Apache Commons BeanUtils library upgraded to version 1.11.0

  - Apache Commons BeanUtils2 library added with version 2.0.0M2
