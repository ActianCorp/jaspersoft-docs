---
title: Representing Joins in XML
description: A join is represented in the design file as a jdbcTable element. A join tree is a child of the resources element.
---

# Representing Joins in XML

A join is represented in the design file as a `jdbcTable` element. A join tree is a child of the `resources` element.

!!! note

    The `jdbcTable` element is also used to represent tables from the data source. See [Representing Tables in XML](representing_tables.md).

## Element Hierarchy for a Join Tree

The following hierarchy is used to represent a join tree.

``` xml
<jdbcTable>
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

## jdbcTable

The `jdbcTable` element is also used to represent a join tree, that is, the results of one or more joins between tables. There is one `jdbcTable` element for each join tree. `jdbcTable` is a child of `resources`.

!!! note

    `jdbcTable` can also be used to represent a table. See [Representing Tables in XML](representing_tables.md) for more information.

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
<td><p><code>id</code></p></td>
<td>String</td>
<td><p>(Required) Unique identifier for the join tree in the Domain design. In the Domain Designer, each join tree is automatically given the ID <code>JoinTree_n</code>, where <code>n</code> is a sequential number. In the design file, you can give the join any name, as long as it is unique among all tables and derived tables.</p>
<p>The <code>id</code> XML attribute can contain alphanumeric characters along with any combination of the following: @#$^`_~? It cannot start with a digit.</p></td>
</tr>
<tr>
<td><p><code>datasourceId</code></p></td>
<td>String</td>
<td><p>(Required) Alias that identifies the data source for the Domain. When creating a design file, this alias may be any name you choose, but it must be identical for all tables and derived tables. When uploading the file, the <code>datasourceId</code> automatically becomes the alias associated with the data source defined for the Domain.</p></td>
</tr>
<tr>
<td><code>schemaAlias</code></td>
<td> </td>
<td><p>Name of the database schema for the first table in the join tree. Required if the data source uses schemas.</p>
<ul>
<li>For schemaless data sources, such as MySQL, <code>schemaAlias</code> is not required.</li>
<li>For schema-based data sources, such as PostgreSQL and Oracle, the name is the literal name of the schema in the data source. For example, <code>public</code>.</li>
<li>For schemaless data sources within a virtual data source, the schema name is of the form <code>dataSourcePrefix</code>, where <code>dataSourcePrefix</code> is the data source prefix defined when the virtual data source was created. For example, <code>FoodmartDataSource</code>.</li>
<li>For schema-based data sources within a virtual data source, the name is in the form <code>dataSourcePrefix_schema</code>, where <code>dataSourcePrefix</code> is the data source prefix defined when the virtual data source was created. For example, <code>FoodmartDataSource_public</code>.</li>
</ul></td>
</tr>
<tr>
<td><code>datasourceTableName</code></td>
<td>String</td>
<td><p>(Required) Literal name of the first table in the join tree.</p></td>
</tr>
</tbody>
</table>

!!! warning

    If you use the `jdbcQuery` element to define derived tables, you may have additional join trees in your Domain.

The Domain Designer automatically exposes all columns of all tables in a join, but in the design file you need to specify only those columns you want to reference elsewhere in the Domain.

### Child Elements

| Element Name | Description |
|----|----|
| `<``fieldList``>` | (Required) A container for the `field` elements in the join tree. A `jdbcTable` element can contain only one `fieldList` element. |
| `<`[`filterString`](representing_pre-filters.md)`>` | Expression that evaluates to true or false when applied to each row of values in the data source. For a join tree, the expression refers to columns using the `table_ID.field_name` form of the column ID. See [Representing Pre-filters in XML](representing_pre-filters.md) for more information. |
| `<``joinInfo``>` | (Required) Gives the table ID and alias for the table specified by the `schemaAlias` and `datasourceTableName` attributes. The table ID and alias are used as the first table in the join definition. This element and its two attributes are required even if they are identical. |
| `<``joinList``>` | (Required) Container for the `join` elements. A `jdbcTable` element can contain only one `joinList` element. The left join in the first `join` in the `joinList` must be the table specified by the `schemaAlias` and `datasourceTableName` attributes of `jdbcTable`. |
| `<``joinOptions``>` | Specifies options for the join tree that influence how the joins that are pushed down to SQL in an Ad Hoc view. |
| `<``tableRefList``>` | (Required) Container for the list of tables and aliases used in the join. Must include a `tableRef` tag for every table used. A `jdbcTable` element can contain only one `tableRefList` element. |

## fieldList

`fieldList` is a container for the `field` elements in the join tree. `fieldList` is a child of the `jdbcTable` element.

