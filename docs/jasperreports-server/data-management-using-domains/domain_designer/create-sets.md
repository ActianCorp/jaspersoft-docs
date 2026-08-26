---
title: Working with Sets and Items
description: "To move a resource to Sets and Items, drag it from the Data Structure panel and drop it in Sets and Items. A blue bar appears in the target location. If you can't see the blue bar, then you can't..."
---

# Working with Sets and Items

Adding a set or item

To move a resource to **Sets and Items**, drag it from the **Data Structure** panel and drop it in **Sets and Items**. A blue bar appears in the target location. If you can't see the blue bar, then you can't drop the resource in that location.

-   To drop a resource in an existing data island or set, drag it anywhere in the data island or set. It appears at the bottom.

-   To add a resource that does not belong to an existing data island, drag the resource to the top or bottom of the Sets and Items list, or in the area between any two data islands. The resource is added, along with the data island that contains it. If you drag a join tree, it creates the corresponding data island.

To move most of the tables and columns in a join tree or a table to Sets and Items

1.  Drag-and-drop a join tree or table from the **Data Structure** panel to **Sets and Items**.

    -   If you drag a join tree, it is added as a data island, all tables are added as sets, and columns are added as items within the sets.

    -   If you drag a table, the table is added as a set, and all columns in the table are added as items with the set.

2.  Remove any unwanted sets or items individually from **Sets and Items** using ![js DomainDesigner icon remove](../assets/images/js-DomainDesigner-icon-remove.png).

To move a few columns from a join tree or a table to Sets and Items

1.  Drag a single column from the **Data Structure** panel to **Sets and Items**.

-   If the column is part of a join tree, the join tree is added as a data island, and the column is added as an item directly under that data island.

    -   If the column is part of an unjoined table, the table is added as a data island and the column is added as an item.

1.  Continue to drag columns to the data island that was created in the first step.

Columns are added directly to the data island.

To create an empty set

You can create empty sets. If the parent is a data island or a set , the set can contain items from different tables.

1.  Click on the set or data island you want as a parent.
2.  Click **Add Set**. You must have a parent selected to use **Add Set**. This button is not active if you do not have any data islands.

The new set appears at the bottom of the parent set you chose. Drag resources from the same join tree or unjoined table to add them to the set.

To change the order of items within a set in Sets and Items

1.  Select the item.
2.  Reposition the item using one of the following buttons:

![js DomainDesigner icon Move Top](../assets/images/js-DomainDesigner-icon-Move-Top.png) Move to top.

![js DomainDesigner icon Move Up](../assets/images/js-DomainDesigner-icon-Move-Up.png) Move up.

![js DomainDesigner icon Move Down](../assets/images/js-DomainDesigner-icon-Move-Down.png) Move down.

![js DomainDesigner icon Move Bottom](../assets/images/js-DomainDesigner-icon-Move-Bottom.png) Move to bottom.

You can also reposition an item or set by dragging.

!!! note

    Individual items inside a set always appear above subsets. You can't move individual items below the sets.
