---
title: Manually Creating the JasperReports Server Database
description: "If you cannot use the js-install scripts to create the JasperReports Server database and the sample databases, you can create them manually. Follow the instructions for your database to create the..."
---

# Manually Creating the JasperReports Server Database

If you cannot use the `js-install` scripts to create the JasperReports Server database and the sample databases, you can create them manually. Follow the instructions for your database to create the repository database and optional sample databases:

-   PostgreSQL

-   MySQL

-   Oracle

-   DB2

-   SQL Server

The commands in these sections have been tested at Jaspersoft, but the commands you need to use on your database instance may be different.

!!! note

    For running the Ant commands, you need to edit the `default_master.properties` file to add the settings for your database and application server as described in [Installing the WAR File Using js-install Scripts](../../../installation-guide/warfileinstall/war_install_using_js_install.md).

## PostgreSQL

To create the JasperReports Server database manually in PostgreSQL:

1.  On the Windows, Linux, or Mac command line, enter these commands:

    ``` bash
    cd <js-install>/buildomatic/install_resources/sql/postgresql
    psql -U postgres -W
    postgres=#create database jasperserver encoding=’utf8’;
    postgres=#\c jasperserver;
    postgres=#\i -pro
        -create.ddl
    postgres=#\i quartz.ddl
    postgres=#\q
    ```

2.  Run the following commands to install the JSAudit database:

    ``` bash
    cd <js-install>/buildomatic/install_resources/sql/postgresql
    psql -U postgres -W
    postgres=#create database jsaudit;
    postgres=#\c jsaudit;
    postgres=#\i js-pro-create-audit.ddl
    postgres=#\q
    ```

3.  (Optional) Run the following commands if you want to install sample databases:

``` bash
cd <js-install>/buildomatic/install_resources/sql/postgresql
psql -U postgres -W
postgres=#create database sugarcrm encoding=’utf8’;
postgres=#create database foodmart encoding=’utf8’;
postgres=#\c sugarcrm;
postgres=#\i sugarcrm.sql; (first make sure the file is unzipped)
postgres=#\c foodmart;
postgres=#\i foodmart-postqresql.sql; (first make sure the file is unzipped)
postgres=#\i supermart-update.sql;
postgres=#\q
```

-   If you didn't install the optional sample databases, complete the installation with these commands:

`cd <js-install>/buildomatic`

`js‑ant import-minimal-``pro`` `

`js-ant deploy-webapp-``pro`` `

If you installed the optional sample databases, complete the installation with these commands:

`cd <js-install>/buildomatic`

`js‑ant import-sample-data-``pro`` `

`js-ant deploy-webapp-``pro`` `

For more information about executing the Ant scripts, see [Installing the WAR File Manually](../../../installation-guide/warfileinstall/war_install_manually.md).

-   Set Java JVM Options (required), as described in [Setting JVM Options for Application Servers](../../../installation-guide/additional/setting_jvm_options_for_application_.md).

-   Set up the JasperReports Server License (required) as described in [Setting Up the JasperReports Server License](../../../installation-guide/additional/setting_up_the_jasperreports_server_.md).

## MySQL

To create the JasperReports Server database manually in MySQL:

You can use the MySQL client software, `mysql.exe` or `mysql`, to interact with the MySQL database.

!!! note

    For specific details on connecting to the MySQL database and setting privileges for databases and db users, please refer to the documentation provided with your database.

1.  On the Windows, Linux, or Mac command line, enter the following commands to create and initialize the JasperReports Server database.

    ``` bash
    cd <js-install>/buildomatic/install_resources/sql/mysql
    mysql -u root -p
    mysql>create database jasperserver character set utf8;
    mysql>use jasperserver;
    mysql>source -pro
        -create.ddl
    mysql>source quartz.ddl
    mysql>exit
    ```

2.  Run these commands to create and initialize the JSAudit database.

    ``` text
    mysql -u root -p
    mysql>create database jsaudit;
    mysql>use jsaudit;
    mysql>source js-pro-create-audit.ddl
    mysql>exit
    ```

3.  (Optional) Run these commands to install sample databases:

``` bash
cd <js-install>/buildomatic/install_resources/sql/mysql
mysql -u root -p
mysql>create database sugarcrm;
mysql>create database foodmart;
mysql>use sugarcrm;
mysql>source sugarcrm.sql;(first make sure the file is unzipped)
mysql>use foodmart;
mysql>source foodmart-mysql.sql; (first make sure the file is unzipped)
mysql>source supermart-update.sql;
mysql>exit
```

-   If you didn't install the optional sample databases, complete the installation with these commands:

