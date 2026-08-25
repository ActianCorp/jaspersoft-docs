---
title: Locating and Changing Buildomatic Configuration Files
description: The Ant-based buildomatic scripts contain support files for setting up and configuring a number of databases and application servers. This section describes the locations of some of these files and...
---

# Locating and Changing Buildomatic Configuration Files

The Ant-based buildomatic scripts contain support files for setting up and configuring a number of databases and application servers. This section describes the locations of some of these files and how to change their content.

## Regenerating Buildomatic Settings

Whenever you change your `default_master.properties` file and re-run the `js-install` scripts (or any other buildomatic target), your generated configuration settings are automatically updated. The generated settings are in this location:

`<js-install>/buildomatic/build_conf/default`

The settings are regenerated automatically based on the updated timestamp on the properties file.

If you want to explicitly regenerate your configuration, run the following buildomatic targets:

`cd <js-install>/buildomatic`

`js-ant clean-config`

`js-ant gen-config`

The first target clears the configuration template files in the `buildomatic/build_conf/default` directory. The second re-builds the configuration settings.

## Locating Buildomatic-Generated Property Files

After you set your database and application server property values, initiate buildomatic to automatically generate the database and application server configuration files needed to prepare for a JasperReports Server installation.

The generated property files are in this location:

`<js-install>/buildomatic/build_conf/default`

Some of the key configuration files are:

`js.jdbc.properties`

`js.quartz.properties`

`js-jboss-ds.xml`

`maven_settings.xml` - (used for source code build)

More generated property files are:

`<js-install>/buildomatic/build_conf/default/webapp`

Included in the /webapp directory are configuration files, such as:

`META-INF/context.xml`

`WEB-INF/classes/hibernate.properties`

`WEB-INF/js.quartz.properties`

`WEB-INF/js.password-storage-config.properties`

These auto-generated files are removed if you run the buildomatic target: `clean-config`. You can then regenerate the files by running the target: `gen-config`. (Also, after running `clean-config`, any subsequent target will regenerate the configuration files.)

## Buildomatic Location for JasperReports Server WAR File

Buildomatic takes the JasperReports Server WAR file from the root of the `<js-install>` directory:

`<js-install>/``jasperserver`` ``-pro`` .war`

When you run the `deploy-webapp-`pro target, buildomatic unpacks the war archive into your application server and copies the needed database configuration files to their appropriate locations. For instance, in the case of Tomcat:

- `<js-install/> ``jasperserver`` ``-pro`` .war`

Unpacked and copied to `<tomcat>/webapps/``jasperserver`` ``-pro`` /*`

- `<js-install>/buildomatic/build_conf/default/webapp/META-INF/context.xml`

Copied to `<tomcat>/webapps/``jasperserver`` ``-pro`` /META-INF/context.xml`

- `<js-install>/buildomatic/build_conf/default/webapp/WEB-INF/classes/hibernate.properties`

Copied to `<tomcat>/webapps/``jasperserver`` ``-pro`` /WEB-INF/classes/hibernate.properties`

- `<js-install>/buildomatic/build_conf/default/webapp/WEB-INF/js.quartz.properties`

Copied to `<tomcat>/webapps/``jasperserver`` ``-pro`` /WEB-INF/js.quartz.properties`

- `<js-install>/buildomatic/build_conf/default/webapp/WEB-INF/js.password-storage-config.properties`

Copied to `<tomcat>/webapps/jasperserver-pro/WEB-INF/js.password-storage-config.properties`

- `<js-install>/buildomatic/build_conf/db/postgres/jdbc/postgresql-42.2.5.jar`

Copied to `<tomcat>/lib`

## Buildomatic Location for SQL Scripts

Buildomatic comes with SQL scripts and other utilities that support a number of databases. These files are located here:

`<js-install>/buildomatic/install_resources/sql/`

For example, some key files are (same pattern for additional databases):

`<js-install>/buildomatic/install_resources/sql/postgresql/``-pro`` -create.ddl`

`<js-install>/buildomatic/install_resources/sql/postgresql/quartz.ddl`

`<js-install>/buildomatic/install_resources/sql/postgresql/upgrade-postgresql-6.0.0-6.1.0-``pro`` .sql`

`<js-install>/buildomatic/install_resources/sql/postgresql/js``-pro`` -drop.ddl`

`<js-install>/buildomatic/install_resources/sql/postgresql/drop-quartz.ddl`

`<js-install>/buildomatic-additional/install_resources/sql/oracle/quartz-23onwards.ddl` (available for Oracle database only)

Note that there is an additional file for Oracle database. Depending on the Oracle database version used, you should run the `quartz.ddl` or `quartz-23onwards.ddl` script.

