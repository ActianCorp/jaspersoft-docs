---
title: Encrypting Passwords in Configuration Files
description: "In JasperReports Server version 5.5 or later, administrators can obfuscate passwords that appear in the configuration files. This satisfies security audit requirement and prevents the passwords from..."
---

# Encrypting Passwords in Configuration Files

In JasperReports Server version 5.5 or later, administrators can obfuscate passwords that appear in the configuration files. This satisfies security audit requirement and prevents the passwords from being seen by unauthorized individuals. Typically, the following are encrypted:

- The password to JasperReports Server's internal database (`jasperserver`).
- The passwords to the sample databases (`foodmart` and `sugarcrm`).
- On Tomcat, passwords in JNDI resource definitions.

You can change the configuration to encrypt:

- The password for the mail server used by the scheduler (`quartz.mail.sender.password`).
- The password for LDAP external authentication.

Passwords in configuration files are encrypted during JasperReports Server installation. If the installation deploys to the Tomcat application server, the database password is also automatically encrypted in the JNDI configuration (in the file `context.xml`).

!!! warning

    Full password security cannot be guaranteed from within JasperReports Server. A user with sufficient privileges and knowledge of JasperReports Server can gain access to the encryption keys and the configuration passwords. While you could require a password on every server restart, this is impractical for most users. The only practical way to guarantee password security is through backup and restriction of access to the keystore property file.

## Encrypting Configuration Passwords on Tomcat

To encrypt passwords in a Tomcat installation, modify the installation procedure:

1.  Depending on the database you use, copy the installation configuration file as usual:

    from: `<js-install>/buildomatic/sample_conf/<database>_master.properties`to: `<js-install>/buildomatic/default_master.properties`

2.  Edit the `default_master.properties` file:

    - Enter values specific to your installation.
    - Enter your passwords in plain text.
    - Turn on configuration file encryption by uncommenting the `encrypt=true` property. You don't have to uncomment any other encryption properties because they all have the default values shown.
    - Unless you are using Oracle, uncomment `propsToEncrypt` and set it to `dbPassword,sysPassword`.
    - Optionally, specify additional properties to encrypt as described in Encrypting Additional Properties in default_master.properties.
    - Optionally, change the settings for configuration file encryption as described in Encryption Options.

3.  Run the buildomatic installation script (js-install) and all other installation steps according to the JasperReports® Server Installation Guide. This has the following effects:

    1.  The plain text passwords in default_master.properties are overwritten with their encrypted equivalents. There is no warning when you run js-install with `encrypt=true`.
    2.  The encrypted passwords are propagated to all configuration files.
    3.  The installation proceeds and copies the files to their final locations.

4.  After installation, passwords are encrypted in the following locations:

- In all server configuration files in `.../WEB-INF/applicationContext*.xml`.
- In JNDI definitions in `.../META-INF/context.xml`.
- In the `default_master.properties` files that remain after installation.

!!! note

    If you get an error like the following when restarting the server:

    `javax.naming.NamingException: KeystoreManager.init was never called or there are errors instantiating an instance`

    You may need to add the following to your Tomcat service start properties:

    `-Duser.home=c:\Users\<TomcatUser>`

## Encrypting Configuration Passwords on Enterprise Servers

Most enterprise servers, like JBoss, Glassfish, WebSphere, and WebLogic, have proprietary ways to set up password encryption. You should use these encryption methods. JasperReports Server doesn't automatically set up encrypted passwords for these servers during deployment. In this case, you can encrypt the passwords in the buildomatic file after deployment:

1.  Deploy JasperReports Server to your enterprise server as specified in the JasperReports Server Installation Guide. The resulting JasperReports Server instance will have unencrypted JNDI data source passwords. If you want to encrypt these passwords, refer to your application server's documentation.

2.  After the server has been successfully configured, encrypt the JasperReports Server configuration files as follows:

    1.  In `default_master.properties`, turn on encryption by uncommenting `encrypt=true`.
    2.  Run the target `js-ant refresh-config`. This will remove and recreate all the configuration files without deploying them to the application server. Now the buildomatic files will have the database passwords encrypted. You should still be able to execute import/export or other scripts.

3.  After running `js-ant refresh-config`, you will need to manually copy the encrypted password to the application server configuration file. Copy the encrypted password from the updated `default_master.properties` file to the corresponding database connection files on the server, such as the `/META-INF/context.xml` file for Tomcat.

!!! warning

    Do not run `js-install` or `js-ant deploy-webapp-pro`. These commands overwrite the WAR file created in step 1 and render the server data sources inaccessible. If you need to redeploy the WAR file, reset the database passwords to plain text in your `default_master.properties` file and start again with step 1.

## Encrypting Additional Properties in default_master.properties

You can encrypt additional properties in the `default_master.properties` file. To work correctly, these properties need to be decrypted when used. Currently decryption is supported for properties loaded into the Spring application context via the `propertyConfigurer` bean in `applicationContext-webapp.xml`.

!!! note

    If a property is defined via JNDI, we recommend pointing there instead of encrypting:

    ``` xml
    <property name="password">
        <jee:jndi-lookup jndi-name="java:comp/env/emailPassword" />
    </property>
    ```

