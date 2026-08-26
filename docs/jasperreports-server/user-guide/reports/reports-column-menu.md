---
title: Column Menu
description: "Reports that contain table components are enabled for user interactivity. Table components are defined in Jaspersoft Studio or from Ad Hoc Views. When a table is enabled for interactivity, the column..."
---

# Column Menu

Reports that contain table components are enabled for user interactivity. Table components are defined in Jaspersoft Studio or from Ad Hoc Views. When a table is enabled for interactivity, the column formatting, filtering, and sorting are managed from a menu displayed by clicking the column you want to apply changes to. These menu icons are described in [Export File Types](reports-moving-columns.md).

<table>
<caption><p>Column Formatting Icons</p></caption>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th><p>Icon</p></th>
<th><p>Name</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><img src="../assets/images/js-icon-columnOptions.png" alt="js icon columnOptions" /></p></td>
<td><p>Formatting/<br />
Show column/<br />
Hide column</p></td>
<td><p>Select <strong>Formatting</strong> to open the Format Column box.</p>
<p>Select the <strong>Show column</strong> or <strong>Hide column</strong>.</p></td>
</tr>
<tr>
<td><p><img src="../assets/images/js-icon-filter.png" alt="js icon filter" /></p></td>
<td><p>Column filters</p></td>
<td><p>Click to open the Filter column box.</p></td>
</tr>
<tr>
<td><p><img src="../assets/images/js-icon-sortAscending.png" alt="js icon sortAscending" /></p></td>
<td><p>Sort ascending</p></td>
<td><p>Click to sort fields in the selected column in ascending order.</p></td>
</tr>
<tr>
<td><p><img src="../assets/images/js-icon-sortDescending.png" alt="js icon sortDescending" /></p></td>
<td><p>Sort descending</p></td>
<td><p>Click to sort the fields in the selected column in ascending order.</p></td>
</tr>
<tr>
<td><p><img src="../assets/images/js-icon-sizer.png" alt="js icon sizer" /></p></td>
<td><p>Column size</p></td>
<td><p>Click and drag this icon to make columns wider or narrower.</p></td>
</tr>
</tbody>
</table>

# Data Snapshots

!!! info "Important"

    The features in this section may be restricted by your JasperReports Server software license. If you don't see some of the options described, your current license likely prohibits their use. Contact us to learn about your licensed features or to discuss upgrading.

Some reports have an optional data snapshot feature enabled. A data snapshot is a cached copy of the data included in a specific report. Data snapshots allow you to access a report's data (including input control settings) without having to retrieve it from the data source, which in some cases can save a significant amount of time.

When a report is opened in the Report Viewer, data is retrieved from the data snapshot. If the snapshot does not exist, then a live query is made to the data source. A snapshot is created when a report is saved from the viewer, or via the scheduler. The Report Viewer UI displays a date and time stamp that indicates when the report data was last refreshed with live source data.

!!! note

    The system administrator can enable or disable the data snapshot feature.

It should be noted that a report can have only one snapshot. For instance, if you edit and save a report that already has a snapshot associated with it, a new snapshot overwrites the previously created snapshot.

# Report Viewer Responsiveness

A responsive report adapts its output to the current size of the screen. When you open a responsive report in the Report Viewer and resize the screen, the Report Viewer lets you view the rendered report based on the screen size. If the screen size is smaller, you can see a rendered report suited for the smaller screen and so on. The response of the Report Viewer to the different screen sizes makes it responsive.

In the main JRXML of the report unit (See [Overview of a Report Unit](../repo-upload-reports/repo-report-unit.md) for more information), the following property is used to communicate to the Report Viewer that the report is responsive.

For example:

``` xml
<property name=“net.sf.jasperreports.htmlviewer.responsive.breakpoints” value=“1000, 1200"/>
```

In this example, the integer values separated by comma declares the screen size intervals. The Report Viewer reads this property when the report is run and retriggers the report to run every time the screen size changes.

When you resize the screen, the Report Viewer reruns the report with the new `REPORT_CONTAINER_WIDTH` value. `REPORT_CONTAINER_WIDTH` is a built-in parameter used to control the rendering of a certain part template.

For example: If you define three screen size intervals:

-   Smaller than 1000px

-   Between 1000px and 1200px

-   Greater than 1200px

Then, there will be three JRXML parts for each interval, and only the suited part appears for the current screen size, read from the built-in `REPORT_CONTAINER_WIDTH` parameter when the report is run.

!!! note

    If your report does not define screen size intervals, it is not considered responsive and the Report Viewer runs the report only once and will not be responsive when the screen is resized.
