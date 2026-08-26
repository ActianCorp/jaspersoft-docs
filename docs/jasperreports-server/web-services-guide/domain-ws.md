---
title: SOAP - Domain Web Service
description: "With the completion of the REST v2 API in JasperReports® Server 5.5, Jaspersoft® announces the end of life of the SOAP web services. The SOAP web services will no longer be maintained or updated to..."
---

# SOAP - Domain Web Service

!!! warning

    With the completion of the REST v2 API in JasperReports® Server 5.5, Jaspersoft® announces the end of life of the SOAP web services. The SOAP web services will no longer be maintained or updated to support new features of the server.

!!! info "Important"

    This section describes functionality that can be restricted by the software license for JasperReports Server. If you don’t see some of the options described in this section, your license may prohibit you from using them. To find out what you're licensed to use, or to upgrade your license, contact Jaspersoft.

The Domain web service exposes a limited subset of JasperReports Server’s Domain functionality to integrating applications by the means of a dedicated web service. Applications may only read the contents of a Domain, not create or edit Domains.

The service works via XML-RPC calls that use the SOAP encoding. It uses the HTTP protocol to send and receive requests and responses. By default, it is deployed at `/services/DomainServices`. You can retrieve the WSDL document by appending `?wsdl` to the service URL. For example:

`http://localhost:8080/jasperserver-pro/services/DomainServices?wsdl`

This chapter contains the following sections:

-   [Types Defined in the WSDL](types_defined_in_the_wsdl1.md)
-   [Operations in the Domain Service](operations_in_the_domain_service.md)
