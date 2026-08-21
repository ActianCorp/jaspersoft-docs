---
title: Deploying JasperReports Server
description: This section describes how to connect a JasperReports Server instance with Jaspersoft IO At-Scale so that the server uses the JRIO At-Scale cluster as a scalable reporting engine. Because JRIO...
---

# Deploying JasperReports Server

This section describes how to connect a JasperReports Server instance with Jaspersoft IO At-Scale so that the server uses the JRIO At-Scale cluster as a scalable reporting engine. Because JRIO creates its own database connections using JDBC, this works only for reports that have a JDBC data source, not JNDI, or other data sources.

1.  If you have a private setup for AWS EKS, then your JasperReports Server has to be placed into the same VPC as AWS EKS. Jaspersoft also recommends doing so in public cases. Assuming your VPC was created by CloudFormation scripts as described in [Creating a Virtual Private Cloud](setting_up_aws_eks.md), create an EC2 instance in AWS EKS VPC for your JasperReports Server. Be sure to use a static IP address assigned to the JasperReports Server instance because that address must be specified in the module configuration before creating Docker images. For JasperReports Server in a clustered setup, configure a static IP address for the load balancer.
2.  Make sure that your JRIO At-Scale cluster does not include the jrio-client module and is configured to use the JasperReports Server instance, as described in [Connecting to a JasperReports Server Repository](../dockerimages/configuration.md).
3.  After the server has been deployed, edit the following file:

|          |                                          |
|----------|------------------------------------------|
| File     | /tomcat9/webapps/js.config.properties    |
| Property | jrio.url                                 |
| Example  | jrio.url=http://192.168.189.2:30030/jrio |

1.  If your JRIO At-Scale cluster handles high throughput, the server's event logging of every repository access may slow down your pods and become a bottleneck. In this case, disable event logging as follows:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td>File</td>
<td>jasperserver-pro/WEB-INF/applicationContext-events-logging.xml</td>
</tr>
<tr>
<td>Bean ID</td>
<td>loggingContextProvider</td>
</tr>
<tr>
<td>Property</td>
<td>&lt;entry key="com.jaspersoft.jasperserver.api.logging.access.domain.AccessEvent"<br />
value="false"/&gt;</td>
</tr>
</tbody>
</table>

1.  For JasperReports Server in a clustered setup, repeat this procedure for each instance.
