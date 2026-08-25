---
title: Calculated Field Reference
description: "This section lists all functions that can be used to create calculated fields and measures in Ad Hoc views. For details of the supported syntax, see Calculated Field Syntax."
---

# Calculated Field Reference

This section lists all functions that can be used to create calculated fields and measures in Ad Hoc views. For details of the supported syntax, see [Calculated Field Syntax](calc-fields-syntax.md).

!!! note

    These functions are available for calculated fields and measures in Ad Hoc views only. See JasperReports Server Data Management Using Domains for supported operators and functions in Domains.

The examples in this section indicate correct syntax, but are not necessarily associated with an Ad Hoc view. If you have installed the Jaspersoft samples, the Ad Hoc view **10. Calculated Fields and Measures** include examples of calculated fields (shown by the icon![js icon calculated field](../assets/images/js-icon-calculated-field.png)) or calculated measures (shown by the icon![js icon calculated measure](../assets/images/js-icon-calculated-measure.png)). You can explore their formulas by right-clicking on the field or measure name and selecting **Edit**. You can also create tables, charts, or crosstabs to see how these calculations work in views.

## Absolute(NumericExpression)

Returns the absolute value of a number or field, that is, the non-negative value of the number.

**Examples:**

`Absolute("Transaction Amount")` — Shows the magnitude of each transaction, regardless of whether the transaction is positive or negative.

`"Commission Rate" * Absolute("Transaction Amount")` — Computes a positive commission on all transactions, regardless of whether the transaction is positive or negative.

## Attribute('StringExpression1', \['StringExpression2' \])

Given the name of an attribute as the first argument and an optional category as the second argument, returns the attribute's current value as a String. If a category is specified (USER, TENANT, or SERVER), returns a categorical attribute, otherwise returns a hierarchical attribute. This value can be cast to a different datatype using one of the casting functions available in Ad Hoc: `Boolean()`, `Date()`, `Decimal()`, `Integer()`, `Time()`, or `Timestamp()`. It is your responsibility to ensure the attribute's format and values work correctly with your Ad Hoc view. See the *JasperReports Server Administrator Guide* for more information about creating and using attributes.

**Example:**

`Attribute('my_attribute')`

## Average(NumericExpression\[,'Level'\])

Returns the average value of a measure or numeric field, based on an optional level. Null values are not included. See [Levels in Aggregate Functions](calc-fields-aggregates.md) for more information.

**Example:**

`Average("Salary", 'RowGroup')`

## Boolean ('StringExpression')

Casting function that takes a String expression and converts it to a Boolean data type. The String can be any expression that returns a supported string, including a field value or an attribute retrieved with the `Attribute()` function. The `Boolean()` function requires one of the following Strings: true, false, True, False, TRUE, or FALSE. Other Strings will return an error.

**Examples:**

`Boolean('true')`

`Boolean(Attribute('my_boolean_attribute'))`

## Case(Expression, ValueExpression1, ReturnExpression1, ValueExpression2, ReturnExpression2\[,..., ValueExpressionN, ReturnExpressionN\]\[,DefaultReturnExpression\])

Takes 2N+1 or 2N+2 arguments: an expression followed by one or more value expression/return expression pairs, with an optional final return expression. Compares the expression in the first argument to each value expression in order of appearance. Returns the value of the expression immediately following the first value expression that matches. If no expression matches, returns the final `DefaultReturnExpression` if present, null otherwise.

The types of all the return expressions must be compatible. For example, you cannot mix numeric and text return value types.

**Example:**

`Case("Shipped by", 1, 'FedEx', 2, 'UPS', 3, 'USPS', 'Unknown')`

## CaseRange (NumericExpressionInput, NumericExpression1, ReturnExpression1, NumericExpression2, ReturnExpression2\[,..., NumericExpressionN, ReturnExpressionN\]\[,DefaultReturnExpression\])

