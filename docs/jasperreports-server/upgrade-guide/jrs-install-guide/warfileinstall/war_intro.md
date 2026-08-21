---
title: Installing the WAR File for Production
description: "For production environments, use the stand-alone WAR file distribution to install the JasperReports Server application. Jaspersoft Technical Support (http://support.jaspersoft.com) or contact your..."
---

# Installing the WAR File for Production

For production environments, use the stand-alone WAR file distribution to install the JasperReports Server application. [[Jaspersoft Technical Support](https://www.jaspersoft.com/support) ](http://support.jaspersoft.com) or contact your sales representative.

The WAR file distribution contains the JasperReports Server web archive file and the scripts to create and load the database. With the integration JasperReports Server and JasperReports Web Studio, two application WAR files, `jrws-jrio.war` and `jrws-repository.war`, are added to the WAR file distribution.

!!! note

    JasperReports Web Studio is the visual designer for creating and editing report templates for the reporting engine and the whole Jaspersoft family of products. It uses an open-source library to produce dynamic content and rich data visualizations. It comes as a web-based alternative to Jaspersoft Studio, the desktop application, which is the most complete and powerful designer for JasperReports templates.

**Important Java Development Kit (JDK) 17 note**: As of release 10.0.0, Tomcat 10.1.24 or higher and Tomcat 11.0.11 or higher are supported by JasperReports Server on a system with JDK 17. An additional installation step is required on a system with JDK 17, which requires adding the JAVA_OPTS environment variable.

This chapter describes how to install the WAR file on the Apache Tomcat and JBossEAP/Wildfly application servers. For other application servers, see [Installing the WAR File for WebLogic](../../../installation-guide/weblogic/warweblogic.md) or [Installing the WAR File for WebSphere](../../../installation-guide/websphere/websphere_intro.md). For a list of supported JDK/JVMs, application servers, databases, operating systems, and browsers, refer to the TIBCO JasperReports® Server Supported Platform Datasheet.

This chapter contains the following sections:

- [WAR File Distribution](../../../installation-guide/warfileinstall/war-overview.md)

- [Applications Supported by the WAR File Distribution](../../../installation-guide/warfileinstall/applications_supported_by_the_war_fi.md)

- [Installing the WAR File Using js-install Scripts](../../../installation-guide/warfileinstall/war_install_using_js_install.md)

- [Additional Steps for Using DB2 and js-install Scripts](../../../installation-guide/warfileinstall/additional_steps_for_using_db2_and_j.md)

- [Starting JasperReports Server](../../../installation-guide/warfileinstall/starting_jasperreports_server.md)

- [Logging into JasperReports Server](../../../installation-guide/warfileinstall/war_logging_into_jrs.md)

- [Troubleshooting Your JasperReports Server Configuration](../../../installation-guide/warfileinstall/war_troubleshooting_jrs.md)

- [Installing the WAR File Manually](../../../installation-guide/warfileinstall/war_install_manually.md)
