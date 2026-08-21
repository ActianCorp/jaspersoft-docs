---
title: SOAP - Report Scheduling Web Service
description: "With the completion of the REST v2 API in JasperReports® Server 5.5, Jaspersoft® announces the end of life of the SOAP web services. The SOAP web services will no longer be maintained or updated to..."
---

# SOAP - Report Scheduling Web Service

!!! warning

    With the completion of the REST v2 API in JasperReports® Server 5.5, Jaspersoft® announces the end of life of the SOAP web services. The SOAP web services will no longer be maintained or updated to support new features of the server.

The scheduling web service exposes JasperReports Server’s report scheduling functionality to integrating applications by the means of a dedicated web service. The web service is the equivalent of the API report scheduling service (`com.jaspersoft.jasperserver.api.engine.scheduling.service.ReportSchedulingService`) and exposes the same operations as this API service.

The service works via XML-RPC calls that use the SOAP encoding. It uses the HTTP protocol to send and receive requests and responses. By default, it is deployed at `/services/ReportScheduler`. You can retrieve the service WSDL (Web Service Description Language) document by appending `?wsdl` to the service URL. For example:

`http://localhost:8080/jasperserver-pro/services/ReportScheduler?wsdl`

This chapter includes the following sections:

- [Types Defined in the WSDL](types_defined_in_the_wsdl.md)
- [Operations in the Scheduling Service](operations_in_the_scheduling_service.md)
- [Java Client Classes](java_client_classes.md)
