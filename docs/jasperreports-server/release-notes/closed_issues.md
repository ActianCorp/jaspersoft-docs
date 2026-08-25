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
<td>JRIO-841</td>
<td>Jetty and JasperReports Library documentation links are not working in JasperReports® IO application.</td>
</tr>
<tr>
<td>JRIO-842</td>
<td>The system fails to generate the expected PDF output files during report bursting.</td>
</tr>
<tr>
<td>JRIO-844</td>
<td>Formatting dialog does not open for Table reports.</td>
</tr>
<tr>
<td>JRIO-846</td>
<td>The <code>AccessibleReport</code> reference sample located in the JasperReports® IO<code> /samples/reports</code> directory is outdated.</td>
</tr>
<tr>
<td>JRL-2112</td>
<td>When a report is configured with PDF/A properties, JasperReports® Web Studio drops the <code>linkType</code> attribute from <code>JRHyperlink</code> elements. As a result, the generated hyperlinks are non-clickable.</td>
</tr>
<tr>
<td>JS-34719</td>
<td>In JasperReports® Server, memory leak warnings during application shutdown prevented the server process from closing entirely, resulting in orphaned Java processes.</td>
</tr>
<tr>
<td>JS-57111</td>
<td>Incorrect date shown on AdHoc view with Oracle DATE datatype.</td>
</tr>
<tr>
<td>JS-67108</td>
<td>When an Ad Hoc View uses an <strong>Is one of filter</strong> and the <strong>Select All</strong> option is applied, saving the view as an Ad Hoc View report fails to transfer the selection. The resulting report's Input Control shows none of the values selected.</td>
</tr>
<tr>
<td>JS-68665</td>
<td>When navigating to <strong>View &gt; Search</strong>, the system fails to return any results if the query exceeds the maximum parameter limit allowed by SQL Server.</td>
</tr>
<tr>
<td>JS-75375</td>
<td><p>On MySQL platform, the API returns wrong response code after updating permissions.</p></td>
</tr>
<tr>
<td>JS-75655</td>
<td>The Report execution (Async) scenario in JasperReports Server 10.0 exhibited a substantial 30% performance degradation compared to JasperReports Server 9.0.0 during regression testing with a single user. This was attributed to a rise in average latency for all actions, and the performance impact became more pronounced with increasing concurrent users.</td>
</tr>
<tr>
<td>JS-75712</td>
<td>Import with jobs failing on JBoss 8 platform.</td>
</tr>
<tr>
<td>JS-75713</td>
<td>On JBoss 8 platform, when the data format of a timestamp field is altered to show date and time, the resulting format is incorrect. It shows extra comma after date value.</td>
</tr>
<tr>
<td>JS-75735</td>
<td>On MySQL platform, the API returns an incorrect response code after the permission is updated.</td>
</tr>
<tr>
<td>JS-75739</td>
<td>On MySQL platform, the API returns an incorrect response code after an attribute's value or description is updated.</td>
</tr>
<tr>
<td>JS-76888</td>
<td>When accessed via the rest_v2 API endpoints, JasperReports® Server 9.0.0 fails to properly sanitize or escape the <code>type</code> query parameter, allowing arbitrary JavaScript to be executed in the context of the user's browser.</td>
</tr>
<tr>
<td>JS-77015</td>
<td>When an item is deselected from the input control's "Selected" list, the report is not updated.</td>
</tr>
<tr>
<td>JS-77222</td>
<td><strong>Select All</strong> option fails in the <strong>Scheduler</strong> input controls for Ad Hoc View reports.</td>
</tr>
<tr>
<td>JS-77308</td>
<td>Editing and saving an existing Domain Topic updates both its 'Modified' and 'Created' dates to the current date.</td>
</tr>
<tr>
<td>JS-77475</td>
<td>In JasperReports® Server 9.0.0, when user role is added for ERROR MESSAGE, then key details are displayed instead of the value in error message.</td>
</tr>
<tr>
<td>JS-77563</td>
<td>When running an Ad Hoc View report, the Input Controls panel displays locale keys for labels instead of the Input Control labels.</td>
</tr>
<tr>
<td>JS-77638</td>
<td>Users encounter an error when attempting to access folder containing dashboard resources following an upgrade or overlay upgrade on Postgresql database.</td>
</tr>
<tr>
<td>JS-78095</td>
<td>In JasperReports® Server 10.0.0, when a scheduled report job is deleted by a user or an administrator, the deletion is incomplete at the database level. The entries are deleted from some tables and still exist in some.</td>
</tr>
<tr>
<td>JS-78203</td>
<td>JasperReports® Server is currently utilizing deprecated and EOL AWS-Java-SDK-1.x dependencies.</td>
</tr>
<tr>
<td>JS-78365</td>
<td>When JasperReports® Server is configured to use an IBM DB2 database, following a standard major version upgrade or an overlay upgrade to JasperReports® Server 10.0.0, users encounter error dialog when navigating to repository folders containing Dashboard resources.</td>
</tr>
<tr>
<td>JS-78499</td>
<td>In JasperReports® Server 9.0.0, a performance is observed when a user interacts with a report input control and selects the <strong>Select All</strong> option, specifically when the underlying dataset for that input control exceeds 100,000 (100K) values.</td>
</tr>
<tr>
<td>JS-78514</td>
<td>JasperReports® Server 10.0.0 fails to start if the theme is configured to load directly from the local file system rather than the standard metadata repository database.</td>
</tr>
<tr>
<td>JS-78530</td>
<td>In JasperReports® Server 10.0.0, when a report is configured with an optional input control and scheduled with the option to save as a data snapshot, the scheduled execution fails to save data snapshot during output generation.</td>
</tr>
<tr>
<td>JS-78612</td>
<td><p>In JasperReports® Server 10.0.0, when a report has a valid data snapshot saved directly to the repository database, manual execution correctly pulls data from that snapshot under normal conditions.</p>
<p>However, if the Apache Tomcat cache is cleared (deleting the contents of the <code>&lt;tomcat&gt;/temp</code> and <code>&lt;tomcat&gt;/work</code> directories) and the service is restarted, manual report execution runs a fresh query instead of referring to data snapshot which is saved to repository database.</p></td>
</tr>
<tr>
<td>JS-78767</td>
<td>Data source creation is blocked when using a license restricted to the FUSION feature.</td>
</tr>
<tr>
<td>JSS-3194</td>
<td>For jasperQL, aggregate functions are not getting applied on the fields and the column is being returned as blank.</td>
</tr>
<tr>
<td>JSS-3531</td>
<td>When copying and pasting a resource within the same directory in the Repository Explorer, the system does not offer the option to rename the duplicate file.</td>
</tr>
<tr>
<td>JSS-3558</td>
<td>When designing reports in Jaspersoft® Studio using jasperQL, field aggregations are not working correctly.</td>
</tr>
<tr>
<td>JSS-3646</td>
<td>Users were unable to view or access the report options within Jaspersoft® Studio.</td>
</tr>
<tr>
<td>JSS-3705</td>
<td>Allow the table column weight property to accept negative numbers for layout configurations.</td>
</tr>
<tr>
<td>JSS-3706</td>
<td>Fix proposed i18n properties file list in Translation Wizard.</td>
</tr>
<tr>
<td>JSS-3707</td>
<td>Exception thrown when creating table-based reports using the <strong>New Report Wizard</strong>.</td>
</tr>
<tr>
<td>JSS-3710</td>
<td>Jaspersoft® Studio requires internal classes to be explicitly added to the whitelist property for publishing to JasperReports® Server.</td>
</tr>
<tr>
<td>JSS-3730</td>
<td>Reports utilizing Google Maps components are currently failing to render and are throwing timeout errors during execution.</td>
</tr>
<tr>
<td>JSS-3733</td>
<td>After successfully publishing a report to JasperReports® Server, the <strong>Reset</strong> and <strong>Legend</strong> components fail to render on the page.</td>
</tr>
<tr>
<td>JSS-3734</td>
<td>There is a color mismatch with Google Maps components, where the marker colors displayed in the legend box do not align with the actual markers on the map.</td>
</tr>
<tr>
<td>JSS-3749</td>
<td>Fix the UI and input handling behavior of the date widget during report previews.</td>
</tr>
<tr>
<td>JRWS-1113</td>
<td>When you drop an element from the Palette to the Designing Area, the alignment of the existing elements on the Designing Area is not displayed.</td>
</tr>
<tr>
<td>JRWS-1129</td>
<td><p>While creating a report:</p>
<ul>
<li>when the report is not saved, it is correctly previewed.</li>
<li>when the report is saved and previewed, an error message is displayed.</li>
<li>when the report is reopened and previewed, an error message is displayed.</li>
</ul></td>
</tr>
<tr>
<td>JRWS-1296</td>
<td><p>The color of the Search icons in Dataset view and in report preview are different.</p></td>
</tr>
<tr>
<td>JRWS-1300</td>
<td>When you log in using Gdrive, add an image in a report and preview it, an error is displayed. However, when you save the report, you can preview it without any errors.</td>
</tr>
<tr>
<td>JRWS-1303</td>
<td>When you log in using JackRabbit, provide a report Description in Properties view, save, and preview or close the report, the added Description is lost.</td>
</tr>
<tr>
<td>JRWS-1312</td>
<td>When you log in using a local repository, on previewing a report from Samples, an error is displayed.</td>
</tr>
<tr>
<td>JRWS-1315</td>
<td>On starting JasperReports® Web Studio and checking the details for JasperReports® Web Studio 3.0.1 in the command prompt, the details are not available.</td>
</tr>
<tr>
<td>JRWS-1317</td>
<td>Log in using the local repository and open a report from the Samples folder. When you change the chart type, and revert to the original chart type of a report, the chart is not displayed on previewing a report.</td>
</tr>
<tr>
<td>JRWS-1130</td>
<td>Two configuration properties within the dataset fail to apply or execute properly.</td>
</tr>
<tr>
<td>JRWS-1214</td>
<td>Missing documentation for concurrent report execution.</td>
</tr>
<tr>
<td>JRWS-1337</td>
<td>Unable to toggle <strong>Start on a new page</strong> and associated group definition checkbox properties.</td>
</tr>
<tr>
<td>JRWS-1405</td>
<td>On previewing a report in the JasperReports® Server + JasperReports® Web Studiointegrated environment, the left-side bookmarks tab does not display correctly.</td>
</tr>
<tr>
<td>JRWS-1406</td>
<td>Previewing a report in the JasperReports® Server + JasperReports® Web Studiointegrated environment triggers a console error and results in page alignment discrepancies when compared to the standalone JasperReports® Web Studio view.</td>
</tr>
<tr>
<td>JRWS-1471</td>
<td>The initial report in the JasperReports® Server sample library fails to render, triggering a <code>Headers too big</code> HTTP error.</td>
</tr>
<tr>
<td>JRWS-1474</td>
<td>The HTML Pro Component is displayed as unparsed text instead of HTML when rendered via Visualize.js.</td>
</tr>
<tr>
<td>JRWS-1486</td>
<td>When exploring repositories or folders in both Standalone JasperReports® Web Studio and the JasperReports® Server integration, repository paths are no longer visible when attempting to select a data adapter.</td>
</tr>
<tr>
<td>JRWS-1487</td>
<td>A 403 Forbidden error occurs when the system attempts to load the required fonts for <code>FirstJasper.jrxml</code>, preventing the report from rendering correctly.</td>
</tr>
<tr>
<td>JRWS-1488</td>
<td>Prevented users from generating TIBCO maps within the system.</td>
</tr>
<tr>
<td>JRWS-1509</td>
<td>Opening the Query Editor initializes the Text tab as <code>undefined</code> and causes an error upon switching to the Outline tab.</td>
</tr>
<tr>
<td>JRWS-1510</td>
<td><p>Intermittent session/state corruption occurs when navigating from JasperReports® Server back to Jackrabbit repository, resulting in:</p>
<ul>
<li><p>An infinite loading loop when expanding the root <code>(/)</code> path in the <strong>New Report</strong> file picker.</p></li>
<li><p>A save failure error (<strong>Error saving this new report</strong>) on report creation.</p></li>
<li><p>Intermittent errors during the logout process on both repositories.</p></li>
</ul></td>
</tr>
<tr>
<td>JRWS-1513</td>
<td>Switching between Text and Outline tabs in Query Editor deletes the <code>WHERE</code> clause.</td>
</tr>
<tr>
<td>JRWS-1515</td>
<td><p>Issues in the <strong>Properties &gt; Dataset</strong> tab:</p>
<ul>
<li><p>Search function is not working as expected.</p></li>
<li><p>The Custom properties section is misnamed.</p></li>
<li><p>The <code>net.sf.jasperreports.style.fontName</code> property is incorrectly displayed by default in the custom properties section.</p></li>
</ul></td>
</tr>
<tr>
<td>JRWS-1518</td>
<td>Implemented standard multi-select behavior in Repository view (Cmd/Ctrl and Shift clicks).</td>
</tr>
<tr>
<td>JRWS-1519</td>
<td>The <code>jrws.jrs.token.login.url.js</code> file was ignored during token-based SSO. The <code>UIService</code> servlet has been updated to correctly pass this property from <code>jrws.properties</code> to the frontend.</td>
</tr>
<tr>
<td>JRWS-1520</td>
<td>Clean up JasperReports® Web Studio by removing all references to the TibcoMaps component.</td>
</tr>
<tr>
<td>JRWS-1533</td>
<td>A 500 Internal Server Error is triggered when a user attempts to log in using their GitHub account.</td>
</tr>
<tr>
<td>JRWS-1534</td>
<td>Update the JasperReports® Web Studio implementation to adopt and integrate JasperReports® Library export tags.</td>
</tr>
<tr>
<td>JRWS-1537</td>
<td>For Integrated JasperReports® Web Studio, clicking <strong>Get Metadata</strong> triggers a 500 Internal Server Error and fails to retrieve data for the selected data adapter.</td>
</tr>
<tr>
<td>JRWS-1539</td>
<td>When running JasperReports® Web Studio in Standalone mode, statistics are not being captured or tracked for the creation of data adapters.</td>
</tr>
<tr>
<td>JRWS-1542</td>
<td><strong>About</strong> dialog shows incorrect product details when license file is missing.</td>
</tr>
</tbody>
</table>

