---
title: Overview of HTML5 Charts
description: "HTML5 charts are a flexible, interactive way to explore your data graphically. You can choose different levels of aggregation for rows and columns and create attractive interactive reports."
---

# Overview of HTML5 Charts

HTML5 charts are a flexible, interactive way to explore your data graphically. You can choose different levels of aggregation for rows and columns and create attractive interactive reports.

The following terminologies are used to describe HTML5 charts:

-   **Values**: Static properties.

-   **Expressions**: Dynamic properties.

-   **Categories**: Rows. In a pie chart, the categories are the slices.

-   **Levels**: Some chart types let you add multiple categories or series ranked hierarchically, with the topmost category set as Level 1. When you export a chart with multiple levels to JasperReports Server, users see a slider that they can use to select the level of aggregation. For example, you might have a chart that has three categories — Country, Region, and City — and users can choose a level for viewing the data.

-   **Measures**: Measures contain summarized values. They are typically numeric fields that determine the length of bars, size of pie slices, location of points (in line charts), or the height of areas.

-   **Series Contributors**: In the Design tab, these are defined at the measure level. In JRXML, these are defined as Series.

!!! note

    In HTML5 Charts, Jaspersoft Studio are similar to Ad Hoc charts in JasperReports Server.

Before you add a chart to your report, consider the best way to display your data. The following table describes the available chart types.

