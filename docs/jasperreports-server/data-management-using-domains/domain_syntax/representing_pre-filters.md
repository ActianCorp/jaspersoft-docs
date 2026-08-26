---
title: Representing Pre-filters in XML
description: "Pre-filters are defined as optional filterString elements inside of jdbcTable and jdbcQuery elements. They impose a condition on any results returned for that table, query, or join tree, thereby..."
---

# Representing Pre-filters in XML

Pre-filters are defined as optional `filterString` elements inside of `jdbcTable` and `jdbcQuery` elements. They impose a condition on any results returned for that table, query, or join tree, thereby limiting the number of rows returned when accessing the data source. Whereas other settings mainly determine which columns are available for use in a report, a pre-filter determines which rows are available when running the report.

## filterString

`filterString` contains an expression that evaluates to true or false when applied to each row of values in the data source. The parent of `filterString` is one of the following:

-   A [`jdbcTable`](representing_tables.md) element for a table
-   A [`jdbcTable`](representing_joins.md) element for a join
-   A [`jdbcQuery`](representing_derived_tables.md) element

The expression refers to columns using their `id` attribute. Thus, a filter on a table or derived table refers to the simple column name, but a filter on a join tree refers to the `table_ID.field_name`. The full syntax for the expression is documented in [Domain Expression Language (DomEL)](../domel/domain_expression_language.md).

!!! warning

    Filters defined in the Domain Designer are limited to conditions on one column or comparisons of two columns, with more complex filters created by the conjunction (logical AND) of several conditions. Other filter expressions are not supported. You can upload a design file with more complex filters, but these filters are not editable in the Domain Designer.

### Examples

The following is an example of the `filterString` used in a `jdbcTable` element representing a table:

``` xml
<jdbcTable datasourceId="SugarCRMDataSource" id="opportunities"
        schemaAlias="public" datasourceTableName="opportunities">
    <fieldList>
        ...
        <field id="opportunity_type" type="java.lang.String"/>
    </fieldList>
    <filterString>opportunity_type == 'Existing Business'</filterString>
</jdbcTable>
```

The following is an example of the `filterString` used in a `jdbcQuery` element:

``` xml
<jdbcQuery datasourceId="SugarCRMDataSource" id="p1cases">
    <fieldList>
        ...
        <field id="status" type="java.lang.String"/>
    </fieldList>
    <filterString>status != 'closed'</filterString>
    <query>...</query>
</jdbcQuery>
```
