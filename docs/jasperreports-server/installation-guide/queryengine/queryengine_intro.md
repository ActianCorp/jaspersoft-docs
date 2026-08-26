---
title: Scalable Query Engine
description: The JasperReports Server scalable query engine is a new feature in version 8.0 that supports high performance reporting under load. It uses Docker containers deployed through Kubernetes to create a...
---

# Scalable Query Engine

The JasperReports Server scalable query engine is a new feature in version 8.0 that supports high performance reporting under load. It uses Docker containers deployed through Kubernetes to create a cluster of virtual pods that process Ad Hoc views in parallel.

The scalable query engine is completely optional: you can choose whether to deploy it during installation, later, or not at all. For small deployments without performance issues, no further installation is necessary and you may skip this chapter. If you have hundreds of users and experience performance issues when displaying dashboards, this chapter explains how to install and configure the scalable query engine.

This chapter contains the following sections:

-   [Overview](overview.md)

-   [Architecture](architecture.md)

-   [Downloading the Software](downloading.md)

-   [Docker Configuration](docker.md)

-   [Deploying with Kubernetes](kubernetes.md)

-   [Configuring JasperReports Server](configuring_jrs.md)

-   [Logging and Debugging](logging.md)
