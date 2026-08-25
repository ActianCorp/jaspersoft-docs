---
title: Introduction
description: JasperReports IO (JRIO) is an HTTP-based reporting service that provides an interface to the JasperReports Library reporting engine through the use of a REST API and a JavaScript API. The REST API...
---

# Introduction

JasperReports IO (JRIO) is an HTTP-based reporting service that provides an interface to the JasperReports Library reporting engine through the use of a REST API and a JavaScript API. The REST API provides services for running, exporting, and interacting with reports while the JavaScript API allows you to embed reports and their input controls into your web pages and web applications using style sheets (CSS) to control the look and feel. Report templates, data sources, and all report resources are stored in a local repository or in an Amazon Web Services (AWS) S3 bucket and you have the option of creating new report templates using Jaspersoft Studio.

JasperReports IO At-Scale is a container-based deployment of JasperReports IO for enterprise applications. JRIO At-Scale allows you to scale the JRIO service in various ways because specialized sub-services run in separate containers but work together to deliver a single, embeddable reporting service. JRIO At-Scale can also be used as a super-scalable reporting engine for JasperReports Server that is transparent to end users. In this configuration, the reports displayed in the server are processed by JRIO At-Scale.

For testing and small-scale deployments, you can create a monolithic web application with all sub-services hosted together. For large-scale deployments, services can run in separate containers and are able to scale automatically for high performance. You can deploy a cluster using Kubernetes or Amazon AWS EKS (Amazon Elastic Kubernetes Service) to scale up to thousands of reports per hour and thousands of pages per report.
