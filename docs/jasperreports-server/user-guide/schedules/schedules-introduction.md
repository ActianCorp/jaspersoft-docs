---
title: Scheduling Reports and Dashboards
description: "Using the JasperReports Server scheduler, you can run reports and take snapshots of dashboards repeatedly and unattended during off hours or at other times. The reports and dashboards are saved in a..."
---

# Scheduling Reports and Dashboards

Using the JasperReports Server scheduler, you can run reports and take snapshots of dashboards repeatedly and unattended during off hours or at other times. The reports and dashboards are saved in a file format of your choice to the repository, the host machine, or an FTP server. Scheduling these jobs to run in the background or during off hours can reduce the performance impact on the server.

You can view a list of scheduled reports or dashboards on the **View &gt; Schedules** page.

Administrative users have access to a set of Ad Hoc views with details of the completed scheduled reports via the server monitoring feature. Administrators can monitor the completed scheduled reports using these Ad Hoc views. This feature is available to users with access to the Audit database. For more information on server monitoring, see the JasperReports Server Administrator Guide.

This chapter contains the following sections:

-   Overview of the Scheduler

-   [Creating a Schedule](schedules-job.md)

-   [List of Scheduled Jobs](schedules-list.md)

-   [Changing Schedules](schedules-list.md)

-   [Pausing a Job](schedules-list.md)

-   [Deleting a Job](schedules-list.md)

-   [Running a Job in the Background](schedules-background.md)

-   [Event Messages](schedules-event-messages.md)

## Overview of the Scheduler

Using the scheduler, you can set up a schedule for generating reports or dashboard with parameters, output options, and notifications:

-   Schedule – When to run the scheduled job, and how often.

-   Parameters – If the report or dashboard was designed with input controls, which parameters the scheduled job uses.

-   Output Options – The name of the output file, the output format and locale, and where the output file is stored.

-   Notifications – Email options for sending the output to recipients and for sending administrative messages.

The permissions of the user who schedules a job determines the data that is exposed. For example, Gloria only has access to inventory data from the Southeast US region. A report that she schedules only shows data from that region, even when the report is viewed by users in other regions. Other users schedule the report themselves to see the data for their own regions.

!!! warning

    Sensitive data could be exposed to unauthorized users if you schedule a job as an administrative user with no data restrictions because the output contain all requested data in the data source. Any user who receives the output can view all the data regardless of the user’s access restrictions.

Scheduling a dashboard requires having Chrome/Chromium installed on the computer hosting JasperReports Server. For information on configuring Chrome/Chromium for dashboards, see the System Configuration chapter in the JasperReports Server Administrator Guide.

By default, in the scheduled report, HTML5 charts are not interactive in the HTML output. To make them interactive in the HTML output, you need to update the `jasperReportsProSchedulerContext` bean in the `applicationContext-adhoc.xml` file.

!!! note

    You can schedule a report with the **Detail Chart Enabled** property as enabled or disabled, while this property is not supported by pie charts, gauge charts, spider charts, horizontal bar charts, and tile map charts.
