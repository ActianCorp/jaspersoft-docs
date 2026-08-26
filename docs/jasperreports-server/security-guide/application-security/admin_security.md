---
title: Application Security
description: "This chapter describes the configuration settings that protect JasperReports Server and its users from unauthorized access. The configuration properties appear in two locations:"
---

# Application Security

This chapter describes the configuration settings that protect JasperReports Server and its users from unauthorized access. The configuration properties appear in two locations:

-   Some properties must be configured during the installation and deployment phase, before users access the server. These settings are configured through files used by the installation scripts. These settings are available only when performing a WAR file installation.
-   Properties you can configure after installation are located in files in various folders. Configuration file paths are relative to the `<js-install>` directory, which is the root of your JasperReports Server installation. To change the configuration, edit these files then restart the server.

Because the locations of files described in this chapter vary with your application server, the paths specified in this chapter are relative to the deployed WAR file for the application. For example, the `applicationContext.xml` file is shown as residing in the WEB-INF folder. If you use the Tomcat application server bundled with the installer, the default path to this location is:

`C:\Program Files\jasperreports-server-10.1\apache-tomcat\webapps\jasperserver-pro\WEB-INF`

!!! warning

    Use caution when editing the properties described in this chapter. Inadvertent changes may cause unexpected errors throughout JasperReports® Server that may be difficult to troubleshoot. Before changing any files, back them up to a location outside of your JasperReports® Server installation.

    Do not modify settings not described in the documentation. Even though some settings may appear straightforward, values other than the default may not work properly and may cause errors.

This chapter contains the following sections:

-   [Encrypting Passwords in Configuration Files](encrypting_passwords_in_files.md)
-   [Configuring CSRF Protection](configuring_csrf_protection.md)
-   [Configuring XSS Protection](configuring_xss_protection.md)
-   [Protecting Against SQL Injection](sql_injection_protection.md)
-   [Protecting Against XML External Entity Attacks](xxe-protection.md)
-   [Protecting Against Clickjacking Attacks](xxe-protection.md)
-   [Restricting File Uploads](restricting_file_uploads.md)
-   [Restricting Groovy Access](restrict-groovy-access.md)
-   [Hiding Stack Trace Messages](hiding_stack_trace_messages.md)
-   [Defining a Cross-Domain Policy for Flash](cross_domain_policy_for_flash.md)
-   [Using SSL in the Web Server](using-ssl-in-web-server.md)
-   [Disabling Unused HTTP Verbs](disabling-unused-http-verbs.md)
-   [Configuring HTTP Header Options](config-http-header-options.md)
-   [Setting the Secure Flag on Cookies](setting-secure-flag-on-cookies.md)
-   [Setting httpOnly for Cookies](setting-httponly-for-cookies.md)
-   [Using a Protection Domain Infrastructure](using-a-protection-domain-infrastructure.md)
-   [Encrypting Passwords in URLs](encrypting-passwords-in-urls.md)
-   [Host Header Injection Protection](host-header-injection-protection.md)
