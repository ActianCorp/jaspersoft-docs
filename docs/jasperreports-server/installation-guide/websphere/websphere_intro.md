---
title: Installing the WAR File for WebSphere
description: "JasperReports Server supports deployment on the IBM WebSphere Application Server, but requires its own database to store information such as users, organizations, and the repository. WebSphere users..."
---

# Installing the WAR File for WebSphere

JasperReports Server supports deployment on the IBM WebSphere Application Server, but requires its own database to store information such as users, organizations, and the repository. WebSphere users must use the WAR file distribution to install JasperReports Server. Download the WAR file distribution from [Jaspersoft Technical Support](https://www.jaspersoft.com/support) or contact your sales representative. The WAR file distribution comes in a file named

`js-jrs``_10.1.0`

\_bin.zip.

The WAR file distribution also includes two sample databases containing data for optional demos. For evaluation, we recommend installing the sample databases. In a production environment, we advise against installing sample data of any kind. You create and initialize the required repository database and the optional sample databases before JasperReports Server is deployed in WebSphere. The WebSphere administrator uses the WebSphere Administrative Console to deploy JasperReports Server.

This chapter contains the following sections:

- [Procedure for Installing and Deploying the WAR File in WebSphere](websphere_install_procedure.md)

- [Logging into JasperReports Server](websphere_logging_in.md)

- [Configuring Report Scheduling](websphere_report_scheduling.md)

- [Updating XML/A Connection Definitions (Optional)](websphere_xmla_connection.md)

- [Troubleshooting your JasperReports Server Configuration](websphere_troubleshooting.md)
