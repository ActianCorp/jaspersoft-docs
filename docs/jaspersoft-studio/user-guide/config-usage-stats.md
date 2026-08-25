---
title: Disabling Usage Statistics
description: "By default, the first time you run a new installation of Jaspersoft Studio, you are prompted to allow us to collect usage statistics. These statistics are anonymous. This pop-up can be disabled in..."
---

# Disabling Usage Statistics

By default, the first time you run a new installation of Jaspersoft Studio, you are prompted to allow us to collect usage statistics. These statistics are anonymous. This pop-up can be disabled in the `.ini` file in the `<jss-install>` folder.

To disable the usage statistics dialog:

1.  Locate the `.ini` file (for example, `Jaspersoft Studio.ini`). This file is in your `<jss-install>` directory on Windows and Linux, and in the `<jss-install>/Contents/Eclipse` directory on Mac.

2.  Open the file in a text editor.

3.  Locate the following line:

    `-vm`

    This line sets the location of the JVM to be used.

4.  Add the following line *before* `-vm`:

    `-com.jaspersoft.studio.skipUsageQuestion true`

5.  Save the file.
