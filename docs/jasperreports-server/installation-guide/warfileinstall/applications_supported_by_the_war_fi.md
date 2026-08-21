---
title: Applications Supported by the WAR File Distribution
description: "The instructions in this and subsequent chapters support the following configurations:"
---

# Applications Supported by the WAR File Distribution

## Database and Application Server Support

The instructions in this and subsequent chapters support the following configurations:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th><p>Database</p></th>
<th><p>Application Server</p></th>
<th><p>Instructions Located In</p></th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="3"><p>PostgreSQL</p>
<p>MySQL</p>
<p>DB2</p>
<p>Oracle</p>
<p>SQL Server</p></td>
<td><p>Apache Tomcat<br />
JBossEAP/Wildfly</p></td>
<td><p>Current chapter</p></td>
</tr>
<tr>
<td><p>WebSphere</p></td>
<td><p><a href="../websphere/websphere_intro.md">Installing the WAR File for WebSphere</a></p></td>
</tr>
<tr>
<td><p>WebLogic</p></td>
<td><p><a href="../weblogic/warweblogic.md">Installing the WAR File for WebLogic</a></p></td>
</tr>
</tbody>
</table>

Jaspersoft recommends that you use Apache Tomcat with PostgreSQL as your repository, unless you have a strong reason to use another configuration. For version information about JVMs, application servers, databases, operating systems, and browsers, refer to the *JasperReports Server Supported Platform Datasheet*.

## Operating System Support for Bash Shell

JasperReports Server is a Java Web Application, which supports all operating system platforms where Java is fully supported. However, for the `js-install` shell scripts (described in the section below), the default shell required is the bash shell. Here is a list of shells required:

| Operating System | Required Shell for js-install scripts | System Default Shell | Script to Run |
|----|----|----|----|
| Windows | CMD shell | CMD shell | `js-install` `.bat` |
| Linux | Bash shell | Bash shell | `js-install` `.sh` |
| Solaris | Bash shell | Korn shell (ksh) | `js-install` `.sh` |
| IBM AIX | Bash shell | Korn shell (ksh) | `js-install` `.sh` |
| HP UX | Bash shell | Posix shell (posix/sh) | `js-install` `.sh` |
| FreeBSD | Bash shell | C shell (tcsh) | `js-install` `.sh` |
