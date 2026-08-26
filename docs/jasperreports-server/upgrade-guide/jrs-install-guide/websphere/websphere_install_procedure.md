---
title: Procedure for Installing and Deploying the WAR File in WebSphere
description: Perform the procedures in this section to install and deploy the JasperReports Server WAR file in WebSphere.
---

# Procedure for Installing and Deploying the WAR File in WebSphere

Perform the procedures in this section to install and deploy the JasperReports Server WAR file in WebSphere.

## Installing WebSphere and a Database

To install WebSphere and a database

1.  Make sure you are using a supported version of WebSphere. See the TIBCO JasperReports Server Supported Platform Datasheet for more information.
2.  Check that the WebSphere installation created a JAVA_HOME system environment variable. The variable needs to be set to the JAVA directory in the WebSphere installation.
3.  Install the database (PostgreSQL, MySQL, Oracle, SQL Server, or DB2).

!!! note

    The target database can be on a remote server. WebSphere should reside on the local machine.

## Preparing Server Files

To prepare JasperReports Server files

1.  Unpack

    `js-jrs``_10.1.0`

    \_bin.zip to a top-level directory. Unpacking the ZIP file creates the directory

    `js-jrs_``pro`` _10.1.0_bin.zip`

    .

2.  (Required) Manually create and load the JasperReports Server database.

3.  (Optional) Manually create and load the sample databases. See [Manually Creating the JasperReports Server Database](../../../installation-guide/manual-db/manually_creating_the_jasperreports_.md) for instructions.

4.  (Required) Manually import the default users and organization.

    1.  Copy the `<dbType>_master.properties` file for your database from `sample_conf` and paste it to `buildomatic`:

        -   `cd <js-install>/buildomatic`
        -   Copy from: `<js-install>/buildomatic/sample_conf`
        -   Paste to: `<js-install>/buildomatic`<br>
            For example, copy `sample_conf/postgresql_master.properties` to `buildomatic`.

    2.  Rename the file that you copied to `default_master.properties`.

    3.  Edit the `default_master.properties` file:

        -   Set `appServerType` to `skipAppServerCheck`.
        -   Change `dbUsername`, `dbPassword`, and `dbHost` to the appropriate settings for your database.
        -   If you are using a port other than the default for your database, or if you have installed the database on a remote machine, change the `dbPort` field under Custom Properties to the appropriate settings.

        For the Split installation, configure the additional settings in the `default_master.properties` file as described in [Additional Buildomatic Configuration for Split Installation Upgrade](../introduction/installation_types.md).

        For the JNDI restricted access installation, configure the additional settings in the `default_master.properties` file as described in [Installation Types](../introduction/installation_types.md).

        Each `sample_conf/<dbType>_master.properties` file contains appropriate sample values.

    4.  Start your database server.

    5.  Open a Command Prompt as Administrator and run these commands:

        <table>
        <caption><p>Buildomatic Targets to Execute</p></caption>
        <colgroup>
        <col style="width: 50%" />
        <col style="width: 50%" />
        </colgroup>
        <thead>
        <tr>
        <th><p>Commands</p></th>
        <th><p>Description</p></th>
        </tr>
        </thead>
        <tbody>
        <tr>
        <td><p><code>cd &lt;js-install&gt;/buildomatic</code></p></td>
        <td><p>Go to the buildomatic directory.</p></td>
        </tr>
        <tr>
        <td><code>js-ant create-js-db</code></td>
        <td>Create the jasperserver repository database.</td>
        </tr>
        <tr>
        <td><p><code>js-ant init-js-db-pro</code></p>
        <p><code>js-ant import-minimal-pro</code></p></td>
        <td><p>Initializes database, loads core application data.</p></td>
        </tr>
        <tr>
        <td><p><code>js-ant create-sugarcrm-db</code></p>
        <code>js-ant create-foodmart-db</code></td>
        <td>(Optional) Creates sample databases.</td>
        </tr>
        <tr>
        <td><p><code>js-ant load-sugarcrm-db</code></p>
        <code>js-ant load-foodmart-db</code></td>
        <td>(Optional) Loads sample data into the sample databases.</td>
        </tr>
        <tr>
        <td><p><code>js-ant import-sample-data-pro</code></p></td>
        <td><p>(Optional) Loads the demos that use the sample data.</p></td>
        </tr>
        <tr>
        <td><code>js-ant create-audit-db</code></td>
        <td><p>(Optional) Creates the audit database. Required only for the Split installation.</p></td>
        </tr>
        <tr>
        <td><code>js-ant init-audit-db-pro</code></td>
        <td>(Optional) Initializes the audit database. Required only for the Split installation.</td>
        </tr>
        </tbody>
        </table>

