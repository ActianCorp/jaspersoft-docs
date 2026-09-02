---
title: Creating and Adding Reports to the Report Book
description: "Now that your framework is established, you can create reports and/or subreports to include in your book."
---

# Creating and Adding Reports to the Report Book

Now that your framework is established, you can create reports and/or subreports to include in your book.

You create a report or subreport as described here, and in [Creating a New Report](../simple-report/reports-creating.md). You can also include previously created reports. See [Adding a Report to the Report Book](#adding-a-report-to-the-report-book).

For our walkthrough, you create a report, then add it to your report book.

## Creating a Report for the Report Book

To create a report

1.  Click ![jss icon new](../assets/images/jss-icon-new.png) and select **Other...** to open the Wizard selection window.

2.  Expand the Jaspersoft Studio folder and select **Jasper Report**. Click **Next**.

3.  In the Report Templates window, scroll to and select the **Leaf Green** template. Click **Next**.

4.  In the Report file window, select the **MyReports** folder and change the Leaf_Green.file name to `Content_Page_One.jrxml`. Click **Next**.

5.  In the Data Source window, select **Sample DB – Database JDBC Connection**, and enter the following query:

    `Select * from orders order by shipcity`

6.  Click **Next**.

7.  In the Fields window, move the following Dataset fields to the Fields panel on the right to include them in your subreport:

-   **ORDERID**

    -   **CUSTOMERID**
    -   **FREIGHT**
    -   **SHIPCITY**
    -   **SHIPCOUNTRY**

1.  Click **Next**.
2.  In the Group By window, move the **SHIPCITY** dataset field into the Fields pane.
3.  Click **Finish**. The **Content_Page_One.jrxml** appears in the Design tab.
4.  In the Project Explorer, right-click **Content_Page_One.jrxml** and select **Compile Report**. The resulting file, Content_Page_One.jasper, appears in the Project Explorer.

## Adding a Report to the Report Book

Now you can add this new subreport to your report book. During this process, you assign a data source for running the subreport.

To add a report to your report book

1.  Double-click the **Sample_Book.jrxml** in the Project Explorer to open it in the Design tab.
2.  Drag **Content_Page_One.jasper** from the Project Explorer into the Content group. In the Connection dialog, click **Finish**.
3.  In the Design tab, click to select **Content_Page_One.jasper**.
4.  In the Properties view, click the **Data** button at the top, then click **Edit Parameters**.
5.  In the Report Part Parameters window, click **Add** to open the Parameter Configuration dialog.
6.  In the Parameter Name field, enter `REPORT_CONNECTION`.
7.  Click ![jss icon expression editor](../assets/images/jss-icon-expression-editor.png) to open the Expression Editor.
8.  In the first column, select **Parameters**.
9.  In the center column, double-click **REPORT_CONNECTION parameter connection** to add it to the editor field, and click **Finish**. The expression appears in the Parameter Configuration field.
10. Click **OK** and confirm that the parameter has been added to the Part Parameters list, then click **Finish**.