### Child Elements

| Element Name  | Description                                      |
|---------------|--------------------------------------------------|
| `<``field``>` | (Required) Represents a column in the join tree. |

## field

`field` represents a column in the join tree. When you export Domain from the Domain Designer, the design file includes every column in every table of the join. When you create your own design file, only the columns you want to reference are required. This includes fields that may not appear directly in the Domain, such as fields used in joins. `field` is a child of the `fieldList` element.

!!! note

    `field` elements are also used to represent calculated fields. Calculated fields still appear as children of `fieldList`, but their usage and attributes are different. See [Representing Calculated Fields in XML](representing_calculated_fields.md) for more information.

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
<td><p><code>id</code></p></td>
<td>String</td>
<td><p>(Required) Identifier for the field, composed of the ID of the table in the design and the literal name of the column in the data source. The syntax is <code>table_ID.field_name</code>.</p>
<p>The <code>id</code> XML attribute can contain alphanumeric characters along with any combination of the following: @#$^`_~? It cannot start with a digit.</p></td>
</tr>
<tr>
<td><p><code>type</code></p></td>
<td>String</td>
<td><p>(Required) The Java type of the column, identical to the type in its table definition.</p></td>
</tr>
</tbody>
</table>

## joinInfo

`joinInfo` gives the table ID and alias for the table specified by the `schemaAlias` and `datasourceTableName` attributes of the `jdbcTable` element. This table is used as the first table in the join definition. The table named in `joinInfo` does not have a `tableRef` element.

Both attributes of `joinInfo` are required even if they are identical to the values in `jdbcTable`.

### XML Attributes

| Attribute | Type | Description |
|----|----|----|
| `alias` | String | (Required) Alias for the table identified in `referenceId`; used in the `expression` attribute of the `join` element. By default, the alias is the same as the `referenceID`. If you use a distinct alias, you must be careful to use the alias throughout the `join` element that defines the join. |
| `datasourceId` | String | (Required) Alias for the data source for the Domain. When creating a design file, this alias may be any name you choose, but it must be identical for all tables and derived tables. When uploading the file, the `datasourceId` automatically becomes the alias associated with the data source defined for the Domain. |

## joinList

`<joinList>` is a container for `join` elements. There is a `join` element for each join in the join tree. The `left` attribute of the first `join` element in `joinList` must be the table specified by the `schemaAlias` and `datasourceTableName` attributes of `jdbcTable`.

### Child Elements

| Element Name | Description                                    |
|--------------|------------------------------------------------|
| `join`       | (Required) Representation of a join statement. |

## join

The `join` element represents a single SQL join statement. The left and right tables, join type, join expression, and optional weight are specified as attributes. Every join in the join tree must have a separate `join` element.

` left="`*left_table_ID*`" right=`*right_table_ID*`" type="`join_type`" expr="`*expression*`"`

!!! warning

    When you add or modify joins in the Domain design file, make sure that all tables in a join element are actually connected. If you include a table that is not actually joined to any other tables, the unjoined table is included in any Ad Hoc view that uses that data island. In this case, the fields in the unjoined table show up in the Ad Hoc view. You receive errors in your Ad Hoc view when you add unconnected fields from a poorly configured join.

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
<td><p><code>left</code></p></td>
<td>String</td>
<td><p>(Required) Identifier for the first table in the join definition. This table must have been declared previously in the <code>jdbcTable</code> element. The declaration can appear either in the <code>&lt;joinInfo&gt;</code> element or in another <code>join</code> element that precedes this <code>join</code> element in the <code>joinList</code>.</p></td>
</tr>
<tr>
<td><p><code>right</code></p></td>
<td>String</td>
<td><p>(Required) Identifier for the second table in the join definition.</p></td>
</tr>
<tr>
<td><code>join_type</code></td>
<td>String</td>
<td><p>(Optional, defaults to <code>inner</code>). One of <code>inner</code>, <code>rightOuter</code>, <code>leftOuter</code>, or <code>fullOuter</code>.</p>
<p>**Note** `fullOuter` is not supported in MySQL.</p></td>
</tr>
<tr>
<td><code>expr</code></td>
<td>String</td>
<td><p>Expression that compares the columns on which the <code>join</code> is made. See <span>Options for the expr Attribute</span> for more information.</p></td>
</tr>
<tr>
<td><code>weight</code></td>
<td>Integer &gt; 0</td>
<td>Integer that specifies a weight to use when calculating the minimum join path. You can assign a weight to one, several, or all of the <code>join</code> elements in a join set that has <code>suppressCircularJoins</code> enabled. Higher weights indicate costlier, less-desirable joins. When <code>suppressCircularJoins</code> is set to <code>true</code>, <code>weight</code> is ignored.</td>
</tr>
</tbody>
</table>

