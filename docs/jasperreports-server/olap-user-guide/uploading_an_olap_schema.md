---
title: Uploading an OLAP Schema
description: Upload an OLAP schema to the repository so that it can be accessed by more than one Mondrian connection. Doing this before creating a view simplifies the procedure for defining Mondrian connections...
---

# Uploading an OLAP Schema

Upload an OLAP schema to the repository so that it can be accessed by more than one Mondrian connection. Doing this before creating a view simplifies the procedure for defining Mondrian connections and OLAP views.

As of JasperReports Server version 8.2, Javascript in OLAP schemas is disabled by default. You can upload a schema with Javascript, but it generates an exception when opening the OLAP view. For more information, see [“Enabling Javascript in OLAP Schemas” on page 1](enabling_javascript.md).

To upload a schema

1.  Click **View &gt; Repository**.

    The repository appears.

2.  In the Folder panel, navigate to **Analysis Components &gt; Analysis Schemas**.

3.  Right-click the folder and navigate to **Add Resource &gt; File &gt; OLAP Schema**.

    The **Upload a File From Your Local Computer** page appears and prompts you to select a file and set its properties.

    ![ja add view uploadfilefromyourlocalcomputer](assets/images/ja-add-view-uploadfilefromyourlocalcomputer.png)

    *Figure 1 Upload a File From Your Local Computer - OLAP Schema*

4.  Under **Path to File**, click **Choose File** and locate the OLAP schema you want to add.

5.  Enter a name and description for the schema.

    The **Resource ID** is auto-generated as you type in the **Name** field. You can change the ID if necessary.

6.  Next to the **Save Location** field, click **Browse**, and navigate to the location in the repository where you want the file to reside.

7.  Click **Submit**.

The new file appears in the repository.
