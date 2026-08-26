---
title: Encrypting User Session Login
description: "As of JasperReports Server 7.5, encryption of HTTP parameters is deprecated and this feature may be removed in future versions. Jaspersoft recommends using TLS (Transport Layer Security) in your app..."
---

# Encrypting User Session Login

!!! warning

    As of JasperReports Server 7.5, encryption of HTTP parameters is deprecated and this feature may be removed in future versions. Jaspersoft recommends using TLS (Transport Layer Security) in your app server to enable HTTPS when accessing your server.

By default, JasperReports Server does *not* enable the Secure Socket Layer/Transport Layer Security (SSL/TLS) to encrypt all data between the browser and the server, also known as HTTPS. Enabling HTTPS requires a certificate and a careful configuration of your servers. We recommend implementing HTTPS but recognize that it is not always feasible. See [Enabling SSL in Tomcat](../application-security/using-ssl-in-web-server.md)

Without HTTPS, all data sent by the user, including passwords, appear unencrypted in the network traffic. Because passwords should never be visible, JasperReports Server provides an independent method for encrypting the password values without using HTTPS. Passwords are encrypted in the following cases:

-   Passwords sent from the login page.
-   Passwords sent from the change password dialog. See [Configuring User Password Options](configuring_user_password_options.md).
-   Passwords sent from the user management pages by an administrator.

When a browser requests one of these pages, the server generates a private-public key pair and sends the public key along with the page. A JavaScript in the requested page encrypts the password when the user posts it to the server. Meanwhile, the server saves its private key and uses it to decrypt the password when it arrives. After decrypting the password, the server continues with the usual authentication methods.

Login encryption is not compatible with password memory in the browser. Independent of the autocomplete setting described in [Configuring Password Memory](configuring_user_password_options.md), the JavaScript that implements login encryption clears the password field before submitting the page. As a result, most browsers will never prompt to remember the encrypted password.

The disadvantage of login encryption is the added processing and the added complexity of web services login. For backward compatibility, login encryption is disabled by default. To enable login encryption, set the following properties. After making any changes, redeploy the JasperReports Server webapp or restart the application server.

!!! warning

    When login encryption is enabled, web services and URL parameters must also send encrypted passwords. Your applications must first obtain the key from the server and then encrypt the password before sending it. See the JasperReports Server Web Services Guide.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>Login Encryption</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>.../WEB-INF/classes/esapi/security-config.properties</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Value</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>encryption.on</code></p></td>
<td><p><code>truefalse</code><br />
&lt;default&gt;</p></td>
<td><p>Turns login encryption on or off. Encryption is off by default. Any other value besides case-insensitive “false” is equivalent to true.</p></td>
</tr>
<tr>
<td><p><code>encryption.type</code></p></td>
<td><p><code>RSA</code> &lt;default&gt;</p></td>
<td><p>Encryption algorithm; currently, only RSA is supported.</p></td>
</tr>
<tr>
<td><p><code>encryption.key.length</code></p></td>
<td><p>integer power of 2<br />
<code>1024</code> &lt;default&gt;</p></td>
<td><p>The length of the generated encryption keys. This affects the strength of encryption and the length of the encrypted string.</p></td>
</tr>
<tr>
<td><p><code>encryption.dynamic.key</code></p></td>
<td><p><code>true</code> &lt;default&gt;<br />
<code>false</code></p></td>
<td><p>When true, a key will be generated per every single request. When false, the key will be generated once per application installation. See descriptions in <span>Dynamic Key Encryption</span> and <span>Static Key Encryption</span> below.</p></td>
</tr>
</tbody>
</table>

Encryption has two modes, dynamic and static, as determined by the `encryption.dynamic.key` parameter. These modes provide different levels of security and are further described in the following sections.

## Dynamic Key Encryption

The advantage of encrypting the password at login is to prevent it from being seen, but also to prevent it from being used. For password encryption to achieve this, the password must be encrypted differently every time it's sent. With dynamic key encryption, the server uses a new public-private key pair with every login request.

Every time someone logs in, the server generates a new key pair and sends the new public key to the JavaScript on the page that sends the password. This ensures that the encrypted password is different every time it's sent, and a potential attacker won't be able to steal the encrypted password to log in or send a different request.

Because it's more secure, dynamic key encryption is the default setting when encryption is enabled. The disadvantage is that it slows down each login, though users may not always notice. Another effect of dynamic key encryption is that it doesn't allow remembering passwords in the browser. While this may seem inconvenient, it's more secure to not store passwords in the browser. See [Configuring Password Memory](configuring_user_password_options.md).

## Static Key Encryption

!!! warning

    As of JasperReports Server 7.5, all encryption in the server relies on cryptoghaphic keys stored in the server's keystore. For more information, see [Key and Keystore Management](../keymanagement/keystore_intro.md).

    The configuration files and properties described in this section are no longer used by this feature. They are documented here only for legacy purposes.

JasperReports Server also supports static key encryption. For every login, the server expects the client to encode parameters such as passwords with the `httpParameterEncSecret` key in the keystore. Because the key is always the same, the encrypted value of a user’s password is always the same. This means an attacker could steal the encrypted password and use it to access the server.

Static key encryption is very insecure and is recommended only for intranet server installation where the network traffic is more protected. The only advantage of static encryption over no encryption at all is that passwords can't be deciphered and used to attack other systems where users might have the same password.

Before setting `encryption.dynamic.key=false` to use static encryption, you must also configure the secure file called keystore where the key pair is kept. Be sure to customize the keystore parameters listed in the following table to make your keystore file unique and secure.

!!! warning

    For security reasons, always change the default keystore passwords immediately after installing the server.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>DEPRECATED Keystore Configuration (when encryption.dynamic.key=false)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>.../WEB-INF/classes/esapi/security-config.properties</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Value</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>keystore.location</code></p></td>
<td><p><code>keystore.jks</code></p>
<p>&lt;default&gt;</p></td>
<td><p>Path and filename of the keystore file. This parameter is either an absolute path or a file in the webapp classpath, for example &lt;tomcat&gt;/webapps/jasperserver-pro/WEB-INF/classes&gt;. By default, the <code>keystore.jks</code> file is shipped with the server and doesn’t contains any keys.</p></td>
</tr>
<tr>
<td><p><code>keystore.password</code></p></td>
<td><p><code>jasper123</code> &lt;default&gt;</p></td>
<td><p>Password for the whole keystore file. This password is used to verify keystore's integrity.</p></td>
</tr>
<tr>
<td><p><code>keystore.key.alias</code></p></td>
<td><p><code>jasper</code> &lt;default&gt;</p></td>
<td><p>Name by which the single key is retrieved from keystore. If a new alias is specified and does not correspond to an existing key, a new key will be generated and inserted into the keystore.</p></td>
</tr>
<tr>
<td><p><code>keystore.key.password</code></p></td>
<td><p><code>jasper321</code> &lt;default&gt;</p></td>
<td><p>Password for the key whose alias is specified by <code>keystore.key.alias</code>.</p></td>
</tr>
</tbody>
</table>

When you change the key alias, the old key will not be deleted. You can use it again by resetting the key alias. Also, once the key has been created with a password, you can't change the password through the keystore configuration. To delete keys or change a keystore password, the server administrator must use the Java `keytool` utility in the bin directory of the JDK. If you change the keystore password or the key password, the keystore configuration above must reflect the new values or login will fail for all users.
