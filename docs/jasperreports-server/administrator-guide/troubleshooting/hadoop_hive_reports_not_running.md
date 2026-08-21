---
title: Hadoop-Hive Reports Not Running
description: "If you created a Hadoop-Hive data source in some older JasperReports Server versions before Version 6, it may not run when imported to a more recent version of the server. This problem is caused by..."
---

# Hadoop-Hive Reports Not Running

If you created a Hadoop-Hive data source in some older JasperReports Server versions before Version 6, it may not run when imported to a more recent version of the server. This problem is caused by the changes to the Hadoop-Hive connectors.

To update Hadoop-Hive data sources

1.  Create a new Hive data source using the same URL as the old Hadoop-Hive data source used by your reports. If you're using Cloudera 5, create a CDH 5 Hive-Impala data source. For all other hive servers, create a JDBC data source that uses the Hive JDBC driver. For instructions, see [Hadoop-Hive Data Sources](../datasources/hadoop-hive_data_sources.md).
2.  Update your Hadoop-Hive-based reports to use the new data source.
3.  Delete the old, imported data source.
