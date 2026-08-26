---
title: Ad Hoc View Types
description: "The Ad Hoc Editor allows you to select from three view types:"
---

# Ad Hoc View Types

The Ad Hoc Editor allows you to select from three view types:

-   Tables , which are used to view values in the database and to summarize the values in columns.
-   Charts , which compare one or more measures across multiple sets of related fields.
-   Crosstabs , which aggregate data across multiple dimensions.

This section provides an overview of each view type. The design and content tasks for working with each type of view are discussed in more detail in the following sections:

-   For more information on table views, see .
-   For more information on chart views, see [Working with Charts](adhoc-charts.md).
-   For more information on crosstab views, see [Working with Standard Crosstabs](adhoc-crosstabs-standard.md).

## Tables

The architecture of a table view consists of columns, rows, and groups.

Columns in a table correspond to the columns in the data source. They are included by adding fields or measures to the table in the Ad Hoc view.

Rows correspond to rows in the database. The information in each row depends on what columns are included in the table.

Using groups, rows can be grouped by identical values in any field with intermediate summaries for each grouped value. For example, a table view of product orders might contain columns to show the dates and amounts of each order, and its rows might be grouped by city and product.

<table>
<thead>
<tr>
<th></th>
<th><p>Date Placed</p></th>
<th><p>Date Filled</p></th>
<th><p>Payment Received</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="4"><p><span>City A</span></p></td>
</tr>
<tr>
<td colspan="4"><p><span>Product 01</span></p></td>
</tr>
<tr>
<td></td>
<td><p>Date</p></td>
<td><p>Date</p></td>
<td><p>Amount</p></td>
</tr>
<tr>
<td></td>
<td><p>Date</p></td>
<td><p>Date</p></td>
<td><p>Amount</p></td>
</tr>
<tr>
<td><p><span>Product 01 totals:</span></p></td>
<td></td>
<td><p><span>Count</span></p></td>
<td><p><span>Sum</span></p></td>
</tr>
<tr>
<td colspan="4"><p><span>Product 02</span></p></td>
</tr>
<tr>
<td></td>
<td><p>Date</p></td>
<td><p>Date</p></td>
<td><p>Amount</p></td>
</tr>
<tr>
<td></td>
<td><p>Date</p></td>
<td><p>Date</p></td>
<td><p>Amount</p></td>
</tr>
<tr>
<td><p><span>Product 02 totals:</span></p></td>
<td></td>
<td><p><span>Count</span></p></td>
<td><p><span>Sum</span></p></td>
</tr>
<tr>
<td colspan="4"><p><span>Product 03</span></p></td>
</tr>
<tr>
<td></td>
<td><p>Date</p></td>
<td><p>Date</p></td>
<td><p>Amount</p></td>
</tr>
<tr>
<td></td>
<td><p>Date</p></td>
<td><p>Date</p></td>
<td><p>Amount</p></td>
</tr>
<tr>
<td><p><span>Product 03 totals:</span></p></td>
<td></td>
<td><p><span>Count</span></p></td>
<td><p><span>Sum</span></p></td>
</tr>
<tr>
<td><p><span>City A totals:</span></p></td>
<td></td>
<td><p><span>Count</span></p></td>
<td><p><span>Sum</span></p></td>
</tr>
<tr>
<td colspan="4"><p><span>City B</span></p></td>
</tr>
<tr>
<td colspan="4"><p><span>Product 01</span></p></td>
</tr>
<tr>
<td></td>
<td><p>Date</p></td>
<td><p>Date</p></td>
<td><p>Amount</p></td>
</tr>
<tr>
<td></td>
<td><p>Date</p></td>
<td><p>Date</p></td>
<td><p>Amount</p></td>
</tr>
<tr>
<td></td>
<td><p>Date</p></td>
<td><p>Date</p></td>
<td><p>Amount</p></td>
</tr>
<tr>
<td></td>
<td><p>...</p></td>
<td><p>...</p></td>
<td><p>...</p></td>
</tr>
</tbody>
</table>

For more information on working with tables, see [Working with Tables](adhoc-tables.md).

## Charts

Charts summarize the data graphically. Types of charts include bar chart, line chart, and pie chart, among others. With the exception of time series and scatter charts, each type of chart compares summarized values for a group. For example, the **Chart** tab might show the data in a bar chart that compared the sum of Payments Received for each of the products in each of the cities.

