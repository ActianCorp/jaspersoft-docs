---
title: Location of Interpreted Files
description: "Interpreted files are located in the JasperReports Server web application, known as &lt;js‑webapp&gt;. Depending on your deployment and your needs, there are several ways to work with the interpreted..."
---

# Location of Interpreted Files

Interpreted files are located in the JasperReports Server web application, known as &lt;js‑webapp&gt;. Depending on your deployment and your needs, there are several ways to work with the interpreted files, which in turn determine the definition of &lt;js-webapp&gt; that you use.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>File Location</p></th>
<th><p>&lt;js-webapp&gt; Path</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Installed server</p></td>
<td><p>Once you have installed your server, either through a platform installer or any other deployment, the files are deployed in a running application server. The location depends on the application server where you installed JasperReports Server. If you used the bundled Apache Tomcat application server, the files are located in:</p>
<p><code>&lt;js-webapp&gt; = &lt;js-install&gt;/apache-tomcat/webapps/jasperserver[-pro]</code></p>
<p>For other application servers, see <a href="customizing-war-files.md">Customizing WAR Files</a>.</p>
<p>After modifying the UI files (except CSS), reload the web app to see the changes. This is the easiest way to customize files, because you can see your changes almost immediately. However, your changes are limited to this one instance of the server.</p></td>
</tr>
<tr>
<td><p>WAR file distribution</p></td>
<td><p>When you download the WAR (web archive) file distribution, you can customize your deployment of JasperReports Server and possibly install it on several machines. The WAR file distribution also includes the UI files in the following location:</p>
<p><code>&lt;js-webapp&gt; = &lt;js-install&gt;/jasperserver[-pro].war</code></p>
<p>To modify files with the WAR file, see <a href="customizing-war-files.md">Customizing WAR Files</a>. After modifying the WAR file distribution, you need to deploy it to your application server, as described in the <span>JasperReports Server Installation Guide</span>. But every time you redeploy your modified WAR file, your UI changes are included.</p></td>
</tr>
<tr>
<td><p>Source code</p></td>
<td><p>The JasperReports Server source code also contains the original versions of the interpreted files. If you maintain other customizations in the source code, you can modify the UI files as well. The files in the source code are located in:</p>
<p><code>&lt;js-webapp&gt; = &lt;js-src&gt;/jasperserver/jasperserver-war/src/main/webapp</code></p>
<p>When building the source, these files are copied into the WAR file that you must then deploy into a running application server. See the <span>JasperReports Server Source Build Guide</span> for more information. The advantage of working with the source code is that you can always generate the server with your customized UI files.</p></td>
</tr>
</tbody>
</table>

!!! note

    When working with the WAR file distribution or source code, you usually modify files in an installed server for testing. But after testing, you copy the changes into your WAR file or source code.
