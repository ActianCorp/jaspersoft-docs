---
title: Domain Expression Language (DomEL)
description: "A DomEL expression is a shorthand way of writing a complex query. Many components of a Domain need to compute values based on some expression involving constants, field values, and environment..."
---

# Domain Expression Language (DomEL)

A DomEL expression is a shorthand way of writing a complex query. Many components of a Domain need to compute values based on some expression involving constants, field values, and environment variables. The Domain Expression Language (DomEL) was created to fill this need. Currently, the following features in XML design files are expressed in DomEL:

-   The `IN` clause for custom joins
-   Calculated fields
-   Filter expressions in Domains and Domain topics (equivalent to `where` clauses)
-   Server attribute values (see [Using Server Attributes in Design Files](../domain_syntax/using_server_attributes.md))
-   Row-level security (see [Securing Data in a Domain](../domain_security/securing_data_in_a_domain.md))

When processing a report based on a Domain, the server interprets DomEL expressions to generate parts of the SQL expression that perform the desired query. Depending on the data policy, either the augmented SQL is passed to the data source, or the server performs a simpler query and applies the DomEL expressions to the full dataset in memory.

This chapter contains the following sections:

-   Datatypes
-   [Field References](field_references.md)
-   [Operators and Functions](operators_and_functions.md)
-   [SQL Functions](sql_functions.md)
-   [The groovy() Function](sql_functions.md)
-   [Complex Expressions](sql_functions.md)
-   [Return Types](return_types.md)

## Datatypes

The following simple datatypes may be declared as constants, used in expressions, and returned as values:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th><p>Simple Type</p></th>
<th><p>Description</p></th>
<th><p>Example of Constant</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>boolean</p></td>
<td><p>Expressions such as comparison operators return boolean values, but <code>true</code> and <code>false</code> constants are undefined and cannot be used.</p></td>
<td><p>none</p></td>
</tr>
<tr>
<td><p>integer</p></td>
<td><p>Whole numbers.</p></td>
<td><p><code>123</code> or <code>-</code><code>123</code></p></td>
</tr>
<tr>
<td><p>decimal</p></td>
<td><p>Floating point numbers. Decimal separator must be a period (<code>.</code>); other separators such as comma (<code>,</code>) are not supported.</p></td>
<td><p><code>123.45</code> or <code>-123.45</code></p></td>
</tr>
<tr>
<td><p>string</p></td>
<td><p>Character string entered with single quotes (<code>'</code>); double quotes (<code>"</code>) are not supported.</p></td>
<td><p>'hello world'</p></td>
</tr>
<tr>
<td><p>date</p></td>
<td><p>ANSI standard date.</p></td>
<td><p><code>d'2009-03-31'</code> or<br />
<code>Date('2009-03-31')</code></p></td>
</tr>
<tr>
<td><p>timestamp</p></td>
<td><p>ANSI standard date and time.</p></td>
<td><p><code>ts'2009-03-31</code> 23:59:59<code>'</code> or<br />
TimeStamp('2009-03-31 23:59:59')</p></td>
</tr>
</tbody>
</table>

The composite datatypes, shown in the following table, may be declared as constants and used with the `in set` or `in range` operator. The values in these composite types are not necessarily constant, they could be determined by field values.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th><p>Composite Type</p></th>
<th><p>Description</p></th>
<th><p>Example</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>set</p></td>
<td><p>Contains any number of any simple type above.</p></td>
<td><p><code>(1, 2, 3)('apples','oranges')</code><br />
</p></td>
</tr>
<tr>
<td><p>range</p></td>
<td><p>Inclusive range applicable to numbers and dates, including fields that are number or date types.</p></td>
<td><p><code>(0:12)</code> or <code>(0.0:12.34)(d'2009-01-01':d'2009-12-31')(limit_min:limit_max)</code><br />
<br />
</p></td>
</tr>
</tbody>
</table>
