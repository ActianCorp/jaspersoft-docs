---
title: Closed Issues
description: "The following issues have been fixed in this release of JasperReports® Server:"
---

# Closed Issues

The following issues have been fixed in this release of JasperReports® Server:

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
<td>JRL-2039</td>
<td>Implement a class whitelist extension to prevent unauthorized or dangerous classes from being loaded during deserialization.</td>
</tr>
<tr>
<td>JS-31960</td>
<td>Data is not displayed in the Crosstab when a filter with the <strong>ElapsedDate</strong> calculated field is applied.</td>
</tr>
<tr>
<td>JS-57052</td>
<td>An error occurred when filtering datetime data in AWS Redshift using an Ad Hoc filter.</td>
</tr>
<tr>
<td>JS-65548</td>
<td>When performing a manual WAR file installation of JasperReports® Server 8.0.0, an error occurred while running the <code>js-ant import-minimal-pro</code> command.</td>
</tr>
<tr>
<td>JS-67848</td>
<td>Ad Hoc View embedded in a JasperReports® Server dashboard incorrectly auto-selects all filter values whereas running same Ad Hoc View in standalone, shows where (1=1) instead of all the values.</td>
</tr>
<tr>
<td>JS-68641</td>
<td>When users upgrade their JasperReports® Server from 7.5 to 8.0 using the samedb script, duplicated scheduled jobs are introduced, resulting in significant performance issues with job execution.</td>
</tr>
<tr>
<td>JS-69038</td>
<td>If JDK 17 is installed on a system, then installing JasperReports® Server using binary installer displayed errors.</td>
</tr>
<tr>
<td>JS-70424</td>
<td>After upgrading to JasperReports® Server 8.2.0, external users are unable to log in to the application and are receiving errors. This functionality worked correctly in JasperReports® Server version 7.5.</td>
</tr>
<tr>
<td>JS-70500</td>
<td>When a user enters a weak password, the system redirects them instead of displaying a password validation error.</td>
</tr>
<tr>
<td>JS-70923</td>
<td>When a user is authenticated via Token Based Authentication, they are unable to successfully export Ad Hoc views or run corresponding Ad Hoc reports.</td>
</tr>
<tr>
<td>JS-71031</td>
<td>JDBC connection leaks are causing Connection Pooling failures and resulting in high JVM memory consumption.</td>
</tr>
<tr>
<td>JS-71042</td>
<td>Input control values fail to refresh upon a new user logging in.</td>
</tr>
<tr>
<td>JS-71193</td>
<td>Column borders are lost on a JasperReport Table when data spans across multiple report pages.</td>
</tr>
<tr>
<td>JS-71577</td>
<td>The Single Select Query Input Control displays the wrong selection after a user performs a search for a value.</td>
</tr>
<tr>
<td>JS-71651</td>
<td><p>User has reported two critical issues with the JasperReports® Server 9.0.0 WAR package installation:</p>
<ul>
<li><p>Missing SQL Server JDBC Configuration: The <code>sqlserver_master.properties</code> (or <code>default_master.properties</code>) file is missing the standard SQL Server JDBC driver configuration details. This omission creates confusion and hinders the clear setup of the JasperReports® Server repository database using Microsoft SQL Server with the standard JDBC driver.</p></li>
<li><p>Missing JDBC Resource Definitions: The <code>js-install.sh</code> minimal script fails to define the <code>jdbc/jasperserverAuditAnalytics</code> and <code>jdbc/jasperserverSystemAnalytics</code> JDBC resources within the context.xml file. This results in server startup failure and the error <strong>javax.naming.NamingException: Could not create resource instance</strong> is displayed.</p></li>
</ul></td>
</tr>
<tr>
<td>JS-71898</td>
<td>Following a session timeout, the presence of the GUID in the URL causes it to become invalid, leading to an intermittent page crash.</td>
</tr>
<tr>
<td>JS-71914</td>
<td>Creating a new user triggers the <code>JSONObject["enabled"] is not a string</code> error.</td>
</tr>
<tr>
<td>JS-71927</td>
<td>SFTP (FTP over SSH) connections are failing for the Scheduler on Rocky Linux 9 and CentOS 8.</td>
</tr>
<tr>
<td>JS-71972</td>
<td>The cascading multi-select input control continually loads and prevents users from selecting any values.</td>
</tr>
<tr>
<td>JS-72016</td>
<td>The inability to disable the Alerts feature poses a risk to system performance.</td>
</tr>
<tr>
<td>JS-72027</td>
<td><p>A user with <code>ROLE_USER</code> is facing functionality issues when accessing a large (15,000+ records) Ad Hoc view from a Snowflake database in JasperReports® Server. The issues include:</p>
<ul>
<li><p>The Ad Hoc view loads very slowly.</p></li>
<li><p>Drill-down functionality in the Ad Hoc view is not working, resulting in a blank screen.</p></li>
</ul></td>
</tr>
<tr>
<td>JS-72194</td>
<td>Drill-down functionality in Ad Hoc views works correctly in the <strong>Edit</strong> mode. But in the <strong>View</strong> mode it fails resulting in a blank page, instead of the expected detailed data.</td>
</tr>
<tr>
<td>JS-72198</td>
<td>Exporting an Ad Hoc report from a dashboard after performing a drill-down results in a blank PDF.</td>
</tr>
<tr>
<td>JS-72210</td>
<td>When editing the scheduler, the recurrence type is incorrectly shown as <strong>Simple</strong> instead of <strong>None</strong>.</td>
</tr>
<tr>
<td>JS-72234</td>
<td>When a ROLE_USER tries to open an Ad Hoc View created from a Snowflake database containing a large dataset of over 15,000 records of visualization type as table or chart (to use drill-down), the view either loads very slowly or fails to load. Additionally, the drill-down feature in the Ad Hoc View is not working and a blank screen is shown.</td>
</tr>
<tr>
<td>JS-72271</td>
<td>Users are unable to create charts when using a Parameterized Report topic as the data source.</td>
</tr>
<tr>
<td>JS-72315</td>
<td>Report execution in JasperReports® Server is failing due to <code>net.sf.jasperreports.engine.JRException: java.lang.NumberFormatException: Input String '4100028930' </code>error.</td>
</tr>
<tr>
<td>JS-72551</td>
<td><p>When the SQL query executor is enabled in JasperReports® Server while creating an Ad Hoc view in <code>NoData</code> mode, database queries are generated when:</p>
<ul>
<li><p>User switches visualization types, for example from Column chart to Crosstab and viceversa.</p></li>
<li><p>User adds fields to Chart visualization.</p></li>
</ul></td>
</tr>
<tr>
<td>JS-72660</td>
<td>Users are unable to open and edit Domains that are imported from JasperReports® Server version 8.0.4 to 9.0.0.</td>
</tr>
<tr>
<td>JS-72997</td>
<td>Using Visualize.js for repeated rendering of reports with input controls causes exceptions.</td>
</tr>
<tr>
<td>JS-73171</td>
<td>When a report is opened, modified, and saved via the <strong>Open in Editor</strong> option in the repository view, the <strong>Modified Date</strong> timestamp fails to update, incorrectly showing the old date and time despite successful changes to the report content.</td>
</tr>
<tr>
<td>JS-73230</td>
<td>The selection order of values in an integer multi-select input control is not preserved when running the report via the scheduler.</td>
</tr>
<tr>
<td>JS-73266</td>
<td>Even when an Ad Hoc view report with no data is scheduled with the <strong>Do not send emails for empty reports</strong> option selected, an email containing an empty report is sent.</td>
</tr>
<tr>
<td>JS-73268</td>
<td><p>In JasperReports® Server version 7.9, to allow existing Ad Hoc views to continue working, <code>&lt;property name="checkSourcesInStrictMode" value="false"/&gt;</code> was set in <code>applicationContext-ad-hoc-dataStrategy.xml</code>.</p>
<p>After upgrading to JasperReports® Server version 9.0.0, the previously implemented workaround is no longer functioning as expected and the existing Ad Hoc views are failing to open.</p></td>
</tr>
<tr>
<td>JS-73279</td>
<td>After upgrading to JasperReports® Server 8.2.0, chart-based Ad Hoc reports are generating console errors upon execution. The error can be viewed in the Console tab of the browser.</td>
</tr>
<tr>
<td>JS-73681</td>
<td>Ad Hoc Views fail to open with a <code>ConcurrentModificationException</code> when they contain date filters and are opened for viewing or editing.</td>
</tr>
<tr>
<td>JS-73692</td>
<td>Scheduler output filenames do not support special characters.</td>
</tr>
<tr>
<td>JS-74069</td>
<td>Cascading input control (IC) values fail to populate on the first attempt. Users must apply a workaround by adding extra spaces or tabs to required fields to trigger the correct population and dismiss the red validation text on the second attempt.</td>
</tr>
<tr>
<td>JS-74097</td>
<td>Attempting to save a dashboard with a Japanese name fails and returns the <strong>Folder not found at xxx</strong> error.</td>
</tr>
<tr>
<td>JS-74555</td>
<td>Repeated Hibernate exceptions in the logs, resulting in the eventual failure of the Tomcat server.</td>
</tr>
<tr>
<td>JS-74637</td>
<td>The <strong>Select All</strong> option is malfunctioning within the Ad Hoc View report input control.</td>
</tr>
<tr>
<td>JS-74599</td>
<td>SFTP error encountered when running scheduled reports on JasperReports® Server 9.0.0 Server.</td>
</tr>
<tr>
<td>JS-74664</td>
<td>The dashboard fails to load or refresh content after a filter is applied, displaying the <strong>This content is not available due to an error</strong> message.</td>
</tr>
<tr>
<td>JS-74815</td>
<td>Installation of JasperReports® Server fails with an <strong>ORA-17056: Non-supported character set: EE8ISO8859P2</strong> error when using the Oracle EE8ISO8859P2 character set.</td>
</tr>
<tr>
<td>JS-74951</td>
<td>The saved Ad Hoc report fails to retain the start date filter, displaying a blank value, even though the date filters appear correctly in the live Ad Hoc view.</td>
</tr>
<tr>
<td>JS-75448</td>
<td>Dashboard performance degrades severely when interacting with linked dashlets, with response time increasing.</td>
</tr>
<tr>
<td>JS-75476</td>
<td>A Null Pointer Exception occurs when users attempt to open a domain topic for editing, specifically if that topic was built using a table found in the JasperServer database.</td>
</tr>
<tr>
<td>JS-76100</td>
<td>The Indian number format is not rendering correctly when applied through conditional formatting in a table.</td>
</tr>
<tr>
<td>JS-76329</td>
<td>Attributes are not being passed through to Ad Hoc reports generated from topics.</td>
</tr>
<tr>
<td>JS-76713</td>
<td>Scheduler is creating duplicate Job IDs in JasperReports® Server 9.0.0.</td>
</tr>
<tr>
<td>JS-76731</td>
<td>The dashboard numeric input control fails (errors out) when all values are deselected by the user.</td>
</tr>
<tr>
<td>JS-77028</td>
<td><p>Using a tenant alias for login requires both the alias and the username to be case-sensitive.</p></td>
</tr>
<tr>
<td>JRWS-141</td>
<td>The spacing functionality for TextFieled/StaticText does not work properly.</td>
</tr>
<tr>
<td>JRWS-1015</td>
<td>When there are multiple Detail bands, JasperReports® Web Studio generates incorrect JRXML with multiple Detail tags.</td>
</tr>
<tr>
<td>JRWS-1016</td>
<td>When an image is set as Lazy, the URL used to render it as div background is invalid.</td>
</tr>
<tr>
<td>JRWS-1047</td>
<td>When you create a report, a new style, and add a conditional expression to edit the style, the designer crashes.</td>
</tr>
<tr>
<td>JRWS-1057</td>
<td>The alignment of text in Text elements is wrong.</td>
</tr>
<tr>
<td>JRWS-1061</td>
<td>When you drag a frame, the content in it also moves, but appears like it does not move. On performing some action, the page is refreshed and the content is repositioned properly.</td>
</tr>
<tr>
<td>JRWS-1064</td>
<td>When previewing an unsaved report, you can view it correctly. However, on previewing the report after saving it, an error is displayed.</td>
</tr>
<tr>
<td>JRWS-1076</td>
<td>When you open the Source Editor of a report and use Ctrl+F multiple times, the JasperReports® Web Studio specific search box is not displayed.</td>
</tr>
<tr>
<td>JRWS-1080</td>
<td>The zoom coefficient is stored in the source, but it is not automatically saved when exiting.</td>
</tr>
<tr>
<td>JRWS-1081</td>
<td>There is a lag in the color selector when selecting a color to fill a shape.</td>
</tr>
<tr>
<td>JRWS-1082</td>
<td>On changing the zoom percentage, the Design Area border width changes.</td>
</tr>
<tr>
<td>JRWS-1101</td>
<td>While previewing a report with 2 parameters that point to .txt files, Preview does not work and the report freezes.</td>
</tr>
<tr>
<td>JRWS-1102</td>
<td>Even when you delete a Text field caption from the expression editor and exit the editor, the caption is still restored.</td>
</tr>
<tr>
<td>JRWS-1103</td>
<td>While changing the Spacing parameters, the selected/deselected Static Text editor preview changes. Also, it looks different when the report is previewed.</td>
</tr>
<tr>
<td>JRWS-1105</td>
<td>When using the support for columns, when you open an existing report, the first columns are grayed out instead of the last.</td>
</tr>
<tr>
<td>JRWS-1109</td>
<td>On resizing an element in a document with margins, the element does not snap to the right margin of the document and there is no line indicating a possible snap.</td>
</tr>
<tr>
<td>JRWS-1112</td>
<td>.gif files are not displayed while browsing for images. However, when you add the .gif image path directly in the image Expression text box, you can use it. But the image is displayed in the editor only after previewing the report.</td>
</tr>
<tr>
<td>JRWS-1114</td>
<td>When you change the Before spacing in a Text field, the text is not displayed properly.</td>
</tr>
<tr>
<td>JRWS-1115</td>
<td>While adding sections in a report from the Outline view, and previewing the report, an error is displayed.</td>
</tr>
<tr>
<td>JRWS-1121</td>
<td>While logging in to JasperReports® Web Studio using any of the options, a blank page is displayed and the user is not able to navigate to the Home page.</td>
</tr>
<tr>
<td>JRWS-1127</td>
<td>The user is unable to edit a Static Text element. While editing the caption, the previous characters are automatically selected (highlighted) and replaced with the newly typed text.</td>
</tr>
<tr>
<td>JRWS-1131</td>
<td>There is an issue preventing the proper configuration of data adapters while working in JasperReports® Web Studio.</td>
</tr>
<tr>
<td>JRWS-1134</td>
<td>When you change the Before spacing in a Static Text element, the element is not displayed properly.</td>
</tr>
<tr>
<td>JRWS-1135</td>
<td>When you change the Before spacing in a Text element, the text is not displayed properly.</td>
</tr>
<tr>
<td>JRWS-1137</td>
<td>At first, the font of the Text field is correctly displayed as SansSerif. But, it changes to Times New Roman immediately (even when it is set as SansSerif in Properties). The same happens in Serif font too.</td>
</tr>
<tr>
<td>JRWS-1143</td>
<td>When you delete a resource, it is still displayed on the page. Only when the page is refreshed, the deleted resource is removed from the page.</td>
</tr>
<tr>
<td>JRWS-1147</td>
<td>There is a difference between the way Static Text and text field elements are displayed in the Editor and in the Preview.</td>
</tr>
<tr>
<td>JRWS-1148</td>
<td>Metadata for the selected data adapter is displayed only on selecting the Read fields option.</td>
</tr>
<tr>
<td>JRWS-1152</td>
<td>When you double-click the Duplicate and Delete options multiple times in a Table element, an error is displayed.</td>
</tr>
<tr>
<td>JRWS-1158</td>
<td>When you change the cell border color in the table editor, there is no change reflected in the table editor as well as the report editor.</td>
</tr>
<tr>
<td>JRWS-1166</td>
<td>After you change the Width or Height of a cell in a table, you cannot select any cell in the table.</td>
</tr>
<tr>
<td>JRWS-1167</td>
<td>When you resize a cell in a row, there is a difference in the size of the resized cell and the other cells in the row.</td>
</tr>
<tr>
<td>JRWS-1170</td>
<td>When you use Separate Cells, the cells below the selected group disappear.</td>
</tr>
<tr>
<td>JRWS-1171</td>
<td>On clicking outside the Width and Height text boxes, the numerical values automatically change to NaN.</td>
</tr>
<tr>
<td>JRWS-1174</td>
<td>On trying to change the Height and Width of a column from Outline, the values are reset to 0 every time you click outside the text box.</td>
</tr>
<tr>
<td>JRWS-1176</td>
<td>When you add a row with merged cells, and try to Separate Cells, the row disappears.</td>
</tr>
<tr>
<td>JRWS-1177</td>
<td>When you expand the Table Row from Outline view, the Table Group Column names are ambiguous.</td>
</tr>
<tr>
<td>JRWS-1180</td>
<td>When you select a cell and Add Column to its left and right, the added columns are wider.</td>
</tr>
<tr>
<td>JRWS-1181</td>
<td>When you add a row from the Table Header in the Outline, and delete the group from the editor, an error is displayed.</td>
</tr>
<tr>
<td>JRWS-1188</td>
<td>When there is a merged/grouped row, even when there are no columns, the Outline displays Table Group Column 1-0. Also, when the cells are separated, their Height is 0 and cannot be modified, and the style is not preserved.</td>
</tr>
<tr>
<td>JRWS-1189</td>
<td><p>When multiple Table Rows are added in a Group Header:</p>
<ul>
<li>Some Table Rows provide the Delete Group option while others provide the Separate Cells option.</li>
<li>When the Separate Cells option is clicked, the row disappears from the Group Header Outline and is moved to Group Footer. And, the original content of Group Footer is replaced.</li>
</ul></td>
</tr>
<tr>
<td>JRWS-1190</td>
<td>When you open a Table element in the editor, and resize the grid, there is inconsistency in resizing it.</td>
</tr>
<tr>
<td>JRWS-1191</td>
<td>When you open two reports and delete a cell from a report, the Height of the deleted cell is not correct.</td>
</tr>
<tr>
<td>JRWS-1192</td>
<td>When you open a table in the editor, and use the vertical scroll bar, the table moves to the right and the horizontal scroll bar cannot be used to view the table. You can view the table only when you decrease the zoom coefficient.</td>
</tr>
<tr>
<td>JRWS-1193</td>
<td>When you add multiple columns to a table, you can use the horizontal scroll bar to view the table. However, the right border of the table is next to the Properties pane.</td>
</tr>
<tr>
<td>JRWS-1194</td>
<td>When you select adjacent cells in a table, depending on the order of the selection, there is inconsistency in the cell borders highlighted and the Merge Cells option displayed.</td>
</tr>
<tr>
<td>JRWS-1195</td>
<td>When you Merge Cells with a colored border, the colored border appears only on one side of the merged cell. When you Separate Cells, the colored border is applied to all the sides.</td>
</tr>
<tr>
<td>JRWS-1196</td>
<td>When you use the Shift key to select the cells in a row, from the last cell to the first cell, it provides an illusion that all the cells in the row are selected.</td>
</tr>
<tr>
<td>JRWS-1197</td>
<td>When you resize the first row of a table, the direction in which the row resizes is unpredictable.</td>
</tr>
<tr>
<td>JRWS-1198</td>
<td>When you open the Table element in the editor, select a cell, and use the arrow keys to move the cell, the cell moves beyond the editor area. However, when you resize the cell, its position is restored.</td>
</tr>
<tr>
<td>JRWS-1199</td>
<td>While trying to change the Styles of any Table Group Column section, an error is displayed.</td>
</tr>
<tr>
<td>JRWS-1200</td>
<td>The Ctrl key can be used to select multiple cells, but cannot be used to deselect cells.</td>
</tr>
<tr>
<td>JRWS-1201</td>
<td>When you select 7 or more cells in a Table, and select Delete, JasperReports® Web Studio freezes and stops responding.</td>
</tr>
<tr>
<td>JRWS-1205</td>
<td>The Merge Cells option is displayed for the merged cells and JasperReports® Web Studio stops responding.</td>
</tr>
<tr>
<td>JRWS-1206</td>
<td>You can only drag the fields into a table from the Dataset pane but not drop them in the table.</td>
</tr>
<tr>
<td>JRWS-1207</td>
<td>When you resize the cells in a table vertically, they are not evenly resized.</td>
</tr>
<tr>
<td>JRWS-1208</td>
<td>When you select multiple cells in a table and change their Height of Properties pane, the cells are not resized evenly.</td>
</tr>
<tr>
<td>JRWS-1209</td>
<td>When you select more than 2 cells in a table, an error is displayed.</td>
</tr>
<tr>
<td>JRWS-1210</td>
<td>When you use the Shift key to select elements from the Outline view, it does not work.</td>
</tr>
<tr>
<td>JRWS-1215</td>
<td>When navigating from Preview to Editor, an error is displayed.</td>
</tr>
<tr>
<td>JRWS-1216</td>
<td>While creating a report, when you switch from Dataset to Properties pane, an error is displayed.</td>
</tr>
<tr>
<td>JRWS-1217</td>
<td>While editing a report, on navigating from the Dataset to the Properties section, an error is displayed.</td>
</tr>
<tr>
<td>JRWS-1218</td>
<td>When you select a cell in a table, and hover the mouse over the options displayed, another cell is highlighted.</td>
</tr>
<tr>
<td>JRWS-1219</td>
<td>When you Add Row in a table and then delete it, the table aspect changes.</td>
</tr>
<tr>
<td>JRWS-1224</td>
<td>When you Add Row in a table, delete the first cell in Outline, Undo the changes, and Delete the second cell in the Outline, the effect of delete is different in both the cases.</td>
</tr>
<tr>
<td>JRWS-1225</td>
<td>When you Add Row to Table Header in Outline, the names of Columns in Column Header change. Also, all the elements in the Outline are not expanded.</td>
</tr>
<tr>
<td>JRWS-1227</td>
<td>When you select multiple cells in a table and click Merge Cells, all table columns disappear.</td>
</tr>
<tr>
<td>JRWS-1231</td>
<td>When you Merge Cells and then Separate Cells, the position of a cell in the Detail band changes.</td>
</tr>
<tr>
<td>JRWS-1232</td>
<td>When you create a report, the Merge Cells option does not work.</td>
</tr>
<tr>
<td>JRWS-1234</td>
<td>On adding an Ellipse in a new report, the outline looks different than usual. However, on changing the Width of the Ellipse the outline appears fine.</td>
</tr>
<tr>
<td>JRWS-1235</td>
<td>When you Merge Cells, and select some cells in Table Header and inspect the Outline, the selected cells are missing form the Outline.</td>
</tr>
<tr>
<td>JRWS-1240</td>
<td><p>When you create two new reports and add a Table element in the first report:</p>
<ul>
<li>When you copy the table to the second report, delete it and copy and paste it again, an error is displayed.</li>
<li>When you add columns in the table in the first report, and copy and paste it in the second report, an error is displayed.</li>
</ul></td>
</tr>
<tr>
<td>JRWS-1241</td>
<td>On clicking Separate Cells for the Group Cell in Group Footer, empty columns in Group Footer are filled with values. The Text fields in the Group Cell (in Group Footer) are preserved, but are arbitrarily distributed to different columns. Also, the columns in the Group Footer are empty and the Text field in the Group Cell (in Group Header) is deleted.</td>
</tr>
<tr>
<td>JRWS-1247</td>
<td>When you Add Row to Table Footer, for the last two cells in the row only the Delete Cell option is available in the Outline. While for the other cells, both Delete Cell and Delete Group options are available in the Outline. On trying to Merge Cells, only the cells with the Delete Group option can be merged.</td>
</tr>
<tr>
<td>JRWS-1248</td>
<td>When you Add Row to Table Footer, for the last two cells in the row only the Delete Cell option is available in the Outline. While for the other cells, both Delete Cell and Delete Group options are available in the Outline.</td>
</tr>
<tr>
<td>JRWS-1259</td>
<td>The elements added in Group Cells of a table are not displayed in the Outline.</td>
</tr>
<tr>
<td>JRWS-1261</td>
<td><p>When you add a Table element in a new report, open it in the editor and add another table element in the table, resize it, and move it to different cells:</p>
<ul>
<li>The new table is mostly displayed in the first cell.</li>
<li>Sometimes, it appears in the Outline and sometimes it does not.</li>
<li>It appears in one cell in the editor, but in a different cell in the Outline.</li>
</ul></td>
</tr>
<tr>
<td>JRWS-1276</td>
<td>The size of some Cross tabs is too wide, obstructing the element editor.</td>
</tr>
<tr>
<td>JRWS-1277</td>
<td>While opening any JRXML file in embedded JasperReports® Web Studio, an error is displayed.</td>
</tr>
<tr>
<td>JRWS-1278</td>
<td>When trying to search for a single character, word, or special character, it is observed that all the instances are not identified.</td>
</tr>
<tr>
<td>JRWS-1284</td>
<td>While creating a data adapter, on selecting a value from the Record Delimiter, Timezone, and Locale drop-downs, the selected field is not displayed in a single click.</td>
</tr>
<tr>
<td>JRWS-1286</td>
<td>While previewing a chart, an error is displayed.</td>
</tr>
<tr>
<td>JRWS-1288</td>
<td>While previewing a report, an error is displayed.</td>
</tr>
<tr>
<td>JRWS-1290</td>
<td>The Properties of a chart are not saved. They are reset to the original state every time you close the preview.</td>
</tr>
<tr>
<td>JRWS-1294</td>
<td>While logging in using GitHub, and trying to test drivers (both existing and new), an error is displayed. Also, the path could not be set.</td>
</tr>
<tr>
<td>JRWS-1295</td>
<td>While trying to drag any element in the Palette in embedded JasperReports® Web Studio, an error is displayed.</td>
</tr>
</tbody>
</table>

