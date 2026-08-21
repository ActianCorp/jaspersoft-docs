---
title: Working With JDBC Drivers
description: This section describes how to set up your installation to use a driver other than the default driver.
---

# Working With JDBC Drivers

This section describes how to set up your installation to use a driver other than the default driver.

## Open Source JDBC Drivers

For open source JDBC drivers, buildomatic is set up to use a single default driver. If you want to use a driver other than the default driver, you can modify the buildomatic property files that determine the default JDBC driver.

The buildomatic JDBC driver property files are set up to point to a specific driver jar. This allows for multiple driver jar files in the same `buildomatic/conf_source/db/<dbType>/jdbc` folder. During the installation procedure, only the default driver jar is copied to your application server.

If you want to use a newer JDBC driver version or a different JDBC driver, you can modify the buildomatic properties seen in your `default_master.properties` file.

### PostgreSQL Example

The buildomatic/conf_source/db/postgresql/jdbc folder contains these driver files:

`postgresql-42.2.5.jar`

For instance, to change the default driver used by PostgreSQL from type `jdbc4.2` to` jdbc4.1`:

1.  Download `postgresql-42.5.5.jar` from https://jdbc.postgresql.org/download.html and save it under `buildomatic/conf_source/db/postgresql/jdbc`.
2.  Edit your `default_master.properties` file, `<js-install>`. Edit your `default_master.properties` file, `<js-install>/buildomatic/default_master.properties` as follows:

Uncomment and change:

`# maven.jdbc.version=42.2.5`

To:

`maven.jdbc.version42.2.5.jre7`

When you next run a buildomatic command, such as `deploy-webapp-``pro`` `, the `jdbc4.1` driver is copied to your application server.

### MySQL Example

The `buildomatic/conf_source/db/mysql/jdbc` folder contains this driver file:

`mariadb-java-client-2.5.4.jar`

If for instance, you want to use a JDBC driver built and distributed by the MySQL project, such as `mysql-connector-java-8.0.20-bin.jar`, then you first need to:

1.  Download the driver from the MySQL Connector/J download location:

    `https://dev.mysql.com/downloads/connector/j/`

2.  Next, change your buildomatic configuration properties to point to this new driver.
    1.  Edit your `default_master.properties` file:

        `<js-install>/buildomatic/default_master.properties`

    2.  Uncomment and change:

        `# jdbcDriverClass=com.mysql.jdbc.Driver`

        `# maven.jdbc.groupId=mysql`

        `# maven.jdbc.artifactId=mysql-connector-java`

        `# maven.jdbc.version=5.1.30-bin`

        To:

        `jdbcDriverClass=com.mysql.jdbc.Driver`

        `maven.jdbc.groupId=mysql`

        `maven.jdbc.artifactId=mysql-connector-java`

        `maven.jdbc.version=5.1.30-bin`

## Installing Database Vendor JDBC Drivers

JasperReports Server no longer includes JDBC drivers for the following commercial databases:

- DB2
- Oracle
- SQL Server

You can download the driver supplied by the database vendor as described below. To do this, you must first obtain and install the driver you want, then copy that driver into buildomatic.

### Download a Vendor JDBC Driver

To use the driver supplied by the database vendor, you have to download and install it.

Download Driver Jar from Vendor Website

You can download a commercial JDBC driver from the vendor's website. Here are some sites where you can download packages for supported databases:

| JDBC Driver | Download Site |
|----|----|
| DB2 | <https://www.ibm.com/support/pages/db2-jdbc-driver-versions-and-downloads> |
| Oracle | <https://www.oracle.com/database/technologies/appdev/jdbc-downloads.html> |
| SQL Server | <https://learn.microsoft.com/en-us/sql/connect/jdbc/download-microsoft-jdbc-driver-for-sql-server?view=sql-server-ver16> |

Once you have downloaded your driver, copy it to the correct location and configure your files as described in the sections below.

