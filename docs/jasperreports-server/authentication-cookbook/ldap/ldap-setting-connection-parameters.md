---
title: Setting the LDAP Connection Parameters
description: "You can configure your connection to the LDAP server in one of two ways:"
---

# Setting the LDAP Connection Parameters

You can configure your connection to the LDAP server in one of two ways:

- Configure the connection by LDAP properties in the default_master properties file before installation or upgrade. You can choose to encrypt any of the LDAP connection parameters. This is the preferred method for setting the LDAP connection parameters.
- For an existing JasperReports Server, you can configure the connection properties directly in your sample-applicationContext-externalAuth-LDAP\[-mt\].xml file. In this case, the properties, including the password, cannot be encrypted.

## Setting LDAP Connection Parameters in default_master.properties

The preferred approach is to configure the `external.ldapUrl`, `external.ldapDn`, and `external.ldapPassword` properties in the `default_master.properties` file before installation or upgrade. The default configuration of the `ldapContextSource` bean in `sample-applicationContext-externalAuth-LDAP[-mt].xml` uses context properties for the LDAP connection properties:

```
<bean id="ldapContextSource"
    class="com.jaspersoft.jasperserver.api.security.externalAuth.ldap.JSLdapContextSource">
  <constructor-arg value="${external.ldap.url}" />
  <property name="userDn" value="${external.ldap.username}" />
  <property name="password" value="${external.ldap.password}"/>
</bean>
```

To configure these properties using default_master.properties, follow these steps:

1.  Open default_master.properties in a text editor.
2.  Locate the following properties and set them for your LDAP server as follows:

- `external.ldapUrl` property: The URL of your LDAP server, including the base DN.
- `external.ldapDn` property: The distinguished name (DN) of your LDAP administrator.
- `external.ldapPassword` property: The password of your LDAP administrator.

3.  You can choose to encrypt any of the LDAP connection parameters.

The following example shows the syntax of the properties in the default_master.properties file:

```
external.ldapUrl=ldap://hostname:389/dc=example,dc=com
external.ldapDn=cn=Administrator,dc=example,dc=com
external.ldapPassword=password
```

To encrypt the password property, also set the following:

```
encrypt=true
propsToEncrypt=dbPassword,external.ldapPassword
```

See the JasperReports Server Security Guide for more information on encrypting passwords using buildomatic.

## Setting LDAP Connection Parameters Manually

To set the connection parameters for the LDAP server directly in the application context file, configure the `ldapContextSource` helper bean as follows:

!!! note

    If you configured your LDAP connection during JasperReports Server installation or upgrade, do not set the parameters using `ldapContextSource`. You can verify whether the parameters are set by looking at the `default_master.properties` file.

1.  In `sample-applicationContext-externalAuth-LDAP[-mt].xml`, locate the `ldapContextSource` bean.
2.  Specify the following information:

- `constructor-arg` value: The URL of your LDAP server, including the base DN.
- `userDn` property: The distinguished name (DN) of your LDAP administrator.
- `password` property: The password of your LDAP administrator.

!!! note

    If your LDAP server is configured to allow anonymous user lookup, you don't need to specify the `userDn` and `password` properties.

Here's an example shows the syntax of the bean’s constructor and properties when manually configured:

```
<bean id="ldapContextSource"
    class="com.jaspersoft.jasperserver.api.security.externalAuth.ldap.JSLdapContextSource">
  <constructor-arg value="ldap://hostname:389/dc=example,dc=com" />
  <property name="userDn"><value>cn=Administrator,dc=example,dc=com</value></property>
  <property name="password"><value>password</value></property>
</bean>
```
