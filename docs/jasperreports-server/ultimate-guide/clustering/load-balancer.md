---
title: Load Balancer
description: "A load balancer is a hardware device or software application that uses any number of techniques to spread traffic between the nodes of the cluster, usually so that all servers have an equal load. The..."
---

# Load Balancer

A load balancer is a hardware device or software application that uses any number of techniques to spread traffic between the nodes of the cluster, usually so that all servers have an equal load. The load balancer provides a single address that all clients can access, and it behaves like an internet router, maintaining each client’s connection with the chosen server in the cluster.

The load balancer is the gateway to the cluster because it directs client traffic and optimizes the performance of your servers. At a minimum, the load balancer can determine that a server is not operating and direct traffic to the remaining functioning servers. Some load balancers offer capabilities such as analyzing client requests and server load to optimize server response times for clients. The JasperReports Server itself does not communicate with load balancers, but some load balancers may communicate with the application server to determine availability and load.

Because JasperReports Server supports partial session replication but not full replication, the load balancer must be configured so that browser users are always connected to the same server during a continuous session. Sessions should be transferred only if a node becomes disabled. For more information, see [Session Management and Failover](session-management-and-failover.md). Beyond that requirement, JasperReports Server can work with any HTTP load balancer, either hardware or software. The load balancer module in the Apache HTTP server is a common software solution.

If you have high concurrent user loads and rigorous availability requirements, you may need a load balancer with more advanced features for balancing client traffic. Also, the load balancer capabilities and configuration sometimes limit the maximum number of servers in your cluster, an important consideration for scalability. Your cluster requirements ultimately determine your choice of load balancer.
