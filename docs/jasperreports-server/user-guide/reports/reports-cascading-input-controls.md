---
title: Cascading Input Controls
description: Cascading input controls in a report reduce a large number of choices to a manageable number. A single value chosen for a cascading input control determines which other values appear as choices for...
---

# Cascading Input Controls

Cascading input controls in a report reduce a large number of choices to a manageable number. A single value chosen for a cascading input control determines which other values appear as choices for input. For example, the choice of a country determines which states or regions are listed as choices. For more information, see [Selecting a Data Source for Running the Complex Report](../repo-upload-reports/repo-data-source-complex-report.md).

To run a report with cascading input controls

1.  In the repository, locate and run the report 16. Interactive Sales Report.<br>
    The report runs, and appears with the **Options** panel open on the left side of the Report Viewer.

2.  In the Options panel’s **Country multi select** dropdown, select a different country, for example Canada.<br>
    The other dropdowns in the Filters panel are automatically updated with Canadian data.

    !!! note

        Cascading input controls are implemented as queries that access the database to retrieve the new values. The server displays an activity monitor while the query is running, and in the case of long queries, you can click Cancel and select different values.

3.  In the Product Name section, select a product to display in the report.

4.  Click **Apply** to run the report with the chosen values.
