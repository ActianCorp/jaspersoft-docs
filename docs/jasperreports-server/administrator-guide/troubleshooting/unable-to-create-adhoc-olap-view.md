---
title: Unable to Create Ad Hoc or OLAP View Using OLAP Client Connection
description: "While creating an OLAP view using an OLAP client connection, an error is displayed:"
---

# Unable to Create Ad Hoc or OLAP View Using OLAP Client Connection

While creating an OLAP view using an OLAP client connection, an error is displayed:

``` text
ERROR ErrorPageHandlerAction,http-nio-8080-exec-1:118 - Error UID 2a0ea859-a839-466a-9d9c-02570a9c6a3a jakarta.servlet.ServletException: Handler dispatch failed: java.lang.NoClassDefFoundError: org/apache/commons/dbcp/ConnectionFactory
```

Similarly, while creating an Ad Hoc view using an OLAP client connection, an error is displayed:

``` yaml
com.jaspersoft.jasperserver.api.JSException: error loading olap4j driver and getting Connection 'mondrian.olap4j.MondrianOlap4jDriver' arguments:
```

This is because of the `dbcp-2` upgrade. The used Mondrian version has dependency on `dbcp-1` and `dbcp-1 jar` is not bundled along.

To fix this:

1.  Download `commons-dbcp-1.4.jar` from the [Maven central repository](https://mvnrepository.com/artifact/commons-dbcp/commons-dbcp/1.4).

2.  Place the jar file in `jasperserver-pro/WEB-INF/lib`.

3.  Restart Tomcat.
