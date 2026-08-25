---
title: Creating a Mondrian Connection
description: To create a Mondrian connection
---

# Creating a Mondrian Connection

To create a Mondrian connection

1.  Click **View \> Repository**.

    The repository page appears.

2.  In the **Folders** panel, navigate to **Organization \> Organization \> Analysis Components \> Analysis Connections**.

3.  Right-click the folder and select **Add Resource \> OLAP Client Connection**.

    The **Set Connection Type and Properties** page appears and prompts you to define a connection.

    ![ja add view setconnectiontypepropertiesmondrian](assets/images/ja-add-view-setconnectiontypepropertiesmondrian.png)

    *Figure 1: Set Connection Type and Properties Page*

    By default, the server prompts you to create a Mondrian connection, If you want to create an XML/A connection, refer to [Creating an XML/A Connection to JasperReports Server](creating_an_xml_a_connection_to_jasp.md).

4.  Enter a name and description for the new connection. The **Resource ID** field is auto-generated when you type in the **Name** field. After it is saved, it cannot be changed.

5.  To change the location of the connection, click **Browse**, navigate to a folder, and click **Select**.

6.  Click **Next.**

    The **Locate OLAP Schema page** appears and prompts you to upload an OLAP schema or select one from the repository.

    ![ja add view locateolapschema](assets/images/ja-add-view-locateolapschema.png)

    *Figure 2: Locate OLAP Schema Page*

7.  Click either:

    - **Upload a Local File** to select a file from your local computer.

    Then, click **Choose File**, navigate to select the file, and click **Select**.

    - **Select a resource from the Repository** to select an existing schema.

    Then click **Browse**, navigate to select the file, and click **Select**.

8.  Click **Next**.

    The **OLAP Schema Resource** page appears.

    ![ja add view OLAP schema details](assets/images/ja-add-view-OLAP-schema-details.png)

    *Figure 3: OLAP Schema Resource Page*

    If you chose to upload a new file from your computer, the fields are editable. Enter the requested information. For details, refer [Uploading an OLAP Schema](uploading_an_olap_schema.md). If you choose a file from the repository, the fields are not editable.

9.  Click **Next**.

    The **Locate Data Source** page appears and prompts you to create or select a data source.

    ![ja add view locatedatasource](assets/images/ja-add-view-locatedatasource.png)

    *Figure 4: Locate Data Source Page*

10. Click either:

    - **Define a Data Source in the next step** to add a data source.
    - **Select a Data Source from the repository** to select a data source from the repository.

    Then click **Browse**, navigate to select the file, and click **Select**.

11. Click **Next**.

    The **Set Data Source Type and Properties** page appears.

    ![ja add view setdatasourcetypeproperties](assets/images/ja-add-view-setdatasourcetypeproperties.png)

    *Figure 5: Set Data Source Type and Properties Page*

    If you chose to define a new data source, the fields are editable. Enter the requested information. For details, refer [Working with Data Sources](working_with_data_sources.md). If you chose a data source from the repository, the fields aren’t editable.

12. Click **Next**.

    The **Locate Access Grant Definition** page appears and prompts you to set the properties for the resource.

    ![ja add view locateaccessgrantdefinition](assets/images/ja-add-view-locateaccessgrantdefinition.png)

    *Figure 6: Locate Access Grant Definition Page*

13. Click one of the following:

    - **Do not link an Access Grant** if you do not need to apply for data security.

    Then skip to another step step 16.

    - **Upload a Local File** to select a file from your local computer.

    Then click **Browse,** navigate to select the file you want, and click **Select**.

    - **Select a resource from the Repository** to select an existing schema.

    Then click **Browse**, navigate to select the schema, and click **Select**.

14. Click **Next**.

    If you chose to secure the view, the **Access Grant Resource** page appears.

    ![ja add view accessgrantresourcewindow](assets/images/ja-add-view-accessgrantresourcewindow.png)

    *Figure 7: Access Grant Resource Page*

15. If you chose to upload a new AGXML file, the fields are editable. Enter the requested information. For details, refer to [Uploading an Access Grant Schema](uploading_an_access_grant_schema.md). If you chose an access grant file from the repository, the fields are not editable.

16. Click **Next**.

The Mondrian connection is added to the repository. Views can now reference this connection to expose data to your users. For information on creating OLAP views, refer to [Administering OLAP Views](administering_olap_views.md). For information about creating Ad Hoc views, refer to JasperReports Server User Guide.
