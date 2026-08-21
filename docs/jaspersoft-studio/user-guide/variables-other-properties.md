---
title: Other Properties of a Variable
description: "The most complex property of a variable is its temporal value. Because its expression is evaluated at every iteration, it is important to understand which value has a variable, and at which time...."
---

# Other Properties of a Variable

The most complex property of a variable is its temporal value. Because its expression is evaluated at every iteration, it is important to understand which value has a variable, and at which time. This can be complicated, considering that a variable can use other variables inside its expression. For these reasons, there are mechanisms that can be used to simplify the evaluation or reading of the variable value during iterations.

## Evaluation Time

Evaluation time is not an attribute of the variable but of elements that can use the variable in their expressions (like a Text Field). Evaluation time determines when the value of the variable should be read. A variable can potentially change value at every iteration, so a value read at one time may be different from the value read another time.

For every element using a variable in its expression, it is possible to say when to evaluate the variable. And because an expression can contain multiple variables, this parameter also influences when these variables are read.

The possible evaluation times are:

- **Report**: The expression is evaluated at the end of the report.

- **Page**: The expression is evaluated at the end of every page of the report.

- **Column**: The expression is evaluated at the end of each column (for a single column report, this is the same as Page).

- **Group**: The expression is evaluated after the break of the specified group (available only if at least one group is defined).

- **Band**: The expression is evaluated after the end of the band where the element with this evaluation time is placed.

- This is a very specific case, introduced to wait until the other elements in the band are completely created. Typically the values of the variables are read at the start of the band. But suppose, for example, you have a subreport with an output parameter to print in the main report. To print this parameter, it must be read after the subreport is computed, so the value can be printed when the band is completely created. In this case, the Band evaluation time is necessary.

- **Auto**: This is used when the expression contains variables and fields that need to be evaluated at different times. The variables are evaluated at a time corresponding to their Reset Type (see below for more information), instead the fields are always evaluated at time -now. This type is useful when report elements have expressions that combine values evaluated at different times (for example, percentage out of a total).

- **Now**: The value of the expression is evaluated after the read of every record, so at every iteration, this is the default behavior.

## Calculation Function

A calculation function is an attribute that specifies when a variable can be used in association with the expression to determine the value of the variable. When using a calculation function, the value of the variable is not determined directly by its expression. Instead, it is passed to the calculation function that uses it to determine its value.

There are many calculation functions built-in to Jaspersoft Studio:

- **Sum**: At every iteration, the variable value is summed. This is one of the cases where the initial value is really important.

- **Count**: At every iteration, the variable value is incremented by one unit (this is only if the expression is not null).

- **Distinct Count:** At every iteration, the variable value is incremented by one unit, but only if the value of the expression was never returned before.

- **Average**: The value of the variable is the arithmetic average of all values received in input from the expression.

- **Lowest**: The variable takes the value of the lowest element received from the expression.

- **Highest**: The variable takes the value of the highest element received from the expression.

- **Standard Deviation**: The standard deviation of all the values received from the expression.

- **First**: The variable takes the value from the first value returned by the expression.

- **System**: No calculation is done and the expression is not evaluated. The value of the variable is the last value set on it. This is useful to store partial results or the final results of a computation.

- **Variance**: The variance of all values returned by evaluation of a report variable’s expression.

## Increment Type

As stated above, when a calculation function is defined, the value of the expression is passed to the function that calculates the variable. By default this occurs for every record read, but sometimes a different behavior is desired. The increment type parameter enables you to change the "time" at which the calculation function is used.

The possible values for this attribute are:

- **Report**: The Calculation Function is called only at the end of the report, passing it to the expression's value at that moment.

- **Page**: The Calculation Function is called at the end of each page, passing to it expression's value at each of those moments.

- **Column**: The Calculation Function is called at the end of each column (for a one-column report, this is the same as Page).

- **Group**: The Calculation Function is called at the start of every occurrence of the specified group. This option is visible only if at least one group is defined.

- **None**: The Calculation Function is called after the read of every record, this is the default behavior.

Remember that the expression is evaluated at every record read, independent of the increment type selected, but the calculation function is used only when the times match those defined in the increment type.

## Reset Type

The reset type specifies when a variable should be reset to its initial value (or to null if no initial value is defined). This is useful when the variable is used to compute a partial value, like a sum or an average of only some of the records read.

The possible values for this attribute are:

- **Report**: The variable is initialized only one time at the beginning of the report creation.

- **Page**: The variable is initialized on each page.

- **Column**: The variable is initialized again in each new column (for a one-column report, this is the same as Page).

- **Group**: The variable is initialized at the start of every occurrence of the specified group. This option is available only if at least one group is defined.

- **None**: The variable is never initialized, so the initial value expression is ignored.

## Incrementer Factory Class Name

The calculation functions are useful, but limited to numeric types. You may have a case where something more specific is needed. Suppose you have a String type field and you want to concatenate the value read. You can do this by defining a new Incrementer. An incrementer is a piece of Java code that extends the `JRIncrementerFactory` interface, and can build a personalized calculation function to do what you need. Every calculation function receives the expression value and the variable value and returns the result of the incrementation, so there is everything needed to do the calculation and return the right value.
