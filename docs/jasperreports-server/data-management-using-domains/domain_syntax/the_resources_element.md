---
title: resources
description: "The resources element contains other elements that define the tables and rows that are accessed through the Domain. It corresponds to the first three tabs of the Domain Designer: Data Management,..."
---

# resources

The `resources` element contains other elements that define the tables and rows that are accessed through the Domain. It corresponds to the first three tabs of the Domain Designer: **Data Management, Joins**, and **Pre-filters**.

The `resources` element contains the `jdbcTable` and `jdbcQuery` elements to represent database tables and derived tables, respectively. Join trees are represented as a `jdbcTable` element with additional contents to define the joins. In order for the Domain to be usable, there must be at least one table, whether as a jdbcTable or jdbcQuery element.

!!! note

    Because the elements under `resources` refer to database objects, they must be externally consistent with the data source for the Domain. For example, the `schemaAlias` and `datasourceTablename` attributes of `jdbcTable` must match the schema and name of a table in the data source.

The `resources` element does not contain presentation elements. It is a direct child of the `schema` element.

### resources Hierarchy

The following hierarchy is used for the `resources` element:

``` xml
<resources>
    <null> (0...1)
        <fieldList> (1)
            <field> (1...n)
    <jdbcTable> (0...n)
        <fieldList> (1)
            <field> (1...n)
        <filterString> (0...n)
    <jdbcQuery> (0...n)
        <fieldList> (1)
            <field> (1...n)
        <filterString> (0...n)
        <query> (1)
    <jdbcTable> (0...n)
        <fieldList> (1)
            <field> (1...n)
        <filterString> (0...n)
        <joinInfo> (1)
        <joinList> (1)
            <join> (1...n)
        <joinOptions> (0...1)
        <tableRefList> (1)
            <tableRef> (1...n)
```

### Child Elements

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>Element Name</p></th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>jdbcTable</code></td>
<td><p>Represents one of the following:</p>
<ul>
<li>A table in the data source or table copy in the Domain (see <a href="representing_tables.md">Representing Tables in XML</a>).</li>
<li>A join in the Domain (see <a href="representing_joins.md">Representing Joins in XML</a>).</li>
</ul></td>
</tr>
<tr>
<td><code>jdbcQuery</code></td>
<td>(Only present if the schema defines derived tables.) Represents a derived table that results from an SQL query. See <a href="representing_derived_tables.md">Representing Derived Tables in XML</a> for more information.</td>
</tr>
<tr>
<td><code>null</code></td>
<td>(Only present if schema defines constant calculated fields.) Container for constant fields.</td>
</tr>
</tbody>
</table>