`cd <js-install>/buildomatic`

`js‑ant import-minimal-``pro`` `

`js-ant deploy-webapp-``pro`` `

If you installed the optional sample databases, complete the installation with these commands:

`cd <js-install>/buildomatic`

`js‑ant import-sample-data-``pro`` `

`js-ant deploy-webapp-``pro`` `

For more information about executing the Ant scripts, see [Installing the WAR File Manually](../../../installation-guide/warfileinstall/war_install_manually.md).

-   Set Java JVM Options (required), as described in [Setting JVM Options for Application Servers](../../../installation-guide/additional/setting_jvm_options_for_application_.md).

-   Set up the JasperReports Server License (required) as described in [Setting Up the JasperReports Server License](../../../installation-guide/additional/setting_up_the_jasperreports_server_.md).

## Oracle

To create the JasperReports Server database manually in Oracle:

You can use the Oracle client software, `sqlplus.exe` or `sqlplus`, to interact with Oracle.

!!! note

    For specific details on connecting to the Oracle database and setting privileges for databases and db users, please refer to the documentation provided with your database.

1.  On the Windows, Linux, or Mac command line, enter the following commands to create and initialize the JasperReports Server database.

    ``` bash
    cd <js-install>/buildomatic/install_resources/sql/oracle
    sqlplus /nolog (start sqlplus client)
    SQL> connect system/password (use your sysUsername and password)
    (or SQL>connect sys/password as sysdba
    SQL> create user jasperserver identified by password; (as sys user)
    SQL> grant connect, resource to jasperserver; (as sys user)
    SQL> grant unlimited tablespace to jasperserver; (as sys user)
    SQL> connect jasperserver/password@ORCL (use your password, your SID)
    SQL> @/opt/jasperreports-server-pro-8.0.0-bin/buildomatic/install_resources/sql/oracle/js-pro-create.ddl
    SQL> @/opt/jasperreports-server-pro-8.0.0-
    bin/buildomatic/install_resources/sql/oracle/quartz.ddl or quartz-23onwards.ddl (depending on the oracle db version being used)
    SQL> exit
    ```

2.  To create and initialize the JSAudit database, enter the following commands.

    ``` text
    SQL> create user jsaudit identified by password; (as sys user)
    SQL> grant connect, resource to jsaudit; (as sys user)
    SQL> grant unlimited tablespace to jsaudit; (as sys user)
    SQL> connect jsaudit/password@ORCL
    SQL> @/opt/jasperreports-server-pro-8.0.0-bin/buildomatic/install_resources/sql/oracle/js-sequence-create.ddl
    SQL> @/opt/jasperreports-server-pro-8.0.0-bin/buildomatic/install_resources/sql/oracle/js-pro-create-audit.ddl
    SQL> exit
    ```

3.  Go to the `<js-install>/buildomatic` path and configure the `default_master.properties` file with the required values. For example:<br>
    <br>
    `cd <js-install>/buildomatic`<br>
    `dbUsername=jasperserver`<br>
    `dbPassword=password`<br>
    `sysUsername=jasperserver`<br>
    `sysPassword=password`<br>
    `dbHost=localhost`<br>
    `dbPort=1521 sid=ORCL `

    `dbVersion=oracleDbVersion` `(for example, 12, 19c, 21c, 23ai, 26ai and so on)`<br>
    <br>
    `#audit props`<br>
    `installType=split`<br>
    `audit.dbHost=localhost`<br>
    `audit.dbPort=1521`<br>
    `audit.sid=ORCL`<br>
    `audit.dbUsername=jsaudit`<br>
    `audit.dbPassword=password`<br>
    `audit.dbName=jsaudit`<br>
    `audit.sysUsername=system`<br>
    `audit.sysPassword=password`

    You can set sysUsername and sysPassword the same as dbUsername and dbPassword.

4.  Create a server setting with the audit db schema name (auditDB=JSAUDIT), to do so:

    1.  Go to `<js-install>/buildomatic/bin` path and edit the `db-common.xml` file.

    2.  Add the following target at the end of file and before `</project>`:<br>
        `<target name="import-profile-attributes">`<br>
        `<import-profile-attribute key="auditDB" attrValue="${audit.dbName}"/>`<br>
        `</target>`

    3.  Save the file.

    4.  Run the following command:<br>
        `./js-ant import-profile-attributes`

        !!! note

            Server setting auditDB=JSAUDIT is needed for audit reports working properly on oracle in case of split installation.

