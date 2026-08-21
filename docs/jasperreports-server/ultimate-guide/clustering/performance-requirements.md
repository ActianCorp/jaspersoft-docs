---
title: Performance Requirements
description: The two sides to performance are performance requirements and load estimates. The goal is to anticipate the number of users and their activities to design a cluster that responds to their needs with...
---

# Performance Requirements

The two sides to performance are performance requirements and load estimates. The goal is to anticipate the number of users and their activities to design a cluster that responds to their needs with minimal delay.

Performance requirements ensure that the cluster is responsive to user requests. Such requirements are usually defined in terms of the system response relative to an amount of traffic in a given period, such as “5 second response for all pages regardless of system load” or “maximum 10 second response time for up to 20 simultaneous users.” There are often different requirements for expected average load versus maximum load.

The requirements should be based on realistic estimates of the number of users and how they'll interact with JasperReports Server. First, you should determine what volume of users will be browser clients (real people) and API clients (applications making API calls) and the ratio between them. See [Session Management and Failover](session-management-and-failover.md) for information about these two types of clients and how their sessions differ.

Then estimate what kinds of operations your users perform, for example:

- How many users will just run reports and save the output?

- How many users will create reports or explore data interactively?

- How large are your typical reports, in terms of data retrieved and processing required, and how often do they run?

- What times of day will have the highest user load?

- Will users or API clients access the repository extensively?

In addition to user sessions, the server instances must also process scheduled jobs, so you should estimate their volume and nature. For example, what volume of jobs are critical to run at exact times, what volume of jobs must run during business hours when user load will be high? Can you educate users to run jobs outside of business hours?

Long jobs contribute to server load and may slow down user sessions. If the scheduled job load is very high at the same time as the user load, you may want to configure a dedicated server instance to run jobs. This advanced cluster architecture is beyond the scope of this document. For more information about running scheduled jobs, see [Job Schedulers](job-schedulers.md).

Client connectivity is also an issue, because the slowest link in the network creates a bottleneck. There's a difference in system performance and scalability between users working remotely over DSL and those in the office on your corporate T1 network.
