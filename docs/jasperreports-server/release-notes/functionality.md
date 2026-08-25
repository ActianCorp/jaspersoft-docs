---
title: Changes in Functionality
description: This section describes changes in functionality in the Jaspersoft BI Suite Version 10.1 release.
---

# Changes in Functionality

This section describes changes in functionality in the Jaspersoft BI Suite Version 10.1 release.

To view the Release Notes of version 10.0.0, see [JasperReports® Server Release Notes v10.0.0](https://community.jaspersoft.com/documentation/jasperreports-server/tibco-jasperreports-server-release-notes/v1000/relnotesbody-_-overview/).

## JasperReports® Server 10.1.0

Following are the list of changes in JasperReports® Server10.1.0:

- **Password History and Storage**

  Enterprise security and compliance have been enhanced with the addition of a password history validation password storage features.

  The password history feature blocks the reuse of the last *n* passwords during resets. And, the new password storage methods with advanced, industry-leading one-way hashing algorithms are used to elevate data protection.

- **PostgreSQL driver**

  Upgraded the PostgreSQL JDBC driver to version 42.7.11.

- **Library changes**

  The library changes include:

  - @babel/runtime library upgraded to 7.26.10

  - lodash library upgraded to 4.18.1

  - underscore library upgraded to 1.13.8

  - underscore.string library upgraded to 3.3.6

  - AWS SDK library upgraded to 2.41.25

  - jakarta.jms-api library upgrade to 3.1.0

  - jersey-\* library upgraded to 4.0.2

  - Spring library upgraded to 6.2.17

  - Spring security library upgraded to 6.5.9

## Jaspersoft® Studio 10.1.0

Following are the list of changes in Jaspersoft® Studio 10.1.0:

- **Enhanced Logging Stability**

  The Eclipse IO Console appender is refactored to natively handle concurrent, multi-threaded invocations. This resolves a known vulnerability in OSGi environments where simultaneous logging requests, whether triggered by UI widgets, internal libraries, or background components, could cause performance bottlenecks or application loops.

  Logging output is now significantly more reliable, and risk of log-induced application freezes is eliminated.

- **Library changes**

  The library changes include:

  - Eclipse Jetty library upgraded to 12.1.9

  - Jackson library upgraded to version 2.18.8

  - Jaxen library upgraded to 2.0.0

  - Microsoft Playwright library upgraded to 1.59.0

  - Mozilla Rhino library upgraded to 1.8.1

  - OWASP Java HTML Sanitizer library upgraded to 20260102.1

  - PostgreSQL library upgraded to 42.7.11

  - Spring library upgraded to 6.2.19

  - BouncyCastle library upgraded 1.84.0

  - Apache Log4J2 library upgraded to 2.25.4

  - Apache XMLBeans library upgraded to 5.3.0

  - Apache Commons Cli library upgraded to 1.11.0

  - Apache Commons Code library upgraded to 1.20.0

  - Apache Commons Compress library upgraded to 1.28.0

  - Apache Commons IO library upgraded to 2.21.0

  - Apache Commons Lang3 library upgraded to 3.20.0

  - Apache Commons Pool2 library upgraded to 2.12.1

  - Hibernate library/plug-in upgrade
