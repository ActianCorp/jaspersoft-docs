---
title: Working with XML/A Data Adapters
description: XML/A (XML for Analysis) is an XML standard for accessing remote data in an OLAP schema. Jaspersoft Studio supports an XML/A data adapter that can connect various XML/A providers such as...
---

# Working with XML/A Data Adapters

XML/A (XML for Analysis) is an XML standard for accessing remote data in an OLAP schema. Jaspersoft Studio supports an XML/A data adapter that can connect various XML/A providers such as JasperReports Server and Microsoft SQL Server Analytic Services (SSAS). Because Jaspersoft Studio uses OLAP4J ([http://www.olap4j.org/](http://www.olap4j.org/)), it may also be able to connect to other types of XML/A providers.

The remote server must also be configured for XML/A. For more information, including instructions for configuring Jaspersoft OLAP, see the Jaspersoft OLAP User Guide .

To create an XML/A Data Adapter

1.  Right-click **Data Adapters** in the Repository Explorer, and select **Create Data Adapter**.

2.  Select **XML/A Server** and click **Next**.

3.  Enter a name for the data adapter.

4.  Enter the URL for your XML/A provider. The type of server determines the value. For example:

    - If the XML/A server is JasperReports Server, the URL is something like: `http://<hostname>:<port>/jasperserver-pro/xmla`
    - If the XML/A server is Microsoft SSAS 2012, the URL is something like:

    `http://<hostname>/MSSQL_2012/msmdpump.dll`

5.  Enter a username and password of a user that has sufficient access to the report server to return your data.

6.  Click `Get Metadata`.

    Jaspersoft Studio attempts to connect to the server and return information about its data sources, catalogs, and cubes. If it is successful, default values appear in the drop-downs. If the connection fails, check the URL, ensure that the remote server is available, and try again.

7.  Select the data source, catalog, and cube that stores the data you want for your report.

8.  Click **Test**.

    Jaspersoft Studio connects to the server and read the cube you selected. If the connection fails, check the URL, ensure that the remote server is available, and try again.

9.  When the test succeeds, click **OK** to close the message and click **Finish** to close the **New Data Adapter Wizard**.

When you create a report using this data adapter, you may see a message indicating that the data adapter does not support the ability to retrieve fields. This means Jaspersoft Studio does not have enough information to preview your data. After you provide an MDX query, Jaspersoft Studio can automatically read fields and suggest their datatypes.

## Registration of fields in XML/A Providers

When you create an XML/A data adapter, you define the cube from which to read data. Jaspersoft Studio can then inspect the remote server and suggest datatypes for the fields returned.

To register fields returned by an XML/A data adapter

1.  With your report open in the Design tab, click ![dataset and query button](../assets/images/dataset-and-query-button.png) to open the **Dataset and Query** window.

2.  Select the data adapter that points to your XML/A provider from the dropdown in the upper-left corner.

3.  Select MDX from the **Language** drop-down.

4.  Enter a valid MDX query in the text field.

    To create a good MDX query, you must be familiar with both the language itself and the data you want to work with. You can also use a tool (such as the Jaspersoft OLAP Workbench) to load your OLAP schema and automatically generate MDX queries from it.

5.  Click **Read Fields**.

    Jaspersoft Studio returns the XML/A provider's data, including fields and parameters, and populates the window's tabs with information. For more on how these tabs can be used to define the data in your report, see [Creating Queries](../query-builder-intro.md).

    Jaspersoft Studio also sets the class type of each field to an appropriate Java datatype. If Jaspersoft Studio sets an incorrect datatype, you can set the correct type after the fields are added to your report.

6.  When the data in the **Data Preview** tab looks like the data you want to fill your report, click **OK** to close the **Dataset and Query** window.
