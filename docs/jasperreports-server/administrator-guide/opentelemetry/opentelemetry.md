---
title: OpenTelemetry
description: "OpenTelemetry (OTel) is an observability framework and toolkit designed to create and manage telemetry data such as traces, metrics, and logs. It is a collection of APIs, SDKs, and tools to..."
---

# OpenTelemetry

OpenTelemetry (OTel) is an observability framework and toolkit designed to create and manage telemetry data such as traces, metrics, and logs. It is a collection of APIs, SDKs, and tools to instrument, generate, and export telemetry data. It provides an overview of the performance and behavior of your application. OTel analyzes the internal state of an application by collecting the data, analyzes the data(or logs), and shows the traces of the logs in Jaeger.

OpenTelemetry performs the following functionality:

- **Instrument data** - The data is instrumented by adding [Annotations](annotations.md) or new lines in the code, which help to instrument the code. The instrumentation can be either Manual or Automated. For more information, see [Instrumentation](instrumenting_jasperreportsserver_for_tracing.md).
- **Generate data** - The instrumented data is captured using a `javaagent` jar, which is specific to the Java language. The `javaagent` jar collects the instrumented data emitted by the code.
- **Export data** - The collected data, which is emitted by the code is then exported and visualized using the Jaeger exporter tool.

## Traces

Traces are helpful in finding out the reason behind the slow performance of the application. Traces help you to understand the complete path and find out what happens when an API request is made to an application. It captures the exact spans or places in the code where the problem occurred.

### Why tracing is necessary?

Tracing helps to investigate performance problems with JasperReports Server. Typically, we have noticed that the response time for running a report in JasperReports Server application was taking longer than usual. This problem might be because of the slow query, which is taking time to execute and deliver back the response. To discover the root cause of the problem in JasperReports Server, it is necessary to implement tracing.

For example, an application performance is slow than usual for a longer time. An application can be slow due to any of the reasons such as it took a lot of time to retrieve data from the network or database took some time to run queries. To find out the reason behind an application slow performance, logs are analyzed to see if there are any errors.

When no errors could be found in the logs, and the root cause remain unknown, then enabling tracing helps to detect the unknown issues. Tracing identifies the slow queries, captures the exact places (spans), and the time spent in the specific area of the code. Therefore, configuring OTel optimizes all such unknown issues and helps in improving the overall code quality and performance of the application.

You can configure OpenTelemetry in the JasperReports Server to overcome the performance issues in the application by enabling tracing.

See [Use cases](usecases_community.md) to understand how enabling tracing helped to improve the performance of the JasperReports Server application for Scheduler and Input Control dialog.

Before enabling tracing, you must first download and run a third-party agent, collector, and aggregator. For more information, see [Configuring OpenTelemetry and Jaeger Agent](configuring_opentelemetry_and_jaegar.md).

## Spans

Spans represent smaller chunks of operation or a unit of work performed within an API request. All operations within an API request are considered as span. OpenTelemetry uses a visualization tool called Jaeger to view the smaller chunks of operation or spans. Spans include the total API execution time, start time of methods, and hidden errors of the code in the logs.

For more information on OpenTelemetry, visit the official website of [https://opentelemetry.io/docs](https://opentelemetry.io/docs/).
