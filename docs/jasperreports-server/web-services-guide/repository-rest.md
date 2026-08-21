---
title: REST v1 - Repository Services
description: "This chapter documents the HTTP methods (sometimes called verbs) and parameters for each of these requests. In every case, you specify the folder, resource, or report to be acted up by adding its..."
---

# REST v1 - Repository Services

This chapter documents the HTTP methods (sometimes called verbs) and parameters for each of these requests. In every case, you specify the folder, resource, or report to be acted up by adding its repository URI to the request URL. This chapter uses the following notation:

http://\<host\>:\<port\>/jasperserver\[-pro\]/rest/\<service\>/path/to/object

Arguments are passed in the URL with the conventional syntax:

http://\<host\>:\<port\>/jasperserver\[-pro\]/rest/\<service\>/path/to/object?\<arg1\>=\<value\>&\<arg2\>=\<value\>&...

The documentation for each method gives the list of arguments it supports. Optional arguments are listed with a question mark after the name, for example `<arg2>?`. Arguments that are not marked optional are mandatory and must be included in the URL with a valid value.

For authentication using the REST web services, see section [REST Authentication](rest_authentication.md).

The RESTful repository services gives responses that contain the same XML data structure that are used in the SOAP repository web service. These data structures are shown as examples throughout the chapter and documented in section [Syntax of resourceDescriptor](syntax_of_resourcedescriptor.md), with reference material in [ResourceDescriptor API Constants](api-constants.md).

This chapter includes the following sections:

- [The resources Service](the_resources_service.md)
- [The resource Service](the_resource_service.md)
- [Working with Dashboards](working_with_dashboards.md)
- [Working with Virtual Data Sources](working_with_virtual_data_sources.md)
- [Working with Domains](working_with_domains.md)
- [The permission Service](the_permission_service.md)
