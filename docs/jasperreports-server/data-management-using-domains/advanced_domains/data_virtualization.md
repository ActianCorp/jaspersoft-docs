---
title: Domains and Data Virtualization
description: "There are two ways to integrate data virtually from multiple sources using Domains in JasperReports Server:"
---

# Domains and Data Virtualization

There are two ways to integrate data virtually from multiple sources using Domains in JasperReports Server:

-   For simple data virtualization with low volumes of data and limited join complexity, create a JasperReports Server virtual data source and build your Domain on top of it. In this case, you define the relationships that connect the tables of the different data sources using the Domain Designer. See the JasperReports Server Administrator Guide for more information about virtual data sources in JasperReports Server. This is a lightweight solution that does not require any additional server or installation.
-   For more complex virtualizations, or where performance and scale are essential, use Jaspersoft Advanced Data Services to access and combine your different data sources. Once you have designed and created an integrated data source in Jaspersoft Advanced Data Services, you create a JasperReports Server JDBC data source to access it and then use the Domain Designer to choose the tables you want and create user-friendly names. Using Jaspersoft Advanced Data Services offers better performance and scaling, with management tools designed specifically for combining multiple data sources. Contact your sales representative for information about licensing for Jaspersoft Advanced Data Services. This requires a separate installation for Jaspersoft Advanced Data Services.

## Notes on Using Virtual Data Sources

Normally, you combine data sources that have relationships you want to explore. To create a useful Domain using a virtual data source, you need to define relationships that connect the tables of the different data sources. You do this by adding at least one schema from each data source and then creating a join between tables in the different schemas. If the data sources do not have a column that matches exactly, you can create derived tables that allow you to implement the join you want. For example, if you use the sample SugarFoodMartVDS virtual data source, which combines the Foodmart and SugarCRM JDBC data sources, you can create two derived tables, one that aggregates `sales` by `city` for the Foodmart data source and another that aggregates `amount` by `city` for the SugarCRM data source. Then you can join the two data sources on `city` to combine them.

!!! note

    Domains built from virtual data sources may have additional syntax restrictions. For example, Domains built from a virtual data source do not work with table names that contain \\.
