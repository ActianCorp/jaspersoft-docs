---
title: Working with Topics
description: "When a user clicks Create > Ad Hoc View on the Home page, the Select Data wizard offers a path to the list of Topics populated from the Ad Hoc Components/Topics folder in the repository. There are..."
---

# Working with Topics

When a user clicks **Create \> Ad Hoc View** on the Home page, the Select Data wizard offers a path to the list of Topics populated from the Ad Hoc Components/Topics folder in the repository. There are two types of Topics:

- JRXML-based Topics–Created by administrators using Jaspersoft Studio and uploaded as JRXML files to the proper location in the repository. Topics are typically of this type.
- Domain Topics–Created from a Domain by administrators using JasperReports Server.

Either type of Topic is an empty view associated with a data source in the server, and is then built on in the Ad Hoc Editor.

## Uploading a Topic Through the Web UI

JRXML-based topics are the most common type of topic. You can upload previously created JRXML topics via the repository.

To upload a JRXML-based Topic

1.  Log in to the server as an administrator and select **View \> Repository**.

    !!! note

        While any user with sufficient repository permissions can upload a Topic to the server, this example requires an administrator login to access the JServer Jdbc data source.

2.  Locate the folder where Topics are stored. The location of the Topics folder depends on your system configuration. By default, Topics are in the **Ad Hoc Components \> Topics** folder.

3.  Right-click the Topics folder name and select **Add Resource  \> JasperReports®** from the context menu. The Set Up the Report page of the Jasper Report wizard appears.

    !!! note

        **Add Resource** appears on the context menu only if your login account has write privilege to the folder.

4.  In the Set Up the Report page, give the Topic a name, a Resource ID, and an optional description, then click **Next**.
    - The **Name** field is the visible name of the file in the repository, such as `Example Topic`.
    - The **Resource ID** field is the internal ID of the object, such as `Example_Topic`. The server does not accept spaces in an internal ID.
    - The **Description** field, such as `Topic uploaded for User Guide example`, helps users understand the purpose of the file.

5.  In the **Locate the JRXML File** section, select **Upload a Local File**, and click **Browse** to locate the file and upload the Topic from the file system. In this example, the file is \<js-install\>/samples/adhoc/topics/adhoc_sample.jrxml.

    !!! note

        To locate adhoc_sample.jrxml, you need access to the server host file system.

6.  Click **Data Source**.

    !!! note

        Because this is a simple Topic without parameters, there are no controls and resources associated with it. If the Topic has a Parametrized query, you can create input controls for it. See [Selecting a Data Source for Running the Complex Report](../repo-upload-reports/repo-data-source-complex-report.md). Such input controls can appear in the Ad Hoc Editor and when the report is run.

7.  Click **Select data source from repository** and **Browse** to locate the data source named **Data Sources/JServer Jdbc data source**.

8.  Select Data Source, then click **Select**.Topics must be associated with the data source that they were designed for.

9.  Click **Submit** at the bottom of the screen.

    Topics usually do not need a query or customization, but you can define them.

When you select **Create \> Ad Hoc View** and click ![js Dashboard icon ViewTree](../assets/images/js-Dashboard-icon-ViewTree.png) in the Select Data wizard, you can browse to **Ad Hoc Components \> Topics**. If you select the Example Topic, you can create a report using the columns available in the data source selected in step 7.

The JRXML file that the Topic is based on must contain a query and a field list.

!!! note

    Any report layout in the Topic’s JRXML file is ignored by the Ad Hoc Editor. We recommend that a Topic’s JRXML file not include anything other that the query and field list.

When you create a JRXML file for use as a Topic, you can specify the name to display for each field that the Topic returns. To do so, define a field property named `adhoc.display` for each field declared in the JRXML. The `adhoc.display` field property must have the following syntax:

` <property name=”adhoc.display” value=”Any Name”/>`

!!! note

    If the Topic includes fields with unusual datatypes, those fields do not appear in the Ad Hoc Editor because it is not equipped to manage them properly. For example, if the Topic is defined against a MongoDB instance that returns data of type array, this field is not available in the Ad Hoc Editor. For more information on datatype support in the Ad Hoc editor, see the JasperReports Server Administrator Guide.

For example, this JRXML code declares a StoreState field that is displayed in reports as Store State:

``` xml
<field name=”StoreState” class=”java.lang.String”>
<property name=”adhoc.display” value=”Store State”/>
</field>
```

Topics also support the \$R expressions for field names; for more information, see [Localizing Reports](../repo-upload-reports/repo-localizing-reports.md).

For fields in a non-domain topic the following properties may be of interest:

- `dimensionOrMeasure`: Marks a field as a field or a measure.
- `defaultAgg`: Which aggregation should be used for this measure (avg, etc.).
- `semantic.item.desc`: A description for the field.
- `defaultMask`: Set a measure as a \$, date etc.

For more information on working with JRXML topics, see the Jaspersoft Studio User Guide.
