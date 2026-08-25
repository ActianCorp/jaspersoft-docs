---
title: Closed Issues
description: "The following issues have been fixed in this release of JasperReports® Web Studio:"
---

# Closed Issues

The following issues have been fixed in this release of JasperReports® Web Studio:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Key</th>
<th>Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td>JRWS-1317</td>
<td><p>While switching a chart type and subsequently reverting it to its original state caused rendering failures during preview.</p></td>
</tr>
<tr>
<td>JRWS-1405</td>
<td>While trying to open a report from JasperReports® Server using the <strong>Open in Editor</strong> option, the <strong>Bookmarks</strong> tab in the report preview would either hide or fail to render correctly.</td>
</tr>
<tr>
<td>JRWS-1406</td>
<td>While trying to open a report from JasperReports® Server using the <strong>Open in Editor</strong> option, there was a discrepancy between the design canvas and the report preview where page alignment appeared inconsistent and triggered console errors.</td>
</tr>
<tr>
<td>JRWS-1411</td>
<td>While working on an existing or a new report, the <strong>Source Editor</strong> icon was displayed different than usual.</td>
</tr>
<tr>
<td>JRWS-1412</td>
<td>While working on an existing or a new report, the <strong>Outline</strong> view was failing to populate. Only the report name is shown, while essential bands like the <strong>Title, Page Header</strong>, and <strong>Detail</strong> sections were missing.</td>
</tr>
<tr>
<td>JRWS-1414</td>
<td>While selecting either a main dataset or a sub-dataset within the <strong>Crosstab Wizard</strong>, the <strong>An unexpected error occurred</strong> exception is displayed.</td>
</tr>
<tr>
<td>JRWS-1422</td>
<td>While creating a report using the <strong>Report Wizard</strong>, <strong>404</strong> error was displayed.</td>
</tr>
<tr>
<td>JRWS-1423</td>
<td>In the <strong>Report Wizard</strong>, when fields are moved from left to right using the arrow buttons, the source items did not reflect their selected state correctly.</td>
</tr>
<tr>
<td><p>JRWS-1429</p></td>
<td>The <strong>New</strong> button is failing to render on the homepage when logging in through <strong>Local Folder, JasperReports Server</strong> and <strong>Google Drive</strong>.</td>
</tr>
<tr>
<td>JRWS-1430</td>
<td>The <strong>Delete</strong> option was not available for newly created user accounts when accessed by an administrator.</td>
</tr>
<tr>
<td>JRWS-1436</td>
<td>The <strong>JDBC Connection</strong> option was missing from the <strong>Data Adapter</strong> selection list when working within a Jackrabbit repository.</td>
</tr>
<tr>
<td>JRWS-1437</td>
<td>The <strong>Data Adapter</strong> selection failed to update the UI even after switching to a different adapter. The configuration and format was stuck on the previous selection and did not reflect the new data source.</td>
</tr>
<tr>
<td>JRWS-1439</td>
<td>When pasting copied or cut items into a new directory, the resources were being placed in the parent directory rather than inside the intended target folder.</td>
</tr>
<tr>
<td>JRWS-1440</td>
<td>When a new file or folder was uploaded, the uploaded files did not appear immediately in the repository view. The file list was not refreshed automatically and a manual refresh was required to view the files.</td>
</tr>
<tr>
<td>JRWS-1441</td>
<td><p>While creating a <strong>New Data Adapter</strong>:</p>
<ul>
<li><p>The <strong>Test</strong> functionality failed for all data sources except <strong>Empty Data</strong> and <strong>Random Data</strong> adapters.</p></li>
<li><p>The <strong>Save</strong> button remained in a disabled state even when all mandatory parameters were correctly populated.</p></li>
<li><p>The <strong>Undo</strong> and <strong>Redo</strong> operations were inconsistent across all data adapter configurations.</p></li>
</ul></td>
</tr>
<tr>
<td>JRWS-1461</td>
<td><p>While creating a <strong>New Data Adapter</strong> and checking the statistics:</p>
<ul>
<li><p>When modifying and saving a secondary data adapter, the system incorrectly overwrote the configuration of the first-created adapter instead of the active one.</p></li>
<li><p>Statistics and metadata were only being generated for the primary data adapter; subsequent adapters failed to produce or display their respective stats.</p></li>
</ul></td>
</tr>
<tr>
<td>JRWS-1471</td>
<td>The first report in JasperReports® Server samples failed to render, triggering a <strong>Headers too big</strong> overflow error.</td>
</tr>
<tr>
<td>JRWS-1473</td>
<td><ul>
<li><p>Enabling the <strong>Ignore Pagination</strong> attribute at the report level caused the preview engine to fail due to a type mismatch error.</p></li>
<li><p>The <strong>File Selection</strong> dialog occasionally generated incorrect resource paths. For example, selecting a data adapter located from the samples folder while working on a report in a sibling folder resulted in a broken path reference.</p></li>
</ul></td>
</tr>
<tr>
<td>JRWS-1476</td>
<td>When clicking the ellipsis (...) menu in the <strong>Dataset &gt; Parameters</strong> section, the <strong>An unexpected error occurred</strong> exception is displayed.</td>
</tr>
<tr>
<td>JRWS-1477</td>
<td>In the <strong>Calculation Configuration Wizard</strong>, when the <strong>Highest</strong> calculation type was selected for a numeric field, the element expression and the respective variable incorrectly displayed the label as <strong>Lowest</strong>.</td>
</tr>
<tr>
<td>JRWS-1484</td>
<td>While testing a data adapter <strong>Report Wizard</strong>, <strong>404</strong> error was displayed.</td>
</tr>
<tr>
<td>JRWS-1485</td>
<td>When attempting to preview reports within JasperReports® Web Studio, both authorization and authentication errors occurred.</td>
</tr>
<tr>
<td>JRWS-1486</td>
<td>After navigating through various folders or repositories, the file path breadcrumbs or labels disappeared when attempting to select a data adapter.</td>
</tr>
<tr>
<td>JRWS-1487</td>
<td>While loading font in the <strong>FirstJasper.jrxml</strong> sample report, <strong>403</strong> error was displayed.</td>
</tr>
</tbody>
</table>