Takes 2N+1 or 2N+2 arguments: an expression followed by one or more numeric expression/return expression pairs, with an optional final return expression. Finds the first numeric expression that is greater than the input expression and returns the value of the corresponding return expression. If no expression is greater, returns the final `DefaultReturnExpression` if present, null otherwise.

The types of all the return expressions must be compatible. For example, you cannot mix numeric and text return value types.

**Examples:**

`Case("Temperature", 60, 'too cold', 80, 'just right', 'too hot')`

`CaseRange(CountAll("Shipping charge") % CountAll("Shipping charge", 'Total'), 2.0, 'Less than 2%', 5.0, '2% - 5%', 'More than 5%')`

## CaseWhen(BooleanExpression1, ReturnExpression1, BooleanExpression2, ReturnExpression2\[,..., BooleanExpressionN, ReturnExpressionN\]\[, DefaultReturnExpression\])

Takes 2N or 2N+1 arguments: one or more pairs of Boolean expressions followed by return expressions, with an optional final return expression. Returns the expression immediately following the first true Boolean expression. If no expression is true, returns the final `DefaultReturnExpression` if present, null otherwise. This is the most flexible construct.

The types of all the return expressions must be compatible. For example, you cannot mix numeric and text return value types.

**Examples:**

`CaseWhen("Shipped by" == 1, 'FedEx', "Shipped by" == 2, 'UPS', "Shipped by"== 3, 'USPS', 'Unknown')`

`Case("Temperature" <= 60, 'too cold', "Temperature" > 80, 'too hot', 'just right')`

## Concatenate(TextExpression1\[ ,TextExpression2,...,TextExpressionN\])

Combines multiple text strings and/or fields into a single text field. Text strings are enclosed in single quotes; labels for fields or measures in Ad Hoc are enclosed in straight quotes.

**Examples:**

`Concatenate("Last Name", ' , ', "First Name")`

`Concatenate("Product Category", ' -- ', "Product Name")`

## Contains(TextExpression1 ,TextExpression2\])

A boolean that returns true if the first string contains the second, false otherwise.

**Example:**

`Contains("Product Name", 'Soda')`

## CountAll(Expression\[,'Level')\]

Returns the count of non-null items in a field or measure. Note that `CountAll` always returns a non-negative integer. `Level` can be one of the following: `Current` (default), `ColumnGroup`, `ColumnTotal`, `RowGroup`, `RowTotal`, `Total`. See [Levels in Aggregate Functions](calc-fields-aggregates.md) for more information.

**Example:**

`CountAll("Transaction Amount", 'RowGroup')` — Counts the total number of non-null transactions in the specified group.

## CountDistinct(Expression\[,'Level'\])

Returns the distinct count of non-null items in the input. Always returns a non-negative integer. `Level` can be one of the following: `Current` (default), `ColumnGroup`, `ColumnTotal`, `RowGroup`, `RowTotal`, `Total`. See [Levels in Aggregate Functions](calc-fields-aggregates.md) for more information.

**Example:**

`CountDistinct("Customer Name", 'Total')` — Counts the number of distinct customers.

## Date('StringExpression')

Casting function that takes a String expression and converts it to a Date data type. The String can be any expression that returns a supported string, including a field value or an attribute retrieved with the `Attribute()` function. The `Date()` function requires a String value formatted as 'yyyy-MM-dd'. Other Strings will return an error.

**Examples:**

`Date('2015-07-17')`

`Date(Attribute('my__date_attribute'))`

## Decimal('StringExpression')

Casting function that takes a String expression and converts it to a Decimal data type. The String can be any expression that returns a supported string, including a field value or an attribute retrieved with the `Attribute()` function. The `Decimal()` function requires a String value in decimal format, for example, '123.45'. Other Strings will return an error.

**Example:**

`Decimal('1234.567')`

## DayName (DateExpression)

Given a date field, returns a text field with the name of the day of the week.

