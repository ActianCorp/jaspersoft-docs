---
title: Representing Calculated Fields in XML
description: "Calculated fields are defined as field elements with an additional XML attribute, dataSetExpression, that holds the calculation for the field."
---

# Representing Calculated Fields in XML

Calculated fields are defined as `field` elements with an additional XML attribute, `dataSetExpression`, that holds the calculation for the field.

## field

The `field` element is a child of the `fieldList` element. The location of the `fieldList` element for calculated fields depends on the location of the fields used in the calculation:

- Calculated fields where all the columns in the calculation come from a single table appear twice in the design file:

  - Under the `jdbcTable` element for the join tree that contains the table.
  - Under the `jdbcTable` or `jdbcQuery` element for that table.

- Calculated fields that use columns from different tables appear only once, under the `jdbcTable` element for the join tree contains both tables. Remember, it is not possible to create calculated fields from columns in different join trees.

- Constant fields appear under `resources` as a `null` element.

Constant fields are calculated fields that do not reference any column names. Constant fields are defined as `field` elements in a `fieldList` under the `null` element. Because constant fields are not dependent on any column values, they may be used in any join tree or data island. They can also be used in other calculated fields and pre-filters.

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
<td><code>dataSetExpression</code></td>
<td>String</td>
<td>(Required) Expression that calculates a value. This value is either based on other columns or is a constant value. For a description of the syntax for the expression, including how to reference columns, see <a href="../domel/domain_expression_language.md">Domain Expression Language (DomEL)</a>. For information on using attributes in calculated fields, see <a href="using_server_attributes.md">Using Server Attributes in Design Files</a>.</td>
</tr>
<tr>
<td><p><code>id</code></p></td>
<td>String</td>
<td><p>(Required) Identifier for the calculated field. The format of the <code>id</code> depends on how the calculated field appears in the design file:</p>
<ol>
<li><p>If all columns used in the expression are from the same table, and the table appears in a join, there are two <code>field</code> elements for the calculated field, with different ids:</p>
<ul>
<li>When the field appears under the <code>jdbcTable</code> or <code>jdbcQuery</code> element for the table, the <code>id</code> is a simple column name <code>field_name</code>.</li>
<li>When the field appears under the <code>jdbcTable</code> element for the join tree that uses the table, the <code>id</code> has the form <code>table_ID.field_name</code>.</li>
</ul></li>
<li>If the expression references columns from different tables, the field appears only in the join tree that contains those tables and the <code>id</code> has the form <code>jointree_ID.field_name</code>.</li>
<li>If the expression is a constant value, the field appears in the <code>null</code> element under <code>resources</code> and the <code>id</code> is <code>constant_fields_level.field_name</code>.</li>
</ol>
<p>The <code>id</code> XML attribute can contain alphanumeric characters along with any combination of the following: @#$^`_~? It cannot start with a digit.</p></td>
</tr>
<tr>
<td><p><code>type</code></p></td>
<td>String</td>
<td><p>The Java type of the value calculated by the expression, for example <code>java.lang.String</code>. This type must be compatible with the result of the DomEL expression and among the JDBC-compatible types listed in <a href="representing_tables.md">Supported Types</a>.</p></td>
</tr>
</tbody>
</table>

### Example

The following example shows the XML for a calculated expression that only references one table, the `accounts` table. Because it references only the columns of `accounts`, it appears in that table and in the join tree.

``` xml
<jdbcTable datasourceId="SugarCRMDataSource" id="accounts"
        schemaAlias="public" datasourceTableName="accounts">
 <fieldList>
  ...
  <field dataSetExpression="concat( billing_address_city, ', ',
      billing_address_state )" id="city_and_state" type="java.lang.String"/>
  ...
 </fieldlist>
</jdbcTable>
...
<jdbcTable datasourceId="SugarCRMDataSource" id="JoinTree_1"
        schemaAlias="public" datasourceTableName="anything">
 <fieldList>
  ...
  <field dataSetExpression="concat( billing_address_city, ', ',
      accounts.billing_address_state )" id="accounts.city_and_state"
      type="java.lang.String"/>
  ...
 </fieldlist>
</jdbcTable>
```

## null

The `null` element is a container for constant fields. `null` is a child of the `resources` element.

### Child Elements

| Element Name | Description |
|----|----|
| `<``fieldList``>` | (Required) A container for the `field` elements for constant fields. The `null` element can contain only one `fieldlist` element. |

## fieldList

As a child of `null`, `fieldList` is a container for one or more `field` elements that represent constant fields.

### Child Elements

| Element Name | Description |
|----|----|
| `<field>` | (Required) A constant field. Constant fields may be used in any join tree or data island. They can also be used in other calculated fields and pre-filters. |

### Example

The following example shows the XML for two constant calculated fields.

``` xml
<resources>
<null id="constant_fields_level" datasourceId="FoodmartDataSourceJNDI">
<fieldList>
<field id="CF_Constant" dataSetExpression="1 + 1 + 1" type="java.math.BigInteger" />
<field id="CF_Constant_2" dataSetExpression="12" type="java.math.BigInteger" />
</fieldList>
</null>
...
</resources>
```
