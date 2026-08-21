---
title: Configuring OpenTelemetry and Jaeger Agent
description: You can configure the OpenTelemetry and Jaeger agent to view the traces in the JasperReports Server application and JasperReports Server cluster.
---

# Configuring OpenTelemetry and Jaeger Agent

You can configure the OpenTelemetry and Jaeger agent to view the traces in the JasperReports Server application and JasperReports Server cluster.

The configuration of the OpenTelemetry and Jaeger agent includes the following steps:

1.  Download [opentelemetry-javaagent.jar](https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/download/v1.26.0/opentelemetry-javaagent.jar).

2.  Download platform-dependent **OpenTelemetry Collector** from <https://github.com/open-telemetry/opentelemetry-collector-releases/releases>.

3.  Download Jaeger Tracing from <https://www.jaegertracing.io/download/> and run the Jaeger aggregator.

To configure step by step, see Setting up OpenTelemetry and Jaeger Agent on JasperReports Server Application and Setting up OpenTelemetry and Jaeger Agent on JasperReports Server Cluster.

## Setting up OpenTelemetry and Jaeger on JasperReports Server Application

This section includes the steps for setting up the OpenTelemetry and Jaeger agent on the JasperReports Server application. This configuration helps to view traces and spans of the JasperReports Server application.

### Prerequisites

The below prerequisites must be satisfied before configuring OpenTelemetry and Jaeger on the JasperReports Server application:

- JasperReports Server setup.

To configure OpenTelemetry and Jaeger in the JasperReports Server:

1.  Stop Tomcat service.

2.  Download [opentelemetry-javaagent.jar](https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/download/v1.26.0/opentelemetry-javaagent.jar) and then place this javaagent on the JasperReports Server node. The javaagent involves some useful libraries, which help in instrumenting the code.

3.  Go to the Tomcat bin directory of each JasperReports Server node and update the following arguments in the `setenv.sh` file of the Tomcat bin:

    - `export JAVA_OPTS`: Provide the correct path of the javaagent where the javaagent is placed.
    - `export OTEL_TRACES_EXPORTER`: Provide Jaeger exporter name as we are using Jaeger exporter to visualize the trace. You can provide the name of the respective exporter that you are using to visualize the traces.
    - `export OTEL_EXPORTER_JAEGER_ENDPOINT`: Provide the correct hostname with port number. If you are using localhost, then provide the localhost name else provide the hostname directly.
    - `export OTEL_RESOURCE_ATTRIBUTES=service.name`: In service name, provide `jasperserver-pro` service name.
    - `export OTEL_JAVAAGENT_DEBUG`: The default value is false for this argument and is not editable.
    - `export OTEL_METRICS_EXPORTER`: The default value is none for this argument and is not editable.

```
export JAVA_OPTS="$JAVA_OPTS -javaagent:/opt/jaeger/opentelemetry-javaagent.jar"
export OTEL_TRACES_EXPORTER=jaeger
export OTEL_EXPORTER_JAEGER_ENDPOINT=http://hostname:14250
export OTEL_RESOURCE_ATTRIBUTES=service.name=jasperserver-pro
export OTEL_JAVAAGENT_DEBUG=false
export OTEL_METRICS_EXPORTER=none
```

!!! note

    Ensure that the correct path of the javaagent and hostname is provided in the `stenv.sh` file.

4.  Download Jaeger using <https://www.jaegertracing.io/download/> on the JasperReports Server node. As a result, Jaeger gets downloaded in ZIP format.

5.  Extract the Jaeger package and go to the location under which the `jaeger-all-in-one` is placed.

6.  Open the command prompt and run ` ./jaeger-all-in-one --collector.zipkin.host-port=:9411 &` command to start the Jaeger application.

!!! note

    Before setting up the javaagent and Jaeger file, ensure that the root user has setup OTel and Jaeger in the respective folders and assigned permissions for the jasperserver user. If no files are set up, then the application misbehaves. In such cases, start the service by logging as a `jasperserver` user.

7.  Start the Tomcat service to access Jaeger using the JasperReports Server URL: `http://<hostname>:16686` to see traces of the JasperReports Server application node. As a result, Jaeger gets successfully configured with JasperReports Server and Jaeger running in two separate tabs in the browser.

