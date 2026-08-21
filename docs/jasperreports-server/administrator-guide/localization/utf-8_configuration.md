---
title: UTF-8 Configuration
description: "JasperReports Server uses UTF-8 (8-bit Unicode Transformation Format) character encoding. If your database server or application server uses a different character encoding form, you may have to..."
---

# UTF-8 Configuration

JasperReports Server uses UTF-8 (8-bit Unicode Transformation Format) character encoding. If your database server or application server uses a different character encoding form, you may have to configure them to support UTF-8. This section provides information for configuring the character encoding for several application servers and database servers. If you use a different application server or database, and its default character encoding isn't UTF-8, you may need to make similar updates to support certain locales. For more information, refer to the documentation for your application server or database.

## Java Options

Make sure that your Java environment is set to support UTF-8. You can set this option as follows:

|         |                                                      |
|---------|------------------------------------------------------|
| Linux   | `export JAVA_OPTS="$JAVA_OPTS -Dfile.encoding=UTF-8` |
| Windows | `set JAVA_OPTS=%JAVA_OPTS% -Dfile.encoding=UTF-8`    |

You may see an error in a report that uses Unicode encoding if the `-Dfile.encoding` option is not set to `UTF-8`.

## Tomcat

By default, Tomcat uses ISO-8859-1 (ISO Latin 1) character encoding for URIs, which is sufficient for Western European locales, but does not support many locales in other parts of the world.

If you plan to support locales that Latin 1 does not support, you must change Tomcat's URI encoding format.

!!! note

    If you chose the instance of Tomcat that is bundled with the installer, you don't need to make this change. The bundled Tomcat is preconfigured to support UTF-8. If you installed the WAR file distribution with your own instance of Tomcat and want to support UTF-8, follow this procedure.

To configure Tomcat to support UTF-8

1.  Open the `conf/server.xml` file and locate the following code:

```
<!-- Define a non-SSL HTTP/1.1 Connector on port 8080 -->
<Connector>
    port="8080" maxHttpHeaderSize="8192"
    maxThreads="150" minSpareThreads="25" maxSpareThreads="75"
    enableLookups="false" redirectPort="8443" acceptCount="100"
    connectionTimeout="20000" disableUploadTimeout="true"
</Connector>
```

2.  At the end of this section, insert the following line before the closing tag:

```
URIEncoding="UTF-8"
```

3.  For example, after your changes, the section might read:

```
<!-- Define a non-SSL HTTP/1.1 Connector on port 8080 -->
    <Connector>
    port="8080" maxHttpHeaderSize="8192"
    maxThreads="150" minSpareThreads="25" maxSpareThreads="75"
    enableLookups="false" redirectPort="8443" acceptCount="100"
    connectionTimeout="20000" disableUploadTimeout="true"
    URIEncoding="UTF-8"
</Connector>
```

4.  Save the file.
5.  Restart Tomcat.

## PostgreSQL

JasperReports Server requires PostgreSQL to use UTF-8 character encoding for the database that stores its repository as well as for data sources. A simple way to meet the requirement is to create the database with a UTF-8 character set. For example, enter the following command:

```
create database jasperserver encoding='utf8';
```

## MySQL

By default, MySQL uses ISO-8859-1 (ISO Latin 1) character encoding. However, JasperReports Server requires MySQL to use UTF-8 character encoding for the database that stores its repository as well as for data sources. The simplest way to meet the requirement is to create the database with a UTF-8 character set. For example, enter the following command:

```
create database jasperserver character set utf8;
```

To support UTF-8, the MySQL JDBC driver also requires that the `useUnicode` and `characterEncoding` parameters be set as in this startup URL:

```
url="jdbc:mysql://localhost:3306/jasperserver?useUnicode=true&characterEncoding=UTF-8"
```

If the MySQL database is a JNDI data source managed by Tomcat, such as the JasperReports Server repository database, the parameters can be added to the JDBC URL in `.../META-INF/context.xml`. The following is a sample resource definition from that file:

```
<Resource name="jdbc/jasperserver" auth="Container" type="javax.sql.DataSource"
    maxTotal="100" maxIdle="30" maxWaitMillis="10000"
    username="root" password="password" driverClassName="com.mysql.jdbc.Driver"
    url="jdbc:mysql://localhost/jasperserver?useUnicode=true&amp;characterEncoding=UTF-8" />
```

## JBoss

JBoss ignores the `context.xml` file. Instead define JNDI data sources in `<jboss>/standalone/deployments/jasperserver.war/WEB-INF/js-jboss7-ds.xml`. For an example configuration, see [JNDI Services on JBoss](../troubleshooting/working_with_data_sources.md).

If the database is a JDBC data source configured in the repository, change the JDBC URL by editing the data source in the JasperReports Server repository. The following is an example of the JDBC URL (note that the ampersand isn't escaped):

```
jdbc:mysql://localhost:3306/foodmart_ja?useUnicode=true&characterEncoding=UTF-8
```

## Oracle

Oracle databases have both a default character set and a national character set that supports Unicode characters. Text types beginning with N (NCHAR, NVARCHAR2, and NCLOB) use the national character set. All the text data used by the JasperReports Server repository (when stored in Oracle) is stored in NVARCHAR2 columns, so that JasperReports Server metadata can use the full Unicode character set. For more information about Unicode text support, refer to the [Oracle white paper (PDF)](http://www.oracle.com/technology/tech/globalization/pdf/TWP_NCHAR_MIGRATION_10gR2.pdf).

To work properly with Unicode data, the Oracle JDBC driver requires you to set a Java system property by passing the following argument to the JVM:

```
-Doracle.jdbc.defaultNChar=true
```

In Tomcat, add the variable to `JAVA_OPTS` in `<jboss>/bin/standalone.conf` (Linux) or `<jboss>\bin\standalone.conf.bat` (Windows):

1.  Locate the following line in the script:

|         |                                                   |
|---------|---------------------------------------------------|
| Linux   | `# Set the default -Djava.endorsed.dirs argument` |
| Windows | `Set the default -Djava.endorsed.dirs argument`   |

2.  Add the following line before it:

|         |                                                          |
|---------|----------------------------------------------------------|
| Linux   | `JAVA_OPTS="$JAVA_OPTS "-Doracle.jdbc.defaultNChar=true` |
| Windows | `JAVA_OPTS=%JAVA_OPTS% -Doracle.jdbc.defaultNChar=true`  |

Because JBoss also uses `JAVA_OPTS` to pass options to the JVM, you can add the same line to `bin/run.sh` (Linux) and `bin/run.bat` (Windows). Add it before this line:

|         |                                    |
|---------|------------------------------------|
| Linux   | `# Setup the java endorsed dirs`   |
| Windows | `rem Setup the java endorsed dirs` |
