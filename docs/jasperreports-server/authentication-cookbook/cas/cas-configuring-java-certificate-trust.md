---
title: Configuring Java to Trust the CAS Certificate
description: The CAS protocol requires that the response to the service validation be established over HTTPS for security. This connection is established from the Java classes of Spring Security. So you need to...
---

# Configuring Java to Trust the CAS Certificate

The CAS protocol requires that the response to the service validation be established over HTTPS for security. This connection is established from the Java classes of Spring Security. So you need to configure the Java security system. Java security must trust the certificate it receives from the CAS server, otherwise it refuses to connect. This trust is based on two factors:

1.  The host name in the certificate has to match the host name in the URL of the connection. Certain JVMs require hostnames as opposed to IP addresses, even if the IP addresses match. If you're using a CAS test server, see [CAS Server for Testing](cas-test-server.md) for instructions to create a certificate in a keystore.

2.  You must tell Java to trust the signing certificate:

    1.  On the CAS server, export your CAS certificate using the command line `keytool` utility. For example:

    ``` text
    keytool -exportcert -alias cascert -file cascertfile.cer
    ```

    Enter the password to the keystore when prompted.

3.  Copy the CAS certificate you just exported to the JasperReports Server host and import it to the Java certificate store. For example, to import the certificate to the default truststore location, you might use the following:

``` text
keytool -importcert -alias cascert -keystore $JAVA_HOME/jre6/lib/security/cacerts -file cascertfile.cer
```

Enter the password to the keystore when prompted.

!!! note

    A non-default cacerts location can be specified using the -Djavax.net.ssl.trustStore JVM parameter.
