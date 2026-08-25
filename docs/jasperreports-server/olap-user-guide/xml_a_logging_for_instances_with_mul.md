---
title: XML/A Logging for Instances with Multiple Organizations
description: "For server instances that have multiple organizations, XML/A logging is configured separately in the JasperReports Server web UI. Messages from this logger are written to the default log file is..."
---

# XML/A Logging for Instances with Multiple Organizations

For server instances that have multiple organizations, XML/A logging is configured separately in the JasperReports Server web UI. Messages from this logger are written to the default log file is `WEB‑INF\logs\jasperserver.log`. To enable this logger, you must enter the correct classname.

To add a logger to the page from the web interface

1.  Log in as system administrator (`superuser` by default).

2.  Select **Manage \>** **Server Settings** and choose **Log Settings** in the left-hand panel.

3.  Scroll to the bottom of the page.

4.  Enter the logger’s classname in the text field. See the other properties on the page for guidance, for example:

    `com.jaspersoft.ji.ja.security.service.MTXmlaServletImpl`

5.  Use the dropdown to set the logging level.

The logger setting is persistent even when the server is restarted. However, the logger setting may not appear on the Log Settings page again. For information about adding loggers to this page permanently, see the JasperReports Server Administrator Guide.