5.  (Optional) Special edit to the `sugarcrm.sql` script that creates the `sugarcrm` sample database. The `sqlplus` command line tool interprets SQL statements differently than a JDBC call (that is, the way buildomatic runs SQL scripts). Because of this, the `sugarcrm.sql` file must be edited to run using `sqlplus`. To make these edits, do the following:

-   Unzip the `sugarcrm.zip` file to get the `sugarcrm.sql` file. Open `sugarcrm.sql` for editing:

    -   Uncomment the `"-- set define off"` line to look like this `"set define off"` (Line 7)

        -   Uncomment the `"--/"` line that follows the `CREATE TRIGGER` statements (there are 12 of these toward the very end of the file on line 71,282. Just before the `CREATE INDEX` statements). Change to be just `"/"`. (This stops the trigger procedure definition in `sqlplus`.)
        -   Save the file.

!!! note

    If you build and load the sample databases using buildomatic, the NLS_LANG setting is automatically handled via a JDBC driver setting.

    If you load the sample databases using buildomatic, you will not need to set any variables or make any script edits.

1.  (Optional) Set the `NLS_LANG` variable. The `sugarcrm` database has test data that requires a specific NLS_LANG setting to load into Oracle correctly. You need to set this in your shell environment if you are manually loading the `sugarcrm` database.

    <table>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <tbody>
    <tr>
    <td><p>Windows:</p></td>
    <td><div class="language-text highlight"><pre><code>set NLS_LANG=AMERICAN_AMERICA.WE8ISO8859P1</code></pre></div></td>
    </tr>
    <tr>
    <td><p>Linux:</p></td>
    <td><div class="language-text highlight"><pre><code>export NLS_LANG=AMERICAN_AMERICA.WE8ISO8859P1</code></pre></div></td>
    </tr>
    </tbody>
    </table>

2.  (Optional) Run the following commands if you want to install sample databases:

``` bash
cd <js-install>/buildomatic/install_resources/sql/oracle
sqlplus /nolog (start sqlplus client)
SQL> connect system/password (use your sysUsername and password)
(or SQL>connect sys/password as sysdba
SQL> create user sugarcrm identified by password;
SQL> create user foodmart identified by password;
SQL> grant connect, resource to sugarcrm;
SQL> grant connect, resource to foodmart;
SQL> connect sugarcrm/password@ORCL
SQL> @sugarcrm.sql (First, make sure file is unzipped)
SQL> connect foodmart/password@ORCL
SQL> @foodmart-oracle.sql (First, make sure file is unzipped)
SQL> @supermart-update.sql
SQL> exit
```

-   If you didn't install the optional sample databases, complete the installation with these commands:

`cd <js-install>/buildomatic`

`js‑ant import-minimal-``pro`` `

`js-ant deploy-webapp-``pro`` `

If you installed the optional sample databases, complete the installation with these commands:

`cd <js-install>/buildomatic`

`js‑ant import-sample-data-``pro`` `

`js-ant deploy-webapp-``pro`` `

For more information about executing the Ant scripts, see [Installing the WAR File Manually](../../../installation-guide/warfileinstall/war_install_manually.md).

-   Set Java JVM Options (required), as described in [Setting JVM Options for Application Servers](../../../installation-guide/additional/setting_jvm_options_for_application_.md).

-   Set up the JasperReports Server License (required) as described in [Setting Up the JasperReports Server License](../../../installation-guide/additional/setting_up_the_jasperreports_server_.md).

## DB2

To create the JasperReports Server database manually in DB2:

Use the DB2 client software, `db2` or `db2cmd`, to interact with DB2.

!!! note

    For specific details on connecting to the DB2 database and setting privileges for databases and db users, please refer to the documentation provided with your database.

1.  Change to the following directory:

    `cd <js-install>/buildomatic/install_resources/sql/db2`

2.  Enter these commands in the DB2 command window to create and initialize the repository database called `jsprsrvr` in DB2 to conform to the 8-character limitation:

    ``` text
    db2 create database jsprsrvr using codeset utf-8 territory us pagesize 16384
    db2 connect to jsprsrvr
    db2 -tf js-pro-create.ddl
    db2 -tf quartz.ddl
    ```

3.  To create and initialize the JSAudit database, enter the following commands in the DB2 command window:

    ``` text
    db2 create database jsaudit
    db2 connect to jsaudit
    db2 -tf js-pro-create-audit.ddl
    db2 exit
    ```

4.  (Optional) Run the following commands in the DB2 command window if you want to install sample databases:

