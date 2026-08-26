---
title: Configuring casServiceProperties
description: "The casServiceProperties bean implements the Spring JSCASServiceProperties bean and stores the properties related to Spring’s CAS: service and sendRenew properties. Configure the following bean to..."
---

# Configuring casServiceProperties

The `casServiceProperties` bean implements the Spring `JSCASServiceProperties` bean and stores the properties related to Spring’s CAS: service and sendRenew properties. Configure the following bean to set up the security check locations:

-   `casServiceProperties` – This bean has the following properties:

    -   `service` property – Configure this property with the JasperReports Server URL that receives and processes tickets for HTTP connections. Make sure to include the `j_spring_security_check` pattern at the end of the URL; this pattern activates user authentication (service ticket validation) in the Spring Security filter chain.
    -   `sendRenew`: When the user is redirected to CAS for authentication, the `sendRenew` property (`true|false`) determines whether or not to disregard TGT (default).

For example, to enable the security check on your localhost, you would set the pattern as in this example:

``` xml
<bean id="casServiceProperties" class="com.jaspersoft.jasperserver.api.security.
      externalAuth.wrappers.spring.cas.JSCASServiceProperties">
  <property name="service" value="http://localhost:8080/jasperserver-pro/        j_spring_security_check"/>
  <property name="sendRenew" value="false"/>
</bean>
```
