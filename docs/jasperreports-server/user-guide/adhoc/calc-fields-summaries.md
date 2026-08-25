---
title: Summary Calculations
description: Summary calculations are aggregate functions used for sub-totals and totals. Summary calculations can be set in the Domain Designer or in the Ad Hoc view.
---

# Summary Calculations

Summary calculations are aggregate functions used for sub-totals and totals. Summary calculations can be set in the Domain Designer or in the Ad Hoc view.

- In Ad Hoc table views, each field can display a single summary calculation. The summary calculation is automatically applied to all groups in the table. Summaries appear at the bottom of each group, as well as at the bottom of the view. When a new group is added, it includes a summary for each column.

- In crosstabs, each measure displays a summarized value. Summaries determine the values of the Totals at the intersection of each row and column.

- In charts, the type of chart determines whether measures are summarized. If summaries are used, they determine the size or location of the graphical elements that represent your data.

  <div class="admonition note">
  <p class="admonition-title">Note</p>
  <p>For dual pie charts, the summary function for the field needs to be Sum or CountAll. Dual pie charts with other summary functions may give unexpected results.</p>
  </div>

In general, you can change the summary calculation of any measure. By default, JasperReports Server summarizes fields of each datatype as shown in the following table.

| Datatype | Default Summary Calculation | Description |
|----|----|----|
| Numeric | Sum | Displays the sum of all values in the set. |
| Date | CountAll | Displays the total number of values in the set. |
| String | CountAll | Displays the number of values in the set. |
| Boolean | CountAll | Displays the number of values in the set. |
| Aggregate | Aggregate Formula | For a calculated field that uses an aggregate function, uses the same aggregate formula as the summary. |
| Combined | None | For a calculated field that combines an aggregate function with a non-aggregate function, the summary calculation is null. |

Default Summary Functions in Calculated Fields

Select from the following options to set a measure’s summary function in any type of view.

| Function | Meaning | Available for…. |
|----|----|----|
| Aggregate Formula | For a calculation that uses an aggregate function, uses the same aggregate formula as the summary. | Aggregate |
| Average | Displays the average of all values in the set. | Numeric |
| CountAll | Displays the number of rows in the set. | Boolean, Date, Numeric, and String |
| CountDistinct | Displays the number of unique values in the set. | Boolean, Date, Numeric, and String |
| Custom | Allows you to enter an aggregate calculation for the summary. Only available for calculated fields and measures in the Ad Hoc Editor; not available for Domains. | Aggregate, Date, Numeric |
| Maximum | Displays the highest value in the set. | Date, Numeric |
| Median | Displays the median value of the set. | Date, Numeric |
| Minimum | Displays the lowest value in the set. | Date, Numeric |
| Mode | Displays the value that occurs most frequently in the set. | Boolean, Date, Numeric, and String |
| None | The aggregate function is null; no summary function is displayed. | Aggregate, Boolean, Date, Numeric, and String |
| Range | Displays the difference between the minimum and maximum values of the set. | Numeric |
| RangeDays | Displays the difference in days between the minimum and maximum values of the set. | Date |
| RangeHours | Displays the difference in hours between the minimum and maximum values of the set. | DateTime |
| RangeMinutes | Displays the difference in minutes between the minimum and maximum values of the set. | DateTime |
| RangeMonths | Displays the difference in months between the minimum and maximum values of the set. | Date |
| RangeQuarters | Displays the difference in quarters between the minimum and maximum values of the set. | Date |
| RangeSemis | Displays the difference in semi-annual periods between the minimum and maximum values of the set. | Date |
| RangeWeeks | Displays the difference in weeks between the minimum and maximum values of the set. | Date |
| RangeYears | Displays the difference in years between the minimum and maximum values of the set. | Date |
| Standard Deviation P | Displays the standard deviation for the population of the set. | Numeric |
| Standard Deviation S | Displays the standard deviation on a sample for the set. | Numeric |
| Sum | Displays the grand total for the set. | Numeric |
| WeightedAverage | Displays the weighted average for the set, based on a second numeric field or expression. Only available for calculated fields and measures in the Ad Hoc Editor; not available for Domains. | Numeric |

Note the following about summaries:

- If you select a summary calculation other than the default, that calculation is shown in parentheses after the field name in the fields picker.

- In Ad Hoc views, you see special behavior when you create a calculated field or measure with the following type of summary calculation:

  - If you create a Custom summary calculation for a field or measure, **Custom** is available on the **Change Summary Calculation** menu for that field. It is not available otherwise.
  - If you create a WeightedAverage summary calculation for a field or measure, **WeightedAverage** is available on the **Change Summary Calculation** menu for that field. It is not available otherwise.

- You can remove summaries by setting the summary function to **None**.

- Only AggregateFormula, Custom, or None are supported as summary calculations for aggregate functions. Custom only appears in the **Change Summary** right-click menu if you have defined a custom function in the **Create Calculated Field** dialog box.
