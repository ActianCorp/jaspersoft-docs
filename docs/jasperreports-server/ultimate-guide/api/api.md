---
title: JasperReports Server APIs
description: "One of the main goals of JasperReports Server is to expose a set of reusable application programming interfaces (APIs) that are easy to understand, extend, and customize. This facilitates adapting..."
---

# JasperReports Server APIs

One of the main goals of JasperReports Server is to expose a set of reusable application programming interfaces (APIs) that are easy to understand, extend, and customize. This facilitates adapting JasperReports Server to the unique requirements of different deployments.

We provide two types of APIs. The client APIs are used to create other applications that call functionality on the server. The server APIs are used to customize and extend the server itself.

The client APIs enable you to embed BI functionality into your own application. With these APIs you can access the server, browse its repository, set input controls, and run reports. The client APIs depend on a configured and running instance of the JasperReports Server. The client APIs have different uses depending on what functionality that you need and which protocol you want to use. They are described in the following sections:

-   [Web Services APIs](web-services-apis.md)

-   [Visualize.js API](visualize-js.md)

-   [Repository HTTP API](repository-http-api.md)

The server APIs are the public interfaces and classes that can be used to extend or customize the behavior of the server itself. Using the server APIs, you can write classes that change the behavior and/or the user interface of the server. Depending on which behavior you want to extend or customize, you can either integrate your code through the Spring framework and redeploy the server or work with the source code distribution and recompile the whole server. The server APIs are described in [The Public JasperReports Server API.](java-apis.md)
