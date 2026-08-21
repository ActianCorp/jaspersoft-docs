---
title: Maintaining Tables
description: "In an OLAP schema, physical tables are often designed for performance, and there are some tables whose data is derivative of other tables. It is important to keep the derived tables up to date. For..."
---

# Maintaining Tables

In an OLAP schema, physical tables are often designed for performance, and there are some tables whose data is derivative of other tables. It is important to keep the derived tables up to date. For example, you can build aggregate tables from the fact tables that they summarize; they would contain the same data aggregated to a higher level in some dimension hierarchies. Then join the two fact tables in the database. This solution performs better than virtual cubes. Closure tables list out all the relations among the levels in underlying parent-child tables, which improves performance.

There are several approaches to maintaining derived tables:

1.  Materialized views can be a useful tool for this task in databases that support them, such as Oracle. The SQL for building the tables simply needs to be expressed as a materialized view, and they are rebuilt as needed from the underlying tables.
2.  When the same data-loading process occurs on a daily cycle, having a scheduled routine to rebuild the derived tables may help. The simplest implementation of this approach is to have a SQL script that drops and rebuilds these tables, which runs at a certain time of day. If the tables are very large, refine the process by incrementally rebuilding only the changes. This potentially requires more complex queries.
3.  Triggers may be appropriate if the timing of new data is unpredictable. One variation of this approach would be similar to the approach in the previous step, except that the data-loading job would update a status table at the end, which would fire triggers to rebuild all the changes to derived tables. Another variation would be to create one trigger per derived table that updates or rebuilds it when the underlying tables change. This latter variant might not be appropriate when the data changes frequently, because of the amount of time that would be spent continually rebuilding these tables.

One of these approaches might be better suited to your data warehouse than the others.

The data-loading job itself can rebuild the derived tables after loading new data. If you are using an ETL tool, this may be a convenient way to unify the tasks of table maintenance and data-loading. The specifics of this depend on the tool used.

!!! note

    It is often better to disable constraints (indexes) before rebuilding a table’s data and to re-enable the constraints afterward than to rebuild the table with the indexes enabled.

After rebuilding or significantly changing the data in any tables, make sure that the statistics for the database optimizer are up to date, which may involve gathering or estimating statistics on tables or the entire schema. This applies only to databases with statistics-based optimizers, such as Oracle or DB2.

Periodically archiving data that is no longer actively used is an important part of a long-term maintenance plan. For example, if a company only regularly reports on the last year’s data, except for quarterly historical reports, data that is older than one year can be moved from the fact tables into archive tables. Quarterly aggregates can be built from these archive tables. These smaller fact tables and aggregate tables perform better.

Another table maintenance task is taking regular backups to protect the data. There are various standard approaches to this which may depend on your database. Fact tables may be very large, but the amount of new data each day may be relatively small in comparison, and often only additive, suggesting that an incremental backup strategy can be well suited for OLAP.