5.  Set up your license file. For more information, refer to [Setting Up the JasperReports Server License](../../../installation-guide/additional/setting_up_the_jasperreports_server_.md).

!!! note

    Installing JasperReports Server automatically generates encryption keys that reside on the file system. These keys are stored in a dedicated Jaspersoft keystore. Make sure that this keystore is properly secured and backed up, as described in the JasperReports Server Security Guide.

## Configuring CSRFGuard, Hibernate, Quartz, and WebSphere Settings

Before deploying the JasperReports Server WAR file, update the CSRFGuard, Hibernate, Quartz, and settings as described here.

Configure CSRFGuard, Hibernate, and Quartz settings in the WAR file

1.  The WAR file is an archive format in a single file.

    1.  Extract the `Websphere.jrs.csrfguard.properties` file using the following command:

        ``` bash
        cd <js-install>
        "%JAVA_HOME%/bin/jar" xf jasperserver-pro.war WEB-INF/csrf/Websphere.jrs.csrfguard.properties
        ```

        This creates the `WEB-INF/csrf` folder in the current location and places the extracted file there.

    2.  Rename the file from `Websphere.jrs.csrfguard.properties` to `jrs.csrfguard.properties` using the following command:

        ``` bash
        mv ./WEB-INF/csrf/Websphere.jrs.csrfguard.properties ./WEB-INF/csrf/jrs.csrfguard.properties
        ```

2.  Extract and rename the `web-version24.xml` file using the commands below:

    ``` bash
    cd <js-install>
    "%JAVA_HOME%/bin/jar" xf jasperserver-pro.war WEB-INF/web-version24.xml
    mv ./WEB-INF/web-version24.xml ./WEB-INF/web.xml
    ```

    The `jar` command creates the `WEB-INF` folder in the current location and places the extracted file there.

    Open the `WEB-INF/web.xml` file for editing and replace every occurrence of

    `<res-type>javax.sql.ConnectionPoolDataSource</res-type>`

    With

    `<res-type>javax.sql.DataSource</res-type>`

    For example, change the following:

    ``` xml
    <resource-ref>
        <description>JasperServer Metadata repository</description>
            <res-ref-name>jdbc/jasperserver</res-ref-name>
            <res-type>javax.sql.ConnectionPoolDataSource</res-type>
            <res-auth>Container</res-auth>
     </resource-ref>
    ```

    To:

    ``` xml
     <resource-ref>
        <description>JasperServer Metadata repository</description>
            <res-ref-name>jdbc/jasperserver</res-ref-name>
            <res-type>javax.sql.DataSource</res-type>
            <res-auth>Container</res-auth>
     </resource-ref>
    ```

    Do the same for the Supermart, Foodmart, Audit, System Analytics and Audit Analytics databases.

3.  Enable Hibernate persistence:

    1.  Extract the `applicationContext.xml` file using the commands below:

        ``` bash
        cd <js-install>
        "%JAVA_HOME%/bin/jar" xf jasperserver-pro.war WEB-INF/applicationContext.xml
        ```

    2.  Uncomment the following line:

        ``` html
        <!--Hibernate-Validator Websphere fix-->
           <bean id="HibernatePersistenceResolverWebsphereFix"
          class="com.jaspersoft.hibernate.resolver.HibernatePersistenceProviderResolver"
          init-method="register"/>
        ```

    3.  In the same file, find the `profileAttributesResolver` bean:

        ``` xml
        <bean id="profileAttributesResolver"
          class="com.jaspersoft.jasperserver.api.metadata.user.service.impl.ProfileAttributesResolverImpl">
        ```

        Add `depends-on="HibernatePersistenceResolverWebsphereFix` to it:

        ``` xml
        <bean id="profileAttributesResolver"
          class="com.jaspersoft.jasperserver.api.metadata.user.service.impl.ProfileAttributesResolverImpl"
          depends-on="HibernatePersistenceResolverWebsphereFix">
        ```

