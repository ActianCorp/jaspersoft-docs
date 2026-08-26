---
title: Configuring JasperReports Server for CAS Authentication
description: We provide sample files for configuring JasperReports Server for external CAS authentication. These files are specific to your edition (commercial or community). CAS sample files are located in the...
---

# Configuring JasperReports Server for CAS Authentication

We provide sample files for configuring JasperReports Server for external CAS authentication. These files are specific to your edition (commercial or community). CAS sample files are located in the &lt;js‑install&gt;/samples/externalAuth-sample-config directory of your JasperReports Server.

The sample files in your deployment that integrate Spring Security’s default CAS implementation with JasperReports Server may include the following:

-   sample-applicationContext-externalAuth-CAS.xml (community only): Sample file for integrating CAS with JasperReports Server, assigning the same roles to all users.
-   sample-applicationContext-externalAuth-CAS-staticRoles.xml (community only): Sample file for integrating CAS with JasperReports Server, assigning additional roles to a list of administrative users.
-   sample-applicationContext-externalAuth-CAS-db-mt.xml (commercial editions only): Sample file for integrating CAS with JasperReports Server with support for multiple organizations, retrieving role and organization data from a JDBC database.
-   sample-applicationContext-externalAuth-CAS-LDAP-mt.xml (commercial editions only): Sample file for integrating CAS with JasperReports Server with support for multiple organizations, retrieving role and organization data from an LDAP server.

!!! note

    To use LDAP or an external database with CAS, configure the LDAP or database connection parameters in default_master.properties before installing JasperReports Server. You can set up encryption for the password to your LDAP server or database at that time. See the JasperReports Server Security Guide for more information.

To configure JasperReports Server to work with your implementation of CAS, select the sample configuration file you want, then modify and deploy it:

1.  Make a copy of the CAS sample file and name it in the form applicationContext-&lt;Name&gt;.xml, for example, applicationContext-externalAuth-CAS-staticRoles-mt.xml.
2.  Edit the file you created and configure the beans correctly for your deployment, as described in the following sections.
3.  Place the modified applicationContext-externalAuth-CAS-staticRoles-mt.xml file in the &lt;js-webapp&gt;/WEB-INF directory.

!!! note

    &lt;js-webapp&gt; is the location of the JasperReports Server web application in your application server, or where you're modifying the configuration files, as explained in [WEB-INF Directory Location](../authentication-in-jrs/sample-files.md). The rest of this chapter refers to file names alone.
