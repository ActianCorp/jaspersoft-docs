---
title: Defining an MDX Query
description: Each OLAP view operates against a particular cube within the OLAP connection. The view includes an MDX query that defines the data to display.
---

# Defining an MDX Query

Each OLAP view operates against a particular cube within the OLAP connection. The view includes an MDX query that defines the data to display.

MDX is a query language used to define the contents of an OLAP view. It is also used when by Ad Hoc views built on OLAP client connections. Originating at Microsoft, the language is widely used for multidimensional data retrieval. An MDX query, coupled with an OLAP schema, retrieves data from a database. The following is a typical MDX query:

``` sql
select {[Measures].[Unit Sales], [Measures].[Store Cost], [Measures].[Store Sales]} ON
COLUMNS, {([Promotion Media].[All Media], [Product].[All Products])} ON ROWS
from [Sales]
where [Time].[2012].[Q4].[12]
```

In the example MDX:

- `[Measures].[STORE SALES]` is a measure.
- `[PRODUCT].[ALL PRODUCTS]` is a member in the PRODUCT dimension.
- `[STORE].[ALL STORES]` is a member in the STORE dimension.
- `[SALES BY PRODUCT BY STORE]` is a cube.
- `[TIME].[2012]` is a member used as a filter axis in the WHERE clause.

Jaspersoft OLAP constructs MDX queries as you use its controls to manipulate the view. If you are not proficient with MDX, you may want your initial view to use the simplest possible MDX query. For example, you can start with one measure and one dimension, then use the tool bar buttons and navigation table to tailor the view to show the exact data you want. You can always see the MDX that underlies the current view by clicking **View MDX query** in the tool bar. You can also edit this query to change the view if you are comfortable with MDX.
