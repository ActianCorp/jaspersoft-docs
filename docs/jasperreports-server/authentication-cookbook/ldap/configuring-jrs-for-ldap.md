---
title: Configuring JasperReports Server for LDAP Authentication
description: "To use LDAP with your JasperReports Server, configure the LDAP connection parameters in defaultmaster.properties before installing JasperReports Server. You can set up encryption for the password to..."
---

# Configuring JasperReports Server for LDAP Authentication

To use LDAP with your JasperReports Server, configure the LDAP connection parameters in default_master.properties before installing JasperReports Server. You can set up encryption for the password to your LDAP server at that time. See the JasperReports Server Security Guide for more information.

A sample file for configuring JasperReports Server for external LDAP authentication is included in the JasperReports Server distribution. Sample files are located in the \<js‑install\>/samples/externalAuth-sample-config directory of your JasperReports Server. The file included depends on your version of JasperReports Server:

- sample-applicationContext-externalAuth-LDAP.xml: Sample file for integrating LDAP with JasperReports Server with a single organization. This file is included in the community edition.
- sample-applicationContext-externalAuth-LDAP-mt.xml: Sample file for integrating LDAP with JasperReports Server with multiple organizations. This file is included in commercial editions of JasperReports Server. To use external authentication with a commercial version of JasperReports Server with a single organization, you need to modify the sample file as described in [Mapping to a Single Organization](ldap-setting-user-organization.md).

To configure JasperReports Server to work with your implementation of LDAP, modify and deploy the sample configuration file as follows:

1.  Make a copy of the LDAP sample file in the \<js-install\>/samples/externalAuth-sample-config/ directory and rename it to remove the sample- prefix.
2.  Edit the file you created and configure the beans correctly for your deployment, as described in the following sections.
3.  Place the modified file in the \<js-webapp\>/WEB-INF directory.

!!! note

    `<js-webapp>` is the location of the JasperReports Server web application in your application server, or where you're modifying the configuration files. The rest of this chapter refers to file names alone.
