---
title: Starting the Installer
description: "In Windows, you will need administrative privileges to run the installer executable file. Right-click the binary installer file and select \"Run as administrator\" from the context menu."
---

# Starting the Installer

In Windows, you will need administrative privileges to run the installer executable file. Right-click the binary installer file and select "Run as administrator" from the context menu.

`js-jrs``_10.1.0`

\_win_x86_64.exe     (64 bit only)

!!! warning

    The Windows installer gets an error installing the PostgreSQL database if the Windows user does not have sufficient Administrative privileges and if the installer is not started by right-clicking to use “Run as administrator”.

In Linux, the installer is a .run file; you can run it from the command line or from a graphical environment. To start the installer from the command line, open a bash shell, and enter the name of the installer file. For example:

`./`

`js-jrs``_10.1.0`

\_linux_x86_64.run     (64 bit)

In Mac OSX, the installer is a .zip file. After download, you should find the installer already unpacked in your \<user\>/Downloads folder. Double-click the following:

`js-jrs``_10.1.0`

\_macosx_x86_64.app          (64 bit only)

Whether you run the installer from the command line or in a graphical environment, you will be prompted for the same information. The following sections describe these prompts and assume you are in a graphical environment. If you are installing from the command line, use your keyboard to specify the same details. For example, with the license text, instead of clicking **I accept the agreement**, you press **Y** and press **Enter**.

The welcome screen introduces the installer. Click **Next**.

!!! warning

    On Windows, you will get an error installing the PostgreSQL database if you do not have Administrative privileges and if you do not start the installer by right-clicking to use “Run as administrator”.
