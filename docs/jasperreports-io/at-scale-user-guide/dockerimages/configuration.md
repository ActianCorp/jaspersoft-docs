---
title: Configuring the Modules
description: "Before you can build Docker images to deploy the modules, you must configure them to add the license file and specify a repository to store your reports. Optionally, you can also enable logging and..."
---

# Configuring the Modules

Before you can build Docker images to deploy the modules, you must configure them to add the license file and specify a repository to store your reports. Optionally, you can also enable logging and set concurrent thread limits.

## Installing the License File

You must purchase a license from Jaspersoft to run JasperReports IO At-Scale. Once you recieve the license file, save a copy in the following folder:

jrio-manager-docker/jrio/classes

For more information about the license file, contact your Jaspersoft support representative.

## Using the Standalone Repository

The jrio-client module only contains a sample application with links to the reports. These reports are stored in the sample repositories. Each module (jrio-client, jrio-reporting, jrio-rest) can access the reports using their local file system.

However, the sample application is not a high-performance repository and is deployed statically in the jrio-client pod. Jaspersoft recommends using a JasperReports Server repository, as described in the next section.

To make your reports appear in the standalone repository of the sample application, add the files in the following folders:

jrio-reporting-docker/jrio-repository/samples

jrio-export-docker/jrio-repository/samples

jrio-rest-docker/jrio-repository/samples

The standalone repository is identical to the file-based repository in JasperReports IO Professional. For more information about its file structure, see the *JasperReports IO Repository* section of the *Managing JasperReports IO* chapter in the JasperReports IO Pro User Guide.

## Connecting to a JasperReports Server Repository

In a production environment, Jaspersoft recommends using JasperReports IO At-Scale with a JasperReports Server instance for maximum throughput and flexibility. In this case, users create and access reports in the JasperReports Server repository, and JRIO At-Scale becomes the scalable, high-performance reporting engine for the server.

When connecting to JasperReports Server, you must specify a URL (IP address or hostname) that is accessible from inside the JasperReports IO At-Scale cluster. If you plan to use JasperReports Server on AWS, you can specify the static IP or loadbalancer with hostname that is attached to that server instance. Be aware that you should create your Virtual Private Cloud (VPC) ahead of time, as well as your JasperReports Server instance so that the IP address is already available for the next steps. For more information, see [Deploying JasperReports Server](../deploying/deploying_the_cluster.md).

!!! note

    The repository URL is usually set in the Helm chart (values.yaml), as described in [Configuring the Helm Chart](../configuring/helm_chart.md). The Helm chart lets you update the repository URL dynamically because its value takes precedence. However, setting this value in the module configuration as described below provides a hardcoded default value.

Optional

1.  Specify the server URL in the following three modules configuration files:

    <table>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <tbody>
    <tr>
    <td>Files</td>
    <td>jrio-reporting-docker/jrio/applicationContext-jrs.xml<br />
    jrio-export-docker/jrio/applicationContext-jrs.xml<br />
    jrio-rest-docker/jrio/WEB-INF/applicationContext-jrs.xml</td>
    </tr>
    <tr>
    <td>Bean</td>
    <td>id="serverConfiguration"<br />
    class="com.jaspersoft.jrio.common.repository.jrs.ServerConfiguration"</td>
    </tr>
    <tr>
    <td>Property</td>
    <td>serverURL</td>
    </tr>
    <tr>
    <td>Example</td>
    <td>&lt;property name="serverURL" value="http://example.com:8080/jasperserver-pro"/&gt;</td>
    </tr>
    </tbody>
    </table>

2.  By default, JasperReports IO At-Scale includes the standalone repository in the jrio-export, jrio-rest, and jrio-reporting modules. The sample repository in each module is accessible. For more information, see [Using a Local Repository](local_repository.md). Deploying the JasperReports IO At-Scale with a sample repository in each module will not impact the performance. If you want to disable these file repositories, open each of the following files and comment out all of the listed beans:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td>Files</td>
<td>jrio-reporting-docker/jrio/applicationContext-repository.xml<br />
jrio-export-docker/jrio/applicationContext-repository.xml<br />
jrio-rest-docker/jrio/WEB-INF/applicationContext-repository.xml</td>
</tr>
<tr>
<td>Beans</td>
<td><p>com.jaspersoft.jrio.common.repository.FileSystemRepository<br />
com.jaspersoft.jrio.common.repository.FileSystemPersistenceServiceFactory</p></td>
</tr>
</tbody>
</table>

