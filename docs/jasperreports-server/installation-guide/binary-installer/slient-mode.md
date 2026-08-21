---
title: Installing in Silent Mode
description: "When you run the installer in silent mode, the installer does not prompt for your input or show any error messages. Instead, the input values are specified in a response file,..."
---

# Installing in Silent Mode

When you run the installer in silent mode, the installer does not prompt for your input or show any error messages. Instead, the input values are specified in a response file, TIBCOUniversalInstaller.silent. You can use the default preconfigured response file or create your own response file. Errors can be found in the logs, which are placed in a .TIBCO folder in your home directory.

By default, the installer uses the TIBCOUniversalInstaller.silent file , which is included in the directory that contains the universal installer.

To run the silent installer

You can run the silent installer with the default settings, or you can create and edit a copy of the TIBCOUniversalInstaller.silent file to use as a response file.

- If no response file has been created, invoke the installer with the `-silent` argument to use the default installation parameters.
- If a response file exists, you can invoke the installer with the arguments `-silent -V responseFile="<responseFileName>"` to use the values specified in the response file.

!!! warning

    Make sure that the ports in the response file are open. If any of the ports specified in the response file are not available, the installer will fail without an error.

To create a response file

1.  Make a copy of TIBCOUniversalInstaller.silent file and rename the file, for example, newfile.silent.
2.  Using a text editor, open the copied file and update the installation location and features to install.
3.  Open a console window, and navigate to the temporary directory where you extracted the product archive file. Run the silent installer using one of the following commands:

- On Windows: `TIBCOUniversalInstaller.cmd -silent -V responseFile="newfile.silent"`
- On UNIX: `TIBCOUniversalInstaller.bin -silent -V responseFile='newfile.silent'`
- On Mac OS: `TIBCOUniversalInstaller-mac.command -silent -V responseFile='newfile.silent'`

To customize the silent installer

- Make a backup copy of the TIBCOUniversalInstaller.silent file and edit the file itself. You can then run the silent installer with or without the response file argument.
