---
title: Representing Tables in XML
description: "To represent tables, use the jdbcTable element. A table is a child of the resources element."
---

# Representing Tables in XML

To represent tables, use the `jdbcTable` element. A table is a child of the `resources` element.

### Table Hierarchy

The following hierarchy is used for `jdbcTable` elements when representing a table from the data source.

```
<jdbcTable>
    <fieldList> (1)
        <field> (1...n)
    <filterString> (0...n)
```

## jdbcTable

The `jdbcTable` element represents a table or a copy of a table in the data source. A Domain design must reference all the tables it needs to access, including tables that you need to construct the Domain but do not want to expose to the end user. `jdbcTable` is a child of the `resources` element.

!!! note

    The `jdbcTable` element is also used with different attributes to describe join trees. See [Representing Joins in XML](representing_joins.md).

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
<td><p>(Required) Unique identifier for the table in the Domain design file. If you copy a table to join it multiple times, each copy has the same <code>datasourceId</code>, <code>schemaAlias</code>, and <code>datasourceTableName</code> but must have a different <code>id</code>. To set a table <code>id</code> in the Domain Designer, right-click the table and select <code>Rename Table</code> from the context menu.</p>
<p>The <code>id</code> XML attribute can contain alphanumeric characters along with any combination of the following: @#$^`_~? It cannot start with a digit.</p>
When generated via the Domain Designer, <code>id</code> is a representation of the table name in the data source, with unsupported characters replaced by underscores.</td>
</tr>
<tr>
<td><code>schemaAlias</code></td>
<td> </td>
<td><p>Name of the database schema in the data source. Required if the data source uses schemas.</p>
<ul>
<li>For schemaless data sources, such as MySQL, <code>schemaAlias</code> is not required.</li>
<li>For schema-based data sources, such as PostgreSQL and Oracle, the name is the literal name of the schema in the data source, for example, <code>public</code>.</li>
<li>For schemaless data sources within a virtual data source, the schema name is of the form <code>dataSourcePrefix</code>, where <code>dataSourcePrefix</code> is the data source prefix defined when the virtual data source was created. For example, <code>FoodmartDataSource</code>.</li>
<li>For schema-based data sources within a virtual data source, the name is in the form <code>dataSourcePrefix_schema</code>, where <code>dataSourcePrefix</code> is the data source prefix defined when the virtual data source was created. For example, <code>FoodmartDataSource_public</code>.</li>
</ul></td>
</tr>
<tr>
<td><code>datasourceTableName</code></td>
<td>String</td>
<td><p>(Required) Literal name of the table in the data source.</p></td>
</tr>
</tbody>
</table>

### Child Elements

| Element Name | Description |
|----|----|
| `<fieldList>` | (Required) A container for the `field` elements in the table. Each `jdbcTable` element can contain only one `fieldList` element. |
| `<filterString>` | Expression that evaluates to true or false when applied to each row of values in the data source. For a table, the expression refers to columns using the `field_name` form of the column ID. See [Representing Pre-filters in XML](representing_pre-filters.md) for more information. |

## fieldList

`fieldList` is a container for one or more `field` elements.

In the Domain Designer, you can select only entire tables, not individual columns. In the XML design file, however, you can specify any subset of columns that you need.

### Child Elements

| Element Name | Description                                                  |
|--------------|--------------------------------------------------------------|
| `<field>`    | (Required) A column from the table specified in `jdbcTable`. |

## field

The `field` element represents a column in the data source. The column must be from the table specified by `jdbcTable`. You must reference all the columns you use in the Domain, including columns that are used to construct the Domain but are not exposed to the end user.

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
<td><code>fieldDBName</code></td>
<td>String</td>
<td>Literal name of the column in the data source.</td>
</tr>
<tr>
<td><code>id</code></td>
<td>String</td>
<td><p>(Required) Identifier for the column. As in the JDBC model that the data source is based on, the <code>id</code> must be unique within the <code>jdbcTable</code>, but not necessarily within the Domain.</p>
<p>The <code>id</code> XML attribute can contain alphanumeric characters along with any combination of the following: @#$^`_~? It cannot start with a digit.</p>
When generated via the Domain Designer, <code>id</code> is a representation of the column name in the data source, where unsupported characters replaced by underscores.</td>
</tr>
<tr>
<td><code>type</code></td>
<td>String</td>
<td>(Required) The Java type of the column, as determined from the data source by the JDBC driver. The available types are shown below.</td>
</tr>
</tbody>
</table>

### Supported Types

The following Java types are supported for the `type` attribute:

<table>
<tbody>
<tr>
<td><p><code>java.lang.Boolean</code></p></td>
<td><p><code>java.lang.Float</code></p></td>
<td><p><code>java.lang.String</code></p></td>
<td rowspan="2"><code>java.sql.Timestamp</code></td>
</tr>
<tr>
<td><p><code>java.lang.Byte</code></p></td>
<td><p><code>java.lang.Integer</code></p></td>
<td><p><code>java.math.BigDecimal</code></p></td>
</tr>
<tr>
<td><p><code>java.lang.Character</code></p></td>
<td><p><code>java.lang.Long</code></p></td>
<td><p><code>java.sql.Date</code></p></td>
<td rowspan="2"><code>java.util.Date </code></td>
</tr>
<tr>
<td><p><code>java.lang.Double</code></p></td>
<td><p><code>java.lang.Short</code></p></td>
<td><p><code>java.sql.Time</code></p></td>
</tr>
</tbody>
</table>

Unless you know the name and type of every column in the data source, it is often easier to select the tables you want in the Domain Designer and then export the XML design file. The Domain Designer accesses the data source to find the names of all tables and columns, as well as their types. You can then modify the exported design.

!!! note

    If you have proprietary types in your database, the server may not be able to map its Java type from the JDBC driver. You can configure the mapping for proprietary types, as described in the JasperReports Server Administrator Guide.

    Alternatively, you can override any mapping by specifying the `type` attribute for any given field in the XML design file. The server uses this Java type for the field, regardless of its mapping. If your proprietary type can't be cast in the specified type, the server raises an exception.
