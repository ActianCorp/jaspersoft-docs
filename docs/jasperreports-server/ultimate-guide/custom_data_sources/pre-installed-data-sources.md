---
title: Pre-installed Data Source Types
description: "The following data source types are pre-installed with JasperReports Server, but not visible by default in the UI:"
---

# Pre-installed Data Source Types

The following data source types are pre-installed with JasperReports Server, but not visible by default in the UI:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>jdbcQueryDataSource</code></p>
<p><code>mongoDBQueryDataSource</code></p>
<p><code>xmlaQueryDataSource</code></p></td>
<td><p>The query data sources for different types of databases let you specify a query and return a single relational table. Thus the instance of the data source in the server contains a query that limits what data can be further queried by the report or view based on it. The <code>jdbcQueryDataSource</code> type is a generic data source that lets you select any JDBC driver in the UI; the other data source types are instances of the <code>jdbcQueryDataSource</code> type where the JDBC driver is hard-coded for the specific database. In addition, the other data source types have database-specific fields that appear in the UI.</p>
<p>The <code>jdbcQueryDataSource</code> data source type appears in the UI with "Before 6.4" appended to its name.</p></td>
</tr>
<tr>
<td><p><code>jsonDataSource</code></p>
<p><code>JsonSeriesDataSource</code></p>
<p><code>remoteXmlDataSource</code></p></td>
<td><p>The file data sources let you specify a system file as well as a query and return a single relational table. The <code>jsonDataSource</code> and <code>remoteXmlDataSource</code> data source types appear in the UI with "Before 6.4" appended to their name.</p>
<p>For information about using the file-based data sources, see the <span>JasperReports Server Administrator Guide</span>.</p></td>
</tr>
<tr>
<td><p><code>jdbcQueryDataSource2</code></p>
<p><code>jsonDataSource2</code></p>
<p><code>remoteXmlDataSource2</code></p>
<p><code>mongoDBQueryDataSource2</code></p>
<p><code>xlsDataSource</code></p>
<p><code>xlsxDataSource</code></p>
<p><code>textDataSource</code></p></td>
<td><p>These are data sources with full domain that support domain-related features like returning JDBC metadata, creating derived tables, supporting calculated fields, domain pre-filtering, joining other data sources in a virtual data source, and full support in the Domain Designer. The <code>xlsDataSource</code> and <code>xlsxDataSource</code> types are Excel file-based custom data sources and the <code>textDataSource</code> is a <code>text/CSV</code> custom data source.</p>
<p>For information about using these data sources, see <span>JasperReports Server Administrator Guide</span>.</p></td>
</tr>
<tr>
<td><p><code>cassandraQueryDataSource</code></p>
<p><code>HiveDataSource</code></p></td>
<td>These data source types are deprecated. Instead, use a JDBC data source type like Cassandra, Hive, or Impala.</td>
</tr>
</tbody>
</table>

All of these data source types support the following:

-   You can use SQL queries in reports to access the data as a relational table.

-   You can create a Domain based on the data source, allowing you to alter the visibility and names of the fields extracted from the database or file. On the Display tab of the Domain Designer you can also specify which fields are measures.

-   You can create Ad Hoc views using the Domain based on the data source, allowing you to explore and interact with data from the database or file.

-   You can create virtual data sources that combine several data sources. You can then create a Domain based on the virtual data source to join the tables and access the joined data in Ad Hoc views and reports. You can even combine different formats, such as an XML file and MongoDB, as long as their data structures are compatible so the tables can be joined.

## Enabling the Pre-installed Data Source Types

By default, the pre-installed data source types do not appear in the **New Data Source** dialog and must be enabled first.

To make pre-installed data source types available in the UI

1.  Open the file `.../WEB-INF/applicationContext-remote-services.xml` for editing.
2.  Locate the element `<util:set id="customDataSourcesToHide">`.
3.  Comment out the data source types you want to display.
4.  Restart the server.

In the following example, JSON, JSON (Before 6.4), and Remote XML data source types are commented out so they appear in the drop-down menu in the **New Data Source** dialog:

