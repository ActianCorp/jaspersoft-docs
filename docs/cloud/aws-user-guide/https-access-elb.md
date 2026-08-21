---
title: Configuring HTTPS Access for AWS ELB and JasperReports Server
description: Follow these instructions if you want to use Elastic Load Balancer (ELB) as an HTTPS termination point with JasperReports Server behind it.
---

# Configuring HTTPS Access for AWS ELB and JasperReports Server

Follow these instructions if you want to use Elastic Load Balancer (ELB) as an HTTPS termination point with JasperReports Server behind it.

1.  Create your ELB in AWS with a JasperReports Server instance behind it.
2.  Configure your load balancer using the instructions found here:

`https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html`

1.  Edit the following file in your JasperReports Server instance:

`/usr/share/tomcat/conf/server.xml`

1.  Locate the connector tag: `<connector port="80"...`
2.  In the connector tag, add the following parameters:

`scheme="https" proxyPort="443" proxyName="Elastic load balancer public DNS name"`

1.  Save the file and restart Tomcat. See [Stopping and Restarting Tomcat](stopping-and-restarting-tomcat.md).
