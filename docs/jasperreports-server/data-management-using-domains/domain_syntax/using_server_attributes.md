---
title: Using Server Attributes in Design Files
description: "A JasperReports Server attribute is a name-value pair associated with a user, organization, or server. Attributes let you create Domains that are customized for each user based on the values of their..."
---

# Using Server Attributes in Design Files

A JasperReports Server attribute is a name-value pair associated with a user, organization, or server. Attributes let you create Domains that are customized for each user based on the values of their attributes. For example, if the database schema is defined using an organization-level attribute, the Domain will access data specific to each user's organization. This lets you create one Domain for many organizations, provided they all use the same tables in the schema.

To define or modify attributes on the server, see the section on attributes in the JasperReports Server Administrator Guide.

You can use attributes in the Domain design file. When you use an attribute, the server derives the value at run time, based on the user, organization, or server. Attributes are supported in DomEl expressions in the following locations:

-   Calculated field calculations
-   Join expressions
-   Pre-filter expressions

They can also be used in other locations in the Domain design, including:

-   Schema entry keys
-   Derived table queries

If you want to use a JasperReports Server attribute in a data source, you must specify the attribute when you create the data source, not in the Domain design file. See the JasperReports Server Administrator Guide for information about using attributes in data sources.

## Attribute Syntax

When referring to an attribute, you can specify the attribute categorically or hierarchically:

-   Categorical reference: If you specify a category for the attribute value, the server attempts to find that particular value of the attribute. You can specify these attribute categories:

    -   User: In the attributes defined on the logged-in user.

    -   Tenant: In the attributes defined on the organization of the logged-in user.

    -   Server: In the attributes defined at the server-level.

-   Hierarchical reference: If you don't specify a category for the attribute, the filter searches attributes hierarchically and uses the value for the first attribute it finds with the given name. This search starts with the logged-in user, then proceeds to the user's organization and parent organization, and finally to the server level.

For join expressions, calculated fields, and pre-filters, the DomEL syntax is used. See [Domain Expression Language (DomEL)](../domel/domain_expression_language.md) for more information.

-   `attribute('attributeName', 'server')` for a server-level attribute.

-   `attribute('attributeName', 'tenant')` for an organization-level attribute.

-   `attribute('attributeName', 'user')` for a user-level attribute.

If no level is specified, the server will search for the attribute hierarchically, starting at the `'user'` level:

-   `attribute('attributeName')`

For schema names and derived tables, the attribute must be escaped with curly brackets ():

-   `{attribute('attributeName'), 'server'}` for a server-level attribute.

-   `{attribute('attributeName', 'tenant')}` for an organization-level attribute.

-   `{attribute('attributeName', 'user')}` for a user-level attribute.

-   `{attribute('attributeName')}` to search for an attribute hierarchically.

For more information on attributes, see the Managing Attributes section  in the *JasperReports Server Administrator Guide*. For information about using JasperReports Server attributes in Domain security files, see [User Attributes](../domain_security/roles-users-attributes.md) and [The attributesService](../domain_security/creating-a-security-file.md).

## Examples

To use a JasperReports Server attribute as the name of a schema in the data source, use the attribute syntax in the `string` element for the `entry` for that schema. You can use a constant or an attribute for the XML `key` attribute of `entry`.

``` xml
<jdbcDataSource id="FoodmartDataSourceJNDI">
  <schemaMap>
    <entry key="defaultSchema">
      <string>public</string>
    </entry>
    <entry key="_attribute_schemaAttribute_">
      <string>{attribute('schemaAttribute')}</string>
    </entry>
  </schemaMap>
</jdbcDataSource>
```

For pre-filters, JasperReports Server attributes can appear in the expression for the `filterString` element in the `jdbcTble` or `jdbcQuery` element:

``` xml
<jdbcTable id="region" datasourceId="FoodmartDataSourceJNDI" schemaAlias="public" datasourceTableName="region">
  <fieldList>
    <field id="region_id" type="java.lang.Integer" />
    <field id="sales_city" type="java.lang.String" />
    <field id="sales_country" type="java.lang.String" />
  </fieldList>
  <filterString>sales_country == attribute('attributeCountry')</filterString>
</jdbcTable>
```

