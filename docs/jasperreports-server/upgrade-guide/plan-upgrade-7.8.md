---
title: Changes in 7.8 That May Affect Your Upgrade
description: "In the 7.8 release, the JavaScript engine is switched to Chrome/Chromium from PhantomJS/Rhino. JasperReports Server now uses the Chromium JavaScript engine to export reports and dashboard to PDF and..."
---

# Changes in 7.8 That May Affect Your Upgrade

## Chrome/Chromium Updates

In the 7.8 release, the JavaScript engine is switched to Chrome/Chromium from PhantomJS/Rhino. JasperReports Server now uses the Chromium JavaScript engine to export reports and dashboard to PDF and other formats. PhantomJS/Rhino support has been removed.

You need to install and configure Chrome/Chromium to export the reports and dashboards to PDF and other output formats.

!!! note

    If you choose to continue the installation without Chrome/Chromium, reports and dashboards cannot be exported to PDF, DOCX, and other output formats.

The configuration properties have been updated to support the Chrome/Chromium configuration.

!!! note

    For information about configuring Chrome/Chromium in JasperReports Server, see the JasperReports Server Administrator Guide.