<table>
<tbody>
<tr>
<td colspan="3"><p>Total Payments Received</p></td>
</tr>
<tr>
<td colspan="3"><p><img src="../assets/images/js-AdHoc-ChartExample.png" alt="js AdHoc ChartExample" /></p></td>
</tr>
<tr>
<td><p><strong>City A</strong></p></td>
<td><p><strong>City B</strong></p></td>
<td><p><strong>City C</strong></p></td>
</tr>
<tr>
<td colspan="3"><p><img src="../assets/images/js-AdHoc-ChartExample-legend.png" alt="js AdHoc ChartExample legend" /></p></td>
</tr>
</tbody>
</table>

Time series and scatter charts use time intervals to group data.

For more information on working with charts, see [Working with Charts](adhoc-charts.md).

## Crosstabs

Crosstabs are more compact representations than tables. They show only aggregate values, rather than individual database values. Columns and rows specify the dimensions for grouping. Cells contain the summarized measurements. For instance, the example above could be displayed in a crosstab with columns grouped by sales manager and year.

<table>
<tbody>
<tr>
<td colspan="2" rowspan="2"></td>
<td colspan="3"><p><span>Tom</span></p></td>
<td colspan="3"><p><span>Harriet</span></p></td>
<td rowspan="2"><p><span>Manager Totals</span></p></td>
</tr>
<tr>
<td><p><span>2012</span></p></td>
<td><p><span>2013</span></p></td>
<td><p><span>Year Totals</span></p></td>
<td><p><span>2012</span></p></td>
<td><p><span>2013</span></p></td>
<td><p><span>Year Totals</span></p></td>
</tr>
<tr>
<td rowspan="4"><p><span>City A</span></p></td>
<td><p><span>Product 01</span></p></td>
<td><p>Payment Received</p></td>
<td><p>Payment Received</p></td>
<td><p><span>Payment Received</span></p></td>
<td><p>Payment Received</p></td>
<td><p>Payment Received</p></td>
<td><p><span>Payment Received</span></p></td>
<td><p><span>Payment Received</span></p></td>
</tr>
<tr>
<td><p><span>Product 02</span></p></td>
<td><p>Payment Received</p></td>
<td><p>Payment Received</p></td>
<td><p><span>Payment Received</span></p></td>
<td><p>Payment Received</p></td>
<td><p>Payment Received</p></td>
<td><p><span>Payment Received</span></p></td>
<td><p><span>Payment Received</span></p></td>
</tr>
<tr>
<td><p><span>Product 03</span></p></td>
<td><p>Payment Received</p></td>
<td><p>Payment Received</p></td>
<td><p><span>Payment Received</span></p></td>
<td><p>Payment Received</p></td>
<td><p>Payment Received</p></td>
<td><p><span>Payment Received</span></p></td>
<td><p><span>Payment Received</span></p></td>
</tr>
<tr>
<td><p><span>Product Totals</span></p></td>
<td><p><span>Payment Received</span></p></td>
<td><p><span>Payment Received</span></p></td>
<td><p><span>Payment Received</span></p></td>
<td><p><span>Payment Received</span></p></td>
<td><p><span>Payment Received</span></p></td>
<td><p><span>Payment Received</span></p></td>
<td><p><span>Payment Received</span></p></td>
</tr>
<tr>
<td rowspan="2"><p><span>City B</span></p></td>
<td><p><span>Product 01</span></p></td>
<td><p>Payment Received</p></td>
<td><p>Payment Received</p></td>
<td><p><span>Payment Received</span></p></td>
<td><p>Payment Received</p></td>
<td><p>Payment Received</p></td>
<td><p><span>Payment Received</span></p></td>
<td><p><span>Payment Received</span></p></td>
</tr>
<tr>
<td><p><span>...</span></p></td>
<td><p>...</p></td>
<td><p>...</p></td>
<td><p><span>...</span></p></td>
<td><p>...</p></td>
<td><p>...</p></td>
<td><p><span>...</span></p></td>
<td><p><span>...</span></p></td>
</tr>
<tr>
<td colspan="2"><p><span>City Totals</span></p></td>
<td><p><span>Payment Received</span></p></td>
<td><p><span>Payment Received</span></p></td>
<td><p><span>Payment Received</span></p></td>
<td><p><span>Payment Received</span></p></td>
<td><p><span>Payment Received</span></p></td>
<td><p><span>Payment Received</span></p></td>
<td><p><span>Payment Received</span></p></td>
</tr>
</tbody>
</table>

For more information on working with crosstabs, see [Working with Standard Crosstabs](adhoc-crosstabs-standard.md).

OLAP connection-based crosstabs behave differently than those created from Topics or Domains. See [Creating Topics](adhoc-topics.md).