## Setting JasperReports Properties

JasperReports properties are the configuration settings for the JasperReports Library that is the reporting engine for JasperReports IO At-Scale. They affect the reporting and exporting modules to determine many aspects of report generation and output.

!!! note

    JasperReports properties are usually set in the Helm chart (values.yaml), as described in [Configuring the Helm Chart](../configuring/helm_chart.md). The Helm chart lets you update the properties dynamically because its values takes precedence. However, setting this value in the module configuration as described below provides a hardcoded default value.

Optional

To set JasperReports properties, add them to the following files:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td>jrio-reporting module</td>
<td>jrio-reporting-docker/jrio/classes/jasperreports.properties<br />
jrio-reporting-docker/jrio/classes/jasperreports_extension.properties</td>
</tr>
<tr>
<td>jrio-export module</td>
<td>jrio-export-docker/jrio/classes/jasperreports.properties<br />
jrio-export-docker/jrio/classes/jasperreports_extension.properties</td>
</tr>
</tbody>
</table>

## Configuring Logging

By default, logging is enabled in the jrio-manager and jrio-reporting modules. Jaspersoft does not recommend changing the logging levels because the logs are used for troubleshooting. You can monitor these logs and use the Kubernetes Logging API to track events inside the cluster.

The logging levels are defined as follows

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td>Module</td>
<td>jrio-manager</td>
</tr>
<tr>
<td>File</td>
<td>jrio-manager-docker/jrio/classes/log4j2.xml</td>
</tr>
<tr>
<td>Loggers</td>
<td>&lt;Logger name="com.jaspersoft.jrio.manager.redis.RedisLicensePublisher" level="INFO"/&gt;<br />
&lt;Logger name="com.jaspersoft.jrio.manager.reporting.ReportingQueueManager"<br />
level="DEBUG"/&gt;</td>
</tr>
</tbody>
</table>

|  |  |
|----|----|
| Module | jrio-reporting |
| File | jrio-reporting-docker/jrio/classes/log4j2.xml |
| Logger | \<Logger name="com.jaspersoft.jrio.reporting.execution.ReportExecutionPoll" level="DEBUG"/\> |

|        |                                                  |
|--------|--------------------------------------------------|
| Module | jrio-rest                                        |
| File   | jrio-rest-docker\jrio\WEB-INF\classes\log4j2.xml |
| Logger | None by default                                  |

## Setting Concurrent Threads

The jrio-reporting and jrio-export modules are the workhorses of a JasperReports IO At-Scale cluster, usually deployed as multiple pods (module instances) to one or more nodes (physical or virtual machines). Each pod can also specify how many threads to run concurrently. This value depends on your performance needs, and it requires fine tuning based on service level requirements, user expectations, peak load, and CPUs available on each node.

!!! note

    The concurrent threads are usually set in the Helm chart (values.yaml), as described in [Configuring the Helm Chart](../configuring/helm_chart.md). The Helm chart lets you update the properties dynamically because its values takes precedence. However, setting threads in the module configuration as described below provides a hardcoded default value.

To specify the default number of concurrent threads in each reporting pod

|          |                                                             |
|----------|-------------------------------------------------------------|
| File     | jrio-reporting-docker/jrio/applicationContext-reporting.xml |
| Bean     | reportExecutionPoll                                         |
| Property | reportExecutionThreads                                      |

To specify the default number of concurrent threads in each export module

|          |                                                          |
|----------|----------------------------------------------------------|
| File     | jrio-export-docker/jrio/applicationContext-export.xml    |
| Bean     | com.jaspersoft.jrio.export.executor.ReportExportExecutor |
| Property | exportThreads                                            |
