---
title: Use cases
description: This section includes scenarios when tracing helped to improve the performance issues in the JasperReports Server application for Scheduler and Input Controls.
---

# Use cases

This section includes scenarios when tracing helped to improve the performance issues in the JasperReports Server application for Scheduler and Input Controls.

## Tracing Report execution triggered by Scheduler

When running a report in JasperReports Server, Scheduler took a longer duration than usual to run a report, which resulted in performance issues in JasperReports Server.

We examined the application server logs to find out the issue, but could not detect anything in the application server logs. This issue was later detected on enabling tracing. Enabling tracing helped to detect the slow queries by capturing the exact places (spans) and the time spent in each major code area.

The following figure shows an example of the errors captured for the JasperReports Server Scheduler in Jaeger UI along with the logs. In this way all the hidden errors that remained undetected in the application server logs were found in Jaeger UI.

![Error captured using OTel in Jaeger UI](../assets/images/Error-captured-using-OTel-in-Jaeger-UI.png)

Example of Error Captured by OpenTelemetry in Jaeger UI

![Error logs captured using OTel](../assets/images/Error-logs-captured-using-OTel.png)

Example of Logs Captured by OpenTelemetry in Jaeger UI

## Tracing the execution of Report with Input Controls

When running a report in JasperReports Server, the Input Controls dialog remained open for too long, which resulted in slow performance of the JasperReports Server application. We examined the application server logs to find out the issue, but could not detect anything in the application server logs. This issue was later detected on enabling tracing.

Tracing helped to capture the time spent for running SQL queries of Input Control. This helped to find out the total time taken to resolve all the values and deliver them back in the REST API response.

Enabling tracing of the report execution helps to find slow SQL queries, and can help to determine if these queries were sent by report or Input Controls. In Jaeger UI you can look for slow queries by checking the start time, total execution time, and the duration of each span.

To enable tracing, you need to configure OpenTelemetry and Jaeger agents on the JasperReports Server application and cluster. For more details, refer to JasperReports Server Administrator Guide.
