---
title: Performance Tuning
description: "For a simple application with a relatively small dataset for which performance is not critical, (for example, a small intranet application or developer environment), the simplest server configuration..."
---

# Performance Tuning

For a simple application with a relatively small dataset for which performance is not critical, (for example, a small intranet application or developer environment), the simplest server configuration is to run a single application server that connects to a local database, which contains both the data being analyzed (that is, the operational data store) and the JasperReports Server repository database. However, this configuration does not perform under a large load. This section describes steps that you can take to improve performance for larger implementations and data sets.

For larger analysis applications, the ROLAP database is often a performance bottleneck. In this case, dedicate a computer to host the ROLAP database, and configure JasperReports Server to access it. The database and its host should be optimized for disk read and write. This separation of the application from the data is sufficient for many implementations.

To improve performance further, separate the Jaspersoft OLAP user interface from other elements. Inside Jaspersoft OLAP, the application that visualizes your results and provides navigation (through a user interface or an XML/A client) competes for resources with the analysis engine (Mondrian). To separate these processing resources, run two different instances of Jaspersoft OLAP: one that handles navigation tasks, and another that handles Mondrian's. The former instance is called the XML/A client. The latter is called the XML/A provider (or XML/A server). In the XML/A provider, define Mondrian connections that point to your operational data store. Then define XML/A connections in the XML/A client that point to Mondrian connections in the XML/A provider.

In this configuration, your users connect to the XML/A client, which sends XML/A requests to the XML/A provider, which in turn connects to the database (using a Mondrian connection) to retrieve the results. It returns the results to the XML/A client. The XML/A client then provides visualization and navigation for your end users.

In this configuration, Mondrian and navigation user interface or XML/A client do not compete for resources, and performance in large implementations is improved. For more information, see [Working with XML/A Connections](working_with_xml_a_connections.md) and [Working with XML/A Sources](working_with_xml_a_sources.md). More detailed information about performance tuning, including load-balancing multiple Jaspersoft OLAP instances in a single deployment, is also found in the Jaspersoft OLAP Ultimate Guide.

!!! note

    When connecting to a remote server using XML/A, the performance may be impaired the first time the data is loaded into the cache. The cache is loaded the first time data is requested from the remote server, and is subsequently refreshed based on your configuration. For details, refer to [Configuring the XML/A Cache](configuring_the_xml_a_cache.md).
