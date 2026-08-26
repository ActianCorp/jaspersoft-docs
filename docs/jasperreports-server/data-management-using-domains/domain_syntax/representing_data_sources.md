---
title: Representing Data Sources and Database Schemas in XML
description: Data sources and database schemas are declared under the dataSources element. A data source for a Domain is declared using jdbcDataSource and a data source for a Topic is declared using...
---

# Representing Data Sources and Database Schemas in XML

Data sources and database schemas are declared under the `dataSources` element. A data source for a Domain is declared using `jdbcDataSource` and a data source for a Topic is declared using `jrQueryDataset`.

## dataSources

The `dataSources` element is a container for the `jdbcDataSource` element. A Domain can only have at most one data source. `dataSources` is a child of the top-level `schema` element.

`dataSources` is not required for schemaless JDBC databases such as MySQL unless you are using an attribute for the database schema name.

### Child Elements

One of the following elements is required for `dataSources`. Only one of these can be declared.

| Element Name | Description |
|----|----|
| `<jdbcDataSource>` | Declares a data source for a Domain and the id used to reference it. |
| `<jrQueryDataset>` | Declares a data source for a Topic and the id used to reference it. |

## jdbcDataSource

The `jdbcDataSource` element declares a data source for a Domain and is a container for the `schemaMap` elements used in the Domain. `jdbcDataSources` does not directly reference a data source in the repository; instead, the actual link to the repository data source is attached as metadata to the Domain design in the repository.

For Topics, use jrQueryDataset. There can only be one `jrQueryDataset` or `jdbcDataSource` element in a Domain design file.

### jdbcDataSource Hierarchy

The following hierarchy is used to represent JDBC data sources and their database schemas. This hierarchy is under the `schema` element.

``` xml
  <dataSources> (1)
    <jdbcDataSource> (1)
      <schemaMap> (1...n)
        <entry> (1)
          <string> (1)
```

### Child Elements

| Element Name  | Description                                               |
|---------------|-----------------------------------------------------------|
| `<schemaMap>` | (Required) Declares a database schema used in the Domain. |

### XML Attributes

| Attribute | Type | Description |
|----|----|----|
| `id` | String | (Required) Unique identifier for the data source in the Domain design file. |

## schemaMap

The `schemaMap` element is a container for `entry` elements that represent database schemas used in the Domain.

### Child Elements

| Element Name | Description                                          |
|--------------|------------------------------------------------------|
| `<entry>`    | A database schema or the default schema declaration. |

## entry

The `entry` element in the schemaMap element declares a database schema for use in the Domain. The actual name of the schema is the value of the `string` child element, while the identifier used in the Domain is set as the `key` attribute.

If `key` is set to `defaultSchema`, the `entry` element is used to define the default schema.

### Child Elements

| Element Name | Description                             |
|--------------|-----------------------------------------|
| `<string>`   | The name of the schema in the database. |

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
<td><p><code>key</code></p></td>
<td>String</td>
<td><p>(Required) Unique identifier for the schema in the Domain design file or the reserved string "<code>defaultSchema</code>".</p>
<p>For regular database schemas in the Domain, the <code>key</code> attribute is used by other elements in the presentation representation to identify the schema, via the <code>referenceId</code>.</p>
<p>If <code>key</code> is set to <code>defaultSchema</code>, this <code>entry</code> element is used to define the default schema. See <span>Default Schema</span> for more information.</p>
<p>The <code>key</code> XML attribute can contain alphanumeric characters along with any combination of the following: @#$^`_~? It cannot start with a digit.</p></td>
</tr>
</tbody>
</table>

## string

The `string` element in the `schemaMap` hierarchy is a string defining the database schema to be used in the Domain. The string can be one of the following:

-   The exact name of a schema in the database.
-   A JasperReports Server attribute. Not supported for `defaultSchema`. See [Using Server Attributes in Design Files](using_server_attributes.md) for more information.

### Default Schema

If the `key` attribute of the parent `entry` element is set to `defaultSchema`, then `entry`/`string` declares the default schema for the Domain. The default schema is a fallback schema name that is substituted when a schema name is missing or not available. This can happen, for example, if you are using a JasperReports Server attribute for the data source or schema. It can also happen if you change the data source for some reason. You can only define one default schema for a database.

## Examples

The following example shows a declaration of a data source and two schemas. Note that the data source name in the Design file does not need to be linked to the data source in the repository. That linkage is done outside of the Domain design file.

!!! note

    Note that in the `key` attribute, an underscore (\_) has been substituted for unsupported characters. Periods (.) are not supported in schema key attributes; numbers are supported, but not in the first character.

``` xml
  <dataSources>
    <jdbcDataSource id="myDataSource">
      <schemaMap>
        <entry key="schema_1">
          <string>schema.1</string>
        </entry>
        <entry key="_234schema">
          <string>1234schema</string>
        </entry>
      </schemaMap>
    </jdbcDataSource>
  </dataSources>
```

The following example shows a file that uses an attribute for the database schema name, and sets a default schema name to use when the attribute is null.

``` xml
  <dataSources>
    <jdbcDataSource id="dsFoodMart">
      <schemaMap>
        <entry key="_attribute_schemaAttr_">
          <string>{attribute('schemaAttr')}</string>
        </entry>
        <entry key="defaultSchema">
          <string>public</string>
        </entry>
      </schemaMap>
    </jdbcDataSource>
  </dataSources>
```

!!! note

    If you use an attribute for the database schema name, and the attribute is undefined on the server, the Domain will fail.

## jrQueryDataset

The `jrQueryDataset` element declares the data source for a Topic. `jrQueryDataset` does not directly reference a data source in the repository; instead, the actual link to the repository data source is attached as metadata to the Domain design in the repository. There can only be one `jrQueryDataset` or `jdbcDataSource` element in a Domain.

`jrQueryDataset` does not support schemas. For more information about Topics, see the JasperReports Server User Guide.

### Element Hierarchy for jrQueryDataset

The following hierarchy is used to represent JDBC data sources and their database schemas. This hierarchy is under the `schema` element.

``` xml
  <dataSources> (1)
    <jrQueryDataset> (1)
```

### XML Attributes

| Attribute | Type | Description |
|----|----|----|
| `id` | String | (Required) Unique identifier for the data source in the Domain design file. |
