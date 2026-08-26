---
title: Configuring Other Database Connections
description: To define the jasperserver JDBC data source and expose it through JNDI
---

# Configuring Other Database Connections

## Defining a JNDI Name and Sample Data Sources for MySQL

To define the jasperserver JDBC data source and expose it through JNDI

1.  Click the name of the JDBC provider that you just created. For example, **MySQL JDBC Provider**.

2.  Click **Data sources** in the **Additional Properties** of the JDBC provider details panel.

3.  To create a new data source, click **New**. The **New Data Source Wizard** appears.

4.  Enter the data source name: `jasperserver`

5.  Enter the JNDI name: `jdbc/jasperserver`

6.  Click **Next**, choose **Select an existing JDBC provider**, then select **MySQL JDBC Provider** from the drop-down list.

7.  Click **Next** and accept the default helper class (com.ibm.websphere.rsadapter.GenericDataStoreHelper). Select the checkbox to use this data source in container managed persistence (CMP).

8.  Click **Next** and select the Setup security aliases:

    | Field Name                             | MySQL Value             |
    |----------------------------------------|-------------------------|
    | Component-managed authentication alias | `mysql_jasperdb`        |
    | Mapping configuration alias            | DefaultPrincipalMapping |
    | Container-managed authentication alias | `mysql_jasperdb`        |

9.  Click **Next**, review the summary information, and click **Finish**.

To set the connection pool size

1.  In the list of JDBC data sources, click the newly created **jasperserver** data source to edit it.
2.  Click **Additional Properties &gt; Connection Pool Properties**. You can see that **Maximum Connections** is set to 10 by default.
3.  Set **Maximum Connections** to 50. You may want to set it to a higher value if necessary.
4.  Click **Save**.

To define custom properties

1.  In the list of JDBC data sources, select the checkbox for the newly created **jasperserver** data source and click **Test Connection**.

    In the Messages area, a success or failure message appears. The failure message gives you information about which custom properties you need to define.

2.  Navigate to the **jasperserver** data sources **General Properties** page.

3.  In **Additional Properties** on the right side of the **General Properties** page, click **Custom properties**.

4.  Scroll down the list of properties and select **databaseName**. Set the value to `jasperserver`.

5.  Create a new property called **url**. Enter the following value and save the change:

    `jdbc:mysql://localhost/jasperserver?useUnicode=true&amp;characterEncoding=UTF-8&amp;tinyInt1isBit=false&amp;allowPublicKeyRetrieval=true`

6.  Click **Save directly to the master configuration**.

To define the jsSystemAnalytics JDBC data source and expose it through JNDI

1.  Click the name of the JDBC provider that you just created. For example, **MySQL JDBC Provider**.

2.  Click **Data sources** in the **Additional Properties** of the JDBC provider details panel.

3.  To create a new data source, click **New**. The **New Data Source Wizard** appears.

4.  Enter the data source name:` jsSystemAnalytics`

5.  Enter the JNDI name: `jdbc/jasperserverSystemAnalytics`

6.  Click **Next**, choose **Select an existing JDBC provider**, then select **MySQL JDBC Provider** from the drop-down list.

7.  Click **Next** and accept the default helper class (com.ibm.websphere.rsadapter.GenericDataStoreHelper). Select the checkbox to use this data source in container managed persistence (CMP).

8.  Click **Next** and select the Setup security aliases:

    | Field Name                             | MySQL Value             |
    |----------------------------------------|-------------------------|
    | Component-managed authentication alias | `mysql_jasperdb`        |
    | Mapping configuration alias            | DefaultPrincipalMapping |
    | Container-managed authentication alias | `mysql_jasperdb`        |

9.  Click **Next**, review the summary information, and click **Finish**.

To set the connection pool size

1.  In the list of JDBC data sources, click the newly created **jsSystemAnalytics** data source to edit it.
2.  Click **Additional Properties &gt; Connection Pool Properties**. You can see that **Maximum Connections** is set to 10 by default.
3.  Set **Maximum Connections** to 50. You may want to set it to a higher value if necessary.
4.  Click **Save**.

To define custom properties

1.  In the list of JDBC data sources, select the checkbox for the newly created **jsSystemAnalytics** data source and click **Test Connection**.

    In the Messages area, a success or failure message appears. The failure message gives you information about which custom properties you need to define.

2.  Navigate to the **jasperserver** data sources **General Properties** page.

3.  In **Additional Properties** on the right side of the **General Properties** page, click **Custom properties**.

4.  Scroll down the list of properties and select **databaseName**. Set the value to `jasperserver`.

5.  Create a new property called **url**. Enter the following value and save the change:

    `jdbc:mysql://localhost/jasperserver?useUnicode=true&amp;characterEncoding=UTF-8&amp;tinyInt1isBit=false&amp;allowPublicKeyRetrieval=true`

6.  Click **Save directly to the master configuration**.

To define the jsaudit JDBC data source and expose it through JNDI

1.  Click the name of the JDBC provider that you just created. For example, **MySQL JDBC Provider**.

