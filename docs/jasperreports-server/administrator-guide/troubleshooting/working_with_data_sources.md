---
title: Working With Data Sources
description: "When adding a data source to JasperReports Server, several things can cause errors. Start by looking at the following general connectivity issues:"
---

# Working With Data Sources

When adding a data source to JasperReports Server, several things can cause errors. Start by looking at the following general connectivity issues:

-   Check that your database server is available and accepting TCP/IP connections from the host where JasperReports Server is installed.
-   Check in your RDBMS that the username and password you are using are correct and have access to the selected database.
-   Check for firewalls or network connectivity errors.

Many databases, including MySQL, also require the user grants to include the specific host from which connections are allowed. Otherwise, when testing the JDBC connection, a connection may not be allowed even though the username and password are correct. For more information, refer to the [MySQL documentation for setting up users](http://dev.mysql.com/doc/refman/5.1/en/adding-users.html).

An easy way to test connectivity from the server to the database with a particular user is to use a tool such as SQuirreL or another DB query tool to connect to the database from the host of your JasperReports Server instance.

## Logging JDBC Operations

You can enable additional logging to help you find the cause of the error. Set any or all of the following loggers in the server settings interface or in the `.../WEB-INF/log4j.properties` file:

-   `log4j.logger.com.jaspersoft.jasperserver.api.engine.jasperreports.service.impl.JdbcDataSourceService`
-   `log4j.logger.com.jaspersoft.jasperserver.api.engine.jasperreports.service.impl.`<br>
    `JndiJdbcDataSourceService`
-   `log4j.logger.com.jaspersoft.jasperserver.war.action.ReportDataSourceAction`
-   `log4j.logger.com.jaspersoft.commons.datarator.JdbcDataSet`
-   `log4j.logger.com.jaspersoft.jasperserver.war.common.JasperServerUtil`
-   `log4j.logger.com.jaspersoft.commons.semantic.dsimpl.JdbcDataSetFactory`
-   `log4j.logger.com.jaspersoft.commons.semantic.metaapi.impl.jdbc.BaseJdbcMetaDataFactoryImpl`
-   `log4j.logger.com.jaspersoft.jasperserver.war.validation.ReportDataSourceValidator`

## JDBC Drivers

JasperReports Server ships with drivers for several databases, as listed in the dialog for creating data sources. If the JDBC driver for your database is not included, the system administrator can easily upload the driver and use it immediately to access a data source.

## Database Permissions

When creating database users, you must ensure that they have the appropriate privileges to access data, as well as permission to connect from the server that JasperReports Server is running on.

-   The database user that you specify in your data source definition needs the privileges to run `SELECT` queries on the tables used in your reports. The server blocks any `DROP, INSERT, UPDATE`, and `DELETE` SQL commands through its SQL injection protection. In some cases, additional permissions may be required to execute stored procedures, depending on your configuration and needs.

-   If you accept the defaults during installation of JasperReports Server on Linux from an RPM using apt-get, rpm, or yum, the bundled PostgreSQL allows only the user who owns PostgreSQL to connect. Enter the following commands to connect:

    ``` text
    su - postgres
    psql -U postgres
    ```

-   Many databases, including MySQL, also require that the user permission name the specific host from which connections are allowed. Otherwise, when testing the JDBC connection, a connection may not be allowed even though the username and password are correct. For example, see the [MySQL documentation for setting up users](http://dev.mysql.com/doc/refman/5.1/en/adding-users.html).

A fairly easy way to test permissions and connectivity is to use a tool such as SquirrelSQL or another DB query tool to connect to the database from the same host as JasperReports Server and to run typical queries against your database.

## Unique JDBC Data Source Fields

When you choose a JDBC driver, the data source creation wizard displays the fields that are required for your database. In some cases, you may need to enter information that is unique to this type of JDBC data source. The following tables explain the field for the most common databases.

### Autonomous REST

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td><p>Field</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><strong>Authentication Method</strong></td>
<td><p>The authentication method for accessing the data source. Changing the authentication method requires you to configure the URL. The authentication method can be one of the following:</p>
<ul>
<li><code>none</code> - Does not use an authentication method for accessing the data source.</li>
<li><code>basic</code> - Uses a user ID and password for authentication Requires <code>user</code> and <code>password</code> properties in the URL.</li>
<li><code>HttpHeader</code> - Uses a security token for authentication. Requires <code>user</code> and <code>SecurityToken</code> properties in the URL.</li>
<li><code>UrlParameter</code> - Uses a security token and URL parameter for authentication. The URL requires <code>user</code>, <code>SecurityToken</code>, and <code>AuthParam</code> properties.</li>
<li><code>OAuth2</code> - Uses OAuth 2.0 for authentication. There are multiple ways to use OAuth 2.0. Jaspersoft recommends using the official documentation for more information.</li>
<li><code>Custom</code> - Uses the custom token-based authentication defined in the config file. Jaspersoft recommends using the official documentation for more information.</li>
</ul>
<p>By default, the authentication method is set to <code>none</code>.</p></td>
</tr>
<tr>
<td><strong>Path to Config File</strong></td>
<td>The full path to the configuration file for the data source.</td>
</tr>
</tbody>
</table>

### Cassandra

|  |  |
|----|----|
| Field | Description |
| **Key Space** | The name of the key space that acts as the data store for the Cassandra data source. |

### Google BigQuery

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td><p>Field</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><strong>Project ID</strong></td>
<td>The unique identifier for your Google Cloud project.</td>
</tr>
<tr>
<td><strong>Dataset ID</strong></td>
<td>The unique BigQuery dataset name.</td>
</tr>
<tr>
<td><strong>Google Service Account Email Address</strong></td>
<td>The email address associated with the BigQuery service account.</td>
</tr>
<tr>
<td><strong>Private Key Path</strong></td>
<td><p>The full path to the <code>.json</code> key file used to authenticate the service account email address.</p>
<p>**Note** The `.p12` files are not supported.</p></td>
</tr>
</tbody>
</table>

### Impala

|               |                                   |
|---------------|-----------------------------------|
| Field         | Description                       |
| `Schema Name` | Name of the Impala Schema object. |

### Oracle

|           |                                      |
|-----------|--------------------------------------|
| Field     | Description                          |
| `Service` | Name of the Oracle database service. |

### Salesforce

|  |  |
|----|----|
| Field | Description |
| `Security Token` | A case-sensitive alphanumeric key is used in combination with a password to access the Salesforce data source. |
| `Maximum Number of Web Service Calls` | The maximum number of times JasperReports Server calls the Salesforce web service in a 24-hour period. Set to `0` for unlimited calls. |

## JDBC Database URLs

When you choose a JDBC driver, the data source creation wizard prompts you for the elements of the URL that are required for your database. In some cases, you may need to add certain arguments to the JDBC URL. Ensure that the database URL you entered when defining your JDBC data source is consistent with what is required for your specific database and database driver. The following table gives the default URLs and port numbers and examples of optional arguments supported by the most common databases:

| Database | Default JDBC Database URL |
|----|----|
| PostgreSQL | `jdbc:postgresql://<host>:5432/<db-name>` |
| MySQL and MariaDB | `jdbc:mysql://<host>:3306/<db-name>?tinyInt1isBit=false` |
| Oracle | `jdbc:oracle:thin:@<host>:1521:ORCL` |
| SQL Server | `jdbc:sqlserver://<host>:1433;databaseName=<db-name>;sendTimestampEscapeAsString=false;encrypt=true;trustServerCertificate=true;sslProtocol=TLSv1.2` |
| IBM DB2 | `jdbc:db2://<host>:50000/<db-name>:driverType=4;currentSchema=<DB-SCHEMA>;` |
| Cassandra | `jdbc:cassandra://<host>:9042;DefaultKeyspace=` |
| RedShift | `jdbc:redshift://<host>:5439/dev` |
| Hive | `jdbc:hive2://host:10000/` |
| SparkSQL | `jdbc:datadirect:sparksql://localhost:10000;TransactionMode=ignore` |
| Impala | `jdbc:impala://host:21050/default` |

## Enabling the JDBC Driver for ElasticSearch Data Sources

The ElasticSearch JDBC driver is not enabled by default due to certain limitations. If you want to use the driver, you can modify the `.../WEB-INF/applicationContext-webapp.xml` file to make it active.

!!! note

    Be aware of the following issues when using an ElasticSearch data source:

    -   It is not supported for JBoss or Wildfly app servers.

    -   Table joins are not supported.

    -   There may be issues with calculated fields, including more complex aggregation functions, using `*` as a special character, and the use of calculated fields in crosstabs and charts.

    -   When an ElasticSearch data source is used in a virtual data source, the virtual data source only displays the Base tables of the ElasticSearch data source, not the views, when used in a domain.

To enable the Jaspersoft JDBC drivers for ElasticSearch data sources

1.  Open the file `.../WEB-INF/applicationContext-webapp.xml` for editing.

2.  Locate the `jdbcTibcoConnectionMap` bean and find the following lines for the inactive ElasticSearch JDBC driver:

    ``` text
    <!--  entry key="elastic_search">
       ...
    </entry -->
    ```

3.  Modify the lines as follows to enable the JDBC driver in JasperReports Server:

    ``` xml
    <entry key="elastic_search">
       ...
    </entry>
    ```

4.  Save the file.

5.  Upload the JDBC driver separately and restart JasperReports Server.

## JNDI Services on Apache Tomcat

If you have trouble with a JNDI connection, you need to look at the JNDI definition for your database on your application server. This section gives common issues with JNDI definitions on Apache Tomcat connecting to MySQL. If you use a different application server or database server, refer to its documentation.

A JNDI connection on Tomcat is defined in two different files. Make sure both have the following information:

-   `<tomcat>/webapps/jasperserver/META-INF/context.xml`

``` xml
<Resource name="jdbc/<db-name>" auth="Container" type="javax.sql.DataSource"
maxTotal="100" maxIdle="30" maxWaitMillis="10000"
username="<db-user>" password="<db-user-password>"
driverClassName="org.postgresql.Driver"
validationQuery="SELECT 1" testOnBorrow="true"
url="jdbc:mysql://<host>:3306/<database>?autoReconnect=true&amp;autoReconnect
ForPools=true"/>
```

-   `<tomcat>/webapps/jasperserver/WEB-INF/web.xml`

``` xml
<resource-ref>
<description>JNDI Example</description>
<res-ref-name>jdbc/<db-name></res-ref-name>
<res-type>javax.sql.DataSource</res-type>
<res-auth>Container</res-auth>
</resource-ref>
```

Also check the following points:

-   Ensure that the driver for your database connection is in the `<tomcat>/lib` folder.
-   Ensure the database user has the privileges to run `SELECT` queries on the tables used in your reports. In some cases, additional permissions may be required to execute stored procedures, depending on your configuration and needs. For more information, see [Database Permissions](working_with_data_sources.md).
-   If you installed JasperReports Server from a WAR file, Tomcat may have created a separate copy of `context.xml` in `<tomcat>/conf/Catalina/Localhost/jasperserver.xml`. See the corresponding section in the troubleshooting appendix of the JasperReports Server Installation Guide.
-   See the [Apache Tomcat documentation for JNDI data sources](http://tomcat.apache.org/tomcat-9.0-doc/jndi-datasource-examples-howto.html).
-   For Oracle databases, you may need to specify additional parameters in the `context.xml` file. For example, to support in Oracle, add the following line:

``` properties
driverClassName="oracle.jdbc.OracleDriver"
validationQuery="SELECT 1 FROM dual"
accessToUnderlyingConnectionAllowed="true"
```

## JNDI Services on JBoss

Follow these steps to configure JasperReports Server to use JNDI data sources with JBoss:

1.  Add a new JNDI service user to `<jboss>/standalone/deployments/jasperserver.war/WEB-INF/js-jboss7-ds.xml`. For example:

``` xml
<datasource jta="false" jndi-name="java:/jdbc/sample_db" pool-name="sample_db" enabled="true" use-ccm="false">
        <connection-url>jdbc:postgresql://localhost:5432/sample_db</connection-url>
        <driver>postgresql-9.4-1210.jdbc41.jar</driver>
        <security>
            <user-name>postgres</user-name>
            <password>postgres</password>
        </security>
        <pool>
            <min-pool-size>5</min-pool-size>
            <max-pool-size>50</max-pool-size>
            <prefill>true</prefill>
    </pool>
    <validation>
            <validate-on-match>false</validate-on-match>
            <background-validation>false</background-validation>
            <check-valid-connection-sql>SELECT 1</check-valid-connection-sql>
        </validation>
        <statement>
            <share-prepared-statements>false</share-prepared-statements>
        </statement>
    </datasource>
```

## JNDI Services on WebLogic

Follow these steps to configure JasperReports Server to use JNDI data sources with WebLogic:

1.  Append the following definition to the `<reference-descriptor>` node of `.../WEB-INF/weblogic.xml`:

    ``` xml
    <resource-description>
        <res-ref-name>TestDatabase</res-ref-name>
        <jndi-name>jdbc/testDatabase</jndi-name>
    </resource-description>
    ```

2.  Append the following definition to `.../WEB-INF/web.xml`:

    ``` xml
    <resource-ref>
        <description>TestDatabase database</description>
        <res-ref-name>TestDatabase</res-ref-name>
        <res-type>javax.sql.DataSource</res-type>
        <res-auth>Container</res-auth>
    </resource-ref>
    ```

3.  In the **WebLogic Admin Console**, create a JNDI data source, in this example its JNDI name would be **TestDatabase**.<br>
    Ensure that the database user in your JNDI definition has the privileges to run `SELECT` queries on the tables used in your reports. In some cases, additional permissions may be required to execute stored procedures, depending on your configuration and needs. For more information, see [Database Permissions](working_with_data_sources.md).

4.  Restart the `jasperserver` instance using the **WebLogic Admin Console**.

## Creating a Data Source on SQL Server Using Windows Authentication

If your database is Microsoft SQL Server and you use Windows Authentication (also called Integrated Security), use the following procedure to create a data source.

1.  Download the latest JDBC driver for your version of Microsoft SQL Server. For example [download Microsoft SQL Server JDBC Driver 6.4](https://www.microsoft.com/en-us/download/details.aspx?id=56615).<br>

    !!! note

        To find the latest version of your Microsoft SQL Server driver, see the [Microsoft JDBC Driver for SQL Server Support Matrix](https://docs.microsoft.com/en-us/sql/connect/jdbc/microsoft-jdbc-driver-for-sql-server-support-matrix).

        For information about downloading and installing Microsoft SQL Server drivers, see the [Microsoft JDBC Driver for SQL Server](https://docs.microsoft.com/en-us/sql/connect/jdbc/microsoft-jdbc-driver-for-sql-server) page.

2.  Download and run the self-extracting executable: **sqljdbc_6.4.0.0_enu.exe**

3.  Open the extracted folder `sqljdbc_6.4\enu\auth\x64` and copy the file `sqljdbc_auth.dll` to the folder your app server automatically searches for DLLs.<br>
    For Tomcat, this is the `<tomcat>\bin` folder.

4.  Open the extracted folder `sqljdbc_6.4\enu` and copy `mssql-jdbc-6.4.0.jre8.jar` to the folder to let your app server automatically searches for jars. For Tomcat, this is the `<tomcat>\lib` folder.

5.  Restart your app server.

6.  Log into JasperReports Server as an administrator.

7.  Select **Create &gt; Data Source** from the main menu.

8.  In the **Type** field, select **JDBC Data Source**. The page refreshes to show the fields necessary for a JDBC data source.

9.  Enter a name and optional description for your data source.

10. From the dropdown field, select `com.microsoft.sqlserver.jdbc.SQLServerDriver`.

11. Enter the database hostname and database name of your SQL Server instance.

12. In the URL field, add the following string to the end of the generated URL:<br>
    `;integratedSecurity=true`

13. In the **Username** field, enter any non-blank string you want, for example **none**.

14. In the **Password** field, enter any non-blank string you want, for example **none**.

15. Set the **Time Zone** and **Save Location** fields if necessary.

16. Click **Test Connection** and verify that the connection works.

17. Click **Save** to save the data source in the repository.

## Upgrading Bean Data Sources

There was a change in the Spring configuration for JasperReports Server 6.0 that changes how some of the existing Spring beans are made accessible for use by other beans. This can break existing custom data sources. This change specifically affects beans that implement the interface `ReportDataSourceServiceFactory`.

Prior to release 6.0, if the code in JasperReports Server accessed a bean of this type, it would get the actual instance of the Spring bean as configured in the Spring XML file, and it could be cast to the concrete class. In 6.0 and later, these beans were intercepted to implement the profile attributes feature, and instead of seeing the actual instance, other code would see a dynamic proxy instead of the actual bean.

Dynamic proxies are a Java feature, which allows classes to be generated at run time that implement any interface that can be loaded on the classpath. The resulting object can be cast to any of those interfaces, but doesn't correspond to any concrete class. For more information:

<http://www.javaworld.com/article/2076233/java-se/explore-the-dynamic-proxy-api.html>

Since proxies can only represent interfaces, existing code that tries to cast the bean to a concrete class will break. Casting is usually done to get access to methods on a more specific class or interface. As long as the code is not casting the bean to a concrete class, it will work, so there are two ways to get around this problem:

-   If the code needs to access methods on an existing interface, do a cast to that interface, or inject the property using the existing interface, so no cast is needed.
-   If the code needs to access methods that are not on an existing interface, simply create an interface with the methods needed, and have the target object implement that interface.

For example, let us say you have a bean with id `myBean` that needs to access the `jdbcDataSourceServiceFactory`, configured as follows:

``` xml
<bean id="jdbcDataSourceServiceFactory" class="com.jaspersoft.jasperserver.
api.engine.jasperreports.service.impl.JdbcReportDataSourceServiceFactory">
...
</bean>
```

Where `myBean` has the following Spring configuration:

``` xml
<bean id="myBean" class="example.MyBean">
    <property name="jdbcDSSF" ref="jdbcDataSourceServiceFactory"/>
```

The following code worked before but will now cause an error:

``` java
public class MyBean {
  private ReportDataSourceServiceFactory jdbcDSSF;
  public ReportDataSourceServiceFactory getJdbcDSSF() {
    return jdbcDSSF;
  }
  // before 6.0, was called by Spring with the actual bean
  // 6.0 and after, is called with a dynamic proxy
  public void setJdbcDSSF(ReportDataSourceServiceFactory jdbcDSSF) {
    this.jdbcDSSF = jdbcDSSF;
  }
  public void doSomething() {
    // this code used to work, but now it will break
    ((JdbcReportDataSourceServiceFactory) jdbcDSSF).createService();
    ((JdbcReportDataSourceServiceFactory) jdbcDSSF).doSomethingElse();
  }
}
```

Because the first call is a method that is part of the `ReportDataSourceServiceFactory`, the cast is unnecessary; to fix it, just leave it out:

``` text
    jdbcDSSF.createService();
```

In this example, `JdbcReportDataSourceServiceFactory` has a method called `doSomethingElse()`. This method is not part of any interface, but you can create an interface that includes it:

``` java
public interface MyDSSF extends ReportDataSourceServiceFactory {
   public void doSomethingElse();
}
```

`JdbcReportDataSourceServiceFactory` would need modification so that it implements this new interface:

``` text
public JdbcReportDataSourceServiceFactory implements MyDSSF {
....
}
```

You do not have to change the declaration in `MyBean` because Spring generates a dynamic proxy implementing `MyDSSF`, but if you change the declaration, the code will be easier to understand because no casts will be necessary:

``` java
public class MyBean {
  private MyDSSF jdbcDSSF;
  public MyDSSF getJdbcDSSF() {
    return jdbcDSSF;
  }
  // called with a dynamic proxy which implements all needed interfaces
  public void setJdbcDSSF(MyDSSF jdbcDSSF) {
    this.jdbcDSSF = jdbcDSSF;
  }
  public void doSomething() {
    // no need to cast
    jdbcDSSF.createService();
    jdbcDSSF.doSomethingElse();
  }
}
```

## Redundant JSON Data Adapter Requests During Parameter Initialization

The JSON data adapter triggered multiple HTTP calls using default parameter values instead of a single call using dynamic parameters passed from input controls.

To resolve this, default parameter evaluation now occurs independently of the data adapter.

To restore the previous behavior where the parameter default values depend on the data adapter, the `net.sf.jasperreports.parameter.defaults.evaluator.prepares.data` property can set to `true` at the report level or globally in the `WEB-INF/classes/jasperreports.properties` file.
