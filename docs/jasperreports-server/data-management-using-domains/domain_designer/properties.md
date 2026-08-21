---
title: Properties
description: Item Properties on the Data Presentation Tab
---

# Properties

![js DomainDesigner presentation item properties](../assets/images/js-DomainDesigner-presentation-item-properties.png)

Item Properties on the Data Presentation Tab

The Properties pane of the Data Presentation tab lets you refine the Domain's appearance by renaming and providing descriptions for sets, subsets, and items. The following table describes the available properties:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th><p>Property</p></th>
<th><p>Appears On</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Label</p></td>
<td><p>Set, Item</p></td>
<td><p>User-friendly name displayed in the Data Chooser and the Ad Hoc Editor.</p></td>
</tr>
<tr>
<td><p>ID</p></td>
<td><p>Set, Item</p></td>
<td><p>An identifier used within the Domain. Default table and field IDs are based on the names in the data source, but you can change the ID of a table as long as it remains unique. Set and item IDs are a separate namespace in which each ID must be unique, although based on table and field IDs by default. The ID property value must be alphanumeric.</p>
<p>You should not change IDs for a Domain that has been used to create Ad Hoc views or Topics.</p></td>
</tr>
<tr>
<td><p>Description</p></td>
<td><p>Set, Item</p></td>
<td><p>User-friendly description displayed as tooltip on the label in the Ad Hoc Editor. The description helps the report creator understand the data represented by this set or item.</p></td>
</tr>
<tr>
<td><p>Content Type</p></td>
<td><p>Item</p></td>
<td><p>Designates the item as either a qualitative value (field) or quantitative value (measure). By default, all numeric types are assumed to be measures, and all non-numeric items are plain fields. Use this setting to override the default.</p></td>
</tr>
<tr>
<td><p>Summary Calculation</p></td>
<td><p>Item</p></td>
<td><p>Default summary calculation of the item when used in a report. The available functions depend on the field's data type (Boolean, date, numeric, or text). See the JasperReports Server User Guide for more information.</p></td>
</tr>
<tr>
<td><p>Data Format</p></td>
<td><p>Item</p></td>
<td><p>Default numerical format (such as number of decimal places) for the item when used in a report. Numeric and dates only.</p></td>
</tr>
<tr>
<td><p>Label Key<br />
</p></td>
<td><p>Set, Item</p></td>
<td><p>Internationalization key for the label property; locale bundles associate this key with the localized text for the label.</p></td>
</tr>
<tr>
<td>Descriptions Key</td>
<td>Set, Item</td>
<td><p>Internationalization key for the description property; locale bundles associate this key with the localized text for the description.</p></td>
</tr>
<tr>
<td><p>Source</p></td>
<td><p>Item</p></td>
<td><p>For a domain based on Trino:</p>
<p>References the data source, catalog, schema, table, and field associated with this item; the syntax is <code>datasource.catalog.schema.table.field</code>. Not editable</p>
<p>For a Domain not based on Trino:</p>
<p>References the data source, schema, table, and field associated with this item; the syntax is <code>datasource.schema.table.field</code>. Not editable.</p></td>
</tr>
</tbody>
</table>

Labels and descriptions are visible to users of the Domain. Descriptions of sets and items appear as tooltips in the Ad Hoc Editor to help report creators understand their purpose.

The internationalization keys must match the property names of strings in locale bundles. Keys may use only characters from the ISO Latin-1 set, digits, and underscores (\_).