## Security Issues

The following security issues have been fixed in this release of JasperReports Server:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th>Key</th>
<th>Area of the Product Affected</th>
<th>Type of Vulnerability</th>
<th>Description and Impact on Users</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>JS-70795</p></td>
<td>N/A</td>
<td>Dependency on third-party libraries</td>
<td><p>Vulnerability in json-20090211.jar:</p>
<ul>
<li><p>CVE-2023-5072</p></li>
<li><p>CVE-2022-45688</p></li>
</ul></td>
</tr>
<tr>
<td>JS-71174</td>
<td>Data Sources</td>
<td>Access to sensitive files</td>
<td>Introduced a validation rule for data source URLs that automatically rejects any address matching localhost or 127.0.0.1.</td>
</tr>
<tr>
<td>JS-71181</td>
<td>User/Tenant Management</td>
<td>Improve organization propagation</td>
<td>Potential security issues allowing a user to be moved from one tenant to another, despite the option not being available in the user interface in the JasperReports® Server is addressed.</td>
</tr>
<tr>
<td>JS-71262</td>
<td>N/A</td>
<td>Dependency on third-party libraries</td>
<td><p>Vulnerability in nevado-jms-1.3.2-JS.jar:</p>
<ul>
<li><p>CVE-2023-31826</p></li>
</ul></td>
</tr>
<tr>
<td>JS-71295</td>
<td>N/A</td>
<td>Dependency on third-party libraries</td>
<td><p>Vulnerability in tiles-api JAR:</p>
<ul>
<li><p>CVE-2023-49735</p></li>
</ul></td>
</tr>
<tr>
<td>JS-71389</td>
<td>N/A</td>
<td>Dependency on third-party libraries</td>
<td><p>Vulnerability in OWASP CSRFGuard through 3.1.0:</p>
<ul>
<li><p>CVE-2021-28490</p></li>
</ul></td>
</tr>
<tr>
<td>JS-71407</td>
<td>N/A</td>
<td>Dependency on third-party libraries</td>
<td><p>Vulnerability in GzipSource:</p>
<ul>
<li><p>CVE-2023-3635</p></li>
</ul></td>
</tr>
<tr>
<td>JS-71591</td>
<td>N/A</td>
<td>Dependency on third-party libraries</td>
<td><p>Security vulnerability in elasticsearch-jdbc-8.2.0.jar:</p>
<ul>
<li><p>CVE-2020-28491</p></li>
</ul></td>
</tr>
<tr>
<td>JS-71620</td>
<td>N/A</td>
<td>Dependency on third-party libraries</td>
<td><p>Upgraded ion-java-1.0.5.jar to resolve the following CVE:</p>
<ul>
<li><p>CVE-2024-21634</p></li>
</ul></td>
</tr>
<tr>
<td>JS-71675</td>
<td>N/A</td>
<td>Dependency on third-party libraries</td>
<td><p>Upgraded Netty Codec to resolve the following CVE:</p>
<ul>
<li><p>CVE-2023-44487</p></li>
</ul></td>
</tr>
<tr>
<td>JS-71676</td>
<td>N/A</td>
<td>Dependency on third-party libraries</td>
<td><p>Upgraded reactor-netty-core-1.0.33.jar to resolve the following CVE:</p>
<ul>
<li><p>CVE-2023-34062</p></li>
</ul></td>
</tr>
<tr>
<td>JS-71687</td>
<td>N/A</td>
<td>Dependency on third-party libraries</td>
<td><p>Upgraded snowflake-jdbc-3.13.33.jar to resolve the following CVE:</p>
<ul>
<li><p>CVE-2021-22573</p></li>
</ul></td>
</tr>
<tr>
<td>JS-71689</td>
<td>N/A</td>
<td>Dependency on third-party libraries</td>
<td><p>Upgraded infinispan-core-10.1.8.Final.jar to resolve the following CVE:</p>
<ul>
<li><p>CVE-2021-22569</p></li>
</ul></td>
</tr>
<tr>
<td>JS-71817</td>
<td>N/A</td>
<td>Dependency on third-party libraries</td>
<td><p>Upgraded poi-4.1.1.jar and poi-ooxml-4.1.1.jar to resolve the following CVE:</p>
<p>CVE-2025-31672</p></td>
</tr>
<tr>
<td>JS-71847</td>
<td>N/A</td>
<td>Dependency on third-party libraries</td>
<td><p>Upgraded ehcache-2.10.9.2.jar to resolve the following CVEs:</p>
<ul>
<li><p>CVE-2020-36518</p></li>
<li><p>CVE-2023-36478</p></li>
</ul></td>
</tr>
<tr>
<td>JS-71852</td>
<td>N/A</td>
<td>Dependency on third-party libraries</td>
<td><p>Upgraded PostgreSQL jar to resolve the following CVE:</p>
<ul>
<li><p>CVE-2024-1597</p></li>
</ul></td>
</tr>
<tr>
<td>JS-71949</td>
<td>N/A</td>
<td>Dependency on third-party libraries</td>
<td><p>Upgraded org.apache.commons:commons-compress to resolve the following CVE:</p>
<ul>
<li><p>CVE-2024-25710</p></li>
</ul></td>
</tr>
<tr>
<td>JS-72030</td>
<td>User Management</td>
<td>Access to sensitive files</td>
<td>Jar file uploads should be restricted exclusively to the operating system (OS) user account.</td>
</tr>
<tr>
<td>JS-72073</td>
<td>N/A</td>
<td>Dependency on third-party libraries</td>
<td><p>Upgraded org.springframework:spring-web to resolve the following CVE:</p>
<ul>
<li><p>CVE-2024-22259</p></li>
</ul></td>
</tr>
<tr>
<td>JS-72074</td>
<td>N/A</td>
<td>Dependency on third-party libraries</td>
<td><p>Upgraded org.springframework.security:spring-security-core to resolve the following CVE:</p>
<ul>
<li><p>CVE-2024-22257</p></li>
</ul></td>
</tr>
<tr>
<td>JS-72091</td>
<td>User Management</td>
<td>Access to sensitive files</td>
<td>When superusers with expired passwords try to log in using REST API, they are able to bypass mandatory password changes and execute administrative functions.</td>
</tr>
<tr>
<td>JS-72109</td>
<td><code>eval</code> changes</td>
<td>Access to sensitive information</td>
<td>Potential security issues stemming from the usage of <code>eval</code> and <code>globalEval</code> in the JasperReports® Server source code are addressed.</td>
</tr>
<tr>
<td>JS-72121</td>
<td>N/A</td>
<td>Dependency on third-party libraries</td>
<td><p>Upgraded com.nimbusds:nimbus-jose-jwt to resolve the following CVE:</p>
<ul>
<li><p>CVE-2023-52428</p></li>
</ul></td>
</tr>
<tr>
<td>JS-72164</td>
<td>N/A</td>
<td>Dependency on third-party libraries</td>
<td><p>Upgraded org.apache.commons:commons-configuration2 to resolve the following CVEs:</p>
<ul>
<li><p>CVE-2024-29133</p></li>
<li><p>CVE-2024-29131</p></li>
<li><p>CWE-787</p></li>
</ul></td>
</tr>
<tr>
<td>JS-72181</td>
<td>N/A</td>
<td>Dependency on third-party libraries</td>
<td><p>Upgraded to Lucene 9.0 to resolve following CVE:</p>
<ul>
<li><p>WS-2021-0646</p></li>
</ul></td>
</tr>
<tr>
<td>JS-72209</td>
<td>N/A</td>
<td>Dependency on third-party libraries</td>
<td><p>Upgraded the Azure CLI version to resolve following CVEs:</p>
<ul>
<li><p>CVE-2023-36052</p></li>
<li><p>CVE-2023-36414</p></li>
<li><p>CVE-2023-36415</p></li>
</ul></td>
</tr>
<tr>
<td>JS-72608</td>
<td>Organization Management</td>
<td>Improve organization propagation</td>
<td>A brief, non-reproducible data exposure occurred where a user from one organization briefly saw another organization's data in an input control, despite all underlying security permissions being confirmed as intact and correctly configured.</td>
</tr>
<tr>
<td>JS-73530</td>
<td>N/A</td>
<td>Dependency on third-party libraries</td>
<td>Enforce a strict Content Security Policy (CSP) that prohibits all 'unsafe' directives.</td>
</tr>
<tr>
<td>JS-73737</td>
<td>N/A</td>
<td>Dependency on third-party libraries</td>
<td><p>Upgraded jasperreports-custom-visualization-6.21.0.jar to resolve the following CVEs:</p>
<ul>
<li><p>CVE-2024-38999</p></li>
<li><p>CVE-2024-38998</p></li>
</ul></td>
</tr>
<tr>
<td>JS-74799</td>
<td>N/A</td>
<td>Dependency on third-party libraries</td>
<td><p>Upgraded mina-core-2.1.6.jar to resolve the following CVE:</p>
<ul>
<li><p>CVE-2024-52046</p></li>
</ul></td>
</tr>
<tr>
<td>JS-75791</td>
<td>N/A</td>
<td>Dependency on third-party libraries</td>
<td><p>Upgraded poi-4.1.1.jar and poi-ooxml-4.1.1.jar to resolve the following CVE:</p>
<ul>
<li><p>CVE-2025-31672</p></li>
</ul></td>
</tr>
<tr>
<td>JS-76592</td>
<td>N/A</td>
<td>Dependency on third-party libraries</td>
<td><p>Upgraded httpclient5-5.4.1.jar to resolve the following CVE:</p>
<ul>
<li><p>CVE-2025-27820</p></li>
</ul></td>
</tr>
<tr>
<td>JSSEC-105</td>
<td>Configuration files</td>
<td>Access to sensitive files</td>
<td><p>Earlier, the server's improper handling of URL path components allowed attackers to bypass intended directory restrictions, enabling unauthorized access to sensitive files using manipulated URLs.</p>
<p>The attacker was able to gain unauthorized access to restricted files, such as the crucial configuration file, <code>WEB-INF/web.xml</code>.</p></td>
</tr>
</tbody>
</table>

For information about cases fixed in previous releases, see that version's release notes. For information about your specific cases, visit [Jaspersoft Technical Support](https://www.jaspersoft.com/support).
