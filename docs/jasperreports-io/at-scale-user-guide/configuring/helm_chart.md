---
title: Configuring the Helm Chart
description: "Before deploying the Docker images to Kubernetes, you must configure the cluster through the Helm chart in the values.yaml file. There is a section in the file for each module, with settings that are..."
---

# Configuring the Helm Chart

Before deploying the Docker images to Kubernetes, you must configure the cluster through the Helm chart in the values.yaml file. There is a section in the file for each module, with settings that are specific to that module's needs. The following table describes the most common properties in the Helm chart.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>Property</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><code>replicas</code></td>
<td>Must be set to 1 when using the Kubernetes auto-scalability feature, because that creates its own replica sets for deployments and your default replica set will not be used anyway. For more information, see <a href="scalability.md">“Configuring Scalability” on page 1</a>.</td>
</tr>
<tr>
<td><code>dockerImage</code></td>
<td>URI and path of the image in the Docker image repository. In these examples, it is an AWS Docker image registry (AWS ECR or Amazon Elastic Container Registry).</td>
</tr>
<tr>
<td><code>dockerTag</code></td>
<td>The tag for the image in the Docker image repository.</td>
</tr>
<tr>
<td><code>memoryRequest</code></td>
<td><p>Minimum amount of memory that the pod needs to run properly. This much memory should be reserved for the pod, even if it may not use it all at first.</p>
<p>The Mi unit is Mebibytes, which for computer memory is synonymous with megabytes (1 MiB = 2^20 bytes = 1048576 bytes). The Gi unit is also supported for Gibibytes, equivalent to gigabytes.</p></td>
</tr>
<tr>
<td><code>memoryLimit</code></td>
<td>Maximum amount of memory that can be allocated to the pod. The pod can not use more than this amount. See the explanation of Mi units above.</td>
</tr>
<tr>
<td><code>cpuRequest</code></td>
<td><p>Minimum amount of CPU that the pod needs to run properly. This much CPU should be reserved for the pod, even if it may not use it all at first.</p>
<p>The unit m is milliCPU, or thousandths of a CPU. Therefore, 1000m is equivalent to one whole CPU, and 500m is half a CPU. 1000m is also equivalent to 1 virtual CPU (AWS vCPU) or 1 virtual core (Azure vCore or Google core).</p></td>
</tr>
<tr>
<td><code>cpuLimit</code></td>
<td>Maximum amount of CPU that can be allocated to the pod. The pod will not be able to use more than this amount. See the explanation of units above.</td>
</tr>
<tr>
<td><code>javaOptions</code></td>
<td>JVM options settings for each pod in a specific deployment. The recommendation is to leave some buffer so the JVM will not take everything up to what is set in <code>memoryLimit</code>. In particular, the jrio-Export pods come with preinstalled chromium driver, which is used to export HTML/Fusion charts. Each chart report export task inside one pod starts multiple chromiums inside the pod.</td>
</tr>
<tr>
<td><code>terminationWaitSeconds</code></td>
<td>This timeout allows the pod to finish all its tasks when Kubernetes decides to scale down the cluster and stops the pod. For more information, see the <a href="https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#hook-handler-execution">Kubernetes documentation</a>.</td>
</tr>
<tr>
<td><code>config</code></td>
<td>Configuration properties that are passed to the pod, especially any <code>jasperReportsProperties</code> for the jrio-reporting and jrio-export pods.</td>
</tr>
</tbody>
</table>

The following examples of the Helm chart for each pod assume that the Docker images are deployed on AWS EKS (Amazon Elastic Kubernetes Service).

- The jrio-client module is optional, and usually only included for demonstration purposes.

``` bash
###############################
## jrio-client config ##
###############################
jrioClient:
#  replicas: 1
  dockerImage: 123456789000.dkr.ecr.us-east-1.amazonaws.com/jrio-client
  dockerTag: my-example-1.0
#  containerPort: 8080
#  servicePort: 8080
```

- The jrio-manager pod has memory and CPU settings, as well as options for its JVM (Java Virtual Machine).

``` bash
#########################
## jrio-manager config ##
#########################
jrioManager:
  dockerImage: 123456789000.dkr.ecr.us-east-1.amazonaws.com/jrio-manager
  dockerTag: my-example-1.0
  memoryRequest: 384Mi
  memoryLimit: 1536Mi
  cpuRequest: 200m
  cpuLimit: 1000m
  javaOptions: "-Xms128m -Xmx1500m"
```