### Options for the expr Attribute

The `expr` XML attribute defines the expression used to compare the columns on which the `join` is made.

Each column used in the expression must come from the two tables in the current `join` element. When two columns are compared directly - for example, `store.store_id == employee.store_id` - the first column must come from the left table and the second column must come from the right table.

The following expressions are supported:

-   Boolean operators: AND, OR, and NOT. See the other expressions for examples of how these are used.

-   Comparison operators: Supports equal to (==), less than (&lt;), less than or equal to (&lt;=), greater than (&gt;), greater than or equal to (&gt;=), and not equal to (!=). Operators other than == must be used in conjunction with ==. For example:

    `expr="(store.store_id == employee.store_id) AND`<br>
    `(store.coffee_bar != store.salad_bar)"`

    `expr="(employee.employee_id == salary.employee_id) AND (salary.overtime_paid &gt; 2)`<br>
    `AND (salary.overtime_paid &lt;= 2.1)"`

    !!! note

        You have to use the character entities for less than (&lt;) and greater than (&gt;).

-   IN operator: Must be used in conjunction with ==. Supports the following:

    -   A set of strings or values, separated by commas. Strings are enclosed in single quotes. For example:

        `expr="(store.region_id == region.region_id) AND (store.store_city IN ('San Francisco','Portland', 'Seattle'))" `

        `expr="(store.store_id == employee.store_id) AND (NOT store.coffee_bar IN ('true'))"`

    -   A range of values, separated by a colon. For example:

        `expr="(employee.employee_id == salary.employee_id) AND (NOT employee.salary IN (7000 : 8000))"`

-   Joins between a table foreign key and a constant value. Must be used in conjunction with ==. For example:

`expr="(employee.employee_id == salary.employee_id) AND (employee.salary == 5000)"`

Some join expressions, such as NOT, cannot be edited in the Domain Designer. However, they can be displayed. When you import the Domain into the Domain Designer, these joins are shown in read-only format. See [Read-Only Joins](../advanced_domains/advanced_joins.md) for more information.

!!! note

    If you are using a field of type Date with an Oracle database, use the JasperReports Server`Date()` function in your join expression. For example:

    `<join left="FOODMART_STORE" right="FOODMART_EMPLOYEE" type="inner"`<br>
    `expr="(FOODMART_STORE.STORE_ID == FOODMART_EMPLOYEE.STORE_ID)`<br>
    `AND (FOODMART_EMPLOYEE.BIRTH_DATE &gt; ``Date('1914-02-02')``)"/>`

    This applies to Date literals only. It is not necessary for fields with date formats but other types, for example, Timestamp.

## joinOptions

The `joinOptions` element allows you to influence the joins that are pushed down to SQL in an Ad Hoc view. A `jdbcTable` element can contain only one `joinOptions` element, which sets the options for the entire join tree. `joinOptions` lets you avoid circular joins in cases where there are N tables with N or more joins. See [Join Tree Options](../advanced_domains/advanced_joins.md) for more information.

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
<td><p><code>suppressCircularJoins</code></p></td>
<td>Boolean</td>
<td><p>(Default = <code>false</code>) When this attribute is set to <code>true</code> for a join tree, an Ad Hoc view created from the join tree uses a minimum join. When <code>suppressCircularJoins</code> is set to <code>true</code>, you can optionally assign weights to the joins in the join set.</p>
<p>When <code>suppressCircularJoins</code> is set to <code>false</code>, all joins in the join tree are used in Ad Hoc views.</p>
<p>For most situations, the best practice is to set this option to <code>true</code> to avoid circular joins. Set it to <code>false</code> only if you need backwards compatibility with schema_1_0.xsd of the Domain syntax.</p></td>
</tr>
<tr>
<td><code>includeAllDataIslandJoins</code></td>
<td>Boolean</td>
<td><p>(Default= <code>false</code>) Available for backwards compatibility. When this attribute is set to <code>true</code> for a join set/data island, an Ad Hoc view created from the data island includes all joins specified for that data island in the Domain. This attribute can only be set to <code>true</code> when <code>suppressCircularJoins</code> is <code>false</code>.</p>
For most situations, the best practice is to set this option to <code>false</code> (default).</td>
</tr>
</tbody>
</table>

## tableRefList

