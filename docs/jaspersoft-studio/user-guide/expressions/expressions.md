---
title: Expressions
description: "Many settings in a report are defined by formulas, such as conditions that can hide an element, special calculations, or text processing that requires knowledge of a scripting language."
---

# Expressions

Many settings in a report are defined by formulas, such as conditions that can hide an element, special calculations, or text processing that requires knowledge of a scripting language.

Formulas can be written in at least three languages, two of which (JavaScript and Groovy) can be used without knowledge of programming methods.

All formulas in JasperReports are defined through expressions. The default expression language is Java, but if you are not a programmer, we recommend JavaScript or Groovy, because those languages remove Java complexity. The language is a property of the document. To set it, select the document root node in the Outline view and choose your language in the `Language` property in the **Properties** view.

An expression is a formula that operates on some values and returns a result, like a formula in a spreadsheet cell. A cell can have a simple value or a complex formula that refers to other values. In a spreadsheet, you refer to values contained in other cells; in JasperReports you use the report fields, parameters, and variables. Whatever is in your expression, when it is computed, it returns a value (which can be null).

This chapter contains the following sections:

- [Expression Types](expressions.md)

- [Expression Operators and Object Methods](expressions.md)

- [Using an If-Else Construct in an Expression](expressions.md)

- [Using Unicode Characters in Expressions](../fonts-characters.md)

- [Using Java as a Language for Expressions](expressions-java.md)

- [Using Groovy as a Language for Expressions](expressions-groovy.md)

- [Using JavaScript as a Language for Expressions](expressions-javascript.md)

## Expression Types

An expression's type is determined by the context in which the expression is used. For example, if your expression is used to evaluate a condition, the expression should be Boolean (true or false); if you are creating an expression to display in a text field, it is probably a String or a number (Integer or Double). Using the right type is crucial; JasperReports requires precision when choosing an expression type.

Some of the most important Java types are:

|  |  |
|----|----|
| `java.lang.Boolean` | Defines an Object that represents a Boolean value such as true and false |
| `java.lang.Byte` | Defines an Object that represents a byte |
| `java.lang.Short` | Defines an Object that represents a short integer |
| `java.lang.Integer` | Defines an Object that represents integer numbers |
| `java.lang.Long` | Defines an Object that represents long integer numbers |
| `java.lang.Float` | Defines an Object that represents floating point numbers |
| `java.lang.Double` | Defines an Object that represents real numbers |
| `java.lang.String` | Defines an Object that represents a text |
| `java.util.Date` | Defines an Object that represents a date or a timestamp |
| `java.lang.Object` | A generic java Object |

If an expression is used to determine the value of a condition that determines, for instance, whether an element should be printed, the return type is `java.lang.Boolean`. To create it, you need an expression that returns an instance of a Boolean object. Similarly, if an expression shows a number in a text field, the return type is `java.lang.Integer` or `java.lang.Double`.

JavaScript and Groovy are not formal about types because they are not typed languages. The language itself treats a value in the best way by trying to guess the value type or by performing implicit casts (conversion of the type).

## Expression Operators and Object Methods

Operators in Java, Groovy, and JavaScript are similar because these languages have the same basic syntax. Operators can be applied to a single operand (unary operators) or on two operands (binary operators). The following table shows a number of operators, but it is not a complete list. For example, there is a unary operator to add 1 to a variable (++), but it is easier to use x + 1.

| Operator | Description | Example |
|----|----|----|
| `+` | Sum (it can be used to sum two numbers or to concatenate two strings) | `A + B` |
| `-` | Subtraction | `A - B` |
| `/` | Division | `A / B` |
| `%` | Rest, it returns the rest of an integer division | `A % B` |
| `||` | Boolean operator OR | `A || B` |
| `&&` | Boolean operator AND | `A && B` |
| `==` | Equals | `A == B` |
| `!=` | Not equals | `A != B` |
| `!` | Boolean operator NOT | `!A` |

Expression operators

!!! note

    - Regarding the Equals operator: in Java, the `==` operator can only be used to compare two primitive values. With objects, you need to use the special method “`equals`”; for example, you cannot write an expression like `"test" == "test"`, you need to write `"test".equals("test")`.

    - Regarding the Equals operator: In Java, the `!=` operator can only be used to compare two primitive values.

Within an expression, you can use the syntax summarized in Syntax for referring to report objects to refer to the parameters, variables, and fields defined in the report.

