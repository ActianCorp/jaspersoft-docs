---
title: Installation Types
description: "As of version 8.0, JasperReports Server supports the following installations:"
---

# Installation Types

As of version 8.0, JasperReports Server supports the following installations:

-   Compact installation: The Repository, Audit, Access, and Monitoring tables are created in a single repository database. This is the same configuration as previous versions.

-   Split installation: Only the Repository tables are created in the repository database. The Audit, Access, and Monitoring tables are created in a separate audit database. For servers with high loads or performance needs, this speeds up repository access by storing diagnostic logs separately.

The default installation is the Compact installation.

!!! note

    The Access and Audit events are now processed asynchronously using a thread pool. The default number of threads is 15 and is configurable in the applicationContext-events-logging.xml file. If you want to switch back to the synchronous mode, comment out the following section:

    ``` xml
    <bean id="loggingEventsService" class="com.jaspersoft.jasperserver.api.logging.service.impl.LoggingFacade">  <property name="asyncExecutor" ref="asyncEventsExecutor"/></bean>
    ```

!!! note

    The binary installer does not support split installation. For split installation, use the standalone WAR file distribution, which is the official JasperReports Server installer.

## Additional Buildomatic Configuration for Split Installation Upgrade

The `default_master.properties` file handles the configuration for the Split installation upgrade.

To configure the `default_master.properties` file for the Split installation upgrade:

-   Edit the `default_master.properties` file to configure settings specific to your database and application server.<br>
    Look for the line **Uncomment below settings ONLY for split installation** and uncomment the settings listed in the following table.

For example: To uncomment `# installType=split`, change it to `installType=split`.

The following table lists the settings you need to uncomment with sample values for each supported database.

<table>
<caption><p>Sample Values for the default_master.properties File for Split Installation</p></caption>
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
<td><p><code># installType=split</code></p>
<p><code># audit.dbHost=localhost</code></p>
<p><code># audit.dbUsername=postgres</code></p>
<p><code># audit.dbPassword=postgres</code></p>
<p><code># audit.dbPort=5432</code></p>
<p><code># audit.dbName=jsaudit</code></p></td>
</tr>
<tr>
<td><p>MySQL</p></td>
<td><p><code># installType=split</code></p>
<p><code># audit.dbHost=localhost</code></p>
<p><code># audit.dbUsername=root</code></p>
<p><code># audit.dbPassword=password</code></p>
<p><code># audit.dbPort=3306</code></p>
<p><code># audit.dbName=jsaudit</code></p></td>
</tr>
<tr>
<td><p>Oracle</p></td>
<td><p><code># installType=split</code></p>
<p><code># audit.dbHost=localhost</code></p>
<p><code># audit.dbUsername=jsaudit</code></p>
<p><code># audit.dbPassword=password</code></p>
<p><code># audit.dbPort=1521</code></p>
<p><code># audit.dbName=jsaudit</code></p>
<p><code># audit.sysUsername=system</code></p>
<p><code># audit.sysPassword=password</code></p>
<p><code># audit.sid=ORCL</code></p>
<p>If you are using an Oracle service name instead of an SID:</p>
<p><code># audit.serviceName=</code>: uncomment and add your service name.</p>
<p>If you are using the TIOracle JDBC driver and need to use the SYS login role as <code>SYSDBA</code>, you must configure the connection property as:</p>
<p><code># audit.AdditionalAdminProperties=;SysLoginRole=SYSDBA;User=sys;Password=password</code></p></td>
</tr>
<tr>
<td><p>DB2</p></td>
<td><p><code># installType=split</code></p>
<p><code># audit.dbHost=localhost</code></p>
<p><code># audit.dbUsername=db2admin</code></p>
<p><code># audit.dbPassword=password</code></p>
<p><code># audit.dbPort=50000</code></p>
<p><code># audit.dbName=JSAUDIT</code></p>
<p>For DB2, the <code>audit.dbName</code> value must be in uppercase.</p></td>
</tr>
<tr>
<td><p>SQL Server</p></td>
<td><p><code># installType=split</code></p>
<p><code># audit.dbHost=localhost</code></p>
<p><code># audit.dbUsername=sa</code></p>
<p><code># audit.dbPassword=sa</code></p>
<p><code># audit.dbPort=1433</code></p>
<p><code># audit.dbName=jsaudit</code></p></td>
</tr>
</tbody>
</table>

!!! note

    Note the following:

    If the `installType=split` property is not configured, the installation upgrade will be compact.

    The `audit.dbPort` property is specific to the database. You can change the values for other properties as required.

Each `sample_conf/<dbType>_master.properties` file contains the properties and appropriate sample values.
