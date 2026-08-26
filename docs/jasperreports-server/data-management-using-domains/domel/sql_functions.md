---
title: SQL Functions
description: "DomEL is the primary language used inside the tags in the Domain design file. You can use SQL in the following situations:"
---

# SQL Functions

DomEL is the primary language used inside the tags in the Domain design file. You can use SQL in the following situations:

-   The `query` tag in the derived tables section of the Domain design file expects an SQL function. See [Derived Tables](../advanced_domains/derived_tables.md) for more information.

-   In addition, you may use SQL functions in a DomEL expression, but only in limited circumstances:

    -   The functions must be supported by the database. See the vendor documentation for available functions and their syntax.

    -   The functions must follow the convention of comma-separated parameters. For example, you can use `TRIM(person.name)`, but not `TRIM('Jr' FROM person.name)`

    -   The type of the return values must be appropriate, either within the expression or for the type of the calculated field.

    -   The SQL context must be appropriate for the functions. For example, you cannot use aggregation functions such as `COUNT` in a calculated field because there is no `GROUP BY` clause.

Except for the comma-separated parameter pattern, the DomEL validation cannot enforce these criteria. You must ensure that any SQL functions meet these criteria, otherwise the expression causes errors when using the Domain to create a report.

# The groovy() Function

Groovy is an interpreted language for the JVM. Domains and DomEL use Groovy in the following ways:

-   The `<principalExpression>` tag in an access grant in the Domain Security file uses a Groovy expression to get the current authentication object and determine its access privileges, along with the user and roles associated with the object. In this case, Groovy is used directly inside the tag. See [Securing Data in a Domain](../domain_security/securing_data_in_a_domain.md) for more information.

-   You can use the DomEL `groovy()` function as part of a DomEL expression. The DomEl `groovy` function takes a single string argument that is interpreted as Groovy code. The output of the function is a string that is put into the SQL. To include Groovy, use the following syntax:

`groovy('your groovy code here')`

-   For example, the following simple expression could be used to set the value of the calculated field `e.groovyEval` to the SQL string corresponding to the value of 5.0/6:

`<field id="e.groovyEval" dataSetExpression="groovy('(5.0/6).toString()')" type="java.lang.String" />`

DomEL validation cannot check your Groovy code. You must ensure that any Groovy code meets these criteria, otherwise the expression causes errors when using the Domain to create a report.

# Complex Expressions

Complex expressions are written by grouping any of the operators or functions above. Parentheses `()` may be used for grouping boolean operators, but arithmetic expressions that rely on parentheses are not supported. To compute complex arithmetic expressions, you may need to define several expressions as separate calculated fields, and then reference them in a simpler expression in another calculated field.

The following examples show complex expressions suitable for filters. This first one selects only stores in Western states of the US:

`s1.store_country in ('USA') and s1.store_state in ('WA', 'OR', 'CA', 'NV')`

The following filter expression uses a date range:

`s1.first_opened_date in ( Date( '2000-01-01' ) : Date( '2004-12-31' )) and not( s1.closed )`

As shown in these examples, field values are often compared to constant values such as `'USA'`. Therefore, the author of the design file must ensure that values used in a DomEL expression exist in the data source. Otherwise, a wrong value might go undetected and impact the quality of data in reports based on the Domain. The Domain Designer determines values for comparison by accessing the data source, so if you export a design file, you can use the values it has found. Another way to reduce errors and also support future data changes is to use more general expressions such as:

`s1.store_country in ('US', 'USA', 'United States')`
