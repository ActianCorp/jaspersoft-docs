---
title: Logging into the Server
description: "After JasperReports Server starts up, log in by going to this URL:"
---

# Logging into the Server

After JasperReports Server starts up, log in by going to this URL:

`http://<hostname>:8080/``jasperserver`` ``-pro`` `

Example:

`http://localhost:8080/``jasperserver`` ``-pro`` `

`http://jasperserver.example.com:8080/``jasperserver`` ``-pro`` `

The login page appears after compiling the necessary JSP files (this may take a few moments).

Use the following credentials to log into JasperReports Server:

| User ID     | Password    | Description                                |
|-------------|-------------|--------------------------------------------|
| superuser   | superuser   | System-wide administrator                  |
| jasperadmin | jasperadmin | Administrator for the default organization |

If you logged in successfully, your JasperReports Server home page appears.

!!! warning

    When you complete the evaluation or testing of your JasperReports Server instance, change the administrator and superuser passwords (jasperadmin and superuser) and remove any sample end-users. Leaving the default passwords and end-users in place weakens the security of your installation.

Refer to the JasperReports Server User Guide to begin adding reports and other objects to the server.

## JasperReports Server Heartbeat

After your initial login, you're asked to opt in to the JasperReports Server Heartbeat. The heartbeat helps Jaspersoft understand customer installation environments to improve our products. If you choose to enable the heartbeat, an HTTPS call at server startup time sends information like this to Jaspersoft:

- Operating System and JVM type and version

- Application Server and Database type and version

- JasperReports Server type and version

- Unique, anonymous identifier value

You can manually enable or disable the heartbeat by modifying the following property file `jasperserver`` ``-pro`` /WEB-INF/js.config.properties`. To disable the heartbeat, set the `heartbeat.enabled` property to `false`:

`heartbeat.enabled=false`

For additional information about enabling and disabling the heartbeat component, see the JasperReports Server Administrator Guide.
