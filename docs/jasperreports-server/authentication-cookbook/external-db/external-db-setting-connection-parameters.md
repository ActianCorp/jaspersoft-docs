---
title: Setting the Database Connection Parameters
description: "You can configure your connection to the database in one of two ways:"
---

# Setting the Database Connection Parameters

You can configure your connection to the database in one of two ways:

- Configure the connection during installation of JasperReports Server by configuring the `external.jdbcDriverClass`, `external.jdbcUrl`, `external.dbUsername`, and/or `external.dbPassword` properties before installation or upgrade. You can choose to encrypt any of the database connection parameters. This is the preferred method for setting the database connection parameters. See the JasperReports Server Security Guide for more information.
- If you have a JasperReports Server, you can configure the connection properties directly in your sample-applicationContext-externalAuth-db-mt.xml file. In this case, the properties, including the password, can't be encrypted.

## Setting Database Connection Parameters in default_master.properties

The preferred method for setting the database connection parameters is to configure the `external.jdbcDriverClass`, `external.jdbcUrl`, `external.dbUsername` and `dbPassword` properties in the default_master.properties file before installation or upgrade. In JasperReports Server 5.6 and later, the default configuration of the `externalDataSource` bean in sample-applicationContext-externalAuth-db-mt.xml uses context properties for the database connection properties:

```
<bean id="externalDataSource" class="com.jaspersoft.jasperserver.api.security.
    externalAuth.wrappers.spring.jdbc.JSDriverManagerDataSource">
  <property name="driverClassName" value="${external.jdbc.driverClassName}"/>
  <property name="url" value="${external.jdbc.url}"/>
  <property name="username" value="${external.jdbc.username}"/>
  <property name="password" value="${external.jdbc.password}"/>
</bean>
```

To configure these properties using default_master.properties, follow these steps:

1.  Open default_master.properties in a text editor.
2.  Locate and set the following properties for your LDAP server:

- `external.jdbcDriverClass` property: The name of the JDBC driver class for your database. Make sure the driver jar library is available on the classpath; for example, you can place the jar in the lib directory of your application server or in the \<js-webapp\>/lib directory.
- `external.jdbcUrl` property: The JDBC URL for your database server, including the hostname, port, and database you want to access.
- `external.dbUsername` property: The username of your database administrator.
- `external.dbPassword` property: The password of your database administrator.

3.  You can choose to encrypt any of the LDAP connection parameters.

The following example shows the syntax of the properties in the default_master.properties file:

```
external.jdbcDriverClass=com.mysql.jdbc.Driver
external.jdbcUrl=jdbc:mysql://127.0.0.1:3306/external_sso_test
external.dbUsername=username
external.dbPassword=password
```

To encrypt the password property, also set the following:

```
encrypt=true
propsToEncrypt=dbPassword,external.dbPassword
```

See the JasperReports Server Security Guide for more information on encrypting passwords using buildomatic.

## Setting Database Connection Parameters Manually

!!! note

    If you configured your database connection during JasperReports Server installation, don't set the parameters using `externalDataSource`. You can verify whether the parameters are set by looking at the `default_master.properties` file.

To set the connection parameters for the external database server directly in the application context file, configure the `externalDataSource` helper bean as follows:

1.  In sample-applicationContext-externalAuth-db-mt.xml, locate the `externalDataSource` bean.
2.  Specify the following information:

- `driverClassName` property: The name of the JDBC driver class for your database. Make sure the driver jar library is available on the classpath. For example, you can place the jar in the lib directory of your application server or in the \<js-webapp\>/lib directory.
- `url` property: The JDBC URL for your database server, including the hostname, port, and database you want to access.
- `username` property: The username of your database administrator.
- `password` property: The password of your database administrator.

The following is an example of the connection information for a MySQL database:

```
<bean id="externalDataSource" class="com.jaspersoft.jasperserver.api.security.
      externalAuth.wrappers.spring.jdbc.JSDriverManagerDataSource">
  <property name="driverClassName" value="com.mysql.jdbc.Driver"/>
  <property name="url" value="jdbc:mysql://127.0.0.1:3306/external_sso_test"/>
  <property name="username" value="username"/>
  <property name="password" value="password"/>
</bean>
```
