---
title: REST API
description: "Through the REST API, your application can query a running instance of JasperReports Server to display repository contents and run reports embedded in your application's own UI. This section gives a..."
---

# REST API

Through the REST API, your application can query a running instance of JasperReports Server to display repository contents and run reports embedded in your application's own UI. This section gives a brief summary of the API. For complete documentation, see the JasperReports Server REST API Reference.

The REST (Representational State Transfer) API depends on the standard methods provided by HTTP: GET, PUT, POST, and DELETE. Using the API, you can create client applications on any platform to access the server, interact with its resources, run reports and, with the right permissions, administer the server. Client applications send requests to named URLs that are called services.

The REST services in JasperReports Server 10.1 include:

-   Repository services: Search the repository; create, modify, and delete resources; view and set permissions on repository objects; and import and export repository catalogs.

-   Report services: Run reports and access report output; access and manipulate report options and input controls; and work with scheduled jobs.

-   Administration services: Work with users and user attributes, roles and role membership, and organizations in commercial editions.

Jaspersoft also publishes a PHP client for embedding reports in PHP applications. The PHP client provides a wrapper for the REST API, so developers can use simple PHP structures and syntax to access JasperReports Server. For more information, see the [PHP client community project](http://community.jaspersoft.com/project/php-client).
