---
title: Creating and Uploading a Topic for Ad Hoc Views
description: "When a JasperReports Server user creates an Ad Hoc view, she can select a Topic, Domain, or OLAP client connection to provide data to the view. This determines the data presented in the editor and..."
---

# Creating and Uploading a Topic for Ad Hoc Views

When a JasperReports Server user creates an Ad Hoc view, she can select a Topic, Domain, or OLAP client connection to provide data to the view. This determines the data presented in the editor and the features available to the user. A Topic is the simplest to create, because it is just a report unit that defines a query. Most other elements of the report unit (such as its layout) are ignored when it is used as a Topic, though the input controls that you define in the report unit are carried over to the topic's Ad Hoc views and their dependent reports. Topics also support resource bundles and localization.

The following steps show how to create a Topic based on the sample database provided with Jaspersoft Studio, and then upload it to the Topics folder in the JasperReports Server repository.

To create a Topic's JRXML

1.  In Jaspersoft Studio, click **File &gt; New &gt; Jasper Report**. The report wizard appears.

2.  Select a report template and click **Next**.

3.  Select a location to save the JRXML, enter a name for it, and click **Next**.

    In this case, name the file `my-topic.jrxml`.

4.  Select a data adapter for the Topic. In this case, select the Sample DB - database JDBC connection.

    This sample includes the same data as the SugarCRM data source in the JasperReports Server samples.

5.  In the text field, enter a query. In this case, enter:

    `select * from orders`

6.  Click **Next**.

7.  Move all the fields in the left list into the right list and click **Next**.

8.  Click **Next** again to skip past the Group By option.

9.  Click **Finish**. The wizard closes and the Jaspersoft Studio displays the JRXML, which has been saved in the location specified.

To upload the Topic

1.  In the Repository Explorer, expand the Servers node and select the JasperReports Server instance where you want to put the Topic.

    If you have not created any server connections, create one before proceeding. For more information, see [Connecting to JasperReports Server](jss2jrs-connecting.md).

2.  Navigate to the Topic folder. For example, if you are logged in as jasperadmin, navigate to **Ad Hoc Components &gt; Topics**.

3.  Right-click the **Topics** folder and select **New**. The **Add Resource Wizard** appears.

4.  Click **Report Unit** and click **Next**.

5.  Enter a name and optional description it and click **Next**.

6.  Select the **Local Resource** radio button and click ![dotdotdot button](../assets/images/dotdotdot-button.png) to locate and select the JRXML you created above. For example, click **Upload/Download Resource**, click **Upload from Workspace**, select the my-topic.jrxml file.

7.  Click **OK** to close the upload window and click **Next**.

8.  Click the **Data Source from Repository** radio button and click ![dotdotdot button](../assets/images/dotdotdot-button.png) to its right.

9.  Navigate to **Analysis Components &gt; Analysis connections**, select the SugarCRM data source, and click **OK**.

10. Click **Finish** to upload the report unit to the Topics folder so it can be used in the JasperReports Server Ad Hoc Editor.

To test the Topic

1.  Log in to JasperReports Server.
2.  Click **Create &gt; Ad Hoc View**.
3.  On the **Topics** tab of the **Data Chooser**, open the **Topics** folder. For example, navigate to **Organizations &gt; Topics**.
4.  Click the **Topic** that you created above and click **Table**, **Chart**, or **Crosstab**.
5.  Verify that the fields you selected in Jaspersoft Studio all appear in the list of available fields.

!!! note

    If the Topic includes fields with unusual datatypes, those fields do not appear in the Ad Hoc Editor because JasperReports Server is not equipped to manage them properly. For example, if the Topic is defined against a MongoDB instance that returns data of type array, this field is not available in the Ad Hoc Editor. For more information on datatype support in the Ad Hoc editor, see the JasperReports Server Administrator Guide.

When you create a JRXML file for use as a Topic, you can specify the name to display for each field the Topic returns. To do so, define a field property named `adhoc.display` for each field declared in the JRXML. The `adhoc.display` field property must have the following syntax:

`<property name=”adhoc.display” value=”Any Name”/>`

For example, this JRXML code declares a StoreState field displayed in reports as Store State:

``` xml
<field name=”StoreState” class=”java.lang.String”>
 <property name=”adhoc.display” value=”Store State”/>
</field>
```

Topics also support the $R expressions for field names; for more information, see [Expressions](../expressions/expressions.md).

For fields in a non-domain topic the following properties may be of interest:

-   `dimensionOrMeasure`, which marks a field as a field or a measure
-   `defaultAgg`, the aggregation to use for this measure (for example, `avg`)
-   `semantic.item.desc`, a description of the field
-   `DefaultMask`, which sets a measure as a $ or date
