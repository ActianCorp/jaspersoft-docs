---
title: XML Design File Reference
description: This section explains each of the XML elements and attributes in a design file and how they relate to the settings in the Domain Designer.
---

# XML Design File Reference

This section explains each of the XML elements and attributes in a design file and how they relate to the settings in the Domain Designer.

!!! note

    Because certain XML elements correspond to objects in the Domain design, this section refers to XML elements that *contain* Domain objects such as sets. This is a short-hand description that means the XML elements contain other XML elements that represent the Domain object.

    Technically, the only requirement to save or upload a Domain design file is a data source reference. However, for the file to be usable, many more elements are needed. As a short-hand, elements you need to create a usable Domain are marked "required".

    The following symbols can't be entered directly; they must be escaped using their HTML encoding:

    & = `&amp;`           " = `&quot;`           &lt; = `&lt;`           &gt; = `&gt;`

## The schema Element

The `schema` element is the outermost container element of an XML Domain design file. The `schema` element is required.

!!! note

    The `schema` element refers to the XML schema. It has no relationship to database schemas in the data source.

#### schema Hierarchy

The following hierarchy is used for the `schema` element:

``` xml
<schema xmlns="http://www.jaspersoft.com/2007/SL/XMLSchema" version="1.3"
    schemaLocation="schema_1_3.xsd">
    <dataIslands> (0..1)
    <dataSources> (0..1)
    <itemGroups> (0..n)
    <items> (0..n)
    <resources> (1)
```

When you export a file from the Domain Designer, these elements appear alphabetically in the file. In this reference, they are presented in the following order, based on their function in the Domain:

-   Data sources and database schemas (`dataSources` element).
-   Domain tables and rows (`resources` element); includes tables, derived tables, calculated fields, joins, and pre-filters.
-   Domain presentation (`dataIslands`, `itemGroups`, and `items` elements).

#### Child Elements

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
<td><code>&lt;dataIslands&gt;</code></td>
<td>Container for a list of data islands in the Domain design.</td>
</tr>
<tr>
<td><code>&lt;dataSources&gt;</code></td>
<td>Container for the Domain data source and schemas.</td>
</tr>
<tr>
<td><code>&lt;itemGroups&gt;</code></td>
<td>Containers for sets; each data island listed in the <code>dataIslands</code> element must have a corresponding <code>itemGroups</code> element.</td>
</tr>
<tr>
<td><code>&lt;items&gt;</code></td>
<td>Containers for items that aren't in any set. Items in different <code>dataIslands</code> must be in different <code>items</code> elements.</td>
</tr>
<tr>
<td><code>&lt;resources&gt;</code></td>
<td><p>(Required) Container for all elements that define tables and rows in the Domain, including:</p>
<ul>
<li><a href="representing_tables.md">Tables</a></li>
<li><a href="representing_derived_tables.md">Derived tables</a></li>
<li><a href="representing_joins.md">Joins</a></li>
<li><a href="representing_calculated_fields.md">Calculated fields</a></li>
<li><a href="representing_pre-filters.md">Pre-filters</a></li>
</ul>
<p>Because the elements under <code>resources</code> refer to database objects, they must be externally consistent with the data source for the Domain.</p></td>
</tr>
</tbody>
</table>

#### XML Attributes

| Attribute | Type | Description |
|----|----|----|
| `schemaLocation` | String | Sometimes added by XML editors to locate the XSD file. |
| `version` | String | Version of the XSD used to create this design file. Included in design files exported from Domain Designer. |
| `xmlns` | String | XML namespace URI. This string is unique to Jaspersoft, and it does not correspond to a valid URL. For more information, see [http://www.w3.org/TR/REC-xml-names](http://www.w3.org/TR/REC-xml-names/). Included in design files exported from Domain Designer. |
