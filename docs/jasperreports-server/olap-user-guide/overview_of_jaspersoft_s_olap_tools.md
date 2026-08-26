---
title: Overview of Jaspersoft’s OLAP Tools
description: "Jaspersoft offers a number of tools to help you define multidimensional cubes and explore their data. For end-users, the following tools provide access to OLAP data:"
---

# Overview of Jaspersoft’s OLAP Tools

Jaspersoft offers a number of tools to help you define multidimensional cubes and explore their data. For end-users, the following tools provide access to OLAP data:

-   Ad Hoc views: Created with the Ad Hoc Editor, these views can be based on OLAP client connections. An Ad Hoc view can be a table, chart, or crosstab and is the entry point to analysis operations such as slice and dice, drill down, and drill-through. You can save an Ad Hoc view as a report to edit it in the interactive report viewer, schedule it, or add it to a dashboard.
-   OLAP-based reports: Reports created in the Ad Hoc Editor, iReport, and Jaspersoft Studio can read data from OLAP data sources. These reports tend to be more static than views based on the same data sources, but are excellent when data exploration, such as slice or drill-through, yields results you need to distribute widely.
-   Jaspersoft OLAP views: A view of multidimensional data that is based on an OLAP client connection and an MDX query. Unlike Ad Hoc views, you can directly edit an OLAP view’s MDX query to change the data and the way they are displayed. An OLAP view is the entry point for advanced analysis users who want to write their own queries.
-   Jaspersoft ODBO Connect: This separate client user interface enables Microsoft Excel Pivot Tables to access Jaspersoft OLAP and other OLAP servers that support the XML for Analysis (XML/A) Simple Object Access Protocol (SOAP) protocol. It lets users familiar with Excel leverage those skills to explore their OLAP cubes and create pivot tables based on them. Jaspersoft ODBO Connect is described in its own user guide, which is installed with the product.

In addition to these end-user tools, the Jaspersoft OLAP workbench helps data analysts define the measures and dimensions of a cube based on the data in their transactional database. The workbench is described in its own user guide, which is installed with the product.

!!! note

    -   The OLAP connections that you define in Jaspersoft OLAP can be used to explore data in Ad Hoc views, which retain the dimension and measure metadata defined for your cubes. For more information, refer to the JasperReports Server User Guide.

    -   Jaspersoft 's Visualize.js does not support Jaspersoft OLAP data sources.
