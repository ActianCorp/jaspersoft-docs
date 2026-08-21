---
title: REST Authentication
description: "When using web services, the calling application must provide a valid user ID and password to JasperReports Server. The REST web services in JasperReports Server support two types of authentication:"
---

# REST Authentication

When using web services, the calling application must provide a valid user ID and password to JasperReports Server. The REST web services in JasperReports Server support two types of authentication:

- HTTP Basic Authentication, where the user ID and password are sent in the header with every request. Basic Authentication with REST is the same as described in section [SOAP Authentication](soap_authentication.md).
- The special login service that allows authentication using a POST request to create a session and return a session ID that is used with subsequent requests. Use of the login service is optional, and it is useful only when HTTP Basic Authentication does not work.

One example where you may need to use the login service is when the username or password contain UTF-8 characters that may be corrupted by the basic authentication mechanism.

Normally, RESTful implementations do not rely on the use of persistent sessions, such as the login service. However, the JasperReports Server architecture automatically creates user sessions internally, and the login service takes advantage of this. By using the login service, you can avoid making the server verify user credentials for each API call. If your server is configured with external authentication, repeatedly verifying credentials may be a performance issue you can avoid with the login service.
