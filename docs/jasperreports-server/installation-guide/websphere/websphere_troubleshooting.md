---
title: Troubleshooting your Configuration
description: The most common problems are errors in the database configuration. These are typically errors in the database configuration files or in the application server configuration files. For information...
---

# Troubleshooting your Configuration

## Startup Problems

The most common problems are errors in the database configuration. These are typically errors in the database configuration files or in the application server configuration files. For information about resolving these errors, refer to the troubleshooting section [Troubleshooting](../troubleshooting/troubleshooting.md).

## Error Running Report

If you have trouble running reports in your new JasperReports Server instance, refer to the troubleshooting section [Error Running a Report](../troubleshooting/database_related_problems.md). If you are having trouble running the MDX example Topic or SugarCRM OLAP view, you need to update the port for XML/A connections. See [Updating XML/A Connection Definitions (Optional)](websphere_xmla_connection.md).

## Filter Error Using MySQL

The following error could be caused by an incorrect ampersand setting on your data source configuration:

`Error 500: Filter [characterEncodingProxyFilter]: could not be initialized`

The data source line needs to have `&amp;` and not `&` to be evaluated correctly. That is, the URL you enter in the procedure to define the JDBC data source and expose it through JNDI should look like this:

`jdbc:mysql://localhost/jasperserver?useUnicode=true&amp;characterEncoding=UTF-8`

## Error Creating Internationalized Name

If you encounter errors when creating resources with internationalized names and you have an Oracle database, configure your Oracle JDBC driver. Set the Oracle-specific option listed in the tables of [Setting JVM Options](websphere_install_procedure.md).

## Xerces Error

In earlier releases of JasperReports Server, it was possible to find the following error in the WebSphere log:

``` yaml
SRVE0068E: Uncaught exception thrown in one of the service methods of the servlet:
jasperserver. Exception thrown: org.springframework.web.util.NestedServletException:
javax.xml.validation.SchemaFactoryFinder$ConfigurationError: Provider
org.apache.xerces.jaxp.validation.XMLSchemaFactory could not be instantiated:
org.apache.xerces.impl.dv.DVFactoryException: DTD factory class
org.apache.xerces.impl.dv.dtd.DTDDVFactoryImpl does not extend from DTDDVFactory.
```

More recently, the server uses version 2.10.0.

The error shown above is caused by a conflict between the IBM JDK used by WebSphere and the xercesImpl-2.6.2 library bundled with older versions of JasperReports Server. There are two solutions:

-   Remove the xercesImpl library from the following location:

    `<websphere>\profiles\AppSrv<NN>\installedApps\<node>\jasperserver-pro_war.ear\`

    `jasperserver-pro.war\WEB-INF\lib`

-   Update the xercesImpl library to a new version (if it is an old version).
