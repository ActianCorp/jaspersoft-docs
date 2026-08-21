---
title: Hadoop-Hive Data Sources
description: "Unlike traditional databases, Hadoop supports huge amounts of data, often called big data. JasperReports Server processes requests to a Hadoop cluster using a JDBC data source with the Hive JDBC..."
---

# Hadoop-Hive Data Sources

Unlike traditional databases, Hadoop supports huge amounts of data, often called big data. JasperReports Server processes requests to a Hadoop cluster using a JDBC data source with the Hive JDBC driver.

The JDBC driver for Hive works with most Hive 1, Hive 2, and Impala servers. However, the original Hive 1 server has high latency with access times on the order of 30 seconds and up to 2 minutes. Hive 2 is much faster, but still not as fast as relational databases. As a result, Hadoop-Hive data sources have certain limitations and guidelines for use in JasperReports Server:

- Hadoop-Hive data sources are not suitable for creating reports interactively in the Ad Hoc Editor.

- Reports based on Hadoop-Hive are not suitable for dashboards.

- Filters and query-based input controls that rely on Hadoop-Hive data sources will be slow to populate the list of choices.

- You must configure your query limits and timeout to handle latency (see [Ad Hoc Data Policies for Big Data](../configuration/configuring_ad_hoc.md)).

- You must configure your JVM memory to handle the expected amount of data (see the JasperReports Server Installation Guide).

In general, reports based on JDBC-Hive data sources are best suited to be run in the background from the repository. For very large reports, consider scheduling them to run at night so the output is available when you need it during the day.

To create a Hive JDBC data source, follow the same procedure as in [JDBC Data Sources](jdbc_data_sources.md).