2.  Click **Data sources** in the **Additional Properties** of the JDBC provider details panel.

3.  To create a new data source, click **New**. The **New Data Source Wizard** appears.

4.  Enter the data source name: `jsaudit`

5.  Enter the JNDI name: `jdbc/jasperserverAudit`

6.  Click **Next**, choose **Select an existing JDBC provider**, then select **MySQL JDBC Provider** from the drop-down list.

7.  Click **Next** and accept the default helper class (com.ibm.websphere.rsadapter.GenericDataStoreHelper). Select the checkbox to use this data source in container managed persistence (CMP).

8.  Click **Next** and select the Setup security aliases:

    | Field Name                             | MySQL Value             |
    |----------------------------------------|-------------------------|
    | Component-managed authentication alias | mysql_jasperdb          |
    | Mapping configuration alias            | DefaultPrincipalMapping |
    | Container-managed authentication alias | mysql_jasperdb          |

9.  Click **Next**, review the summary information, and click **Finish**.

To set the connection pool size

1.  In the list of JDBC data sources, click the newly created **jsaudit** data source to edit it.
2.  Click **Additional Properties &gt; Connection Pool Properties**. You can see that **Maximum Connections** is set to 10 by default.
3.  Set **Maximum Connections** to 50. You may want to set it to a higher value if necessary.
4.  Click **Save**.

To define custom properties

1.  In the list of JDBC data sources, select the checkbox for the newly created **jsaudit** data source and click **Test Connection**.

    In the Messages area, a success or failure message appears. The failure message gives you information about which custom properties you need to define.

2.  Navigate to the **jsaudit** data sources **General Properties** page.

3.  In **Additional Properties** on the right side of the **General Properties** page, click **Custom properties**.

4.  Scroll down the list of properties and select **databaseName**. Set the value to

-   For Compact installation: `jasperserver`

    -   For Split installation: `jsaudit`

        1.  Create a new property called **url**. Enter the following value and save the change:

    -   For Compact installation: `jdbc:mysql://localhost/jasperserver?useUnicode=true&amp;characterEncoding=UTF-8&amp;tinyInt1isBit=false&amp;allowPublicKeyRetrieval=true`

    -   For Split installation: `jdbc:mysql://localhost/jsaudit?useUnicode=true&amp;characterEncoding=UTF-8&amp;tinyInt1isBit=false&amp;allowPublicKeyRetrieval=true`

        1.  Click **Save directly to the master configuration**.

        To define the jsAuditAnalytics JDBC data source and expose it through JNDI

        1.  Click the name of the JDBC provider that you just created. For example, **MySQL JDBC Provider**.

        2.  Click **Data sources** in the **Additional Properties** of the JDBC provider details panel.

        3.  To create a new data source, click **New**. The **New Data Source Wizard** appears.

        4.  Enter the data source name:` jsAuditAnalytics`

        5.  Enter the JNDI name: `jdbc/jasperserverAuditAnalytics`

        6.  Click **Next**, choose **Select an existing JDBC provider**, then select **MySQL JDBC Provider** from the drop-down list.

        7.  Click **Next** and accept the default helper class (com.ibm.websphere.rsadapter.GenericDataStoreHelper). Select the checkbox to use this data source in container managed persistence (CMP).

        8.  Click **Next** and select the Setup security aliases:

            | Field Name                             | MySQL Value             |
            |----------------------------------------|-------------------------|
            | Component-managed authentication alias | `mysql_jasperdb`        |
            | Mapping configuration alias            | DefaultPrincipalMapping |
            | Container-managed authentication alias | `mysql_jasperdb`        |

        9.  Click `Next`, review the summary information, and click `Finish`.

        To set the connection pool size

        1.  In the list of JDBC data sources, click the newly created **jsAuditAnalytics** data source to edit it.
        2.  Click **Additional Properties &gt; Connection Pool Properties**. You can see that **Maximum Connections** is set to 10 by default.
        3.  Set **Maximum Connections** to 50. You may want to set it to a higher value if necessary.
        4.  Click **Save**.

        To define custom properties

        1.  In the list of JDBC data sources, select the checkbox for the newly created **jsAuditAnalytics** data source and click **Test Connection**.

            In the Messages area, a success or failure message appears. The failure message gives you information about which custom properties you need to define.

        2.  Navigate to the **jsaudit** data sources **General Properties** page.

        3.  In **Additional Properties** on the right side of the **General Properties** page, click **Custom properties**.

        4.  Scroll down the list of properties and select **databaseName**. Set the value to

    -   For Compact installation: `jasperserver`

    -   For Split installation: `jsaudit`

        1.  Create a new property called **url**. Enter the following value and save the change:

    -   For Compact installation: `jdbc:mysql://localhost/jasperserver?useUnicode=true&amp;characterEncoding=UTF-8&amp;tinyInt1isBit=false&amp;allowPublicKeyRetrieval=true`

    -   For Split installation: `jdbc:mysql://localhost/jsaudit?useUnicode=true&amp;characterEncoding=UTF-8&amp;tinyInt1isBit=false&amp;allowPublicKeyRetrieval=true`

