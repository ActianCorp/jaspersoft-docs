---
title: Downloading the Software
description: The scalable query engine is contained in scalable-query-engine- 10.1.0 .jar in the WAR (web archive) file distribution of JasperReports Server. There are also additional files for Docker and...
---

# Downloading the Software

The scalable query engine is contained in scalable-query-engine- 10.1.0 .jar in the WAR (web archive) file distribution of JasperReports Server. There are also additional files for Docker and Kubernetes in a GitHub that you can clone. You do not need an account on github.com, but you do need the Git software locally on the host where you download and install JasperReports Server.

## Prerequisites

This deployment is based on a licensed installation of the JasperReports Server WAR file distribution, enterprise edition 10.1.0 or later. The scalable query engine is not supported with the JasperReports Server binary installer, any evaluation version, or the Community Project. You must complete the installation and configuration of the server, in particular the keystore (either generated new or imported from a previous version) before deploying the scalable query engine. See the rest of this JasperReports Server Installation Guide or the JasperReports Server Upgrade Guide to complete your server installation before continuing.

You will also need the following third-party software for this deployment:

-   git

-   Docker engine (20.x+) including Docker Compose V2 (3.9+)

-   Kubernetes (1.25+) including kubectl

-   Helm 3.5

This manual assumes that this software is installed and available in your path. You should be proficient with the concepts and commands for these tools.

## Downloading From Git

After installing the JasperReports Server WAR file distribution, you need to download the GitHub project that contains folders for Docker and Kubernetes.

1.  Go to the base folder of the unzipped WAR file distribution, referred to as `<js-install>` in this manual. The content of the GitHub repository must be placed in this folder:

    `cd jasperreports-server-pro-10.1.0-bin`

    Run the following command to download the project from GitHub:

    ``` text
    git clone git@github.com:TIBCOSoftware/js-docker.git
    ```

The `jaspersoft-containers` project in Git includes the following top-level folders:

| Folder | Description |
|----|----|
| `Docker/scalableQueryEngine` | Docker components for the Scalable Query Engine, described in [Docker Configuration](docker.md). |
| `Docker/jrs` | Docker components for a containerized version of JasperReports Server, which is beyond the scope of this document. |
| `K8s/scalableQueryEngine` | Kubernetes components for the Scalable Query Engine, described in [Deploying with Kubernetes](kubernetes.md). |
| `K8s/jrs` | Kubernetes components for the containerized version of JasperReports Server, which is beyond the scope of this document. |
