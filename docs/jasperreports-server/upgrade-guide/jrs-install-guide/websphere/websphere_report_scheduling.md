---
title: Configuring Report Scheduling
description: Scheduled reporting in JasperReports Server allows you to run reports at specified times and gives you the option to send an email notification to users when a new report is available.
---

# Configuring Report Scheduling

Scheduled reporting in JasperReports Server allows you to run reports at specified times and gives you the option to send an email notification to users when a new report is available.

## Additional Fix for Scheduled Report with JNDI Data Source

On the WebSphere application server, reports using a JNDI data source require additional configuration to correctly resolve the JNDI lookup.

The `jasperserver-pro.war` archive includes WebSphere-specific configuration files. These files are generated during the installation process. To enable this fix, you'll need to remove the `webSphere` prefix from the names of these files. Two of the file rename operations will overwrite the existing configuration file names.

|         |                                                                 |
|---------|-----------------------------------------------------------------|
| Rename: | `WEB-INF/webSphere-applicationContext-report-scheduling-wm.xml` |
| To:     | `WEB-INF/applicationContext-report-scheduling-wm.xml`           |

|         |                                                               |
|---------|---------------------------------------------------------------|
| Rename: | `WEB-INF/webSphere-js.quartz.base.properties`                 |
| To:     | `WEB-INF/js.quartz.base.properties` (overwrite existing file) |

|         |                                                              |
|---------|--------------------------------------------------------------|
| Rename: | `WEB-INF/webSphere-js.scheduling.properties`                 |
| To:     | `WEB-INF/js.scheduling.properties` (overwrite existing file) |

!!! note

    A work manager class is used to run scheduled report jobs on WebSphere. The JNDI name of the work manager and its default value (wm/default) are configured in `js.scheduling.properties`. The number of threads that run report jobs is provided by the work manager configuration.

## Additional Change for Mail Server Authentication

If your mail server requires authentication, edit the a`pplicationContext-report-scheduling.xml` file after applying the changes above.

1.  Extract the file from the WAR archive:

`"%JAVA_HOME%\bin\jar" xf jasperserver-pro.war WEB-INF/applicationContext-report-scheduling.xml`

1.  Open the file for editing and locate the `reportSchedulerMailSender` bean.
2.  Set the `javaMailProperties key=`"`mail.smtp.auth`" value to `true`.
3.  Save the file and replace it in the archive:

`"%JAVA_HOME%\bin\jar" uf jasperserver-pro.war WEB-INF/applicationContext-report-scheduling.xml`

1.  Delete the `WEB-INF` directory that was created, along with the file it contains.

For more information about setting up report scheduling, refer to [Configuring Report Scheduling](../../../installation-guide/additional/configuring_report_scheduling.md).
