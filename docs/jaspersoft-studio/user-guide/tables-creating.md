---
title: Creating a Table
description: "Once you have placed your table in your report, use the Table Wizard to choose a new or existing dataset for your table."
---

# Creating a Table

To create a table

- To autosize your table, drag the Table element ![table element](assets/images/table-element.png) from the Elements palette into any band of the report.

- To set the size of the table manually when you insert it, click the Table element ![table element](assets/images/table-element.png), but do not drag. The cursor changes ![jss icon loaded palette element](assets/images/jss-icon-loaded-palette-element.png) to show that an element is selected. Click and drag in the report editing area to size and place the element. When you size the table when you first insert it, the columns fill the whole table.

Once you have placed your table in your report, use the **Table Wizard** to choose a new or existing dataset for your table.

|                                                         |
|---------------------------------------------------------|
| ![table wizard new](assets/images/table-wizard-new.png) |
| *Figure 1: Table Wizard - New Table*                    |

To create a new dataset for your table

1.  Select **Create a Table from a new dataset** and click **Next**. The **Dataset** window is displayed.

    |                                                                 |
    |-----------------------------------------------------------------|
    | ![table wizard dataset](assets/images/table-wizard-dataset.png) |
    | *Figure 2: Table Wizard - Dataset*                              |

2.  Name your dataset and select your option: **Create new dataset from a connection or data source** or **Create an empty dataset**. For this example, choose the first option and click **Next**. You are prompted to select a data source and design query.

    |  |
    |----|
    | ![table wizard dataset datasource](assets/images/table-wizard-dataset-datasource.png) |
    | *Figure 3: Table Wizard - Dataset Datasource* |

3.  Select a data source and enter an SQL query such as: `select * from orders` and click **Next**. You are prompted to select dataset fields.

    |  |
    |----|
    | ![table wizard dataset fields](assets/images/table-wizard-dataset-fields.png) |
    | *Figure 4: Table Wizard - Dataset Fields* |

4.  Select the fields that you want in your table and add them to the **Fields** list on the right. Then click **Next**. You are prompted to select the fields to group by from among your chosen fields.

    |  |
    |----|
    | ![table wizard dataset groupby](assets/images/table-wizard-dataset-groupby.png) |
    | *Figure 5: Table Wizard - Dataset \> Group By* |

5.  Select one or more fields to group by and move them to the **Fields** list on the right. Click **Next**. You are prompted to select a connection.

    |                                                                       |
    |-----------------------------------------------------------------------|
    | ![table wizard connection](assets/images/table-wizard-connection.png) |
    | *Figure 6: Table Wizard - Connection*                                 |

6.  Select a data connection option. Your options are:

    - Use the same connection used to fill the master report (the option used in this example)
    - Use another connection (you provide a connection)
    - Use an empty data source
    - Use a JRDatasource expression (you enter a JRDatasource expression)
    - Do not use any data source or connection

7.  Click **Next**. You are prompted to choose the fields for produce table columns.

    |  |
    |----|
    | ![table wizard table columns](assets/images/table-wizard-table-columns.png) |
    | *Figure 7: Table Wizard - Table Columns* |

8.  Select one or more fields to for table columns and move them to the Fields list on the right. Click **Next**. You are prompted to select a layout.

    |                                                               |
    |---------------------------------------------------------------|
    | ![table wizard layout](assets/images/table-wizard-layout.png) |
    | *Figure 8: Table Wizard - Layout*                             |

9.  Select the layout for your table, and click **Finish**. The table appears where you dragged the table element in your report.

|                                                       |
|-------------------------------------------------------|
| ![table in report](assets/images/table-in-report.png) |
| *Figure 9: Report Containing a Table*                 |

To use an existing dataset when creating a table

Creating a table using an existing dataset is largely the same as creating a table using a new dataset.

1.  In the **Dataset** window of the **Table Wizard**, select **Create a Table using an existing dataset**.

2.  Select a dataset from the drop-down.

    |  |
    |----|
    | ![table wizard dataset existing](assets/images/table-wizard-dataset-existing.png) |
    | *Figure 10: Table Wizard - Dataset* |

3.  Click **Next**. You are prompted to select the connection.

From this point, the steps are the same as creating a table using a new dataset.
