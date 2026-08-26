---
title: Installing the WAR File for WebLogic
description: "JasperReports Server supports deployment on the WebLogic Application Server, but requires its own database to store information such as users, organizations, and the repository. WebLogic users need..."
---

# Installing the WAR File for WebLogic

JasperReports Server supports deployment on the WebLogic Application Server, but requires its own database to store information such as users, organizations, and the repository. WebLogic users need the WAR file distribution to install JasperReports Server. Download the WAR file distribution from [Jaspersoft Technical Support](https://www.jaspersoft.com/support) or contact your sales representative. The WAR file distribution comes in a file named

`js-jrs``_10.1.0`

\_bin.zip.

The WAR file distribution includes two sample databases containing data for optional demos. For evaluation, we recommend you install the sample databases. In a production environment, we advise against installing sample data of any kind. You create and initialize the required repository database and the optional sample databases before deploying JasperReports Server in WebLogic. The WebLogic administrator uses the WebLogic Administrative Console or domain `config.xml` to deploy JasperReports Server.

This chapter contains the following sections:

-   [Procedure for Installing the WAR File for WebLogic](weblogic_install_procedure.md)
-   [Setting Java Properties](setting_java_properties.md)
-   [Configuring Other Database Connections](weblogic_database_connections.md)
-   [Starting the Server](weblogic_starting_jrs.md)
-   [Logging into the Server](logging_into_jasperreports_server3.md)
-   [Configuring Report Scheduling](configuring_report_scheduling2.md)
-   [Restarting the Server](restarting_jasperreports_server.md)
-   [Updating XML/A Connection Definitions (Optional)](updating_xml_a_connection_definition2.md)
-   [Troubleshooting Your JasperReports Server Configuration](weblogic_troubleshooting_jrs.md)