The following code sample shows the `propertyConfigurer` bean in `applicationContext-webapp.xml`:

``` xml
<bean id="propertyConfigurer" class="com.jaspersoft.jasperserver.api.common.properties.DecryptingPropertyPlaceholderConfigurer">
    <property name="locations">
      <list>
        <value>/WEB-INF/classes/hibernate.properties</value>
        <value>/WEB-INF/js.quartz.properties</value>
        <value>/WEB-INF/js.spring.properties</value>
        <value>/WEB-INF/js.scheduling.properties</value>
        <value>/WEB-INF/mondrian.connect.string.properties</value>
        <value>/WEB-INF/js.diagnostic.properties</value>
        <value>/WEB-INF/js.aws.datasource.properties</value>
        <value>/WEB-INF/js.config.properties</value>
        <value>/WEB-INF/js.externalAuth.properties</value>
      </list>
    </property>
    ...
</bean>
</pre>
```

Because we extended Spring's `PropertyPlaceholderConfigurer` class as `DecryptingPropertyPlaceholderConfigurer`, all the loaded properties are scanned for the special marker `ENC-<value>-`. If that marker is found around the property value, that property is decrypted before it is loaded into the Spring context.To determine if your property is scanned by `propertyConfigurer`, search the files in `propertyConfigurer`'s location to see if it is defined in one of these files. For example, suppose you want to encrypt the `password` property of the `reportSchedulerMailSender` bean in `applicationContext-report-scheduling.xml`:

``` xml
<bean id="reportSchedulerMailSender" class="org.springframework.mail.javamail.JavaMailSenderImpl">
  <property name="host" value="${report.scheduler.mail.sender.host}"/>
  <property name="username" value="${report.scheduler.mail.sender.username}"/>
  <property name="password" value="${report.scheduler.mail.sender.password}"/>
  <property name="protocol" value="${report.scheduler.mail.sender.protocol}"/>
  <property name="port" value="${report.scheduler.mail.sender.port}"/>
  <property name="javaMailProperties">
    <props>
      <prop key="mail.smtp.auth">false</prop>
    </props>
  </property>
</bean>
```

The use of the `${...}` syntax tells you that `report.scheduler.mail.sender.password` is most likely defined via the `propertyConfigurer` bean. Search through the `propertyConfigurer` locations to verify. This property is defined in `/WEB-INF/js.quartz.properties` as follows: `report.scheduler.mail.sender.password=${quartz.mail.sender.password}`. Once you've verified that the `quartz.mail.sender.password` property can be encrypted using `default-master.properties`, you set up encryption before installation as follows:

1.  Set the password for `quartz.mail.sender.password` in `default-master.properties`:

    ``` properties
    quartz.mail.sender.password=cleartextpassword
    ```

2.  Uncomment the `encrypt=true` property in the same file.

3.  Uncomment `propsToEncrypt=dbPassword` in `default-master.properties`.

4.  Add `quartz.mail.sender.password` to `propsToEncrypt`:

    ``` properties
    quartz.mail.sender.password=cleartextpassword
    ...
    encrypt=true
    propsToEncrypt=dbPassword,quartz.mail.sender.password
    ```

5.  Configure and install your JasperReports® Server WAR installation as described in the JasperReports Server Installation Guide.

6.  Verify that `report.scheduler.mail.sender.password` was encrypted in both `default-master.properties` and in `/WEB-INF/js.quartz.properties`.

## Password Encryption for External Authentication

As of JasperReports Server 5.6, you can encrypt the passwords in the external authentication configuration files for LDAP and external database authentication. Here we cover only the encryption of these passwords; for details about configuring external authentication, see the JasperReports Server External Authentication Cookbook. To enable encryption during installation, property values in the external authentication sample configuration are referenced from other configuration files. For example, if you're using LDAP to authenticate, the sample configuration file contains the following reference to the LDAP password:

``` xml
<bean id="ldapContextSource"
    class="com.jaspersoft.jasperserver.api.security.externalAuth.ldap.JSLdapContextSource">
  <constructor-arg value="${external.ldap.url}" />
  <property name="userDn" value="${external.ldap.username}" />
  <property name="password" value="${external.ldap.password}"/>
</bean>
```

The values referenced by the `${...}` format are defined in the `js.externalAuth.properties` file and imported into the Spring context via the `propertyConfigurer`. For example, the LDAP properties are defined in `js.externalAuth.properties` as follows:

``` properties
external.ldap.url=${external.ldapUrl}
external.ldap.username=${external.ldapDn}
external.ldap.password=${external.ldapPassword}
```

The `${...}` syntax again references other configuration properties that must be set in `default_master.properties` before installation or upgrade. The following example shows the syntax of the properties in the `default_master.properties` file:

``` properties
external.ldapUrl=ldap://hostname:389/dc=example,dc=com
external.ldapDn=cn=Administrator,dc=example,dc=com
external.ldapPassword=password
```

To encrypt the password property, set the following values in `default_master.properties` before installation or upgrade:

