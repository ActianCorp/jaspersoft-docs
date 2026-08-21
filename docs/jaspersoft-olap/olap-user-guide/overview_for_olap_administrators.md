---
title: Overview for OLAP Administrators
description: "Jaspersoft OLAP lets you analyze data organized into a hierarchical dimensional model, which has cubes and dimensions as its primary entities. In a relational database implementation of online..."
---

# Overview for OLAP Administrators

Jaspersoft OLAP lets you analyze data organized into a hierarchical dimensional model, which has cubes and dimensions as its primary entities. In a relational database implementation of online analytical processing (OLAP), the entities reside in relational tables. This is sometimes referred to as Relational OLAP (ROLAP).

Jaspersoft OLAP is based on an open source ROLAP server called Mondrian.

The de facto standard for OLAP query languages is MDX; many analysis applications use it. In a distributed computing environment, XML for Analysis (XML/A) is the standard for accessing OLAP data sources remotely. XML/A uses a web services architecture and transmits MDX queries using the SOAP protocol.

!!! note

    This overview assumes that you rely exclusively on JasperReports Server’s built-in OLAP engine. If you rely on a different OLAP engine, such as Microsoft SQL Server Analytic Services, refer to the associated documentation for instructions on maintenance.

To implement and maintain Jaspersoft OLAP

1.  Store cube data in a relational database and use an OLAP schema file to define the cubes. Note that using existing transactional databases may be inefficient with large amounts of data. To improve performance, use an extract, transform, and load (ETL) process: extract information from one or more data sources, integrate and transform the data, and load the result into the separate cube database.
2.  Identify facts or measures (the values to summarize) and dimensions (divisions of the measures–for example, dividing time into weeks, months, and years) in the cube database.
3.  Define an OLAP schema, mapping logical facts and dimensions onto the physical database. The Jaspersoft OLAP engine uses the schema to interpret the database and perform OLAP queries. The Jaspersoft OLAP Schema Workbench enables you to develop, validate, and test schemas against the database. The [Mondrian Technical Guide](http://mondrian.pentaho.com/documentation/) gives details of schemas and their options.
4.  Create an OLAP client connection that includes your schema and a database connection. Optionally, define data level security for the cube with access grants that limit users to only the data they are allowed to see, based on their roles and attributes. The repository stores the information that you provide to define an OLAP client connection.
5.  Define entry points for analysis of the cube data, known as OLAP views. You can use the Jaspersoft OLAP Schema Workbench to develop and test MDX queries.
6.  If you have defined access grants, test them by using the **Log in As** function to impersonate users with different roles.
7.  Plan for updates to data in the cube, usually regularly (for example, nightly or weekly). After an update, flush (empty) the Jaspersoft OLAP data cache so that subsequent queries get the results of new data. For more information, see [Flushing the OLAP Cache](flushing_the_olap_cache.md).
8.  Tune for performance. As a database administrator, analyze the SQL queries that Jaspersoft OLAP issues against the cube database. Jaspersoft OLAP has built-in tools that enable you to track queries (for more information, refer to [Performance Tuning](performance_tuning.md)). Tune the cube database accordingly with tools specific to the database type (for example, indexes and data striping). With large data volumes, you can create pre-calculated tables during the data load (ETL) process to aggregate measure values. Jaspersoft OLAP can use the aggregate tables to replace calculations and thus improve query performance.
9.  Design your environment for scalability and availability. Jaspersoft OLAP can run on a single machine. However, for large numbers of users, large data volumes, and high availability, you can use a multi-host environment with load balancers and some machines dedicated to either OLAP user interface or OLAP server duties. You can use XML/A to distribute processing. For more information, refer to [Working with XML/A Connections](working_with_xml_a_connections.md) and [Working with XML/A Sources](working_with_xml_a_sources.md).

The detailed procedures, beginning in this section [Creating an OLAP View with a Mondrian Connection](creating_an_olap_view_with_a_mondria.md), step you through the process of setting up all components of an OLAP view.
