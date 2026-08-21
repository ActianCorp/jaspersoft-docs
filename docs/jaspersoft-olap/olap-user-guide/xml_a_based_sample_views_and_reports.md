---
title: XML/A-based Sample Views and Reports Fail
description: Some of JasperReports Server’s sample views and reports demonstrate the ability to retrieve data using the XML/A protocol by loading data from the sample Foodmart and Sugar XML/A connections. Because...
---

# XML/A-based Sample Views and Reports Fail

Some of JasperReports Server’s sample views and reports demonstrate the ability to retrieve data using the XML/A protocol by loading data from the sample Foodmart and Sugar XML/A connections. Because XML/A client connections have to specify a port number in their URI value, the port numbers are hard-coded to the default for Apache Tomcat (8080). If your application server uses a different port number, these reports and views fail. For example, if WebSphere hosts your (commercial edition) server, and it uses its default port number (9080), the sample views and reports based on XML/A connections fail. Another example where this failure occurs is if you used a non-default port number for Apache Tomcat.

To use these samples, you must edit the XML/A connections and enter the correct port number. For instructions, refer to the JasperReports Server Installation Guide.

Note that the XML/A connection samples are contrived, in that they retrieve data from the local server, when XML/A is meant to retrieve data from remote OLAP sources.
