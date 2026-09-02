---
title: Deploying with Kubernetes
description: "After configuring and building the Docker images, the next step is to configure Kubernetes and Helm charts to deploy the worker pods."
---

# Deploying with Kubernetes

After configuring and building the Docker images, the next step is to configure Kubernetes and Helm charts to deploy the worker pods.

In the git project, jaspersoft-containers/K8s/scalableQueryEngine/helm/ contains the following files and folders:

| File or Folder | Description |
|----|----|
| `Chart.yaml` | Helm chart for the scalable query engine. |
| `values.yaml` | Configuration values for the Helm chart. |
| `charts` | Folder containing dependencies. |
| `config/jndi.properties` | Configuration file for JNDI data sources. |
| `secret/keystore` | Folder where you place a copy of the JasperReports Server keystore. |

## Creating a Secret

The configuration files in this section contain passwords for your server and databases. If you store passwords in files, you should manage your permissions carefully to prevent unwanted access. An alternative is to store passwords in a secret, a separate data structure managed by Kubernetes. For details about the secrets, see the [Kubernetes documentation](https://kubernetes.io/docs/concepts/configuration/secret/).

Use the following command to create a secret containing your passwords. Note that commands are often stored in a history, therefore it is best to create a script to run these commands:

``` text
kubectl create secret generic jrs-credentials --from-literal=appCredentialsSecretName=password
        --from-literal=foodmart.password=password --from-literal=audit.password=password
```

You can then reference this secret inside the configuration files, for example:

``` properties
appCredentialsSecretName=jrs-credentials
```

## Configuring the Helm Chart

The tables in this section describe the properties that you can set in the values.yaml file.

General settings:

| Property | Description |
|----|----|
| `replicaCount` | The number of workers to be created, but has no effect if autoscaling is enabled. The default is `1`. |
| `jrsVersion` | The version of your JasperReports Server release, by default `8.0.0`. |
| `image.tag` | Tag of the scalable query engine Docker image, by default `8.0.0`. |
| `image.name` | Name of the scalable query engine Docker image, which should be `scalable-query-engine`. |
| `image.pullPolicy` | The Docker image pull policy, by default `IfNotPresent`. |
| `image.PullSecrets` | If you have customized your Docker image to [pull from a private registry](https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/), specify the secret here, otherwise leave null. |
| `image.nameOverride` | Overrides the default image name. Can be left as `""`. |
| `image.fullnameOverride` | Overrides the full image name. Can be left as `""`. |

The data source properties have default values for the foodmart and sugarcrm sample data sources that you can use with the sample dashboards. In production, you should redefine `config/jndi.properties` for your own data sources as shown in [Specifying JNDI Data Sources](#specifying-a-jndi-data-source), and then set the corresponding values here.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Property</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>foodmart.jdbcUrl</code></p></td>
<td><p>The default URL of the foodmart data source.</p></td>
</tr>
<tr>
<td><p><code>foodmart.username</code></p></td>
<td><p>The username to access the foodmart data source, by default <code>postgres</code>.</p></td>
</tr>
<tr>
<td><p><code>foodmart.password</code></p></td>
<td><p>The password for the foodmart data source user. The default is <code>postgres</code>, but it must be entered in base64 encoded format.</p></td>
</tr>
<tr>
<td><p><code>sugarcrm.jdbcUrl</code><br />
<code>sugarcrm.username</code><br />
<code>sugarcrm.password</code></p></td>
<td><p>URL, password, and username for the sugarcrm sample data source, in the same format as foodmart. The default values are also <code>postgres</code>.</p></td>
</tr>
<tr>
<td><p><code>audit.enabled</code></p></td>
<td><p>Whether audit monitoring is enabled on JasperReports Server, the default is false. When set to true, workers attempt to write audit events to the database specified below.</p></td>
</tr>
<tr>
<td><p><code>audit.jdbcUrl</code></p></td>
<td><p>The URL of the database for writing audit events, by default this is the same as the server's repository. If you have a split installation with a separate audit database, specify its URL instead.</p></td>
</tr>
<tr>
<td><p><code>audit.userName</code></p></td>
<td><p>The username to access the audit database.</p></td>
</tr>
<tr>
<td><p><code>audit.password</code></p></td>
<td><p>The password to access the audit database, in base64 encoded format.</p></td>
</tr>
<tr>
<td><p><code>appCredentialsSecretName</code></p></td>
<td><p>Instead of storing passwords in this file, you can manually create a secret to store the server password. See <a href="#creating-a-secret">Creating a Secret</a>.</p></td>
</tr>
</tbody>
</table>

The following table contains the environment properties for the workers. For more information, see the Kubernetes documentation links in the descriptions. There are additional properties in the file `templates/app-configmap.yml`, mainly for the Spring configuration on the workers.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Property</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>timeZone</code></p></td>
<td><p>The default timezone that the workers use when processing reports, for example <code>"America/Los_Angeles"</code>. The time zone names are those supported by <code>java.time.ZoneID</code>, which are defined in the <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones">tz database</a>.</p></td>
</tr>
<tr>
<td><p><code>securityContext.</code><br />
<code>capabilities.drop</code></p></td>
<td><p>Drops the Linux host capabilities. The default value is <code>ALL</code>. See the Kubernetes documentation about the <a href="https://kubernetes.io/docs/tasks/configure-pod-container/security-context/">security context</a>.</p></td>
</tr>
<tr>
<td><p><code>securityContext.</code><br />
<code>runAsNonRoot</code></p></td>
<td><p>Runs the worker application as a non-root user when true (the default).</p></td>
</tr>
<tr>
<td><p><code>securityContext.</code><br />
<code>runAsUser</code></p></td>
<td><p>Specifies the user id to run the worker application. The default is <code>11099</code>.</p></td>
</tr>
<tr>
<td><p><code>securityContext.</code><br />
<code>allowPrivilegeEscalation</code></p></td>
<td><p>Whether to allow the container to have host privileges. The default is <code>false</code>.</p></td>
</tr>
<tr>
<td><p><code>Service.type</code></p></td>
<td><p>The <a href="https://kubernetes.io/docs/concepts/services-networking/service/#defining-a-service">service type</a> for workers should be <code>ClusterIP</code>.</p></td>
</tr>
<tr>
<td><p><code>Service.port</code></p></td>
<td><p>The service port should be set to <code>8080</code>.</p></td>
</tr>
<tr>
<td><p><code>serviceAccount.enabled</code></p></td>
<td><p>Enables the <a href="https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/">service account</a> on the workers; <code>true</code> by default.</p></td>
</tr>
<tr>
<td><p><code>serviceAccount.annotations</code></p></td>
<td><p>Annotations for the service account; empty <code></code> by default.</p></td>
</tr>
<tr>
<td><p><code>serviceAccount.name</code></p></td>
<td><p>Name of the service account, by default <code>query-engine</code>.</p></td>
</tr>
<tr>
<td><p><code>rbac.create</code></p></td>
<td><p>Whether to create a role to use <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/">role-based access control</a>; true by default.</p></td>
</tr>
<tr>
<td><p><code>rbac.name</code></p></td>
<td><p>Name of the role; the default should be <code>query-engine-role</code>.</p></td>
</tr>
<tr>
<td><p><code>extraEnv.javaopts</code></p></td>
<td><p>String to add JAVA_OPTS to the worker's <a href="https://kubernetes.io/docs/tasks/inject-data-application/define-environment-variable-container/">environment variables</a>.</p></td>
</tr>
<tr>
<td><p><code>extraEnv.normal</code></p></td>
<td><p>Additional key=value pairs to add to environment variables. There is none by default (null value).</p></td>
</tr>
<tr>
<td><p><code>extraEnv.secrets</code></p></td>
<td><p>Specify environment variables in <a href="https://kubernetes.io/docs/concepts/configuration/secret/#using-secrets-as-environment-variables">secrets</a> or <a href="https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/">configmaps</a>. There are none by default (null value).</p></td>
</tr>
<tr>
<td><p><code>extraVolumeMounts</code></p></td>
<td><p>Adds volume mounts for <a href="https://kubernetes.io/docs/concepts/storage/volumes/">storage volumes</a>; empty <code></code> by default.</p></td>
</tr>
<tr>
<td><p><code>extraVolumes</code></p></td>
<td><p>Adds storage volumes; empty <code></code> by default.</p></td>
</tr>
</tbody>
</table>

Health check properties:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Property</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>healthcheck.enabled</code></p></td>
<td><p>Enables the health check so Kubernetes can detect when workers are busy or down. The default is true. See the Kubernetes documentation on <a href="https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#configure-probes">liveness and readiness probes</a>.</p></td>
</tr>
<tr>
<td><p><code>healthcheck.</code><br />
<code>livenessProbe.*</code></p></td>
<td><p>The liveness probe checks whether the worker is blocked or has crashed. It has the following properties:</p>
<ul>
<li><code>port</code>: Port of the worker, by default 8080.</li>
<li><code>initialDelaySeconds</code>: Time after startup when the probe begins checks, by default 120 (2 minutes).</li>
<li><code>failureThreshold</code>: How many failures before the worker is restarted (or marked unready), by default 24 times the period of the check.</li>
<li><code>periodSeconds</code>: How often the check is performed, by default 10 seconds.</li>
<li><code>timeoutSeconds</code>: How long the probe waits for a response before failing the check, by default 4 seconds.</li>
</ul></td>
</tr>
<tr>
<td><p><code>healthcheck.</code><br />
<code>readinessProbe.*</code></p></td>
<td><p>The readiness probe checks when the worker is running but unable to process requests. It has the same properties and defaults as the liveness probe, except the value of <code>initialDelaySeconds</code> is 60 (one minute).</p></td>
</tr>
</tbody>
</table>

CPU and memory resources:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Property</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>resources.enabled</code></p></td>
<td><p>Whether the <a href="https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/">resource requests and limits</a> are applied, by default <code>true</code>.</p></td>
</tr>
<tr>
<td><p><code>resources.limits.cpu</code></p></td>
<td><p>The most CPUs that each worker is allowed to use, by default <code>3</code>.</p></td>
</tr>
<tr>
<td><p><code>resources.limits.memory</code></p></td>
<td><p>The most memory that each worker is allowed to use, by default, 4Gi (gibibytes).</p></td>
</tr>
<tr>
<td><p><code>resources.requests.cpu</code></p></td>
<td><p>The least number of CPUs that will be available to the worker, by default 2.</p></td>
</tr>
<tr>
<td><p><code>resources.requests.memory</code></p></td>
<td><p>The least amount of memory that will be available to the worker, by default <code>2 Gi</code> (gibibytes).</p></td>
</tr>
<tr>
<td><p><code>engineProperties.</code><br />
<code>sharedCacheExpiration</code></p></td>
<td><p>The length of time that cache contents are valid, by default <code>20m</code> (minutes). Set this value depending on your dataset size, data update intervals, and repeated report viewing. Longer cache expiration speeds up report display times, but it takes up cache space and may not display instantaneous data.</p>
<p>There is also an issue with saved report options that do not apply if the report has run with previous values and is still in the cache. If you are having issues with report options not being applied in a report, lower the cache expiration, for example to 5m. The new values will apply when the report is generated after the previous report expires in the cache.</p></td>
</tr>
</tbody>
</table>

Ingress load balancer:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Property</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>ingress.enabled</code></p></td>
<td><p>Whether the ingress load balancer is enabled, allowing the cluster to have multiple pods and implement stickyness, the default is <code>true</code>.</p></td>
</tr>
<tr>
<td><p><code>ingress.hosts.host</code></p></td>
<td><p>Adds the valid DNS hostname to access the scalable query engine, by default <code>null</code> (no value).</p></td>
</tr>
<tr>
<td><p><code>ingress.hosts.paths.</code><br />
<code>path</code></p></td>
<td><p>Application context path, by default <code>/query-engine</code>.</p></td>
</tr>
<tr>
<td><p><code>ingress.hosts.paths.</code><br />
<code>pathType</code></p></td>
<td><p>The path type, by default <code>Prefix</code>.</p></td>
</tr>
<tr>
<td><p><code>ingress.tls[0].secretName</code></p></td>
<td><p>Adds TLS secret name to allow secure traffic, by default <code>null</code> (no value).</p></td>
</tr>
</tbody>
</table>

Redis properties:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Property</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>rediscluster.enabled</code></p></td>
<td><p>Enables the redis cluster for caching, by default <code>true</code>.</p></td>
</tr>
<tr>
<td><p><code>rediscluster.externalRedis</code><br />
<code>Clusteraddress</code></p></td>
<td><p>If you want to use an existing redis cluster, specify its address here, for example <code>redis://redis-cluster:6379</code>. By default, this is empty <code></code> and the <code>redis-cluster.*</code> properties are used to create the redis pods.</p></td>
</tr>
<tr>
<td><p><code>rediscluster.externalRedis</code><br />
<code>Clusterpassword</code></p></td>
<td><p>If you specify an external redis cluster, specify its password here, otherwise empty <code></code> by default.</p></td>
</tr>
<tr>
<td><p><code>redis-cluster.nameOverride</code></p></td>
<td><p>If no external redis cluster is given, Kubernetes will create a one and give it this name for identification, by default <code>query-engine-redis-cluster</code>.</p></td>
</tr>
<tr>
<td><p><code>redis-cluster.</code><br />
<code>cluster.nodes</code></p></td>
<td><p>Number of nodes to create in the redis cluster, by default <code>6</code>.</p></td>
</tr>
<tr>
<td><p><code>redis-cluster.</code><br />
<code>persistence.size</code></p></td>
<td><p>Size of each redis node, by default <code>8Gi</code> (gibibytes).</p></td>
</tr>
<tr>
<td><p><code>global.redis.password</code></p></td>
<td><p>Create a password for the redis cluster.</p></td>
</tr>
</tbody>
</table>

Autoscaling properties:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Property</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>autoscaling.enabled</code></p></td>
<td><p>Enables the HorizontalPodAutoscaler (HPA). The default is <code>true</code>. The metrics should also be enabled so they are available for the autoscaler to work.</p></td>
</tr>
<tr>
<td><p><code>autoscaling.*</code></p></td>
<td><p>The following properties define the behavior of the autoscaler:</p>
<ul>
<li><code>minReplicas</code>: Minimum number of active workers, by default <code>2</code>.</li>
<li><code>maxReplicas</code>: Maximum number or active workers, by default <code>10</code>.</li>
<li><code>targetCPUUtilizationPercentage</code>: Minimum average CPU load of active workers to create a worker (scale up), by default <code>50%</code>.</li>
<li><code>targetMemoryUtilizationPercentage</code>: Minimum average memory usage on active workers to create a worker (scale up), by default not specified <code></code>.</li>
<li><code>scaleDown.stabilizationWindowSeconds</code>: Time to wait with no activity to remove a worker (scale down), by default <code>300</code> (5 minutes).</li>
</ul></td>
</tr>
<tr>
<td><p><code>customMetricScaling.</code><br />
<code>enabled</code></p></td>
<td><p>If you want to implement the custom metrics-based autoscaling, set this to true. The default is false. This enables the Prometheus-based autoscaling that uses the number of queued Ad Hoc tasks for scaling up. It can also be further customized for other metrics, although that is beyond the scope of this document.</p></td>
</tr>
<tr>
<td><p><code>scalable-query-engine-scaling.*</code></p></td>
<td><p>Properties for the Prometheus-based autoscaler. The name and function of each property is the same as for <code>autoscaling.*</code>, except for the following:</p>
<ul>
<li><code>averageQueuedExecutions</code>: Minimum average queue length on active workers to create a worker, by default 10.</li>
</ul></td>
</tr>
</tbody>
</table>

Ingress controller properties that configure the load balancing. It is also possible to configure a different load balancer such as AWS by modifying `templates/internal-ingress.yaml`, but the details are beyond the scope of this document:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Property</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>ingressClass</code></p></td>
<td><p>By default <code>intranet</code>.</p></td>
</tr>
<tr>
<td><p><code>kubernetes-ingress.</code><br />
<code>nameOverride</code></p></td>
<td><p>By default <code>query-engine-ingress</code>.</p></td>
</tr>
<tr>
<td><p><code>kubernetes-ingress.</code><br />
<code>controller.replicaCount</code></p></td>
<td><p>Number of ingress controller replicas, by default <code>1</code>.</p></td>
</tr>
<tr>
<td><p><code>kubernetes-ingress.</code><br />
<code>controller.service.type</code></p></td>
<td><p>By default <code>LoadBalancer</code>.</p></td>
</tr>
<tr>
<td><p><code>kubernetes-ingress.</code><br />
<code>controller.ingressClass</code></p></td>
<td><p>By default <code>intranet</code>.</p></td>
</tr>
<tr>
<td><p><code>kubernetes-ingress.</code><br />
<code>controller.config.</code><br />
<code>timeout-connect</code></p></td>
<td><p>By default <code>30s</code> (seconds).</p></td>
</tr>
<tr>
<td><p><code>kubernetes-ingress.</code><br />
<code>controller.config.</code><br />
<code>timeout-check</code></p></td>
<td><p>By default <code>60s</code> (seconds).</p></td>
</tr>
<tr>
<td><p><code>kubernetes-ingress.</code><br />
<code>controller.config.</code><br />
<code>timeout-client</code></p></td>
<td><p>By default <code>240s</code> (seconds).</p></td>
</tr>
<tr>
<td><p><code>kubernetes-ingress.</code><br />
<code>controller.config.</code><br />
<code>timeout-server</code></p></td>
<td><p>By default <code>240s</code> (seconds).</p></td>
</tr>
<tr>
<td><p><code>kubernetes-ingress.</code><br />
<code>defaultBackend.replicaCount</code></p></td>
<td><p>By default <code>1</code>.</p></td>
</tr>
<tr>
<td><p><code>server.tomcat.</code><br />
<code>connectionTimeout</code></p></td>
<td><p>Timeout request in milliseconds for a Tomcat request, by default <code>300000</code> (5 minutes).</p></td>
</tr>
</tbody>
</table>

Server properties for the workers to access the JasperReports Server instance through the REST API:

| Property | Description |
|----|----|
| `jrs.server.scheme` | The protocol to access JasperReports Server, used to create the server URL, by default `http`. |
| `jrs.server.host` | String to create the hostname of your JasperReports Server instance to the workers within the cluster (behind the ingress load balancer). |
| `jrs.server.port` | Port number of your JasperReports Server instance, by default `80`. |
| `jrs.server.path` | Path in the URL to access the server through the REST API, by default `jasperserver-pro/rest_v2`. |
| `jrs.server.username` | Username to access the server's REST API. By default this is `jasperadmin`, but you might need to change it if you have multiple organizations. |
| `jrs.proxy.enabled` | Enables the proxy for the scalable query engine, by default `true`. |
| `jrs.proxy.scheme` | Protocol for access through the proxy, by default `http`. |
| `jrs.proxy.host` | String to create the hostname of the proxy to the workers within the cluster (behind the ingress load balancer). |
| `jrs.proxy.port` | Port number of the proxy, by default `80`. |
| `jrs.proxy.path` | Path in the URL of the proxy, by default `rest_v2`. |
| `jrs.proxy.username` | Username to reply to the proxy. By default this is `jasperadmin`, but you might need to change it if you have multiple organizations. |
| `jrs.proxy.timedOut` | Timeout in millisecons when replying to the proxy, by default `30000`. |

JDBC driver properties for copying them to the workers:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Property</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>drivers.enabled</code></p></td>
<td><p>Whether Kubernetes will copy the JDBC driver JARs to the workers, by default <code>true</code>.</p></td>
</tr>
<tr>
<td><p><code>drivers.image.tag</code></p></td>
<td><p>Tag of the drivers image to copy from, by default <code>8.0.0</code>.</p></td>
</tr>
<tr>
<td><p><code>drivers.image.name</code></p></td>
<td><p>Name of drivers image, by default <code>null</code> (empty value).</p></td>
</tr>
<tr>
<td><p><code>drivers.image.</code><br />
<code>pullPolicy</code></p></td>
<td><p>Pull policy for the drivers image, by default <code>IfNotPresent</code>.</p></td>
</tr>
<tr>
<td><p><code>drivers.jdbcDriversPath</code></p></td>
<td><p>Destination path where JDBC drivers are copied in the workers, by default /<code>usr/lib/drivers</code>.</p></td>
</tr>
</tbody>
</table>

Logging-related properties; for more information, see [Logging and Debugging](logging.md):

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Property</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>metrics.enabled</code></p></td>
<td><p>Enables the metrics for Prometheus-based autoscaling, by default <code>false</code>.</p></td>
</tr>
<tr>
<td><p><code>kube-prometheus-stack.</code><br />
<code>prometheus-node-exporter.</code><br />
<code>hostRootFsMount</code></p></td>
<td><p>Whether to mount Prometheus in the host file system, the default is <code>false</code>.</p></td>
</tr>
<tr>
<td><p><code>kube-prometheus-stack.</code><br />
<code>grafana.service.type</code></p></td>
<td><p>By default <code>NodePort</code>.</p></td>
</tr>
<tr>
<td><p><code>logging.enabled</code></p></td>
<td><p>Enables the Elasticsearch, Fluentd and Kibana (EFK) logging, by default <code>false</code>.</p></td>
</tr>
<tr>
<td><p><code>logging.level</code></p></td>
<td><p>Logging level in the workers, by default <code>INFO</code>.</p></td>
</tr>
<tr>
<td><p><code>logging.pretty</code></p></td>
<td><p>Logging format in the workers, by default <code>false</code>.</p></td>
</tr>
<tr>
<td><p><code>fluentd.imageName</code></p></td>
<td><p>By default <code>fluent/fluentd-kubernetes-daemonset</code>.</p></td>
</tr>
<tr>
<td><p><code>fluentd.imageTag</code></p></td>
<td><p>By default <code>v1.12.3-debian-elasticsearch7-1.0</code>.</p></td>
</tr>
<tr>
<td><p><code>fluentd.esClusterName</code></p></td>
<td><p>Elasticsearch cluster name, by default <code>elasticsearch</code>.</p></td>
</tr>
<tr>
<td><p><code>fluentd.esPort</code></p></td>
<td><p>Elasticsearch port number, by default <code>9200</code>.</p></td>
</tr>
<tr>
<td><p><code>elasticsearch.replicas</code></p></td>
<td><p>Number of pods for Elasticsearch, by default <code>1</code>.</p></td>
</tr>
<tr>
<td><p><code>elasticsearch.</code><br />
<code>volumeClaimTemplate.</code><br />
<code>resources.requests.storage</code></p></td>
<td><p>By default <code>10Gi</code> (gibibytes).</p></td>
</tr>
<tr>
<td><p><code>kibana.service.type</code></p></td>
<td><p>By default <code>NodePort</code>.</p></td>
</tr>
</tbody>
</table>

## Specifying a JNDI Data Source

To use a JNDI data source, you must specify its JDBC parameters in the file config/jndi.properties. Remove the sample databases, and add one or more JDNI data sources as follows:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Property</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>jndi.dataSources[</code><span><code>i</code></span><code>].*</code></p></td>
<td><p>The array of data source properties where <span><code>i</code></span> is zero-based.</p></td>
</tr>
<tr>
<td><p><code> .name</code></p></td>
<td><p>The name of the JDBC database to use with JNDI, in the format <code>jdbc/&lt;jdbc-name&gt;</code>. .auth=The type of authentication, by default <code>Container</code>.</p></td>
</tr>
<tr>
<td><p><code> .factory</code></p></td>
<td><p>The Java factory class to use by default <code>com.jaspersoft.jasperserver.tomcat.jndi.JSCommonsBasicDataSourceFactory</code>.</p></td>
</tr>
<tr>
<td><p><code> .driverClassName</code></p></td>
<td><p>JDBC driver class for this database. The JAR file for this driver must be copied into the Docker image.</p></td>
</tr>
<tr>
<td><p><code> .url</code></p></td>
<td><p>JDBC URL to access the database, for example <code>jdbc:postgresql://&lt;hostname&gt;:&lt;port&gt;/&lt;dababase&gt;</code>.</p></td>
</tr>
<tr>
<td><p><code> .username</code></p></td>
<td><p>Database username.</p></td>
</tr>
<tr>
<td><p><code> .password</code></p></td>
<td><p>Database user password, or configure the password in a secret and provide its name here.</p></td>
</tr>
<tr>
<td><p><code> .accessToUnderlying</code><br />
<code>ConnectionAllowed</code></p></td>
<td><p>By default <code>true</code>.</p></td>
</tr>
<tr>
<td><p><code> .validationQuery</code></p></td>
<td><p>Simple query to test the connection, usually <code>SELECT 1</code>.</p></td>
</tr>
<tr>
<td><p><code> .testOnBorrow</code></p></td>
<td><p>By default <code>true</code>.</p></td>
</tr>
<tr>
<td><p><code> .maxActive</code></p></td>
<td><p>The maximum number of connections to allocate in the connection pool, for example 100.</p></td>
</tr>
<tr>
<td><p><code> .maxIdle</code></p></td>
<td><p>The maximum number of connections to maintain in the pool when they are idle, for example 30.</p></td>
</tr>
<tr>
<td><p><code> .maxWait</code></p></td>
<td><p>When all connections are in use, the duration in milliseconds that the pool let a request wait before returning a timeout. The default is <code>10000</code> (10 seconds).</p></td>
</tr>
</tbody>
</table>

If you want to update the JNDI properties after having deployed the workers with Kubernetes, you will need to restart or redeploy the workers.

## Deploying to Kubernetes

Use the following procedure to deploy the cluster of workers using Kubernetes:

1.  Download the Docker images and Helm charts from github.com as described in [Downloading the Software](downloading.md).

2.  Configure and build the Docker images as described in [Docker Configuration](docker.md).

3.  Add the helm dependencies with the following commands:

    ``` text
    helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
    helm repo add haproxytech https://haproxytech.github.io/helm-charts
    helm repo add bitnami https://charts.bitnami.com/bitnami
    helm repo add elastic https://helm.elastic.co
    ```

4.  Update the helm dependencies when needed with the following commands:

    ``` bash
    cd <js-install>/jaspersoft-containers/K8s
    helm dependencies update scalableQueryEngine/helm
    ```

5.  If you have not done so already, configure the Helm chart in values.yaml for the deployment of Redis, Ingress, and the workers as described in [Configuring the Helm Chart](#configuring-the-helm-chart). You can also set individual values by adding `--set <parameter_name>=<paramter_value>` to the Helm commands below.

6.  If you have not done so already, configure your JNDI data sources as described in [Specifying a JNDI Data Source](#specifying-a-jndi-data-source).

7.  Now you can deploy the workers on Kubernetes with the following command:

    ``` text
    helm install engine scalableQueryEngine/helm
    ```

8.  Get the ingress external IP address or nodeport and check the workers' status at:

    `<ingress-IP>/query-engine/actuator/health`

9.  Configure your JasperReports Server instance as described in [Configuring JasperReports Server](configuring_jrs.md), then restart your server.

Once your server and query engine are running, you can test a dashboard that contains an Ad Hoc view. After it runs, you can check the logs as described in [Logging and Debugging](logging.md).
