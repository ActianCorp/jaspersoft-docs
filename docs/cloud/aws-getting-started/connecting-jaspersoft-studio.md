---
title: Connecting JSS Pro to Your Data
description: 1. Create a new DataAdapter (called Data Source in JSS).
---

# Connecting JSS Pro to Your Data

1.  Create a new DataAdapter (called Data Source in JSS).

<img src="assets/images/03000013.png" alt="03000013" />

New DataAdapter button

In Jaspersoft Studio, click the New Data Adapter icon to display the DataAdapter wizard.

<img src="assets/images/03000014.png" alt="03000014" />

DataAdapter wizard

1.  Name your DataAdapter and click **Next**.

<img src="assets/images/03000015.png" alt="03000015" />

Selecting a data source type

1.  Select the data source type. For Amazon RDS and Redshift, use **JDBC**. Then click **Next**.

<img src="assets/images/03000017.png" alt="03000017" />

Entering your database location

1.  Add the **JDBC Driver**. You may need to search the web for one that corresponds to your RDBMS or other technology on your EC2 instance.
2.  Enter the **JDBC Url**. This is the Endpoint URL from your Amazon EC2 dashboard (including the port) and database type.

<img src="assets/images/03000016.png" alt="03000016" />

Locating the Endpoint

1.  Click the **Driver Classpath** tab and select the local path of the driver.

<img src="assets/images/03000018.png" alt="03000018" />

Selecting the driver classpath

1.  Test the connection.

# Connecting JSS Pro to the JRS Repository

You'll need to connect to the JSS repository to manage and schedule reports

To define the Repository Explorer's connection

1.  In JSS, select **Window** \> **Show Views** \> **Other….**

<img src="assets/images/0300001A.png" alt="0300001A" />

**Window** \> **Show Views** \> **Other….** menu

1.  Select **Repository Explorer**.

<img src="assets/images/0300001B.png" alt="0300001B" />

Selecting the Repository Explorer

1.  Select the instance’s URL. It should start with `ec2`.

<img src="assets/images/0300001C.png" alt="0300001C" />

Selecting the instance URL

1.  Right-click the name of your instance to create a JRS repository connection.

<img src="assets/images/0300001D.png" alt="0300001D" />

Creating the JRS repository connection

1.  Fill in the instance’s url, but don’t add the port ID number. Make sure to include “/jasperserver-pro/” at the end of the path.

<img src="assets/images/0300001E.png" alt="0300001E" />

Filling in the instance URL

From here you should follow the Jaspersoft Studio documentation on how to create reports. There is also online training and tutorials available here:

<http://community.jaspersoft.com/wiki/jaspersoft-studio-tutorials-archive>
