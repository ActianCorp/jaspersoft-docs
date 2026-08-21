---
title: Operations in the Domain Service
description: "The Domain web service provides the following operations:"
---

# 1.1 Operations in the Domain Service

The Domain web service provides the following operations:

- `getDomainMetaData`. Returns the tree structure of sets and items in a Domain. The object returned can be used to render the Domain for users and allow them to select items for a query.
- `executeDomainQuery`. Returns a set of values in response to a query.

If an exception occurs while processing an operation request, the exception is converted to a SOAP fault that is sent as its response. In this case, the exception stacktrace is included in the response, which can be useful for debugging.

Exceptions thrown by JasperReports Server have localizable messages. The operation caller can specify the locale in which the messages of such exceptions are returned by setting a SOAP envelope header. The header should be named `locale` and should use` http://www.jasperforge.org/jasperserver/ws` as its namespace; the header value is a string representation of the desired message locale. For more information, see [section , “Request and Operation Result,” on page 1](request_and_operation_result.md).
