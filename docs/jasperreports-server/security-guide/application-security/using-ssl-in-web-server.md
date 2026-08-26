---
title: Enabling SSL in Tomcat
description: "Secure Sockets Layer (SSL) is a widely-used protocol for secure network communications. It encrypts network connections at the Transport Layer and is used with HTTPS, the secure version of the HTTP..."
---

# Enabling SSL in Tomcat

Secure Sockets Layer (SSL) is a widely-used protocol for secure network communications. It encrypts network connections at the Transport Layer and is used with HTTPS, the secure version of the HTTP protocol. This section shows how to install SSL on Tomcat 9 and to configure JasperReports Server to use only SSL in Tomcat.

## Setting Up an SSL Certificate

To use SSL, you need a valid certificate in the Tomcat keystore. In the Java Virtual Machine (JVM), certificates and private keys are saved in a keystore. This is the repository for your keys and certificates. By default, it is implemented as a password-protected file (public keys and certificates are stored elsewhere).

If you already have a suitable certificate, you can import it into the keystore, using the import switch on the JVM keytool utility. If you do not have a certificate, you can use the keytool utility to generate a self-signed certificate (one signed by your own certificate authority). Self-signed certificates are acceptable in most cases, although certificates issued by certificate authorities are even more secure. And they do not require your users to respond to a security warning every time they login, as self-signed certificates do.

The following command is an example of how to import a certificate. In this case a self-signed certificate imported into a PKCS12 keystore using OpenSSL:

``` text
openssl pkcs12 \-export \-in mycert.crt \-inkey mykey.key \-out mycert.p12
               \-name tomcat \-CAfile myCA.crt \-caname root \-chain
```

Next in this example, you create key.bin, the keystore file, in the Tomcat home folder. Use one of these commands.

For Windows:

``` text
%JAVA_HOME%\bin\keytool -genkey -alias tomcat -keyalg RSA -keystore %CATALINA_HOME%\conf\key.bin
```

For Unix:

``` bash
$JAVA_HOME/bin/keytool -genkey -alias tomcat -keyalg RSA -keystore $CATALINA_HOME/conf/key.bin
```

The basic install requires certain data. With the above commands, you are prompted for the data:

-   Enter two passwords twice. The default for both is “changeit”. If you use the default, be sure to set better, stronger passwords later.
-   Specify information about your organization, including your first and last name, your organization unit, and organization. The normal response for the first and last name is the domain of your server, such as jasperserver.mycompany.com. This identifies the organization that the certificate is issued *to*. For organization unit, enter your department or similar-sized unit; for organization, enter the company or corporation. These identify the organization that the certificate is issued *by*.
-   Keytool has numerous switches. For more information about it, see the [Java documentation](http://download.oracle.com/javase/6/docs/technotes/tools/solaris/keytool.html).

## Enabling SSL in the Web Server

Once the certificate and key are saved in the Tomcat keystore, you need to configure your secure socket in the $CATALINA_BASE/conf/server.xml file, where $CATALINA_BASE represents the base directory for the Tomcat instance. For your convenience, sample `<Connector>` elements for two common SSL connectors (blocking and non-blocking) are included in the default server.xml file that is installed with Tomcat. They are similar to the code below, with the connector elements commented out, as shown.

``` text
<!-- Define a SSL HTTP/1.1 Connector on port 8443
     This connector uses the JSSE configuration, when using APR, the
     connector should be using the OpenSSL style configuration
     described in the APR documentation -->
<!--
<Connector port="8443" protocol="HTTP/1.1" SSLEnabled="true"
           maxThreads="150" scheme="https" secure="true"
           clientAuth="false" sslProtocol="TLS" />
-->
```

To implement a connector, you need to remove the comment tags around its code. Then you can customize the specified options as necessary. For detailed information about the common options, consult the [Tomcat 9.0 SSL Configuration HOW-TO](http://tomcat.apache.org/tomcat-9.0-doc/ssl-howto.html). For detailed information about all possible options, consult the [Server Configuration Reference](http://tomcat.apache.org/tomcat-9.0-doc/config/index.html).

The default protocol is HTTP 1.1. The default port is 8443. The port is the TCP/IP port number on which Tomcat listens for secure connections. You can change it to any port number (such as the default port for HTTPS communications, which is 443). However, note that if you run Tomcat on port numbers lower than 1024, a special setup outside the scope of this document is necessary on many operating systems.

## Configuring JasperReports Server to Use Only SSL

At this point, the JasperReports Server web application runs on either protocol (HTTP and HTTPS). You can test the protocols in your web browser.

| HTTP:  | http://localhost:8080/jasperserver\[-pro\]/              |
|--------|----------------------------------------------------------|
| HTTPS: | https://localhost:&lt;SSLport&gt;./jasperserver\[-pro\]/ |

The next step then is to configure the web application to enforce SSL as the *only* protocol allowed. Otherwise, requests coming through HTTP are still serviced.

Edit the file &lt;js-webapp&gt;/WEB-INF/web.xml. Near the end of the file, make the following changes inside the first `<security-constraint>` tag:

-   Comment out the line `<transport-guarantee>NONE</transport-guarantee>`.
-   Uncomment the line `<transport-guarantee>CONFIDENTIAL</transport-guarantee>`.

Your final code should be like the following:

``` xml
<security-constraint>
  <web-resource-collection>
    <web-resource-name>JasperServerWebApp</web-resource-name>
    <url-pattern>/*</url-pattern>
  </web-resource-collection>
  <user-data-constraint>
    <!-- SSL not enforced -->
    <!-- <transport-guarantee>NONE</transport-guarantee> -->
    <!-- SSL enforced -->
    <transport-guarantee>CONFIDENTIAL</transport-guarantee>
  </user-data-constraint>
</security-constraint>
```

The term `CONFIDENTIAL` forces the server to accept only SSL connections through HTTPS. And because of the URL pattern `/*`, all web services must also use HTTPS. If you need to turn off SSL mode, you can set the transport guarantee back to `NONE` or delete the entire `<security-constraint>` tag.
