---
title: Job Schedulers
description: "The JasperReports Server scheduler is a module that exists in every server instance to run reports scheduled to run at a later time, either once or repeatedly. Schedules, also known as jobs, are..."
---

# Job Schedulers

The JasperReports Server scheduler is a module that exists in every server instance to run reports scheduled to run at a later time, either once or repeatedly. Schedules, also known as jobs, are stored in the repository to be triggered by the scheduler whenever necessary. For simplicity, schedulers are not shown in [Architecture of a Sample JasperReports Server Cluster](sample-cluster-architecture.md).

To prevent every instance from triggering the same job at the same time, the scheduler uses a software locking mechanism when accessing jobs in the repository. This allows the scheduler to be deployed on every instance in a cluster environment but ensures that any job is triggered only once. Jobs can be created by client sessions on any instance, then be run by the scheduler on any instance, and the client sees no difference. Job output will then be emailed as necessary and, if saved in the repository, accessible from any instance.

The scheduler is based on the Quartz scheduler, an open source library. The JasperReports Server includes settings for the scheduler in the file `<js-webapp>/WEB-INF/js.quartz.base.properties`. The default configuration of the scheduler includes the following settings that allow it to work in both stand-alone servers and clusters:

`org.quartz.scheduler.instanceId = AUTO`

`org.quartz.jobStore.isClustered = true`

Be sure to synchronize the clocks on all nodes, so the scheduler doesn’t always run jobs on the node with the earliest time. For further details, see the [online documentation for the Quartz scheduler](https://www.quartz-scheduler.org/documentation/quartz-2.3.0/configuration/).

There are advantages to running jobs on all the server instances. If several long jobs are scheduled at the same time, a single server must process them sequentially, and some won’t start at exactly the designated time. Multiple servers in a cluster can process those jobs in parallel, and they will start on time, at least for a number of jobs up to the number of instances.
