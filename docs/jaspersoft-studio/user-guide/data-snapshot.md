---
title: Using Data Snapshots
description: "Data snapshots store a static snapshot of the data that you need to run a report. Without data snapshots, you can only run a report if you have access to everything the report depends on, in..."
---

# Using Data Snapshots

Data snapshots store a static snapshot of the data that you need to run a report. Without data snapshots, you can only run a report if you have access to everything the report depends on, in particular, the data used by the report and its subreports or subdatasets. A data snapshot saves the data for a specific run so that you can run the report without any data connections. This lets you work on report layout and presentation offline, share a version of the report for troubleshooting, or create a sample report together with the data.

The snapshot only contains the data needed by the report at the time that it is run. If you change the report that affect its data use, such as adding fields, you need to create an updated snapshot. When **Cache Data in Memory** is selected and you have made changes that affect the data use, this is detected and the cached data is automatically updated. Changes that only affect the layout, such as moving fields or resizing bands, do not trigger a cache update.

To create a data snapshot

1.  Select the **Preview** tab.
2.  Click the ![jss icon report data snapshot](assets/images/jss-icon-report-data-snapshot.png) icon and select **Data Snapshot Options**. The **Data Snapshot Options** dialog appears.
3.  Select the **Enable data snapshot** checkbox and click **OK**.
4.  Run the report to capture the report data.

To save a data snapshot to a file

1.  Select the **Preview** tab.
2.  Click the ![jss icon report data snapshot](assets/images/jss-icon-report-data-snapshot.png) icon and select **Data Snapshot Options**.
3.  Click **Browse** to save the report data to a file.
4.  Enter a file name and click **Save**. The file is saved with a **.jrds** (JasperReports data snapshot) extension.
5.  Click **OK** on the **Data Snapshot Options** dialog.
6.  Run the report to capture the report data in the file you just created.

To update a data snapshot with new data

1.  Select the **Preview** tab.
2.  Click the ![jss icon report data snapshot](assets/images/jss-icon-report-data-snapshot.png) icon and select **Data Snapshot Options**.
3.  Deselect **Enable data snapshot** checkbox and click OK.
4.  Run the report to update the latest report data.
5.  Click ![jss icon report data snapshot](assets/images/jss-icon-report-data-snapshot.png) and select **Data Snapshot Options**.
6.  Select the **Enable data snapshot** checkbox and click OK. You can also save the updated report data in the file.

To use a data snapshot

1.  Select the **Preview** tab.
2.  Click the ![jss icon report data snapshot](assets/images/jss-icon-report-data-snapshot.png) icon and select **Load Data From File.**
3.  Select the existing file and click **Open**.

The data in the snapshot is used to fill the report. Information about the snapshot is displayed in the **Report State** window, including when the snapshot was created (Data Queried At) and the name and location of the snapshot file.
