---
title: "Ad Hoc Sources: Topics, Domains, and OLAP Connections"
description: "The following repository objects provide a prepared connection to a data source for Ad Hoc view creation:"
---

# Ad Hoc Sources: Topics, Domains, and OLAP Connections

The following repository objects provide a prepared connection to a data source for Ad Hoc view creation:

-   Topics , JRMXL files are created externally and uploaded to JasperReports Server as a basis for Ad Hoc views.

-   Domains , virtual views of a data source that present the data in business terms, allow for localization, and provide data-level security.

-   OLAP Connections , multi-dimensional views of data that allow users to analyze a large number of aggregate data levels.

You can also open and edit an existing Ad Hoc view to create a new Ad Hoc view. After editing the Ad Hoc view, if you close the Ad Hoc view without saving the changes, you are prompted to save or cancel the changes.

## Topics

Generally, an administrator or Jaspersoft Studio user creates a Topic as a JRXML file. The JRXML topic is then associated with a data source in the server. A Topic can also be created from a Domain in the server. Both types of topics appear in the Select Data wizard when you create an Ad Hoc view.

Using a Topic as your source generates an empty view, which allows you to begin adding data to your view right away, without choosing, pre-filtering, or changing display names of the data (all of which are required steps when creating a Domain-based view).

The views in the /Ad Hoc Components/Topics folder populate the Topics tab that appears when users click **Create &gt; Ad Hoc View**.

To begin designing a Topic-based view

1.  Launch the Ad Hoc Editor by clicking **Create &gt; Ad Hoc View.**
2.  In the Select Data wizard, click ![js Dashboard icon ViewTree](../assets/images/js-Dashboard-icon-ViewTree.png) and navigate to **Ad Hoc Components &gt; Topics**.
3.  Expand the Topics folder and select a topic.
4.  Select the type of view that you intend to create: table, chart, or crosstab. For an overview of view types, see [Ad Hoc View Types](adhoc-view-types.md).

You can now begin working on your view in the Ad Hoc Editor.

## Domains

Administrators create Domains that typically filter the data, create input controls, and manage the list of available fields and measures. A Domain specifies tables in the database, join clauses, calculated fields, display names, and default properties, all of which define items and sets of items for creating Ad Hoc views.

Unlike Topics, which must be stored in a specific folder in the repository, Domains are detected regardless of their location in the repository. The /Domains folder is included for your convenience, but the Domains tab in the Source dialog displays all the Domains to which you have access in the repository.

To begin designing a Domain-based view

1.  Launch the Ad Hoc Editor by clicking **Create &gt; Ad Hoc View.**

2.  In the Select Data wizard, click ![js Dashboard icon ViewTree](../assets/images/js-Dashboard-icon-ViewTree.png) and navigate to **Domains**.

3.  Expand the Domains folder and select a domain.

4.  Click **Choose Data...**, and click the options on the left of the window to perform the following tasks:

    -   Click **Fields** to select fields of data to use in the view.
    -   Click **Pre-filters** to create filters to limit the data available in the Ad Hoc Editor.
    -   Click **Display** to change the fields’ display names.
    -   Click **Save as Topic** to save the customized topic for later use.

5.  Select the type of view that you want to create: table, chart, or crosstab. For an overview of view types, see [Ad Hoc View Types](adhoc-view-types.md).

You can now begin working on your view in the Ad Hoc Editor.

## OLAP Connections

Administrators create OLAP client connections that expose transactional data and define how the data can be seen as a multidimensional cube. An OLAP connection can expose multiple cubes in a single OLAP connection.

!!! note

    With OLAP connections, you can create chart and crosstab views only.

To begin designing an OLAP connection-based view

1.  Launch the Ad Hoc Editor by clicking **Create &gt; Ad Hoc View.**
2.  In the Select Data wizard, click ![js Dashboard icon ViewTree](../assets/images/js-Dashboard-icon-ViewTree.png) and navigate to **Analysis Components &gt; Analysis Connections** and select a sample project and a connection.

You can now begin working on your view in the Ad Hoc Editor.

For more information about OLAP-based view functionality, refer to the following sections:

-   [Working with OLAP Connection-based Crosstabs](adhoc-crosstabs-olap.md)

-   [Creating Topics](adhoc-topics.md)
