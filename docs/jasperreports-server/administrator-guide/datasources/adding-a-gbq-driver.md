---
title: Adding a Google Big Query Driver
description: 1. Log in as the system administrator (superuser).
---

# Adding a Google Big Query Driver

Procedure:

1.  Log in as the system administrator (superuser).

2.  For the artifacts to download the Google Big Query driver, contact [Customer Support](https://www.jaspersoft.com/support).

3.  Enable JDBC driver uploads, as described in Enabling JDBC Driver Uploads.

4.  Select **View &gt; Repository**, right-click a folder's name, and select **Add Resource &gt; Data Source** from the context menu. Alternatively, you can select **Create &gt; Data Source** from the main menu on any page.

5.  From the **Type** drop-down, select **JDBC**. The page refreshes to show the fields necessary for a JDBC data source.

6.  The JDBC Driver drop-down lists the available JDBC drivers and the ones that are not installed. Select **Other**.

7.  In the **JDBC Driver (required)** field, enter `com.simba.googlebigquery.jdbc42.Driver`.

8.  Click **Add Driver**. The **Select Driver** dialog appears.

9.  In the **Select Driver** dialog, click **Choose File** to locate the appropriate driver JAR file.

10. Click **Upload** to install the driver.

11. In the **URL** field, enter `jdbc:bigquery://https://www.googleapis.com/bigquery/v2:443;ProjectId=\{project_id};OAuthType=0;OAuthServiceAcctEmail={service_account_mail_id};OAuthPvtKeyPath={path_to_service_account_file_in_repository};EnableSession=1`.

    !!! note

        Download and save the private key for the used Google Service Account and provide it as [OAuthPvtKeyPath](https://www.googleapis.com/bigquery/v2:443;ProjectId=jaspersoft-qa;OAuthType=0;OAuthServiceAcctEmail=js-qa-service-account@jaspersoft-qa.iam.gserviceaccount.com;OAuthPvtKeyPath=repo:/public/jaspersoft_qa_923f0db23c7a.json;EnableSession=1) value in the URL.

12. Provide relevant information in the **User Name, Password** and **Time Zone** fields.

    !!! note

        **JDBC Driver** and **URL** are mandatory fields.

13. Click **Test Connection** to check if all inputs are correct.

14. Click **Save** to save the data source.
