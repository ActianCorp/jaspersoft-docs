---
title: Introduction
description: "JasperReports® Server builds on JasperReports® Library as a comprehensive family of Business Intelligence (BI) products, providing robust static and interactive reporting, report server, and data..."
---

# Introduction

JasperReports® Server builds on JasperReports® Library as a comprehensive family of Business Intelligence (BI) products, providing robust static and interactive reporting, report server, and data analysis capabilities. These capabilities are available as either stand-alone products, or as part of an integrated end-to-end BI suite. The products utilize common metadata and provide shared services, such as security, a repository, and scheduling. The server exposes comprehensive public interfaces. This enables seamless integration with other applications and the capability to add custom functionality with ease.

!!! info "Important"

    The features in this section may be restricted by your JasperReports Server software license. If you don't see some of the options described, your current license likely prohibits their use. Contact us to learn about your licensed features or to discuss upgrading.

The heart of the Jaspersoft® BI Suite is the server, which provides the ability to:

-   Easily create reports based on views designed in an intuitive, web-based, drag and drop Ad Hoc Editor.
-   Efficiently and securely manage many reports.
-   Interact with reports, including sorting, changing formatting, entering parameters, and drilling on data.
-   Schedule reports for distribution through email and storage in the repository.
-   Arrange reports and web content to create appealing, data-rich Jaspersoft Dashboards that quickly convey business trends.

For users interested in multi-dimensional modeling, we offer Jaspersoft® OLAP, which runs as part of the server.

While the Ad Hoc Editor lets users create simple reports, more complex reports can be created outside of the server. You can either use Jaspersoft® Studio or manually write JRXML code to create a report that can be run in the server. We recommend that you use Jaspersoft Studio unless you have a thorough understanding of the JasperReports file structure.

You can use the following sources of information to learn about JasperReports Server:

-   Our core documentation describes how to install, administer, and use JasperReports Server and Jaspersoft Studio. Core documentation is available in PDF format on the [Product Documentation website](https://community.jaspersoft.com/documentation/). You can also access PDF and HTML versions of these guides from the [Documentation section](http://community.jaspersoft.com/documentation) of the Jaspersoft Community website.

-   Our Ultimate Guides document advanced features and configuration. They also include best practice recommendations and numerous examples. You can access PDF and HTML versions of these guides online from the [Documentation section](http://community.jaspersoft.com/documentation) of the Jaspersoft Community website.

-   The [Jaspersoft Community site](https://community.jaspersoft.com/) covers topics for:

    -   Developers
    -   System administrators
    -   Business users
    -   Data integration users

-   Our free samples, which are installed with JasperReports Library, Jaspersoft Studio, and JasperReports Server, are available and documented online. Please visit our [GitHub repository](https://github.com/Jaspersoft/jasperreports).

-   If you have a subscription to our professional support offerings, please contact our Technical Support team when you have questions or run into difficulties. They're available on the web at <https://www.jaspersoft.com/support>.

JasperReports Server is a component of commercial offerings. It integrates the standard features such as security, scheduling, web services interface, and much more for running and sharing reports. Commercial editions provide additional features for hosting large BI deployments, including:

-   Reporting Engine
-   Pixel-perfect report designer
-   Web-based design tool
-   Interactive visualizations
-   HTML5 charts
-   Maps
-   HTML Pro component
-   Custom visualizations
-   Ad Hoc views and reports
-   Advanced charts
-   Business Intelligence dashboards
-   Domains/metadata layer
-   Data virtualization
-   Data snapshots
-   Bursting
-   Alerting
-   Audit logging (administration/tracking)
-   Multi-organization architecture
-   Clustering
-   White labelling

This guide assists developers in obtaining, setting up, building, and running JasperReports Server from its source files.

!!! note

    This document describes how to build from a command line shell in Linux or Windows. It does not address the process of building within an IDE (Integrated Development Environment) such as Eclipse or IntelliJ.

## Supported Build Configurations

The following table lists the target configurations that can be built from the source:

<table>
<thead>
<tr>
<th><p>Application Server</p></th>
<th><p>Database</p></th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="5"><p>Tomcat or JBoss</p></td>
<td><p>PostgreSQL</p></td>
</tr>
<tr>
<td><p>MySQL</p></td>
</tr>
<tr>
<td><p>Oracle</p></td>
</tr>
<tr>
<td><p>SQL Server</p></td>
</tr>
<tr>
<td><p>DB2</p></td>
</tr>
</tbody>
</table>

## JasperReports Server Source Code Archives and Current Files

The following table lists the source code archive files and current files for JasperReports Server:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th><p>File</p></th>
<th><p>Description</p></th>
<th><p>Documented In</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>js-jrs</code><code>_10.1.0</code></p>
_src.zip</td>
<td><p>JasperReports Server source code</p></td>
<td><p><a href="building_jasperreports_server_source.md">Building JasperReports Server Source Code</a></p></td>
</tr>
<tr>
<td>js-jrs_
<p><code>js-jrs</code><code>_10.1.0</code></p>
_repo.zip</td>
<td>JasperReports Server repository files</td>
<td><a href="building_jasperreports_server_source.md">Building JasperReports Server Source Code</a></td>
</tr>
</tbody>
</table>
