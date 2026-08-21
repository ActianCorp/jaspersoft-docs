---
title: Adding a CDP Driver to use Apache Hive Driver
description: 1. Log in as the system administrator (superuser).
---

# Adding a CDP Driver to use Apache Hive Driver

Procedure:

1.  Log in as the system administrator (superuser).

2.  Download the Hive driver from [Cloudera](https://www.cloudera.com/downloads/connectors/hive/jdbc/2-6-23.html).

    !!! note

        The location for accessing the driver is provided for convenience only, and this does not constitute an endorsement or representation that this drivers is fit for any particular purpose. You are solely responsible for the deployment and use of the driver in connection with the JasperReports Server product.

3.  Enable JDBC driver uploads, as described in [Enabling JDBC Driver Uploads](managing_jdbc_drivers.md).

4.  Select **View \> Repository**, right-click a folder's name, and select **Add Resource \> Data Source** from the context menu. Alternatively, you can select **Create \> Data Source** from the main menu on any page.

5.  From the **Type** drop-down, select **JDBC**. The page refreshes to show the fields necessary for a JDBC data source.

6.  The JDBC Driver drop-down lists the available JDBC drivers and the ones that are not installed. Select **Other**.

7.  In the **JDBC Driver (required)** field, enter `com.cloudera.hive.jdbc.HS2Driver`.

8.  Click **Add Driver**. The **Select Driver** dialog appears.

9.  In the **Select Driver** dialog, click **Choose File** to locate the appropriate driver JAR file.

10. Click **Upload** to install the driver.

11. In the **URL** field, enter `jdbc:hive2://localhost:10000/`.

12. Provide relevant information in the **User Name, Password** and **Time Zone** fields.

    !!! note

        **JDBC Driver** and **URL** are mandatory fields.

13. Click **Test Connection** to check if all inputs are correct.

14. Click **Save** to save the data source.
