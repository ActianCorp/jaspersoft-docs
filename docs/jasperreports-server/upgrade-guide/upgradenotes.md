---
title: Upgrading JasperReports Server 6.4.x or Earlier
description: "If you are running JasperReports Server version 6.4.x or earlier, your upgrade requires multiple steps."
---

# Upgrading JasperReports Server 6.4.x or Earlier

## Upgrading from 6.4.x or Earlier

If you are running JasperReports Server version 6.4.x or earlier, your upgrade requires multiple steps.

If you are running JasperReports Server 6.0 through 6.4.x:

1.  Upgrade to the latest version of 7.1.x.
2.  Upgrade from 7.1.x to version 8.2.
3.  Upgrade from 8.2 to version 9.0.
4.  Upgrade from 9.0 to version 10.1.

The steps for upgrade to 6.3.x, 6.4.x, 7.1.x or 8.x.x are documented in the *JasperServer Installation Guide* for that release. Download the JasperReports Server WAR file distribution zip package for the release that you want to get the relevant files and documentation. The Installation Guide is in the docs folder.

You can download the JasperReports Server WAR file distribution zip package from [Jaspersoft Technical Support](https://www.jaspersoft.com/support) or contact your sales representative.

If you are running a JasperServer version earlier than 3.7, first upgrade to 3.7.0, then to 6.3.x, then 7.x to 8.x and then to 9.0.

## Best Practices for Upgrading on Windows

The two methods for installing JasperReports Server are:

1.  Installing with the Binary Installer and Bundled Components

    The binary installer is an executable that puts all the components in place to run JasperReports Server. For example, if you take the default installation choices, you get the Apache Tomcat application server, the PostgreSQL database, and the Java execution environment.

    But keep in mind that these components are specially configured to run a specific version of JasperReports Server. This applies to the Windows Start Menu items created to start and stop JasperReports Server.

2.  Installing to Pre-existing Components

    When installing a “Production" instance of JasperReports Server, you may want to install the main components before you install JasperReports Server. This way you have more control over updating and upgrading components like the application server, database, and Java.

    Once you put these components in place, you have two options for installing JasperReports Server:

    1.  Use the War File ZIP distribution (file name:

        `js-jrs``_10.1.0`

        \_bin.zip).

        You can install JasperReports Server to the existing components using the `js-install.bat` script. You create a `default_master.properties` file that specifies the location of the application server and database components.

    2.  Use the Binary Installer, ` `

        `js-jrs``_10.1.0`

        \_win_x86_64.exe.

        The installer prompts you for the location of the application server and database components.

If you intend to upgrade your Windows installation with future releases of JasperReports Server, we recommend installing pre-existing components. This reduces any post-upgrade confusion caused by the Windows Start menu showing the older version of JasperReports Server.
