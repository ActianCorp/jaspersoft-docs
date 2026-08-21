---
title: Jaspersoft IO At-Scale Modules
description: "Jaspersoft IO At-Scale contains several modules, also called pods, described in the following table. Each of these modules becomes a separate Docker image:"
---

# Jaspersoft IO At-Scale Modules

Jaspersoft IO At-Scale contains several modules, also called pods, described in the following table. Each of these modules becomes a separate Docker image:

| Module | Description |
|----|----|
| jrio-client | This module contains a sample HTML application with documentation. The jrio-client module is also used for sample viz.js implementation that is used in an embedded report viewer. |
| jrio-manager | This is the main manager or orchestrator module that also contains the license file. There is always exactly one instance of this module in the cluster. |
| jrio-reporting | This is the main reporting application that generates reports from JRXML, but the reports are generated as serialized Java objects to be stored in the Redis cache module. |
| jrio-rest | This module is responsible for inbound and outbound communication from the cluster, such that all tasks are input and output through this module. Its k8s service should be exposed. |
| redis | This module is responsible for caching and queuing all report creation tasks in a Redis queue. The jrio-reporting and jrio-rest pods monitor the Redis queue for new tasks requests or task results. The jrio-manager module also checks report execution status which is stored in the Redis queue. |
| jrio-export | The module that will generate the requested output format from the Java objects stored in the cache of the redis module. jrio-export stores all generated outputs back into the Redis cache. |
