---
title: Big Data Connectors for Virtual Data Sources
description: "Virtual data sources can also connect to several flavors of big data:"
---

# Big Data Connectors for Virtual Data Sources

Virtual data sources can also connect to several flavors of big data:

- Cassandra
- Hadoop-Hive 1, 2, and Impala
- MongoDB

Virtual data sources use the Teiid query engine internally to join the data from various sources, and to access big data stores. In the case of big data, the virtual data source extracts the connection information from the existing data source and uses an internal Teiid connector to access data. The Teiid connectors map the various structures used in each big data model to a relational model with tables and fields. This connector is distinct from what are called the native data sources for big data. For this reason, when a data source for big data is wrapped in a virtual data source, the resulting data source has the following limitations:

- The Cassandra, Hadoop, and MongoDB connectors in virtual data sources do not support query parameters (`$P` and `$X`). Therefore, if you use a big data connector wrapped in a virtual data source as the data source for a stand-alone query, report or Topic, you cannot include parameters to create input controls. When used in Domains and then Ad Hoc views, you can define filters to replace this functionality.
- The Cassandra connector for virtual data sources does not support any aggregation functions.
- The MongoDB connector for virtual data sources does not support the find operations, aggregation, or map reduce functions that the native MongoDB data source allows.
- The MongoDB connector for virtual data sources cannot be used in stand-alone reports or Topics. It must be used in a Domain and accessed through an Ad Hoc view or report.

However, there are significant advantages to accessing big data through virtual data sources:

- When wrapped in a virtual data source, you can access Cassandra, Hadoop, and MongoDB through a Domain, Domain Topic, Ad Hoc view, and Ad Hoc report.
- A virtual data source can contain any mix of JDBC, JNDI, and big data connectors. When you define a Domain using this data source, you can access the tables from each store and define joins between compatible fields.
- Virtual data sources that use a big data connector support query optimization, unlike the native data sources for big data. In fact, the big data connectors for virtual data sources support query optimization in Ad Hoc views and reports based on stand-alone Topics, and in Ad Ho views and reports based on Domains. The only exceptions are calculated fields, which cannot be optimized when used in Ad Hoc views or reports that are based on Topics or Domains. For more information about query optimization, see [“Ad Hoc Data Policies for Big Data” on page 1](../configuration/configuring_ad_hoc.md).

For more information about Teiid, see <http://www.jboss.org/teiid/>.

## Creating Big Data Connectors

To create a virtual data source that accesses a data source for big data

1.  Create a native data source for big data, or verify that it was created as described in one of the following sections:

- [“Cassandra Data Sources” on page 1](cassandra_data_sources.md)
- [“Hadoop-Hive Data Sources” on page 1](hadoop-hive_data_sources.md)
- [“MongoDB Data Sources” on page 1](mongodb_data_sources.md)

1.  Create a virtual data source as described in [“Virtual Data Sources” on page 1](virtual_data_sources.md).
2.  In the virtual data source creation dialog, select the big data source that you created in the first step, and save the virtual data source. You can select one or more big data sources, or any mix of big data, JDBC, and JNDI data sources.
3.  Create a Domain, specify the virtual data source you just created, and then select the big data tables when you create the Domain schema. The data from the data source is mapped to tables and fields in the Domain that you can use to create joins, filters, and all other features of a Domain.