!!! note

    You can run these scripts manually by copying them to the location of your database client software.

## Buildomatic Location for Database Creation Scripts

For most databases the buildomatic scripts can create the metadata repository database used by JasperReports Server. This is the database that stores data defining users, roles, data sources, reports, OLAP views, domains, and other data. This database is normally named `jasperserver`.

Buildomatic attempts to create the jasperserver database via JDBC when the `create-js-db` target is executed. The scripts and property files used to create the jasperserver database are located in the following directory:

`<js-install>/buildomatic/conf_source/db/<db_name>/scripts.properties`

## Buildomatic Location for Sample Data Catalog ZIP Files

Buildomatic includes export files that hold the JasperReports Server sample data (with examples of new features). This sample data is loaded when you run the buildomatic target `import-sample-data-``pro`` `, for instance. These export files along with other important export files are located here:

`<js-install>/buildomatic/install_resources/export/`

Here are some key files:

`js-catalog-<db_name>-minimal-``pro`` .zip`

`js-catalog-<db_name>-``pro`` .zip`

## Hibernate Properties Settings

After you run buildomatic to generate your configuration files, your `hibernate.properties` settings are in the following directory:

`<js-install>/buildomatic/build_conf/default/webapp/WEB-INF/classes/hibernate.properties`

Within the `jasperserver`` ``-pro`` ` WAR file the hibernate.properties file is found at the following location:

`<appserver-path>/``jasperserver`` ``-pro`` /WEB-INF/classes/hibernate.properties`

The buildomatic scripts automatically create this configuration file. When you run the buildomatic target `deploy-webapp-``pro`` ` this file is copied to JasperReports Server in your application server.

Hibernate property values are:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td><p>PostgreSQL:</p></td>
<td><pre class="properties"><code>metadata.hibernate.dialect=com.jaspersoft.hibernate.dialect.PostgresqlNoBlobDialect</code></pre></td>
</tr>
<tr>
<td><p>MySQL 5.5:</p></td>
<td><pre class="properties"><code>metadata.hibernate.dialect=org.hibernate.dialect.MySQL5InnoDBDialect</code></pre></td>
</tr>
<tr>
<td><p>DB2:</p></td>
<td><pre class="properties"><code>metadata.hibernate.dialect=com.jaspersoft.ji.hibernate.dialect.DB2JICustomDialect</code></pre></td>
</tr>
<tr>
<td><p>Oracle:</p></td>
<td><pre class="properties"><code>metadata.hibernate.dialect=com.jaspersoft.ji.hibernate.dialect.OracleJICustomDialect</code></pre></td>
</tr>
<tr>
<td><p>SQL Server:</p></td>
<td><pre class="properties"><code>metadata.hibernate.dialect=com.jaspersoft.ji.hibernate.dialect.SQLServerJICustomDialect</code></pre></td>
</tr>
</tbody>
</table>

## Database Connection Configuration Files

### Tomcat

When you have set up the buildomatic configuration for your database, the Tomcat context.xml is automatically created with the appropriate settings for JasperReports Server.

When you run the buildomatic target `deploy-webapp-``pro`` `, the context.xml is automatically copied into the `jasperserver` `-pro` WAR set of files.

You can view the automatically generated `context.xml` at the following location:

`<js-install>/buildomatic/build_conf/default/webapp/META-INF/context.xml`

The final location of the `context.xml` is:

`<tomcat>/webapps/``jasperserver`` ``-pro`` /META-INF/context.xml`

Older versions of Tomcat create a copy of the `context.xml` file with a changed name that is read instead of the one found in the `jasperserver` `-pro` war file. This can be confusing for Tomcat users who try to change their database settings. If you change your settings, delete the file in this location:

`<tomcat>/conf/Catalina/localhost/``jasperserver`` ``-pro`` .xml`

### JBoss

When you have set up the buildomatic configuration for your database, the JBoss data source definition file is automatically created with the appropriate settings for JasperReports Server.

When you run the buildomatic target `deploy-webapp-``pro`` `, the `js-jboss-ds.xml` is automatically copied into the JBoss instance.

You can view the automatically generated `js-jboss-ds.xml` at the following location:

`<js-install>/buildomatic/build_conf/default/js-jboss-ds.xml`

The final location of the `js-jboss-ds.xml` is:

`<jboss>/standalone/deployments/``jasperserver`` ``-pro`` .war/WEB-INF/js-jboss7-ds.xml`

When JasperReports Server is running under JBoss, a couple of INFO log messages and an XML/A connection error may occur depending on the version of JBoss you are running.

For more information, refer to the troubleshooting section [JBoss Modifications](../troubleshooting/application_server_related_problems.md).
