---
title: Selecting a Chrome/Chromium Configuration
description: "Chrome/Chromium runs JavaScript when generating graphical reports that are run in the background or scheduled. (When run directly in the Web UI, the browser itself renders the graphics.) You have..."
---

# Selecting a Chrome/Chromium Configuration

Chrome/Chromium runs JavaScript when generating graphical reports that are run in the background or scheduled. (When run directly in the Web UI, the browser itself renders the graphics.) You have three options:

- Use an existing Chrome/Chromium.

- Download Chrome/Chromium.

- Install without Chrome/Chromium.

## Using an Existing Chrome/Chromium

If you choose to use an existing Chrome/Chromium executable, you will be prompted for the location of Chrome/Chromium. If Chrome/Chromium is installed at the default location, the installer detects the path, or you can select another location.

The installer first checks for Chrome at the default location, if Chrome is not available, it checks for Chromium at the default location.

!!! note

    Auto-detection only works for Chrome/Chromium. A different path can be specified only for Chrome/Chromium in the installer. To use another browser, such as Edge, set the path in the js.config.properties file.

For information about configuring Chrome/Chromium or another browser in JasperReports Server, see the JasperReports® Server Administrator Guide.

## Downloading Chrome/Chromium

If you do not have Chrome/Chromium installed, you can download Chrome or Chromium during installation. The installer provides the Chrome and Chromium download links.

For information about configuring Chrome/Chromium in JasperReports Server, see the JasperReports® Server Administrator Guide.

## Installing without Chrome/Chromium

If you choose to continue the installation without Chrome/Chromium, reports and dashboards cannot be exported to PDF, DOCX, and other output formats.
