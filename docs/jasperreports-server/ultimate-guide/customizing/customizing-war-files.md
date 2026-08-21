---
title: Customizing WAR Files
description: "When you modify UI files in application servers other than Apache Tomcat or in the WAR file distribution, the web application is kept as a single WAR (web archive) file. To modify files inside the..."
---

# Customizing WAR Files

When you modify UI files in application servers other than Apache Tomcat or in the WAR file distribution, the web application is kept as a single WAR (web archive) file. To modify files inside the WAR file, you must extract, modify, and replace the files. The following example shows one way to do this from the Windows command line (commands are similar in Linux).

In this example, \<path/filename\> refers to the relative path and name of the file to modify within the WAR file:

``` bash
cd <js-webapp>
"%JAVA_HOME%\bin\jar" xf jasperserver[-pro].war <path/filename>
<edit> <path\filename>
"%JAVA_HOME%\bin\jar" uf jasperserver[-pro].war <path/filename>
delete <path\filename>
```

After modifying files in the running application or reloading the web application, you may need to perform the following steps, depending on your application server:

1.  Clear the application server's work folder. In the case of Apache Tomcat, you would delete all files and folders in the \<tomcat\>/work folder.
2.  Click Refresh on your browser.
3.  In some cases, you may need to restart the application server.