``` text
db2 create database sugarcrm
db2 connect to sugarcrm
db2 -tf sugarcrm.sql (first make sure file is unzipped)
db2 create database foodmart
db2 connect to foodmart
db2 -tf foodmart-db2.sql (first make sure file is unzipped)
db2 -tf supermart-update.sql (if script is available)
```

-   If you didn't install the optional sample databases, complete the installation with these commands:

`cd <js-install>/buildomatic`

`js‑ant import-minimal-``pro`` `

`js-ant deploy-webapp-``pro`` `

If you installed the optional sample databases, complete the installation with these commands:

`cd <js-install>/buildomatic`

`js‑ant import-sample-data-``pro`` `

`js-ant deploy-webapp-``pro`` `

For more information about executing the Ant scripts, see [Installing the WAR File Manually](../../../installation-guide/warfileinstall/war_install_manually.md).

-   Set Java JVM Options (required), as described in [Setting JVM Options for Application Servers](../../../installation-guide/additional/setting_jvm_options_for_application_.md).

-   Set up the JasperReports Server License (required) as described in [Setting Up the JasperReports Server License](../../../installation-guide/additional/setting_up_the_jasperreports_server_.md).

Further considerations:

-   If JasperReports Server is deployed on the same host as DB2, delete the following file to avoid conflicts:

`<db2>/SQLLIB/java/db2jcc.jar`

## SQL Server

Use the `sqlcmd` utility to build the `jasperserver` database manually.

!!! note

    For specific details on connecting to the SQL Server database and setting privileges for databases and db users, please refer to the documentation provided with your database.

To create the JasperReports Server database manually in SQL Server:

1.  Open a Command Prompt and enter the following commands using the administrator (sa) username and password.

    ``` bash
    cd <js-install>\buildomatic\install_resources\sql\sqlserversqlcmd -S ServerName -Usa -Psa
    1> CREATE DATABASE [jasperserver]
    2> GO
    1> USE [jasperserver]
    2> GO
    1> :r js-pro-create.ddl
    2> GO
    1> :r quartz.ddl
    2> GO
    ```

2.  From the Windows Start menu, select ****Microsoft SQL Server &gt; SQL Server Management Studio****.

3.  Connect to SQL Server as the administrative database user, and check that the `jasperserver` database appears in the Object Explorer.

4.  Expand the tables in the `jasperserver` database, and check that the tables have been added.

    To create and initialize the JSAudit database:

5.  Run the following commands:

    ``` bash
    cd <js-install>\buildomatic\install_resources\sql\sqlserver
    sqlcmd -S ServerName -Usa -Psa
    1> CREATE DATABASE [jsaudit]
    2> GO
    1> USE [jsaudit]
    2> GO
    1> :r js-pro-create-audit.ddl
    2> GO
    ```

    To create the optional sample databases manually in SQL Server:

6.  Extract the files in the `sugarcrm.zip` file to the level above your current directory, placing the `sugarcrm.sql` file in this directory:

    `<js-install>\jasperserver\buildomatic\install_resources\sql\sqlserver`

7.  Enter these commands to create and initialize the `sugarcrm` database:

    ``` text
    1> CREATE DATABASE [sugarcrm]
    2> GO
    1> USE [sugarcrm]
    2> GO
    1> :r sugarcrm.sql
    2> GO
    ```

8.  You cannot initialize the foodmart database manually. Instead, change to the buildomatic directory and use the following buildomatic commands to create and initialize it from the command line:

`js-ant create-foodmart-db`

`js-ant load-foodmart-db`

Alternatively, you can replace the first command and create the database manually using the following SQL Server commands, but you still have to use the buildomatic command `js-ant load-foodmart-db` to load the data:

``` text
1> CREATE DATABASE [foodmart]
2> GO
1> USE [foodmart]
2> GO
```

To complete the manual installation of databases in SQL Server

-   If you didn't install the optional sample databases, complete the installation with these commands:

`cd <js-install>/buildomatic`

`js‑ant import-minimal-``pro`` `

`js-ant deploy-webapp-``pro`` `

If you installed the optional sample databases, complete the installation with these commands:

`cd <js-install>/buildomatic`

`js‑ant import-sample-data-``pro`` `

`js-ant deploy-webapp-``pro`` `

For more information about executing the Ant scripts, see [Installing the WAR File Manually](../../../installation-guide/warfileinstall/war_install_manually.md).

-   Set Java JVM Options (required), as described in [Setting JVM Options for Application Servers](../../../installation-guide/additional/setting_jvm_options_for_application_.md).

-   Set up the JasperReports Server License (required) as described in [Setting Up the JasperReports Server License](../../../installation-guide/additional/setting_up_the_jasperreports_server_.md).
