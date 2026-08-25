---
title: Installation
description: "When you run the installer in GUI mode, the installer presents panels that you can use to choose the installation environment and customize your installation."
---

# Installation

## Installing in GUI Mode

When you run the installer in GUI mode, the installer presents panels that you can use to choose the installation environment and customize your installation.

Steps for all installations

1.  Run the installer executable. On Windows, make sure to right-click the binary installer file and select **Run as administrator** from the context menu.

    - On Microsoft Windows:

      `js-jrs``_10.1.0`

      \_win_x86_64.exe

    - On Unix:

      `js-jrs``_10.1.0`

      \_linux_x86_64.run

    - On Mac OS:

      `js-jrs``_10.1.0`

      \_macosx_x86_64.zip

2.  On the welcome screen, click **Next**.

3.  To accept the license agreement, click **I accept the agreement** then click **Next**.

4.  Select the installation type that you want, then click **Next**.

    - **Install All Components and Samples** installs all components and samples.
    - **Custom Install** lets you choose some pre-installed and some bundled components. Make sure you have installed supported versions of the components you want. If you are using a pre-installed Tomcat, make sure it is stopped. If you are using an existing PostgreSQL instance, it must be running during install. See the *JasperReports Server Supported Platforms Datasheet* for information about supported versions.

5.  Select an installation path, then click **Next**. The default `<js-install>` directory depends on your operating system:

    |                 |                        |
    |-----------------|------------------------|
    | Windows:        | `C:\Jaspersoft\10.1.0` |
    | Linux:          | `<USER_HOME>/10.1.0`   |
    | Linux (as root) | `/opt/10.1.0`          |
    | Mac OSX         | `/Applications/10.1.0` |

    !!! note

        On Linux, choose a `<js-install>` path that is no more than 84 characters.

6.  In the **Chromium folder** window, choose whether or not to use Chromium, then click **Next**.

    - Yes
    - No

    !!! note

        JasperReports Server uses the Chromium browser engine when you export reports and dashboards to PDF and other formats. If you do not have Chrome/Chromium installed, you can download Chrome or Chromium using the links given on the **Chromium folder** window.

7.  If you choose **Yes**, specify the Chromium binary you want to use. If Chrome/Chromium is installed at the default location, the installer detects the path, or click **Browse** to select another location.

    Auto-detection only works for Chrome/Chromium. A different path can be specified only for Chrome/Chromium in the installer. To use another browser, such as Edge, set the path in the js.config.properties file.

    !!! note

        For information about configuring Chrome/Chromium or another browser in JasperReports Server, see the JasperReports Server Administrator Guide.

8.  If you choose **No**, a warning message is displayed. Click **Yes** to continue.

    !!! warning

        If you choose to continue the installation without Chrome/Chromium, reports and dashboards cannot be exported to PDF, DOCX, and other output formats.

9.  If you plan to install JasperReports Server 10.1 on the same machine as an existing version 7.2.x or 7.5.x, you may encounter errors due to shared keystore files. Jaspersoft does not recommend running different versions on the same machine, but it is possible for evaluation purposes. You will need to follow additional steps after installation, as given by the link on the installer screen. To acknowledge this warning, click **Next**.

    If you chose **Install All Components and Samples**, installation begins.

    Additional steps for custom install

10. If you selected **Custom Install**, choose your components:

    - Select the bundled or an existing Tomcat, then click **Next**.
    - Select the bundled or an existing PostgreSQL database, then click **Next**. If you select an existing database, a warning popup appears. Click **Yes** to continue.

11. Enter your Tomcat ports, which may include server port, shutdown port, and AJP port. Then click **Next**.

12. Enter your database server port and click **Next**.

13. If you selected an existing Tomcat, specify your Tomcat directory and click **Next**.

14. If you selected an existing PostgreSQL, specify your PostgreSQL directory and click **Next**.

15. When you are prompted, choose whether or not to install sample databases and reports. Then click **Next**.

16. Click **Next** to begin the installation.<br>
    JasperReports® Server and any selected bundled components are installed on your system.

    Finalizing the installation

17. Make your post-install selections on the final screen:

    - **Launch JasperReports Server Login Page**: If you selected both bundled Tomcat and PostgreSQL, you see an option **Launch JasperReports Server Login Page**. If you are installing on Linux, then do not close the terminal window running the start script.

    If you choose not to **Launch JasperReports Server Now**, the bundled components will not be started. If you have only one bundled component, it will not be started unless you use the Start/Stop menus or scripts.

    - **Opt-in for JasperServer Heartbeat**: Sends anonymous system and version information to Jaspersoft using HTTPS.

18. Click **Finish** to complete the installation process and close the installer window.

## Installing Using the Command Line

In Linux, the installer is a .run file; you can run it from the command line or from a graphical environment. To start the installer from the command line, open a bash shell, and enter the name of the installer file. For example:

`.js-jrs_10.1.0_linux_x86_64.run`

Whether you run the installer from the command line or in a graphical environment, you are prompted for the same information. If you are installing from the command line, use your keyboard to specify your answers. For example, with the license text, instead of clicking **I accept the agreement**, press **Y**, and press **Enter**.
