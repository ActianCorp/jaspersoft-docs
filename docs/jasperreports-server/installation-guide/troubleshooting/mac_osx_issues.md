---
title: Mac OSX Issues
description: We have seen some issues caused by the improper shutdown of the Tomcat included with JasperReports Server. This may be caused by shutting the machine down while the Tomcat is running.
---

# Mac OSX Issues

## Problem Starting JasperReports Server on Mac

We have seen some issues caused by the improper shutdown of the Tomcat included with JasperReports Server. This may be caused by shutting the machine down while the Tomcat is running.

When the Tomcat scripts start Tomcat, they write a .pid (Process ID) file to the Tomcat folder. Tomcat uses this to determine whether the Tomcat instance is already running. When Tomcat is shut down, this `pid` file is removed. However, if the `pid` file is not removed on shutdown, Tomcat fails to start up.

You may see this when you double-click the jasperServerStart.app startup. JasperReports Server seems to be starting up, but it never actually does.

To recover from this issue, manually delete the `pid` file.

Delete catalina.pid using the Finder:

1.  Navigate to the `<js-install>/tomcat/temp` folder.

    For instance: `/Applications/10.1.0/tomcat/temp`

2.  Delete `catalina.pid`

Delete the catalina.pid file using the Terminal shell:

1.  Open a Terminal shell (**Finder \> Go \> Utilities \> Terminal Icon**)

2.  Navigate to the `<js-install>/tomcat/temp` folder.

    For instance: `/Applications/10.1.0/tomcat/temp`

3.  Enter the following command:

`rm catalina.pid`

To start and stop the PostgreSQL and Tomcat components separately from the command-line shell:

1.  Open a Terminal shell (**Finder \> Go \> Utilities \> Terminal Icon**).

2.  Navigate to the `<js-install>` folder.

    For instance: `/Applications/10.1.0`

3.  To start:

    `./ctlscript start postgresql`

    `./ctlscript start tomcat`

4.  To shut down:

`./ctlscript stop `

Or

`./ctlscript stop tomcat`

`./ctlscript stop postgresql`