1.  Click **Save directly to the master configuration**.

To create optional sugarcrm and foodmart data sources

1.  If you plan to run the sample reports, use the values in the following table to create the foodmart and sugarcrm JNDI data sources.

    <table>
    <thead>
    <tr>
    <th>Field Name</th>
    <th colspan="2">Value</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td><p>Data source name</p></td>
    <td><p><strong>foodmart</strong></p></td>
    <td><p><strong>sugarcrm</strong></p></td>
    </tr>
    <tr>
    <td><p>JNDI name</p></td>
    <td><p><strong>jdbc/foodmart</strong></p></td>
    <td><p><strong>jdbc/sugarcrm</strong></p></td>
    </tr>
    </tbody>
    </table>

2.  Click **Save directly to the master configuration**.

3.  Set the connection pool size as described in Set the connection pool size.

Next, deploy the WAR file in WebSphere as described in [Deploying the WAR File in WebSphere](websphere_install_procedure.md).

## Defining a JNDI Name and Sample Data Sources for DB2

To define the JSPRSRVR JDBC data source and expose it through JNDI

1.  Click the name of the JDBC provider you just created. For example, **DB2 Universal JDBC Provider**.

2.  Click Data sources under the **Additional Properties** of the JDBC provider details panel.

3.  To create a new data source, click **New**. The **New Data Source Wizard** appears.

4.  Enter the data source name: `JSPRSRVR`

5.  Enter the JNDI name: `jdbc/jasperserver`

6.  Click **Next**.

7.  For DB2 driver, choose **Select an existing JDBC provider**, then select **DB2 Universal JDBC Provider** from the drop-down list.

8.  Click **Next** and enter these values:

    | Field Name    | Value     |
    |---------------|-----------|
    | Driver type   | 4         |
    | Database name | JSPRSRVR  |
    | Server name   | localhost |
    | Port number   | 50000     |

9.  Select **Use this data source in CMP** and click **Next**.

10. On the Setup security aliases page, enter the following value for the Component-managed authentication alias:

    `db2admin_user`

11. Click **Next**, review the summary information, and click **Finish**.

To set the connection pool size

1.  In the list of JDBC data sources, click the newly created **JSPRSRVR** data source to edit it.
2.  Click **Additional Properties &gt; Connection Pool Properties**. You can see that **Maximum Connections** is set to 10 by default.
3.  Set **Maximum Connections** to 50. You may want to set it to a higher value if necessary.
4.  Click **Save**.

To define custom properties

1.  In the list of JDBC data sources, select the checkbox for the newly created **JSPRSRVR** data source, and click **Test Connection**.

2.  In the Messages area, a success or failure message appears. The failure message gives you information about which custom properties you need to define.

3.  Edit the following properties, adding any that are missing, then save the changes:

    | Property Name                | Value    |
    |------------------------------|----------|
    | currentSchema                | JSPRSRVR |
    | fullyMaterializeLobData      | true     |
    | fullyMaterializeInputStreams | true     |
    | progressiveStreaming         | 2        |
    | progressiveLocators          | 2        |

    Properties for DB2 JDBC Driver

4.  Go back to the list of JDBC data sources, select the checkbox for the **JSPRSRVR** data source, and click **Test Connection**.

To define the jsSystemAnalytics JDBC data source and expose it through JNDI

1.  Click the name of the JDBC provider you just created. For example, **DB2 Universal JDBC Provider**.

2.  Click Data sources under the **Additional Properties** of the JDBC provider details panel.

3.  To create a new data source, click **New**. The **New Data Source Wizard** appears.

4.  Enter the data source name: `jsSystemAnalytics`

5.  Enter the JNDI name: `jdbc/jasperserverSystemAnalytics`

6.  Click **Next**.

7.  For DB2 driver, choose **Select an existing JDBC provider**, then select **DB2 Universal JDBC Provider** from the drop-down list.

8.  Click **Next** and enter these values:

    | Field Name    | Value     |
    |---------------|-----------|
    | Driver type   | 4         |
    | Database name | JSPRSRVR  |
    | Server name   | localhost |
    | Port number   | 50000     |

9.  Select **Use this data source in CMP** and click **Next**.

10. On the Setup security aliases page, enter the following value for the Component-managed authentication alias:

    `db2admin_user`

11. Click **Next**, review the summary information, and click **Finish**.

To set the connection pool size

1.  In the list of JDBC data sources, click the newly created **jsSystemAnalytics** data source to edit it.
2.  Click **Additional Properties &gt; Connection Pool Properties**. You can see that **Maximum Connections** is set to 10 by default.
3.  Set **Maximum Connections** to 50. You may want to set it to a higher value if necessary.
4.  Click **Save**.

To define custom properties

1.  In the list of JDBC data sources, select the checkbox for the newly created **jsSystemAnalytics** data source, and click **Test Connection**.

