---
title: Procedure for Installing the WAR File for WebLogic
description: "To meet the prerequisites for installing the WAR file for WebLogic:"
---

# Procedure for Installing the WAR File for WebLogic

To meet the prerequisites for installing the WAR file for WebLogic:

1.  Check that a supported version of the Oracle/Sun Java JDK is installed.
2.  Check that the `JAVA_HOME` system environment variable points to the JDK.
3.  Install the PostgreSQL, MySQL, Oracle, SQL Server, or DB2 database.

!!! note

    The target database can be on a remote server.

    Due to limitations in the vendor's driver for MySQL, Jaspersoft has verified MySQL using the MariaDB driver.

To install the WAR file for WebLogic:

1.  Extract all files in

    `js-jrs``_10.1.0`

    `_bin.zip` into a top-level directory, such as `C:\Jaspersoft` on Windows or `/home/<user>` on Linux.

    Unpacking the ZIP file creates the directory

    `js-jrs_``pro`` _10.1.0_bin.zip`

    .

2.  Check that WebLogic is installed in the default location on your local machine.

    If WebLogic is not installed in the default location, or if you encounter problems using the buildomatic scripts, set up the database manually as described in [Manually Creating the JasperReports Server Database](../../../installation-guide/manual-db/manually_creating_the_jasperreports_.md). After setting up the database manually, skip Step 6 through Step 9 , and proceed to Step 10.

3.  (If you are using MySQL, you can skip this step.) Copy your JDBC driver to WebLogic.<br>
    PostgreSQL Example:

    1.  Copy the JDBC jar:<br>
        From:

        `<js-install>/buildomatic/conf_source/db/postgresql/jdbc`

        To:

        `<weblogic_home>/server/lib`

        Note that the MySQL JDBC driver is included in recent versions of WebLogic.

