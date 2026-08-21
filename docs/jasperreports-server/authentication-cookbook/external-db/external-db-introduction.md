---
title: External Database Authentication
description: "This chapter shows how to configure JasperReports Server to perform external authentication and authorization using tables in an external database. To help you with this, the JasperReports Server..."
---

# External Database Authentication

This chapter shows how to configure JasperReports Server to perform external authentication and authorization using tables in an external database. To help you with this, the JasperReports Server deployment includes a sample file, sample-applicationContext-externalAuth-db-mt.xml, that serves as a template for external database authentication. Customizing this template should satisfy the requirements of most external database authentication cases.

This chapter assumes you have some familiarity with Spring Security filter chains. Examples in this chapter assume you are running JasperReports Server on an application server, such as Apache Tomcat, and an external SQL database.

This chapter contains the following sections:

- [Overview of External Database Authentication](external-db-authentication-steps.md)
- [Configuring JasperReports Server for External Database Authentication](external-db-configuring-jrs.md)
- [Beans to Configure](external-db-beans.md)
- [Configuring User Authentication and Authorization via Database Queries](external-db-authentication-queries.md)
- [Setting the Password Encryption](external-db-password-encryption.md)
- [Mapping User Roles](external-db-mapping-roles.md)
- [Setting the User Organization](external-db-setting-user-organization.md)
- [Setting the Database Connection Parameters](external-db-setting-connection-parameters.md)
- [Configuring the Login Page for a Single-Organization Deployment](external-db-single-org-login.md)
- [Restarting JasperReports Server](external-db-jrs-restart.md)
