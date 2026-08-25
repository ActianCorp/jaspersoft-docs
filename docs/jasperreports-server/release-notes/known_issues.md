---
title: Known Issues
description: "The following issues exist in this release of JasperReports® Server:"
---

# Known Issues

The following issues exist in this release of JasperReports® Server:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Key</th>
<th>Summary and Workaround</th>
</tr>
</thead>
<tbody>
<tr>
<td>JRL-1655</td>
<td><p><strong>Summary:</strong> For AWS Athena, when a report with the WHERE clause is run in JasperReports® Server , the following error message is displayed:</p>
<p><code>net.sf.jasperreports.engine.JRException: Error preparing statement for executing the report query:</code></p>
<p><code>SELECT *</code></p>
<p><code>FROM sampledb.test</code></p>
<p><code>where sampledb.test.integer = ?</code></p>
<p><strong>Workaround:</strong> Instead of using <code>WHERE sampledb.test.integer = $P{Parameter1} )</code>, provide the WHERE clause in the following format:</p>
<p><code>WHERE sampledb.test.integer = $P!{Parameter1}</code></p></td>
</tr>
<tr>
<td>JS-57241</td>
<td><strong>Summary:</strong> When an ElasticSearch data source is used in a virtual data source, the virtual data source only displays the Base tables of the ElasticSearch data source, not the views, when used in a domain.
<p><strong>Workaround:</strong> None</p></td>
</tr>
<tr>
<td>JS-57742</td>
<td><strong>Summary:</strong> Table joins cannot be used in the domain when using an ElasticSearch data source.
<p><strong>Workaround:</strong> None</p></td>
</tr>
<tr>
<td>JS-57748</td>
<td><strong>Summary:</strong> Aggregations cannot be used on scalar functions in calculated fields when using an ElasticSearch data source.
<p><strong>Workaround:</strong> None</p></td>
</tr>
<tr>
<td>JS-58065</td>
<td><strong>Summary:</strong> Creating an ElasticSearch data source connection might result in an error when using JBoss EAP or WildFly app servers. By default, ElasticSearch data source connections are not available for JasperReports® Server and require additional configuration.
<p><strong>Workaround:</strong> None</p></td>
</tr>
<tr>
<td>JS-58055</td>
<td><strong>Summary:</strong> The Safari browser often blocks access to the Visualize.js script because the script uses third-party cookies to enable cross-site access.
<p><strong>Workaround:</strong> See the JasperReports® Server Visualize.js Guide for workarounds for this issue.</p></td>
</tr>
<tr>
<td>JS-58144</td>
<td><strong>Summary:</strong> If the input string contains a semicolon (<code>;</code>), dash (<code>–</code>), or number sign (<code>#</code>), the SQL validation for an Input Control could result in an error.
<p><strong>Workaround:</strong> None</p></td>
</tr>
<tr>
<td>JS-58145</td>
<td><strong>Summary:</strong> Trying to use input controls for strings and integers for reports with a very large data size (for example, more than 100,000 rows) could result in the JasperReports® Server freezing in the <code>Loading</code> stage until the session is ended.
<p><strong>Workaround:</strong> None</p></td>
</tr>
<tr>
<td>JS-58285</td>
<td><strong>Summary:</strong> When using the Neo4j JDBC data source for a domain, if the pre-filter uses a value with an apostrophe ('). then creating an <code>is one of</code> pre-filter for a table or crosstab returns an error.
<p><strong>Workaround:</strong> None</p></td>
</tr>
<tr>
<td>JS-58316</td>
<td><strong>Summary:</strong> The TIBCO Data Virtualization data source driver does not support using ORDER BY for Boolean columns in queries.
<p><strong>Workaround:</strong> None</p></td>
</tr>
<tr>
<td>JS-58540</td>
<td><strong>Summary:</strong> When using Schemafilter to connect to MongoDB data sources, formats, such as regex, do not work.
<p><strong>Workaround:</strong> Use the <code>ConfigOptions=Schemafilter=&lt;database_name&gt;:&lt; collector_name&gt;</code> format.</p></td>
</tr>
<tr>
<td>JS-58574</td>
<td><strong>Summary:</strong> In recent versions of Mac OS, the Stop and Start scripts in the installation directory cannot be executed without Automator.
<p><strong>Workaround:</strong> None</p></td>
</tr>
<tr>
<td>JS-58860</td>
<td><strong>Summary:</strong>The buildomatic JDBC driver property files for DB2, Oracle, and SQL Server data sources in JasperReports® Server 10.1.0 contain references to old JDBC JAR files.
<p><strong>Workaround:</strong> Change the <code>maven.jdbc.version</code> property in the buildomatic files to the latest JDBC driver versions offered by the developers. You can find these files in the <code>&lt;js-install&gt;/buildomatic/sample_conf/</code> directory.</p></td>
</tr>
<tr>
<td>JS-58890</td>
<td><strong>Summary:</strong> Domain Security does not work for blocked users on Column Level Grants.
<p><strong>Workaround:</strong> None</p></td>
</tr>
<tr>
<td>JS-58922</td>
<td><strong>Summary:</strong> Unable to edit domain when Full Outer Join is applied.
<p><strong>Workaround:</strong> None</p></td>
</tr>
<tr>
<td>JS-60070</td>
<td><strong>Summary:</strong> The domain created from data source using the MongoDB JDBC driver is not editable.
<p><strong>Workaround:</strong> None</p></td>
</tr>
<tr>
<td>JS-62643</td>
<td><strong>Summary:</strong> When executing an AdHoc report when JasperReports® IO is not up and running, the following error message is displayed: <code>An unexpected error has occurred</code> and 500 error code is displayed in the console.
<p><strong>Workaround:</strong> None</p></td>
</tr>
<tr>
<td>JS-62645</td>
<td><strong>Summary:</strong> While executing AdHoc reports in JasperReports® IO and trying to apply any JIVE function, an empty error box, along with 500 error code in the console, is displayed.
<p><strong>Workaround:</strong> None</p></td>
</tr>
<tr>
<td>JS-62646</td>
<td><strong>Summary:</strong> While executing AdHoc reports in JasperReports® IO when you cancel the report load and search for different text, 409 error code is displayed in the console the first time and later the page just displays <code>Loading..</code>.
<p><strong>Workaround:</strong> None</p></td>
</tr>
<tr>
<td>JS-62647</td>
<td><strong>Summary:</strong> While executing AdHoc reports in JasperReports® IO and restarting the JasperReports® IO server, the report keeps on loading and does not display any error message.
<p><strong>Workaround:</strong> None</p></td>
</tr>
<tr>
<td>JS-62674</td>
<td><strong>Summary:</strong> While executing AdHoc reports in JasperReports® IO and navigating from viewing to editing mode in the dashboard, error is displayed in the JasperReports® IO logs.
<p><strong>Workaround:</strong> None</p></td>
</tr>
<tr>
<td>JS-62675</td>
<td><strong>Summary:</strong> When using AdHoc reports in JasperReports® IO and exporting to XML using the <code>/reports</code> endpoint, <code>.jrpxml</code> is appended with the report name.
<p><strong>Workaround:</strong> None</p></td>
</tr>
<tr>
<td>JS-62676</td>
<td><strong>Summary:</strong> When using AdHoc reports in JasperReports® IO and exporting to Excel/XLSX, the output in not generated in non-paginated format.
<p><strong>Workaround:</strong> None</p></td>
</tr>
<tr>
<td>JS-62766</td>
<td><strong>Summary:</strong> The Snowflake JDBC driver does not validate the non-existing or invalid or empty database during connection creation time when passing the db parameter in the connection URL.
<p><strong>Workaround:</strong> None</p></td>
</tr>
<tr>
<td>JS-62783</td>
<td><strong>Summary:</strong> The Snowflake JDBC driver does not validate the warehouse.
<p><strong>Workaround:</strong> None</p></td>
</tr>
<tr>
<td>JS-62826</td>
<td><strong>Summary:</strong> When using AdHoc reports in JasperReports® IO and executing any AdHoc View report using invalid data source details, 500 error code is displayed in the console.
<p><strong>Workaround:</strong> None</p></td>
</tr>
<tr>
<td>JS-63394</td>
<td><strong>Summary:</strong> When running a domain report in a suborganization in JasperReports® IO using Input Control, the following error message is displayed in JasperReports® IO logs: <code>net.sf.jasperreports.engine.JRException: Resource not found at: /organizations/organization_1/qa_automation/Domains/Store</code>.
<p><strong>Workaround:</strong> None</p></td>
</tr>
<tr>
<td>JS-63395</td>
<td><strong>Summary:</strong> When using AdHoc reports in JasperReports® IO, an incorrect Response Content-Type generated for AdHoc View reports.
<p><strong>Workaround:</strong> None</p></td>
</tr>
<tr>
<td>JS-63396</td>
<td><strong>Summary:</strong> When using AdHoc reports in JasperReports® IO, a proper error message is not displayed when an AdHoc report with deleted fields from a domain is run or included into a dashboard.
<p><strong>Workaround:</strong> None</p></td>
</tr>
<tr>
<td>JS-63462</td>
<td><strong>Summary:</strong> For Snowflake connector, a null Pointer Exception is shown when using a data source connection with an invalid host name.
<p><strong>Workaround:</strong> None</p></td>
</tr>
<tr>
<td>JS-65363</td>
<td><strong>Summary:</strong> In the <code>Process Monitor</code> dashboard, data loaded in the work report does not get updated as per the selection done in the work allocation report.
<p><strong>Workaround:</strong> None</p></td>
</tr>
<tr>
<td>JS-65890</td>
<td><strong>Summary:</strong> For report bursting, the Excel output file is not generated after scheduling the burster report with bursting enabled.
<p><strong>Workaround:</strong> None</p></td>
</tr>
<tr>
<td>JS-66367</td>
<td><strong>Summary:</strong> The dashboard filter does not work correctly all the time when charts with the filter are updated.
<p><strong>Workaround:</strong> None</p></td>
</tr>
<tr>
<td>JS-79740</td>
<td><strong>Summary:</strong> JasperReports® Server fails to start following an overlay upgrade from version 9.0.0 to 10.1.0.
<p><strong>Workaround:</strong> Customers can perform either a samedb or newdb upgrade to version 10.1.0, but any previous customizations will need to be reapplied.</p></td>
</tr>
<tr>
<td>JS-70941</td>
<td><p><strong>Summary:</strong> SQE startup fails within the Docker environment (JRS + SQE) due to a <code>java.lang.NoClassDefFoundError: org/quartz/Calendar</code>.</p>
<p><strong>Workaround:</strong> None</p></td>
</tr>
<tr>
<td>JS-79431</td>
<td><strong>Summary:</strong> When attempting to export large reports in JasperReports® Server and JasperReports® IO version 10.1.0, the process fails and throws an error.
<p><strong>Workaround:</strong> None</p></td>
</tr>
<tr>
<td>JSS-3161</td>
<td><strong>Summary:</strong> HighMaps hyperlinks are not functioning as expected. Clicking the links within the report does not trigger navigation.
<p><strong>Workaround:</strong> None</p></td>
</tr>
<tr>
<td>JSS-3254</td>
<td><p><strong>Summary:</strong> For report bursting, when the specified repository folder is non-existent, the folder is not created in the JasperReports® Server repository.</p>
<p><strong>Workaround:</strong> None</p></td>
</tr>
<tr>
<td>JSS-3266</td>
<td><strong>Summary:</strong> For report bursting, invalid parameter name has no validation.
<p><strong>Workaround:</strong> None</p></td>
</tr>
<tr>
<td>JSS-3748</td>
<td><strong>Summary:</strong> Selecting a JSON data adapter and attempting to open the <strong>Add Property</strong> dialog triggers an <code>IllegalArgumentException</code> crash.
<p><strong>Workaround:</strong> None</p></td>
</tr>
<tr>
<td>JSS-3751</td>
<td><strong>Summary:</strong> In Jaspersoft® Studio 9.0.3, users are unable to change the font size of a text field using the toolbar dropdown list.
<p><strong>Workaround:</strong> None</p></td>
</tr>
<tr>
<td>JS-57772</td>
<td><strong>Summary:</strong> Cannot log in to JasperReports® Server due to password length exception.
<p><strong>Workaround:</strong> Ensure that all app servers that participate in a cluster (or when app servers are configured to share the <code>jasperserver</code> repository database) are installed with the same keystore files. For more information, see <a href="https://community.jaspersoft.com/wiki/external-authentication-external-users-are-failing-login-due-password-decryption-and-encryption">Jaspersoft Community article</a>.</p></td>
</tr>
<tr>
<td>JS-57552</td>
<td><strong>Summary:</strong> Using an asterisk (<code>*</code>) for the <code>EndsWith</code> and <code>StartWith</code> functions in the calculated fields results in errors when using an ElasticSearch data source.
<p><strong>Workaround:</strong> None</p></td>
</tr>
<tr>
<td>JS-57241</td>
<td><strong>Summary:</strong> When an ElasticSearch data source is used in a virtual data source, the virtual data source only displays the Base tables of the ElasticSearch data source, not the views, when used in a domain.
<p><strong>Workaround:</strong> None</p></td>
</tr>
<tr>
<td>JS-41999</td>
<td><strong>Summary:</strong> Changing an AdHoc View from table to crosstab may change the timestamp data because of incorrect categorizers for timestamps in the query.
<p><strong>Workaround:</strong> None</p></td>
</tr>
<tr>
<td>JS-34767</td>
<td><strong>Summary:</strong> Administrators in an attempt to import a file receive the following error message on the first attempt: <code>Import failed. The import of an organization to the root is not allowed</code>. Importing the file a second time is successful.
<p><strong>Workaround:</strong> Administrators in a multi-tenant organization can work around this issue by going to <strong>Manage &gt; Server Settings</strong> and right-clicking <strong>Organization</strong> in the tree and choosing <strong>Import...</strong> to import the file. Administrators in a single-tenant organization must go through the import procedure twice to import a file.</p></td>
</tr>
<tr>
<td>JS-34346</td>
<td><strong>Summary:</strong> This release changes resource visibility constraints in multi-tenant deployments (that is, those that include more than one organization). The change disables certain cases of improper resource referencing, such as providing an absolute repository path (starting with the root organization) for a resource referenced in a report. If you have a reference to an image, a subreport, or other resource that has an absolute path (or uses a <code>$P</code> parameter that later resolves to an absolute path), the server returns an error.
<p><strong>Workaround:</strong> Update such references to use paths that you can view in the organization in question. Consider using relative paths, or use the public folder for reports used by multiple organizations.</p></td>
</tr>
<tr>
<td>JS-30847 (was 43707)</td>
<td><strong>Summary:</strong> If a dashboard contains an image dashlet that relies on the <code>repo:</code> syntax to refer to its image, and the <code>superuser</code> exports the dashboard (using the repository's <strong>Export</strong> context menu item or the <strong>Manage &gt; Server Settings &gt; Export</strong> page), the image is not exported with the dashboard.
<p><strong>Workaround:</strong> None</p></td>
</tr>
<tr>
<td>JS-19493</td>
<td><strong>Summary:</strong> XML/A data sources return all datatypes to the AdHoc Editor as strings. When an XML/A-based AdHoc view is saved as a report, JasperReports® Server attempts to convert the data to their original types when the AdHoc view is saved as a report, but in some cases, such as currency, no such type is available. The currency data is converted to type double. The currency is displayed as a number and the currency symbol is omitted.
<p><strong>Workaround:</strong> None</p></td>
</tr>
<tr>
<td>JS-57551</td>
<td><strong>Summary:</strong> Scalar functions cannot be used as a filter for AdHoc views when using an ElasticSearch data source.
<p><strong>Workaround:</strong> None</p></td>
</tr>
<tr>
<td>JS-32077</td>
<td><strong>Summary:</strong> Multi-select input controls for reports treat the values as case-sensitive even if the data source is case-insenstive.
<p><strong>Workaround:</strong> None</p></td>
</tr>
<tr>
<td>JRL-242 (was 17824)</td>
<td><strong>Summary:</strong> While Fusion Charts support annotations, JasperReports® Server and Jaspersoft® Studio do not support them.
<p><strong>Workaround:</strong> None</p></td>
</tr>
<tr>
<td>JS-75621</td>
<td><p><strong>Summary:</strong> The report with HTML Pro component, with a URL, doesn't run correctly and PDF export is continuously loading.</p>
<p><strong>Workaround:</strong> None</p></td>
</tr>
</tbody>
</table>