4.  To ensure you have full support for import/export from the command line, copy your JDBC driver to the following location. If you are not using the command line for import/export, you can skip this step:

    |       |                                                                 |
    |-------|-----------------------------------------------------------------|
    | from: | `<js-install>\buildomatic\conf_source\db\<your_database>\jdbc\` |
    | to:   | `<js-install>\buildomatic\conf_source\iePro\lib`                |

5.  Restart WebLogic using `startWebLogic.cmd/sh`.

6.  Copy the .properties file for your database:

    From: `<js-install>/buildomatic/sample_conf/`

    To: `<js-install>/buildomatic`

7.  Rename the file that you copied to the `default_master.properties` file.

8.  Edit the default_master.properties file to add settings specific to your database and your application server. Sample Values for the default_master.properties File shows sample property values.

    !!! note

        When appServerType = skipAppServerCheck, buildomatic skips the application server type validation. Use this setting when installing JasperReports Server with WebLogic. Backslashes in appServerDir must be doubled, for example C:\\\\WL\\\\Application_Server. Make sure that there are no spaces in the appServerDir path.

    <table>
    <caption><p>Sample Values for the default_master.properties File</p></caption>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <thead>
    <tr>
    <th><p>Database</p></th>
    <th><p>Sample Property Values</p></th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td><p>PostgreSQL</p></td>
    <td><code>appServerType=skipAppServerCheck appServerDir=[path to WebLogic application server] dbUsername=postgres dbPassword=postgres dbHost=localhost</code></td>
    </tr>
    <tr>
    <td><p>DB2</p></td>
    <td><code>appServerType=skipAppServerCheck appServerDir=[path to WebLogic application server] dbUsername=db2inst1 dbPassword=password dbHost=localhost</code></td>
    </tr>
    <tr>
    <td><p>MySQL</p></td>
    <td><code>appServerType=skipAppServerCheck appServerDir=[path to WebLogic application server] dbUsername=root dbPassword=password dbHost=localhost</code></td>
    </tr>
    <tr>
    <td><p>Oracle</p></td>
    <td><code>appServerType=skipAppServerCheck appServerDir=[path to WebLogic application server] sysUsername=system sysPassword=password dbUsername=jasperserver dbPassword=password dbHost=hostname</code>
    <p>Note that <code>dbUsername</code> must be the same as the Oracle username.</p></td>
    </tr>
    <tr>
    <td><p>SQL Server</p></td>
    <td><code>appServerType=skipAppServerCheck appServerDir=[path to WebLogic application server] dbUsername=sa dbPassword=sa dbHost=localhost</code></td>
    </tr>
    </tbody>
    </table>

    For the Split installation, configure the additional settings in the `default_master.properties` file as described in [Additional Buildomatic Configuration for Split Installation Upgrade](../introduction/installation_types.md).

    For the JNDI Restricted Access installation, configure the additional settings in the `default_master.properties` file as described in [Installation Types](../introduction/installation_types.md).

9.  Set up the database and optional sample databases using the buildomatic Ant scripts. Enter the commands in the table below to call buildomatic Ant scripts:

    !!! note

        Exception: For DB2, skip this step and perform [Step 1](../../../installation-guide/manual-db/manually_creating_the_jasperreports_.md) to [Step 4](../../../installation-guide/manual-db/manually_creating_the_jasperreports_.md) in [DB2](../../../installation-guide/manual-db/manually_creating_the_jasperreports_.md), then go to Step 10 of this procedure.

    You call buildomatic Ant scripts from the command line using the following syntax:

    `Windows — js-ant <target-name>`

    `Linux — ./js-ant <target-name>`

    <table>
    <caption>Buildomatic Targets to Run</caption>
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
    <td><p>Goes to the buildomatic directory.</p></td>
    </tr>
    <tr>
    <td><code>js-ant create-js-db</code></td>
    <td>Creates the jasperserver repository database.</td>
    </tr>
    <tr>
    <td><p><code>js-ant init-js-db-pro</code></p>
    <p><code>js-ant import-minimal-pro</code></p></td>
    <td><p>Initializes database, loads core application data.</p></td>
    </tr>
    <tr>
    <td><p><code>js-ant create-sugarcrm-db</code></p>
    <p><code>js-ant create-foodmart-db</code></p></td>
    <td>(Optional) Creates sample databases.</td>
    </tr>
    <tr>
    <td><p><code>js-ant load-sugarcrm-db</code></p>
    <p><code>js-ant load-foodmart-db</code></p></td>
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

    !!! note

        On non-Linux Unix platforms, the js-ant commands may not be compatible with all shells. If you have errors, use the `bash` shell explicitly. For more information, see [Bash Shell for Solaris, IBM AIX, HP UX and FreeBSD](../../../installation-guide/troubleshooting/bash_shell_for_other_linux.md).

    !!! note

        Installing JasperReports Server automatically generates encryption keys that reside on the file system. These keys are stored in a dedicated Jaspersoft keystore. Make sure that this keystore is properly secured and backed up, as described in the JasperReports Server Security Guide.

10. Add the database driver location to the WebLogic classpath in the following file:

    `<weblogic_home>/domains/<user_domain>/bin/setDomainEnv.sh`

    Use the path for the driver copied in Step 3. For example, for a PostgreSQL driver, you might add the following:

    `export CLASSPATH=/opt/Oracle/Middleware/Oracle_Home/wlserver/server/lib/postgresql.jar:`<br>
    `/opt/Oracle/Middleware/Oracle_Home/wlserver/server/lib/jswlstc-1.0.jar:$CLASSPATH`

11. In WebLogic, open an **Administrative Console** window and navigate to **Services &gt;** ****Data Sources**** or **Domain Configurations &gt; Services &gt; Data Sources**.

12. Click **New** and then **Generic Data Source** for each of the data source columns in the following table, and enter the following values for a PostgreSQL database. You will need to click **Next** after entering the database driver and after **One-Phase Commit**.

    !!! note

        To use a database other than PostgreSQL, configure the database connections using the settings shown in [Configuring Databases Using the Vendor's Driver](../../../installation-guide/weblogic/weblogic_database_connections.md).

        If you plan to use the sample databases (Foodmart and Sugar CRM), perform this step and the following step for each database.

    <table style="width:100%;">
    <colgroup>
    <col style="width: 14%" />
    <col style="width: 14%" />
    <col style="width: 14%" />
    <col style="width: 14%" />
    <col style="width: 14%" />
    <col style="width: 14%" />
    <col style="width: 14%" />
    </colgroup>
    <thead>
    <tr>
    <th>Parameter Name</th>
    <th>JasperReports Server</th>
    <th>JasperReports Server Audit</th>
    <th>JasperServerSystemDataBase</th>
    <th>AuditAnalyticsDataBase</th>
    <th>Foodmart</th>
    <th>Sugar CRM</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td><p>Name</p></td>
    <td><p>JasperServerDataBase</p></td>
    <td><p>AuditDataBase</p></td>
    <td>Jasper Server System DataBase</td>
    <td>Audit Analytics DataBase</td>
    <td><p>FoodmartDataBase</p></td>
    <td><p>SugarcrmDataBase</p></td>
    </tr>
    <tr>
    <td><p>JNDI Name</p></td>
    <td><p>JasperServerDataBase</p></td>
    <td><p>AuditDataBase</p></td>
    <td>JasperServerSystemDataBase</td>
    <td>AuditAnalyticsDataBase</td>
    <td><p>FoodmartDataBase</p></td>
    <td><p>SugarcrmDataBase</p></td>
    </tr>
    <tr>
    <td><p>Database Type</p></td>
    <td colspan="6"><p>PostgreSQL</p></td>
    </tr>
    <tr>
    <td><p>Database Driver</p></td>
    <td colspan="6"><p>PostgreSQL Driver Versions: using org.postgresql.Driver</p></td>
    </tr>
    <tr>
    <td><p>Supports Global<br />
    Transactions</p></td>
    <td colspan="6"><p>Selected</p></td>
    </tr>
    <tr>
    <td><p>One-Phase Commit</p></td>
    <td colspan="6"><p>Selected</p></td>
    </tr>
    </tbody>
    </table>

13. Set connection properties. Sample properties for a PostgreSQL database are:

    <table>
    <colgroup>
    <col style="width: 20%" />
    <col style="width: 20%" />
    <col style="width: 20%" />
    <col style="width: 20%" />
    <col style="width: 20%" />
    </colgroup>
    <thead>
    <tr>
    <th>Parameter Name</th>
    <th>JasperReports Server</th>
    <th>JasperReports Server Audit</th>
    <th>Foodmart</th>
    <th>Sugar CRM</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td><p>Database Name</p></td>
    <td><p>jasperserver</p></td>
    <td>For Compact installation: jasperserver<br />
    For Split installation: jsaudit</td>
    <td><p>foodmart</p></td>
    <td><p>sugarcrm</p></td>
    </tr>
    <tr>
    <td><p>Host Name</p></td>
    <td colspan="4"><p>localhost</p></td>
    </tr>
    <tr>
    <td><p>Port</p></td>
    <td colspan="4"><p>5432</p></td>
    </tr>
    <tr>
    <td><p>Database username</p></td>
    <td colspan="4"><p>PostgreSQL</p></td>
    </tr>
    <tr>
    <td><p>Password</p></td>
    <td colspan="4"><p>PostgreSQL</p></td>
    </tr>
    <tr>
    <td><p>Confirm Password</p></td>
    <td colspan="4"><p>PostgreSQL</p></td>
    </tr>
    </tbody>
    </table>

14. Test the database connection:

    1.  For SugarCRM and Foodmart, use the default connections:

        **JDBC:postgresql://localhost:5432/sugarcrm**

        **jdbc:postgresql://localhost:5432/foodmart**

    2.  Change the URL for the JasperServerDataBase to:

        **jdbc:postgresql://localhost:5432/jasperserver**

    3.  Change the URL for the AuditDataBase to:

        For Compact installation: **jdbc:postgresql://localhost:5432/jasperserver**

        For Split installation: **jdbc:postgresql://localhost:5432/jsaudit**

    4.  Change the URL for the JasperServerSystemDataBase to:

        **jdbc:postgresql://localhost:5432/jasperserver**

    5.  Change the URL for the AuditAnalyticsDataBase to:

        For Compact installation: **jdbc:postgresql://localhost:5432/jasperserver**

        For Split installation: **jdbc:postgresql://localhost:5432/jsaudit**

15. Select targets and ensure that **AdminServer** is set for all data sources.

16. In WebLogic, open an **Administrative Console** window and navigate to **Services &gt; Data Sources** or **Domain Configurations &gt; Services &gt; Data Sources**.

17. Select each created data source (JasperServerDataBase, AuditDataBase, FoodmartDataBase, and SugarcrmDataBase)

18. Select the Connection Pool tab and increase the **Maximum Capacity** setting, depending on load. For most installations, a **Maximum Capacity** in the range 50 – 100 should be sufficient. If you receive connection pool errors, increase this setting; see the documentation for WebLogic for more information.

19. On the Connection Pool tab, expand **Advanced** and enable **Test Connections On Reserve**. Set the **Test Frequency** to 30 seconds and set the **Test Table Name** for your datasource and database type. Sample properties for a PostgreSQL database are:

    | Parameter Name | JasperReports Server | JasperReports Server Audit | JasperServerSystemDataBase | AuditAnalyticsDataBase | Foodmart | Sugar CRM |
    |----|----|----|----|----|----|----|
    | Name | JasperServerDataBase | AuditDataBase | Jasper Server System DataBase | Audit Analytics DataBase | FoodmartDataBase | SugarcrmDataBase |
    | Test Table Name | JIREPORTJOB | JIREPORTJOB | JIREPORTJOB | JIREPORTJOB | ACCOUNT | ACCOUNTS |

20. Click **Save**.

21. Use the Java jar tool or an unzip tool to unpack the jasperserver-pro.war file. For example, using the Java jar tool, enter these commands to unpack the jasperserver-pro.war file to a folder:

    ``` bash
    cd <js-install-dir>
    mkdir jasperserver-pro
    cd jasperserver-pro
    "%JAVA_HOME%/bin/jar" xvf ../jasperserver-pro.war
    ```

22. Search for conflicting JARs and delete them from the WAR file. If the following JARs are present in your WebLogic installation, you need to delete them from your JasperReports Server installation to avoid conflicts. To do this:

    1.  Search your WebLogic installation for the following files:

        `jaxb-api-<ver>.jar`

        `jaxb-impl-<ver>.jar`

        `serializer-<ver>.jar`

        `stax-api-<ver>.jar`

        `xalan-<ver>.jar`

        `xercesImpl-<ver>.jar`

        `xml-apis-<ver>.jar`

    2.  Change to the JasperReports Server WEB-INF/lib directory:

        `cd <js-install>/jasperserver-pro/WEB-INF/lib`

    3.  Delete any conflicting JARs.

23. Replace the default web.xml file with the following commands:

    ``` bash
    cd <js-install-dir>/jasperserver-pro/WEB-INF
    mv ./web-version24.xml ./web.xml
    ```

24. Update your Hibernate, Quartz, and Mail Server configuration:

    1.  The buildomatic logic has already configured the `hibernate.properties` and `js.quartz.properties` files for your database type. So you can copy these files to the `jasperserver-pro` file as shown below.

        Copy from:

        `<js-install>/buildomatic/build_conf/default/webapp/WEB-INF/classes/hibernate.properties`

        `<js-install>/buildomatic/build_conf/default/webapp/WEB-INF/js.quartz.properties`

        To:

        `jasperserver-pro/WEB-INF/classes`

    2.  Edit the scheduler URI port value for WebLogic in the `js.quartz.properties`:

        Edit `js.quartz.properties`:

        Set:

        `report.scheduler.web.deployment.uri=http://localhost:8080/jasperserver-pro`

        To:

        `report.scheduler.web.deployment.uri=http://localhost:7001/jasperserver-pro`

    3.  If you want to configure JasperReports Server to automatically schedule and email reports, enter your mail server information in the `js.quartz.properties` file. Modify all `report.scheduler.mail.sender.*` properties as necessary for your mail server.

        Copy the `../buildomatic/keystore.init.properties` file to the `../WEB-INF/classes` directory.

        Also for WebLogic (for DB2, Oracle, and SQL Server):

        `progressiveStreaming=2` needs to be added to the variables.

        For more information on the progressiveStreaming variable, refer to the section "BeanDefinitionStoreException with DB2" with Vendor's Driver in [Database-related Problems](../../../installation-guide/troubleshooting/database_related_problems.md).

