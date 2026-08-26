---
title: Adding an Autonomous REST JDBC Driver
description: 1. Request the Support team to provide the TIautorest Progress JAR.
---

# Adding an Autonomous REST JDBC Driver

Prerequisite:

1.  Request the Support team to provide the TIautorest Progress JAR.

Procedure:

1.  Log in as the system administrator (superuser).

2.  Select **View &gt; Repository**, right-click a folder's name, and select **Add Resource &gt; Data Source** from the context menu. Alternatively, you can select **Create &gt; Data Source** from the main menu on any page.

3.  From the **Type** drop-down, select **JDBC**. The page refreshes to show the fields necessary for a JDBC data source.

4.  The JDBC Driver drop-down lists the available JDBC drivers and the ones that are not installed. Select **Other**.

5.  In the **JDBC Driver (required)** field, enter `tibcosoftware.jdbc.autorest.AutoRESTDriver`.

6.  Click **Add Driver**. The **Select Driver** dialog appears.

7.  In the **Select Driver** dialog, click **Choose File** to locate the appropriate driver JAR file.

8.  Click **Upload** to install the driver.

9.  In the **URL** field, enter the connection string by specifying the location of the config file using the Config connection property. For example, `jdbc:tibcosoftware:autorest:config=C:\\example.rest`.

    To understand how to use an autonomous REST connector, see the [documentation](https://www.progress.com/tutorials/jdbc/query-any-rest-api-using-sql-via-jdbc-in-5-mins---getting-started-(part-1)).

10. Click **Test Connection** to check if all inputs are correct.

11. Click **Save** to save the data source.
