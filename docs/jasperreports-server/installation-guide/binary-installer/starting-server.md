---
title: Starting and Stopping the Server
description: This section describes start and stop procedures that vary depending on whether you installed the bundled Tomcat and PostgreSQL or used your own Tomcat and PostgreSQL.
---

# Starting and Stopping the Server

-   [Start/Stop Menu — Windows](#startstop-menuwindows)

-   [Start/Stop Scripts — Linux](#startstop-scriptslinux)

-   [Start/Stop Apps — Mac OSX](#startstop-appsmac-osx)

## Start/Stop Menu—Windows

This section describes start and stop procedures that vary depending on whether you installed the bundled Tomcat and PostgreSQL or used your own Tomcat and PostgreSQL.

### Start/Stop Menus—Bundled Tomcat and PostgreSQL

If you installed the bundled Tomcat and PostgreSQL, use the Windows Start menu to start and stop JasperReports Server.

-   Click **Start &gt; JasperReports Server &gt; Start Service**.

-   Click **Start &gt; JasperReports Server &gt; Stop Service.**

### Additional Information about the Bundled Tomcat and PostgreSQL

The Windows installer installs PostgreSQL and Tomcat as Windows Services. You can manage these services in the Windows Control Panel:

**Control Panel &gt; System and Security &gt; Administrative Tools &gt; Services**

You can also start JasperReports Server from the Windows Start menu or by using the Desktop icon. You can shut down using the Desktop icon.

#### JasperReports Server Windows Service Names

PostgreSQL and Tomcat, installed as Windows Services, are listed in the Windows Services Panel as:

-   `jasperreportsPostgreSQL`

-   `jasperreportsTomcat`

#### Preventing JasperReports Server from starting up automatically

By default, the bundled services start automatically on a reboot, which also starts JasperReports Server. To change the startup mode for the services from automatic to manual:

-   In the Windows Services Panel, select `jasperreportsTomcat`.

-   Right-click the `jasperreportsTomcat` service, and select Properties.

-   Change the Startup type dropdown setting from Automatic to Manual.

-   Follow the same steps for `jasperreportsPostgreSQL` service.

To start JasperReports Server from the Windows Services Panel:

1.  Open the Windows Services Panel.
2.  Select `jasperreportsPostgreSQL`, click Start.
3.  Select `jasperreportsTomcat`, click Start.

To start JasperReports Server from the CMD Shell:

1.  Open a Windows CMD Shell.

2.  Navigate to the root of the &lt;js-install&gt; folder (for example, C:\\Jaspersoft\\10.1.0)

    1.  To start JasperReports Server, run the following command:

        `servicerun START`

    2.  To shut down JasperReports Server, run the following command:

        `servicerun STOP`

Running Processes

When JasperReports Server is running, the Windows Task Manager lists information about the processes running under the SYSTEM username, for example:

-   `postgres.exe`

-   `tomcat9.exe`

### Start/Stop Scripts—No Bundled Applications

During installation, if you chose to install one bundled and one existing Tomcat or PostgreSQL, you can use the Windows start/stop scripts to start and stop only the bundled one.

For example, if you have an existing Tomcat and you install the bundled PostgreSQL, the scripts and menus specified in the previous section would start and stop the PostgreSQL application. To start and stop the existing Tomcat, you would use the management scripts provided by the Tomcat application.

!!! note

    JasperReports Server requires database and application servers to be started in this order:

    1.  Database server.
    2.  Application server.

## Start/Stop Scripts—Linux

This section describes start and stop procedures that vary depending on whether you installed the bundled Tomcat and PostgreSQL or used your own Tomcat and PostgreSQL.

### Manual Start/Stop

You typically start and stop JasperReports Server at the Linux command line. Run the following commands in a Linux shell.

-   To start JasperReports Server, enter:

    `cd <js-install>`

    `./ctlscript.sh start`

-   To stop JasperReports Server, enter:

    `cd <js-install>`

    `./ctlscript.sh stop`

To start and stop individual components:

``` bash
cd <js-install>
./ctlscript.sh start|stop   postgresql
./ctlscript.sh start|stop   tomcat
```

If you enter just the `./ctlscript.sh` command, then you get the following:

``` bash
./ctlscript.sh
usage: ./ctlscript.sh help
./ctlscript.sh (start|stop|restart|status)
./ctlscript.sh (start|stop|restart|status) postgresql
./ctlscript.sh (start|stop|restart|status) tomcat
help - this screen
start - start the service(s)
stop - stop the service(s)
restart - restart or start the service(s)
status - show the status of the service(s)
```

### Auto Start/Stop with Bundled Tomcat and PostgreSQL

If you want JasperReports Server to start automatically when you reboot your Linux server, you need to install the JasperReports Server database and application server as services. If you have installed JasperReports Server using the binary installer with the bundled Tomcat and bundled PostgreSQL options, you will find an example of the `jasperserver` service script in the following location:

`<js-install>/scripts/linux/jasperserver`

Edit this script and set permissions as described in the `<js-install>/scripts/linux/readme` file in the same location.

Once installed, these services start automatically when you reboot, which also starts JasperReports Server.

## Start/Stop Apps—Mac OSX

After you complete the Mac OSX installation, you typically find JasperReports Server installed in the following location:

`/Applications/`10.1.0

When JasperReports Server is running, you can see the names of the Java and PostgreSQL processes in the Activity Monitor.

-   To start JasperReports Server, locate this folder in the Finder and double-click the following app:

`jasperServerStart.app`

-   To stop JasperReports Server, locate this folder in the Finder and double-click the following app:

`jasperServerStop.app`

The Mac lists the following information in the Activity Monitor:

-   Java

Or

`org.apache.catalina.startup.Bootstrap`

-   PostgreSQL

### Start/Stop Apps—Mac Dock

Using Finder, move the following apps into the Mac Dock to start, stop, and log in to JasperReports Server:

-   `jasperServerStart.app`

-   `jasperServerStop.app`

-   `jasperServerLogin.app`

### Start/Stop JasperReports Server — Mac Terminal Shell

To start and stop JasperReports Server using the Mac terminal shell:

1.  Open a Terminal shell (**Finder &gt; Go &gt; Utilities &gt; Terminal Icon**).

2.  Navigate to the `<js-install>` folder. For instance: `/Applications/`10.1.0

3.  To start PostgreSQL, Tomcat, and JasperReports Server, enter:

    `./ctlscript.sh start`

4.  To shut down PostgreSQL, Tomcat, and JasperReports Server, enter:

    `./ctlscript.sh stop`

5.  To start and stop individual components:

``` bash
cd <js-install>
./ctlscript.sh start|stop   postgresql
./ctlscript.sh start|stop   tomcat
```

If you enter just the `./ctlscript.sh` command you get the following:

``` bash
./ctlscript.sh
usage: ./ctlscript.sh help
./ctlscript.sh (start|stop|restart|status)
./ctlscript.sh (start|stop|restart|status) postgresql
./ctlscript.sh (start|stop|restart|status) tomcat
help - this screen
start - start the service(s)
stop - stop the service(s)
restart - restart or start the service(s)
status - show the status of the service(s)
```
