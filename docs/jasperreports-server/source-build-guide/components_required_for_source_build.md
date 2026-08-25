---
title: Components Required for Source Build
description: "The components and versions listed in this section are required to build and run JasperReports Server:"
---

# Components Required for Source Build

The components and versions listed in this section are required to build and run JasperReports Server:

- Check Your Java JDK
- Check Your Maven Version
- Check Your Application Server
- Check Your Database Instance
- Check Your Chrome/Chromium Installation

## Check Your Java JDK

Compile the JasperReports Server source code under Java 17. To check the version of your JDK (Java Development Kit), run the following command:

`javac -version`

To download the Java JDK, follow the instructions on the Java website: http://www.oracle.com/technetwork/java/javase/downloads/index.html.

The Oracle/Sun JDK is the certified Java platform for JasperReports Server. OpenJDK 17, Oracle 17 and Temurin 17 are supported.

## Check Your Maven Version

We use Apache Maven 3.9 to compile, build, and package the JasperReports Server source code because of its ability to manage third-party dependencies via online repositories.

To download and install Maven, go to:  <http://maven.apache.org/download.html#installation>

To run `mvn` from the command line, put the maven binary (`mvn` or `mvn.exe`) in your environment `PATH`. To check your Maven version, run this command:

``` bash
mvn -version
```

For information about Maven, see [Maven Troubleshooting](troubleshooting.md).

## Check Your Application Server

To run JasperReports Server, you need an application server on the same computer as your source code. We support the following application servers:

| Application Server | Comments |
|----|----|
| Apache Tomcat | Source build can automatically deploy to this application server. |
| JBoss EAP/Wildfly | Source build can automatically deploy to this application server. |
|  |  |
|  |  |

## Check Your Database Instance

To run JasperReports® Server, you need a database instance. We support the following:

| Database | Comments |
|----|----|
| PostgreSQL | Source build automatically creates the `jasperserver` database. |
| MySQL | Source build automatically creates the `jasperserver` database. |
| Oracle | Source build automatically creates the `jasperserver` database. |
| SQL Server | Source build automatically creates the `jasperserver` database. |
| DB2 | The `jasperserver` database must be created by the DB administrator. |

## Check Your Chrome/Chromium Installation

To build JasperReports Server, you need to install Chrome, Chromium, or any other browser based on Chromium like Microsoft Edge, and set the property `chrome.path` in default_master.properties. See the JasperReports Server Administrator Guide for more information about Chrome/Chromium.
