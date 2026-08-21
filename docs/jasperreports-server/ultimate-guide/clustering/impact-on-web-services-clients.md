---
title: Impact on API Clients
description: "Applications can invoke to interact programmatically with JasperReports Server through the REST API and Visualize.js. API calls can also be interrupted by a node failure, but because operations are..."
---

# Impact on API Clients

Applications can invoke to interact programmatically with JasperReports Server through the REST API and Visualize.js. API calls can also be interrupted by a node failure, but because operations are quicker, consisting of a short request and almost immediate response, this is much less likely. Applications that call APIs should implement a reasonable timeout and verify the return value to determine if the server instance completed the operation or had a failure. In the case of a timeout or an error, the application should call the same operation again, which the load balancer should automatically direct to a remaining node.

In general, API calls are stateless, meaning the server does not store any information about the operation or the caller from one API request to the next. This is why APIs do not support interactive work such as designing an Ad Hoc view, a dashboard, a Domain, or exploring data in OLAP, all of which require the server to store an intermediate state.

In the case of the interactive wizards for creating and editing complex repository resources, API calls to do the equivalent operations are also stateless. When using APIs, the calling application has the responsibility to remember the state of the interaction between it and the server. For example, in the UI, an interactive wizard helps administrators define nested resources such as queries and input controls. When using web services, the client application must remember which nested resources have been created and how to reference them.

In practice, the REST API is not entirely stateless because it supports a login that allows the client to use the session cookie instead of HTTP authentication with every call. However, login information is included in the partially replicated session and therefore handled transparently in the case of node failure and failover. So if a login request completes on one node but that node eventually fails, the load balancer sends further requests to a new node that accepts the same session cookie because it has the partially replicated session.

There is one more case where web services rely on a session object: the JasperPrint object cannot be replicated, as explained in the following table.

| Non-Replicated Session Element | REST API Impacted by Failure |
|----|----|
| JasperPrint object from running a report | The initial call to the `rest_v2/reportExecutions` service runs a report and stores a JasperPrint object in the user session. Upon failover, subsequent calls to the same service will return an error. Your application must have logic to detect this error and perform the initial call again. |
