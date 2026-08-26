---
title: Adding a Snowflake Driver
description: 1. Create a Snowflake account from snowflakecomputing.com for the preferred ROLE.
---

# Adding a Snowflake Driver

Prerequisites:

1.  Create a Snowflake account from [snowflakecomputing.com](http://snowflakecomputing.com/) for the preferred ROLE.

2.  Activate your account from the dedicated login **URL** received from Snowflake.

3.  Generate the **Username** and **Password**.

Procedure:

1.  Log in as the system administrator (superuser).

2.  Download the Snowflake driver from [here](https://spark.apache.org/downloads.html).

    !!! note

        The location for accessing the driver is provided for convenience only, and this does not constitute an endorsement or representation that this drivers is fit for any particular purpose. You are solely responsible for the deployment and use of the driver in connection with the JasperReports Server product.

3.  Enable JDBC driver uploads, as described in [Enabling JDBC Driver Uploads](managing_jdbc_drivers.md).

4.  Select **View &gt; Repository**, right-click a folder's name, and select **Add Resource &gt; Data Source** from the context menu. Alternatively, you can select **Create &gt; Data Source** from the main menu on any page.

5.  From the **Type** drop-down, select **JDBC**. The page refreshes to show the fields necessary for a JDBC data source.

6.  The JDBC Driver drop-down lists the available JDBC drivers and the ones that are not installed. Select **Snowflake(net.snowflake.client.jdbc.SnowflakeDriver)**.

7.  In the **HOST** field, enter the host details from the dedicated Login URL received from Snowflake. The format of the HOST is `xxxxxxx-xxxxxxxx.snowflakecomputing.com`.

8.  Provide relevant information in the **Role, Virtual Warehouse** and **Database** fields.

9.  The **URL** field is auto populated.

10. Provide relevant information in the **User Name** and **Password** fields.

11. Click **Test Connection** to check if all inputs are correct.

12. Click **Save** to save the data source.
