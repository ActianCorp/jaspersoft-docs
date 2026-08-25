---
title: Logging into the Server
description: "1. Go to the following URL to log in:"
---

# Logging into the Server

1.  Go to the following URL to log in:

    `http://<hostname>:9080/jasperserver-pro`

    where \<hostname\> is localhost, a machine name, or an IP address. The login page should appear after some time to compile the necessary JSP files.

2.  Log in with administrative credentials:

| User ID       | Password      | Description                                |
|---------------|---------------|--------------------------------------------|
| `superuser`   | `superuser`   | System-wide administrator                  |
| `jasperadmin` | `jasperadmin` | Administrator for the default organization |

If you have trouble logging in and get the following error message, you may be running at a WebSphere patch level that needs further configuration:

`Page cannot be found, HTTP 404 error`

Refer to the troubleshooting section [Websphere Modifications](../../../installation-guide/troubleshooting/application_server_related_problems.md).

!!! note

    The first time you log into JasperReports Server, you will be prompted to opt in to the JasperReports Server Heartbeat. For more information, refer to [JasperReports Server Heartbeat](../../../installation-guide/warfileinstall/war_logging_into_jrs.md).

Refer to the JasperReports Server User Guide to begin adding reports and other resources to JasperReports Server.
