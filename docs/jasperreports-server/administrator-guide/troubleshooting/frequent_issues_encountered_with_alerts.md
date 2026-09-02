---
title: Frequent Issues Encountered with Alerts
description: This section includes the list of common troubleshooting scenarios that might occur when an alert is set on the report but the user does not receive any email notification.
---

# Frequent Issues Encountered with Alerts

This section includes the list of common troubleshooting scenarios that might occur when an alert is set on the report but the user does not receive any email notification.

-   [Alert fails to trigger when the data source is modified](#alert-fails-to-trigger-when-the-data-source-is-modified)
-   [Alert fails to trigger when measure is edited from the domain designer](#alert-fails-to-trigger-when-the-measure-is-edited-from-the-domain-designer)
-   [Alert fails to trigger when the visualization type is changed](#alert-fails-to-trigger-when-the-visualization-type-is-changed)
-   [Alert fails to trigger when data mode is changed](#alert-fails-to-trigger-when-data-mode-is-changed)
-   [Alert fails to trigger when the summary function is removed](#alert-fails-to-trigger-when-the-summary-function-is-removed)
-   [Alert fails to trigger when a user is disabled](#alert-fails-to-trigger-when-a-user-is-disabled)

## Alert fails to trigger when the data source is modified

The alert is not triggered when the data source is modified for the report on which the alert is set. To receive an alert notification, it is necessary to fix the data source connection back to the correct values.

For more information, see [Data Sources](../datasources/datasources_intro.md) section in JasperReports® Server Administrator Guide.

## Alert fails to trigger when the measure is edited from the domain designer

The alert is not triggered when the report measures are modified on which alert is set from the domain designer. To receive an alert notification, the user must edit the domain and change back the report measure value to its original value and re-save it.

For more information, see the *Working with the domain designer* section in the JasperReports® Server Data Management Using Domains Guide.

## Alert fails to trigger when the visualization type is changed

The alert is not triggered when the visualization type is changed to a different type (for example, changing from Table report to Crosstabs report) for which the user has set an alert. To receive an alert notification, the visualization type must be changed back to its original setting, which is the visualization type on which the alert was initially set.

For more information, see *The Visualization Selector* section in JasperReports® Server User Guide.

## Alert fails to trigger when data mode is changed

The alert is not triggered when the data mode is changed to a different mode. For example, if an alert is set for the Totals value of a column in a table report, and the user changes the Data Detail mode to Details. To receive alert notifications, the Data Detail mode must be changed back to its original value that is, Totals value on which the alert was initially set or edit the same alert to a new threshold value.

For more information on users, see *Controlling the Data Set* section in JasperReports® Server User Guide.

## Alert fails to trigger when the summary function is removed

The alert is not triggered when summary data is removed. For example, if an alert is set up based on a summary function to obtain the Totals value of a column in the report, and the user removes the summary function. To receive alert notifications, the summary function must be changed back to its original setting, the type on which the alert was initially set, or edit the same alert to the new threshold value.

To add or remove data summaries from all columns, see the *Summaries* section in JasperReports® Server User Guide.

## Alert fails to trigger when a user is disabled

The alert is not triggered when a user profile of a user who has set an alert is disabled. To re-enable the user profile on the **Admin Home** page, click **Manage &gt; Users**.

For more information on users, see [Managing Users](../management/managing_users.md) section in JasperReports® Server Administrator Guide.
