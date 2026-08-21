---
title: Additional Steps for Using the IBM JDK
description: "If you are using the IBM JDK, you need to set OWASP to use the correct Pseudo-random Number Generator (PRNG). To do this before installation, you can modify the WAR file as follows:"
---

# Additional Steps for Using the IBM JDK

If you are using the IBM JDK, you need to set OWASP to use the correct Pseudo-random Number Generator (PRNG). To do this before installation, you can modify the WAR file as follows:

1.  The WAR file is an archive format in a single file.
2.  Extract the `Websphere.jrs.csrfguard.properties` file using the following command:

```
cd <js-install>
"%JAVA_HOME%/bin/jar" xf jasperserver-pro.war WEB-INF/csrf/Websphere.jrs.csrfguard.properties
```

This creates the `WEB-INF/csrf` folder in the current location and places the extracted file there.

1.  Rename the file from `Websphere.jrs.csrfguard.properties` to `jrs.csrfguard.properties` using the following command:

```
mv ./WEB-INF/csrf/Websphere.jrs.csrfguard.properties ./WEB-INF/csrf/jrs.csrfguard.properties
```

1.  After you have modified the file, replace it in the WAR file archive using the following commands.

```
cd <js-install>
"%JAVA_HOME%\bin\jar" uf jasperserver-pro
    .war WEB-INF/csrf/jrs.csrfguard.properties
```
