---
title: Using a Local Repository
description: "Typically, JasperReports IO At-Scale cluster accesses the repository in a JasperReports Server instance, as described in Connecting to a JasperReports Server Repository. As an option for high..."
---

# Using a Local Repository

Typically, JasperReports IO At-Scale cluster accesses the repository in a JasperReports Server instance, as described in [Connecting to a JasperReports Server Repository](configuration.md). As an option for high performance needs, you can also use a local repository in every deployed jrio-reporting pod, jrio-export pod, and jrio-rest pod. By using a file-based repository in the docker images, JRIO can process some requests locally, which is about 20% faster than using the server's repository.

Several repository structures are possible in JasperReports IO At-Scale, the same as with JasperReports IO Professional:

- This section describes how to create a repository of static files in the docker images. The files are static because they are copied and deployed in each pod without any mechanism to update the contents. To change the contents of the local repository, you must rebuild the docker images and redeploy every pod.
- You can have both a local repository and the JasperReports Server repository that are used at the same time. In this case, all requests that are proxied from the server to JRIO will use the server's repository, and all requests that you send to the JRIO REST service will resolve in the local repository.
- JasperReports IO At-Scale can also use an S3 repository, as described in the *AWS S3 Bucket Repository* section of the *Managing JasperReports IO* chapter in the JasperReports IO Pro User Guide. When using an S3 bucket, you can modify the contents of the repository without rebuilding the docker images.
- You can have several file repositories that will be accessed as one, as described in the *Configuring the Web Application Server to Use Multiple Repositories* section of the *Managing JasperReports IO* chapter in the JasperReports IO Pro User Guide.

The following procedure describes how to create a local, file-based repository copy in every docker pod.

To build the Docker images

1.  The file format of the file-based repository is described in the *JasperReports IO Repository* section of the *Managing JasperReports IO* chapter in the JasperReports IO Pro User Guide. Once you have all your resource files ready, copy them to the following folders:

    - jrio-reporting-docker/jrio-repository/samples
    - jrio-export-docker/jrio-repository/samples
    - jrio-rest-docker/jrio-repository/samples

    When building the docker images, files in the above locations are copied to the following locations:

    - jrio-reporting \> /usr/local/jrio
    - jrio-export \> /usr/local/jrio
    - jrio-rest \> /var/lib/jetty/webapps/jrio/repository

2.  Finish any other module configuration as described in [Configuring the Modules](configuration.md), then build the Docker images in [Building Docker Images](building_images.md).
