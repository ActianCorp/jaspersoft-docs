---
title: Configuring OAuth
description: The following sections describe how to configure JasperReports Server to use an OAuth provider.
---

# Configuring OAuth

The following sections describe how to configure JasperReports Server to use an OAuth provider.

## Configuring JasperReports Server to use OAuth

On the JasperReports Server instance, locate the following file:

*../WEB-INF/classes/oauth-clientconfig.properties file*, then edit the following variables:

- *spring.security.oauth2.user.attributes.mapping.roles=*
- *spring.security.oauth2.external.user.organizationRoleMap=*

The variable *spring.security.oauth2.user.attributes.mapping.roles=* requires the value to be used in your OAuth environment.

For example:

spring.security.oauth2.user.attributes.mapping.roles=roles_new

The variable *spring.security.oauth2.external.user.organizationRoleMap=* defines the roles that you want to add to the user.

For example:

spring.security.oauth2.external.user.organizationRoleMap={\\

\\jrs_admin\\: \\ROLE_ADMINISTRATOR\\,\\

\\jrs_user\\: \\ROLE_USER\\,\\

\\ext_role\\: \\ROLE_SUBORG_CHG\|\*\\\\

}

Then, save your changes to the file.

## Mapping JWT to User Details in JasperReports Server

To map a JSON web token (JWT) to a user's details in JasperReports Server, use the following variables in the **oauth-clientconfig.properties** file:

- *spring.security.oauth2.user.attributes.mapping.name=preferred_username*
- *spring.security.oauth2.user.attributes.mapping.display-name=name*
- *spring.security.oauth2.user.attributes.mapping.email=email*

These variables are mapped to the OAuth parameters: *username*, *name*, and *email*

(Role variables are mentioned in the previous section.)

## Mapping Internal Roles to External Roles or Groups

As mentioned in the previous section, the variable *spring.security.oauth2.user.attributes.mapping.roles=* can be used for roles, but it can also be used for groups.

For example:

spring.security.oauth2.user.attributes.mapping.roles=groups4roles

You can define an attribute for groups, and then assign role attributes to the group.

You can then use the variable *spring.security.oauth2.external.user.organizationRoleMap=* to define which internal roles go with the external groups.

For example:

spring.security.oauth2.external.user.organizationRoleMap={\\

\\EXT_JRS_ADMINS\\: \\ROLE_ADMINISTRATOR\\,\\

\\EXT_JRS_USERS\\: \\ROLE_USER\\,\\

\\ext_role\\: \\ROLE_SUBORG_CHG\|\*\\\\

}

## How to Enable OAuth in JasperReports Server

To enable OAuth in JasperReports Server, edit the *web.xml* file.

In the section:

\<context-param\>

\<param-name\>spring.profiles.active\</param-name\>

\<param-value\>default,engine,jrs\</param-value\>

\</context-param\>

Add *,oauth* after JRS.

For example:

\<param-value\>default,engine,jrs,oauth\</param-value\>

## Spring Security Values

The following list describes additional variables found in the oauth-clientconfig.properties file:

- spring.security.oauth2.client.registration.oidc.client-id=
- spring.security.oauth2.client.registration.oidc.client-secret=
- spring.security.oauth2.client.registration.oidc.redirect-uri=http://\<jrs-installation-instance\>:8080/jasperserver-pro/oauth
- authorization-uri identifies the authentication
- spring.security.oauth2.client.registration.oidc.authorization-uri=https://dev-12345678.okta.com/oauth2/default/v1/authorize
- spring.security.oauth2.client.provider.oidc.token-uri=https://dev-12345678.okta.com/oauth2/default/v1/token
- spring.security.oauth2.client.provider.oidc.jwk-uri=https://dev-12345678.okta.com/oauth2/default/v1/keys
- spring.security.oauth2.client.provider.oidc.issuer-uri=https://dev-12345678.okta.com/oauth2/default
- spring.security.oauth2.jrs.entrypoint=http://infra-platforms-na2-12345-johndoe.jaspersoft.com:8080/jasperserver-pro/oauth2/authorization/oidc
- spring.security.oauth2.jrs.logouturl=https://dev-12345678.okta.com/oauth2/default/v1/logout?id_token_hint=##ID_TOKEN##&post_logout_redirect_uri=http%3A%2F%2F\<jrs-installation-instance\>%3A8080%2Fjasperserver-pro%2F

For more information on these property mappings, refer to the [Spring Boot 2.x Property Mappings](https://docs.spring.io/spring-security/site/docs/5.2.12.RELEASE/reference/html/oauth2.html) page of Spring's Security Reference documentation site.
