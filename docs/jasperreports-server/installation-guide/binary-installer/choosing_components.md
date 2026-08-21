---
title: Choosing Installer Components
description: The installer is designed to get JasperReports Server up and running quickly. The server requires an application server and a database. The installation executable lets you choose whether to install...
---

# Choosing Installer Components

The installer is designed to get JasperReports Server up and running quickly. The server requires an application server and a database. The installation executable lets you choose whether to install bundled components or use versions of these already present on your system.

## Bundled Components

The installer distribution bundles the following components:

| Component | Description |
|----|----|
| JasperReports Server Application | WAR file and configuration support scripts. |
| Apache Tomcat | Web application container. You can use the bundled version or an existing version. |
| PostgreSQL Database | Database server. You can use the bundled version or an existing version. |

## Preparing Existing Components

You can use components that you have installed previously. Make sure that you are using supported versions of the components. For information about specific versions of third-party applications supported by the installer, refer to the JasperReports Server Supported Platform Datasheet.

- Tomcat application server: If you want to use an existing Tomcat, it must be on the local machine. See [Selecting Third-Party Components](select-tomcat.md) for more information.

- PostgreSQL database: If you want to use an existing PostgreSQL, it can be on a local or remote machine. If it’s on a remote Linux machine, configure PostgreSQL to allow remote connections as described in [Enabling Connections to a Remote Host](select-postgresql.md). See [Selecting a PostgreSQL Configuration](select-postgresql.md) for more information.

- Chrome/Chromium browser: See [Selecting a Chrome/Chromium Configuration](select-phantomjs.md) for more information.

!!! note

    If you want to use an existing PostgreSQL database instance, the database must be running at install time. If you want to use an existing Apache Tomcat, the Tomcat instance must be stopped.

If you choose to install the bundled Tomcat and database, both are installed on the same host as the server.
