---
title: Configuring Logging for Debugging
description: "If your connection is failing, for example, with an “Invalid credentials supplied” error, and you cannot find information in the JasperReports Server logs, you may want to enable logging for Spring..."
---

# Configuring Logging for Debugging

If your connection is failing, for example, with an “Invalid credentials supplied” error, and you cannot find information in the JasperReports Server logs, you may want to enable logging for Spring Security or JasperReports Server external authentication.

To enable logging, add the corresponding line to the &lt;js‑webapp&gt;/WEB‑INF/log4j.properties file, in the form:

``` text
  log4j.logger.<logger-classname> = <log-level>, <output-type>
```

For example:

``` properties
  log4j.logger.org.springframework.security=DEBUG, stdout, fileout
```

You must restart the server for your changes to take effect. For more information about log configuration, see the JasperReports Server Administrator Guide.

You can reduce impact on performance by restricting logging to functionality that you are interested in, for example, to a subset of Spring Security instead of all of Spring Security. [Useful Logger Classnames for External Authentication](logging.md) shows some logger classnames commonly used when debugging authentication.

| Functionality to Log | Logger Classname |
|----|----|
| Spring Security | `org.springframework.security` |
| Subset of Spring Security related to LDAP | `org.springframework.security.ldap` |
| Useful subsets of Spring Security's LDAP logging | `org.springframework.security.ldap.userdetails.LdapAuthoritiesPopulator org.springframework.security.ldap.userdetails.LdapUserDetailsService org.springframework.security.ldap.search.LdapUserSearch org.springframework.security.ldap.search.FilterBasedLdapUserSearch org.springframework.security.ldap.SpringSecurityLdapTemplate` |
| Other LDAP-related Spring Security loggers | `org.springframework.security.providers.ldap.LdapAuthenticationProvider org.springframework.security.userdetails.ldap.LdapUserDetailsMapper org.springframework.security.providers.ldap.authenticator.BindAuthenticator` |
| Subset of Spring related to LDAP | `org.springframework.ldap` |
| CAS | `org.jasig.cas` |
| JasperReports Server external authentication API | `com.jaspersoft.jasperserver.multipleTenancy.security.externalAuth` |
| Subset of external authentication API related to single tenancy | `com.jaspersoft.jasperserver.api.security.externalAuth` |
| Subset of external authentication API related to token-based authentication | `com.jaspersoft.jasperserver.api.security.externalAuth.preauth` |
| Subset of external authentication API related to external database authentication | `com.jaspersoft.jasperserver.api.security.externalAuth` |
| External authentication specific logs | `com.jaspersoft.jasperserver.multipleTenancy.security.externalAuth` |
| Additional processor and synchronization specific logs | `com.jaspersoft.jasperserver.api.security.externalAuth` |
| Spring security OAuth2 client logs | `org.springframework.security.oauth2.client` |
| Spring security authentication logs | `org.springframework.security.authentication` |

Useful Logger Classnames for External Authentication

!!! note

    Enabling a logger and a sublogger together creates duplicate entries in the logs. For example, `org.springframework.security` and `org.springframework.security.ldap` creates duplicate entries.
