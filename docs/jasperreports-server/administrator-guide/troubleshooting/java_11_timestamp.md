---
title: Extra Comma Appearing in Time Stamp
description: "Java 11 changed the default date format to conform to CLDR 33, which results in an extra comma appearing in the time stamps for Domains, Ad Hoc views, and reports. If you are running on Java 11 and..."
---

# Extra Comma Appearing in Time Stamp

Java 11 changed the default date format to conform to CLDR 33, which results in an extra comma appearing in the time stamps for Domains, Ad Hoc views, and reports. If you are running on Java 11 and want backwards compatibility with Java 8 date formatting, you need to set the following parameter on all nodes:

``` text
-Djava.locale.providers=JRE,COMPAT,CLDR
```

For JasperReports Server to show reports correctly in Java 11, we recommend running with these parameters in the given order.

For more information on setting JVM options, see the JasperReports Server Installation Guide.

# Error Exporting Reports, Ad Hoc Views, and Dashboards

The export of Reports, Ad Hoc Views, and Dashboards fails when Tomcat is run as root in the JasperReports Server installation on Linux. The Tomcat log file displays an error, for example:

``` text
2020-06-11T17:32:19,031 ERROR SecureExceptionHandlerImpl,http-nio-8080-exec-8:116 - com.github.kklisura.cdt.launch.exceptions.ChromeProcessTimeoutException: Failed while waiting for chrome to start: Timeout expired! Chrome output: [0611/173218.897370:ERROR:zygote_host_impl_linux.cc(89)] Running as root without --no-sandbox is not supported. See https://crbug.com/638180.
```

To resolve this, you need to set the following property in the `jasperreports.properties` file:

`net.sf.jasperreports.chrome.argument.no-sandbox=true`

After setting this property, restart JasperReports Server to enable it.

For information about configuring this property, see [Configuring a JavaScript Engine for Graphical Report Rendering](../configuration/configuring_jasperreports_library.md).
