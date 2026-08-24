---
title: Clearing the Cache
description: Jaspersoft OLAP caches OLAP query results and metadata (such as cube structures and data source connection information) in memory. Cached items are removed automatically through a JVM garbage...
---

# Clearing the Cache

Jaspersoft OLAP caches OLAP query results and metadata (such as cube structures and data source connection information) in memory. Cached items are removed automatically through a JVM garbage collection, where the least-recently-used items are cleared first. However, when new data is loaded into a database accessed by Mondrian connections, the cache must be cleared; otherwise, OLAP query results cannot include the new data. The cache must also be flushed when you modify Mondrian client definitions or their data sources.

For information about creating XML/A sources and connections, see the Jaspersoft OLAP User Guide.
