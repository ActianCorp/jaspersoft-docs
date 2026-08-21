---
title: Availability Requirements
description: "High availability depends on the cluster's ability to effectively avoid downtime. In general, failover prevents the total system unresponsiveness that happens when a single server fails, but a..."
---

# Availability Requirements

High availability depends on the cluster's ability to effectively avoid downtime. In general, failover prevents the total system unresponsiveness that happens when a single server fails, but a properly designed cluster must also address the failure of other cluster components.

High availability is usually defined as a high percentage of uptime, such as 99.999%, 24/7/365 (always), or business hours during business days. To design for high availability, all system components must be made redundant or recoverable enough so that no single component failure can bring the entire environment to a stop.

Identifying the failure modes of a cluster is good practice for any deployment. For every component in the cluster, analyze what happens to users and overall availability when that component fails. See [Session Management and Failover](session-management-and-failover.md) for an explanation of what happens to users on a server instance that fails. You should also consider the overall performance degradation of the cluster and the impact of failures on other cluster components.

A further aspect of high availability is sizing the cluster so, should one server (hardware or software) become unavailable, the rest can still respond to anticipated demand. If you have strict availability and performance requirements, you may need to plan for additional nodes. As you design your JasperReports Server cluster, you should take all these issues into account to properly assess your availability requirements.

Another aspect of high availability is the ability of certain clusters to keep operating during planned maintenance and upgrades, called rolling upgrades. JasperReports Server does not support rolling upgrades, because different versions can require different schemas in the shared repository. So your availability planning must include the time to stop the entire cluster and perform upgrades as necessary.
