---
title: Session Management and Failover
description: Failover is the ability of the cluster to minimize the impact of a node failure and continue serving clients with the remaining nodes. A failure is assumed to be any unplanned incident that causes a...
---

# Session Management and Failover

Failover is the ability of the cluster to minimize the impact of a node failure and continue serving clients with the remaining nodes. A failure is assumed to be any unplanned incident that causes a node, either its software or hardware, to become and remain unavailable. To implement failover, you need to understand how JasperReports Server manages client sessions. This allows you to configure the cluster for optimal performance and set user expectations.

A client session is an in-memory object that represents the user to the server at run-time. After a user logs in or a web services client sends a request with credentials, the session contains the user profile such as organization and role membership for use in enforcing permissions. For browser users, the session also stores information about the state of the web interface, for example the last folder viewed in the repository, the last search term, or the data entered in a wizard. In commercial editions with the Ad Hoc Editor and Dashboard Designer, the user session also stores the on-screen state of the report or dashboard the user creates interactively through the browser.

There are several types of session management in cluster design, each of which determines a different failover scenario:

- Fully replicated sessions: The state of every client session is continuously communicated among all nodes and stored on every node or in a shared location. This is usually managed by the app server. Upon failure, the load balancer automatically redirects client connections to a remaining node. Because every node has access to a copy of the client session, the user can continue work from the previous state, often unaware of the failure or the change. Some load balancers can transfer sessions when a node is overloaded but hasn't failed.

!!! warning

    JasperReports Server does not support fully replicated sessions. See explanation below.

- Sticky or pinned sessions: Client sessions are created and managed privately by each server instance and cannot be transferred to another node. When a failure shuts down an instance, all of its client sessions are lost. When users reconnect, the load balancer directs them to another node where they login and begin a new session on the new node.

- Partially replicated sessions: In this hybrid solution, only the vital parts of the session are replicated to allow some failover, but in the absence of node failure, sessions must remain pinned to a node.

Unlike small e-commerce sessions, JasperReports Server has larger and more complex sessions that would degrade performance if fully replicated. In particular, the JasperPrint object for an executed report is measured in megabytes and stored in the user session. To store and replicate the JasperPrint objects for all users across all nodes would impact performance significantly. Therefore, JasperReports Server uses partial replication so that user login information is replicated, but not large state objects such as JasperPrint objects.

By using partially replicated sessions, JasperReports Server balances the performance of the cluster with the risks and consequences of a failure. If a failure occurs when the user is browsing the repository, the load balancer will connect the user to a new node and work can continue because the login information and repository state in the session were replicated. If a failure occurs when a user is creating or viewing a report, the load balancer will connect the user to a new node, but the report cannot be replicated. In this case users may lose unsaved reports, but they can resume work right away. The chance of a user experiencing a failure is much lower and the consequences are less severe than when working on a non-clustered server.

Even though the risk of failure is low, cluster designers should understand the impact on users. The following sections explain the exact impact of failures with partial session replication in JasperReports Server.