**Examples:**

`DayName("Open Date")` - Displays the day of the week on which a store was opened.

`Mode(DayName("Open Date"), 'Total')` - The day of the week on which the most stores were opened.

## DayNumber (DateExpression)

A numeric field that returns the day of the month from a date field.

**Example:**

`DayNumber("Open Date")` - Displays the day of the month on which a store was opened.

## ElapsedDays (DateExpression1, DateExpression2)

Calculates the number of days elapsed between two date fields that contain time values.

**Example:**

`ElapsedDays ("Date shipped","Date required")`

## ElapsedHours (DateTimeExpression1, DateTimeExpression2)

Calculates the number of hours elapsed between two date fields that contain time values.

**Example:**

`ElapsedHours ("Date shipped","Date required")`

## ElapsedMinutes (DateTimeExpression1,DateTimeExpression2)

Calculates the number of minutes elapsed between two date fields that contain time values.

**Example:**

`ElapsedMinutes ("Date shipped","Date required")`

## ElapsedMonths (DateTimeExpression1,DateTimeExpression2)

Calculates the number of months elapsed between two date fields that contain time values.

**Example:**

`ElapsedMonths ("Date shipped","Date required")`

## ElapsedQuarters (DateExpression1, DateExpression2)

Calculates the number of quarters elapsed between two date fields.

**Example:**

`ElapsedQuarters ("Date shipped","Date required")`

## ElapsedSeconds (DateTimeExpression1,DateTimeExpression2)

Calculates the number of seconds elapsed between two date fields that contain time values.

**Example:**

`ElapsedSeconds ("Date shipped","Date required")`

## ElapsedSemis (DateExpression1,DateExpression2)

Calculates the number of semi-years elapsed between two date fields.

**Example:**

`ElapsedSemis ("Date shipped","Date required")`

## ElapsedWeeks (DateExpression1,DateExpression2)

Calculates the number of weeks elapsed between two date fields that contain time values.

**Example:**

`ElapsedWeeks ("Date shipped","Date required")`

!!! note

    This replaces the two-date custom field operation **Date Difference \> Weeks** available in Ad Hoc views created in Server 5.5 or earlier.

## ElapsedYears (DateExpression1,DateExpression2)

Calculates the number of years between two date fields.

**Example:**

`ElapsedYears ("Date shipped","Date required")`

## EndsWith(TextExpression1, TextExpression2\]

Boolean that returns true if the first text input ends with the string specified in the second input; false otherwise.

**Example:**

`EndsWith("Product Name", 's')`

## IF (BooleanExpression, ExpressionWhenTrue\[, ExpressionWhenFalse\])

Given a Boolean field or calculation as the first argument, returns the second argument if true, optionally returns the third argument if false. Returns null if the first argument is null.

`ExpressionWhenFalse` must be of the same type as `ExpressionWhenTrue`. For example, if `ExpressionWhenTrue` is a date, `ExpressionWhenFalse` must be a date in the same format. If `ExpressionWhenFalse` is not set, then a false result returns a null value.

!!! note

    You can create a `BooleanExpression` using the comparison operators(“==”, “!=”, “\>”, “\>=”, “\<”, “\<=”); any functions that return Boolean values (`StartsWith`, `EndsWith`, `IsNull`, `Contains`) and logical operators (`and`, `or`, `not`).

!!! note

    When dates are used in comparisons or the IF function, they must be the same type, (date only, date/time, or time only). Make sure to use the correct modifier (d, ts, t) when using date constants in comparisons.

**Example:**

`IF(Contains("Product Name", 'Soda'), 'Yes', 'No')` - Uses the Contains function to see whether the product name contains the string "Soda". If it does, sets the field value to Yes.

## Integer('StringExpression')

Casting function that takes a String expression and converts it to an Integer data type. The String can be any expression that returns a supported string, including a field value or an attribute retrieved with the `Attribute()` function. The `Integer()` function requires a String value that can be read as an integer, such as '123'. Other Strings will return an error.

