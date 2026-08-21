---
title: Field References
description: "DomEL expressions are stored in the Domain design and interpreted when the server prepares to run a query to retrieve data from the data source. Therefore, all references to field values in an..."
---

# Field References

DomEL expressions are stored in the Domain design and interpreted when the server prepares to run a query to retrieve data from the data source. Therefore, all references to field values in an expression are based on the `id` attributes defined in the Domain design. Field references have the following format, depending on where the expression appears:

<table>
<thead>
<tr>
<th><p>Appears In</p></th>
<th><p>Field Reference</p></th>
<th><p>Explanation</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Derived table</p></td>
<td><p><code>table_id.field_name</code></p></td>
<td><p>The SQL query that defines a derived table can refer to any previously defined table or derived table in the Domain. Therefore, you must include the table ID.</p></td>
</tr>
<tr>
<td><p>Join expression</p></td>
<td><p><code>table_id.field_name</code></p></td>
<td><p>Within a join expression, tables are given alias names that must be used.</p></td>
</tr>
<tr>
<td><p>Calculated field on a table or derived table</p></td>
<td><p><code>field_name</code></p></td>
<td><p>Calculated fields can only appear on a table if they refer exclusively to fields of the table, in which case no table ID is needed. However, the table ID is not forbidden, and the Domain Designer sometimes includes it.</p></td>
</tr>
<tr>
<td><p>Calculated field on a join tree</p></td>
<td><p><code>table_id.field_name</code></p></td>
<td><p>Calculated fields declared in join trees refer to fields prefixed with their table ID.</p></td>
</tr>
<tr>
<td><p>Filter on a table or derived table</p></td>
<td><p><code>field_name</code></p></td>
<td><p>Filters that are evaluated within the table or derived table do not need the table ID.</p></td>
</tr>
<tr>
<td><p>Filter on a join tree</p></td>
<td><p><code>table_id.field_name</code></p></td>
<td><p>Filters that refer to fields in separate tables of the join tree need to use the table ID on each field name.</p></td>
</tr>
<tr>
<td rowspan="2"><p>Calculated field in an Ad Hoc view</p></td>
<td><p><code>"Field Label"</code></p></td>
<td><p>Calculated fields declared in Ad Hoc views can refer to fields using their item <strong>Label</strong> entered with double quotes (<code>"</code>). Item labels are created on the <strong>Data Presentation</strong> tab of the Domain Designer.</p></td>
</tr>
<tr>
<td><code>table_ID.field_name</code></td>
<td><p>Calculated fields declared in Ad Hoc views can refer to fields prefixed with their table ID.</p></td>
</tr>
</tbody>
</table>
