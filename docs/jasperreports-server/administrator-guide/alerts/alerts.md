---
title: Alerts
description: "The features in this section may be restricted by your JasperReports Server software license. If you don't see some of the options described, your current license likely prohibits their use. Contact..."
---

# Alerts

!!! info "Important"

    The features in this section may be restricted by your JasperReports Server software license. If you don't see some of the options described, your current license likely prohibits their use. Contact us to learn about your licensed features or to discuss upgrading.

Using the JasperReports Server alert feature, you can set alerts for reports from the Report Viewer toolbar. This functionality is available for Tables and Crosstabs. Alerts help you to monitor the data and notifies you when there is any significant change in the data. You can create, view, search, edit, and delete an alert.

For more information, see JasperReports Server User Guide.

## Configuring Alerts

The prerequisite to contain configuration settings is that the email needs to be set up for alerting to function properly.

The scheduled alert run for the reports in the background according to a user-defined schedule. Alerts use the same engine and the same misfire policy as the Scheduler. You can configure alerts using the aspects of the Scheduler. For more information, see [Configuring the Scheduler](../configuration/configuring_the_scheduler.md).

## Performance Impact

The JasperReports Server could experience performance impact since both the Scheduler and Alert functionalities rely on the same engine. This might be due to various scenarios, for example, when multiple alerts are set on the same report the import operation affects server performance.

## Recommendation

Whenever there is a performance issue on JasperReports Server, we encourage you to increase the thread count in the `js.quartz.base.properties` configuration file by setting the property `org.quartz.threadPool.threadCount=6`.
