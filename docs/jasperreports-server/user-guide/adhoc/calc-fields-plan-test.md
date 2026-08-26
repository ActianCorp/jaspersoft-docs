---
title: Planning and Testing Calculated Fields and Measures
description: "When you are creating calculated fields and measures, you may need to follow an iterative process: first create your new fields and measures, then view the results, and finally adjust as needed. The..."
---

# Planning and Testing Calculated Fields and Measures

When you are creating calculated fields and measures, you may need to follow an iterative process: first create your new fields and measures, then view the results, and finally adjust as needed. The following practices can help:

-   Reduce the size of your data set — To speed field creation and testing, reduce the size of your working data set in the following ways:

    -   Select **Sample Data** from the drop-down menu in the Ad Hoc tool bar.
    -   Create one or more filters. This is especially useful for tables, which display all data by default.
    -   Limit the number of fields and measures you add to your test reports to restrict the number of summary levels to one or two.

-   Create one or more formulas, as described in [section 1.0.1, “Creating and Editing Calculated Fields and Measures,” on page 1](calc-fields-creating.md).

-   After you have created your fields and measures, add them to a table or crosstab in your view and verify that they behave as you expect. You may need to edit your fields to get the desired behavior. See [section 1.0.1, “Creating and Editing Calculated Fields and Measures,” on page 1](calc-fields-creating.md) for more information.

In addition, keep the following in mind when creating calculated fields:

-   When you create a calculated field, it appears at the bottom of the list.

-   Calculated fields that use aggregate functions cannot be added to groups and should not be used as filters.

-   By default, the Ad Hoc Editor supports only two decimal places. If the calculated fields return data that are significant to the third decimal place, you can add new masking options by editing configuration files. For more information, refer to the JasperReports Server Administrator Guide.

-   You can’t delete a calculated field that is in use; these fields have their name in italics.

    -   If the calculated field is used in the Ad Hoc view panel, remove the calculated field from the Ad Hoc View panel and then delete it from the **Data Source Selection** panel.
    -   If the calculated field is the basis of another field, you can’t delete it until you delete the one that builds on it.
    -   If the calculated field uses an item that was removed from the data source, the Ad Hoc Editor displays an error message. You will need to either edit or delete the calculated field.