For calculated fields, JasperReports Server attributes can appear in `dataSetExpression` in the `field` element:

``` xml
<field id="Sample_Calculated_Field" dataSetExpression="salary_paid &gt; attribute('numericAttribute')" type="java.lang.Boolean" />
```

For derived tables, JasperReports Server attributes can appear in the `query` element in `jdbcQuery`. For example, if you have defined an attribute with the name of the table you want called `tableAttribute`, a derived table that uses that attribute might look like this:

``` xml
<jdbcQuery id="inventory_fact_1998_2" datasourceId="dsFoodMart">
      <fieldList>
        <field id="warehouse_cost" type="java.math.BigDecimal" />
        <field id="warehouse_profit" type="java.math.BigDecimal" />
        <field id="warehouse_sales" type="java.math.BigDecimal" />
      </fieldList>
      <query>select

   {attribute('tableAttribute')}.warehouse_sales as warehouse_sales,
   {attribute('tableAttribute')}.warehouse_cost as warehouse_cost,

  ( {attribute('tableAttribute')}.warehouse_sales -  {attribute('tableAttribute')}.warehouse_cost) as warehouse_profit

from
  {attribute('tableAttribute')}</query>
    </jdbcQuery>
```

You can use attributes in the secondary joins in a complex join `expression`. However, you can't use attributes in the first join in the expression:

``` xml
<joinInfo alias="account" referenceId="account" />
<joinList>
    <join expr="account.account_id == expense_fact.account_id and
       account.account_description == attribute('tableAttribute')"
       left="account" right="expense_fact" type="inner" weight="1" />
</joinList>
<joinOptions />
```

## Attribute Casting Functions

A JasperReports Server attribute value is always a string. You can use the following functions to cast it to other types in DomEl expressions, for example if you want to compare it to a field value.

| Function | Syntax | Example |
|----|----|----|
| Integer | `Integer('string')` | Integer('345') = 345; |
| Decimal | `Decimal('string')` | Decimal('24.5') = 24.5; |
| Boolean | `Boolean('string')` | Boolean('true') = true; |
| Date | `Date('string')` | Date('2008-02-08') = d'2008-02-08'; |
| Timestamp | `Timestamp('string')` | Timestamp('2008-02-08 11:30:00') = ts'2008-02-08 11:30:00'; |
| Time | `Time('string')` | Time('11:30:00') = t'11:30:00'; |

## Guidelines for Using Attributes

Note the following when using attributes:

-   The JasperReports Server attribute value must match the expected data type. For example, if you are creating a calculated field of type Integer, the attribute value must be an Integer.
-   Attribute collections are not supported in the main Domain design. The JasperReports Server attribute must be a single value. Attribute collections can be used in Domain security, however.
-   If you are using JasperReports Server attributes for the name of a schema, make sure that any dependent tables and columns in the Domain will be available for every possible value of the attribute. See [Changing the Data Source](../advanced_domains/modifying_a_domain.md) for more information.

!!! note

    If you use an attribute in your data source definition, you must ensure that referenced schemas, tables, and columns will be available. Data source attributes are defined outside the Domain Designer. See the section on defining attributes in the JasperReports Server Administrator Guide for more information.

-   If a specified attribute does not exist, any item that uses it will fail. For example, if you specify the attribute `Country` for a schema name, and a `Country` attribute does not exist anywhere on the server, you will be unable to load the schema. This is similar to referring to column that does not exist.

-   If an attribute exists but is not defined (empty) for a particular user, the behavior depends on where the attribute is used. An empty attribute can occur, for example, if you have set up a `Country` attribute, but the current user has no value defined for `Country`.

-   For pre-filters, an empty attribute is interpreted based on the field's data type, as described below.

    -   For a field of type String, an empty attribute is interpreted as an empty string: `""`

        -   For a Boolean field, and empty attribute is interpreted as `FALSE`.
        -   For numeric and date fields, an error will occur.

    -   For derived table queries and custom joins, the attribute will fail in most cases. However, in some cases, JasperReports Server will consider the resulting expression to be valid, with potentially unexpected results, so be cautious when using attributes in this part of your design.

    -   For schema names, the default schema is used when the attribute is empty. The default schema must be defined in the XML Domain design file. See [Default Schema](representing_data_sources.md) for more information.
