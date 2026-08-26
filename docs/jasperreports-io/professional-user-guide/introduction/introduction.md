---
title: Introduction to JasperReports® IO Professional Edition
description: "JasperReports IO is an HTTP-based reporting service for JasperReports® Library, providing an interface to the JasperReports Library reporting engine through the use of a REST API and a JavaScript..."
---

# Introduction to JasperReports® IO Professional Edition

JasperReports IO is an HTTP-based reporting service for JasperReports® Library, providing an interface to the JasperReports Library reporting engine through the use of a REST API and a JavaScript API. The REST API provides services for running, exporting, and interacting with reports while the JavaScript API allows you to embed reports and their input controls into your web pages and web applications using JavaScript frameworks for the layout and style sheets (CSS) to control the look and feel. Report templates, data sources, and all report resources are stored in a local repository or in an Amazon Web Services (AWS) S3 bucket and you have the option to create new report templates using Jaspersoft® Studio.

The JasperReports IO service can be deployed in various ways, from a single web application with interactive reports for small-scale deployments, to container-based deployments in the cloud, where specialized services running in separate containers work together to deliver a single, embeddable reporting service for large-scale deployments.

JasperReports IO is available as a downloadable standalone package and as an hourly offering on the AWS Marketplace.

This chapter contains the following sections:

-   JasperReports IO Professional Edition License Usage and Restrictions
-   [Installing JasperReports IO Using the Standalone Package](installation.md)
-   [Installing JasperReports IO For AWS](aws_installation.md)

## JasperReports IO Professional Edition License Usage and Restrictions

This version of JasperReports IO can simultaneously run up to the licensed number of concurrent report runs, with queuing of additional requests. Usage is restricted to a single machine instance and it may not be deployed into an environment where multiple JasperReports IO instances are used to distribute the workload for a single end use application.

JasperReports IO licensees are entitled to use Jaspersoft Studio Professional to create reports. JasperReports IO Professional for AWS users must register via a link on the AWS Marketplace product page to receive a copy of Jaspersoft Studio Professional. Users that obtain the downloadable copy of JasperReports IO from the `Jaspersoft.com` site are entitled to apply the license file from the JasperReports IO Professional installation to their Jaspersoft Studio installation.
