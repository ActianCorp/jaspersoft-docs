---
title: JasperReports Server Instances
description: "The JasperReports Server instances deployed in a cluster are normal servers with only minor configuration needed for the cluster. As with all server instances, they run in a Java servlet container..."
---

# JasperReports Server Instances

The JasperReports Server instances deployed in a cluster are normal servers with only minor configuration needed for the cluster. As with all server instances, they run in a Java servlet container that's usually implemented as an application server. While the load balancer may interact with the application servers, and the application servers and internal caches may communicate between nodes to maintain user sessions, JasperReports Server itself does not have any special behavior when deployed in the cluster environment.

In this document, a node refers to the computer hosting a JVM, an application server, and a single instance of JasperReports Server as the only application. Each node can be a physical computer or a cloud-based virtual computer, as long as the operating system is supported by JasperReports Server. For performance and stability reasons, we recommend that the only other software installed is the required Java Virtual Machine (JVM) and the application server. This design allows you to allocate as much memory as possible to the JVM and to JasperReports Server.

We also recommend that you use a lightweight application server such as Apache Tomcat or Glassfish. For example, Tomcat is a well-tested application server with JasperReports Server. A typical configuration for handling most reporting uses 64-bit Java with 2 gigabytes of memory allocated to the Java heap. See the JasperReports Server Installation Guide for guidelines and instructions for installing JasperReports Server in your choice of application server and to configure your JVM.

Alternatively, you can deploy virtual server instances pre-configured for high-availability in Amazon's Elastic Compute Cloud (EC2). By deploying virtual machines, you have the flexibility of scaling on-demand and paying only for what you use. If your repository also uses Amazon's Relational Database Service (RDS), you can create an entirely virtual cluster within Amazon's Web Service offerings. For CloudFormation Templates that can launch a variety of AMIs (Amazon Machine Instances) in your selected region, see [Launching Jaspersoft for AWS](https://aws.amazon.com/marketplace/pp/prodview-2rym5fbrzlshy) on the Jaspersoft Community website.

The general procedure for deploying nodes in a cluster is as follows:

1.  Install a single instance from the WAR file distribution or in the cloud, and configure it completely. This includes all your security settings, user settings, and customizations or authentication such as single sign-on (SSO).
2.  Provision the physical or virtual machines for the other nodes of the cluster.
3.  Copy the deployed WAR file to each of the other app servers in the cluster. When using JNDI data sources provided by the application server, you must make sure they are pre-configured and identical on every application server. Often, the entire application server with JasperReports Server deployed within it can be copied as well. This is sometimes called “cloning” the server. Upgrades can be handled in the same way.
4.  In order to implement partial session replication, the application servers and internal caches must be configured to communicate with each other within the cluster. After cloning or deploying the server instances, you should configure each node separately, as described in [1.0.1, “Sample Configuration for Failover,” on page 1](app-server-configuration.md).

Except for the session replication and internal caches, every node should have an identical configuration. While it is possible for each instance to be configured differently, it's not recommended. When instances are deployed on differing hardware with different configurations, the load balancer's algorithm may not be effective. Having identical JasperReports Server instances in your cluster greatly simplifies its installation and maintenance.
