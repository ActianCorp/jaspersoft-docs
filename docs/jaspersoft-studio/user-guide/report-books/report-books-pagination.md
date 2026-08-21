---
title: Report Book Pagination
description: "To ensure that the report book's pagination increments correctly, you need to modify a few variables."
---

# Report Book Pagination

To ensure that the report book's pagination increments correctly, you need to modify a few variables.

To establish the report book pagination

1.  In the Project Explorer, double-click to open **Content_Page_One.jrxml**.
2.  On the Design tab, double-click the text field containing the expression **" "+\$V{PAGE_NUMBER}**.
3.  In the Expression Editor, and click **Variables** in the left panel.
4.  Update the expression to the following:

**"Page "+\$V{MASTER_CURRENT_PAGE}+" of"**

1.  Click **Finish**.
2.  Click to select the text field you just updated. Then in the Properties view, select **Text Field**.
3.  Use the Evaluation Time drop-down menu to select **Master**.
4.  Back in the Design tab, double-click the text field containing the expression **"Page "+\$V{PAGE_NUMBER}**.
5.  In the Expression Editor, and click **Variables** in the left panel.
6.  Update the expression to the following:

`" "+$V{MASTER_TOTAL_PAGES}`

1.  Click **Finish**.
2.  As you did in steps 6-7, use the Evaluation Time drop-down menu to select **Master**.
3.  Save your project.
