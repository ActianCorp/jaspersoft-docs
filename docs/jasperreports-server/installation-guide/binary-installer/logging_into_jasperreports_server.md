---
title: Logging into JasperReports Server
description: To log into JasperReports Server on any operating system
---

# Logging into JasperReports Server

To log into JasperReports Server on any operating system

1.  Start JasperReports Server.
2.  Open a supported browser: Firefox, Internet Explorer, Chrome, or Safari.
3.  Log into JasperReports Server by entering the startup URL in your browser’s address field. The URL depends upon your application server. If you installed the default, bundled Tomcat use:

`http://<hostname>:8080/``jasperserver`` ``-pro`` `

- `<hostname>` is the name or IP address of the computer hosting JasperReports Server.
- 8080 is the default port number for the Apache Tomcat application server. If you used a different port when installing your application server, specify its port number instead of 8080.

The login page appears.

1.  Log in using the following credentials:

| User ID     | Password    | Description                                |
|-------------|-------------|--------------------------------------------|
| superuser   | superuser   | System-wide administrator                  |
| jasperadmin | jasperadmin | Administrator for the default organization |

If you installed the sample data, these additional sample end-users are also created. These users are non-administrative users with fewer system privileges.

| User ID | Password | Description                                               |
|---------|----------|-----------------------------------------------------------|
| joeuser | joeuser  | Sample end-user                                           |
| demo    | demo     | Sample end-user for the SuperMart Dashboard demonstration |

!!! warning

    When you complete the evaluation or testing of your JasperReports Server instance, change the administrator and superuser passwords (jasperadmin and superuser) and remove any sample end-users. Leaving the default passwords and end-users in place weakens the security of your installation.

To log into JasperReports Server on Windows

On Windows, you can launch the login page from the desktop of the JasperReports Server host computer by clicking ****Start \> All Programs \> JasperReports Server\> JasperReports Server Login****.

To log into JasperReports Server on Mac OSX

On Mac OSX, you can launch the login page by going to Finder and clicking the following script:

`/Applications/<js-install>/jasperServerLogin`

For example: `/Applications/10.1.0/jasperServerLogin`

To use the Dock to log into JasperReports Server:

From Finder, you can drag the `/Applications/<js-install>/jasperServerLogin.app` to the Dock to handle logging into JasperReports Server using your default system browser.
