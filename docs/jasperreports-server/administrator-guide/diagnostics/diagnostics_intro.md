---
title: Server Diagnostics
description: JasperReports Server provides comprehensive diagnostics so administrators can monitor the health and performance of the running server. The following tools can help you troubleshoot issues and...
---

# Server Diagnostics

JasperReports Server provides comprehensive diagnostics so administrators can monitor the health and performance of the running server. The following tools can help you troubleshoot issues and analyze performance:

-   System logs capture any errors in the code running the server, but can be configured to capture more information for debugging. If you suspect a problem or cannot pinpoint an error, you can turn log collectors on and off to capture logs while you test your issue.

-   Auditing stores key events of interest to system administrators, such as login time, log out time, user, report generated, report details, and object sizes. The audited events can be saved and moved to an archive automatically after a specified number of days.

-   Monitoring is based on audit events and provides a multi-dimensional Domain to create Ad Hoc views. This helps you generate reports that contain key metrics such as which reports use the most resources. It allows you to find places to optimize your data sources and your reports.

-   Diagnostics provide run-time data that shows the overall health of your server instance. For example, it includes values such as logged in users, currently running reports, scheduled reports, and memory use and performance in the Ad Hoc cache. The diagnostic data is exposed in a custom data source and can be easily viewed in a report or integrated with industry standard management consoles.

This chapter contains the following sections:

-   [Configuring System Logs](configuring_system_logs.md)

-   [Using Log Collectors](using_log_collectors.md)

-   [Auditing and Monitoring Events](events_being_audited_and_monitored.md)

-   [Configuring Auditing and Monitoring](configuring_auditing_and_monitoring.md)

-   [Using the Audit Data](using_the_audit_data.md)

-   [Using the Monitoring Data](using_the_monitoring_data.md)

-   [Importing and Exporting Event Data](importing_and_exporting_event_data.md)

-   [Real-Time Diagnostics](real_time_diagnostics.md)

-   [Exposing Diagnostics Through Jaspersoft's JMX Agent](jaspersofts_jmx_agent.md)

-   [Using the Diagnostic Data In Reports](using_the_diagnostic_data_in_reports.md)

-   [Excluding Diagnostic Attributes](excluding_diagnostic_attributes.md)

-   [Disabling Real-Time Diagnostics](disabling_real-time_diagnostics.md)

-   [Server Monitoring](server_monitoring.md)
