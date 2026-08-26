---
title: Databases
description: "The following table lists databases that are supported for:"
---

# Databases

The following table lists databases that are supported for:

-   JasperReports® Server 10.1.0

-   Jaspersoft® Studio Pro 10.1.0

-   JasperReports® IO Pro 10.1.0

-   JasperReports® Web Studio Pro 10.1.0

Database

Version

Type

Commercial

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

-   8.4

<!-- -->

-   Data Source
-   Repository

Certified



Oracle RDBMS

-   19c
-   23ai
-   26ai

<!-- -->

-   Data Source
-   Repository

Certified



PostgreSQL

-   14
-   15
-   16
-   17

<!-- -->

-   Data Source
-   Repository

Certified



IBM DB2

-   11.5

<!-- -->

-   Data Source
-   Repository

Certified



Microsoft SQL Server

-   2016
-   2017
-   2019
-   2022

<!-- -->

-   Data Source
-   Repository

Certified



Microsoft SQL Azure

-   Latest

Data Source

Certified

Snowflake

Data Source

Compatible

Sybase ASE

-   15.7

Data Source

Compatible

Sybase SQL Anywhere

-   17

Data Source

Compatible



ElasticSearch<span class="jsd-footnote-ref">^1^</span> <span class="jsd-footnote">Refer to the JasperReports® Server Release Notes for limitations with ElasticSearch.</span>

-   8.12.1

Data Source

Certified

Neo4j

-   4.0.4

Data Source

Certified

Google BigQuery

Data Source

Certified

TIBCO Data Virtualization

-   8.8.x

Data Source

Certified

AWS Athena<span class="jsd-footnote-ref">^2^</span>

<div class="jsd-footnote">

Only databases under the default catalog (AwsDataCatalog) will be displayed.

</div>

-   2
-   3

Data Source

Certified

AWS Redshift

Data Source

Certified

AWS RDS - PostgreSQL

-   12
-   13
-   14
-   15

Data Source

Certified

REST API<span class="jsd-footnote-ref">^3^</span>

<div class="jsd-footnote">

It is Compatible and tested only for Progress driver.

</div>

Data Source

Compatible

Infobright



Data Source

Compatible only if the database complies to JDBC 2.1 and later standard.

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

-   JasperReports® Server 10.1.0

-   Jaspersoft® Studio Pro 10.1.0

-   JasperReports® IO Pro 10.1.0

-   JasperReports® Web Studio Pro 10.1.0

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
<td><p>Apache Hive</p></td>
<td><p>4.0.0</p></td>
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
<td><p>Compatible</p></td>
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

-   Elasticsearch

-   Neo4j

-   MongoDB

-   Apache Hive

-   Impala

-   Cassandra

-   Spark SQL

-   Apache Spark

-   Snowflake

-   Mongo DB native

-   Azure SQL

-   Google BigQuery

-   Autonomous REST JDBC

For details, see the JasperReports Server Administrator Guide.

## JDBC/SQL Support Note

JasperReports Server data Domains (which dynamically generate queries) work with any JDBC 2.1 and SQL-92 or higher compliant data source.