``` xml
<util:set id="customDataSourcesToHide">
        <value>remoteXmlDataSource2</value> <!-- Full domain support remote XML custom data source -->
        <value>remoteXmlDataSource</value>  <!-- Simple single table remote XML custom data source -->
        <value>mongoDBQueryDataSource2</value> <!-- Full domain support mongodb query custom data source -->
        <value>mongoDBQueryDataSource</value>  <!-- Simple single table remote XML custom data source -->
        <value>jsonDataSource2</value> <!-- Full domain support JSON custom data source -->
        <value>jsonDataSource</value>  <!-- Simple single table remote XML custom data source -->
                <value>jsonQLDataSource</value>  <!-- Full domain support JSON QL custom data source -->
        <value>jdbcQueryDataSource2</value> <!-- Full domain support jdbc query custom data source -->
        <value>jdbcQueryDataSource</value>  <!-- Simple single table remote XML custom data source -->
        <!--<value>xlsDataSource</value>  Full domain support XLS custom data source -->
        <!--<value>xlsxDataSource</value> Full domain support XLSX custom data source -->
        <value>textDataSource</value> <!-- Full domain support TEXT/ CSV custom data source -->
        <value>JsonSeriesDataSource</value> <!-- Simple single table remote XML custom data source -->
        <value>xmlaQueryDataSource</value> <!-- Simple single table XMLA Query custom data source -->
        <value>cassandraQueryDataSource</value> <!-- Deprecated.  Please use cassandra SIMBA JDBC driver to run native CQL.  Append "QueryMode=1" in URL in order to run CQL  -->
        <value>HiveDataSource</value> <!-- Deprecated.  Please use Hive/ Impala JDBC drivers instead -->
    </util:set>
```

After a data source type has been enabled in the UI, you can create an instance of that type.

To create a data source using a query example

1.  Log on as an administrator.

2.  Click **View &gt; Repository**, expand the folder tree, and right-click a folder to select **Add Resource &gt; Data Source** from the context menu. Alternatively, you can select **Create &gt; Data Source** from the main menu on any page and specify a folder location later. If you installed the sample data, the suggested folder is Data Sources. The **New Data Source** page appears.

3.  In the Type field, select a data source that you enabled, for example **JSON Data Source (Before 6.4)** or **Remote XML Data Source**. The fields on the page change to prompt for the connection information required for your data source.

    You have the option to use attributes in the values of data source parameters. See the JasperReports Server Administrator Guide for more information.

4.  Fill in the required connection information and enter the query you want to use.

5.  Enter a name for the data source and an optional description. The Resource ID is generated from the name you enter. If you haven't already specified a location, expand the folder tree and select the location for your data source.

6.  Click **Save** in the dialog. The data source appears in the repository.

## Understanding the Pre-installed Data Sources

The Java source for the pre-installed samples can be found online:

1.  Navigate to the pre-installed samples source code:

    <https://github.com/TIBCOSoftware/jasperreports-server-ce/tree/master/jasperserver/jasperserver-custom-datasources/src/main/java/example/cdspro>

The JDBC query and flat file data source types each leverage an existing data adapter class in JasperReports Library. The data adapter class used depends on the data source type. For example, the JDBC query data source type uses a `JDBCQueryDataSourceDefinition` class, based on `JdbcDataAdapterImpl`, to allow the user to enter database connection information and a JDBC query in the **New Data Source** dialog. When a user creates or views a report or Ad Hoc view based on an implementation of this data source type, JasperReports Server creates a JasperReports data source as follows:

-   Builds a custom data source using the JasperReports Library JDBC Data Adapter.
-   `JDBCQueryDataSourceService` creates a JDBC connection based on the driver, URL, username, and password entered by the user.
-   `JRJdbcQueryExecuterFactory` executes the user-defined query and retrieves the metadata layer necessary for Domain support.
-   `JDBCQueryDataSourceService` creates the JasperReports data source that is used by JasperReports Library to fill the report.

In addition, the pre-installed data sources implement Domain support using the `CustomDomainMetaData` class.

You can find the message catalog and Spring bean definition file for each pre-installed data source type in the locations described in [Table 1-1, “Files Used by a Custom Data Source Implementation,” on page 1](custom-data-source-creation.md). The file names are based on the data source name, for example:

`.../WEB-INF/bundles/cassandraqueryds.properties`
