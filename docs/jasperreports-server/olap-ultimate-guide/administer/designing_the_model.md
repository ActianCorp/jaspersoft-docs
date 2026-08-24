---
title: Designing the Model
description: Facilitating questions and answers about large sets of data involves some planning and intuition to know which questions are relevant.
---

# Designing the Model

Facilitating questions and answers about large sets of data involves some planning and intuition to know which questions are relevant.

Even if you do not know how a particular variable affects the results, you may still want to model it if you suspect an influence; this may help you to understand the variable’s effects.

The basic premise is that we can lay our data out such that mathematics can reveal meaning. It is essential to phrase measures quantitatively. For example, instead of posing a yes or no question, provide a count of each possible answer, either 1 or 0. This way, the number of yes answers can be tallied at any level of aggregation and for any set of dimensional parameters.

In an OLAP schema:

- A cube is the logical entity that holds all the facts for each measure. Cubes can contain millions of facts, which are too numerous to be analyzed individually.
- A fact is the value of a measure for a specific member of a dimension; facts relate directly to their dimensional positions.
- Dimensions provide the structure for slicing and dicing data. Each fact references the dimensional members that correspond to the variables defining the observation of this fact. Generally speaking, the most useful way to aggregate data reflects the domain model; for companies, the data organization should reflect their business rules.

The art of dimensional modeling lies in finding useful ways to aggregate your data.

Dimensions are organized into hierarchies that represent increasing levels of aggregation. Consider the example of a dimension representing time. Such dimensions often include levels representing month, day, and year. If your requirements necessitate it, the dimension might also include levels for quarters, fiscal quarters, 10-day periods, weeks, or even days.

The hierarchical nature of dimensions allows both roll-up and drill-down. For example, if fiscal quarters are made up of 3 months, the quarterly data can be broken out by month. Then, if the measures for a particular month are anomalous, you can drill deeper into that month (grouping results by day) to identify the cause of the anomaly. You can also compare your expectations and actual results in the same OLAP view by representing them both as measures.

Measures are essentially numerical formulas. The values they resolve to are called facts. For example, if weight is the measure, 10 pounds is a fact. To be useful, a fact needs context, such as what an object weighs 10 pounds and when it weighed 10 pounds. In a business context, common measures may include number of units, transactions, cost per unit, and price per unit. Calculated measures allow for more complex formulas that work off other measures. So, for example, operating profit margin may be a calculated measure that is a formula based on many measures.

Restating briefly, cubes contain facts, which are instances of measures. These facts are defined by dimensional coordinates.

For businesses, useful dimensions may include time, locations, product categorizations, customers, employees, and any other categorizations that provide business context for individual records. Organizing each dimension into a hierarchy allows roll-up and drill down.

Designing and using a dimensional model involves creating processes, such as those listed in the following table.

Creating a Dimensional Model

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>Process in Dimensional Modeling</p></th>
<th><p>Examples of Process Applied to Specific Data</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Phrasing the business problems to be understood and solved.</p></td>
<td><ul>
<li>How does customer satisfaction affect revenue?</li>
<li>How can we improve customer satisfaction?</li>
</ul></td>
</tr>
<tr>
<td><p>Identifying quantifiable measures of interest, Key Performance Indicators (KPIs), and metrics.</p></td>
<td><ul>
<li>Revenue</li>
<li>Customer survey results</li>
<li>Repeat customers</li>
</ul></td>
</tr>
<tr>
<td><p>Identifying variables that are thought to influence those measures.</p></td>
<td><ul>
<li>Interactions between the customer and business</li>
<li>Quality of the product or service</li>
<li>Preferences of individual customers</li>
</ul></td>
</tr>
<tr>
<td><p>Organizing those variables into dimensional hierarchies.</p></td>
<td><ul>
<li>Product dimension with levels for Line, Category, Product, and SKU</li>
<li>Store Location dimension with levels for Country, State, City</li>
</ul></td>
</tr>
<tr>
<td><p>Expressing those measures and variables in cubes and dimensions.</p></td>
<td><ul>
<li>Dimensions - Store location, Products, Time, Customers, CRM cases</li>
<li>Cubes - Sales, Accounts, Surveys</li>
<li>Measures - Satisfaction Score, Number of Interactions, Number of Transactions, Prices, Size of Transactions, Revenues</li>
</ul></td>
</tr>
<tr>
<td><p>Mapping the source data into a schema for analysis.</p></td>
<td><ul>
<li>FoodMart source data --&gt; <span> foodmart.xml</span></li>
</ul></td>
</tr>
<tr>
<td><p>Making queries whose answers provide analytical insight.</p></td>
<td><ul>
<li>What are the average satisfaction Scores and Size of Transactions for each store by month?</li>
<li>Why does the September Revenue appear to be an outlier for stores in Florida, although the Satisfaction Scores are within the normal range?</li>
<li>Why are the Satisfaction Scores and Number of Repeat Transactions consistently lower for one particular store than the average across the business?</li>
</ul></td>
</tr>
</tbody>
</table>
