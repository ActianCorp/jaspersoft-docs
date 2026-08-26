---
title: On-Line Analytical Processing
description: On-Line Analytical Processing (OLAP) entails analyzing quantitative and categorical data using a set of analytical operations. We compare and contrast the quantitative data (measures) among a set of...
---

# On-Line Analytical Processing

On-Line Analytical Processing (OLAP) entails analyzing quantitative and categorical data using a set of analytical operations. We compare and contrast the quantitative data (measures) among a set of categories (dimensions). Jaspersoft OLAP facilitates such analysis with a standard set of functions, often called operations. OLAP compliments traditional reporting with a series of dynamic reports. Analytical operations let you filter information, get instant and incremental feedback, and devise what-if questions across a set of categories for comparing various numeric data. OLAP is well suited to sales analysis, customer profiling, and trend analysis.

Generally, the people most interested in OLAP applications are technical business analysts with in-depth knowledge of their data and basic capability in analysis. From their perspective, OLAP systems answer five questions:

-   Who buys the product?
-   What products are they buying?
-   Where are the most successful stores?
-   When are sales being made?
-   Why are certain products are sold, and under which promotional conditions?

You can derive the answers to these questions from a special data structure known as a cube. A cube contains all the data pertaining to a single business context, such as sales activities and customer demographics. To analyze the data in the cube, use the Jaspersoft OLAP web interface to slice and dice, expand and collapse, zoom in and out, and drill-through. For more information on these operations, see [Using the OLAP View Tools](../analyze-data/using_the_olap_view_tools.md).

!!! note

    The examples in this guide assume that you are using MySQL. If you are using a different database, you may need to use slightly different MDX queries; for example, if you use Oracle, you cannot use the upper-case member names shown in the examples.
