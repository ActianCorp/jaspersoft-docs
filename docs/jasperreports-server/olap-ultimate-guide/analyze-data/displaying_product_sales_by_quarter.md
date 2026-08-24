---
title: Displaying Product Sales by Quarter
description: Jaspersoft OLAP is well suited to comparing numeric data across a period of time or by product category. That is how to answer the example question about snack food sales.
---

# Displaying Product Sales by Quarter

Jaspersoft OLAP is well suited to comparing numeric data across a period of time or by product category. That is how to answer the example question about snack food sales.

To open the sample OLAP view

1.  Click **View \> Repository** to display the Repository panel.
2.  In the Folders panel, expand the folder **Organization \>** **Analysis Components \>** **Analysis Views**.

A list of OLAP views appears in the Repository panel.

1.  Double-click to open **Foodmart Sample Analysis View**.

The default navigation table appears along with the Jaspersoft OLAP tool bar.

![ja ug foodmart default](../assets/images/ja-ug-foodmart-default.png)

*Figure 1: FoodMart Sample OLAP View*

To find the quarterly sales dollar amount in 2012 for stores in California

1.  Click the **Change Data Cube** tool bar button: ![ja pro change data cube](../assets/images/ja-pro-change-data-cube.png).

The Change Data Cube dialog appears.

![ja ug analysisview tools ChangeDataCube Cubetools](../assets/images/ja-ug-analysisview-tools-ChangeDataCube-Cubetools.png)

*Figure 2: Change Data Cube*

The Change Data Cute dialog includes the following sections:

- Columns
- Rows
- Filters

1.  Next to the Time filter, click the **Move to Columns** icon ![ja table move to column](../assets/images/ja-table-move-to-column.png) to make Time a column.

![ja ug analysisview tools ChangeDataCube Cubetools TimeColumn](../assets/images/ja-ug-analysisview-tools-ChangeDataCube-Cubetools-TimeColumn.png)

*Figure 3: Adding a Time Column*

1.  In the Columns section, click **Time** to open a tree displaying the dimension members.
2.  Expand Time by clicking ![ja table expand red](../assets/images/ja-table-expand-red.png) next to it, and select **2012**.

![ja ug analysisview tools ChangeDataCube Cubetools Time2012filter](../assets/images/ja-ug-analysisview-tools-ChangeDataCube-Cubetools-Time2012filter.png)

*Figure 4: Defining the Time Filter*

1.  Click **OK** to close the tree and return to the Change Data Cube dialog.

!!! note

    Changes you make in the Change Data Cube dialog are not applied to the view until you click **OK** again to close the dialog. Thus, while the Change Data Cube dialog is open, the view will not match your selections in the dialog.

1.  In the Change Data Cube dialog, click **Store** in the Filter list to change the filter.

The Store filter appears.

1.  Expand **All Stores** by clicking ![ja table expand red](../assets/images/ja-table-expand-red.png) next to it, then expand **USA**, and select **CA**.

![ja ug analysisview tools ChangeDataCube Cubetools StoreCAfilter](../assets/images/ja-ug-analysisview-tools-ChangeDataCube-Cubetools-StoreCAfilter.png)

*Figure 5: Defining the Store Filter*

1.  Click **OK** to close the tree and return to the Change Data Cube dialog.
2.  Click **Measures** and clear the checkboxes next to Unit Sales and Store Cost to remove them.
3.  Click **OK** to accept the selections and close the Measures list, then click **OK** again to close the dialog.

Jaspersoft OLAP updates the view to match your selections. It is now filtered to show only the sales data for stores in California.

![ja ug analysisview foodmart ca 2012 without drill](../assets/images/ja-ug-analysisview-foodmart-ca-2012-without-drill.png)

*Figure 6: 2012 Store Sales Volume for Snacks at California Stores*

1.  Ensure that the Zoom on Drill is active by checking whether its icon is pressed:

- When **Zoom on Drill** is active, its tool bar button looks like this ![ja pro zoom on drill active](../assets/images/ja-pro-zoom-on-drill-active.png).
- When **Zoom on Drill** is not active, its tool bar button looks like this ![ja pro zoom on drill](../assets/images/ja-pro-zoom%20on%20drill.png). Click it to enable zooming when you click a dimension member.

Now, when the cursor hovers over a dimension member, it changes to ![ja table zoomSelector](../assets/images/ja-table-zoomSelector.png).

1.  Click **2012** to zoom into 2012 data.
2.  Click ALL PRODUCTS, Food, and Snack Foods to zoom into this data.
3.  Click the **Edit Display Options** tool bar button ![ja pro editdisplayoptions](../assets/images/ja-pro-editdisplayoptions.png), click the **Show all parent Columns** checkbox to clear it, and click **OK**.

The following navigation table appears:

![ja ug analysisview foodmart mondrian CA](../assets/images/ja-ug-analysisview-foodmart-mondrian-CA.png)

*Figure 7: 2012 Quarterly Store Sales Volume for Snacks at California Stores*

This view now shows the total sales for snack food in stores in California for 2012, broken down by quarter.

The following sections build on this example.