4.  Copy the already configured files for `hibernate.properties` and `js.quartz.properties` to the `WEB-INF` folder.

    (Buildomatic configured these files for your database type in the steps above.)

    From:

    `<js-install>/buildomatic/build_conf/default/webapp/WEB-INF/classes/hibernate.properties`

    `<js-install>/buildomatic/build_conf/default/webapp/WEB-INF/js.quartz.properties`

    To:

    `<js-install>/WEB-INF/classes`

    Copy the `../buildomatic/keystore.init.properties` file needs to the `../WEB-INF/classes` directory.

5.  Edit the scheduler URI port value for WebSphere in the `js.quartz.properties`:

    Edit `js.quartz.properties`:

    Set:

    `report.scheduler.web.deployment.uri=http://localhost:8080/jasperserver-pro`

    To:

    `report.scheduler.web.deployment.uri=http://localhost:9080/jasperserver-pro`

6.  If you want to configure JasperReports Server to automatically schedule and email reports, enter your mail server information in the `js.quartz.properties` file. Modify all `report.scheduler.mail.sender.*` properties for your mail server.

7.  Now that you have modified/updated the individual configuration files, you must replace them in the WAR file archive using the following commands.

    ``` bash
    cd <js-install>
    "%JAVA_HOME%\bin\jar" uf jasperserver-pro.war WEB-INF/classes/hibernate.properties
    "%JAVA_HOME%\bin\jar" uf jasperserver-pro.war WEB-INF/js.quartz.properties
    "%JAVA_HOME%\bin\jar" uf jasperserver-pro.war WEB-INF/csrf/jrs.csrfguard.properties
    "%JAVA_HOME%\bin\jar" uf jasperserver-pro.war WEB-INF/applicationContext.xml
    ```

8.  If you have modified the `web.xml` file, replace that file in the WAR file archive using the following additional commands.

    ``` bash
    cd <js-install>
    "%JAVA_HOME%\bin\jar" uf jasperserver-pro.war WEB-INF/web.xml
    ```

9.  Enter the following additional commands:

    ``` bash
    cd <js-install>
    zip -d jasperserver-pro.war WEB-INF/lib/stax-api-1.0.2.jar
    zip -d jasperserver-pro.war WEB-INF/lib/xercesImpl-2.12.0.jar
    zip -d jasperserver-pro.war WEB-INF/lib/jta-1.1.jar
    zip -d jasperserver-pro.war WEB-INF/lib/xml-apis-1.4.01.jar
    zip -d jasperserver-pro.war WEB-INF/lib/javax.el-2.2.4.jar
    zip -d jasperserver-pro.war WEB-INF/lib/javax.el-api-2.2.4.jar
    zip -d jasperserver-pro.war WEB-INF/lib/batik\*
    ```

10. Add the latest `batik-all.jar` from Websphere:

    1.  Find the jar using the following command:

        ``` text
        find /opt/IBM/ -name "batik*.*"
        ```

    2.  Copy the file into a lib directory in the `jasperserver-pro.war` file, for example:

        ``` bash
        cd <js-install>
        mkdir -p WEB-INF/lib
        cp /opt/IBM/WebSphere/AppServer/systemApps/isclite.ear/lib/batik-all.jar WEB-INF/lib
        "%JAVA_HOME%\bin\jar" uf jasperserver-pro.war WEB-INF/lib/batik-all.jar
        ```

11. Clean up your file system by deleting the `WEB-INF` directory that you created along with the edited files it contains.

## Configuring a JDBC Provider in WebSphere

To configure a JDBC Provider in WebSphere

1.  Launch the WebSphere Administrative Console and navigate to **Resources &gt; JDBC &gt; JDBC Providers**.

