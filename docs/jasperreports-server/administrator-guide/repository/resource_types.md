---
title: Resource Types
description: "Some resources are created interactively, others are uploaded from files. Many of these resource types are used to upload or define the components of reports. The following tables list the resource..."
---

# Resource Types

Some resources are created interactively, others are uploaded from files. Many of these resource types are used to upload or define the components of reports. The following tables list the resource types that users and administrators can create in the repository:

**Resource Types in the Repository**

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>Resource Type</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Ad Hoc view</p></td>
<td><p>Users Create Ad Hoc views interactively in the Ad Hoc Editor by dragging and dropping columns of data onto a table, chart, or crosstab. Users can then explore their data by applying filters and performing pivot operations. An Ad Hoc view can also be saved as an interactive report and shared with other users.</p></td>
</tr>
<tr>
<td><p>Dashboard</p></td>
<td><p>A collection of reports, input controls, graphics, labels, and web content displayed together. Users create dashboards interactively in the Dashboard Designer and save them in the repository.</p></td>
</tr>
<tr>
<td><p>Domain</p></td>
<td><p>A metadata layer that selects, joins, and filters tables and fields from your data. A Domain can be the basis for an Ad Hoc report. Domains also support row-level security and localization of labels. Only administrators may create Domains. Domains are further documented in the <span>JasperReports Server Data Management Using Domains</span>.</p></td>
</tr>
<tr>
<td><p>Topic<br />
Domain Topic</p></td>
<td><p>A report or Domain that has been prepared for use in creating Ad Hoc views. Topics filter and select the fields that are available in the Ad Hoc Editor. Topics are stored in the <span>Ad Hoc Components/Topics</span> folder; they are further documented in the <span>JasperReports Server User Guide</span>.</p></td>
</tr>
<tr>
<td><p>JasperReport<br />
(JRXML report)</p></td>
<td><p>A JasperReport combines a JRXML file, a data source, and optional components such as input controls. Depending on the use case, both users and administrators create JasperReports in the server. For more information, see <a href="jasperreport_structure.md">JasperReport Structure</a>. Procedures for adding reports to the server are described in the <span>JasperReports Server User Guide</span>.</p></td>
</tr>
<tr>
<td><p>Report options</p></td>
<td><p>Reports with input controls allow you to save combinations of input values so that you can run the report again directly. In the repository, report options are always listed under the original report.</p></td>
</tr>
<tr>
<td><p>Content resource</p></td>
<td><p>Report output of any format, either from running a report in the background or from scheduling a report. A content resource is a simple file that the repository allows users to view or download.</p></td>
</tr>
<tr>
<td><p>Data source</p></td>
<td><p>A connection that points to a database or other data store. Data sources define where data is stored for reporting. There are several types of data sources, based on the type of connection or location of the data: JDBC, JNDI, and several others. Only administrators may create data sources. For more information, see <a href="../datasources/datasources_intro.md">Data Sources</a>.</p></td>
</tr>
<tr>
<td><p>Query</p></td>
<td><p>A database query string, for example in SQL. The JRXML doesn't necessarily include the query, in which case, you must define a query resource for use in the JasperReport.</p></td>
</tr>
<tr>
<td><p>Input Control</p></td>
<td><p>A complex type that specifies the values users can input for a report and how the input field appears when running the report, for example radio buttons or check boxes. Input controls depend on datatypes or lists of values to specify the format of the input.</p></td>
</tr>
<tr>
<td><p>Datatype</p></td>
<td><p>A basic resource that defines the format for input values, for example text, number, or date. A datatype may also specify a valid range for the input value.</p></td>
</tr>
<tr>
<td><p>List of Values</p></td>
<td><p>A basic resource that defines a list of arbitrary labels for input. Each label is associated with a value that can correspond to your data. For example, the Month Names List in the sample data associates the name of each month with a value 1 to 12.</p></td>
</tr>
<tr>
<td><p>File</p></td>
<td><p>A resource that stores a file in the repository, usually as part of a report, such as a JRXML file or image logo. The supported file formats are listed in <a href="../resources/file_resources.md">File Resource Types</a>.</p></td>
</tr>
</tbody>
</table>

Administrators and users can also manage OLAP resources in the repository, if their license supports Jaspersoft OLAP. For more information about OLAP and Mondrian resources, see the Jaspersoft OLAP User Guide.

**Resource Types for OLAP**

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>Resource Type</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Mondrian XML/A Source</p></td>
<td><p>A server-side XMLA source definition of a remote client-side XML/A connection.</p></td>
</tr>
<tr>
<td><p>OLAP Client Connection</p></td>
<td><p>Specifies how to retrieve data for an OLAP view. An OLAP client connection is either a direct Java connection (Mondrian connection) or an XML-based API connection<br />
(XML/A connection).</p></td>
</tr>
</tbody>
</table>
