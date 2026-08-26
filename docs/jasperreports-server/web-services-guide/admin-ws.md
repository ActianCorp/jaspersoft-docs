---
title: SOAP - Web Services for Administration
description: "With the completion of the REST v2 API in JasperReports® Server 5.5, Jaspersoft® announces the end of life of the SOAP web services. The SOAP web services will no longer be maintained or updated to..."
---

# SOAP - Web Services for Administration

!!! warning

    With the completion of the REST v2 API in JasperReports® Server 5.5, Jaspersoft® announces the end of life of the SOAP web services. The SOAP web services will no longer be maintained or updated to support new features of the server.

Web services for administration expose a limited set of JasperReports Server’s system administration functionality. There are three services:

-   Users and Roles

-   Organizations/Tenants

-   Permissions

    The services work via XML-RPC calls that use the SOAP encoding. They use the HTTP protocol to send and receive requests and responses. By default, they are deployed at `/services/UserAndRoleManagementService`, `/services/OrganizationManagementService`, and `/services/PermissionsManagementService`. You can retrieve the WSDL documents by appending `?wsdl` to the service URL. For example:

    `http://localhost:8080/jasperserver-pro/services/UserAndRoleManagementService?wsdl`

    If an exception occurs while processing an operation request, the exception is converted to a SOAP fault that is sent as its response. In this case, the exception stacktrace is included in the response, which can be useful for debugging.

    Exceptions thrown by JasperReports Server have localizable messages. The operation caller can specify the locale in which the messages of such exceptions are returned by setting a SOAP envelope header. The header should be named `locale` and should use `http://www.jasperforge.org/jasperserver/ws` as its namespace; the header value is a string representation of the desired message locale. For more information, refer to section [Request and Operation Result](request_and_operation_result.md).

    All authentication and authorization rules established in the system apply to operations run through the web services. Refer to Jasper Administrator Guide for more information about the rules.

    This chapter includes the following sections:

-   [Types Defined in the WSDL](types_defined_in_the_wsdl2.md)

-   [Users and Roles](users_and_roles.md)

-   [Organizations/Tenants](organizations_tenants.md)

-   [Permissions](permissions.md)

-   [Related Files](related_files.md)