2.  In the Messages area, a success or failure message appears. The failure message gives you information about which custom properties you need to define.

3.  Edit the following properties, adding any that are missing, then save the changes:

    | Property Name                | Value    |
    |------------------------------|----------|
    | currentSchema                | JSPRSRVR |
    | fullyMaterializeLobData      | true     |
    | fullyMaterializeInputStreams | true     |
    | progressiveStreaming         | 2        |
    | progressiveLocators          | 2        |

    Properties for DB2 JDBC Driver

4.  Go back to the list of JDBC data sources, select the checkbox for the **jsSystemAnalytics** data source, and click **Test Connection**.

To define the jsaudit JDBC data source and expose it through JNDI

1.  Click the name of the JDBC provider you just created. For example, **DB2 Universal JDBC Provider**.

2.  Click Data sources under the **Additional Properties** of the JDBC provider details panel.

3.  To create a new data source, click **New**. The **New Data Source Wizard** appears.

4.  Enter the data source name: `jsaudit`

5.  Enter the JNDI name: `jdbc/jasperserverAudit`

6.  Click **Next**.

7.  For DB2 driver, choose **Select an existing JDBC provider**, then select **DB2 Universal JDBC Provider** from the drop-down list.

8.  Click **Next** and enter these values:

    <table>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <thead>
    <tr>
    <th>Field Name</th>
    <th>Value</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td><p>Driver type</p></td>
    <td><p>4</p></td>
    </tr>
    <tr>
    <td><p>Database name</p></td>
    <td><p>For Compact installation: JSPRSRVR<br />
    For Split installation: JSAUDIT</p></td>
    </tr>
    <tr>
    <td><p>Server name</p></td>
    <td><p>localhost</p></td>
    </tr>
    <tr>
    <td><p>Port number</p></td>
    <td><p>50000</p></td>
    </tr>
    </tbody>
    </table>

9.  Select **Use this data source in CMP** and click **Next**.

10. On the Setup security aliases page, enter the following value for the Component-managed authentication alias:

    `db2admin_user`

11. Click **Next**, review the summary information, and click **Finish**.

To set the connection pool size

1.  In the list of JDBC data sources, click the newly created **jsaudit** data source to edit it.
2.  Click **Additional Properties &gt; Connection Pool Properties**. You can see that **Maximum Connections** is set to 10 by default.
3.  Set **Maximum Connections** to 50. You may want to set it to a higher value if necessary.
4.  Click **Save**.

To define custom properties

1.  In the list of JDBC data sources, select the checkbox for the newly created **jsaudit** data source, and click **Test Connection**.

2.  In the Messages area, a success or failure message appears. The failure message gives you information about which custom properties you need to define.

3.  Edit the following properties, adding any that are missing, then save the changes:

    <table>
    <caption><p>Properties for DB2 JDBC Driver</p></caption>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <thead>
    <tr>
    <th>Property Name</th>
    <th>Value</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td><p>currentSchema</p></td>
    <td><p>For Compact Installation: JSPRSRVR</p>
    <p>For Split Installation: JSAUDIT</p></td>
    </tr>
    <tr>
    <td><p>fullyMaterializeLobData</p></td>
    <td><p>true</p></td>
    </tr>
    <tr>
    <td><p>fullyMaterializeInputStreams</p></td>
    <td><p>true</p></td>
    </tr>
    <tr>
    <td><p>progressiveStreaming</p></td>
    <td><p>2</p></td>
    </tr>
    <tr>
    <td><p>progressiveLocators</p></td>
    <td><p>2</p></td>
    </tr>
    </tbody>
    </table>

4.  Go back to the list of JDBC data sources, select the checkbox for the **jsaudit** data source, and click **Test Connection**.

To define the jsAuditAnalytics JDBC data source and expose it through JNDI

1.  Click the name of the JDBC provider you just created. For example, **DB2 Universal JDBC Provider**.

2.  Click Data sources under the **Additional Properties** of the JDBC provider details panel.

3.  To create a new data source, click **New**. The **New Data Source Wizard** appears.

4.  Enter the data source name: `jsAuditAnalytics`

5.  Enter the JNDI name: `jdbc/jasperserverAuditAnalytics`

6.  Click **Next**.

7.  For DB2 driver, choose **Select an existing JDBC provider**, then select **DB2 Universal JDBC Provider** from the drop-down list.

8.  Click **Next** and enter these values:

    <table>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <thead>
    <tr>
    <th>Field Name</th>
    <th>Value</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td><p>Driver type</p></td>
    <td><p>4</p></td>
    </tr>
    <tr>
    <td><p>Database name</p></td>
    <td><p>For Compact installation: JSPRSRVR<br />
    For Split installation: JSAUDIT</p></td>
    </tr>
    <tr>
    <td><p>Server name</p></td>
    <td><p>localhost</p></td>
    </tr>
    <tr>
    <td><p>Port number</p></td>
    <td><p>50000</p></td>
    </tr>
    </tbody>
    </table>

