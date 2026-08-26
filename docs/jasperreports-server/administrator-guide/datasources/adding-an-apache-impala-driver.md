---
title: Adding an Apache Impala Driver
description: 1. Log in as the system administrator (superuser).
---

# Adding an Apache Impala Driver

Procedure:

1.  Log in as the system administrator (superuser).

2.  Download the Apache Impala driver from [here](https://www.cloudera.com/downloads/connectors/impala/jdbc/2-6-33.html).

    !!! note

        The location for accessing the driver is provided for convenience only, and this does not constitute an endorsement or representation that this drivers is fit for any particular purpose. You are solely responsible for the deployment and use of the driver in connection with the JasperReports Server product.

3.  Enable JDBC driver uploads, as described in [Enabling JDBC Driver Uploads](managing_jdbc_drivers.md).

4.  Select **View &gt; Repository**, right-click a folder's name, and select **Add Resource &gt; Data Source** from the context menu. Alternatively, you can select **Create &gt; Data Source** from the main menu on any page.

5.  From the **Type** drop-down, select **JDBC**. The page refreshes to show the fields necessary for a JDBC data source.

6.  The JDBC Driver drop-down lists the available JDBC drivers and the ones that are not installed. Select **Other**.

7.  In the **JDBC Driver (required)** field, enter `com.cloudera.impala.jdbc.Driver`.

    !!! note

        Before creating an Azure datasource, create the resource group, server and database on Azure portal. These parameters are used when the URL is formed.

8.  Click **Add Driver**. The **Select Driver** dialog appears.

9.  In the **Select Driver** dialog, click **Choose File** to locate the appropriate driver JAR file.

10. Click **Upload** to install the driver.

11. In the **URL** field, enter `jdbc:impala://localhost:21050/default`.

12. Provide relevant information in the **User Name, Password** and **Time Zone** fields.

    !!! note

        **JDBC Driver** and **URL** are mandatory fields.

13. Click **Test Connection** to check if all inputs are correct.

14. Click **Save** to save the data source.
