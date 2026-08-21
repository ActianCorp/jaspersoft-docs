---
title: Log Files
description: "Runtime log files contain important information about JasperReports Server operations. Depending on your application server, the log output goes to one of the following files."
---

# Log Files

Runtime log files contain important information about JasperReports Server operations. Depending on your application server, the log output goes to one of the following files.

|  |  |
|----|----|
| Tomcat: | `<tomcat>/webapps/``jasperserver`` ``-pro`` /WEB-INF/logs/jasperserver.log` |
| JBoss: | `<jboss>/standalone/deployments/``jasperserver`` ``-pro`` .war/WEB-INF/logs/jasperserver.log` |

To view the log file, you must have access to the file system where JasperReports Server is installed. This section describes the settings that control the information JasperReports Server writes to its logs.

## Managing Log Settings

To set the current logging levels

1.  Log in as system administrator (`superuser` by default).
2.  Select **Manage \> Server Settings** and choose **Log Settings** in the left-panel.
3.  In the **Log Settings** panel, use the drop-down selectors to change the log level for each class being logged.

For more information about system logging, see the JasperReports Server Administrator Guide.
