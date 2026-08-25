---
title: Configuring JasperReports Server
description: "After deploying the Scalable Query Engine through Docker and Kubernetes and verifying that the workers are active, you can configure your JasperReports Server instance to use the workers."
---

# Configuring JasperReports Server

After deploying the Scalable Query Engine through Docker and Kubernetes and verifying that the workers are active, you can configure your JasperReports Server instance to use the workers.

Locate the js.config.properties file in the server instance and set the `scalableQueryEngine.enabled` and `scalableQueryEngine.url` properties. You can also set other properties such as the number of connections and length of timeouts as shown in the file below. On the server instance, you can also set the environment variable `SCALABLE_QUERY_ENGINE_URL` to the hostname of the ingress load balancer.

When done, restart your JasperReports Server instance.

``` bash
# enables filter
scalableQueryEngine.enabled = true

# url where proxy servlet will redirect all calls (exposed from k8s), same as jrio.url
# for Docker-only deployment, use <worker_ip>:8081
scalableQueryEngine.url = http://<ingress_ip>:8088

# supported datasources
scalableQueryEngine.dataSourceTypes=
com.jaspersoft.jasperserver.api.metadata.jasperreports.domain.JdbcReportDataSource, com.jaspersoft.jasperserver.api.metadata.jasperreports.domain.JndiJdbcReportDataSource, com.jaspersoft.jasperserver.api.metadata.jasperreports.domain.CustomReportDataSource, com.jaspersoft.jasperserver.api.metadata.jasperreports.domain.AwsReportDataSource, com.jaspersoft.jasperserver.api.metadata.jasperreports.domain.AzureSqlReportDataSource

# periodic check of provided scalableQueryEngine.url to see if system is OK
scalableQueryEngine.livenessCheck.url = /actuator/health
scalableQueryEngine.livenessCheck.periodSeconds = 30

# in case of a failure execute on jrs, but these are only HTTP 50x errors and task rejection
scalableQueryEngine.recover.enabled = false

#Defines the socket timeout (SO_TIMEOUT) in milliseconds, which is the timeout for waiting for data or, put differently, a maximum period inactivity between two consecutive data packets).
#A timeout value of zero is interpreted as an infinite timeout. A negative value is interpreted as undefined (system default).
scalableQueryEngine.http.read.timeout=240000

#Returns the timeout in milliseconds used when requesting a connection from the connection manager. A timeout value of zero is interpreted as an infinite timeout.
#A timeout value of zero is interpreted as an infinite timeout. A negative value is interpreted as undefined (system default).#/** A integer parameter name to set the connection request timeout (millis) */
scalableQueryEngine.http.connectionrequest.timeout=120000

# A integer parameter name to set max connection number. Defines the overall connection limit for a connection pool. 10 by default is if not set
scalableQueryEngine.http.maxConnections=1000
scalableQueryEngine.http.maxConnectionsPerRoute=100

# Determines the timeout in milliseconds until a connection is established. A timeout value of zero is interpreted as an infinite timeout.
# A timeout value of zero is interpreted as an infinite timeout.
# A negative value is interpreted as undefined (system default).
scalableQueryEngine.http.connect.timeout=120000

# The CircuitBreaker uses a sliding window to store and aggregate the outcome of calls. In case of to manny errors either stop sending or go to recover, more options to cover
scalableQueryEngine.circuitBreaker.disabled = true
```
