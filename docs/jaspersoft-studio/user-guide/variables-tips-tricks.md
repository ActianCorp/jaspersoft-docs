---
title: "Tips & Tricks"
description: "Pay attention to the variable type. For example, if your expression returns a number but the variable type is string (the default type) then its value is always zero."
---

# Tips & Tricks

Pay attention to the variable type. For example, if your expression returns a number but the variable type is string (the default type) then its value is always zero.

The form of the expression is very important for the computation of a value, especially when the variable itself is used in the expression. Consider the following example:

A field with the name `Money_Gained` with an integer value, which could be null, is read from the data source.

A variable `Total1` with the expression:<br>
`IF(EQUALS($F{Money_Gained}, null), $V{Total1}, $V{Total1}+$F{Money_Gained})`<br>
initial value zero, and no calculation function;

A variable `Total2` with the expression<br>
`$V{Money_Gained} == null ? $V{Total2} : $V{Total2}+$F{Money_Gained}`<br>
initial value zero, and no calculation function;

The two expressions seem equivalent. They both add the money gained to the variable when it is not null (remember that if there is no calculation function, the value of the expression is assigned to the variable). The check if the `Money_Gained` has a null value is necessary because the sum of a number with the value null is null. So adding null to Total1 or Total2 changes the variable to null. But even with this check when `Money_Gained` becomes null for the first time even `Total1` is null, instead `Total2` has the correct value.

This happens because these two expressions have different interpreters, the first is interpreted by Groovy, the second by Java. The Java behavior evaluates the condition and then selects the correct branch. The Groovy behavior computes the two branches, then evaluates the expression, and finally returns the correct branch. Doing this adds the null value to `Total1` before doing the check, and makes `Total1` null. To avoid this, use the variable in the main branch only, for example `Total1` could be rewritten as:<br>
`$V{Total1} + IF(EQUALS($F{Money_Gained}, null),0,F{Money_Gained})`.

The syntax is still interpreted by Groovy, but now the variable is out of the `IF` branches, so even if they are both evaluated, the variable maintains its value.
