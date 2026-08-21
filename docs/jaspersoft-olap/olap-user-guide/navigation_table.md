---
title: Navigation Table
description: "The navigation table appears at the top of the OLAP view (Foodmart Sample Analysis View). It shows the data that is retrieved by the current MDX query, which appears in both the main view and in a..."
---

# Navigation Table

The navigation table appears at the top of the OLAP view ([Foodmart Sample Analysis View](opening_an_olap_view.md)). It shows the data that is retrieved by the current MDX query, which appears in both the main view and in a drill-through tables.

<table>
<caption><p>Navigation Table Icons and Options</p></caption>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th><p>Icon</p></th>
<th><p>Name</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><img src="assets/images/ja-toolbar-expandpositionbutton.png" alt="ja toolbar expandpositionbutton" /></p></td>
<td><p>Expand Position</p></td>
<td><p>Expands rows at a specific hierarchy member.</p></td>
</tr>
<tr>
<td><p><img src="assets/images/ja-toolbar-collapsepositionbutton.png" alt="ja toolbar collapsepositionbutton" /></p></td>
<td><p>Collapse Position</p></td>
<td><p>Collapses rows at a specific hierarchy member.</p></td>
</tr>
<tr>
<td></td>
<td><p>Expand/Collapse Member</p></td>
<td><p>Synchronizes the expansion or contraction of rows across all hierarchy members when they are clicked.</p>
<p><img src="assets/images/ja-navtable-expandmember.png" alt="ja navtable expandmember" /></p></td>
</tr>
<tr>
<td></td>
<td><p>Zoom In/Out</p></td>
<td><p>Click hyperlinked hierarchy members to replace the current table with a sub-table that depicts the selected member. This option is only available when <strong>Zoom on Drill</strong> is enabled.</p></td>
</tr>
<tr>
<td><img src="assets/images/ja-toolbar-zoomoutallbutton.png" alt="ja toolbar zoomoutallbutton" /></td>
<td><p>Zoom Out All</p></td>
<td><p>Restores the navigation table to its initial view after having zoomed. This option is only available when you are in Zoom on Drill mode.</p></td>
</tr>
<tr>
<td> </td>
<td>Show Source Data</td>
<td><p>Click hyperlinked fact data to display additional columns from that specific fact data. The following drill-through table shows the drill-through of Total Unit Sale for Alcoholic Beverages. For more information about the drill-through table’s options, refer to <a href="drill_through_table.md">Drill-through Table</a>.</p>
<p><img src="assets/images/ja-navtable-showsource.png" alt="ja navtable showsource" /></p></td>
</tr>
<tr>
<td><p><img src="assets/images/ja-toolbar-naturalorderbutton.png" alt="ja toolbar naturalorderbutton" /></p></td>
<td><p>Natural Order</p></td>
<td><p>Located next to measure labels, indicates that the navigation table is sorted according to the order of hierarchy members. Click it to change the sort order.</p></td>
</tr>
<tr>
<td><p><img src="assets/images/ja-toolbar-ascendingbutton.png" alt="ja toolbar ascendingbutton" /></p></td>
<td><p>Ascending</p></td>
<td><p>Located next to measure labels, indicates that the navigation table is sorted according to their numeric value, from smallest to largest. Click it to change the sort order.</p></td>
</tr>
<tr>
<td><p><img src="assets/images/ja-toolbar-descendingbutton.png" alt="ja toolbar descendingbutton" /></p></td>
<td><p>Descending</p></td>
<td><p>Located next to measure labels, indicates that the navigation table is sorted according to their numeric value, from largest to smallest. Click it to change the sort order.</p></td>
</tr>
<tr>
<td><p><img src="assets/images/ja-toolbar-expandpositionbutton.png" alt="ja toolbar expandpositionbutton" /></p></td>
<td><p>Expand All</p></td>
<td><p>Located near the top-left corner of the navigation table, expands all of the currently displayed members (all those that display the plus sign) to the next level of detail in the hierarchies. This can be selected repeatedly to expand all levels of detail. This option is only available when the Zoom on Drill is not active. This operation is limited by the memory available to the application server that hosts the JasperReports Server. It stops expanding members when this limit is reached.</p></td>
</tr>
<tr>
<td><p><img src="assets/images/ja-toolbar-collapsepositionbutton.png" alt="ja toolbar collapsepositionbutton" /></p></td>
<td><p>Collapse All</p></td>
<td><p>Located in the top-left corner of the navigation table, collapses the navigation table to its initial view.</p></td>
</tr>
</tbody>
</table>