25. If your mail server requires authentication, edit the `applicationContext-report-scheduling.xml` file:

    1.  Open the `jasperserver-pro/WEB-INF/applicationContext-report-scheduling.xml` file for editing and locate the `reportSchedulerMailSender` bean.
    2.  Set the `javaMailProperties key=`"`mail.smtp.auth`" value to `true`.

26. Now you can change to the `jasperserver-pro` folder and re-archive the `jasperserver-pro.war` file, using commands such as the following.

    <table>
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
    <td><p><code>cd ../..</code></p></td>
    <td><p>Changes to the jasperserver-pro folder</p></td>
    </tr>
    <tr>
    <td><p><code>mv ../jasperserver-pro.war ../BAK-jasperserver-pro.war</code></p></td>
    <td><p>Renames the original jasperserver-pro.war file.</p></td>
    </tr>
    <tr>
    <td><p><code>"%JAVA_HOME%/bin/jar" cvf ../jasperserver-pro.war *</code></p></td>
    <td><p>Re-archives the jasperserver-pro.war file.</p></td>
    </tr>
    <tr>
    <td><p><code>cd ..</code></p>
    <p><code>mv jasperserver-pro BAK-jasperserver-pro</code></p></td>
    <td><p>Renames the unneeded working folder to a backup location.</p></td>
    </tr>
    </tbody>
    </table>

    !!! note

        You now have a `jasperserver-pro.war` file that you can use for deploying to WebLogic.

