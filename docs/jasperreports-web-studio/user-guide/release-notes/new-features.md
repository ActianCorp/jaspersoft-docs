---
title: New Features
description: This section describes new features introduced in the JasperReports Web Studio 10.1.0 release.
---

# New Features

This section describes new features introduced in the JasperReports Web Studio 10.1.0 release.

For JasperReports Web Studio 10.1.0, the following improvements have been added:

-   **Drag-and-Drop Query Building**

    You can now drag nodes from the **Metadata** panel directly into the Query Editor area. This streamlines query creation, ensures naming accuracy, and significantly reduces manual typing.

-   **Composite Elements**

    Added support for Composite elements. These are **TextFields** with predefined system expressions (Pagination, Date/Time, Calculations), allowing for faster report design and reduced expression errors.

-   **Contextual "Maximize" Action**

    Added a new contextual action that allows you to instantly expand an element band to its maximum available height. The tool intelligently calculates the remaining space based on your document dimensions and the space occupied by other report bands.

-   **Manual Parameter Reordering**

    You can now manage the resolution sequence of your datasets by dragging and dropping parameters. Using the new handle icon on the left of each parameter name, you can ensure that dependent variables are resolved in the correct order for your query.

-   **Enhanced Pattern Editor**

    Configuring formats for numeric and date-time TextFields is now easier. Clicking the ellipsis (...) button in the pattern section opens a new dialog featuring a library of common presets. You can select a predefined pattern and use the built-in controls to fine-tune it to your specific needs.

-   **Automated Aggregate Calculations**

    Dragging fields into summary or group bands now triggers a "Smart Calculation" dialog. Choose from a variety of aggregation types (with extra options for numbers), and the system will instantly create the required variables and expressions for you.

-   **JDBC Scalability Improvements**

    Large database schemas now load significantly faster thanks to new lazy-loading logic. This update eliminates timeouts by fetching metadata in smaller, on-demand increments.

-   **Streamlined Repository Access**

    To simplify your setup, report repositories and owners are now generated automatically. Upon login, the interface directs you straight to your personal repository, eliminating manual configuration and providing a smoother start-to-finish workflow.

-   **Cross-Site Request Forgery (CSRF) Protection**

Implemented CSRF security filters across the application to prevent unauthorized commands from being executed on behalf of authenticated users.