<table>
<caption><p>Syntax for referring to report objects</p></caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>Syntax</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>$F{name_field}</code></p></td>
<td><p>Specifies the <code>name_field</code> field ("F" means field).</p></td>
</tr>
<tr>
<td><p><code>$V{name_variable}</code></p></td>
<td><p>Specifies the <code>name_variable</code> variable.</p></td>
</tr>
<tr>
<td><p><code>$P{name_parameter}</code></p></td>
<td><p>Specifies the <code>name_parameter</code> parameter.</p></td>
</tr>
<tr>
<td><p><code>$P!{name_parameter}</code></p></td>
<td><p>Special syntax is used in the report SQL query to indicate that the parameter does not have to be dealt as a value to transfer to a prepared statement, but that it represents a little piece of the query.</p></td>
</tr>
<tr>
<td><p><code>$R{resource_key}</code></p></td>
<td><p>Special syntax for localization of strings.</p></td>
</tr>
<tr>
<td><code>$X{functionName, col_name, param1,[param2]}</code></td>
<td><p>Syntax for complex queries, such as comparing a column value to a parameter value. Based on the function in the first argument, JasperReports constructs a SQL clause. The following functions are available:</p>
<ul>
<li>Functions expecting three arguments for <code>$X</code> – <code>EQUAL</code>, <code>NOTEQUAL</code>, <code>LESS</code>, <code>LESS]</code> (less than or equal to), <code>GREATER</code>, <code>[GREATER</code> (greater than or equal to), <code>IN</code>, <code>NOTIN</code>. For example:</li>
</ul>
<p><code>$X{EQUAL, order_date, date_parameter}</code></p>
<ul>
<li>Functions expecting four arguments for <code>$X</code> –</li>
</ul>
<p><code>BETWEEN</code> (excludes both endpoints)</p>
<p><code>BETWEEN]</code> (includes right endpoint)</p>
<p><code>[BETWEEN</code> (includes left endpoint)</p>
<p><code>[BETWEEN]</code> (includes both endpoints)</p>
<p>For example:</p>
<p><code>$X{BETWEEN, order_date, start_date_param, end_date_param}</code></p></td>
</tr>
</tbody>
</table>

In summary, fields, variables, and parameters represent objects; specify their type when you declare them within a report.

Although expressions can be complicated, usually it is a simple operation that returns a value. There is a simple if-else expression that is very useful in many situations. An expression is just an arbitrary operation that any stage must represent a value. In Java, these operators can be applied only to primitive values, except for the sum operator (+). The sum operator can be applied to a String expression with the special meaning of concatenate. For example:

`$F{city} + “, ” + $F{state}`

results in a string like:

`San Francisco, California`

Any object in an expression can include methods. A method can accept zero or more arguments, and it can return or not a value. In an expression you can use only methods that return a value; otherwise, you would have nothing to return from your expression. The syntax of a method call is:

`Object.method(argument1, argument2, <and so on,>)`

Some examples:

| Expression                               | Result  |
|------------------------------------------|---------|
| `“test”.length()`                        | `4`     |
| `“test”.substring(0, 3)`                 | `“tes”` |
| `“test”.startsWith(“A”)`                 | `false` |
| `“test”.substring(1, 2).startsWith(“e”)` | `true`  |

The methods of each object are usually explained in the JasperReports Library Javadocs, that is available at <http://jasperreports.sourceforge.net/api/>.

You can use parentheses to isolate expressions and make the overall expression more readable.

## Using an If-Else Construct in an Expression

A way to create an if-else-like expression is by using the special question mark operator. For example:

`(($F{name}.length() > 50) ? $F{name}.substring(0,50) : $F{name})`

The syntax is` (<condition>) ? <value on true> : <value on false>`. It is extremely useful, and can be recursive, meaning that the value on `true` and `false` can be represented by another expression that can be a new condition:

`(($F{name}.length() > 50) ? `

`(($F{name}.startsWith(“A”)) ? “AAAA” : “BBB”)`

` :`

` $F{name})`

This expression returns the String `AAAA` when the value of the field name is longer than 50 characters and starts with A, returns BBB if it is longer than 50 characters but does not start with A, and, finally, returns the original field value if neither of these conditions is true.

Despite the possible complexity of an expression, it can be insufficient to define a needed value. For example, if you want to print a number in Roman numerals or return the name of the weekday of a date, it is possible to transfer the elaborations to an external Java class method, which must be declared as static, as shown in the following example:

`MyFormatter.toRomanNumber( $F{MyInteger}.intValue() )`

The function operand `toRomanNumber` is a static method of the `MyFormatter` class, which takes an `int` as argument (the conversion from Integer to `int` is done by means of the `intValue()` method; it is required only when using Java as language) and gives back the Roman version of a number in a lace.

This technique can be used for many purposes. For example, to read the text from a CLOB field or to add a value into a `HashMap` (a Java object that represents a set of key/value pairs).
