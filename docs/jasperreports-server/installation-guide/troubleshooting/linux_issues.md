---
title: Linux Issues
description: "Your operating system configuration can influence the behavior of characters supported by JasperReports Server. On some Linux systems, Oracle JDK 8 sets the 'sun.jnu.encoding' system property to..."
---

# Linux Issues

## File Issues with Extended Character Sets on Linux

Your operating system configuration can influence the behavior of characters supported by JasperReports Server. On some Linux systems, Oracle JDK 8 sets the '`sun.jnu.encoding`' system property to define the character set for encoding file names for I/O operations. This system property is set up on Java application startup and takes its value from the Linux system locale.

However, if the operating system is configured to use a non-UTF-8 encoding, JasperReports Server components may function in an unexpected way. For example, log collectors with non-UTF-8 names may be configured incorrectly. To fix these problems on a Linux operating system, enable Unicode support by setting the `LANG` and `LC_ALL` environment variables to a locale with the UTF-8 character set. This allows the operating system to process any character in Unicode. For example, `LANG=en_US.UTF-8` and `LC_ALL=en_US.UTF-8`.

## Linux Installer Issue with Unknown Host Error

If your Linux server doesn't have proper hostname entries in the `/etc/hosts` file, you may get installer errors.

The installer carries out an import operation to load the core minimal data into the repository database. This import operation can fail if the host is not configured.

If the import operation fails during installation, the installation will also fail. However, there should be an installation.log in the root of the installation folder to help debug the problem. The `installation.log` is located here:

`<js-install>/installation.log`

An improperly configured hosts file typically causes error messages like these:

```
Caused by: java.net.NoRouteToHostException: No route to host
com.mysql.jdbc.exceptions.jdbc4.CommunicationsException: Communications link failure
ERROR Cache:145 - Unable to set localhost. This prevents creation of a GUID
java.net.UnknownHostException
org.quartz.SchedulerException: Couldn't get host name!
```

To fix the /etc/hosts file:

1.  Include entries that look like these:

`127.0.0.1      localhost.localdomain`

`172.17.5.0     myhost.mydomain.com       myhost`

For instance:

`127.0.0.1       localhost.localdomain           localhost`

`172.17.5.0      myhost.jaspersoft.com          myhost`

1.  You can also double check the file `/etc/sysconfig/network` (if it exists). In this file it would be similar to the following:

`HOSTNAME=myhost`

1.  After fixing the `/etc/hosts` file, reinstall JasperReports Server.