- In addition to resource limits and JVM options, the jrio-reporting pod has a timeout setting and a thread setting. You can also specify the `jasperReportsProperties` property and provide a list of JasperReports Library property names and values to be used when generating reports.

``` bash
###########################
## jrio-reporting config ##
###########################
jrioReporting:
  replicas: 1
  dockerImage: 123456789000.dkr.ecr.us-east-1.amazonaws.com/jrio-reporting
  dockerTag: my-example-1.0
  memoryRequest: 512Mi
  memoryLimit: 2048Mi
  cpuRequest: 500m
  cpuLimit: 1000m
  javaOptions: "-Xms128m -Xmx1536m"
  terminationWaitSeconds: 600
  config:
    reportExecutionThreads: 4
    jasperReportsProperties: |
      net.sf.jasperreports.chrome.argument.no-sandbox=true
      #net.sf.jasperreports.second.property.example=abc
```

- In addition to resource limits and JVM options, the jrio-export pod also has a timeout setting and a thread setting. You can also specify the `jasperReportsProperties` property and provide a list of JasperReports Library property names and values to be used when exporting reports.

``` bash
###########################
## jrio-export config ##
###########################
jrioExport:
  replicas: 1
  dockerImage: 123456789000.dkr.ecr.us-east-1.amazonaws.com/jrio-export
  dockerTag: my-example-1.0
  memoryRequest: 512Mi
  memoryLimit: 2048Mi
  cpuRequest: 500m
  cpuLimit: 1000m
  javaOptions: "-Xms128m -Xmx1536m"
  terminationWaitSeconds: 900
  config:
    exportExecutionThreads: 4
      jasperReportsProperties: |
      net.sf.jasperreports.chrome.argument.no-sandbox=true
      #net.sf.jasperreports.second.property.example=abc
```

- The jrio-rest pod has properties for resource limits, JVM options and a timeout. If you are not using the standard 8080 port, specify it here as well.

``` bash
######################
## jrio-rest config ##
######################
jrioRest:
  replicas: 1
  dockerImage: 123456789000.dkr.ecr.us-east-1.amazonaws.com/jrio-rest
  dockerTag: my-example-1.0
  memoryRequest: 512Mi
  memoryLimit: 2048Mi
  cpuRequest: 500m
  cpuLimit: 1000m
  javaOptions: "-Xms128m -Xmx1536m"
  terminationWaitSeconds: 900
#  containerPort: 8080
#  servicePort: 8080
```

- The redis pod for the Redis queue only needs the port specified if you are not using the default (6379).

``` bash
##################
## redis config ##
##################
redis:
#  replicas: 1
#  dockerImage: redis
  dockerTag: 1-example
#  containerPort: 6379
#  servicePort: 6379
```

- This setting identifies the URL of the JasperReports Server instance hosting the repository that you want to use for reports and data adapters. This value overrides any repository URL defined in the docker images.

``` bash
################
## JRS config ##
################
repository:
  jasperReportsServer:
    url: "http://example.com:8080/jasperserver-pro"
```

If you deploy JasperReports Server in the cloud, you must open it first so its URL is available to you now. If you have a private setup for AWS EKS (Elastic Kubernetes Service), then the server must be placed into the same virtual private cloud (VPC) as AWS EKS. If you have a public setup, it is not required but it is recommended to do so as well.

Jaspersoft recommended using a static IP address for the JasperReports Server EC2 instance, so you will not have to rebuild JRIO images and update the repository URL in this file. For a server in a clustered setup, you should use the load balancer hostname.

In the following example, the server is running on AWS (Amazon Web Services). You do not need to specify the port if it uses the default port 80.

``` yaml
    url: "http://jrs-instance-lb-002.us-east-1.elb.amazonaws.com/jasperserver-pro"
```

## Minikube on Docker VM

If you deploy on Minikube using the Docker VM, you must specify the following JasperReports Library property in the jrioReporting and jrioExport sections.

``` yaml
jasperReportsProperties:
    net.sf.jasperreports.chrome.argument.no-sandbox=true
```

This property is needed because of a known issue with chrome driver on the Docker VM. This property is not needed for Minikube on a virtual box or other virtual machines, or for actual Kubernetes clusters, for example when deployed on AWS EKS.
