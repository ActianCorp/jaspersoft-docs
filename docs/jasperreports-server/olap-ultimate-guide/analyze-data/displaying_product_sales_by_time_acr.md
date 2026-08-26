---
title: Displaying Product Sales by Time Across Store Locations
description: We can also analyze multiple numeric values across time. Suppose we want to compare the quarterly snack foods sales dollar amount among the West Coast states.
---

# Displaying Product Sales by Time Across Store Locations

We can also analyze multiple numeric values across time. Suppose we want to compare the quarterly snack foods sales dollar amount among the West Coast states.

In the following example, we’ll use the Foodmart Sample Analysis View.

To compare quarterly snack foods sales dollar amounts among the West Coast states

1.  Click **View &gt; Repository** to display the Repository panel.

2.  In the Folders panel, expand the folder **Organization &gt;** **Analysis Components &gt;** **Analysis Views**.

    A list of OLAP views appears in the Repository panel

3.  Click **Foodmart Sample Analysis View** to open it.

4.  Click ![ja pro change data cube](../assets/images/ja-pro-change-data-cube.png).

    For details about using cube dimensions, see [Columns, Rows, and Filters](cube_configuration.md).

5.  Click the **Move to Rows** icon ![ja table move to row](../assets/images/ja-table-move-to-row.png) next to the **Store** filter to create a row, then expand the Store row and select **All Stores &gt; USA**. Click **OK**.

6.  Click the filter icon ![ja table filter](../assets/images/ja-table-filter.png) next to **Product** in the Rows section, then click it and expand to and select **All Products &gt; Food &gt; Snack Foods**.

7.  Click **OK** twice to accept the selections.

8.  Click **Zoom on Drill** to activate it. When active, its tool bar button looks like this ![ja pro zoom on drill active](../assets/images/ja-pro-zoom-on-drill-active.png).

9.  Click the **Edit Display Options** tool bar button ![ja pro editdisplayoptions](../assets/images/ja-pro-editdisplayoptions.png), click the **Show all parent Columns** check box to clear it, and click **OK**.

10. In the table, click **USA** to zoom in.

The following navigation table appears.

![ja ug analysisview foodmart mondrian westcoast](../assets/images/ja-ug-analysisview-foodmart-mondrian-westcoast.png)

2012 Quarterly Snack Food Sales, Dollar Amount, for West Coast States

The view now shows the quarterly snack food sales compared by state.
