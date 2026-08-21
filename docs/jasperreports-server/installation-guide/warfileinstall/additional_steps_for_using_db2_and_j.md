---
title: Additional Steps for Using DB2 and js-install Scripts
description: "The buildomatic scripts cannot automatically connect to a remote DB2 database and carry out Admin operations, so you have to perform additional steps to create the databases."
---

# Additional Steps for Using DB2 and js-install Scripts

The buildomatic scripts cannot automatically connect to a remote DB2 database and carry out Admin operations, so you have to perform additional steps to create the databases.

The DB2 client software, db2 or db2cmd, can be used to interact with DB2.

1.  Enter commands similar to the ones below in the DB2 command window to create and initialize the repository database, called `jsprsrvr` in DB2 to conform to the 8-character limitation:

```
db2 create database jsprsrvr using codeset utf-8 territory us pagesize 16384
```

1.  Enter the following commands to create and initialize the JSAudit database `jsaudit` in DB2 to conform to the 8-character limitation:

```
db2 create database jsaudit using codeset utf-8 territory us pagesize 16384
```

1.  (Optional) Run the following commands in the DB2 command window if you want to install sample databases:

```
db2 create database sugarcrm
db2 create database foodmart
```

1.  Continue installing JasperReports Server as described in [Installing the WAR File Using js-install Scripts](war_install_using_js_install.md).

Further considerations:

- If JasperReports Server is deployed on the same host as DB2, delete the following file to avoid conflicts:<br>
  `<db2>/SQLLIB/java/db2jcc.jar`

# Additional Steps for Using JBoss EAP, JBoss Web Server or Wildfly

If you're using JBoss EAP, JBoss Web Server (JWS), or Wildfly as your application server and Oracle, SQL Server, or DB2 as your database, an additional set of steps is required to handle the JDBC driver. If you're using a driver different from the one supplied with JasperReports Server, you should have already downloaded a JDBC driver jar for your database type. (See [Working With JDBC Drivers](../additional/jdbc-driver.md), if you have not yet done this.)

!!! note

    There is a JDBC JAR issue that causes an installation error with JBoss EAP 7.0.0 with JasperReports Server 7.9 and 7.8. Because the solution is to remove the JAR, this prevents using Elasticsearch with this combination of servers. This issue does not affect JBoss EAP 7.1.0 or 7.2.0. For more information, see [JBoss 7.2.0 Startup JDBC Version Error](../troubleshooting/application_server_related_problems.md).

    For other issues and work-arounds for JBoss EAP, see [JBoss Modifications](../troubleshooting/application_server_related_problems.md) in the Troubleshooting appendix.

## JBoss EAP/Wildfly Installation

You need to make an explicit reference to your JDBC driver file name so that JBoss EAP/Wildfly knows the exact file name. For example, if you are using Oracle as your database, you need to do the following:

1.  Update your `default_master.properties` file to specify the exact name (`artifactId `and `version`) of your JDBC driver:

2.  Edit:

    `<js-install>/buildomatic/default_master.properties`

    1.  Look for the section "Setup JDBC Driver".

    2.  Uncomment and edit these two lines:

        `# maven.jdbc.artifactId=ojdbc6`

        `# maven.jdbc.version=11.2.0.3`

        So that they look like this:

        `maven.jdbc.artifactId=ojdbc6`

        `maven.jdbc.version=11.2.0.3`

        (This works for a driver with the filename: `ojdbc6-11.2.0.3.jar`)

3.  Edit your `jboss-deployment-structure.xml` file so that the JDBC filename is specified:

    1.  Edit:

        `<js-install>/buildomatic/install_resources/jboss7/jboss-deployment-structure.xml`

    2.  Look for the section "Setup JDBC Driver".

    3.  Uncomment and edit the line for your database type, as shown in the following example:

        `<!-- <resource-root path="WEB-INF/lib/ojdbc6-11.2.0.3.jar" use-physical-code-source="true"/> -->`

        So that it looks like this:

        `<resource-root path="WEB-INF/lib/ojdbc6-11.2.0.3.jar" use-physical-code-source="true"/>`

        (This works for a driver with the filename: `ojdbc6-11.2.0.3.jar`)

        !!! note

            If your JDBC driver filename does not have a version number, you may need to rename the file and give it a version number.

        For instance, if you are using SQL Server and you have a file named:

        `sqljdbc6.jar`

        Then, you can rename it with a "dummy" version number:

        `sqljdbc6-1.6.jar`

    Then the `artifactId` and `version` can look like this:

    `maven.jdbc.artifactId=sqljdbc6`

    `maven.jdbc.version=1.6`

## JBoss Web Server Installation

Installation for JBoss Web Server (JWS) is similar to installing Tomcat.

In the `default_master.properties` file:

- The *appServerType* can be left as **tomcat**.
- The *appServerDir* should be set to the **../tomcat** directory.

For example:

appServerDir = /opt/jws-5.7/tomcat

!!! note

    All the databases are verified to work with JasperReports Server on JWS 5.7.2. Any DB2, MySQL, Oracle, PostgreSQL, SQL Server versions, listed in the *JasperReports Server Platform Support Guide* should work.
