---
title: Using Local Folder as a Repository
description: "It is possible to use a folder from the PC as a report repository. In the case JasperReports Web Studio is installed and used by a single report developer, the developer could work with reports from..."
---

# Using Local Folder as a Repository

It is possible to use a folder from the PC as a report repository. In the case JasperReports Web Studio is installed and used by a single report developer, the developer could work with reports from a laptop. To do that, a property should be configured in the startup script `jrws.repository.file.[name]`. For example:

For Linux:

`JRWS_ARGS="${JRWS_ARGS} -Djrws.repository.file.samples=/path/to/the/samples"`

For Windows:

`set "JRWS_ARGS=%JRWS_ARGS% -Djrws.repository.file.samples=C:/path/to/the/samples"`

It is also possible to configure multiple folders.

!!! note

    You can also configure a property by adding it in the `jrws.properties` file instead of modifying the script using `-D`.

!!! warning

    Because JasperReports Web Studio is listed by default on the `localhost:8088`, this folder is seen by other network users. To avoid this, the users must protect this port with a firewall (not allowing connections from outside) or configure the Jetty server to allow connections only from the `localhost`.
