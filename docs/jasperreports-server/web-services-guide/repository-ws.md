---
title: SOAP - Repository Web Service
description: "With the completion of the REST v2 API in JasperReports® Server 5.5, Jaspersoft® announces the end of life of the SOAP web services. The SOAP web services will no longer be maintained or updated to..."
---

# SOAP - Repository Web Service

!!! warning

    With the completion of the REST v2 API in JasperReports® Server 5.5, Jaspersoft® announces the end of life of the SOAP web services. The SOAP web services will no longer be maintained or updated to support new features of the server. In particular, the SOAP web services do not support interactive charts or interactive HTML5 tables.

The repository web service is comprised of seven methods: `list`, `get`, `put`, `move`, `copy`, `delete`, and `runReport`.

You can retrieve the WSDL (Web Services Description Language) document that describes the repository service by invoking the URL of the service and appending the string `?wsdl`. For example:

`http://localhost:8080/jasperserver-pro/services/repository?wsdl`

This chapter contains the following sections:

- [Request and Operation Result](request_and_operation_result.md)
- [List Operation](list_operation.md)
- [Get Operation](get_operation.md)
- [Put Operation](put_operation.md)
- [Delete Operation](delete_operation.md)
- [Move Operation](move_operation.md)
- [Copy Operation](copy_operation.md)
- [runReport Operation](runreport_operation.md)
- [Errors](errors.md)
- [Implementation Suggestions](implementation_suggestions.md)
