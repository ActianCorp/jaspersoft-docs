---
title: Create and Load Sample Data
description: "The procedure for Building JasperReports Server Source Code loads core data required to start the application, but it doesn't create sample data, such as sample reports to run and sample databases...."
---

# Create and Load Sample Data

The procedure for [Building JasperReports Server Source Code](building_jasperreports_server_source.md) loads core data required to start the application, but it doesn't create sample data, such as sample reports to run and sample databases. Follow the steps below to create and load sample data.

## Load Sample Data

The buildomatic scripts can load sample resources and sample databases. Note: In the procedure below, your `jasperserver` database will be deleted and re-created unless you choose ‘n’ for No when prompted.

Your `default_master.properties` should already be created.

1.  Start your database server.

2.  Stop your application server.

3.  Run the commands shown below:

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
    <td><p><code>cd &lt;js-src&gt;/jasperserver/buildomatic</code></p></td>
    <td></td>
    </tr>
    <tr>
    <td><p><code>js-ant create-load-all-dbs-</code><span><code>pro</code></span><code> </code></p></td>
    <td><p>Creates and loads the <code>jasperserver</code> database</p>
    <p>Imports core bootstrap resources</p>
    <p>Creates and loads sample databases</p>
    <p>Imports sample resources</p>
    <p>(Choose ‘n’ when prompted if you do not want to recreate your <code>jasperserver</code> database.)</p></td>
    </tr>
    </tbody>
    </table>

## Generate Your Own Sample Resources

This procedure generates the same resources imported and used by the released version of JasperReports Server. Your jasperserver database will be deleted and re-created.

Your `default_master.properties` should have already been created.

### Generating Sample Resources for MySQL, PostgreSQL, Oracle, and SQL Server Databases

1.  Make sure that the sample data has been loaded.

2.  Start your database server.

3.  Stop your application server.

4.  Run the commands shown below:

    | Commands | Description |
    |----|----|
    | `cd <js-src>/jasperserver/buildomatic` |  |
    | `js-ant re-init-js-db-``pro`` ` | Drop, create, and initialize the `jasperserver` database. |
    | `js-ant run-production-data-``pro`` ` | Generate sample resources using the processing logic from the production-test source code. |

### Generating Sample Resources for the DB2 Database

The buildomatic scripts cannot automatically connect to a remote DB2 database and carry out admin operations, so you have to perform additional steps to create the databases.

The DB2 client software, db2 or db2cmd, can be used to interact with DB2.

1.  Start your database server.

2.  Stop your application server.

3.  If the database already exists, remove it before creating a new one.

4.  Run the commands shown below:

    | Commands | Description |
    |----|----|
    | `db2 create database jsprsrvr using codeset utf-8 territory us pagesize 16384` | Create and initialize the `jasperserver` database. |
    | `db2 create database sugarcrm` | Optionally, create the `sugarcrm` database. |
    | `db2 create database foodmart` | Optionally, create the `foodmart` database. |
