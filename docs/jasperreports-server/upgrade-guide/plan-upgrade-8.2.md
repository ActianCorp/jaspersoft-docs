---
title: Changes in 8.2 That May Affect Your Upgrade
description: "If users need 8.2 Split installations but they are on 8.1 Compact, the required upgrade path is to:"
---

# Changes in 8.2 That May Affect Your Upgrade

- Users are able to upgrade from 8.1 Compact to 8.2 Compact using samedb and newdb.

- Users are able to upgrade from 8.1 Split to 8.2 Split using samedb and newdb.

- Users will not be able to upgrade:

  - From 8.1 Compact to 8.2 Split.
  - From 8.1 Split to 8.2 Compact.

If users need 8.2 Split installations but they are on 8.1 Compact, the required upgrade path is to:

1.  Upgrade 8.1 Compact to 8.2 Compact.
2.  Then, migrate from 8.2 Compact to 8.2 Split.

For more information on these installation options, see the *Installation* and *Upgrade* guides.

## Simba Driver Removal

As of release 8.0.4, Simba drivers are removed from JasperReports Server.

If you have any resources that use or depend on any of the following Simba Drivers:

- athena-jdbc42 2.0.33.1003
- cassandra-jdbc42 2.0.13.1014
- impala-jdbc42 2.6.26.1031
- neo4j-jdbc42
- spark-jdbc42 2.6.22.1040

then you must manually install publicly available drivers (for example, Athena and Cassandra have the same Simba drivers publicly available). For other drivers, you must obtain the drivers that are recommended by the database vendor. After installing new drivers, update the resources in JasperReports Server to use the new drivers.
