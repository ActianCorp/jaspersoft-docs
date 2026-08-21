---
title: Installing in Console Mode
description: "In console mode, the installer prompts for values in a console window. You move through the installation by responding to the prompts."
---

# Installing in Console Mode

In console mode, the installer prompts for values in a console window. You move through the installation by responding to the prompts.

Prerequisites

Prepare your system and the installation media before running the installer in console mode.

Procedure

1.  Open a console window and navigate to the temporary directory where you extracted the product archive file.
2.  Run the installer using one of the following commands:

- On Windows:

`Run TIBCOUniversalInstaller -console`

The installer launches a second console window.

- On UNIX:

`Run ./TIBCOUniversalInstaller.lnx-x86-64.bin -console`

- On Mac OS:

`Run ./TIBCOUniversalInstaller.mac.command -console`

1.  Complete the installation by responding to the console window prompts, which are similar to those described in the section [Installing in GUI Mode](tibco-installation.md). The console also provides an option to return to a previous selection periodically.
2.  When the installation is completed, press **Enter** to exit the installer.
