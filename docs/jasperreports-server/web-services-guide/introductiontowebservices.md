---
title: Introduction to Web Services
description: "JasperReports Server is a component of both a community project and commercial offerings. Each integrates the standard features such as security, scheduling, a web services interface, and much more..."
---

# Introduction to Web Services

!!! note

    JasperReports Server is a component of both a community project and commercial offerings. Each integrates the standard features such as security, scheduling, a web services interface, and much more for running and sharing reports. This guide discusses all editions. Sections of the guide that apply only to the commercial editions are indicated with a special note.

This document describes the JasperReports Server’s web services that allow client applications to interact with the server programmatically.

There are three different Application Programming Interfaces (APIs) using two different protocols:

-   REST (REpresentational State Transfer) – A RESTful interface depends on the standard methods provided by HTTP: GET, PUT, POST, and DELETE. The API sends and receives resource descriptors that are the object or result of the operation.

    -   REST v2 – Jaspersoft® has fully re-implemented the original REST API to improve performance and use simpler resource descriptors in JSON (JavaScript Object Notation). Jaspersoft strongly recommends using or upgrading to the REST v2 API for support of the latest features in JasperReports® Server.
    -   REST (v1) – The original REST API supports only XML descriptors, and it is not as efficient or simple to use. This interface is deprecated: it is still supported but is not enhanced with new features. The REST (v1) API may be unsupported and later removed in future versions of the server.

-   SOAP (Simple Object Access Protocol) – The SOAP interface sends and receives XML documents to describe operations, process requests and provide results. The SOAP interface is no longer supported nor maintained, but it is still included in JasperReports® Server for backwards compatibility. The SOAP API may be removed in future versions of the server.

    In order to describe the contents of resources in the repository, both REST and SOAP web services use a custom XML format called a `resourceDescriptor`. When the client requests information about resources, the server responds with lists of resource descriptors, and when the client creates or modifies a resource, it must send a well-formed `resourceDescriptor` that describes the resource. Newer RESTful APIs also support JSON (JavaScript Object Notation) objects.

    This chapter contains the following sections:

-   [REST Web Services Overview](rest_web_services_overview.md)

-   [REST Authentication](rest_authentication.md)

-   [REST Server Information](rest_server_information.md)

-   [SOAP Web Services Overview](soap_web_services_overview.md)

-   [SOAP Authentication](soap_authentication.md)

-   [Syntax of resourceDescriptor](syntax_of_resourcedescriptor.md)
