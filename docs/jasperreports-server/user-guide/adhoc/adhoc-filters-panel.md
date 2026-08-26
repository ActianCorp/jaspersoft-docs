---
title: The Filters Panel
description: "The Filters panel displays any filters defined for the view. You can set the filter values and see the resulting change in the Ad Hoc View panel. To minimize the Filters panel, click the &gt; button..."
---

# The Filters Panel

The Filters panel displays any filters defined for the view. You can set the filter values and see the resulting change in the Ad Hoc View panel. To minimize the Filters panel, click the **&gt;** button in the top left corner of the panel. Click the **&lt;**  button on the minimized panel to expand it again.

For more information on working with filters, see [Using Filters and Input Controls](adhoc-filters-and-input-controls.md).

# Saving an Ad Hoc View, Previewing and Creating a Report

After you create a compelling table, chart, or crosstab, you can save the view in the repository for future use.

To save an Ad Hoc view

1.  Hover your mouse over ![js AdHoc SaveReport](../assets/images/js-AdHoc-SaveReport.png).
2.  Select **Save Ad Hoc View**or **Save Ad Hoc View As**.
3.  Name the view as needed, and click **Save**. The view is saved in the repository.

You can also save an Ad Hoc view as a report. Typically, a report is created when you want to:

-   See data in the interactive Report Viewer.

-   Perform additional formatting of the table data.

-   Embed the data content in a dashboard.

Create a report from the view by selecting **Save Ad Hoc View and Create Report**; you can also create and run a report directly from the repository. For more information, see [Running or Creating a Simple Report](../reports/reports-running-simple.md). When you run the report, it is displayed as a JasperReport.

To preview an Ad Hoc view

-   Click the **Editing** button and select **Viewing**.

To switch to the design mode from the preview (display mode)

-   Click the **Viewing** button and select **Editing**.

## Dependent Reports

When you create a report from an Ad Hoc view, the report is considered “dependent” on that view.

When you save an Ad Hoc view, some, but not all, of its changes appear in its dependent reports. For example, if you open an Ad Hoc view with a table and adjust the data level for its columns, the column changes show up in previous reports created from that view.

In cases where changes to an Ad Hoc view could cause errors in dependent reports, you should save the updated view with a different file name and create a new report.

# Updating Ad Hoc Reports

The Ad Hoc Designer **Save Ad Hoc View and Create Report** option in the tool bar creates an Ad Hoc report unit. In the report unit, the main JRXML is a reference to a JRXML template and contains an Ad Hoc component in it. Therefore there is no longer a copy of that style template.

The new Ad Hoc reports reference an external report template (JRXML) means that changes in the reusable template get reflected to all Ad Hoc report units.

Also, unlike older Ad Hoc reports, the styles are not copied into every report unit and they are referenced externally using a style template file (JRTX). It means that changing the styling of all Ad Hoc reports is as easy as modifying the reference style template.

Ad Hoc report units are just simple report units that use the Ad Hoc view as data source and reference one of the new Ad Hoc report templates under `/public/templates` as a main JRXML.

![Ad hoc view data source](../assets/images/Ad%20hoc%20view-data%20source.png)

*Figure 1: Ad Hoc View as Data Source*

The default template can be changed if needed by modifying the `defaultTemplateUri` property of the `reportGeneratorDefaultConf` bean in the `applicationContext-adhoc.xml` Spring configuration file.

## Impact of JIVE Changes

The report having JIVE changes saved in the Report Viewer remain unchanged after the Ad Hoc view changes. The report behaves like an old Ad Hoc report that means it does not even break because of incompatible changes made in the view. For example, you sort the column of a table and save the dependent report and then you add a column to Ad Hoc View in the Ad Hoc Designer.

This result into an Ad Hoc report with a sorted column and a column added to the Ad Hoc view is not reflected to the same Ad Hoc report.

You can also revert the JIVE saved report to the dynamic state offered by the Ad Hoc component. To do so, edit the report unit and remove the internal resource called `adhoc.jrxml`, which contains the JIVE saved state.

Also, the JIVE save operation makes a copy of the main JRXML into the report unit. You can replace this JIVE made copy with an external JRXML reference that points to the original Ad Hoc report template from the `/public/templates` folder.
