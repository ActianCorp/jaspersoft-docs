---
title: JasperReports Server Alerts Feature
description: "The features in this section may be restricted by your JasperReports Server software license. If you don't see some of the options described, your current license likely prohibits their use. Contact..."
---

# JasperReports Server Alerts Feature

!!! info "Important"

    The features in this section may be restricted by your JasperReports Server software license. If you don't see some of the options described, your current license likely prohibits their use. Contact us to learn about your licensed features or to discuss upgrading.

You can use this feature to set alerts for reports from the Reports Viewer toolbar. Currently this feature is only available for the **Tables** and the **Crosstabs**. Alerts notify you when the specified Condition is met. You can create alerts to monitor the data and to notify yourself when there is any significant change in the data.

For creating an alert, you must click the Turn on alert mode icon ![js alert add icon](../assets/images/js-alert-add-icon.png) on the toolbar. This enables the numeric fields or data points of the report for creating alerts. When creating an alert, you must specify the condition for which alerts have to be generated. The alerting feature is dependent on the Threshold, Data point, and Condition set while creating an alert. You get notified via an email for an alert when the specified Condition matches the Threshold value.

You can view a list of alerts on the **Manage &gt; Admin Console &gt; Alerts** tab.

This chapter contains the following sections:

-   Alert Overview
-   [Creating an Alert](create-alert.md)
-   [Viewing the List of Alerts](alerts-list.md)
-   [Searching an Alert](alerts-list.md)
-   [Editing an Alert](alerts-list.md)
-   [Deleting an Alert](alerts-list.md)

## Alert Overview

By using the alert feature, you can set up an alert for the following tabs:

-   **Condition** - Which condition an alert is using to notify you about the alert. You can customize the condition based on the available options.
-   **Parameters** - Which input controls are applied on the report. When a report has no input controls, then the Parameters tab is disabled.
-   **Schedule** - Which recurrence and start time for the alert is to be set to schedule the alert and get notified.
-   **Notifications** - The email options to send alert notifications along with subject and message to the recipients for an alert.
-   **Output** - The name of the output file, output format, and time zone.

### Sample Use case to Generate an Alert

For example, consider that you are working in a warehouse. You have to restock the inventory based on the storage space. A report is generated that shows the inventory for the products. You have to check the stock twice a day to maintain the inventory value. If the inventory falls below 100 units, then new items must be ordered.

In this scenario, your data point is the inventory values, the threshold limit is 100, and the condition is when the inventory value is less than 100 units.

To generate an alert:

1.  Turn on the alert mode to enable the inventory values.
2.  Click any inventory number. This is your data point.
3.  Select an inventory number to create an alert.

An email is sent to the user if any of the Inventory values meets the conditions set in the alert.

As shown in the following table, only individual inventory values are considered for checking the conditions set for generating an alert and not the total values.

| Product | Country | Warehouse | Inventory |
|---------|---------|-----------|-----------|
| iPhone  | US      | NYC-1     | 120       |
| iPhone  | US      | NYC-2     | 300       |
| iPhone  | Canada  | TOR-1     | 250       |
| iPhone  | Canada  | TOR-2     | 50        |
| iPad    | US      | NYC-1     | 200       |
| iPad    | US      | NYC-2     | 70        |
| Total   |         |           | 990       |