9.  Select **Use this data source in CMP** and click **Next**.

10. On the Setup security aliases page, enter the following value for the Component-managed authentication alias:

    `db2admin_user`

11. Click **Next**, review the summary information, and click **Finish**.

To set the connection pool size

1.  In the list of JDBC data sources, click the newly created **jsAuditAnalytics** data source to edit it.
2.  Click **Additional Properties &gt; Connection Pool Properties**. You can see that **Maximum Connections** is set to 10 by default.
3.  Set **Maximum Connections** to 50. You may want to set it to a higher value if necessary.
4.  Click **Save**.

To define custom properties

1.  In the list of JDBC data sources, select the checkbox for the newly created **jsAuditAnalytics** data source, and click **Test Connection**.

2.  In the Messages area, a success or failure message appears. The failure message gives you information about which custom properties you need to define.

3.  Edit the following properties, adding any that are missing, then save the changes:

    <table>
    <caption><p>Properties for DB2 JDBC Driver</p></caption>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <thead>
    <tr>
    <th>Property Name</th>
    <th>Value</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td><p>currentSchema</p></td>
    <td><p>For Compact Installation: JSPRSRVR</p>
    <p>For Split Installation: JSAUDIT</p></td>
    </tr>
    <tr>
    <td><p>fullyMaterializeLobData</p></td>
    <td><p>true</p></td>
    </tr>
    <tr>
    <td><p>fullyMaterializeInputStreams</p></td>
    <td><p>true</p></td>
    </tr>
    <tr>
    <td><p>progressiveStreaming</p></td>
    <td><p>2</p></td>
    </tr>
    <tr>
    <td><p>progressiveLocators</p></td>
    <td><p>2</p></td>
    </tr>
    </tbody>
    </table>

4.  Go back to the list of JDBC data sources, select the checkbox for the **jsAuditAnalytics** data source, and click **Test Connection**.

To create optional sugarcrm and foodmart data sources

1.  If you plan to run the sample reports, use the following values to create the foodmart and sugarcrm JNDI data sources.

    <table>
    <caption><p>Field Values for Optional Data Sources for DB2 Drivers with WebSphere</p></caption>
    <thead>
    <tr>
    <th>Field Name</th>
    <th colspan="2"><p>Value</p></th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td><p>Data source name</p></td>
    <td><p>foodmart</p></td>
    <td><p>sugarcrm</p></td>
    </tr>
    <tr>
    <td><p>JNDI name</p></td>
    <td><p>jdbc/foodmart</p></td>
    <td><p>jdbc/sugarcrm</p></td>
    </tr>
    <tr>
    <td><p>Component-managed authentication alias</p></td>
    <td colspan="2"><p>&lt;node&gt;/db2admin_user</p></td>
    </tr>
    <tr>
    <td><p>Database name</p></td>
    <td><p>foodmart</p></td>
    <td><p>sugarcrm</p></td>
    </tr>
    <tr>
    <td><p>Driver type</p></td>
    <td colspan="2"><p>4</p></td>
    </tr>
    <tr>
    <td><p>Server name</p></td>
    <td colspan="2"><p>localhost</p></td>
    </tr>
    <tr>
    <td><p>Port number</p></td>
    <td colspan="2"><p>50000</p></td>
    </tr>
    <tr>
    <td><p>Use this data source in CMP</p></td>
    <td colspan="2"><p>selected</p></td>
    </tr>
    </tbody>
    </table>

    <table>
    <caption><p>Custom Properties for DB2 Driver with WebSphere</p></caption>
    <thead>
    <tr>
    <th>Property Name</th>
    <th colspan="2"><p>Value</p></th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td><p>currentSchema</p></td>
    <td><p>FOODMART</p></td>
    <td><p>SUGARCRM</p></td>
    </tr>
    <tr>
    <td><p>resultSetHoldability</p></td>
    <td colspan="2"><p>1</p></td>
    </tr>
    </tbody>
    </table>

2.  Click **Save directly to the master configuration**.

3.  Set the connection pool size as described in Set the connection pool size.

Next, deploy the WAR file in WebSphere as described in [Deploying the WAR File in WebSphere](websphere_install_procedure.md).

## Defining a JNDI Name and Sample Data Sources for Oracle

To define the jasperserver JDBC data source and expose it through JNDI

1.  Click the name of the JDBC provider you just created. For example, **Oracle JDBC Driver**.

2.  Click Data sources in the **Additional Properties** of the JDBC provider details panel.

3.  To create a new data source, click **New**. The **New Data Source Wizard** appears.

4.  Enter the data source name: `jasperserver`

5.  Enter the JNDI name: `jdbc/jasperserver`

6.  Click **Next**.

7.  For Oracle driver, choose **Select an existing JDBC provider**, then select **Oracle JDBC Driver** from the drop-down list.

8.  Click **Next** and enter the following values:

    | Field Name                   | Value                                   |
    |------------------------------|-----------------------------------------|
    | URL                          | `jdbc:oracle:thin:@localhost:1521:orcl` |
    | Data store helper class name | Oracle11g data store helper             |
    | Use this data source in CMP  | selected                                |

