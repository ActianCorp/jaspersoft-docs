---
title: JasperReports Server Distributions
description: "JasperReports Server is a web application that runs in an app server and uses an external database to store its repository. Depending on your use case, JasperReports Server is available in a WAR file..."
---

# JasperReports Server Distributions

JasperReports Server is a web application that runs in an app server and uses an external database to store its repository. Depending on your use case, JasperReports Server is available in a WAR file for production.

-   The WAR (web archive) file is a zipped file containing only the JasperReports Server web app. To install the WAR file in production, you must first install and configure one of the supported app servers (for example Tomcat, JBoss, WebLogic, or Websphere) and one of the supported databases (most major relational databases). These servers can be in the cloud or on premises, shared with other web apps or dedicated to JasperReports Server (recommended), but they should be configured for performance under the expected load, reliability (uptime), security, and backups.

    The WAR file distribution includes scripts that you edit to specify your app server and database. When you run these scripts, they create the necessary tables in your database and copy the files of the web app to your app server. You can also import an existing repository if you are upgrading from a previous version of JasperReports Server. For more information, see [Installing the WAR File for Production](../warfileinstall/war_intro.md). For the list of supported app servers and databases, see the Jaspersoft Platform Support Guide for this release.

The WAR file is available from [Technical Support](https://jira.tibco.com/browse/JS-76039).