!!! note

    To view traces of the load balancer, replace the hostname(`http://<hostname>:16686`) with the load balancer URL.

## Setting up OpenTelemetry and Jaeger on JasperReports Server Cluster

This section includes steps for setting up the OpenTelemetry and Jaeger agent on the JasperReports Server cluster environment. This configuration helps to view the traces and spans for each node of the JasperReports Server cluster.

### Prerequisites

The below prerequisites must be satisfied before configuring OpenTelemetry and Jaeger on the JasperReports Server cluster environment:

- JasperReports Server cluster setup.

To configure OpenTelemetry and Jaeger in the JasperReports Server cluster environment:

1.  Stop Tomcat service.

2.  Download [opentelemetry-javaagent.jar](https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/download/v1.26.0/opentelemetry-javaagent.jar) and then place this javaagent on all the JasperReports Server User Guidenodes of the cluster. The javaagent involves some useful libraries that help in instrumenting the code.

3.  Go to the Tomcat bin directory of each JasperReports Server node and update the following arguments in the setenv.sh file of the Tomcat bin:

    - `export JAVA_OPTS`: Provide the correct path of the javaagent where the javaagent is placed.
    - `export OTEL_TRACES_EXPORTER`: Provide Jaeger exporter name as we are using Jaeger exporter to visualize the trace. You can provide the name of the respective exporter that you are using to visualize the traces.
    - `export OTEL_EXPORTER_JAEGER_ENDPOINT`: Provide the correct hostname with port number. If you are using localhost, then provide the localhost name else provide the hostname directly.
    - `export OTEL_RESOURCE_ATTRIBUTES=service.name`: In service name, provide jasperserver-pro service name.
    - `export OTEL_JAVAAGENT_DEBUG`: The default value is false for this argument and is not editable.
    - `export OTEL_METRICS_EXPORTER`: The default value is none for this argument and is not editable.

    !!! note

        Ensure that the correct path of the javaagent and hostname is provided in the stenv.sh file.

    ``` text
    export JAVA_OPTS="$JAVA_OPTS -javaagent:/opt/jaeger/opentelemetry-javaagent.jar"
    export OTEL_TRACES_EXPORTER=jaeger
    export OTEL_EXPORTER_JAEGER_ENDPOINT=http://hostname:14250
    export OTEL_RESOURCE_ATTRIBUTES=service.name=jasperserver-pro
    export OTEL_JAVAAGENT_DEBUG=false
    export OTEL_METRICS_EXPORTER=none
    ```

!!! note

    In the above code snippet, ensure the `OTEL_EXPORTER_JAEGER_ENDPOINT` option should have the URL of the JasperReports Server Load balancer and the `-javaagent` option should have the correct path where the OpenTelemetry javaagent is stored.

4.  Login to Load balancer node and download Jaeger on the JasperReports Server node using - <https://www.jaegertracing.io/download/>. As a result, Jaeger gets downloaded in ZIP format.

5.  Extract the Jaeger package and go to the location under which the `jaeger-all-in-one` is placed.

6.  Open the command prompt and run `./jaeger-all-in-one --collector.zipkin.host-port=:9411 &` command to start the Jaeger application.

    !!! note

        Before setting up the javaagent and Jaeger files, ensure that the root user has setup OTel and Jaeger in the respective folders and assigned permissions for the jasperserver user. If no files are set up, then the application misbehaves. In such cases, start the service by logging as a jasperserver user.

7.  Start the Tomcat service to access Jaeger using the JasperReports Server URL: http://\<hostname\>:16686 to see traces of the JasperReports Server application node. As a result, Jaeger gets successfully configured with JasperReports Server and Jaeger running in two separate tabs in the browser.

    !!! note

        To view traces of the Load balancer, replace the hostname (http://\<hostname\>:16686) with the load balancer URL.

By default, Jaeger shows traces of all the nodes of the JasperReports Server cluster. To view the spans and traces of a specific node of the cluster, segregate the traces of the specific node using the host.name tag under the tags option in Jaeger UI.

For example, to view traces of the specific node in the Jaeger UI, enter the `"host.name=na2devjaspf831"` tag under the tags option. As a result, the traces and spans of the mentioned node having the `" host.name=na2devjaspf831"` tag is displayed.
