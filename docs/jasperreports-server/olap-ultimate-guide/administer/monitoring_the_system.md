---
title: Monitoring the System
description: "Jaspersoft OLAP uses standards-based technology, so the maintenance of the application itself is similar to that of any web application. The important considerations are reliability (making sure the..."
---

# Monitoring the System

Jaspersoft OLAP uses standards-based technology, so the maintenance of the application itself is similar to that of any web application. The important considerations are reliability (making sure the application servers and DBMS are up and running) and performance.

Jaspersoft recommends standard monitoring tools for production deployments that have rigorous availability requirements. Besides doing a basic check of system health, occasional monitoring of the amount of memory being used by the OLAP engine can be useful for optimizing performance depending on your usage. If the OLAP engine is consistently using close to the maximum amount of heap memory allocated, it could be caching more if more memory were allocated to that JVM process.

When you notice problems, your first step is generally to search the logs for clues. JasperReports Server uses standard log4j for all system logging, and all output is directed to WEB-INF/jasperserver.log by default.

- If there are FATAL messages in the log, the cause is usually related to the configuration of the web application and is something that keeps the application server from loading the web application.
- If there are any ERROR messages in the log, they denote an unexpected error within the application and should be investigated.
- Messages at the WARN level do not indicate a serious problem, but they may contain useful information that something may be wrong with the setup that could lead to errors.
- DEBUG and INFO messages may help developers or expert users of the system, but may be safely suppressed by setting the log4j.rootLogger to WARN messages and above in the log4j.propertiesfile. When debugging an exception, set the logging level to DEBUG for the specific classes mentioned in the exception.
- The log4j documentation is available at: <https://logging.apache.org/log4j/2.x/manual/index.html>.[](http://logging.apache.org/log4j/docs/manual.html). For Jaspersoft-specific information on logging, see the Jaspersoft OLAP User Guide and JasperReports Server Administrator Guide.

If you need to contact Technical Support, they may request that you use the log collector feature to supply your logs to them so they can understand what may be causing any issues you may encounter. This feature is also described in JasperReports Server Administrator Guide.

!!! note

    For information on contacting Technical Support, see [Troubleshooting Information for Technical Support](troubleshooting_information_for_tech.md).
