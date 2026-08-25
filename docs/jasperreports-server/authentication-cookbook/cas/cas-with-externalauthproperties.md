---
title: Configuring externalAuthProperties
description: "The externalAuthProperties bean stores properties specific to Jaspersoft’s external authentication API. For CAS authentication, configure the externalAuthProperties bean to specify the following URLs..."
---

# Configuring externalAuthProperties

The `externalAuthProperties` bean stores properties specific to Jaspersoft’s external authentication API. For CAS authentication, configure the `externalAuthProperties` bean to specify the following URLs for communication with the CAS server:

- `ssoServerLocation` property — Specifies the HTTPS URL where tickets are validated on the CAS server.
- `externalLoginUrl` property — Specifies the login URL for external users. Can be set relative to `ssoServerLocation`.
- `logoutUrl` property — Specifies the logout URL for external users. Can be set relative to `ssoServerLocation`.

The following example shows how you might set these beans:

``` xml
<bean id="externalAuthProperties" class="com.jaspersoft.jasperserver.api.security.
      externalAuth.ExternalAuthProperties">
  <property name="externalLoginUrl" value="#ssoServerLocation#/login"/>
  <property name="logoutUrl" value="#ssoServerLocation#/logout"/>
  <property name="ssoServerLocation" value="https://casserver:8443/cas"/>
</bean>
```
