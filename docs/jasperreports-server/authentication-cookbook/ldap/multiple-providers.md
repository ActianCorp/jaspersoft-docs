---
title: Setting Up Multiple Providers
description: "The file sample-applicationContext-externalAuth-LDAP-mt.xml contains an LDAP-specific authentication manager, ldapAuthenticationManager, configured as follows."
---

# Setting Up Multiple Providers

The file sample-applicationContext-externalAuth-LDAP\[-mt\].xml contains an LDAP-specific authentication manager, `ldapAuthenticationManager`, configured as follows.

```
<bean id="ldapAuthenticationManager" class="com.jaspersoft.jasperserver.api.security.
      externalAuth.wrappers.spring.JSProviderManager">
  <constructor-arg index="0">
    <list>
      <ref bean="ldapAuthenticationProvider"/>
      <ref bean="${bean.daoAuthenticationProvider}"/>
    </list>
  <constructor-arg>
</bean>
```

The `ldapAuthenticationManager` bean attempts to authenticate a user session with each provider in the list in the order they appear. When one of the providers successfully authenticates the user, the rest of the providers are skipped.

As shown in the example above, you can list other authentication providers with LDAP.

The `daoAuthenticationProvider` is the default internal authentication using the internal database. You may keep this provider in the list to access the `jasperadmin` and `superuser` accounts, or any other administrator accounts you've created. Or, if you have configured system role mapping as described in [Mapping Roles to System Roles](ldap-mapping-system-roles.md), you can remove the `daoAuthenticationProvider` from the list.

!!! note

    The internal database contains accounts for all of the external users that have previously logged into the server. However, these external accounts do not contain passwords and cannot be used for authentication with the default internal authentication, for example when the LDAP server is unavailable.
