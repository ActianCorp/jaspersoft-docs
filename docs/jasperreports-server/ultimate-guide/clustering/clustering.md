---
title: Designing a Cluster
description: "To provide scalability and high availability of your business intelligence infrastructure, you can deploy a cluster of JasperReports Server instances behind a load balancer. You can implement a..."
---

# Designing a Cluster

To provide scalability and high availability of your business intelligence infrastructure, you can deploy a cluster of JasperReports Server instances behind a load balancer. You can implement a cluster with either the community or commercial edition of JasperReports Server as long as all instances are the same edition, the same version, and all are configured identically.

With a properly designed cluster, you can support many more users and organizations, avoid unintended downtime, and plan for future growth. The load balancer makes sure that user load is spread evenly and, when needed, you can add new instances of JasperReports Server to the cluster.

Clusters can be implemented on your own hardware, but JasperReports Server also provides more support for virtual machines in a cloud. Jaspersoft has partnered with Amazon to offer quick and affordable virtual instances in Amazon's EC2 (Elastic Compute Cloud) that can be used to create a cluster. By using CloudFormation Templates provided by Jaspersoft, you can easily launch pre-configured AMIs (Amazon Machine Instances) in your choice of size and location, and then connect them to your Amazon RDS (Relational Database Services) to create an on-demand cluster. You can create high-availability that is eminently scalable, requires no hardware, and you only pay for what you use.

One important detail of any cluster is how sessions are managed in case of a failure. JasperReports Server supports partial replication of sessions. In case of a node failure, the session is transferred automatically between nodes so that users are not logged out. However, work in the Ad Hoc editor and report viewer will be interrupted, though work saved in the repository can be resumed on the new node.

This chapter introduces a sample architecture for JasperReports Server cluster environments and explains its components. It also discusses design considerations and deployment constraints, such as session management. This document is not intended as a tutorial, nor as a detailed deployment plan, and should be used only as a high level overview.

This chapter contains the following sections:

-   [Sample Cluster Architecture](sample-cluster-architecture.md)

-   [Jaspersoft OLAP in a Cluster](jaspersoft-olap-in-a-cluster.md)

-   [Session Management and Failover](session-management-and-failover.md)

-   [Cluster Design Process](cluster_design_process.md)

-   [Performance Requirements](performance-requirements.md)

-   [Availability Requirements](availability-requirements.md)

-   [Scalability Requirements](scalability-requirements.md)

-   [Sizing a Cluster](sizing-a-cluster.md)