``` properties
external.ldapPassword=cleartextpassword
...
encrypt=true
propsToEncrypt=dbPassword, external.ldapPassword
```

During the installation process, the password value in `default_master.properties` and its reference in `js.externalAuth.properties` are overwritten with the encrypted value. If your external authentication is configured to create organizations for external users, and you're using JasperReports Server 6.0, or later, there is another password to encrypt. When external authentication creates an organization, it uses the information in `ExternalTenantSetupUser` of the `externalTenantSetupProcessor` bean to create the organization administrator.

``` xml
<bean class="com.jaspersoft.jasperserver.multipleTenancy.security.externalAuth.processors.
             MTAbstractExternalProcessor.ExternalTenantSetupUser">
  <property name="username" value="${new.tenant.user.name.1}"/>
  <property name="fullName" value="${new.tenant.user.fullname.1}"/>
  <property name="password" value="${new.tenant.user.password.1}"/>
  <property name="emailAddress" value="${new.tenant.user.email.1}"/>
  <property name="roleSet">
    <set>
      <value>ROLE_ADMINISTRATOR</value>
      <value>ROLE_USER</value>
    </set>
  </property>
</bean>
```

The values referenced by the `${...}` format are defined in the `js.config.properties` file as follows:

``` bash
## New tenant creation: user config
new.tenant.user.name.1=jasperadmin
new.tenant.user.fullname.1=jasperadmin
...
new.tenant.user.password.1=jasperadmin
new.tenant.user.email.1=
```

!!! note

    The default values for new tenant (organization) administrators in `js.config.properties` apply *only* to external authentication. They do not apply to organizations created by administrators through the UI or REST interface.

To encrypt this password, modify the `js.config.properties` file as follows:

``` properties
new.tenant.user.password.1=${tenant.user.password}
```

Then add the following lines to `default_master.properties` before installation or upgrade:

``` properties
tenant.user.password=cleartextpassword
...
encrypt=true
propsToEncrypt=dbPassword, external.ldapPassword, tenant.user.password
```

During the installation process, the password value in `default_master.properties` and its reference in `js.config.properties` are overwritten with the encrypted value.

## Encryption Options

!!! warning

    As of JasperReports Server 7.5, all encryption in the server relies on cryptoghaphic keys stored in the server's keystore. For more information, see [Key and Keystore Management](../keymanagement/keystore_intro.md).The configuration files and properties described in this section are no longer used by this feature. They are documented here only for legacy purposes.

In buildomatic installation scripts, the passwords are symmetrically encrypted: the same secret key is used for both encryption and decryption. The key and its containing keystore file are randomly generated on each machine during the first JasperReports® Server installation. All subsequent JasperReports® Server installations on the same server rely on the same keystore; they do not regenerate the key. The keystore is an encrypted file used to securely store secret keys. JasperReports® Server uses keystore properties to access the keystore. Both the keystore and keystore properties files are created by default in the user home directory. Alternatively, before running js-install, you can specify different locations for the keystore and keystore properties files via the environmental variables ks and ksp. By default, database passwords are encrypted with the AES-128 algorithm in Cipher Block Chaining mode with PKCS5 padding. The AES algorithm is the current industry encryption standard. You can choose to modify the encryption strength by choosing either a different algorithm, a longer secret key size (for example AES-256), or a different encryption mode. Edit the following properties in your `default_master.properties` and set these options. If a property is commented out, the default is used:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th>Property</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>build.key.algo</code></td>
<td>The algorithm is used to encrypt the properties in configuration files.</td>
<td>AES</td>
</tr>
<tr>
<td><code>build.key.size</code></td>
<td><p>Size of the encryption key as in AES-128.To increase the key size, if it has not been done before, you might have to install "Unlimited Strength Jurisdiction Policy Files" from the Oracle site for your Java version. To install the files, download<code> US_export_policy.jar</code> and <code>local_policy.jar</code>. AFTER backing up the old files, extract the jars into <code>%JAVA_HOME%/jre/lib/security</code> directory. Alternatively, you may download one of the reputable providers such as Bouncy Castle (ships with JasperReports® Server). You would need to add the Bouncy Castle provider to the list in<br />
<code>%JAVA_HOME%/jre/lib/security/java.security file: security.provider.&lt;seq number&gt;=</code><br />
<code>org.bouncycastle.jce.provider.BouncyCastleProvider</code></p></td>
<td>128 (bits)</td>
</tr>
<tr>
<td><code>enc.transformation</code></td>
<td>So-called encryption mode. See Java's <code>javax.crypto</code> documentation to understand the modes and padding better.</td>
<td>AES/CBC<br />
/PKCS5<br />
Padding</td>
</tr>
<tr>
<td><code>enc.block.size</code></td>
<td>The size of the block that is encrypted. Encrypted text can contain many blocks. Usually the block is changed together with the encryption algorithm.</td>
<td>16 (bytes)</td>
</tr>
<tr>
<td><code>propsToEncrypt</code></td>
<td>A comma separated list of the properties to encrypt.</td>
<td>dbPassword</td>
</tr>
</tbody>
</table>
