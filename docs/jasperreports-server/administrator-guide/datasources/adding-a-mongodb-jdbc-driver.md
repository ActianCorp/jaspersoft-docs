---
title: Adding a MongoDB JDBC Driver
description: "1. Request the Support team to provide the TImongodb Progress JAR and place it in the <tomcat-home>/webapp/jasperserver-pro/WEB-INF/lib/ folder."
---

# Adding a MongoDB JDBC Driver

Prerequisites:

1.  Request the Support team to provide the TImongodb Progress JAR and place it in the `<tomcat-home>/webapp/jasperserver-pro/WEB-INF/lib/` folder.

2.  Restart the Tomcat server.

Procedure:

1.  Log in as the system administrator (superuser).

2.  Select **View &gt; Repository**, right-click a folder's name, and select **Add Resource &gt; Data Source** from the context menu. Alternatively, you can select **Create &gt; Data Source** from the main menu on any page.

3.  From the **Type** drop-down, select **MongoDB JDBC**.

4.  Provide the relevant information in the fields, along with any optional information.

5.  Specify the **Connection Options**.

    For example, if you are using MongoDB and you want to enable SSL, enter, `EncryptionMethod=SSL;ValidateServerCertificate=false`

    To enable both SSL encryption and self-signed CA, enter the **TrustStore** and **KeyStore** paths and the **KeyStore** password. For example, `EncryptionMethod=SSL;TrustStore=<path>;KeyStore=<path>;KeyStorePassword=<password>;`

    The **Auto Generate Schema Definition** check box is checked by default. With this option selected, when you first connect to a MongoDB server, the driver automatically creates a normalized schema of the data and generates a SchemaDefinition for housing and sharing the normalized schema.

6.  To specify a schema you have created, uncheck this box and:

    1.  Use the **File Source** drop-down to select the schema file location, **Repository** or **Server File System**. For steps to create a schema using the schema tool, see Creating a Schema with the Schema Tool.

    2.  If your file is in the repository, click **Browse** and locate it in the repository. If your file is in the server file system, provide the path in the **Server File Location** field. For steps to upload a schema to the repository, see Uploading a Schema to the Repository.

7.  Click **Test Connection** to check if all inputs are correct.

8.  Click **Save** to save the data source.

## Creating a Schema with the Schema Tool

To create a schema with the schema tool:

1.  Go to `<js-install>/buildomatic/tools` and double click the `schematool.jar` file.

2.  Follow the instructions in the schema tool documentation found [here](https://documentation.progress.com/output/DataDirect/jdbcmongohelp/index.html#page/mongohelp/startingthe-schema-tool.html).

## Uploading a Schema to the Repository

To upload a schema to the repository:

1.  Click **View &gt; Repository** and expand the folder tree.

2.  Right-click a folder and from the context menu, select **Add Resource &gt; File &gt; MongoDB JDBC Schema**.

3.  Use **Upload File From Your Local Computer** page to locate and upload your schema file.
