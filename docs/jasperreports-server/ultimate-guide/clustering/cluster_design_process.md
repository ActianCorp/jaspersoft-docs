---
title: Cluster Design Process
description: The rest of this chapter looks at how you would design a JasperReports Server cluster to fit your needs. It assumes that your cluster will follow the traditional pattern with a load balancer and some...
---

# Cluster Design Process

The rest of this chapter looks at how you would design a JasperReports Server cluster to fit your needs. It assumes that your cluster will follow the traditional pattern with a load balancer and some number of identical nodes, as shown in the sample architecture. Other architectures, such as dedicated OLAP nodes or a geographically distributed cluster, are possible but beyond the scope of this chapter.

As with any software project, careful design and planning will help you meet your goals. A simplified process for designing a cluster might include the following steps:

1.  Gather cluster requirements in the following areas:

- Performance – Usually defined as average response time for a given load.
- High availability – Usually measured as percentage up-time.
- Scalability – The ease of adding nodes to improve performance and availability over time.

1.  Estimate the size of your cluster to meet your requirements within your limitations such as time and budget. Sizing determines the architecture of your cluster:

- Load-balancing hardware
- Size and number of cluster nodes
- Shared resources, especially databases
- JasperReports Server configuration

1.  Deploy your cluster:

- Hardware purchases and installation
- Network configuration
- Software configuration, including JasperReports Server configuration
- Testing of all components individually and in the cluster architecture
- Rollout to end-users
- Administration, maintenance, and scaling procedures

Deployment and implementation are beyond the scope of this chapter. The following sections give more details about gathering cluster requirements and sizing.
