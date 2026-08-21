---
title: Using Attributes in the Domain Designer
description: "You can use attributes in the Domain Designer to have the server derive values at run time, based on the user, organization, or server. The Domain Designer supports attributes in the following places:"
---

# Using Attributes in the Domain Designer

You can use attributes in the Domain Designer to have the server derive values at run time, based on the user, organization, or server. The Domain Designer supports attributes in the following places:

- Schema names
- Derived table queries
- Calculated fields
- Custom joins
- Pre-filters

In addition, you can use attributes in a data source definition. This does not appear directly in the Domain Designer, but allows you to change the data source based on the attribute value.

## Attribute Syntax

When referring to an attribute, you can specify the attribute categorically or hierarchically:

- Categorical reference: If you specify a category for the attribute value, the server attempts to find that particular value of the attribute. You can specify these attribute categories:

  - User: In the attributes defined on the logged-in user.

  - Tenant: In the attributes defined on the organization of the logged-in user.

  - Server: In the attributes defined at the server-level.

- Hierarchical reference: If you don't specify a category for the attribute, the filter searches attributes hierarchically and uses the value for the first attribute it finds with the given name. This search starts with the logged-in user, then proceeds to the user's organization and parent organization, and finally to the server level.

For join expressions, calculated fields, and pre-filters, the following syntax is used:

- `attribute('attributeName', 'server')` for a server-level attribute.

- `attribute('attributeName', 'tenant')` for an organization-level attribute.

- `attribute('attributeName', 'user')` for a user-level attribute.

If no level is specified, the server will search for the attribute hierarchically, starting at the `'user'` level:

- `attribute('attributeName')`

!!! note

    The simplified syntax is used in locations that support the internal Domain syntax, DomEL. See [Domain Expression Language (DomEL)](../domel/domain_expression_language.md).

For schema names and derived tables, the attribute must be escaped with curly brackets ():

- `{attribute('attributeName'), 'server'}` for a server-level attribute.

- `{attribute('attributeName', 'tenant')}` for an organization-level attribute.

- `{attribute('attributeName', 'user')}` for a user-level attribute.

- `{attribute('attributeName')}` to search for an attribute hierarchically.

For more information on attributes, see the section "Managing Attributes" in the *JasperReports Server Administrator Guide*.

## Things to Remember When Using Attributes

Note the following when using attributes:

- The attribute value must match the expected data type. For example, if you are creating a calculated field of type Integer, the attribute value must be an Integer.
- Attribute collections are not supported in the main Domain design. The attribute must be a single value. Attribute collections can be used in Domain security, however.
- If you are using attributes for the schema, make sure that the tables and columns referenced in the Domain are available for every possible value of the attribute. See [Changing the Data Source](modifying_a_domain.md) for more information.

!!! note

    If you use an attribute in your data source definition, you must ensure that referenced schemas, tables, and columns will be available. Data source attributes are defined outside the Domain Designer. See the section on defining attributes in the JasperReports Server Administrator Guide for more information.

- If a specified attribute does not exist, any item that uses it will fail. For example, if you specify the attribute `Country` for a schema name, and a `Country` attribute does not exist anywhere on the server, you will be unable to load the schema. This is similar to referring to column that does not exist.
- If an attribute exists but is not defined (empty) for this particular user, the behavior depends on where the attribute is used. An empty attribute can occur, for example, if you have set up a `Country` attribute, but the current user has no value defined for `Country`.
- For pre-filters, an empty attribute is interpreted based on the field's data type as described below.
  - For a field of type string, an empty attribute is interpreted as an empty string: `""`
  - For a boolean field, and empty attribute is interpreted as `FALSE`.
  - For numeric and date fields, an error will occur.
- For derived table queries and custom joins, the attribute will fail in most cases. However, in some cases, JasperReports Server will consider the resulting expression to be valid, with potentially unexpected results, so be cautious when using attributes in this part of your design.
- For schema names, the default schema is used. The default schema must be defined in the XML Domain design file. See [Default Schema](../domain_syntax/representing_data_sources.md) for more information.

## Using Attributes for Pre-Filters

For example, you can use attributes to create a pre-filter for a country. Instead of a static filter that filters out data for every country except the USA, you could create a filter that only shows data for the logged-in user's country. To do this, you would create a Country attribute for your users in their profiles and enter the name of their country, which must match one of the country names used in the Domain's data source. Then, when creating the pre-filter, you can use the parameter `attribute('Country')` to filter out data for all countries except the user's country.

For pre-filters, the data type for the attribute is automatically based on the filtered column's type. For example, if you are creating a filter based on a Date column, the attribute parameter will return a Date value.

## Using Attributes for Schema Names

You can use attributes to choose a schema in your database. For example, suppose you have schemas named dev and qa in your database. You could create a server-level attribute and set it to `dev` on one server and `qa` on another. You can then use the attribute for the database schema in your Domain. Similarly, in a multi-organization deployment, you could have different schemas for different organizations, and set an organization-level attribute to choose which schema to access.

The Domain Designer needs a concrete schema to read and display tables. When you use an attribute for a schema name, the Domain Designer automatically substitutes the current value of the attribute. For the example above, if you use the Domain Designer on a server where the attribute is set to `dev`, the Domain Designer displays the `dev` schema in the Selected Schemas list and in the Select Data panel. You will see the tables and columns in the `dev` schema in the Domain Designer UI. Any joins, pre-filters, or presentation sets you create are based on that `dev` schema.

- To find the underlying attribute for a schema, go to the **Data Management** tab, select the database in the **Data Structure** panel, and then click on the schema name in the **Selected Schemas** list. The attribute details appear in the **You may also use an attribute for the schema name:** text box.

!!! note

    When you use an attribute for a schema name, the Domain will fail if the schema is missing. You can optionally set a default schema in the Domain design file. The default schema is used whenever the schema is missing or undefined. See [Default Schema](../domain_syntax/representing_data_sources.md) for more information.
