---
title: Databases
description: "The following table lists databases that are supported for:"
---

# Databases

The following table lists databases that are supported for:

- JasperReports® Server 8.2

- Jaspersoft Studio Community Edition 6.20.3

Database

Version

Type

JasperReports® Server

Bean

Certified

JNDI

Certified

Jaspersoft (Mondrian) Connection

Certified

XML/A Connection

Certified

Custom (e.g. Hibernate, XML, etc.)

Certified

MySQL

- 8.0
- 8.4

<!-- -->

- Data Source
- Repository

Certified



Oracle RDBMS

- 19c

<!-- -->

- Data Source
- Repository

Compatible



PostgreSQL

- 14
- 15
- 16
- 17

<!-- -->

- Data Source
- Repository

Certified



IBM DB2

- 11.5

<!-- -->

- Data Source

Certified



Microsoft SQL Server

- 2016
- 2017
- 2019
- 2022

<!-- -->

- Data Source

Compatible



Microsoft SQL Azure

- Latest

Data Source

Certified

JBoss Teiid

- 9.1.1

Data Source

Certified

Sybase ASE

- 15.7

Data Source

Certified

Sybase SQL Anywhere

- 17

Data Source

Certified



Google BigQuery

Data Source

Certified

TIBCO Data Virtualization

- 8.8.x

Data Source

Certified

AWS Athena

Only databases under the default catalog (AwsDataCatalog) will be displayed.

- 2
- 3

Data Source

Certified

AWS Redshift

Data Source

Certified

AWS RDS - PostgreSQL

- 12
- 13
- 14
- 15

Data Source

Certified

REST API

It is Compatible and tested only for Progress driver.

Data Source

Compatible

Vertica

Data Source

Compatible only if the database complies to JDBC 2.1 and later standard.

Greenplum Database

Data Source

Compatible only if the database complies to JDBC 2.1 and later standard.

Ingres Vectorwise

Data Source

Compatible only if the database complies to JDBC 2.1 and later standard.

Netezza

Data Source

Compatible only if the database complies to JDBC 2.1 and later standard.

Teradata

Data Source

Compatible only if the database complies to JDBC 2.1 and later standard.

## Big Data Certified Support (JDBC Drivers)

The following table lists JDBC Drivers that are supported for:

- JasperReports® Server 8.2

- Jaspersoft Studio Community Edition 6.20.3

!!! note

    Virtual connections are supported only on JasperReports® Server (JRS).

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th><p>Data Source</p></th>
<th><p>Versions</p></th>
<th><p>JasperReports® Server</p></th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2">MongoDB</td>
<td><p>6.x</p></td>
<td><p>Certified</p></td>
</tr>
<tr>
<td>7</td>
<td>Certified</td>
</tr>
<tr>
<td><p>Hive 2</p></td>
<td><ul>
<li><p>Cloudera 5.3-5.7</p></li>
<li><p>HDP 2.3 - 2.4</p></li>
</ul></td>
<td><p>Certified</p></td>
</tr>
<tr>
<td><p>Impala</p></td>
<td><p>4.0</p></td>
<td><p>Certified</p></td>
</tr>
<tr>
<td><p>Cassandra</p></td>
<td><p>3.10 - 3.11</p></td>
<td><p>Certified</p></td>
</tr>
<tr>
<td><p>Spark SQL</p></td>
<td><p>2.3.3 - 3.1.2</p></td>
<td><p>Certified</p></td>
</tr>
<tr>
<td><p>Salesforce</p></td>
<td></td>
<td><p>Certified</p></td>
</tr>
<tr>
<td><p>DataStax Enterprise</p></td>
<td><ul>
<li>6.0</li>
<li>6.8</li>
</ul></td>
<td><p>Compatible</p></td>
</tr>
</tbody>
</table>

The following data sources are tested for Progress Driver replacement:

- Elasticsearch

- Neo4j

- MongoDB

- Apache Hive

- Impala

- Cassandra

- Spark SQL

- Apache Spark

- Snowflake

- Mongo DB native

- Azure SQL

- Google BigQuery

- Autonomous REST JDBC

For details, see the JasperReports Server Administrator Guide.

## JDBC/SQL Support Note

JasperReports Server data Domains (which dynamically generate queries) work with any JDBC 2.1 and SQL-92 or higher compliant data source.
