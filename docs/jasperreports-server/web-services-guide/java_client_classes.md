---
title: Java Client Classes
description: The JasperReports Server web service client jars contain classes that can be used by Java clients to easily communicate with the report scheduling web service.
---

# Java Client Classes

The JasperReports Server web service client jars contain classes that can be used by Java clients to easily communicate with the report scheduling web service.

XML types used by the report scheduling web service are mapped to Java bean classes found in the `weekday` package (for example, `Job`, `JobSimpleTrigger`, and `CalendarDaysType`). Instances of these classes can be used as report job objects that are sent to or returned by the web service.

The service itself is represented by Apache Axis-generated client stub classes. A façade (`com.jaspersoft.jasperserver.ws.scheduling.ReportSchedulerFacade`) has been developed on top of these classes. The façade can be instantiated by providing the information required to locate and connect to a web service (the endpoint URL and the username/password for authentication).

Jaspersoft recommends using the façade because it handles items such as the Axis client configuration and the messages locale header.