## Security Issues

The following security issues have been fixed in this release of JasperReports® Server:

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
<td>JSSEC-163/ JRL-2103</td>
<td>Configuration files</td>
<td>Access to sensitive files</td>
<td><p>The server's insecure handling of untrusted object serialization allowed attackers to bypass type validation restrictions, enabling remote code execution via a manipulated report file.</p>
<p>The attacker was able to trigger arbitrary code execution by uploading a malicious JRXML report that forces the server to fetch and parse a crafted <code>.jrprint</code> file, which directly processes untrusted data through an unsafe object input stream. The following CVE was resolved:</p>
<ul>
<li><p>CVE-2026-6009</p></li>
</ul></td>
</tr>
<tr>
<td>JS-70720</td>
<td>N/A</td>
<td>Dependency on third-party libraries</td>
<td><p>Upgraded aws-java-sdk-core-1.11.505.jar to resolve the following CVE:</p>
<ul>
<li><p>CVE-2022-31159</p></li>
</ul></td>
</tr>
<tr>
<td>JS-76514</td>
<td>N/A</td>
<td>Dependency on third-party libraries</td>
<td><p>Upgraded jackson-core-2.13.4.jar to resolve the following CVE:</p>
<ul>
<li><p>CVE-2025-52999</p></li>
</ul></td>
</tr>
<tr>
<td>JS-76953</td>
<td>N/A</td>
<td>Dependency on third-party libraries</td>
<td><p>Upgraded commons-lang3-3.0.jar to resolve the following CVE:</p>
<ul>
<li><p>CVE-2025-48924</p></li>
</ul></td>
</tr>
<tr>
<td>JS-77826</td>
<td>N/A</td>
<td>Dependency on third-party libraries</td>
<td><p>Upgraded Spring JARs to resolve the following CVE:</p>
<ul>
<li><p>CVE-2025-41254</p></li>
</ul></td>
</tr>
<tr>
<td>JS-77889</td>
<td>N/A</td>
<td>Dependency on third-party libraries</td>
<td><p>Upgraded underscore.string to resolve the following CVE:</p>
<ul>
<li><p>WS-2017-3772</p></li>
</ul></td>
</tr>
<tr>
<td>JS-78055</td>
<td>N/A</td>
<td>Dependency on third-party libraries</td>
<td><p>Upgraded Log4j2 JARs to resolve the following CVE:</p>
<ul>
<li><p>CVE-2025-68161</p></li>
</ul></td>
</tr>
<tr>
<td>JS-78254</td>
<td>N/A</td>
<td>Dependency on third-party libraries</td>
<td><p>Upgraded netty-codec-http-4.1.127.Final.jar to resolve the following CVE:</p>
<ul>
<li><p>CVE-2025-67735</p></li>
</ul></td>
</tr>
<tr>
<td>JS-78653</td>
<td>N/A</td>
<td>Dependency on third-party libraries</td>
<td><p>Upgraded the Spring security JARs to resolve the following CVE:</p>
<ul>
<li><p>CVE-2026-22732</p></li>
</ul></td>
</tr>
<tr>
<td>JS-78719</td>
<td>N/A</td>
<td>Dependency on third-party libraries</td>
<td><p>Upgraded Netty jar to 4.1.132.Final and 4.2.10.Final to resolve the following CVE:</p>
<ul>
<li><p>CVE-2026-33870</p></li>
</ul></td>
</tr>
<tr>
<td>JS-79040</td>
<td>N/A</td>
<td>Dependency on third-party libraries</td>
<td><p>Upgraded Log4j2 JARs to resolve the following CVEs:</p>
<ul>
<li><p>CVE-2026-34477</p></li>
<li><p>CVE-2026-34478</p></li>
<li><p>CVE-2026-34479</p></li>
<li><p>CVE-2026-34480</p></li>
</ul></td>
</tr>
<tr>
<td>JSS-3742</td>
<td>N/A</td>
<td>Dependency on third-party libraries</td>
<td><p>Upgraded Log4j2 JARs to resolve the following CVEs:</p>
<ul>
<li><p>CVE-2026-34480</p></li>
<li><p>CVE-2026-34478</p></li>
</ul></td>
</tr>
<tr>
<td>JRWS-1470</td>
<td>HTTP protocol</td>
<td>Cross-Site Request Forgery (CSRF)</td>
<td>Verified and corrected CSRF behavior for JasperReports® Web Studio when embedded within JasperReports® Server, addressing previous integration issues.</td>
</tr>
<tr>
<td>JRWS-1504</td>
<td>N/A</td>
<td>Dependency on third-party libraries</td>
<td><p>Upgraded log4j2 JARs for jrws-jrio-jrs.war and jrws-repository-jrs.war to resolve the following CVE:</p>
<ul>
<li><p>CVE-2025-68161</p></li>
</ul></td>
</tr>
</tbody>
</table>

For information about cases fixed in previous releases, see that version's release notes. For information about your specific cases, visit [Jaspersoft Technical Support](https://www.jaspersoft.com/support).
