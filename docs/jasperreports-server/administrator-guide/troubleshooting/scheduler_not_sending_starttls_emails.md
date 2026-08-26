---
title: Scheduler Not Sending STARTTLS Emails
description: "If you use OpenJDK 7 as your JVM, the scheduler may not be able to send emails if you have configured it to use secure email with STARTTLS. The reports run as scheduled, but the emails are not sent,..."
---

# Scheduler Not Sending STARTTLS Emails

If you use OpenJDK 7 as your JVM, the scheduler may not be able to send emails if you have configured it to use secure email with STARTTLS. The reports run as scheduled, but the emails are not sent, and an error is recorded in the server log.

This error occurs with the following configuration in the file `.../WEB-INF/applicationContext-report-scheduling.xml`:

``` xml
    <props>
        <prop key="mail.smtp.auth">true</prop>
        <prop key="mail.smtp.starttls.enable">true</prop>
        <prop key="mail.smtp.sendpartial">true</prop>
        ...
    </props>
```

To fix this behavior, do one of the following:

-   Upgrade to OpenJDK 8.
-   Or upgrade to the latest `nss` library. The error no longer occurs with the following version:

``` text
Name        : nss
Arch        : x86_64
Version     : 3.19.1
Release     : 3.el6_6
```
