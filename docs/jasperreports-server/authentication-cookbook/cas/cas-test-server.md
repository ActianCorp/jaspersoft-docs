---
title: CAS Server for Testing
description: "This section describes how to set up a simple CAS server for testing purposes. If you have a CAS server you want to use, you can skip this section."
---

# CAS Server for Testing

!!! note

    This section describes how to set up a simple CAS server for testing purposes. If you have a CAS server you want to use, you can skip this section.

The CAS server is Java servlet built on the Spring Framework. Its primary responsibility is to authenticate users and grant access to CAS-enabled services by issuing and validating tickets. You can download the server from the following page: <https://www.apereo.org/projects/cas>.

As described in the next section, the CAS validation service accepts only requests using a secure transport. This means you must have a valid certificate on your CAS server machine, and your CAS client (the JasperReports Server JVM) must be configured to trust that certificate. There are two important points to keep in mind:

- Test with the CAS server on a separate machine, not the localhost where JasperReports Server is installed. For this purpose, you can use a virtual machine.
- Most issues in configuring CAS are caused by the improper use of certificates. The single most common failure occurs when the hostname in the server’s certificate doesn’t match the actual hostname.

To create a certificate for the server you must use the Java `keytool` utility. Run the following command on the host of the CAS server:

`keytool -genkey -alias tomcat -keyalg RSA -validity 365 -keystore <filename>`

The utility prompts you for several pieces of information, two of which are critical. When prompted for your first and last name enter the hostname of the CAS server. When asked for the keystore password use `changeit` to match what Apache Tomcat uses by default.

After installation of the CAS server, configure the Apache Tomcat application server that's running the CAS server so it uses the certificate in the keystore created above. Modify \$CATALINA_HOME/conf/server.xml, locate the commented section about setting up a secure HTTPS connector, and follow the instructions it contains. Restart the Tomcat server and test that it accepts HTTPS connections.

For further information about CAS, including deployment information, documentation, and community links, refer to the CAS website <https://www.apereo.org/projects/cas>. In particular, the page [](https://apereo.github.io/cas/7.0.x/installation/Troubleshooting-Guide.html)<https://apereo.github.io/cas/7.0.x/installation/Troubleshooting-Guide.html> can help you deploy your certificates.

!!! note

    CAS server is based on Spring Security, like JasperReports Server. In a production environment, you must replace the built-in authentication for testing with an external authority that validates your users when they log into CAS. As with JasperReports Server, you can configure CAS with a variety of external authorities to suit your needs, including LDAP. However, the external authority used by CAS may not be accessible to JasperReports Server.

    Follow the CAS documentation to ensure you create a secure and robust configuration on your CAS server.
