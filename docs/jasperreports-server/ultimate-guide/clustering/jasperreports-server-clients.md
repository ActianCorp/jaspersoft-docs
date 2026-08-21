---
title: JasperReports Server Clients
description: "JasperReports Server supports two fundamentally different client types:"
---

# JasperReports Server Clients

JasperReports Server supports two fundamentally different client types:

- Browser users – Through the web interface, users interact with all the features of JasperReports Server, such as viewing and scheduling reports. Working with Ad Hoc reports and Dashboards in product editions that provide these features is an interactive process with multiple requests to access data, display it, and modify its appearance. Users with the proper permissions can upload JasperReports and use the wizards to define the required resources.

- API clients – Applications that use the REST APIs and Visualize.js to access the features of JasperReports Server. For example, Jaspersoft Studio relies on the REST API to access the JasperReports Server repository for reading and writing reports and their associated resources. A web application might use the Visualize.js library to embed JasperReports and dashboards within its own UI. For more information, see the JasperReports Server REST API Reference and JasperReports Server Visualize.js Guide.

An API client is an application that sends requests programmatically, and the server performs an action or provides structured information in a reply to the client. API calls are generally stateless operations, meaning that an entire operation is performed in a single request and does not rely on any previous requests. Complex structures such as a report resource must be fully defined and managed by the client before being sent in a request, as opposed to the interactive nature of the browser user.

User sessions in a cluster are further explained in [Session Management and Failover](session-management-and-failover.md).

A significant task in the design of your cluster is to characterize client use, such as total number of potential clients, fraction of browser users and API clients, peak client load, average request size, and typical client bandwidth. This information will help you optimize the size and number of servers in your cluster to meet your service availability goals. For more information, see [Sizing a Cluster](sizing-a-cluster.md).