**Examples:**

`Integer('123')`

`Integer(Attribute('my_integer_attribute'))`

## IsNull(Expression)

Boolean that returns true if the field value is null; false otherwise.

**Example:**

`IsNull("First Name")`

## Length(TextExpression)

Given a text string, returns its length. Null values return null.

**Example:**

`Length("First Name")`

## Max (NumericExpression\|DateExpression\[,'Level'\])

Returns the maximum value reached by the specified field or calculation. `Level` can be one of the following: `Current` (default), `ColumnGroup`, `ColumnTotal`, `RowGroup`, `RowTotal`, `Total`. See [Levels in Aggregate Functions](calc-fields-aggregates.md) for more information.

**Example:**

`Max("Salary")`

## Median (NumericExpression\|DateExpression\[,'Level'\])

For an odd number of values, returns the middle value after all values are listed in order. For an even number of values, returns the average of the middle two values. For example, if a field has only five instances, with values {1,1,3,10,20}, the median is 3. `Level` can be one of the following: `Current` (default), `ColumnGroup`, `ColumnTotal`, `RowGroup`, `RowTotal`, `Total`. See [Levels in Aggregate Functions](calc-fields-aggregates.md) for more information.

**Example:**

`Median("Salary")`

## Mid (TextExpression,Integer1,Integer2)

Given a text string, returns the substring starting at Integer1 with length Integer2.

**Example:**

`Mid("Phone", 1, 3)` - Given an American phone number starting with a 3-digit area code, extracts the area code.

## Min (NumericExpression\|DateExpression\[,'Level'\])

Returns the minimum value reached by the specified field or calculation based on an optional level. `Level` can be one of the following: `Current` (default), `ColumnGroup`, `ColumnTotal`, `RowGroup`, `RowTotal`, `Total`. See [Levels in Aggregate Functions](calc-fields-aggregates.md) for more information.

**Example:**

`Min("Salary")`

## Mode (Expression\[,'Level'\])

Returns the most frequent value reached by the specified input, based on an optional level. For example, if a field has only five instances with values {1,2,2,4,5}, the mode is 2. `Level` can be one of the following: `Current` (default), `ColumnGroup`, `ColumnTotal`, `RowGroup`, `RowTotal`, `Total`. See [Levels in Aggregate Functions](calc-fields-aggregates.md) for more information.

**Example:**

`Mode (DayName ("Order Date",RowGroup))` - For each row group, returns the day of the week on which the most orders were placed.

## MonthName (DateExpression)

Returns a text field with the name of the month.

**Example:**

`MonthName ("Order Date" )`

## MonthNumber (DateExpression)

Returns the number of the month, with January = 1 and December = 12. Null values return null.

**Example:**

`MonthNumber ("Order Date")`

## Now (StringExpression)

Returns the current value Date-Time with time zone. The time zone is picked from the logged in user's time zone.

Offset Date and Time for Now Functions

`Offset for Today()` uses only the date. Offset works the same as `Today()` function - filter ranges created with using `Today()` or `Now()` will remember Date-Time and time zone during creation, and if another user with another time zone uses this range, then Date-Time will be offset according to the Time Zone time difference.

!!! note

    When using the *Elapsedhours* calculation, the function `Now()`, which would return Date-Time, needs to be used. The `Today()` function stays as is.

**Example:**

`Offset for Today("")`

## PercentOf (NumericExpression\[,'Level'\])

Returns the value as a percent of the total for the specified level. Null values are ignored. Note that possible values for `Level `are `ColumnGroup`, `ColumnTotal`, `RowGroup`, `RowTotal`, `Total` (default). See [Levels in Aggregate Functions](calc-fields-aggregates.md) for more information.

!!! note

    `PercentOf (NumericExpression, Total)` replaces the custom field calculation **Percent of Total Group** available in Ad Hoc views created in Server 5.5 or earlier.

