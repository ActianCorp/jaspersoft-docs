---
title: "Configuring CZS's Ad Hoc View"
description: The following sections go into more depth about how to define and take advantage of attributes.
---

# Configuring CZS's Ad Hoc View

The following sections go into more depth about how to define and take advantage of attributes.

## Defining a Sales Numbers Cube

The following sections describe the measures and dimensions in the cube that represent CZS's sales data. These data are displayed to CZS's users in an Ad Hoc view that is built from the measures and dimensions in the cube.

### Measures

CZS is primarily interested in the volume and revenue of their sales, as well as their operational cost. These metrics are represented in Jaspersoft OLAP as measures defined in a cube. The measures can be aggregated (rolled up) by dimension hierarchies (described below), such as product, geographical area, and time.

CZS's measures are numeric values contained in the sales_fact_2012 fact table. This fact table includes three measures: unit sales, store cost, and store sales.

### Dimensions

Dimensions are categorical entities used to analyze measures. The cube underlying the Sales Numbers Ad Hoc view includes two dimensions:

- The geographical dimension includes these levels: country, region, state, and city.
- The product dimension describes the merchandise being sold and includes these levels: product family, product line, and product.

For more information about how the Sales Numbers schema joins the hierarchical tables with the detail tables, refer to [OLAP Schema](reference_material.md).