**Collect Driver Jar from Existing Application**

You may already have a JDBC driver in an application running on your network. If so, you can simply copy that driver jar to the JasperReports Server install location.

### Oracle Example

Copy your Oracle driver to the following directory:

`<js-install>/buildomatic/conf_source/db/oracle/jdbc/`

### SQL Server Example

Copy your SQL Server driver to the following directory:

`<js-install>/buildomatic/conf_source/db/sqlserver/jdbc`

### DB2 Example

Copy your DB2 driver to the following directory:

`<js-install>/buildomatic/conf_source/db/db2/jdbc`

## Working with Oracle RAC

You can use Oracle RAC with the TIBCO JDBC Oracle driver. This driver works with Oracle RAC with the following settings:

- Use Oracle for non-CDB connection settings as described in [Standard Oracle options](../../../installation-guide/warfileinstall/war_install_using_js_install.md).

- Use `js-install.bat/sh minimal` with Oracle. This option does not install sample databases.

To support additional functionality with Oracle RAC, such as load balancing with multiple servers, you need to configure your application server and manually set up the correct connection URL.

### Tomcat Load Balancing Example

1.  Change to the `<tomcat>/webapps/jasperserver-pro/META-INF` directory and open `context.xml` in a text editor.
2.  Edit the `url` property by adding additional connection properties for the data sources that you want. The following example shows how to set up the connection pool to use Oracle RAC with load balancing with a primary server and three alternate servers:

```
jdbc:oracle:thin:@(DESCRIPTION=(LOAD_BALANCE=on)(ADDRESS=(PROTOCOL=tcp)(HOST=myhost1)(PORT=1525))(ADDRESS=(PROTOCOL=tcp)(HOST=myhost2)(PORT=1525))(CONNECT_DATA=(SERVICE_NAME=myserviceDB1)))
```

### JBoss EAP/WildFly Load Balancing Example

1.  Change to the `<jboss-install>/standalone/deployments/jasperserver-pro.war/WEB-INF` directory and open `js-jboss7-ds.xml` in a text editor.
2.  Edit the `connection-url` tag for the data sources that you want. The following example shows how to set up a connection pool to use PostgreSQL RAC with load balancing with a primary server and three alternate servers.

```
<datasource jta="false" jndi-name="java:/jdbc/jasperserver" pool-name="jasperserver" enabled="true" use-ccm="false">
   <connection-url>jdbc:oracle:thin:@(DESCRIPTION=(LOAD_BALANCE=on)(ADDRESS=(PROTOCOL=tcp)(HOST=myhost1)(PORT=1525))(ADDRESS=(PROTOCOL=tcp)(HOST=myhost2)(PORT=1525))(CONNECT_DATA=(SERVICE_NAME=myserviceDB1)))</connection-url>
   <driver>ojdbc8-23.2.0.0.jar</driver>
   <security>
      <user-name>jasperserver</user-name>
      <password>password</password>
   </security>
   <pool>
      <min-pool-size>5</min-pool-size>
      <max-pool-size>50</max-pool-size>
      <prefill>true</prefill>
   </pool>
   <validation>
      <validate-on-match>false</validate-on-match>
      <background-validation>false</background-validation>
      <check-valid-connection-sql>SELECT 1 FROM DUAL</check-valid-connection-sql>
   </validation>
   <statement>
      <share-prepared-statements>false</share-prepared-statements>
   </statement>
</datasource>
```

For DB2, Oracle, and SQL Server, replace these with the appropriate driver details.

## Application Server Copy-to Locations

When the `deploy-webapp-``pro`` ` buildomatic target is executed, it copies the JDBC driver to the following default locations:

|          |                                    |
|----------|------------------------------------|
| Tomcat:  | `<tomcat>/lib`                     |
| JBoss:   | `<jboss>/standalone/deployments `  |
| Wildfly: | `<wildfly>/standalone/deployments` |