9.  Click **Next** and in **Setup security alias**, set the **Component-managed authentication alias** to the following value:

    `jasperserver_user`

10. Click **Next**, review the summary information, and click **Finish**.

To set the connection pool size

1.  In the list of JDBC data sources, click the newly created **jasperserver** data source to edit it.
2.  Click **Additional Properties &gt; Connection Pool Properties**. You can see that **Maximum Connections** is set to 10 by default.
3.  Set **Maximum Connections** to 50. You may want to set it to a higher value if necessary.
4.  Click **Save**.

To define custom properties

1.  In the list of JDBC data sources, select the checkbox for the newly created **jasperserver** data source and click **Test Connection**.

    In the **Messages** area, a success or failure message appears. The failure message gives you information about which custom properties you need to define.

2.  Navigate to the jasperserver data sources **General Properties** page.

3.  In **Additional Properties** on the right side, click **Custom properties**.

4.  Go back to the list of JDBC data sources, select the checkbox for the **jasperserver** data source, and click **Test Connection**.

To define the jsSystemAnalytics JDBC data source and expose it through JNDI

1.  Click the name of the JDBC provider you just created. For example, **Oracle JDBC Driver**.

2.  Click Data sources in the Additional Properties of the JDBC provider details panel.

3.  To create a new data source, click **New**. The **New Data Source Wizard** appears.

4.  Enter the data source name: `jsSystemAnalytics`

5.  Enter the JNDI name: `jdbc/jasperserverSystemAnalytics`

6.  Click **Next**.

7.  For Oracle driver, choose **Select an existing JDBC provider**, then select **Oracle JDBC Driver** from the drop-down list.

8.  Click **Next** and enter the following values:

    | Field Name                   | Value                                     |
    |------------------------------|-------------------------------------------|
    | URL                          | **jdbc:oracle:thin:@localhost:1521:orcl** |
    | Data store helper class name | Oracle11g data store helper               |
    | Use this data source in CMP  | selected                                  |

9.  Click **Next** and in **Setup security alias**, set the **Component-managed authentication alias** to the following value:

    `jasperserver_user`

10. Click **Next**, review the summary information and click **Finish**.

To set the connection pool size

1.  In the list of JDBC data sources, click the newly created **jsSystemAnalytics** data source to edit it.
2.  Click **Additional Properties &gt; Connection Pool Properties**. You can see that **Maximum Connections** is set to 10 by default.
3.  Set **Maximum Connections** to 50. You may want to set it to a higher value if necessary.
4.  Click **Save**.

To define custom properties

1.  In the list of JDBC data sources, select the checkbox for the newly created **jsSystemAnalytics** data source and click **Test Connection**.

    In the **Messages** area, a success or failure message appears. The failure message gives you information about which custom properties you need to define.

2.  Navigate to the jasperserver data sources **General Properties** page.

3.  In **Additional Properties** on the right side, click **Custom properties**.

4.  Go back to the list of JDBC data sources, select the checkbox for the **jsSystemAnalytics** data source, and click **Test Connection**.

To define the jsaudit JDBC data source and expose it through JNDI

1.  Click the name of the JDBC provider you just created. For example, **Oracle JDBC Driver**.

2.  Click Data sources in the **Additional Properties** of the JDBC provider details panel.

3.  To create a new data source, click **New**. The **New Data Source Wizard** appears.

4.  Enter the data source name: `jsaudit`

5.  Enter the JNDI name: `jdbc/jasperserverAudit`

6.  Click **Next**.

7.  For Oracle driver, choose **Select an existing JDBC provider**, then select **Oracle JDBC Driver** from the drop-down list.

8.  Click **Next** and enter the following values:

    | Field Name                   | Value                                   |
    |------------------------------|-----------------------------------------|
    | URL                          | `jdbc:oracle:thin:@localhost:1521:orcl` |
    | Data store helper class name | Oracle11g data store helper             |
    | Use this data source in CMP  | selected                                |

9.  Click **Next** and in **Setup security alias**, set the **Component-managed authentication alias** to the following value:

    `jasperserver_user`

10. Click **Next**, review the summary information and click **Finish**.

To set the connection pool size

1.  In the list of JDBC data sources, click the newly created **jsaudit** data source to edit it.
2.  Click **Additional Properties &gt; Connection Pool Properties**. You can see that **Maximum Connections** is set to 10 by default.
3.  Set **Maximum Connections** to 50. You may want to set it to a higher value if necessary.
4.  Click **Save**.

To define custom properties

1.  In the list of JDBC data sources, select the checkbox for the newly created **jsaudit** data source and click **Test Connection**.

    In the **Messages** area, a success or failure message appears. The failure message gives you information about which custom properties you need to define.

2.  Navigate to the **jsaudit** data sources **General Properties** page.

3.  In **Additional Properties** on the right side, click **Custom properties**.

