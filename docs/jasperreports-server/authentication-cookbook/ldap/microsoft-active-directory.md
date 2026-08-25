---
title: Authentication with Microsoft Active Directory
description: "Microsoft Active Directory can be used to authenticate users through the ldapAuthenticationProvider provided by Spring Security. When setting up an LDAP provider for Active Directory, you should be..."
---

# Authentication with Microsoft Active Directory

Microsoft Active Directory can be used to authenticate users through the `ldapAuthenticationProvider` provided by Spring Security. When setting up an LDAP provider for Active Directory, you should be aware of the following:

- You must use configure user search to work with the `sAMAccountName` attribute containing the user’s login name. See Configuring User Search for Active Directory for more information.
- You may need to set the Spring `referral` property in `LdapContextSource` to `follow`. See Configuring the Spring Referral Property for more information.

In addition, the structure of an Active Directory instance can become quite complex and this can be a challenge when setting up user search.

## Configuring User Search for Active Directory

The most important difference in configuration between Active Directory and a standard LDAP server is the need to search for the `sAMAccountName` attribute containing the user’s login name. Because of this requirement, you must use the `JSBindAuthenticator` bean, along with the `userSearch` bean and corresponding property in `JSBindAuthenticator`.

The following example shows how to configure the `userSearch` bean for LDAP authentication with the special syntax for Active Directory. This configuration is only an example; you need to configure the `JSBindAuthenticator` and `ldapContextSource` beans correctly for your LDAP server, as described earlier in this chapter.

The following example shows how you might set the `sAMAccountName` attribute.

``` xml
<bean id="userSearch"  class="com.jaspersoft.jasperserver.api.security.externalAuth.wrappers.
       spring.ldap.JSFilterBasedLdapUserSearch">
  <constructor-arg index="0"><value>cn=Users</value></constructor-arg>
  <constructor-arg index="1"><value>(&amp;(sAMAccountName={0}))</value></constructor-arg>
  <constructor-arg index="2"><ref bean="ldapContextSource"/></constructor-arg>
  <property name="searchSubtree"><value>true</value></property>
</bean>
```

You must also include a role mapping for any roles you want to import to JasperReports Server, and you must include an organization mapping if you implement multiple organizations. For more information, see [Mapping the User Roles](ldap-user-role-mapping.md).

Note that for Active Directory, `sAMAccountName` must be in `constructor-arg index="1"` of the `userSearch` bean.

## Configuring the Spring Referral Property

Some Active Directory servers are unable to automatically follow referrals, which leads to a `PartialResultException` being thrown in searches. To handle this, set the Spring `referral` property in `LdapContextSource` to follow, for example:

``` xml
<bean id="ldapContextSource"
        class="com.jaspersoft.jasperserver.api.security.externalAuth.ldap.JSLdapContextSource">
  <constructor-arg value="ldap://hostname:389/dc=example, dc=com" />
  <property name="userDn">
    <value>cn=Administrator, dc=example, dc=com</value>
  </property>
  <property name="password"><value>password</value></property>
  <property name="referral" value="follow"/>
</bean>
```
