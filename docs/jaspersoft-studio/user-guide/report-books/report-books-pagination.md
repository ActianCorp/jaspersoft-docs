---
title: Report Book Pagination
description: "To ensure that the report book's pagination increments correctly, you need to modify a few variables."
---

# Report Book Pagination

To ensure that the report book's pagination increments correctly, you need to modify a few variables.

To establish the report book pagination

1.  In the Project Explorer, double-click to open **Content_Page_One.jrxml**.

2.  On the Design tab, double-click the text field containing the expression **" "+$V{PAGE_NUMBER}**.

3.  In the Expression Editor, and click **Variables** in the left panel.

4.  Update the expression to the following:

    **"Page "+$V{MASTER_CURRENT_PAGE}+" of"**

5.  Click **Finish**.

6.  Click to select the text field you just updated. Then in the Properties view, select **Text Field**.

7.  Use the Evaluation Time drop-down menu to select **Master**.

8.  Back in the Design tab, double-click the text field containing the expression **"Page "+$V{PAGE_NUMBER}**.

9.  In the Expression Editor, and click **Variables** in the left panel.

10. Update the expression to the following:

    `" "+$V{MASTER_TOTAL_PAGES}`

11. Click **Finish**.

12. As you did in steps 6-7, use the Evaluation Time drop-down menu to select **Master**.

13. Save your project.
