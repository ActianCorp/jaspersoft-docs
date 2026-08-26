---
title: Base Properties of a Variable
description: "At a minimum, all variables must have the following defined:"
---

# Base Properties of a Variable

At a minimum, all variables must have the following defined:

-   **Name**: A string that is used to refer to a variable. It is necessary to use this variable inside other expressions like the evaluation of a Text Field or the computation of another variable. Use the following syntax to refer to a variable: **$V{variable_name}**.

-   **Type**: Necessary because a variable is an object that is probably used in other expressions, so its type must be known to be manipulated correctly.

-   **Expression**: The function used to define the variable value, it can be composed of more fields and variables, which could be logic operators, math operators and so on. Jaspersoft Studio provides an expression editor. To open it, click the button to the right of the expression text field. The expression is evaluated on each iteration (every time a record is read from the data source). If no calculation function is defined, the result of the expression is assigned to the variable. So it is important that the result has a type compatible with the one in the variable.

-   **Initial Value**: The value assumed from the variable at the beginning, before the first computation of its expression. The initial value is an expression itself, so it can be defined through the expression editor.

-   It is not mandatory, but it is good practice to define an initial value. For example, if you have a variable called **variable1** with the expression **new Integer(5)**, at every iteration, the variable is assigned the integer value 5. In this context, the initial value is not important. But if you change the expression to **$V{variable1}+5**, at every iteration, the variable is incremented by 5. In this case, an initial value is necessary because if the **variable1** is undefined at the first iteration, all future evaluations break.
