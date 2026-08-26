---
title: Installation Requirements
description: "Before installing the product on your system, ensure that you can log in to the system with the appropriate permissions. Your system should meet the hardware and software requirements needed to..."
---

# Installation Requirements

Before installing the product on your system, ensure that you can log in to the system with the appropriate permissions. Your system should meet the hardware and software requirements needed to install JasperReports Server. See the JasperReports Server Supported Platform Datasheet for more information.

## Pre-installation Tasks

Pre-installation tasks include the tasks that you must complete before you start the installer, such as ensuring your system meets the installation requirements. If you want to use existing versions of any component software, you must also prepare them, as described in later sections.

### Exclude JasperReports Server Installer File from Security Software Scans

If using anti-virus security software, you may need to ensure that the exception list includes the `js-jrs_10.x.x_win_x86_64.exe` installer file.

### Download JasperReports Server Software

Download the JasperReports Server software package for your platform from the [Download section](https://www.jaspersoft.com/download) of the Jaspersoft Community website or from the TIBCO Software Product Download Site (<https://edelivery.tibco.com/>). Extract the JasperReports Server archive file to a temporary directory on the machine on which you run the installer.

The installers have the following file names:

-   `js-jrs``_10.1.0`

    \_win_x86_64.exe

-   `js-jrs``_10.1.0`

    \_linux_x86_64.run

-   `js-jrs``_10.1.0`

    \_macosx_x86_64.zip

## Installation Account

The privileges required to install the product differ for Windows and UNIX platforms. Ensure that you have the appropriate privileges to install on the target platform.

### Microsoft Windows

You must have administrator privileges for the machine on which you want to install the software. Right-click the binary installer file and select "Run as administrator" from the context menu.

!!! warning

    The Windows installer gets an error installing the PostgreSQL database if the Windows user does not have sufficient administrative privileges and if the installer is not started by right-clicking to use "Run as administrator".

### UNIX

In Linux, the installer is a `.run` file. You can run it from the command line or from a graphical environment. Any non-root user can perform the installation.

### Mac

In Mac OSX, the installer file is

`js-jrs``_10.1.0`

\_macosx_x86_64.zip. After download, you should find the installer already unpacked in your `<user>/Downloads` folder.

When you double-click the installer application, you see a security warning such as "&lt;filename&gt; cannot be opened because the developer cannot be verified". The Mac installer app is signed by Jaspersoft®, but it has not been notarized because that requires separately signing all dynamic libraries and enabling the hardened runtime option. Click **Cancel** to exit the warning. There are two possible ways to run the installer:

-   On older versions of Mac OSX, you can double-click again to get a different security dialog.
-   On newer versions of Mac OSX, you hold **control** and click the app, then select **Open** from the menu.

When run this way, there is another security warning such as "macOS cannot verify the developer of &lt;filename&gt;. Are you sure you want to open it?". Now there is an option to **Open** the app, so click that to open the installer.