!!! warning

    Calculated fields using the `PercentOf` function should not be used as filters. If `PercentOf` is used as a filter, then the total percent may not be 100.

**Example:**

`PercentOf("")`

## PeriodOverPeriod (POP) (NumericExpression, 'AggregateFunctionName')

The ratio between last (previous) period and current period is described as:

`AggregateFunction(CurrentValue) / AggregateFunction(PreviousValue) - 1` calculation for the specified field where *AggregateFunction* can be 'Sum', 'Average', 'CountAll', 'CountDistinct', 'Max', 'Median', 'Min', 'Mode', 'Range', 'StdDevP' (Standard Deviation P) or 'StdDevS' (Standard Deviation S). CurrentValue and PreviousValue are row values grouped by date field, where Previous is taken based on selected date categorizer: year, month, quarter etc.

The *PeriodOverPeriod* function accepts *NumericExpression* and *AggregateFunctionName* as string, and then performs calculations based on aggregate functions results.

**Example:**

`PeriodOverPeriod("NumericExpression",'AggregateFunctionName')`

!!! note

    You can only apply POP calculations on the measure field grouped by a date/timestamp field with *year/quarter* by *year/month* by *year* categorizer. Also, these calculations only work for crosstabs and charts. They do not work with tables. Specifically for charts, it is recommended to add the date/timestamp field to both columns (with Year grouping) and rows (Quarter or Month grouping).

## PeriodToPeriod (PTP (NumericExpression, 'AggregateFunctionName')

The difference between last (previous) period and the current period can be described as:

`AggregateFunction(CurrentValue) - AggregateFunction(PreviousValue)` calculation for the specified field where *AggregateFunction* can be 'Sum', 'Average', 'CountAll', 'CountDistinct', 'Max', 'Median', 'Min', 'Mode', 'Range', 'StdDevP' (Standard Deviation P) or 'StdDevS' (Standard Deviation S). CurrentValue and PreviousValue are row values grouped by date field, where Previous is taken based on selected date categorizer: year, month, quarter etc.

The *PeriodToPeriod* function accepts *NumericExpression* and *AggregateFunctionName* as String, and then performs calculations based on aggregate functions results.

Example:

`PeriodToPeriod("NumericExpression",'AggregateFunctionName')`

!!! note

    You can only apply PTP calculations on the measure field grouped by a date/timestamp field with *year/quarter* by *year/month* by *year* categorizer. Also, these calculations only work for crosstabs and charts. They do not work with tables. Specifically for charts, it is recommended to add the date/timestamp field to both columns (with Year grouping) and rows (Quarter or Month grouping).

## Range (NumericExpression\[,'Level'\])

The difference between the largest and smallest values of the given input.

**Example:**

`Range("Salary",'ColumnGroup')`

## Rank (NumericExpression)

Returns the position of each value relative to the other values after all the values are listed in order. For example, the top ten in sales are the top ten in rank. Null values are ignored.

**Example:**

`Rank("Store Sales")`

## Round (NumericExpression\[,Integer\])

Rounds a number to a specified number of digits. Default is zero (0) digits. Decimal values greater than 0.5 are rounded to the next largest whole number, and values less than 0.5 are rounded down.

**Example:**

`Round("Sales")`

## StartsWith(TextExpression1, TextExpression2\]

Boolean that returns true if the first text input starts with the string specified in the second input; false otherwise.

**Example:**

`StartsWith("Product Name", 'Q')`

## StdevP (NumericExpression\[,'Level'\])

Standard deviation is based on the entire population, taken over the values at the specified (optional) level. Null values are excluded. `Level` can be one of the following: `Current` (default), `ColumnGroup`, `ColumnTotal`, `RowGroup`, `RowTotal`, `Total`. See [Levels in Aggregate Functions](calc-fields-aggregates.md) for more information.

**Example:**