27. Edit your WebLogic domain configuration file `<wl-domain>/config/config.xml`:

    !!! note

        &lt;wl-domain&gt; is the path of the domain within WebLogic that contains your JasperReports Server deployment. For example, `<weblogic>/samples/domains/wl_server`.

    1.  Locate the `server` and `security-configuration` elements, and insert the following parameters:

        ``` xml
        <server>
        ...
            <stuck-thread-max-time>1200</stuck-thread-max-time>
            <listen-address></listen-address>
        </server>
        <security-configuration>
            ...
            <enforce-valid-basic-auth-credentials>false</enforce-valid-basic-auth-credentials>
        </security-configuration>
        ```

    2.  Check that the `stuck-thread-max-time` element appears above the `listen-address` element before the closing `</server>` tag.

        !!! note

            In some cases, setting the `stuck-thread-max-time` may cause a schema validation error. Then, you can try removing this line from the configuration file.

28. Set JVM options as described in [Setting Java Properties](../../../installation-guide/weblogic/setting_java_properties.md).

Deploy JasperReports Server to WebLogic:

1.  Enable the **Lock & Edit** button:

    1.  Select the **Preferences** link at the top of the Admin console.
    2.  Scroll to the bottom of the **User Preferences** screen and deselect **Automatically Acquire Lock** and **Activate Changes**.
    3.  Save.

2.  In the **Administrative Console**, click the **Lock & Edit** button and navigate to **Deployments**.

3.  On the **Deployments** page, click the **Install** button.

4.  Select the path to `<js-install>`. Click **Next**.

5.  Leave the radio button selected for **Install this deployment as an application**. Click **Next**.

6.  When prompted, enter the following parameter values:

    | Parameter Name       | Example Value                                        |
    |----------------------|------------------------------------------------------|
    | Name                 | `jasperserver-pro`                                   |
    | Security             | Custom Roles and Policies                            |
    | Source accessibility | Use the defaults defined by the deployment's targets |

7.  Review your choices and click **Finish**.

8.  Click **Save.**
