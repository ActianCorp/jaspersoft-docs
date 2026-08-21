---
title: Flushing the OLAP Cache Using the API
description: "Jaspersoft OLAP maintains a cache of previously-retrieved results in order to achieve high performance. A simple interface enables you to flush the entire cache programmatically, an action required..."
---

# Flushing the OLAP Cache Using the API

Jaspersoft OLAP maintains a cache of previously-retrieved results in order to achieve high performance. A simple interface enables you to flush the entire cache programmatically, an action required when new data is inserted into databases while Jaspersoft OLAP is running.

``` java
public interface OlapManagementService {
public void flushOlapCache();
}
```

You can configure the interface as a Spring bean or instantiate it with a standard Java constructor call. The default implementation of the interface is `com.jaspersoft.jasperserver.api.metadata.olap.service.impl.OlapManagementServiceImpl`.
