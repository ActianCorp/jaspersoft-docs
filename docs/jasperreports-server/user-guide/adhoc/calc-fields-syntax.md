---
title: Calculated Field Syntax
description: "This section describes the syntax required when creating calculated fields in Ad Hoc views. See section 1.0.1, “Calculated Field Reference,” on page 1 for more information."
---

# Calculated Field Syntax

This section describes the syntax required when creating calculated fields in Ad Hoc views. See [section 1.0.1, “Calculated Field Reference,” on page 1](calc-fields-reference.md) for more information.

Use the following syntax for inputs:

-   To reference a text string, use single quotes (') - `'Text String'`.

-   To reference a field label, use double quotes (") - `"``Ad Hoc Label``"`.

-   To reference date constants, indicate the date type as part of the syntax, as listed below:

    -   To reference a date without time data (for example: yyyy-dd-mm), use `d` followed by single quotes (') - `d'2014-06-10'`.
    -   To reference a date with day and time data (for example: yyyy-dd-mm hh:mm:ss) use `ts `followed by single quotes (') - `ts'2014-06-10 01:30:00'`. If you use `ts `and enter the date information only, the time is automatically set to `00:00:00`.
    -   To reference a date with time data only (hh:mm:ss), use `t` followed by single quotes (') - `t'01:30:00'`.

-   To reference a date field label, use double quotes (") - `"``Ad Hoc Date Field Label``"`.

!!! note

    The following are reserved words and cannot be used as field names: AND, And, and, IN, In, in, NOT, Not, not, OR, Or, or. Names containing these strings, such as "Not Available", can be used.

!!! note

    When dates are used in comparisons or the IF function, they must be the same type, (date only, date/time, or time only). Make sure to use the correct modifier (d, ts, t) when using date constants in comparisons.

In the function descriptions for calculated fields in [section 1.0.1, “Calculated Field Reference,” on page 1](calc-fields-reference.md), the argument name describes the type of input the function accepts. For more information about input types, see JasperReports Server Data Management Using Domains:

-   `BooleanExpression` - Any expression that takes on Boolean values, including the label of a Boolean field or measure, a Boolean calculation, or a Boolean value.

    !!! note

        You can create a BooleanExpression using the following: comparison operators (==, !=, &gt;, &gt;=, &lt;, &lt;=, in); functions that return Boolean values (StartsWith, EndsWith, IsNull, Contains) and logical functions (AND, OR, NOT).

-   `DateExpression` - Any type of date or timestamp values, including the label of a date field or measure, or a calculation that returns dates.

-   `DateTimeExpression` - Date expressions that contain time values, including the label of a date field or measure, or a calculation that returns dates. These values are also known as timestamp values.

-   `Expression` - Any valid date, date-time, numeric, or string expression.

-   `NumericExpression` - Numeric values, including the label of a numeric field or measure, or a calculation that returns numbers.

-   `TextExpression` - Text values, including the label of a text field or measure, or a text string.

-   `Level` - For aggregate functions, specifies the set of values used to compute the calculation. Possible values include Current (not available for PercentOf), ColumnGroup, ColumnTotal, RowGroup, RowTotal, Total. See [section 1.0.1.1, “Levels in Aggregate Functions,” on page 1](calc-fields-aggregates.md) for more information.
