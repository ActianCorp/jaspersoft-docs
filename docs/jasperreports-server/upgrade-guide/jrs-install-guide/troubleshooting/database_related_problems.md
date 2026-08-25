---
title: Database-related Problems
description: Install/upgrade process permissions
---

# Database-related Problems

## Database Privileges Required By JasperReports Server

Install/upgrade process permissions

The JasperReports Server installation/upgrade processes and the repository database user need the following privileges to install and initialize the `jasperserver` repository database.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Database Component</th>
<th>Permissions Required</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>databases</p></td>
<td><p><code>CREATE</code></p>
<p><code>DROP</code></p></td>
</tr>
<tr>
<td><p>tables</p>
<p>indexes</p>
<p>constraints</p></td>
<td><p><code>CREATE</code></p>
<p><code>ALTER</code></p>
<p><code>DROP</code></p></td>
</tr>
<tr>
<td><p>data records</p></td>
<td><p><code>INSERT</code></p>
<p><code>UPDATE</code></p>
<p><code>DELETE</code></p></td>
</tr>
</tbody>
</table>

If you are upgrading in a restricted environment, your database administrator may need to give you temporary admin permissions for the upgrade. For example, if you are using PostgreSQL for your database, the database admin may use one of the following workarounds:

- Add administrator credentials in the `default_master.properties` file prior to upgrade and then replace them with jasperadmin credentials after upgrade.

- Prior to upgrade, grant `CREATE` and `DROP` permissions at the database server level for the jasperadmin user, then revoke those permissions after successful upgrade.

## Database Connectivity Errors

The most common problems encountered with a new JasperReports Server instance are database configuration problems. The connection may fail because the application server cannot find the driver for the data source. For example, in a default installation of JasperReports Server, Tomcat looks for data source drivers in `<js‑install>/apache-tomcat/lib`. If the driver's in a different location, put a copy of the driver in this directory and restart Tomcat.

### Testing the Database Connection

The simplest database configuration problem is an incorrect username or password. If you encounter database problems on startup or login, check the username and password by logging directly into your RDBMS as described below.

You can connect to your database using the database configuration settings in JasperReports Server. This validates the database hostname, port, username, and password.

If you are having trouble logging into JasperReports Server on the login page, check the existing users and passwords in the `jasperserver.JIUser` table.

### Logging into PostgreSQL

Run the PostgreSQL client from the command line and try to connect to the database. For example:

`psql -U postgres jasperserver`

### Logging into MySQL

Run the MySQL client from the command line and try to log in directly as the `root` user, for example:

`<mysql>/bin/mysql -u root -p`

You are prompted for the password of the user that you specified on the command line.

### Logging into Oracle

Start SQL\*Plus and try logging into Oracle directly. Use the password specified during installation to log in as each of these users:

- `jasperserver`: schema user for the JasperReports Server metadata.

- `sugarcrm`: schema user for the SugarCRM sample data.

- `foodmart`: schema user for the foodmart sample data.

### Logging into Microsoft SQL Server

Run the `sqlcmd` and try logging into MSSQL Server directly. For example:

`sqlcmd -S localhost\jasperserver -d jasperserver -U jasperadmin -P password`

### Connectivity Errors with SQL Server Driver

If you are using the SQL Server driver and have configured default_master.properties as described in [SQL Server Example](../../../installation-guide/additional/jdbc-driver.md), you'll see connection errors if you uncommented the following line:

``` bash
# admin.jdbcUrl=jdbc:sqlserver://${dbHostOrInstance};SelectMethod=cursor
```

Make sure that this line is commented.

## Case-sensitive Collation in SQL Server

Microsoft SQL Server does not support standalone case-sensitive collation. When collation is case-sensitive SQL Server also treats column and table names as case-sensitive. This can happen when setting a locale that includes case‑sensitive collation. In this case you may see an error such as the following.

