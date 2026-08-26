---
title: Changing JVM to Start Jaspersoft Studio
description: "Jaspersoft Studio includes a bundled JRE, using which you can also start the application. This means that Jaspersoft Studio can be launched even on machines that do not have JRE or JDK installed..."
---

# Changing JVM to Start Jaspersoft Studio

Jaspersoft Studio includes a bundled JRE, using which you can also start the application. This means that Jaspersoft Studio can be launched even on machines that do not have JRE or JDK installed previously.

The configuration for this is available in the `.ini` file in the installation folder. The file is named `Jaspersoft Studio.ini` or `Jaspersoft Studio Professional.ini` depending on the version of Jaspersoft Studio that you are using.

Java development is not the main use case of Jaspersoft Studio. However, you can unlock this dedicated capability on the preferences page.

To change the JVM

1.  Navigate to `General `&gt; `Capabilities` page. Additional pages are displayed.

2.  View the `Java `&gt; `Installed JREs` page.

3.  Navigate to the `Execution Environments` page.

    As Jaspersoft Studio is run using a JRE, an error is displayed and the page is not opened.

    Hence, for proper Java development you must use a Java Development Kit (JDK). To start the application, use a required version of JDK. As far as possible, the JDK version must be in sync with the JRE bundled.

    For example, for Jaspersoft Studio Professional 8.2.0 that contains Adoptium Temurin OpenJDK 11.0.18, download the latest available JDK 11 LTS from the [Adoptium website](https://adoptium.net/download/).

    After selecting the proper version (that is Windows x64), you can compress the files to a directory of your choice of the package (.zip or .tar.gz).

4.  Edit the `.ini` file to modify the configuration for the `-vm` flag.

    For example, for Windows, change

    `-vm`

    `features/jre.win32.win32.x86_64.feature_11.0.18/adoptopenjdk_jre/bin`

    to:

    `-vm`

    `C:/jdk-11.0.21+9/bin`

5.  View the correct preference pages.

6.  Add or delete or modify the `Installed JREs`.

7.  Navigate to the `Execution Environments` page and configure the settings on this page.
