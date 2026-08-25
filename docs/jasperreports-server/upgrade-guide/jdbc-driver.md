---
title: Working With JDBC Drivers
description: This section describes how to set up your installation to use a driver other than the default driver.
---

# Working With JDBC Drivers

This section describes how to set up your installation to use a driver other than the default driver.

## Open Source JDBC Drivers

For open source JDBC drivers, buildomatic is set up to use a single default driver. If you want to use a driver other than the default driver, you can modify the buildomatic property files that determine the default JDBC driver.

The buildomatic JDBC driver property files are set up to point to a specific driver jar. This allows for multiple driver jar files in the same `buildomatic/conf_source/db/<dbType>/jdbc` folder. During the installation procedure only the default driver jar is copied to your application server.

If you want to use a newer JDBC driver version or a different JDBC driver, you can modify the buildomatic properties seen in your `default_master.properties` file.

### PostgreSQL Example

The `buildomatic/conf_source/db/postgresql/jdbc` folder contains the following driver file:

`postgresql-42.2.20.jar`

If, for instance, you want to change the default driver used by PostgreSQL from type jdbc4 to jdbc3, edit your `default_master.properties` file:

|                  |                                                          |
|------------------|----------------------------------------------------------|
| Overlay upgrade: | `<overlay-folder>/buildomatic/default_master.properties` |
| Other upgrade:   | `<js-install>/buildomatic/default_master.properties`     |

Uncomment and change:

`# maven.jdbc.version=42.2.5`

To:

`maven.jdbc.version=9.2-1002.jdbc3`

When you next run a buildomatic command, such as deploy-webapp-pro , the jdbc3 driver will be copied to your application server.

### MySQL Example

The `buildomatic/conf_source/db/mysql/jdbc` folder contains this driver file:

`mariadb-java-client-2.5.3.jar`

If, for instance, you want to use a JDBC driver built and distributed by the MySQL project, such as `mysql-connector-java-5.1.43-bin.jar`, you first need to download the driver from the MySQL Connector/J download location:

`https://dev.mysql.com/downloads/connector/j/`

Next, change your buildomatic configuration properties to point to this new driver.

Edit your `default_master.properties` file:

|                  |                                                          |
|------------------|----------------------------------------------------------|
| Overlay upgrade: | `<overlay-folder>/buildomatic/default_master.properties` |
| Other upgrade:   | `<js-install>/buildomatic/default_master.properties`     |

Uncomment and change:

`# jdbcDriverClass=com.mysql.jdbc.Driver`

`# jdbcDataSourceClass=com.mysql.jdbc.jdbc2.optional.MysqlConnectionPoolDataSource`

`# maven.jdbc.groupId=mysql`

`# maven.jdbc.artifactId=mysql-connector-java`

`# maven.jdbc.version=5.1.43-bin`

To:

`jdbcDriverClass=com.mysql.jdbc.Driver`

`jdbcDataSourceClass=com.mysql.jdbc.jdbc2.optional.MysqlConnectionPoolDataSource`

`maven.jdbc.groupId=mysql`

`maven.jdbc.artifactId=mysql-connector-java`

`maven.jdbc.version=5.1.43-bin`

## Installing Database Vendor JDBC Drivers

JasperReports Server no longer includes JDBC drivers for the following commercial databases:

- DB2
- Oracle
- SQL Server

You can download the driver supplied by the database vendor as described below. To do this, you must first obtain and install the driver you want, then copy that driver into buildomatic.

### Oracle Example

1.  Copy your Oracle driver to the following directory:

|  |  |
|----|----|
| Overlay upgrade: | `<overlay-folder>/buildomatic/conf_source/db/oracle/jdbc/` |
| Other upgrade: | `<js-install>/buildomatic/conf_source/db/oracle/jdbc/` |

``` bash
# 1) Setup Standard Oracle JDBC Driver
#
# Uncomment and modify the value to native
jdbcDriverMaker=native
#
# Uncomment and modify the value in order to change the default
# 1a) Driver will be found here: <path>/buildomatic/conf_source/db/oracle/native.jdbc
#
maven.jdbc.groupId=oracle
maven.jdbc.artifactId=ojdbc6
maven.jdbc.version=11.2.0.3
```

### SQL Server Example

1.  Copy your SQL Server driver to the following directory:

    |  |  |
    |----|----|
    | Overlay upgrade: | `<overlay_folder>/buildomatic/conf_source/db/sqlserver/jdbc` |
    | Other upgrade: | `<js_install>/buildomatic/conf_source/db/sqlserver/jdbc` |

2.  Change to the `<js_install>/buildomatic` directory and open `default_master.properties` in a text editor.

3.  Go to the Additional Settings section in this file.

4.  Go to the first setup item, Setup Standard SQL Server JDBC Driver.

5.  Uncomment the required properties and enable your driver. The following example shows how to set up `default_master.properties` to point to a driver named `mssql-jdbc-6.4.0.jre8.jar`:

    ``` bash
    # 1) Setup Standard SQLServer JDBC Driver
    #
    # Uncomment and modify the value to native
    jdbcDriverMaker=native
    #
    # Uncomment and modify the value in order to change the default
    # Driver will be found here: <path>/buildomatic/conf_source/db/sqlserver/native.jdbc
    #
    maven.jdbc.groupId=sqlserver
    maven.jdbc.artifactId=sqljdbc
    maven.jdbc.version=6.4.0.jre8
    ```

6.  Save the `default_master.properties` file.

### DB2 Example

1.  Copy your DB2 driver to the following directory:

    |                  |                                                        |
    |------------------|--------------------------------------------------------|
    | Overlay upgrade: | `<overlay_folder>/buildomatic/conf_source/db/db2/jdbc` |
    | Other upgrade:   | `<js_install>/buildomatic/conf_source/db/db2/jdbc`     |

2.  Change to the `<js_install>/buildomatic directory` and open `default_master.properties` in a text editor.

3.  Go to the Additional Settings section in this file.

4.  Go to the first setup item, Setup Standard DB2 JDBC Driver.

5.  Uncomment the required properties and enable your driver.

    ``` bash
    # 1) Setup Standard DB2 JDBC Driver
    #
    # Uncomment and modify the value to native
    jdbcDriverMaker=native
    #
    # Uncomment and modify the value in order to change the default
    # Driver will be found here: <path>/buildomatic/conf_source/db/db2/native.jdbc
    #
    maven.jdbc.groupId=ibm
    maven.jdbc.artifactId=db2jcc
    maven.jdbc.version=9.7
    ```

6.  Add the following additional properties, setting the correct values for your installation. For example:

    ``` properties
    db2.driverType=4
    db2.fullyMaterializeLobData=true
    db2.fullyMaterializeInputStreams=true
    db2.progressiveStreaming=2
    db2.progressiveLocators=2
    dbPort=50000
    js.dbName=JSPRSRVR
    sugarcrm.dbName=SUGARCRM
    foodmart.dbName=FOODMART
    ```

7.  Save the `default_master.properties` file.