2.  On the **JDBC providers** page, click the **Guided Activity** link at the top of the **JDBC Providers** page and follow the Integrated Solutions Console instructions:

    1.  Configure credentials for a secure database:

-   Use the J2C authentication aliases panel to create a new authenticated user.

    -   In Global Security, click **New** and enter the user alias, user ID, and password. The following table shows the credentials that WebSphere uses to access the database.

        |            | Alias               | Example User ID | Example Password |
        |------------|---------------------|-----------------|------------------|
        | PostgreSQL | postgresql_jasperdb | postgres        | postgres         |
        | MySQL      | mysql_jasperdb      | root            | password         |
        | Oracle     | jasperserver_user   | jasperserver    | password         |
        | DB2        | db2admin_user       | db2inst1        | password         |
        | SQL Server | jasperserver_user   | sa              | sa               |

        J2C Authentication Alias Settings

        1.  Connect to a database panel. From the Scope drop-down, choose **`Node:<node_name>,Server=<server_name>`**

            1.  Click the **New** button to create a new JDBC Provider.
            2.  Select your database type:

        -   If you are using PostgreSQL or MySQL — select User-defined.

        -   If you want to use the JDBC driver built and distributed by the MySQL project, see [MySQL Example](../../../installation-guide/additional/jdbc-driver.md)

        -   If you are using the DB2, Oracle, or SQL Server — select the appropriate database.

            1.  Select or enter these options. Your options depend on your database type.

                <table>
                <colgroup>
                <col style="width: 33%" />
                <col style="width: 33%" />
                <col style="width: 33%" />
                </colgroup>
                <thead>
                <tr>
                <th>Database type</th>
                <th>Implementation class name or type</th>
                <th>Name</th>
                </tr>
                </thead>
                <tbody>
                <tr>
                <td><p>User-defined (PostgreSQL)</p></td>
                <td><p><code>org.postgresql.jdbc2.optional.ConnectionPool</code></p></td>
                <td><p>PostgreSQL JDBC Provider</p></td>
                </tr>
                <tr>
                <td>User-defined<br />
                (MySQL)</td>
                <td><code>org.mariadb.jdbc.MySQLDataSource</code></td>
                <td><p>MySQL JDBC Provider</p></td>
                </tr>
                <tr>
                <td><p>User-defined<br />
                (MySQL)</p></td>
                <td><p><code>com.mysql.jdbc.jdbc2.optional</code>.<br />
                  <code>MysqlConnectionPoolDataSource</code></p></td>
                <td><p>MySQL JDBC Provider</p></td>
                </tr>
                <tr>
                <td><p>DB2 Universal JDBC Driver Provider</p></td>
                <td><p>Connection pool data source</p></td>
                <td><p>DB2 Universal JDBC Driver Provider</p></td>
                </tr>
                <tr>
                <td><p>Oracle</p></td>
                <td><p>Connection pool data source</p></td>
                <td><p>Oracle JDBC Driver</p></td>
                </tr>
                <tr>
                <td><p>SQL Server</p></td>
                <td><p>Connection pool data source</p></td>
                <td><p>Microsoft SQL Server JDBC Driver</p></td>
                </tr>
                </tbody>
                </table>

            2.  Click `Next` and enter the database classpath information for the JDBC provider.

                1.  For PostgreSQL, MySQL, Oracle, SQL Server, and DB2, enter the following:

                    `<js-install>\buildomatic\conf_source\db\<your_database>\jdbc\`

                    For example, enter:

                    `C:\`

                    `js-jrs``_10.1.0`

                    \_bin\\buildomatic\\conf_source\\db\\postgresql\\jdbc\\postgresql-42.2.5.jar

                    Alternatively, you can copy the jar to a location in your WebSphere deployment and specify that location for the JDBC driver path.

                    !!! note

                        If JasperReports Server is deployed on the same host as DB2, delete the following file to avoid conflicts: `<db2>/SQLLIB/java/db2jcc.jar`

            3.  To ensure you have full support for import/export from the command line, copy your JDBC driver to the following location. If you are not using the command line for import/export, you can skip this step:

                |       |                                                                 |
                |-------|-----------------------------------------------------------------|
                | from: | `<js-install>\buildomatic\conf_source\db\<your_database>\jdbc\` |
                | to:   | `<js-install>\buildomatic\conf_source\iePro\lib`                |

            4.  Click **Next** to proceed to the next step.

            5.  Review the JDBC provider information that you entered and click **Finish**.

            To define the jasperserver JDBC data source and expose it through JNDI

            1.  Click the name of the JDBC provider that you just created. For example, for PostgreSQL, click **PostgreSQL JDBC Provider**.

                !!! note

                    To use a database other than PostgreSQL, configure the database connections and custom properties as described in [Configuring Other Database Connections](../../../installation-guide/websphere/websphere_other_dbs.md) .

            2.  Click **Data sources** in the **Additional Properties** of the JDBC provider details panel.

            3.  To create a new data source, click **New**. The **New Data Source** wizard appears.

            4.  Enter the data source name: `jasperserver`

            5.  Enter the JNDI name: `jdbc/jasperserver`

            6.  Click **Next**, choose **Select an existing JDBC provider**, then select **PostgreSQL JDBC Provider** from the drop-down list.

            7.  Click **Next** and accept the default helper class (`com.ibm.websphere.rsadapter.GenericDataStoreHelper`). Select the checkbox to use this data source in container managed persistence (CMP).

            8.  Click **Next** and select the Setup security aliases, as shown in the following table.

                | Field Name                             | PostgreSQL Value        |
                |----------------------------------------|-------------------------|
                | Component-managed authentication alias | `postgresql_jasperdb`   |
                | Mapping configuration alias            | DefaultPrincipalMapping |
                | Container-managed authentication alias | `postgresql_jasperdb`   |

            9.  Click **Next**, review the summary information, and click **Finish**.

            To set the connection pool size

            1.  In the list of JDBC data sources, click the newly created **jasperserver** data source to edit it.
            2.  Click **Additional Properties &gt; Connection Pool Properties**. You can see that **Maximum Connections** is set to 10 by default.
            3.  Set **Maximum Connections** to 50. You may want to set it to a higher value if necessary.
            4.  Click **Save**.

            To define custom properties

            1.  In the list of JDBC data sources, select the check box for the newly created **jasperserver** data source and click **Test Connection**.

                In the Messages area, a success or failure message appears. The failure message gives you information about which custom properties you need to define.

            2.  Navigate to the jasperserver data sources **General Properties** page.

            3.  In **Additional Properties**, on the right side of the **General Properties** page, click **Custom properties**.

            4.  Scroll down the list of properties and select **databaseName**. Set the value to `jasperserver`.

            5.  Set **serverName** to the correct value for your server.

            To define the jsSystemAnalytics JDBC data source and expose it through JNDI

            1.  Click the name of the JDBC provider that you just created. For example, for PostgreSQL, click **PostgreSQL JDBC Provider**.

                !!! note

                    To use a database other than PostgreSQL, configure the database connections and custom properties as described in [Configuring Other Database Connections](../../../installation-guide/websphere/websphere_other_dbs.md).

            2.  Click **Data sources** in the **Additional Properties** of the JDBC provider details panel.

            3.  To create a new data source, click **New**. The **New Data Source Wizard** appears.

            4.  Enter the data source name: `jsSystemAnalytics`

            5.  Enter the JNDI name: `jdbc/jasperserverSystemAnalytics`

            6.  Click **Next**, choose **Select an existing JDBC provider**, then select **PostgreSQL JDBC Provider** from the drop-down list.

            7.  Click **Next** and accept the default helper class (com.ibm.websphere.rsadapter.GenericDataStoreHelper). Select the checkbox to use this data source in container managed persistence (CMP).

            8.  Click **Next** and select the Setup security aliases, as shown in the following table.

                | Field Name                             | PostgreSQL Value        |
                |----------------------------------------|-------------------------|
                | Component-managed authentication alias | `postgresql_jasperdb`   |
                | Mapping configuration alias            | DefaultPrincipalMapping |
                | Container-managed authentication alias | `postgresql_jasperdb`   |

            9.  Click **Next**, review the summary information, and click **Finish**.

            To set the connection pool size

            1.  In the list of JDBC data sources, click the newly created **jsSystemAnalytics** data source to edit it.
            2.  Click **Additional Properties &gt; Connection Pool Properties**. You can see that **Maximum Connections** is set to 10 by default.
            3.  Set **Maximum Connections** to 50. You may want to set it to a higher value if necessary.
            4.  Click **Save**.

            To define custom properties

            1.  In the list of JDBC data sources, select the check box for the newly created **jsSystemAnalytics** data source and click **Test Connection**.

                In the Messages area, a success or failure message appears. The failure message gives you information about which custom properties you need to define.

            2.  Navigate to the jasperserver data sources **General Properties** page.

            3.  In **Additional Properties**, on the right side of the **General Properties** page, click **Custom properties**.

            4.  Scroll down the list of properties and select **databaseName**. Set the value to `jsSystemAnalytics`.

            5.  Set **serverName** to the correct value for your server.

            To define the jsaudit JDBC data source and expose it through JNDI

            1.  Click the name of the JDBC provider that you just created. For example, for PostgreSQL, click **PostgreSQL JDBC Provider**.

                !!! note

                    To use a database other than PostgreSQL, configure the database connections and custom properties as described in [Configuring Other Database Connections](../../../installation-guide/websphere/websphere_other_dbs.md).

            2.  Click **Data sources** in the **Additional Properties** of the JDBC provider details panel.

            3.  To create a new data source, click **New**. The **New Data Source Wizard** appears.

            4.  Enter the data source name:` jsaudit`

            5.  Enter the JNDI name: `jdbc/jasperserverAudit`

            6.  Click **Next**, choose **Select an existing JDBC provider**, then select **PostgreSQL JDBC Provider** from the drop-down list.

            7.  Click **Next** and accept the default helper class (com.ibm.websphere.rsadapter.GenericDataStoreHelper). Select the check box to use this data source in container managed persistence (CMP).

            8.  Click **Next** and select the Setup security aliases, as shown in the following table.

                | Field Name                             | PostgreSQL Value        |
                |----------------------------------------|-------------------------|
                | Component-managed authentication alias | `postgresql_jasperdb`   |
                | Mapping configuration alias            | DefaultPrincipalMapping |
                | Container-managed authentication alias | `postgresql_jasperdb`   |

            9.  Click **Next**, review the summary information, and click **Finish**.

            To set the connection pool size

            1.  In the list of JDBC data sources, click the newly created **jsaudit** data source to edit it.
            2.  Click **Additional Properties &gt; Connection Pool Properties**. You can see that **Maximum Connections** is set to 10 by default.
            3.  Set **Maximum Connections** to 50. You may want to set it to a higher value if necessary.
            4.  Click **Save**.

            To define custom properties

            1.  In the list of JDBC data sources, select the check box for the newly created **jsaudit** data source and click **Test Connection**.

                In the Messages area, a success or failure message appears. The failure message gives you information about which custom properties you need to define.

                !!! note

                    If you are using the TIBCO JDBC driver with SQL Server, and you see an error such as the following:

                    `Could not find stored procedure 'master..xp_jdbc_open2' DSRA0010E: SQL State = HY000, Error Code=2,812`

                    Add the following variable to **Custom properties**:

                    `enable2Phase = false`

            2.  Navigate to the **jsaudit** data sources **General Properties** page.

            3.  In **Additional Properties**, on the right side of the **General Properties** page, click **Custom properties**.

            4.  Scroll down the list of properties and select **databaseName**. Set the value to:

    -   For Compact installation: `jasperserver`

    -   For Split installation: `jsaudit`

        1.  Set **serverName** to the correct value for your server.

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
            <td><p><code>foodmart</code></p></td>
            <td><p><code>sugarcrm</code></p></td>
            </tr>
            <tr>
            <td><p>JNDI name</p></td>
            <td><p><code>jdbc/foodmart</code></p></td>
            <td><p><code>jdbc/sugarcrm</code></p></td>
            </tr>
            </tbody>
            </table>

        2.  Click **Save directly to the master configuration**.

        Next, deploy the WAR file in WebSphere as described in Deploying the WAR File in WebSphere.

        To define the jsAuditAnalytics JDBC data source and expose it through JNDI

        1.  Click the name of the JDBC provider that you just created. For example, for PostgreSQL, click **PostgreSQL JDBC Provider**.

            !!! note

                To use a database other than PostgreSQL, configure the database connections and custom properties as described in [Configuring Other Database Connections](../../../installation-guide/websphere/websphere_other_dbs.md).

        2.  Click **Data sources** in the **Additional Properties** of the JDBC provider details panel.

        3.  To create a new data source, click **New**. The **New Data Source Wizard** appears.

        4.  Enter the data source name: `jsAuditAnalytics`

        5.  Enter the JNDI name: `jdbc/jasperserverAuditAnalytics`

        6.  Click **Next**, choose **Select an existing JDBC provider**, then select **PostgreSQL JDBC Provider** from the drop-down list.

        7.  Click **Next** and accept the default helper class (com.ibm.websphere.rsadapter.GenericDataStoreHelper). Select the check box to use this data source in container managed persistence (CMP).

        8.  Click **Next** and select the Setup security aliases, as shown in the following table.

            | Field Name                             | PostgreSQL Value        |
            |----------------------------------------|-------------------------|
            | Component-managed authentication alias | `postgresql_jasperdb`   |
            | Mapping configuration alias            | DefaultPrincipalMapping |
            | Container-managed authentication alias | `postgresql_jasperdb`   |

        9.  Click **Next**, review the summary information, and click **Finish**.

        To set the connection pool size

        1.  In the list of JDBC data sources, click the newly created **jsaudit** data source to edit it.
        2.  Click **Additional Properties &gt; Connection Pool Properties**. You can see that **Maximum Connections** is set to 10 by default.
        3.  Set **Maximum Connections** to 50. You may want to set it to a higher value if necessary.
        4.  Click **Save**.

        To define custom properties

        1.  In the list of JDBC data sources, select the check box for the newly created **jsAuditAnalytics** data source and click **Test Connection**.

            In the Messages area, a success or failure message appears. The failure message gives you information about which custom properties you need to define.

        2.  Navigate to the **jsaudit** data sources **General Properties** page.

        3.  In **Additional Properties**, on the right side of the **General Properties** page, click **Custom properties**.

        4.  Scroll down the list of properties and select **databaseName**. Set the value to:

    -   For Compact installation: `jasperserver`

    -   For Split installation: `jsaudit`

1.  Set **serverName** to the correct value for your server.

## Deploying the WAR File in WebSphere

To deploy the JasperReports Server WAR file in WebSphere

1.  In the Administrative Console, navigate to ****Applications &gt; New Application**** and select **New Enterprise Application.**

    JasperReports Server is a modern application, based on Java Servlet version 2.4, so you do not select the older, WebSphere V4‑compliant application type.

2.  Browse to `<js-install>/jasperserver-pro.war` on the local file system. Keep the default setting (**Fast path**) selected and click **Next**.

3.  On the **Select installation options** page, accept all the default settings and click **Next**.

4.  On the Map modules to servers page, make sure the JasperReports Server module is mapped to the cell, node, and server that you want. Click **Next**.

5.  On the Map modules to servers page, select **jasperserver**. Click **Next**.

6.  On the Map resource references to resources page, map the resources you want:

    1.  First, select the **Browse** button under the `jdbc/jasperserver` resource. In the page that opens, select the **jdbc/jasperserver** radio button, and click **Apply**. Then select the check box next to the **jdbc/jasperserver** resource.
    2.  Select the **Browse** button under the `jdbc/jasperserverAudit` resource. In the page that opens, select the **jdbc/jasperserverAudit** radio button, and click **Apply**. Then select the check box next to the **jdbc/jasperserverAudit** resource.
    3.  Select the **Browse** button under the `jdbc/jasperserverSystemAnalytics` resource. In the page that opens, select the **jdbc/jasperserverSystemAnalytics** radio button, and click **Apply**. Then select the check box next to the **jdbc/jasperserverSystemAnalytics** resource.
    4.  Select the **Browse** button under the `jdbc/jasperserverAuditAnalytics` resource. In the page that opens, select the **jdbc/jasperserverAuditAnalytics** radio button, and click **Apply**. Then select the check box next to the **jdbc/jasperserverAuditAnalytics** resource.
    5.  If you plan to run the sample reports, follow the same steps for `jdbc/surgarcrm` and `jdbc/foodmart`, making sure to select the correct radio button for each one.
    6.  When you have mapped all resources, select the check boxes next to every resource have mapped.
    7.  Click **Next**.

7.  On the Map virtual hosts page, choose the **JasperServer UI application module**. Click **Next.**

8.  In the Map context roots for Web modules, enter `jasperserver-pro`.

9.  Click **Next**, review the summary information and start the installation process. (The installation process may take a while.)

10. Click **Save directly to the master configuration**.

## Setting JVM Options

To set the Java JVM Options

For the JasperReports Server XML/A functionality to work, special Java JVM options need to be set to resolve class conflicts between the WebSphere and JasperReports Server web services implementation. JVM options also provide the optimal resources for running JasperReports Server.

To configure your Java JVM options

1.  Select ****Enterprise Applications &gt; jasperserver-pro_war &gt; Target specific application status &gt; (server name)****.

2.  Expand ****Java and Process Management**** **&gt; Process Definition &gt; Java Virtual Machine &gt; Generic JVM arguments.**

3.  In the **Generic JVM Options** text box, paste in the following JVM options that explicitly specify JasperReports Server classes for Xalan, as well as optimize JVM resources. The memory settings are a recommended minimum; you may need to increase the memory assigned to the JVM according to your usage:

    <table>
    <thead>
    <tr>
    <th colspan="2"><p>Generic JVM Options on Windows</p></th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td><p>Options for all databases</p></td>
    <td><code>-Dclient.encoding.override=UTF-8 -Xms2048m -Xmx4096m -Xss2m -XX:+UseG1GC -Dlog4j.configurationFile=WEB-INF/log4j2.properties</code></td>
    </tr>
    <tr>
    <td><p>Additional option for Oracle</p></td>
    <td><code>-Doracle.jdbc.defaultNChar=true</code></td>
    </tr>
    <tr>
    <td>Additional option for FTPS connections</td>
    <td><code>-Dcom.ibm.jsse2.overrideDefaultTLS=true</code></td>
    </tr>
    </tbody>
    </table>

    <table>
    <thead>
    <tr>
    <th colspan="2"><p>Generic JVM Options on Linux</p></th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td><p>Options for all databases</p></td>
    <td><code>-Dclient.encoding.override=UTF-8 -Xms2048m -Xmx4096m -Xss2m -XX:+UseG1GC -Dlog4j.configurationFile=WEB-INF/log4j2.properties</code></td>
    </tr>
    <tr>
    <td><p>Additional option for Oracle</p></td>
    <td><code>-Doracle.jdbc.defaultNChar=true</code></td>
    </tr>
    <tr>
    <td>Additional option for FTPS connections</td>
    <td><code>-Dcom.ibm.jsse2.overrideDefaultTLS=true</code></td>
    </tr>
    </tbody>
    </table>

    !!! note

        Setting the Oracle localization option, `defaultNChar`, can substantially impact the performance of JDBC queries. If you don't need to support UTF-8 for your Oracle database, you can omit this setting.

4.  Click **Save** on the console task bar.

To configure class loading

1.  Select **Enterprise Applications &gt; jasperserver-pro_war &gt; Class loading and update detection**.
2.  In the section **Class loader order**, select **Classes loaded with local class loader first (parent last)**.
3.  In the **WAR class loader policy** section select **Single class loader for application**.
4.  Save directly to your master configuration.
5.  Restart WebSphere.

Next, start JasperReports Server as described in [Starting and Restarting JasperReports Server](../../../installation-guide/websphere/websphere_starting_jrs.md).
