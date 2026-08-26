---
title: Input Controls and Filters Availability
description: "Input controls and filters can appear in the Editor and when a report runs:"
---

# Input Controls and Filters Availability

Input controls and filters can appear in the Editor and when a report runs:

-   Input controls can be set to be visible or invisible when you edit a view:

    -   Input controls set to **Always prompt** are displayed in the editor and always appear before the report is run.
    -   Input controls that are not set to **Always prompt** are always hidden in the editor and hidden when the report is run.

-   Filters defined in the Domain design are always hidden in the editor and when the report is run.

-   Filters created in the Data Chooser can be locked or unlocked:

    -   Filters that are unlocked display filter information in the editor and are available from the **Options** button when the report is run.
    -   Filters that are locked display input controls in the editor when you see the view in display mode but are not available from the **Options** button when the report is run. Users can remove the filter while in the editor, allowing them to see all the data unfiltered when the report is run.
    -   You cannot change whether the filter is displayed after the report is created.

-   Filters defined in the editor are always available in the Filters panel of the editor and from the **Options** button when the report is run.

When setting up input controls for a huge view that takes a long time to run, consider setting the view to **Always prompt**. Before a report is run, the Report Viewer prompts you to provide the input options**,** preventing the report from running with the default input options.

Filters that are unlocked are available. When input controls or filters do not appear in the Report Viewer, click the **Options** button to view them. You can learn more about how filters and input controls interact in the editor by walking through the data exploration tutorial with the Filters panel open.

To set an input control to always prompt

1.  Locate a Topic, such as the Parametrized Report Topic, in the repository and click **Edit**.
2.  On the Controls & Resources page of the JasperReport wizard, under Input Control Options, select **Always prompt**:

To determine whether an input control is visible

1.  Locate a Topic, such as the Parametrized Report Topic, in the repository and click **Edit**.

2.  On the Controls & Resources page, click the name of an input control, such as Country.

3.  On the Locate Input Control page, click **Next**.

    At the bottom of the Create Input Control page, if the **Visible** checkbox is selected, the input control appears on the report when it runs. For more information, see [Adding Input Controls](../repo-upload-reports/repo-adding-input-controls.md).

    !!! note

        If you do not provide a default value for the input control, users are prompted to select a value when they create a view based on the Topic.

To lock a filter

1.  Click **Create** &gt; **Ad Hoc View**.

2.  In the Select Data wizard, click ![js Dashboard icon ViewTree](../assets/images/js-Dashboard-icon-ViewTree.png) and browse to **Domains** to create a new view based on a Domain.

3.  Click **Choose Data**.

4.  In **Fields**, move tables and fields from **Source** to **Selected Fields**.

5.  Click **Pre-filters**.

6.  Double-click a field in the **Fields** panel.

7.  In the Filters panel, define a filter as described in [The Pre-filters Page](adhoc-data-chooser.md).

8.  Check the **Locked** checkbox, and click **OK**.

9.  Click **Table** to open the Ad Hoc Editor.

    In the Filters panel, the name of the filter and a note about the lock appears under the heading **Locked**.
