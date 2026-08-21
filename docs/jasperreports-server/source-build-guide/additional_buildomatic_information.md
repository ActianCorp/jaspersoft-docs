---
title: Additional Buildomatic Information
description: The Ant-based buildomatic scripts contain support files for the setup and configuration of a number of databases and application servers. This chapter gives the locations of many of these files.
---

# Additional Buildomatic Information

The Ant-based buildomatic scripts contain support files for the setup and configuration of a number of databases and application servers. This chapter gives the locations of many of these files.

## Detailed Description of the deploy-webapp-pro Target

The `deploy-webapp-``pro`` ` target performs the following actions in your application server environment:

- Deletes any existing `jasperserver`` ``-pro`` ` WAR file.
- Copies the JDBC driver to the appropriate application server directory.
- Copies additional JDBC drivers to the application server to support data source creation in the UI.
- Adds a data source definition to the appropriate application server directory.
- Deploys the newly built `jasperserver`` ``-pro`` ` WAR file.
- Deletes files within the application server work directory (to clear out compiled JSP files and other cached files).
- On Tomcat, if present, deletes the old version of `<tomcat>/conf/Catalina/Localhost/``jasperserver`` ``-pro`` .xml`.

## Running Ant in Debug Mode

Ant can be run with a -v (verbose) or a -d (debug) option to help with troubleshooting, for example:

```
js-ant -v build-pro
```

### Regenerate Your Buildomatic Property Settings

If you change your `default_master.properties` file, buildomatic automatically cleans and regenerates all configuration settings. To explicitly clean and regenerate your settings manually, run the following commands:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>Commands</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>js-ant clean-config</p>
<p>js-ant gen-config</p></td>
<td><p>Clears the <code>buildomatic/build_conf/default</code> directory.</p>
<p>Rebuilds the <code>buildomatic/build_conf/default</code> directory.</p></td>
</tr>
</tbody>
</table>

!!! note

    Anytime you modify the `default_master.properties` file, the configuration settings are automatically regenerated into the `buildomatic/build_conf/default` folder.

## Using Your Own Apache Ant: Get ant-contrib.jar

If you prefer to use your own version of Apache Ant, get the file `ant-contrib-1.0b3.jar`. This JAR enables conditional logic in Ant scripts.

1.  Make sure you are using Apache Ant 1.10.*latest*.

2.  Copy the file ant-contrib-1.0b3.jar from the \<js-src\>/apache-ant/lib folder to your \<ant-home\>/lib folder:

    From:

    \<js-src\>/apache-ant/lib/ant-contrib.jar

    or

    \<js-src\>/jasperserver/buildomatic/install_resources/extra-jars/ant-contrib.jar

    To:

    |                                  |                   |
    |----------------------------------|-------------------|
    | \<ant-home\>/lib                 | (General example) |
    | C:\apache-ant-1.10.*latest*\lib  | (Windows example) |
    | `/usr/share/java/apache-ant/lib` | (Linux example)   |
    | `/usr/share/ant/lib`             | (Mac example)     |

## Generated Property Files

Once your database and application server property values are set, run buildomatic scripts to generate the database and application server configuration files to run JasperReports Server. Generated property files are in the following directory:

\<js-src\>/jasperserver/buildomatic/build_conf/default

Some of the key configuration files are:

js.jdbc.properties

maven_settings.xml   -   (This is the maven settings file used by the source build)

More generated property files are in the following directory:

\<js-src\>/jasperserver/buildomatic/build_conf/default/webapp

Some of the configuration files in this directory are:

META-INF/context.xml

WEB-INF/classes/hibernate.properties

WEB-INF/js.quartz.properties

Running `clean-config` removes these generated files. Running `gen-config` or any other target, regenerates these files.

## Existing and Generated Database SQL Files

Buildomatic files that support various databases are located in:

\<js-src\>/jasperserver/buildomatic/install_resources/sql/\<db-type\>

The source code build procedure creates the `jasperserver` repository database schema using these files:

- `js-``pro`` -create.ddl`
- `js-``pro`` -drop.ddl`

When you run the buildomatic target `build-js-ddl-``pro`` `, these database files are freshly generated for your specified database platform. The files are generated to the following location:

\<js-src\>/`jasperserver` `-pro` /repository-hibernate/build-db/target/sql

Then the files are automatically copied into their buildomatic directory location:

\<js-src\>/jasperserver/buildomatic/install_resources/sql/\<db-type\>

!!! note

    These generated files also overwrite the ones already in the buildomatic directory location.

## Generated WAR File Location and deploy-webapp-pro Target

The JasperReports Server source code build creates a `jasperserver` `-pro` WAR file. The build assembles the WAR file into the following location:

\<js-src\>/`jasperserver` `-pro` /jasperserver-war/target

When the `build-``pro`` ` target is run, buildomatic assembles the `jasperserver` `-pro` WAR file, and copies the file to this location for use by subsequent buildomatic targets:

\<js-src\>/jasperserver/buildomatic/install_resources/war/`jasperserver` `-pro`