**HTML5 Chart Types**

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>Icon</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p>Column charts - Compare values displayed as columns</p></td>
</tr>
<tr>
<td><p><img src="../assets/images/column-icon.png" alt="column icon" /></p></td>
<td><p><strong>Column</strong>. Multiple measures of a group are depicted as individual columns.</p></td>
</tr>
<tr>
<td><p><img src="../assets/images/jss-icon-html5-stacked-column.png" alt="jss icon html5 stacked column" /></p></td>
<td><p><strong>Stacked Column</strong>. Multiple measures of a group are depicted as portions of a single column whose size reflects the aggregate value of the group.</p></td>
</tr>
<tr>
<td><p><img src="../assets/images/jss-html5-charts-column-percent.png" alt="jss html5 charts column percent" /></p></td>
<td><p><strong>Percent Column</strong>. Multiple measures of a group are depicted as portions of a single column of fixed size representing 100% of the amounts for a category. Used when you have three or more data series and want to compare distributions within categories and at the same time display the differences between categories.</p></td>
</tr>
<tr>
<td colspan="2"><p>Bar charts - Compare values displayed as bars</p></td>
</tr>
<tr>
<td><p><img src="../assets/images/jss-html5-charts-bar.png" alt="jss html5 charts bar" /></p></td>
<td><p><strong>Bar</strong>. Graphically summarize and display categories of data to let users easily compare amounts or values among categories.</p></td>
</tr>
<tr>
<td><p><img src="../assets/images/jss-html5-icon-stacked-bar.png" alt="jss html5 icon stacked bar" /></p></td>
<td><p><strong>Stacked Bar</strong>. Multiple measures of a group are depicted as portions of a single bar whose size reflects the aggregate value of the group.</p></td>
</tr>
<tr>
<td><p><img src="../assets/images/jss-html5-icon-stacked-percent-bar.png" alt="jss html5 icon stacked percent bar" /></p></td>
<td><p><strong>Percent Bar</strong>. Multiple measures of a group are depicted as portions of a single bar of fixed size representing 100% of the amounts for a category. Used when you have three or more data series and want to compare distributions within categories and at the same time display the differences between categories.</p></td>
</tr>
<tr>
<td colspan="2"><p>Line charts - Compare values displayed as points connected by lines</p></td>
</tr>
<tr>
<td><p><img src="../assets/images/15_22.jpg" alt="15 22" /></p></td>
<td><p><strong>Line</strong>. Displays data points connected with straight lines, typically to show trends.</p></td>
</tr>
<tr>
<td><p><img src="../assets/images/15_23.jpg" alt="15 23" /></p></td>
<td><p><strong>Spline</strong>. Displays data points connected with a fitted curve. Allow you to take a limited set of known data points and approximate intervening values.</p></td>
</tr>
<tr>
<td><p><img src="../assets/images/15_24.jpg" alt="15 24" /></p></td>
<td><p><strong>Stacked Line</strong>. Displays a series as a set of points connected by a line. Values are represented on the y-axis and categories are displayed on the x-axis. Lines do not overlap because they are cumulative at each point.</p></td>
</tr>
<tr>
<td><p><img src="../assets/images/stackedSpline-icon.png" alt="stackedSpline icon" /></p></td>
<td><p><strong>Stacked Spline</strong>. Displays a series as a set of points connected with a fitted curve. Values are represented on the y-axis and categories are displayed on the x-axis. Lines do not overlap because they are cumulative at each point</p></td>
</tr>
<tr>
<td><p><img src="../assets/images/percentLine-icon.png" alt="percentLine icon" /></p></td>
<td><p><strong>Stacked Percent Line</strong>. A variation of a line chart in which each series adjoins but does not overlap the preceding series.</p></td>
</tr>
<tr>
<td><p><img src="../assets/images/percentSpline-icon.png" alt="percentSpline icon" /></p></td>
<td><p><strong>Stacked Percent Spline</strong>. A variation of a spline chart in which each series adjoins but does not overlap the preceding series.</p></td>
</tr>
<tr>
<td colspan="2"><p>Area charts - Compare values displayed as shaded areas. Compared to line charts, area charts emphasize quantities rather than trends.</p></td>
</tr>
<tr>
<td><p><img src="../assets/images/15_25.jpg" alt="15 25" /></p></td>
<td><p><strong>Area</strong>. Displays data points connected with a straight line and a color below the line. Groups are displayed as transparent overlays.</p></td>
</tr>
<tr>
<td><p><img src="../assets/images/15_26.jpg" alt="15 26" /></p></td>
<td><p><strong>Stacked Area</strong>. Displays data points connected with a straight line and a solid color below the line. Groups are displayed as solid areas arranged vertically, one on top of another.</p></td>
</tr>
<tr>
<td><p><img src="../assets/images/15_27.jpg" alt="15 27" /></p></td>
<td><p><strong>Stacked Percent Area</strong>. Displays data points connected with a straight line and a solid color below the line. Groups are displayed as portions of an area of fixed size, and arranged vertically one on top of each other.</p></td>
</tr>
<tr>
<td><p><img src="../assets/images/jss-icon-html5-area-spline.png" alt="jss icon html5 area spline" /></p></td>
<td><p><strong>Area Spline</strong>. Displays data points connected with a fitted curve and a color below the line. Groups are displayed as transparent overlays.</p></td>
</tr>
<tr>
<td><p><img src="../assets/images/15_29.jpg" alt="15 29" /></p></td>
<td><p><strong>Stacked Area Spline</strong>. Displays a series as a set of points connected by a smooth line with the area below the line filled in. Values are represented on the y-axis and categories are displayed on the x-axis. Areas do not overlap because they are cumulative at each point.</p></td>
</tr>
<tr>
<td><p><img src="../assets/images/percentAreaSpline-icon.png" alt="percentAreaSpline icon" /></p></td>
<td><p><strong>Stacked Percent Area Spline</strong>. A variation of area spline charts that present values as trends for percentages, totaling 100% for each category.</p></td>
</tr>
<tr>
<td colspan="2"><p>Pie charts - Compare values displayed as slices of a circular graph</p></td>
</tr>
<tr>
<td><p><img src="../assets/images/15_30.jpg" alt="15 30" /></p></td>
<td><p><strong>Pie</strong>. Multiple items of a single group are displayed as sectors of a circle.</p></td>
</tr>
<tr>
<td><img src="../assets/images/jss-html5-chart-dualLevelPie.png" alt="jss html5 chart dualLevelPie" /></td>
<td><p><strong>Dual-Level Pie</strong>. A variation of pie charts that present the grouped values in two concentric circles. The inner circle represents the coarsest grouping level in the data. In Jaspersoft Studio, note these rules about data configuration for dual-level pie charts:</p>
<ul>
<li>Only one measure is displayed (the first)</li>
<li>The last row level is rendered as the outer pie</li>
<li>The next to the last row level is rendered as the inner pie. If only one row level is defined, the inner pie consists of a single section representing the total</li>
</ul></td>
</tr>
<tr>
<td><img src="../assets/images/jss-icon-html5-semi-pie.png" alt="jss icon html5 semi pie" /></td>
<td><strong>Semi-Pie</strong>. Multiple measures of a group are displayed as sectors of a half-circle.</td>
</tr>
<tr>
<td colspan="2"><p>Scatter and Bubble Charts - Show the extent of correlation, if any, between the values of observed quantities.</p></td>
</tr>
<tr>
<td><p><img src="../assets/images/scatter-icon.png" alt="scatter icon" /></p></td>
<td><p><strong>Scatter</strong>. Displays a single point for each point in a data series without connecting the points.</p></td>
</tr>
<tr>
<td><img src="../assets/images/jss-html5-chart-bubble.png" alt="jss html5 chart bubble" /></td>
<td><p><strong>Bubble</strong>. Compares the relationships between the three measures displayed on the x-y axis. The location and size of each bubble indicates the relative values of each data point.</p></td>
</tr>
<tr>
<td colspan="2"><p>Multi-Axis Charts - Compare trends in two or more data sets whose numeric range differs greatly.</p></td>
</tr>
<tr>
<td><p><img src="../assets/images/multiAxisColumn-icon.png" alt="multiAxisColumn icon" /></p></td>
<td><p><strong>Multi-Axis Column</strong>. A column chart with two series and two axis ranges.</p></td>
</tr>
<tr>
<td><p><img src="../assets/images/multiAxisLine-icon.png" alt="multiAxisLine icon" /></p></td>
<td><p><strong>Multi-Axis Line</strong>. A line chart with two series and two axis ranges.</p></td>
</tr>
<tr>
<td><p><img src="../assets/images/multiAxisSpline-icon.png" alt="multiAxisSpline icon" /></p></td>
<td><p><strong>Multi-Axis Spline</strong>. A spline chart with two series and two axis ranges.</p></td>
</tr>
<tr>
<td colspan="2"><p>Combination Charts - Display multiple data series in a single chart, combining the features of an area, bar, column, or line charts.</p></td>
</tr>
<tr>
<td><p><img src="../assets/images/columnLine-icon.png" alt="columnLine icon" /></p></td>
<td><p><strong>Column Line</strong>. Combines the features of a column chart with a line chart.</p></td>
</tr>
<tr>
<td><p><img src="../assets/images/columnSpline-icon.png" alt="columnSpline icon" /></p></td>
<td><p><strong>Column Spline</strong>. Combines the features of a column chart with a spline chart.</p></td>
</tr>
<tr>
<td><p><img src="../assets/images/stackedColumnLine-icon.png" alt="stackedColumnLine icon" /></p></td>
<td><p><strong>Stacked Column Line</strong>. Combines the features of a stacked column chart with a line chart.</p></td>
</tr>
<tr>
<td><p><img src="../assets/images/stackedColumnSpline-icon.png" alt="stackedColumnSpline icon" /></p></td>
<td><p><strong>Stacked Column Spline</strong>. Combines the features of a stacked column chart with a line chart.</p></td>
</tr>
<tr>
<td colspan="2"><p>Time Series Charts - Illustrate data points at successive time intervals. Also called Fever Chart.</p></td>
</tr>
<tr>
<td><p><img src="../assets/images/timeSeriesArea-icon.png" alt="timeSeriesArea icon" /></p></td>
<td><p><strong>Time Series Area</strong>. Displays data points over time connected with a straight line and a color below the line.</p></td>
</tr>
<tr>
<td><p><img src="../assets/images/timeSeriesAreaSpline-icon.png" alt="timeSeriesAreaSpline icon" /></p></td>
<td><p><strong>Time Series Area Spline</strong>. Displays data points over time connected with a fitted curve and a color below the line.</p></td>
</tr>
<tr>
<td><p><img src="../assets/images/timeSeriesLine-icon.png" alt="timeSeriesLine icon" /></p></td>
<td><p><strong>Time Series Line</strong>. Displays data points over time connected with straight lines.</p></td>
</tr>
<tr>
<td><p><img src="../assets/images/timeSeriesSpline-icon.png" alt="timeSeriesSpline icon" /></p></td>
<td><p><strong>Time Series Spline</strong>. Displays data points over time connected with a fitted curve.</p></td>
</tr>
<tr>
<td colspan="2"><p>Spider Charts - Display data in line or data bars arranged on a circular spider web chart. It is also called a Radar Chart.</p></td>
</tr>
<tr>
<td><img src="../assets/images/jss-html5-chart-spiderColumn.png" alt="jss html5 chart spiderColumn" /></td>
<td><p><strong>Spider Column</strong>. Plots one or more series over multiple common quantitative variables by providing axes for each variable arranged as spokes around a central point. The column variation of spider charts displays values as bars that extend out from the central point towards the edges of the circular web. The bar's length indicates the relative value.</p></td>
</tr>
<tr>
<td><img src="../assets/images/jss-html5-chart-spiderLine.png" alt="jss html5 chart spiderLine" /></td>
<td><p><strong>Spider Line</strong>. Plots one or more series over multiple common quantitative variables by providing axes for each variable arranged as spokes around a central point. The line variation of spider charts displays values as points arranged around the circular web. The data points are joined by a line. Each point's distance from the central point indicates the relative value.</p></td>
</tr>
<tr>
<td><img src="../assets/images/jss-html5-chart-spiderArea.png" alt="jss html5 chart spiderArea" /></td>
<td><p><strong>Spider Area</strong>. Plots one or more series over multiple common quantitative variables by providing axes for each variable arranged as spokes around a central point. The area variation of spider charts is similar to the line variation, but the shape defined by the line that connects each series' points is filled with color.</p></td>
</tr>
<tr>
<td colspan="2">Range Charts</td>
</tr>
<tr>
<td><img src="../assets/images/jss-icon-heatmap.png" alt="jss icon heatmap" /></td>
<td><strong>Heat Map</strong>. Represents data in a matrix format, using color coding to show values.</td>
</tr>
<tr>
<td><img src="../assets/images/jss-icon-html5-heatmap-timeseries.png" alt="jss icon html5 heatmap timeseries" /></td>
<td><strong>Time Series Heat Map</strong>. Represents data across time in a heat map, using color coding to show values.</td>
</tr>
<tr>
<td><img src="../assets/images/jss-icon-html5-dual-measure-tree.png" alt="jss icon html5 dual measure tree" /></td>
<td><strong>Dual Measure Tree Map</strong>. Displays data as color-coded rectangles. The size of each rectangle is proportional to the first measure and the color represents the second measure.</td>
</tr>
<tr>
<td><img src="../assets/images/jss-icon-html5-tree.png" alt="jss icon html5 tree" /></td>
<td><strong>Tree Map.</strong> Displays data as rectangles. The size of each rectangle is proportional to the measure of the data it represents. The tree map displays nested rectangles when you have more than one field. The parent rectangle represents the leftmost measure while the nested rectangles represent the current level of aggregation. Click on a parent rectangle to drill down to the nest rectangles.</td>
</tr>
<tr>
<td><img src="../assets/images/jss-icon-html5-one-parent-tree.png" alt="jss icon html5 one parent tree" /></td>
<td><strong>One Parent Tree Map</strong>. Displays data as nested rectangles. The size of each rectangle is proportional to the measure of the data it represents. The nested rectangles represent the current level of aggregation while the larger rectangle represents the parent level in the hierarchy. Click a parent rectangle to drill down to the nest rectangles.</td>
</tr>
<tr>
<td><img src="../assets/images/jss-tiles-icon.png" alt="jss tiles icon" /></td>
<td><strong>Tile Map.</strong> Displays data in the form of tiles aligned on a grid to create a pattern. The related data measure is displayed on each tile.</td>
</tr>
<tr>
<td colspan="2">Gauge Charts</td>
</tr>
<tr>
<td><img src="../assets/images/jss-chart-gauge.png" alt="jss chart gauge" /></td>
<td><p><strong>Gauge</strong>. Displays a single data value as a portion of a circle. The length of the circle is the data's numeric value proportional to the maximum size defined for the measure.</p>
<ul>
<li>One or more Measures required in the Columns location.</li>
<li>One or more Fields required in the Columns location.</li>
<li>Define the minimum and maximum sizes, color stops, and layout on the Appearance tab.</li>
</ul></td>
</tr>
<tr>
<td><img src="../assets/images/jss-chart-multilevel-gauge.png" alt="jss chart multilevel gauge" /></td>
<td><p><strong>Multi-level Gauge</strong>. Displays one or more data values as concentric circles. Each circle represents a measure and the length of the circle is the data's numeric value proportional to the maximum size defined for the measures.</p>
<ul>
<li>Two or more Measures required in the Columns location.</li>
<li>One or more Fields required in the Columns location.</li>
<li>Define the minimum and maximum sizes, color stops, and layout on the Appearance tab.</li>
</ul></td>
</tr>
<tr>
<td><img src="../assets/images/jss-gaugeArc.png" alt="jss gaugeArc" /></td>
<td><p><strong>Arc Gauge</strong>. Displays a single data value as a portion of a semi-circular arc. The length of the arc is the data's value proportional to the maximum size defined for the measure.</p>
<ul>
<li>One or more Measures required in the Columns location.</li>
<li>One or more Fields required in the Rows location.</li>
<li>Define the minimum and maximum sizes, color stops, and layout on the Appearance tab.</li>
</ul></td>
</tr>
</tbody>
</table>