``` text
[sql] Failed to execute:
INSERT INTO JIUserRole (userId,roleId) select u.id, r.id
from JIUser u, JIRole r
where u.username = \'anonymousUser\' and r.roleName = \'ROLE_ANONYMOUS\'
  [sql] com.microsoft.sqlserver.jdbc.SQLServerException: Invalid column name \'roleName\'
```

Use a different locale or remove the case-sensitivity setting.

## Configuring the Oracle or SQL Server Driver for NTLM Authentication

To avoid storage of the user and password values for the database, you can configure the Oracle or SQL Server driver to use Windows authentication. To do this, copy the NTLM authentication DLLs for your database from the `<js-install>\jasperserverwar\tools directory` directory to a location in your Windows system path (defined by the PATH environment variable) and onfigure them as described in the instructions for your database:

- <https://blogs.oracle.com/blogbypuneeth/post/steps-to-configure-kerberos-spnego-ntlm-authentication-with-weblogic-server-running-on-oracle-jdk->
- <https://learn.microsoft.com/en-us/sql/connect/jdbc/using-ntlm-authentication-to-connect-to-sql-server?view=sql-server-ver16>

## Maximum Packet Size in MySQL

If you are upgrading or importing into a MySQL database and your repository contains large objects like images, you may see an error like this:

`ERROR 1153 (08S01): Got a packet bigger than 'max_allowed_packet' bytes`

The default `max_allowed_packet` on the MySQL server is 1M (one Megabyte = 1,048,576 bytes). The most effective fix is to change this value in the server configuration to accommodate the largest resource stored in your repository. The server configuration file is typically named my.cnf (or my.ini) and located in the MySQL root directory, but this may vary. Change the configuration setting to a larger value, for example:

`max_allowed_packet = 16M`

For more information, see <http://dev.mysql.com/doc/refman/5.0/en/packet-too-large.html>.

After changing this value, restart the MySQL server. Then perform the upgrade or import step again.

### Connection reset by peer MySQL Error

If you are using the MariaDB JDBC driver to connect to the MySQL database and get an error such as the following:

``` text
Could not send query:
Connection reset by peer: socket write error
```

This message refers to the maximum packet size error described above. Follow those instructions.

## Case Sensitivity for Table and Column Names

In some databases, table names are case-sensitive and “customer” and “Customer” are two different tables.

If you are using a case-sensitive database for JasperReports Server, the table names specified in query strings in the JRXML file of a saved report must match the table names used in the database. A mismatch when transferring data from one database to another may cause the capitalization of table names to change.

In Windows MySQL, table and column names are not case-sensitive.

In Linux MySQL, table and column names are case-sensitive. You can configure Linux MySQL to be non-case-sensitive by setting the configuration parameter `lower_case_table_names` to `1` in the my.ini or my.cnf file. For more information, search the MySQL documentation for a section about identifier case sensitivity.

Table and column names in Oracle and PostgreSQL are case-sensitive.

## PostgreSQL: Job Scheduling Error

If the Quartz settings in the PostgreSQL database are not updated to specify the driver delegate class specific to PostgreSQL, then you get errors when you try to run a scheduled report.

The errors look like this:

``` text
Error while fetching Quartz runtime information
org.quartz.JobPersistenceException: Couldn't obtain triggers: Bad value for type int
org.postgresql.util.PSQLException: Bad value for type int
```

If you see this error, check your Quartz properties file in the following location:

`<tomcat>/webapps/jasperserver-``pro`` /WEB-INF/js.quartz.properties`

Make sure that the following property does not have the standard driver delegate, but instead has the PostgreSQL-specific driver delegate. It should look like the following for PostgreSQL:

`quartz.delegateClass=org.quartz.impl.jdbcjobstore.PostgreSQLDelegate`

## Performance Issues with Oracle JDBC Queries

Setting the Oracle database localization option `defaultNChar` to `true` can substantially impact the performance of JDBC queries. When `defaultNChar` is set to `true`, the database implicitly converts all `CHAR` data to `NCHAR` when you access `CHAR` columns. If you do not need to support UTF-8 for your Oracle database, you can omit this setting.

