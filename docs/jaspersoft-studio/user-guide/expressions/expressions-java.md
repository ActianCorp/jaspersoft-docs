---
title: Using Java as a Language for Expressions
description: Java was the first language supported by JasperReports and is still the most commonly-used language as well as being the default.
---

# Using Java as a Language for Expressions

Java was the first language supported by JasperReports and is still the most commonly-used language as well as being the default.

Following are some examples of Java expressions:

-   `“This is an expression”`

-   `new Boolean(true)`

-   `new Integer(3)`

-   `(($P{MyParam}.equals("S")) ? "Yes" : "No")`

The first thing to note is that each of these expressions represents a Java Object, meaning that the result of each expression is a non-primitive value. The difference between an object and a primitive value makes sense only in Java, but it is very important: a primitive value is a pure value like the number 5 or the Boolean value true.

Operations between primitive values have as a result a new primitive value, so the expression:

`5+5`

results in the primitive value 10. Objects are complex types that can have methods, can be null, and must be “instanced” with the keyword “new” most of the time. In the second example above, for instance (`new Boolean(true)`), we must wrap the primitive value `true` in an object that represents it.

By contrast, in a scripting language such as Groovy and JavaScript, primitive values are automatically wrapped into objects, so the distinction between primitive values and objects wanes. When using Java, the result of our expression must be an object, which is why the expression 5+3 is not legal as-is but must be fixed with something like this:

`new Integer( 5 + 3 )`

The fix creates a new object of type `Integer` representing the primitive value 8.

So, if you use Java as the default language for your expressions, remember that expressions like the following are not valid:

-   `3 + 2 * 5`

-   `true`

-   `(($P{MyParam} == 1) ? "Yes" : "No")`

These expressions don’t make the correct use of objects. In particular, the first and the second expressions are not valid because they are of primitive types (`integer` in the first case and `boolean` in the second case) which do not produce an object as a result. The third expression is not valid because it assumes that the `MyParam` parameter is a primitive type and that it can be compared through the == operator with an `int`, but it cannot. In fact, we said that parameters, variables, and fields are always objects and primitive values cannot be compared or used directly in a mathematical expression with an object.
