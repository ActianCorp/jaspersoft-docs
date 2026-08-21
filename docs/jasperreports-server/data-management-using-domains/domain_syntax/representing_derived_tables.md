---
title: Representing Derived Tables in XML
description: "To represent derived tables, use the jdbcQuery element. This element is very similar to the jdbcTable element for tables, but contains an additional query element, used to represent the query for the..."
---

# Representing Derived Tables in XML

To represent derived tables, use the `jdbcQuery` element. This element is very similar to the [`jdbcTable`](representing_tables.md) element for tables, but contains an additional query element, used to represent the query for the derived table. `jdbcQuery` is a child of `resources`.

### Table Hierarchy

The following hierarchy is used for `jdbcQuery` elements.

```
<jdbcQuery>
    <fieldList> (1)
        <field> (1...n)
    <filterString> (0...n)
    <query> (1)
```

## jdbcQuery

The `jdbcQuery` element represents a derived table that results from an SQL query. `jdbcQuery` is similar to the jdbcTable element for a table, but has an additional child, `query`, used for the derived table query. `jdbcQuery` is a child of `resources`.

### XML Attributes

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th><p>Attribute</p></th>
<th>Type</th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>datasourceId</code></p></td>
<td>String</td>
<td><p>(Required) Identifier for the data source, as set in the <code>id</code> attribute of <a href="representing_data_sources.md"><code>jdbcDataSource</code></a>. When creating a design file, this alias may be any name you choose, but it must be identical for all tables and derived tables. When uploading the file, the <code>datasourceId</code> automatically becomes the alias associated with the data source defined for the Domain.</p></td>
</tr>
<tr>
<td><p><code>id</code></p></td>
<td>String</td>
<td><p>(Required) Unique identifier for the derived table in the Domain design file. The <code>id</code> of a derived table is used everywhere the <code>id</code> of <code>jdbcTable</code> is used. If you copy a derived table to join it multiple times, each copy must have a different <code>id</code>.</p>
<p>The <code>id</code> XML attribute can contain alphanumeric characters along with any combination of the following: @#$^`_~? It cannot start with a digit.</p></td>
</tr>
</tbody>
</table>

### Child Elements

| Element Name | Description |
|----|----|
| `<fieldList>` | (Required) A container for the `field` elements in the derived table. A `jdbcQuery` element can contain only one `fieldList` element. |
| `<filterString>` | Expression that evaluates to true or false when applied to each row of values in the data source. For a derived table, the expression refers to columns using the `field_name` form of the column ID. See [1.0.1, “Representing Pre-filters in XML,” on page 1](representing_pre-filters.md) for more information. |
| `<query>` | (Required) The SQL query sent to the database server. |

## fieldList

The `fieldList` is a container for the `field` elements in the table. When the derived table is created in the Domain Designer, the set of columns corresponds to the selection of columns in the query result on the **Derived Tables** tab.

### Child Elements

| Element Name | Description |
|----|----|
| `<``field``>` | (Required) A column from the table specified in `jdbcQuery`. |

## field

The `field` element represents in the results of the query. A `field` element of a derived table must reference a column that is returned by the query. Only the columns represented by a `field` element are available for reference by other elements.

### XML Attributes

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th><p>Attribute</p></th>
<th>Type</th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><code>id</code></td>
<td>String</td>
<td><p>(Required) Literal name of the column in the query result. If the query gives an alias to the column in a <code>SELECT AS</code> statement, the <code>id</code> is the same as the alias. The <code>id</code> must be unique within the query results, but not necessarily within the Domain.</p>
<p>The <code>id</code> XML attribute can contain alphanumeric characters along with any combination of the following: @#$^`_~? It cannot start with a digit.</p></td>
</tr>
<tr>
<td><code>type</code></td>
<td>String</td>
<td><p>(Required) The Java type of the column, as determined from the data source by the JDBC driver. The available types are shown in <a href="representing_tables.md">Supported Types</a>.</p></td>
</tr>
</tbody>
</table>

## query

The `query` element contains the SQL query that is sent to the database server. You can use any valid SQL that returns results, as long as the tables and columns in the query exist in the data source, and the columns in the result match the `id` and `type` of all `field` elements of the derived table given in the `fieldList`. SQL queries for a derived table are with respect to the JDBC driver for the data source. The syntax for a valid SQL query does *not* include a closing semi-colon.

You can also use JasperReports Server attributes in queries. See [Using Server Attributes in Design Files](using_server_attributes.md) for more information.

!!! note

    If you are working with a virtual data source, SQL queries are validated against Teiid SQL, which provides DML SQL-92 support with select SQL-99 features. For more information, see the Teiid Reference Guide under the Documentation link on the [Jaspersoft Support Portal](http://support.jaspersoft.com).

In many cases, the easiest way to create a derived table in the XML design file is to create the initial derived table in the Domain Designer and then export the file. When you create a derived table in the Domain Designer, it runs the query and generates columns based on the result set. These columns are present in the export file.

### Example

The following sample query in PostgreSQL selects some columns from the result of a join and orders the results. One of the columns includes a field calculated in the SQL.

Only fields selected in the query – in this case, `exp_date`, `store_id`, `amount`, `currency`, `conv`, and `as_dollars` – can be exposed as columns of the derived table. Fields not selected in the query cannot be referenced in the Domain design.

```
<query>
 select e.exp_date, e.store_id, e.amount, c.currency, c.conversion_ratio conv,
  amount * c.conversion_ratio as_dollars
 from expense_fact e join currency c
  on (e.currency_id = c.currency_id and date(e.exp_date) = c.date)
 order by e.exp_date
</query>
```

!!! warning

    The preceding example is not valid for SQL Server. SQL queries for a derived table are resolved using the JDBC driver for the data source and the derived table becomes a subquery in the generated SQL. SQL Server requires a TOP or FOR XML clause in any subquery that uses ORDER BY.

## Using Derived Tables

A derived table provides an alternate way to create joins and calculated fields. Here are some things to keep in mind when deciding how to implement the Domain:

- Calculated fields created within derived tables may use any function call recognized by the RDBMS. Calculated fields created in the Domain using the `dataSetExpression` attribute of the `field` element are limited to the functions available in the DomEL language. See [Domain Expression Language (DomEL)](../domel/domain_expression_language.md) for more information.
- The Domain mechanism applies filters, aggregation, and joins to derived tables by wrapping the SQL in a nested query, which may be less efficient on some databases than the equivalent query generated for a non-derived table.
