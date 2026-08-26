---
title: Ad Hoc Dimensions Too Large
description: A column or row dimension in an Ad Hoc crosstab is the equivalent of a row group in an Ad Hoc table. The members of a dimension or group are the unique values used to aggregate the data. Some...
---

# Ad Hoc Dimensions Too Large

A column or row dimension in an Ad Hoc crosstab is the equivalent of a row group in an Ad Hoc table. The members of a dimension or group are the unique values used to aggregate the data. Some dimensions and groups can have hundreds or thousands of members. Even if the dimensions are collapsed, the internal engine must calculate and store the values for all dimension members and all cells.

Some datasets contain fields that make huge dimensions on the order of tens of thousands or hundreds of thousands of members. These fields are usually meant to be filtered. But if they are inserted into the crosstab before filtering or by accident, they trigger a large database operation and a large processing load in the Ad Hoc Editor. To limit this impact, you can configure a limit to the number of members in any dimension.

The internal process that calculates groups, dimensions, and members are called the `categorizer`. Change the following settings to reduce this limit and avoid performance issues with large cardinality dimensions.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>Reducing the Size Limit for Ad Hoc Dimensions</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>.../WEB-INF/applicationContext-catFactory.xml</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Bean</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>maxMembers</code><br />
</p></td>
<td><p><code>baseCategorizer</code><br />
<br />
</p></td>
<td><p>By default, the limit is set to 100,000 members per dimension. When the limit is reached, all other members are grouped in a member named "Other". Set this property to a lower value based on your typical data and reporting needs.</p></td>
</tr>
</tbody>
</table>

In addition, dimensions and groups may be nested on several levels, for example Country, Province, and City. If your row data has 100 countries, and each country has 10 provinces, and each province has 10 cities or towns, there will be 100 x 10 x 10 = 10,000 rows in your full crosstab. If you also have two column dimension, each with 10 members, there will be 100 columns in your crosstab and one million cells when all dimensions are fully expanded. This scenario has several implications:

-   Nested dimensions and high cardinality dimensions quickly create huge crosstabs.
-   Huge crosstabs have a performance impact and take a long time to display and update.
-   Consider whether it is possible for users to actually read and interpret such a large crosstab.
-   Avoid dimensions with more than 10 members and avoid nesting many levels on each axis.
-   Use filters as input controls instead of hiding and expanding dimensions in the crosstab.

For example, it is unlikely that a user can read the expanded data for more than one country at a time. The large report in this example can be replaced with two reports, one that has only the country dimension and allows the user to compare aggregate values from all countries, and another that displays all provinces and cities for a single country selected by a dropdown filter list. Both reports will run much faster than the single large report, and the user will not be blocked waiting for the report to refresh.
