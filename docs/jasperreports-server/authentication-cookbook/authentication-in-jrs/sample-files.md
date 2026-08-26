---
title: Locating and Working With Sample Files
description: "All Spring Security configuration files are located in the JasperReports Server web application deployed in an application server. In general, all of the sample files for external authentication are..."
---

# Locating and Working With Sample Files

All Spring Security configuration files are located in the JasperReports Server web application deployed in an application server. In general, all of the sample files for external authentication are located in the &lt;js‑install&gt;/samples/externalAuth-sample-config directory. Unless otherwise specified, all file names mentioned in this guide are located in this directory.

## Deploying Configuration Files

To configure JasperReports Server to work with external authentication, you need to create and deploy an external configuration file as follows:

1.  Create or copy a file and name it in the form applicationContext-&lt;customName&gt;.xml, for example, applicationContext-externalAuth-LDAP.xml. JasperReports Server includes sample files for some implementations, for example, LDAP, CAS, and an external JDBC database, in the &lt;js‑install&gt;/samples/externalAuth-sample-config/ directory.
2.  Edit the file and create and configure the bean properties correctly for your deployment, as described in the following sections.
3.  Place the correctly configured applicationContext-&lt;customName&gt;.xml file in the &lt;js-webapp&gt;/WEB-INF directory.

## WEB-INF Directory Location

Depending on your deployment and your needs, there are several ways to work with configuration files:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>Deployment</p></th>
<th><p>&lt;js-webapp&gt;/WEB-INF File Location</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Installed server</p></td>
<td><p>Once you've installed your server, either through a platform installer or any other deployment, the configuration files are deployed in the application server. The location depends on the application server where you installed JasperReports Server. If you used the bundled Apache Tomcat application server, the modified configuration files should be placed in:</p>
<p>&lt;js-webapp&gt;/WEB-INF = &lt;js-install&gt;/apache-tomcat/webapps/jasperserver[-pro]/WEB-INF</p>
<p>After modifying the configuration files, restart the application server to use the settings.</p></td>
</tr>
<tr>
<td><p>WAR file distribution</p></td>
<td><p>When you download the WAR file distribution, you can customize your deployment of JasperReports Server and possibly install it on several machines. You can find the WAR file in the following location:</p>
<p>&lt;js-webapp&gt; = &lt;js-install&gt;/jasperserver[-pro].war</p>
<p>After modifying the WAR file distribution, you need to redeploy it to your application server, as described in the <span>JasperReports Server Installation Guide</span>. But every time you redeploy your modified WAR file, external authentication is pre-configured.</p></td>
</tr>
<tr>
<td><p>Source code</p></td>
<td><p>The JasperReports Server source code contains the XML source of the configuration files. If you maintain other customizations in the source code, you can modify the configuration files for external authentication. The modified configuration files for source code are placed in:</p>
<p>&lt;js-webapp&gt;/WEB-INF = &lt;js-src&gt;/jasperserver/jasperserver-war/src/main/webapp/WEB-INF</p>
<p>When building the source, these files are copied into the WAR file that you must then deploy into a running application server. See the <span>JasperReports Server Source Build Guide</span> for more information.</p></td>
</tr>
</tbody>
</table>

!!! note

    When working with the WAR file distribution or source code, you usually modify the files in an installed server for testing. But after testing, you copy the changes into your WAR file or source code.

When working with the WAR file distribution or servers installed in application servers other than Apache Tomcat, the WAR file is kept as a single archive file from which you must extract, modify and replace the files. The following code sample shows one way to do this from the command line.

``` bash
cd <js-webapp>
"%JAVA_HOME%\bin\jar" xf jasperserver[-pro].war <path/filename>
<edit> <path\filename>
"%JAVA_HOME%\bin\jar" uf jasperserver[-pro].war <path/filename>
delete <path\filename>
```

In this sample:

-   `<path/filename>` refers to the relative path and name of the file to modify within the WAR file
-   `-pro` is part of the WAR file name if you installed a commercial edition of JasperReports Server.