4.  Go back to the list of JDBC data sources, select the checkbox for the **jsaudit** data source, and click **Test Connection**.

To define the jsAuditAnalytics JDBC data source and expose it through JNDI

1.  Click the name of the JDBC provider you just created. For example, **Oracle JDBC Driver**.

2.  Click Data sources in the **Additional Properties** of the JDBC provider details panel.

3.  To create a new data source, click **New**. The **New Data Source Wizard** appears.

4.  Enter the data source name: `jsAuditAnalytics`

5.  Enter the JNDI name: `jdbc/jasperserverAuditAnalytics`

6.  Click **Next**.

7.  For Oracle driver, choose **Select an existing JDBC provider**, then select **Oracle JDBC Driver** from the drop-down list.

8.  Click **Next** and enter the following values:

    | Field Name                   | Value                                   |
    |------------------------------|-----------------------------------------|
    | URL                          | `jdbc:oracle:thin:@localhost:1521:orcl` |
    | Data store helper class name | Oracle11g data store helper             |
    | Use this data source in CMP  | selected                                |

9.  Click **Next** and in **Setup security alias**, set the **Component-managed authentication alias** to the following value:

    `jasperserver_user`

10. Click **Next**, review the summary information and click **Finish**.

To set the connection pool size

1.  In the list of JDBC data sources, click the newly created **jsAuditAnalytics** data source to edit it.
2.  Click **Additional Properties &gt; Connection Pool Properties**. You can see that **Maximum Connections** is set to 10 by default.
3.  Set **Maximum Connections** to 50. You may want to set it to a higher value if necessary.
4.  Click **Save**.

To define custom properties

1.  In the list of JDBC data sources, select the checkbox for the newly created **jsAuditAnalytics** data source and click **Test Connection**.

    In the **Messages** area, a success or failure message appears. The failure message gives you information about which custom properties you need to define.

2.  Navigate to the **jsaudit** data sources **General Properties** page.

3.  In **Additional Properties** on the right side, click **Custom properties**.

4.  Go back to the list of JDBC data sources, select the checkbox for the **jsAuditAnalytics** data source, and click **Test Connection**.

To create optional sugarcrm and foodmart data sources

1.  If you plan to run the sample reports, use the following values to create the foodmart and sugarcrm JNDI data sources:

    <table>
    <thead>
    <tr>
    <th>Field Name</th>
    <th colspan="2"><p>Value</p></th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td><p>Data source name</p></td>
    <td><p>foodmart</p></td>
    <td><p>sugarcrm</p></td>
    </tr>
    <tr>
    <td><p>JNDI name</p></td>
    <td><p>jdbc/foodmart</p></td>
    <td><p>jdbc/sugarcrm</p></td>
    </tr>
    <tr>
    <td><p>Component-managed authentication alias</p></td>
    <td><p>&lt;node&gt;/foodmart_user</p></td>
    <td><p>&lt;node&gt;/sugarcrm_user</p></td>
    </tr>
    </tbody>
    </table>

    <table>
    <thead>
    <tr>
    <th>Property Name</th>
    <th colspan="2"><p>Value</p></th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>portNumber</td>
    <td colspan="2"><p>1521</p></td>
    </tr>
    <tr>
    <td>serverName</td>
    <td colspan="2"><p>localhost</p></td>
    </tr>
    </tbody>
    </table>

2.  Click **Save directly to the master configuration**.

3.  Set the connection pool size as described in Set the connection pool size.

Next, deploy the WAR file in WebSphere as described in [Deploying the WAR File in WebSphere](websphere_install_procedure.md).

## Defining a JNDI Name and Sample Data Sources for SQL Server

To define the jasperserver JDBC provider

1.  Click the name of the JDBC provider you just created. For example, **Microsoft SQL Server JDBC Driver**.

2.  Click Data sources under the **Additional Properties** of the JDBC provider details panel.

3.  To create a new data source, click **New**. The **New Data Source Wizard** appears.

4.  Enter the data source name: `jasperserver`

5.  Enter the JNDI name: `jdbc/jasperserver`

6.  Click **Next**.

7.  For SQL Server driver, choose **Select an existing JDBC provider**, then select **Microsoft SQL Server JDBC Driver** from the drop-down list.

8.  Click **Next** and in Setup security alias, set the Component-managed authentication alias to the following value:

    `jasperserver_user`

9.  Click **Next**, review the summary information and click **Finish**.

To set the connection pool size

1.  In the list of JDBC data sources, click the newly created **jasperserver** data source to edit it.
2.  Click **Additional Properties &gt; Connection Pool Properties**. You can see that **Maximum Connections** is set to 10 by default.
3.  Set **Maximum Connections** to 50. You may want to set it to a higher value if necessary.
4.  Click **Save**.

To define custom properties

1.  In the list of JDBC data sources, select the checkbox for the newly created **jasperserver** data source, and click **Test Connection**.

    In the Messages area, a success or failure message appears. The failure message gives you information about which custom properties you need to define.

