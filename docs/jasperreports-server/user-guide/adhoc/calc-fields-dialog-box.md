---
title: Overview of the Calculated Fields Dialog
description: The Calculated Field or Calculated Measures dialog creates a calculated field or measure and set its summary function. This section describes the functionality available in this dialog.
---

# Overview of the Calculated Fields Dialog

The **Calculated Field** or **Calculated Measures** dialog creates a calculated field or measure and set its summary function. This section describes the functionality available in this dialog.

To open the calculated fields dialog for Ad Hoc views

1.  Create or open an Ad Hoc view.

2.  Open the calculated fields dialog using one of these methods:

    -   Click ![js AdHoc icon kebab](../assets/images/js-AdHoc-icon-kebab.png) at the top right of either the **Fields** section or the **Measures** section of the Data Source Selection panel and select **Create Calculated Field...** from the context menu.
    -   Right-click on an existing calculated field (shown by the icon![js icon calculated field](../assets/images/js-icon-calculated-field.png)) or calculated measure (shown by the icon![js icon calculated measure](../assets/images/js-icon-calculated-measure.png)) and select **Edit**.

    The dialog displays a text field for the name and two tabs, **Formula Builder** and **Summary**.

    !!! note

        The following are reserved words and cannot be used as field names: AND, And, and, IN, In, in, NOT, Not, not, OR, Or, or. Names containing these strings, such as "Not Available", can be used.

## The Formula Builder Tab

The Formula Builder tab is where you create the formula for your calculated field or measure. This tab includes the following:

-   Formula entry box - Shows the current formula for calculating your field or measure. You can edit the formula by typing directly in the panel. You can also add Fields, Measures, and Functions by double-clicking them. Click the buttons below the Formula field to add operators. Formulas must use the following syntax:

    1.  Labels for fields and measures must be in double quotes ("): "Customer ID", "Date ordered".
    2.  Text must be in single quotes ('): '--'.
    3.  Levels must be in single quotes ('): 'ColumnGroup', 'Total'. See [section 1.0.1.1, “Levels in Aggregate Functions,” on page 1](calc-fields-aggregates.md) for more information about levels.<br>
        For more information on syntax, see [section 1.0.1, “Calculated Field Syntax,” on page 1](calc-fields-syntax.md).

-   Operator buttons - Click these buttons to insert the operator in the Formula entry box. For more information on operators, see [section 1.0.1, “Operators in Ad Hoc Views,” on page 1](calc-fields-operators.md)

-   Fields and Measures - Lists all the fields and measures currently in your Ad Hoc view, including any calculated fields or measures you have already created.

    !!! note

        Hovering over a field or measure displays additional information in a tool tip. This information includes the data type of the field or measure, its description if any is given in the Domain, and its default summary function if applicable. Use this information to choose the appropriate field or measure, and to use it correctly in the formula.

-   The tooltip content includes:

    -   **Field Path** (for example: Sales &gt; Stores &gt; Regions &gt; City) for Domain-based Ad Hoc
    -   **Original name** (from the domains)
    -   **Formula** (for calculated fields and calculated measure only)
    -   **Description**
    -   **Data Type** (Possible values are string, number, date, time, timestamp, boolean)
    -   **Field type** (Field, Measure, Calculated Field, Calculated Measure)
    -   **Default summary calculation**

-   Functions - Lists all the available functions that you can use in your formula. For more information, see [section 1.0.1, “Calculated Field Reference,” on page 1](calc-fields-reference.md).

-   Function Description panel - Gives a brief description of the function selected in the Functions list, if any. The sample inputs are intended to be as descriptive as possible. See [section 1.0.1, “Calculated Field Reference,” on page 1](calc-fields-reference.md) for the precise syntax that each function requires.

-   Show arguments in formula checkbox - When this checkbox is selected, double-clicking a function name in the Functions list adds the full description to the Formula entry box. When the checkbox is not selected, double-clicking a function name adds only the function. For example, double-clicking `Round` adds `Round("NumberFieldName", Integer)` when the checkbox is selected, and adds `Round()` when the checkbox is not selected. If you select this checkbox, you can double-click a string, such as `NumberFieldName`, and then replace it by double-clicking a name in the Fields and Measures list.

-   Validate button - Checks the formula for syntax errors, such as missing parentheses or quotes. Your calculated field or measure must be valid before you can create it. Syntax validation does not guarantee that your formula gives the results you want.

## The Summary Tab

Summaries show a result applied to all data values. For example, for a numeric field such as Cost, the summary value might be the sum of all the costs; for a text field such as Customer Name, the summary value might be the count of all customers. The Summary tab sets the default summary function for your calculated field or measure.

-   Calculation list - Displays allowed summary functions for your calculated field or measure. The available options depend on the data type of the calculation. See [section 1.0.1, “Summary Calculations,” on page 1](calc-fields-summaries.md) for more information. Depending on your selection, you may see additional options:

    -   Custom selection - Displays the same options available in the Formula Builder tab, including the Formula entry box, operator buttons, Fields and Measures list, Functions list, and Validate button. You can use these options to build a formula for your custom summary. However, for summaries, you are limited to aggregate functions, that is, functions that operate on all the values in your field. For example, `Sum` and `Mode` are valid summary functions, because they use all available field values to get a result. `Round` is not a valid summary function, because it operates on a single value at a time. See [section 1.0.1, “Summary Calculations,” on page 1](calc-fields-summaries.md) for more information.
    -   Weighted Average - Displays a Weighted On dropdown list, which allows you to choose another field or measure to use as the weight for the average.
