---
title: Configuring JasperReports Server for External Database Authentication
description: "To use an external database with your JasperReports Server, configure the database connection parameters in defaultmaster.properties before installing JasperReports Server. You can set up encryption..."
---

# Configuring JasperReports Server for External Database Authentication

To use an external database with your JasperReports Server, configure the database connection parameters in default_master.properties before installing JasperReports Server. You can set up encryption for the password for your database at that time. See the JasperReports Server Security Guide for more information.

A sample file for configuring JasperReports Server for external database authentication is included in the JasperReports Server distribution. To configure JasperReports Server to work with your external database, modify and deploy the sample configuration file as follows:

1.  Make a copy of the external database sample file:<br>
    \<js-install\>/samples/externalAuth-sample-config/sample-applicationContext-externalAuth-db-mt.xml and name it applicationContext-externalAuth-db-mt.xml.
2.  Edit the file you created and configure the beans correctly for your deployment, as described in the following sections.
3.  Place the modified applicationContext-externalAuth-db-mt.xml file in the \<js-webapp\>/WEB-INF directory.

!!! note

    `<js-webapp>` is the location of the JasperReports Server web application in your application server, or where you're modifying the configuration files. The rest of this chapter refers to file names alone.