Later, when you run the buildomatic target `deploy-webapp-``pro`` `, the following actions take place, for example on Tomcat:

|  |  |
|----|----|
| Files: | \<js-src\>/jasperserver/buildomatic/install_resources/war/`jasperserver` `-pro` /\* |
| Copied to: | \<tomcat\>/webapps |

|  |  |
|----|----|
| File: | \<js-src\>/jasperserver/buildomatic/build_conf/default/webapp/META-INF/context.xml |
| Copied to: | \<tomcat\>/webapps/jasperserver/`jasperserver` `-pro` /META-INF |

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td><p>Files:</p></td>
<td><p><span>&lt;js-src&gt;/jasperserver/buildomatic/build_conf/default/webapp/WEB-INF/classes/hibernate.properties</span><br />
</p></td>
</tr>
<tr>
<td><p>Copied to:</p></td>
<td><p><span>&lt;tomcat&gt;/webapps/<code>jasperserver</code> <code>-pro</code> /WEB-INF/classes</span></p></td>
</tr>
</tbody>
</table>

|  |  |
|----|----|
| Files: | \<js-src\>/jasperserver/buildomatic/build_conf/default/webapp/WEB-INF/js.quartz.properties |
| Copied to: | \<tomcat\>/webapps/`jasperserver` `-pro` /WEB-INF/ |

|  |  |
|----|----|
| File: | \<js-src\>/jasperserver/buildomatic/build_conf/db/postgresql/jdbc/postgresql-9.2-1002.jdbc4.jar |
| Copied to: | \<tomcat\>/lib |

|  |  |
|----|----|
| Files: | \<js-src\>/jasperserver/buildomatic/conf_source/db/app-srv-jdbc-drivers/\*/jar |
| Copied to: | \<tomcat\>/lib |

## Details on Database Load Build Targets

The buildomatic targets shown below are used in [Building JasperReports Server Source Code](building_jasperreports_server_source.md) to create and populate the databases used with JasperReports Server. These targets consolidate and simplify the handling of the `jasperserver` database and the optional sample databases:

- `create-load-js-db-``pro`` `
- `create-load-all-dbs-``pro`` `

### create-load-js-db-pro

This buildomatic target is a consolidation of the following targets:

- `drop-js-db` (if necessary)
- `create-js-db`
- `init-js-db-``pro`` `
- `import-minimal-``pro`` `

Additional functionality determines whether the `jasperserver` database exists. If so, a command-line prompt asks you if you want to delete and re-create the database.

### create-load-all-dbs-pro

This buildomatic target is a consolidation of the following targets:

- `drop-js-db` (if necessary)
- `create-js-db`
- `init-js-db-``pro`` `
- `import-minimal-``pro`` `
- `import-sample-data-``pro`` `
- (`drop-foodmart-db`, if necessary)
- `create-foodmart-db`
- `load-foodmart-db`
- (`drop-sugarcrm-db`, if necessary)
- `create-sugarcrm-db`
- `load-sugarcrm-db`

Additional functionality determines whether the `jasperserver` database exists. If so, a command-line prompt asks you if you want to delete and re-create the database. The same logic applies for the sample databases: foodmart and sugarcrm.

## General Fresh Database Schema File

The consolidated database scripts do not regenerate the database schema file. Instead the existing default database schema files are used. To regenerate the database schema files, run the following target:

js-ant build-js-ddl-pro

The files are generated to the following location:

\<js-src\>/`jasperserver` `-pro` /repository-hibernate/build-db/target/sql

Then the files are automatically copied into their buildomatic directory location:

\<js-src\>/jasperserver/buildomatic/install_resources/sql/\<db-type\>

## Manual Creation of Databases

JasperReports Server runs with a repository database typically named `jasperserver`. The automated buildomatic steps create the jasperserver database and sample databases. But you can also create your databases manually.

### Manually Creating Databases: PostgreSQL

You can manually run the scripts buildomatic uses to create and populate databases. Here is an example for PostgreSQL:

1.  To create the `jasperserver` database, use a client tool to log into PostgreSQL:

    ``` bash
    cd <js-install>/buildomatic/install_resources/sql/postgresql
    psql -U postgres -W
    postgres=#create database jasperserver encoding=’utf8’;
    postgres=#\c jasperserver;
    postgres=#\i js-pro
        -create.ddl
    postgres=#\i quartz.ddl
    postgres=#\q
    ```

2.  To create the sample databases, run these commands:

    ``` bash
    cd <js-install>/buildomatic/install_resources/sql/postgresql
    psql -U postgres -W
    postgres=#create database sugarcrm encoding=’utf8’;
    postgres=#create database foodmart encoding=’utf8’;
    postgres=#\c sugarcrm;
    postgres=#\i sugarcrm-postgresql.sql; (first make sure the file is unzipped)
    postgres=#\c foodmart;
    postgres=#\i foodmart-postqresql.sql; (first make sure the file is unzipped)
    postgres=#\i supermart-update.sql;
    postgres=#\q
    ```

### Additional Databases

For information on manual setup of databases other than PostgreSQL, refer to the JasperReports Server Installation Guide.
