---
title: Managing JasperReports IO
description: "After installing JasperReports IO, you will need to create the reports, web applications, and anything else you require for reporting and storing the files in a repository for the reporting service..."
---

# Managing JasperReports IO

After installing JasperReports IO, you will need to create the reports, web applications, and anything else you require for reporting and storing the files in a repository for the reporting service to use. The JasperReports IO installation includes many sample files that you can use for reference. You need to use a file browser on the host machine to view and manage the contents of the JasperReports IO installation.

This chapter covers the basics of managing your JasperReports IO installation, including:

- File directory structure
- The web application servers and web applications
- The repository
- AWS S3 buckets
- Cloud repositories
- Security permissions

Unless noted otherwise, all references to JasperReports IO are for the standalone version, not JasperReports IO for AWS.

!!! note

    For JasperReports IO for AWS, the reporting service is part of an instance hosted on Amazon Web Services. Use the AWS Management Console to manage the JasperReports IO instance hosted on the service. See [Managing JasperReports IO for AWS](repository.md) for information on managing JasperReports IO for AWS.

This chapter includes the following sections:

- JasperReports IO Directories
- JasperReports IO Reporting Service and Web Application Directories
- [Web Application Server](web_app_server.md)
- [JasperReports IO Repository](repository.md)
- [Managing AWS for JasperReports IO](repository.md)
- [Cloud Repositories for JasperReports IO](repository.md)
- [Security](security.md)

## JasperReports IO Directories

The directory where JasperReports IO is installed on the host machine is referred to as **`<jrio-install`**`>` in this guide. The `<jrio-install>` directory contains the start and stops scripts for the server and the license agreement. The contents of JasperReports IO are organized as the following directories when first installed:

| Directory | Description |
|----|----|
| `docker` | Contains a Dockerfile for creating a docker image of JasperReports IO, a start script for the image, and a repository configuration file. |
| `jetty` | Contains the Eclipse Jetty web application server that hosts the JasperReports IO web application. See [Web Application Server](web_app_server.md) for more information. |
| jre | Contains the Java Run time Environment for running the JasperReports IO reporting service. |
| `jrio` | Contains the files for the JasperReports IO reporting service and web applications. See JasperReports IO Standalone Reporting Service for more information. |
| `repository` | The repository stores all the resources used to run and create reports, including data source definitions, JRXML files, datatypes, and helper files such as images. See [Repository](repository.md) for more information. |

JasperReports IO Directories

## JasperReports IO Reporting Service and Web Application Directories

The `<jrio-install>/jrio/webapps` directory contains the files for the JasperReports IO reporting service, JavaScript API, and the sample web application.

| Directory | Description |
|----|----|
| `jrio` | The JasperReports IO web application, including the reporting service and all configuration files. |
| `jrio-client` | Contains the files for JasperReports IO's JavaScript API, including the `jrio.js` file and UI themes. See the JavaScript API for more information. |
| `jrio-docs` | Contains the files for the JasperReports IO sample web application, which demonstrates the capabilities of the reporting service, as well as documentation and report samples. |
| `ROOT` | The sample HTML file in this directory forwards root requests to the `jrio-docs` web application. |

Web Application Directories
