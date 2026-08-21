---
title: Cassandra Reports Not Running
description: "The Cassandra architecture introduces some restrictions that other databases do no have. Certain filters such as is-one-of (IN), <, and > cannot be used with all fields. For example, you may see the..."
---

# Cassandra Reports Not Running

The Cassandra architecture introduces some restrictions that other databases do no have. Certain filters such as is-one-of (IN), \<, and \> cannot be used with all fields. For example, you may see the following error:

``` text
Caused by: com.datastax.driver.core.exceptions.InvalidQueryException: Cannot use IN operator
on column not part of the partition key
```

Cassandra clusters use partition keys to split data between nodes, but this imposes a certain segmentation of the data. This segmentation is not compatible with all filtering, because it would be very inefficient. Therefore, the definition of the partition keys in your Cassandra schema limits you to certain comparison operations on certain fields.

In general you should avoid comparison operators other than strict equality in filters on Cassandra data sources. The Cassandra reference documentation recommends *not* using the IN comparison "under most conditions."

For more details, see the [Cassandra documentation of the SELECT WHERE clause](http://www.datastax.com/documentation/cql/3.0/cql/cql_reference/select_r.html) in CQL (Cassandra Query Language).
