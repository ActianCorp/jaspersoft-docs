---
title: Working with Subreports
description: The subreport element lets you nest one report (the subreport) inside another (the master report). A subreport can use the same database connection as the parent report or you can specify a different...
---

# Working with Subreports

The subreport element lets you nest one report (the subreport) inside another (the master report). A subreport can use the same database connection as the parent report or you can specify a different data source in the subreport properties. A master report can contain multiple subreports and subreports can be nested.

Subreports are one of the most advanced features of JasperReports. They allow you to design very complex reports by inserting one or more reports into another report.

!!! note

    Reflecting standard Eclipse design, saving or previewing a report that contains subreports does not update the subreports. When you edit a subreport, you must explicitly save and build the subreport for the changes to be visible when you preview the report that contains it. To build a subreport, right-click the project in the Project Explorer and select **Build Project**, or type **Ctrl-B** to build all projects in the workspace.

Subreports also let you combine two or more child lists of data relating to a single parent element, for example, a report with multiple detail bands of different types. You map parameters between the master report and its subreports to create a blended report where each subreport displays details for each record from the master report. As the master report runs, each time a subreport element is reached, it is run and its content is embedded into the output of the master report.

Uses for subreports include:

-   Modularizing reports–You can create a subreport with your preferred data fields and layout, then use the subreport in multiple master reports.

-   Combining multiple queries or data sources in a single report.

This topic contains the following sections:

-   [Creating a New Report via the Subreport Wizard](subreports-wizard.md)

-   [Understanding Subreports](subreports-reference.md)
