---
title: External Authentication Framework
description: JasperReports Server uses an external authentication bean framework to make it easier to configure the security system for external authentication. Although each external authentication situation is...
---

# External Authentication Framework

JasperReports Server uses an external authentication bean framework to make it easier to configure the security system for external authentication. Although each external authentication situation is different, we've extracted the common principals and extended the set of Spring Security beans to help you configure your own external authentication.

Jaspersoft has implemented a proxy bean for each filter chain, for example, `delegatingAuthenticationRestProcessingFilter`, that serves as a proxy for the standard Spring `authenticationProcessingFilter` and initiates external authentication for the pattern. These proxy beans inspect the application context for external authentication beans, and use them if they are present. Otherwise, the default internal authentication beans are used.

The following sample files use JasperReports Server’s external authentication APIs to integrate with custom SSO servers following a CAS-like protocol:

-   sample-applicationContext-externalAuth-sso.xml: Sample file for integrating CAS with a single-organization JasperReports Server. Included with the community edition of JasperReports Server only.
-   sample-applicationContext-externalAuth-sso-mt.xml: Sample file for integrating CAS with a multiple-organization JasperReports Server. In this example, user details like external roles and organization are retrieved from an external database. Included with the commercial version of JasperReports Server only.
