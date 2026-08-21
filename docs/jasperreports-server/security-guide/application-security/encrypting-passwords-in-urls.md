---
title: Encrypting Passwords in URLs
description: "As of JasperReports Server 7.5, encryption of HTTP parameters is deprecated and this feature may be removed in future versions. Jaspersoft recommends using TLS (Transport Layer Security) in your app..."
---

# Encrypting Passwords in URLs

!!! warning

    As of JasperReports Server 7.5, encryption of HTTP parameters is deprecated and this feature may be removed in future versions. Jaspersoft recommends using TLS (Transport Layer Security) in your app server to enable HTTPS when accessing your server.

One advantage of JasperReports Server is the ability to share reports with other users. You can easily share the URL to access a report, even with people who do not have a username. To embed the web app, it is often necessary to include a link to a page without logging in, for example:

http://example.com:8080/jasperserver/flow.html?\_flowId=homeFlow&j_username=joeuser&j_password=joeuser

However, you must take special precautions to avoid revealing a password in plain text. The server provides a way to encrypt any password that appears in a URL:

1.  Configure login encryption as described in [Encrypting User Session Login](../user-security/encrypting_user_session_login.md). Specify static key encryption by setting `encryption.dynamic.key` to `false` and configure the keystore as described.

2.  Once the server is restarted, log into the server to generate the static key.

3.  Open the following URL: `http://example.com:8080/jasperserver/encrypt.html`.

4.  Enter the password that you want to encrypt then click **Encrypt**. The script on this page uses the public key to encrypt the password.

5.  Paste the encrypted password into the URL instead of the plain text password (log out of the server to test this):

    `http://example.com:8080/jasperserver/flow.html?_flowId=homeFlow&j_username=joeuser&j_password=<encrypted>`

6.  Use the URL with the encrypted password to share a report.

For complex web applications generating report URLs on the fly, you can also encrypt the password with JavaScript. Your JavaScript should perform the same operations as the `encrypt.js` script used by the `encrypt.html` page at the URL indicated above. Using the `encryptData()` function in `encrypt.js`, your JavaScript can generate the encrypted password and use it to create the URL.

!!! warning

    Static key encryption is very insecure and is recommended only for intranet server installation where the network traffic is more protected. Anyone who sees the username and encrypted password can use them to log into JasperReports Server. Therefore, we recommend creating user IDs with very specific permissions to control access from URLs.

    The only advantage of encrypting passwords in URLs is that passwords cannot be deciphered and used to attack other systems where users might have the same password.