The option you need and how to set it depends on your version of Java, your application server, and how it is deployed. For information about changing a JVM option setting for your particular environment, see your application server documentation.

To change this setting on Windows, enter a command like this at the command line:

`set JAVA_OPTS=%JAVA_OPTS% -Doracle.jdbc.defaultNChar=false`

To change this setting on Linux, enter a command like this at the command line:

`export JAVA_OPTS="$JAVA_OPTS -Doracle.jdbc.defaultNChar=false"`

## Using an Oracle Service Name

If your Oracle database is configured to use a service name instead of an Oracle system identifier (SID), set up the service name by updating your default_master.properties file before using buildomatic:

`<js-install>/buildomatic/default_master.properties`

In default_master.properties, uncomment the `serviceName` property and enter your Oracle service name, for example:

`serviceName=ORCL`

When you are using an Oracle service name, make sure that you do not set the SID or dbPort in the default_master.properties file.

## Error Running a Scheduled Report

If you run a scheduled report and save it as HTML or RTF, the resulting report may be quite large. If you are running MySQL and get the error shown here, the problem may be the default size of the MySQL blob datatype.

``` text
JDBC exception on Hibernate data access
org.hibernate.exception.GenericJDBCException: could not insert
```

You can increase the size of this datatype by updating your my.ini or my.cnf MySQL configuration file with the following setting:

`max_allowed_packet=32M`

## Error Running a Report

If you can log into JasperReports Server but encounter an error when running a report, browse the repository to identify and resolve the problem.

One common problem with an individual report is the data source. To validate a data source connection:

1.  Log into JasperReports Server as a user with administrative permissions and locate the report unit that returns errors.

2.  Select the report and click the **Edit** button in the toolbar and identify the data source on the fourth edit page.

3.  Edit the data source in the repository and check its settings.

4.  Click the **Test Connection** button.

    If the connection fails, perhaps the application server can't find the driver for the data source. For example, in a default installation of JasperReports Server, Tomcat looks for data source drivers in `<js‑install>/apache-tomcat/lib`.

5.  Test your report. If it still returns errors, edit the data source again and try checking other values, like the port used by the database.

## Save Error with DB2 Database

When the DB2 database is your repository database, you may get errors when saving longer strings (over 50 characters) to data entry fields in the UI. For example, saving a resource with a name over 50 characters may cause an error like this:

``` text
Expected status code is 200, but was 400. Response body contained:
An unexpected exception has occurred
```

The problem here is that DB2 handles UTF-8 characters differently than other Jaspersoft certified databases. When DB2 is used as the repository database, it limits the number of characters that can be entered in UI fields. The database columns holding these strings need to be made larger.

## BeanDefinitionStoreException with DB2 Driver

When using the DB2 driver, you need to add properties manually todefault_master.properties, or you get an error like the following.

``` text
[java] Resource name: applicationContext-virtual-data-source.xml
     [java] org.springframework.beans.factory.BeanDefinitionStoreException:
Invalid bean definition with name 'dataSource' defined in file
[/opt/JasperReports-Server-10.1.0-src/jasperserver/buildomatic/conf_source/iePro/applicationContext-export-config.xml]:
Could not resolve placeholder 'dbPort' in string value
```

Add the following properties to your `default_master.properties`, setting the correct values for your installation:

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

## JDBC Driver Loading Error on Import/Export from WebLogic or WebSphere

If you are using WebLogic or WebSphere and want to run import/export from the command line, you need to manually copy the JDBC driver to the same location as the import/export scripts. If you have not copied these files, you may encounter the following error:

``` text
Cannot load JDBC driver class <database class>
```

To fix this error, copy your database driver to the correct location:

|       |                                                                 |
|-------|-----------------------------------------------------------------|
| from: | `<js-install>\buildomatic\conf_source\db\<your_database>\jdbc\` |
| to:   | `<js-install>\buildomatic\conf_source\iePro\lib`                |
