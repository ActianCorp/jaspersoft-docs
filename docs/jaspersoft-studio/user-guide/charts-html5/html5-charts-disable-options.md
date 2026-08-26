---
title: Setting Advanced Options for HTML5 Charts in Properties View
description: You can add or edit advanced options for HTML5 Charts using the Chart Properties dialog. This section shows how to prevent users from changing chart types in the reports that you upload to...
---

# Setting Advanced Options for HTML5 Charts in Properties View

You can add or edit advanced options for HTML5 Charts using the **Chart Properties** dialog. This section shows how to prevent users from changing chart types in the reports that you upload to JasperReports Server.

When you create an HTML5 chart in Jaspersoft Studio and upload it to JasperReports Server, users may see a Canvas Options icon ![js AdHoc icon options](../assets/images/js-AdHoc-icon-options.png). Clicking this icon displays a **Chart Types...** option that allows the user to select a different chart type. You can disable this option at any level – for the chart, for the report, or for this instance of Jaspersoft Studio.

To disable this option for a chart:

1.  Select the chart element in the **Design or Outline** view.

2.  In the **Properties** view for the chart element, click the **Advanced** tab.

3.  Expand the **Misc** section and click **...** next to **Edit Properties**.

    The **Properties** dialog opens.

4.  Click **Add** to add a property.

5.  Enter the following information:

-   **Name**: `com.jaspersoft.jasperreports.highcharts.interactive`

    -   **Value**: `false`

        1.  Click **OK** and then click **Finish**.

        Like many advanced charting options, this option can be set at a higher level. If you set an option at multiple levels, the lowest level is the one that is applied.

-   To disable this option for a report, click the report's root node in **Outline** view and make sure that the **Properties** view is displayed. In the **Properties** view, on the tab, select **Advanced &gt; Misc &gt; Properties** and click **...** to open the **Properties** dialog. Enter the values shown above and click **OK** twice to apply the setting.

-   To disable this option Jaspersoft Studio, select **Window &gt; Preferences** from the menu (**Eclipse &gt; Preferences** on Mac). In the Preferences dialog, select **Properties** and click **Add** to open the **Properties** dialog. Enter the values shown above and click **OK** twice to apply the setting.

You can also set this particular option in JasperReports Server. See the JasperReports Server Administrator Guide for more information.
