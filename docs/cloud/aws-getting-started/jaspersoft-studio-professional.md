---
title: Working With Jaspersoft Studio Professional
description: "Jaspersoft Studio enables you to create sophisticated, pixel-perfect reports on the desktop and upload those reports to JasperReports Server on AWS. Jaspersoft Studio allows you to create..."
---

# Working With Jaspersoft Studio Professional

Jaspersoft Studio enables you to create sophisticated, pixel-perfect reports on the desktop and upload those reports to JasperReports Server on AWS. Jaspersoft Studio allows you to create sophisticated layouts containing charts, images, subreports, crosstabs, and more.

## Downloading Jaspersoft Studio

Jaspersoft Studio is available as an Eclipse Rich Client Package (RCP), downloadable from the following location: <http://community.jaspersoft.com/project/jaspersoft-studio/releases>.

See the Jaspersoft Studio User Guide for instructions on how to install Jaspersoft Studio on your local machine and installing your license.

## Connecting Jaspersoft Studio to Your Data

1.  Create a new Data Adapter (called Data Source in Jaspersoft Studio).

    ![03000013](assets/images/03000013.png)

    New DataAdapter button

    In Jaspersoft Studio, click the New Data Adapter icon to display the DataAdapter wizard.

    ![03000014](assets/images/03000014.png)

    DataAdapter wizard

2.  Name your DataAdapter and click **Next**.

    ![03000015](assets/images/03000015.png)

    Selecting a data source type

3.  Select the data source type. For Amazon RDS and Redshift, use **JDBC**. Then click **Next**.

    ![03000017](assets/images/03000017.png)

    Entering your database location

4.  Add the **JDBC Driver**. You may need to search the web for one that corresponds to your RDBMS or other technology on your EC2 instance.

5.  Enter the **JDBC Url**. This is the Endpoint URL from your Amazon EC2 dashboard (including the port) and database type.

    ![03000016](assets/images/03000016.png)

    Locating the Endpoint

6.  Click the **Driver Classpath** tab and select the local path of the driver.

    ![03000018](assets/images/03000018.png)

    Selecting the driver classpath

7.  Test the connection.

## Connecting Jaspersoft Studio Pro to the JasperReports Server Repository

You'll need to connect to the Jaspersoft Studio repository to manage and schedule reports

To define the Repository Explorer's connection

1.  In Jaspersoft Studio, select **Window** \> **Show Views** \> **Other….**

    ![0300001A](assets/images/0300001A.png)

    **Window** \> **Show Views** \> **Other….** menu

2.  Select **Repository Explorer**.

    ![0300001B](assets/images/0300001B.png)

    Selecting the Repository Explorer

3.  Select the instance’s URL. It should start with `ec2`.

    ![0300001C](assets/images/0300001C.png)

    Selecting the instance URL

4.  Right-click the name of your instance to create a JasperReports Server repository connection.

    ![0300001D](assets/images/0300001D.png)

    Creating the JasperReports Server repository connection

5.  Fill in the instance’s url, but don’t add the port ID number. Make sure to include `/jasperserver-pro/` at the end of the path.

![0300001E](assets/images/0300001E.png)

Filling in the instance URL

From here you should follow the Jaspersoft Studio documentation on how to create reports. There is also online training and tutorials available here:

<http://community.jaspersoft.com/wiki/jaspersoft-studio-tutorials-archive>
