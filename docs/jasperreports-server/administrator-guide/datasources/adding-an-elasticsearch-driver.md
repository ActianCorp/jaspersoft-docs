---
title: Adding an Elasticsearch Driver
description: 1. Log in as the system administrator (superuser).
---

# Adding an Elasticsearch Driver

Procedure:

1.  Log in as the system administrator (superuser).

2.  Download the Elasticsearch driver from [here](https://mvnrepository.com/artifact/org.elasticsearch.plugin/x-pack-sql-jdbc).

    !!! note

        The location for accessing the driver is provided for convenience only, and this does not constitute an endorsement or representation that this drivers is fit for any particular purpose. You are solely responsible for the deployment and use of the driver in connection with the JasperReports Server product.

3.  Enable JDBC driver uploads, as described in [Enabling JDBC Driver Uploads](managing_jdbc_drivers.md).

4.  Select **View \> Repository**, right-click a folder's name, and select **Add Resource \> Data Source** from the context menu. Alternatively, you can select **Create \> Data Source** from the main menu on any page.

5.  From the **Type** drop-down, select **JDBC**. The page refreshes to show the fields necessary for a JDBC data source.

6.  The JDBC Driver drop-down lists the available JDBC drivers and the ones that are not installed. Select **Other**.

7.  In the **JDBC Driver (required)** field, enter `org.elasticsearch.xpack.sql.jdbc.EsDriver`.

8.  Click **Add Driver**. The **Select Driver** dialog appears.

9.  In the **Select Driver** dialog, click **Choose File** to locate the appropriate driver JAR file.

10. Click **Upload** to install the driver.

11. In the **URL** field, enter `jdbc:es://dbhost:9200/?ssl=true&ssl.keystore.location=/opt/home/jasperserver/truststore_jdbc.jks&ssl.keystore.pass=elasticsearch&ssl.truststore.location=/opt/home/jasperserver/truststore_jdbc.jks&ssl.truststore.pass=elasticsearch`.

12. Provide relevant information in the **User Name, Password** and **Time Zone** fields.

    !!! note

        **JDBC Driver** and **URL** are mandatory fields.

13. Click **Test Connection** to check if all inputs are correct.

14. Click **Save** to save the data source.

## Connect to Elasticsearch With Security Enabled JDBC URL

To connect to ElasticSearch with security enabled JDBC URL, **ssl** must be set to **true** (**ssl=true**) and the related certificates, and the key must be provided. For details, see [SQL JDBC](https://www.elastic.co/guide/en/elasticsearch/reference/current/sql-jdbc.html).

To get and repackage the files, search for xpack.security.http.ssl: section in the `elasticsearch.yml`.

To get the truststore_jdbc.jks file on Linux:

1.  On terminal, run the `` `openssl pkcs12 -export -out bundle_jdbc.p12 -in elastic.crt -inkey elastic.key` `` command.
2.  Select a secure password, when prompted.
3.  On terminal, run the `` `keytool -keystore truststore_jdbc.jks -import -file CA.crt -alias cacert` `` command.
4.  Select a secure password, when prompted.
5.  Type `'yes'`.
6.  On terminal, run the `` `keytool -destkeystore truststore_jdbc.jks -importkeystore -srckeystore bundle_jdbc.p12 -srcstoretype PKCS12` `` command.
7.  Enter the password to get the `truststore_jdbc.jks` file.
8.  Copy the `truststore_jdbc.jks` file to `/opt/home/jasperserver` on JasperReports Server.