The `<tableRefList>` element is a container for the list of tables and aliases used in the join tree. It must include a `tableRef` element for every table in the join tree.

### Child Elements

| Element Name     | Description                                          |
|------------------|------------------------------------------------------|
| `<``tableRef``>` | (Required) Represents a table used in the join tree. |

## tableRef

The `<tableRef>` element represents a table used in the join tree. There must be a `tableRef` element for every table in the join tree.

### XML Attributes

| Attribute | Type | Description |
|----|----|----|
| `tableId` | String | The ID of a table within the design. |
| `tableAlias` | String | Alternative name for the table used within the join expression. |
| `alwaysIncludeTable` | Boolean | (Default = `false`) Setting this to `true` forces this table to be included in all Ad Hoc views created from this data island. For most situations, the best practice is to set this option to `false` (default). |

## Join Tree Example

The following example shows a join tree with three joins between three tables. This example shows how you might use the following:

-   To avoid circular joins, `suppressCircularJoins` is set to true.
-   The join between `region` and `customer` has a join `weight` of 2. This makes it a less desirable join than the other joins in the tree.
-   `alwaysIncludeTable` is set to `true` for the `region` table.

``` xml
<schema xmlns="http://www.jaspersoft.com/2007/SL/XMLSchema" version="1.3">
<resources>
 <jdbcTable id="JoinTree_1" datasourceId="FoodmartDataSourceJNDI" schemaAlias="public" datasourceTableName="customer">
     <fieldList>
       <field id="customer.account_num" fieldDBName="account_num" type="java.lang.Long" />
    ...
     <fieldList>
          <joinInfo alias="store" referenceId="store" />
       <joinOptions suppressCircularJoins="true"/>

       <tableRefList>
         <tableRef tableId="store" tableAlias="store"/>
         <tableRef tableId="customer" tableAlias="customer"/>
         <tableRef alwaysIncludeTable="true" tableId="region" tableAlias="region"/>
       </tableRefList>

      <joinList>
         <join left="store" right="customer" type="inner"
                         expr="store.region_id == customer.customer_region_id"/>
         <join left="store" right="region" type="inner"
                         expr="store.region_id == region.region_id"/>
        <join weight="2" left="region" right="customer" type="inner"
                         expr="region.region_id == customer.customer_region_id"/>
         </joinList>

   </jdbcTable>
</resources>
</schema>
```

## Working With Joins

Keep the following in mind when working with join syntax:

-   When you add or modify joins in the Domain design file, make sure that all tables in a join element are actually connected. If you include a table that is not actually joined to any other tables, the unjoined table is included in any Ad Hoc view that uses that data island. In this case, the fields in the unjoined table show up in the Ad Hoc view. You receive errors in your Ad Hoc view when you add unconnected fields from a poorly configured join.

-   When you use a `join` tag, the `left` table must have been defined previously in the `jdbcTable` element. You can define the table either in the `joinInfo` tag or as the `right` table in a previous join in the same `joinList`. Follow these guidelines for your joins:

-   When you have a `join` that depends on the `right` table from another join in the `joinList`, make sure that the dependent `join` appears after the join it depends on.

    -   When you have a `join` that refers to a table that has not yet been defined, make sure that the new table is referenced as the `right` table in the join.

-   In some cases, you can start your Domain creation using the Domain Designer. To do this:

1.  Set up the rest of your Domain, such as derived tables and calculated fields, in the Domain Designer.

    1.  Create a join that uses the same tables that you want to join in your Domain. This sets up the `jdbcTable` and `fieldList` tags for you.
    2.  Export the schema from the Domain Designer.
    3.  Manually edit the `tableRefList` and `joinInfo` sections of the exported design file to create the join you want.

## Tips for Using Joins

-   To avoid join cycles in queries, set `<joinOptions suppressCircularJoins=true/>`. This finds the lowest weight join set.
-   To configure your Domain to use the fewest number of joins required to reach a given set of chosen fields, use `<joinOptions suppressCircularJoins=true/>` AND set all `<join weight="W">` values to be the same value. In this case, the lowest weight join set will be a set that has the minimum possible number of joins.
-   You do not have to set the join weight explicitly. If the weight is not set, it defaults to 1.
-   To give preferential treatment to joins that involve indexed columns for better join performance, assign lower join weights to the preferred joins and higher join weights to less desirable joins.
-   To make sure that one or more specific table(s) always get included in your results, set `alwaysIncludeTable=true`. For example, to make sure tableA is always included, use:<br>
    `<tableRef tableId=tableA tableAlias=tableA alwaysIncludeTable=true/>`
