---
title: Using Groovy as a Language for Expressions
description: "The modular architecture of JasperReports provides a way to plug in support for languages other than Java. By default, the library supports Groovy and JavaScript."
---

# Using Groovy as a Language for Expressions

The modular architecture of JasperReports provides a way to plug in support for languages other than Java. By default, the library supports Groovy and JavaScript.

Groovy is a full language for the Java 2 Platform. Inside the Groovy language you can use all classes and JARs that are available for Java. The following table compares some typical JasperReports expressions written in Java and Groovy:

**Groovy and Java code samples**

| Expression | Java | Groovy |
|----|----|----|
| Field | `$F{field_name}` | `$F{field_name}` |
| Sum of two double fields | `new Double($F{f1}.doubleValue() + $F{f2}.doubleValue())` | `$F{f1} + $F{f2}` |
| Comparison of numbers | `new Boolean($F{f}.intValue() == 1)` | `$F{f} == 1` |
| Comparison of strings | `new Boolean($F{f} != null && $F{f}.equals("test"))` | `$F{f} == "test"` |

The following is a correct Groovy expression:

`new JREmptyDataSource($F{num_of_void_records})`

`JREmptyDataSource` is a class of JasperReports that creates an empty record set (meaning with the all fields set to null). You can see how you can instance this class (a pure Java class) in Groovy without any problem. At the same time, Groovy allows you to use a simple expression like this one:

`5+5`

The language automatically encapsulates the primitive value 10 (the result of that expression) in a proper object. Actually, you can do more: you can treat this value as an object of type `String` and create an expression such as:

`5 + 5+ ”my value”`

Whether or not such an expression resolves to a rational value, it is still a legal expression and the result is an object of type `String` with the value:

`10 my value`

Hiding the difference between objects and primitive values, Groovy allows the comparison of different types of objects and primitive values, such as the legal expression:

`$F{Name} == “John”`

This expression returns true or false, or, again:

|  |  |
|----|----|
| `$F{Age} > 18 ` | Returns true if the `Age` object interpreted as a number is greater than 18. |
| `“340” < 100` | Always returns false. |
| `“340”.substring(0,2) < 100` | Always returns true (since the substring method call produces the string “34”, which is less than 100). |

Groovy provides a way to greatly simplify expressions and never complains about null objects that can crash a Java expression throwing a `NullPointerException`. It really does open the doors of JasperReports to people who don’t know Java.
