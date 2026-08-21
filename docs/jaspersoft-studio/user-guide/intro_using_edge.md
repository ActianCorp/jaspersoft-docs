---
title: Using Edge in Jaspersoft Studio Window Builds
description: The following section describes how to use the latest available version of the Microsoft Edge browser in Jaspersoft Studio Windows builds.
---

# Using Edge in Jaspersoft Studio Window Builds

The following section describes how to use the latest available version of the Microsoft Edge browser in Jaspersoft Studio Windows builds.

Eclipse (and its associated products) can use Edge by properly configure some information in the startup configuration file and/or via code.

To configure your Jaspersoft Studio installation to work with Microsoft Edge, perform the following:

1.  Download the Microsoft Edge WebView2 Runtime from <https://developer.microsoft.com/en-us/microsoft-edge/webview2/>. The recommended option is "Fixed version" x64.

2.  Unpack the downloaded package to your local directory using a tool such as 7-zip, or the following command:

    ``` text
    expand Microsoft.WebView2.FixedVersionRuntime.<VERSION>.x64.cab -F:* C:\<TARGET_DIR>
    ```

3.  Edit the `Jaspersoft Studio Professional.ini` file appending the following two Java properties (replace with the proper WebView file location):

    ``` text
    -Dorg.eclipse.swt.browser.DefaultType=edge-Dorg.eclipse.swt.browser.EdgeDir=C:\\dev\\webview
    ```

If the Edge browser configuration is missing, the following warning is displayed in the bottom toolbar of the JRXML editor.<br>

`Edge browser engine is not setup. HTML ` ` Preview will not work fine`.<br>