2.  Navigate to the **jasperserver** data sources **General Properties** page.

To define the jsSystemAnalytics JDBC data source and expose it through JNDI

1.  Click the name of the JDBC provider you just created. For example, **Microsoft SQL Server JDBC Driver**.

2.  Click Data sources under the Additional Properties of the JDBC provider details panel.

3.  To create a new data source, click **New**. The **New Data Source Wizard** appears.

4.  Enter the data source name: `jsSystemAnalytics`

5.  Enter the JNDI name: `jdbc/jasperserverSystemAnalytics`

6.  Click **Next**.

7.  For SQL Server driver, choose **Select an existing JDBC provider**, then select **Microsoft SQL Server JDBC Driver** from the drop-down list.

8.  Click **Next** and in Setup security alias, set the Component-managed authentication alias to the following value:

    `jasperserver_user`

9.  Click **Next**, review the summary information and click **Finish**.

To set the connection pool size

1.  In the list of JDBC data sources, click the newly created **jsSystemAnalytics** data source to edit it.
2.  Click **Additional Properties &gt; Connection Pool Properties**. You can see that **Maximum Connections** is set to 10 by default.
3.  Set **Maximum Connections** to 50. You may want to set it to a higher value if necessary.
4.  Click **Save**.

To define custom properties

1.  In the list of JDBC data sources, select the checkbox for the newly created **jsSystemAnalytics** data source, and click **Test Connection**.

    In the Messages area, a success or failure message appears. The failure message gives you information about which custom properties you need to define.

2.  Navigate to the jasperserver data sources **General Properties** page.

To define the jsaudit JDBC provider

1.  Click the name of the JDBC provider you just created. For example, **Microsoft SQL Server JDBC Driver**.

2.  Click Data sources under the **Additional Properties** of the JDBC provider details panel.

3.  To create a new data source, click **New**. The **New Data Source Wizard** appears.

4.  Enter the data source name: `jsaudit`

5.  Enter the JNDI name: `jdbc/jasperserverAudit`

6.  Click **Next**.

7.  For SQL Server driver, choose **Select an existing JDBC provider**, then select **Microsoft SQL Server JDBC Driver** from the drop-down list.

8.  Click **Next** and in Setup security alias, set the Component-managed authentication alias to the following value:

    `jasperserver_user`

9.  Click **Next**, review the summary information and click **Finish**.

To set the connection pool size

1.  In the list of JDBC data sources, click the newly created **jsaudit** data source to edit it.
2.  Click **Additional Properties &gt; Connection Pool Properties**. You can see that **Maximum Connections** is set to 10 by default.
3.  Set **Maximum Connections** to 50. You may want to set it to a higher value if necessary.
4.  Click **Save**.

To define custom properties

1.  In the list of JDBC data sources, select the checkbox for the newly created **jsaudit** data source, and click **Test Connection**.

    In the Messages area, a success or failure message appears. The failure message gives you information about which custom properties you need to define.

2.  Navigate to the **jsaudit** data sources **General Properties** page.

To define the jsAuditAnalytics JDBC data source and expose it through JNDI

1.  Click the name of the JDBC provider you just created. For example, **Microsoft SQL Server JDBC Driver**.

2.  Click Data sources under the **Additional Properties** of the JDBC provider details panel.

3.  To create a new data source, click **New**. The **New Data Source Wizard** appears.

4.  Enter the data source name: `jsAuditAnalytics`

5.  Enter the JNDI name: `jdbc/jasperserverAuditAnalytics`

6.  Click **Next**.

7.  For SQL Server driver, choose **Select an existing JDBC provider**, then select **Microsoft SQL Server JDBC Driver** from the drop-down list.

8.  Click **Next** and in Setup security alias, set the Component-managed authentication alias to the following value:

    `jasperserver_user`

9.  Click **Next**, review the summary information, and click **Finish**.

To set the connection pool size

1.  In the list of JDBC data sources, click the newly created **jsAuditAnalytics** data source to edit it.
2.  Click **Additional Properties &gt; Connection Pool Properties**. You can see that **Maximum Connections** is set to 10 by default.
3.  Set **Maximum Connections** to 50. You may want to set it to a higher value if necessary.
4.  Click **Save**.

To define custom properties

1.  In the list of JDBC data sources, select the checkbox for the newly created **jsAuditAnalytics** data source, and click **Test Connection**.

    In the Messages area, a success or failure message appears. The failure message gives you information about which custom properties you need to define.

2.  Navigate to the **jsaudit** data sources **General Properties** page.

To create optional sugarcrm and foodmart data sources

If you plan to run the sample reports, use the following values to create the foodmart and sugarcrm JNDI data sources:

1.  In the list of JDBC data sources, click the link for the newly created **jasperserver** data source.
2.  Click **Save directly to the master configuration**.
3.  Set the connection pool size as described in Set the connection pool size.

Next, deploy the WAR file in WebSphere as described in [Deploying the WAR File in WebSphere](websphere_install_procedure.md).
