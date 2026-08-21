---
title: Cleaning Cached Data
description: "In some cases, you may want to clean up any cached data used by the OSGI framework and Eclipse runtime. You might do this, for example, after you upgrade, install new plug-ins, or apply patches. You..."
---

# Cleaning Cached Data

In some cases, you may want to clean up any cached data used by the OSGI framework and Eclipse runtime. You might do this, for example, after you upgrade, install new plug-ins, or apply patches. You can do this via the command line or by temporarily setting a flag in the `.ini` file for Jaspersoft Studio. Because the clean operations slow down the startup time, it is better to specify it on an as-needed basis.

## Cleaning From the Command Line

### Mac OS X

To set the clean flag at startup on Mac OS X, run the following commands:

`cd <jss-install>/Contents/MacOS`

`./Jaspersoft\ Studio\ Professional -clean`

### Linux

To set the clean flag at startup on Linux, run the following commands:

`cd <jss-install>`

`./Jaspersoft\ Studio\ Professional -clean`

### Windows

To set the clean flag at startup on Windows, edit the desktop shortcut as follows:

1.  Right-click on the desktop shortcut and select **Properties**.
2.  On the Shortcut tab, append `-clean` to the **Target** field. For example:

`"<jss-install>\Jaspersoft Studio Professional" -clean`

1.  Click **OK**.
2.  Double-click the shortcut to run the application.
3.  Once you have cleaned the application, edit the shortcut again to remove the `-clean` flag to avoid slowing down application startup.

## Setting the -clean Flag in the .ini File

As an Eclipse-based product, Jaspersoft Studio uses an `.ini` configuration file to control Eclipse behavior at startup. General information about Eclipse `.ini` file is available on the web, for example, at [https://wiki.eclipse.org/Eclipse.ini](https://wiki.eclipse.org/Eclipse.ini). In the case of Jaspersoft Studio, the configuration file is found in the root directory of your Jaspersoft Studio installation, with a name such as `Jaspersoft Studio.ini `or Jaspersoft Studio` Professional.ini`.

To enable cleaning via the .ini file:

1.  Locate the `.ini` file (for example, `Jaspersoft Studio.ini`). This file is in your `<jss-install>` directory on Windows and Linux, and in the `<jss-install>/Contents/Eclipse` directory on Mac.
2.  Open the file in a text editor.
3.  Locate the following line:

`-vm`

This line sets the location of the JVM to be used.

1.  Add the following line *before*`-vm`:

`-clean`

1.  Save the file.
2.  Start Jaspersoft Studio.
3.  Once you have cleaned the application, edit the `.ini` file again to remove the `-clean` flag to avoid slowing down application startup.
