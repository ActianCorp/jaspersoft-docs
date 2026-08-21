---
title: CAS Authentication
description: "Central Authentication Service (CAS) is an open source, Java-based authentication server that supports for single sign-on (SSO) across web applications, including those running on different..."
---

# CAS Authentication

Central Authentication Service (CAS) is an open source, Java-based authentication server that supports for single sign-on (SSO) across web applications, including those running on different application servers. When a user requests a page from a CAS-enabled web application, the application redirects the user to the CAS server login page. Thereafter, logged-in users can navigate among all participating applications without needing to log in again. Each application communicates with the CAS server in the background to verify that the user is valid before providing access to its resources.

With the CAS protocol, the client application (such as JasperReports Server) never receives or transmits the user’s password. As a result, the client application doesn't need to apply any encryption to protect passwords. However, unlike LDAP, CAS does not provide any user context, such as roles or organizations, that can be mapped to JasperReports Server. Instead, you can configure any organization and static roles that apply to each CAS-authenticated user, or pull user details from an external data source.

This chapter shows how JasperReports Server’s default authentication mechanism using Spring Security can be configured to perform external authentication with CAS. The JasperReports Server deployment includes several sample files that provide the beans for CAS integration. The implementation of these beans is sufficient to enable CAS authentication but may not provide enough functionality in a complex deployment. Further customization of these beans is beyond the scope of this guide.

This chapter assumes that you're familiar with security concepts such as certificates, tokens, and cookies. The first section explains how to install a CAS server for testing. All examples refer to the test server and assume you're using the Apache Tomcat application server. When configuring JasperReports Server to use CAS in production, you must take into account any differences between application servers and the contents of certificates.

This chapter contains the following sections:

- [Overview of External CAS Authentication](cas-authentication-steps.md)
- [CAS Server for Testing](cas-test-server.md)
- [Configuring JasperReports Server for CAS Authentication](cas-configuring-jrs.md)
- [Configuring Java to Trust the CAS Certificate](cas-configuring-java-certificate-trust.md)
- [Beans to Configure](cas-beans.md)
- [Setting CAS Authentication Properties](cas-setting-authentication-properties.md)
- [Setting User Roles](cas-setting-user-roles.md)
- [Setting the User Organization](cas-setting-user-organization.md)
- [Restarting JasperReports Server](cas-jrs-restart.md)
