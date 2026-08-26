---
title: Operations in the Scheduling Service
description: "The report scheduling web service consists of the following operations:"
---

# Operations in the Scheduling Service

## Operation Descriptions

The report scheduling web service consists of the following operations:

-   `getAllJobs`. Returns the list of all accessible report jobs.
-   `getReportJobs`. Returns the list of all accessible report jobs for a specific report (whose URL is sent as a parameter).
-   `scheduleJob`. Schedules a new job. The job details must be sent as parameters; the operation returns the saved job details as its result.
-   `updateJob`. Updates an existing job. The full job details (as retrieved via `getJob`) must be sent as a parameter; the operation returns the updated job details as saved by the JasperReports Server scheduling service.
-   `getJob`. Returns the full job details of a report job whose ID is sent as a parameter.
-   `deleteJob` and `deleteJobs`. Delete a single or several report job specified by their IDs. These operations do not return any information.

If an exception occurs while processing an operation request, the exception is converted to a SOAP fault which is sent as its response. In this case, the exception stacktrace is included in the response, and can be used for debugging.

Exceptions thrown by the JasperReports Server code have localizable messages. The operation caller can specify the locale in which the messages of such exceptions are returned by setting a SOAP envelope header. The header should be named `locale` and should use` http://www.jasperforge.org/jasperserver/ws` as namespace; the header value is a string representation of the desired message locale. For more information, refer to [Request and Operation Result](request_and_operation_result.md).
