---
title: Instrumenting JasperReports Server for Tracing
description: Instrumentation is the process of adding annotations or new lines in the code to view traces when an issue has occurred within the application. It helps to identify major issues within the code by...
---

# Instrumenting JasperReports Server for Tracing

## Instrumentation

Instrumentation is the process of adding annotations or new lines in the code to view traces when an issue has occurred within the application. It helps to identify major issues within the code by instrumenting specific areas in the code.

There are two types of instrumentation:

-   **Auto Instrumentation**: Auto instrumentation uses the `opentelemetry-api` to view traces within the code. It creates a span for a method using the `@WithSpan` annotation for which it is annotated with within the code.

-   **Manual Instrumentation**: Manual instrumentation involves manually adding new lines of code. It uses `opentelemetry-api` and `opentelemetry-sdk` to view traces within the code.

The following span name and properties were instrumented in the code to view traces of spans in Jaeger:

-   `@WithSpan`: Adds annotation to view method names in Jaeger UI. This is an auto-instrumentation process for viewing method names.

-   `Span span = Span.current()`: It helps to create a span. This is a manual instrumentation process for creating span names.

-   `span.updateName()`: It changes the name of the method that appears in Jaeger.

-   `span.setAttribute()`: It filters out the spans in Jaeger based on the attributes.

-   `export OTEL_INSTRUMENTATION_HIBERNATE_ENABLED=false`: It suppresses the unwanted hibernate spans, which resulted in increasing the number of spans by setting this value to `false` in `tomcat\bin`.