`StdevP("Sales",'RowTotal')`

## StdevS (NumericExpression\[,'Level'\])

Standard deviation based on a sample, taken over the values at the specified level. Null values are excluded. `Level` can be one of the following: `Current` (default), `ColumnGroup`, `ColumnTotal`, `RowGroup`, `RowTotal`, `Total`. See [Levels in Aggregate Functions](calc-fields-aggregates.md) for more information.

**Example:**

`StdevS("Sales",'RowTotal')`

## Sum (NumericExpression\[,'Level'\])

The sum of all values in the range. Null values are excluded. `Level` can be one of the following: `Current` (default), `ColumnGroup`, `ColumnTotal`, `RowGroup`, `RowTotal`, `Total`. See [Levels in Aggregate Functions](calc-fields-aggregates.md) for more information.

**Example:**

`Sum("Sales",'RowGroup')`

!!! note

    If an error occurs when using a calculated `Sum` field in a crosstab, ensure the processing logic is shifted to in-memory. This bypasses the query generator’s aggregate limitations and allows the application to handle the data processing.

## Time('StringExpression')

Casting function that takes a String expression in the format 'HH:mm:ss.SSS' and converts it to a Time data type. The String can be any expression that returns a valid String, including a field value or an attribute retrieved with the `Attribute()` function.

**Examples:**

`Time('17:12:33:147')`

`Time(Attribute('my_time_attribute'))`

## Timestamp('StringExpression')

Casting function that takes a String expression in the format 'yyyy-MM-dd HH:mm:ss.SSS' and converts it to a Timestamp data type. The String can be any expression that returns a valid String, including a field value or an attribute retrieved with the `Attribute()` function.

**Examples:**

`Timestamp('2015-07-17 17:12:33:147')`

`Timestamp(Attribute('my_timestamp_attribute'))`

## Today (Integer)

Calculates the date that is the specified number of days from the current system date.

**Examples:**

`Today (0)` - The current system date.

`Today(1)` - The day after the current system date.

`Today(-1)` - The day before the current system date.

## WeightedAverage (NumericExpression1,NumericExpression2,'Level')

Returns the weighted average for the first input weighted with respect to the second input, calculated at an optional level. Null values are excluded. `Level` can be one of the following: `Current` (default), `ColumnGroup`, `ColumnTotal`, `RowGroup`, `RowTotal`, `Total`. See [Levels in Aggregate Functions](calc-fields-aggregates.md) for more information.

**Examples:**

`WeightedAverage ("Price","Units", 'Current')` - The extended price based on the number of units.

`WeightedAverage ("Price","Units", 'RowGroup')` - The sum of the extended price for all units in the row group.

## Year (DateExpression)

Given a date field, returns the year.

**Example:**

`Year("Order Date" )`

## YearToDate (YTD) (NumericExpression, 'AggregateFunctionName')

Given a date field, returns an accumulated aggregated value from a specific start of the fiscal year to the current date. The *YearToDate* function accepts *NumericExpression* and *AggregateFunctionName* as string, and then performs calculations based on aggregate functions results.

Available options for *AggregateFunctionName*: 'Sum', 'Average', 'CountAll', 'CountDistinct', 'Max', 'Median', 'Min', 'Mode', 'Range', 'StdDevP', and 'StdDevS'

!!! note

    You can start the year from a specific month, for example, if your fiscal year starts in July, you can set this to July 1 instead of January 1. Then the first quarter of the year will be July 1 to September 30.

**Example:**

`YearToDate("NumericExpression",'AggregateFunctionName')`

!!! note

    You can only apply YTD calculations on the measure field grouped by a date/timestamp field with *year/quarter* by *year/month* by *year* categorizer. Also, these calculations only work for crosstabs and charts. They do not work with tables. Specifically for charts, it is recommended to add the date/timestamp field to both columns (with Year grouping) and rows (Quarter or Month grouping).
