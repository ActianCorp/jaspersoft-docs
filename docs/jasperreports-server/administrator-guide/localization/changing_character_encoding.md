---
title: Changing Character Encoding
description: "Depending on the third-party software used and supported locales, you may also have to configure JasperReports Server and its host."
---

# Changing Character Encoding

Depending on the third-party software used and supported locales, you may also have to configure JasperReports Server and its host.

The steps described in this section are necessary only under certain circumstances, such as if you plan to use a character encoding form that UTF-8 cannot handle.

To use a character encoding form other than UTF-8, you must configure JasperReports Server, your application server, and your database server.

## Configuring JasperReports Server

To specify a different character encoding

1.  Open the `.../WEB-INF/applicationContext.xml` file and locate the following bean. It is configured for UTF-8:

    ``` xml
    <bean id="encodingProvider"
            class="com.jaspersoft.jasperserver.api.common.util.
            StaticCharacterEncodingProvider">
        <constructor-arg value="UTF-8" />
    </bean>
    ```

2.  Change `"UTF-8"` to the encoding type your database server and application server use. For example:

    ``` xml
    <bean id="encodingProvider"
            class="com.jaspersoft.jasperserver.api.common.util.
            StaticCharacterEncodingProvider">
        <constructor-arg value="UTF-16" />
    </bean>
    ```

3.  Save the file.

4.  Restart JasperReports Server.

## Configuring the Application Server and Database Server

If you want to use a character encoding other than UTF-8, you may need to configure the third-party software that JasperReports Server relies on. For more information, refer to the documentation for your application server and database server. For Tomcat, you can specify a different character encoding by following steps similar to those described in [Tomcat](utf-8_configuration.md) and [UTF-8 Configuration](utf-8_configuration.md).

## Configuration for Localized Analysis Schemas

If you plan to use localized OLAP views, you must take additional steps to configure JasperReports Server.

To configure JasperReports Server for localized OLAP views

1.  Every Unicode database that JasperReports Server interacts with (whether it is the repository database or a database accessed through a data source defined in JasperReports Server) must be created to support UTF-8. For example, to create the Foodmart database in PostgreSQL, you might give a command similar to the following:

    ``` sql
    create database foodmart_ja encoding='utf8';
    ```

2.  The URL of any OLAP data source that JasperReports Server accesses must be properly configured in the `.../META-INF/context.xml` file. For example, the URL definition for the Foodmart sample database might be similar to the following:

    ``` xml
    <Resource name="jdbc/MondrianFoodMart_ja"
        auth="Container" type="javax.sql.DataSource"
        maxTotal="100" maxIdle="30" maxWaitMillis="10000"
        username="postgres" password="postgres" driverClassName="org.postgresql.Driver"
        url="jdbc:postgresql://localhost:5432/foodmart_ja" />
    ```

3.  Encoding options must be added to the JDBC connection string for any data source that points to an OLAP database. For example, when creating a data source in JasperReports Server that points to an OLAP database, use the following connection string:

``` text
jdbc:postgresql://localhost:5432/foodmart_ja
```
