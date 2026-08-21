---
title: Configuring Report Scheduling
description: The JasperReports Server report scheduling feature is powered by the Quartz scheduler tool. Buildomatic automatically handles configuration settings for Quartz-based report scheduling.
---

# Configuring Report Scheduling

The JasperReports Server report scheduling feature is powered by the Quartz scheduler tool. Buildomatic automatically handles configuration settings for Quartz-based report scheduling.

In a deployed JasperReports Server instance, you will find the `js.quartz.properties` file in this location:

`<app-server-path>/` `jasperserver` `-pro` `/WEB-INF/js.quartz.properties`

For mail server configuration, you will find an additional property setting for authentication in this file:

`<app-server-path>/webapps/` `jasperserver` `-pro` `/WEB-INF/applicationContext-report-scheduling.xml`

The following configurations are discussed in this section:

- Mail Server Configuration
- Quartz Driver Delegate Class
- Report Scheduler Web URI
- Quartz Table Prefix
- Settings for import-export
- Setting Properties in the `default_master.properties` file
- Settings for Skipping Calendar Job Execution Immediately After Import

## Mail Server Configuration Settings

You can specify email addresses to be notified when a report run is complete. To do this, configure JasperReports Server to contact an email server. The email server can be contacted via mail or by using a graph API.

!!! note

    By default, JasperReports Server uses mail to contact an email server. To change it to:

    - Graph API: In the `js.quartz.properties` file, set `emailService.type=graph`.

    - SendGrid: In the `js.quartz.properties` file, set `emailService.type=sendGrid`.

### Mail Server Configuration Settings Using E-mail

The following table provides the configuration information to contact an email server via mail:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>&lt;app-server&gt;/&lt;deployment&gt;/WEB-INF/js.quartz.properties</code></p></td>
</tr>
<tr>
<td colspan="2"><p>Property</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td colspan="2"><p><code>report.scheduler.mail.sender.host</code></p></td>
<td><p>The name of the computer hosting the mail server.</p></td>
</tr>
<tr>
<td colspan="2"><p><code>report.scheduler.mail.sender.username</code></p></td>
<td><p>The name of the mail server the user JasperReports Server can use.</p></td>
</tr>
<tr>
<td colspan="2"><p><code>report.scheduler.mail.sender.password</code></p></td>
<td><p>The password of the mail server user.</p></td>
</tr>
<tr>
<td colspan="2"><p><code>report.scheduler.mail.sender.from</code></p></td>
<td><p>The address for the <code>From</code> field on email notifications.</p></td>
</tr>
<tr>
<td colspan="2"><p><code>report.scheduler.mail.sender.protocol</code></p></td>
<td><p>The protocol that the mail server uses. JasperReports Server supports only SMTP.</p>
<p>Note: Your entry must be lower case (<code>smtp</code>).</p></td>
</tr>
<tr>
<td colspan="2"><p><code>report.scheduler.mail.sender.port</code></p></td>
<td><p>The port number that the mail server uses. The default is typically 25 (other ports may not work in earlier JasperReports Server versions).</p></td>
</tr>
<tr>
<td colspan="3"><p>**Note** - `host ,username, port` and `password` are mandatory parameters. If any of these parameters are missed, a bean is created with the default values provided in the `js.quartz.properties` file. - If `protocol` is missed, it will set to the default value, which is `SMTP`. - If the `from `address is missed, it picks the value from the `js.quartz.properties` file.</p></td>
</tr>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>&lt;app-server&gt;/&lt;deployment&gt;/WEB-INF/applicationContext-report-scheduling.xml</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Bean</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>javaMailProperties key="mail.smtp.auth"</code></p></td>
<td><p><code>reportScheduler</code></p>
<p><code>MailSender</code></p></td>
<td><p>If your mail server requires authentication, change this property from <code>false</code> to <code>true</code>.</p></td>
</tr>
</tbody>
</table>

### Mail Server Configuration Settings Using Graph API

### Prerequisite for Azure Graph API login

The following are the prerequisites for Azure Graph API login:

1.  Register JasperReports Server as an application on the Azure portal.

2.  Obtain the details for **Resource Owner** flow and **Client Credentials** flow.

3.  For **Resource Owner** flow, obtain the following details:

    1.  Username

    2.  Password

4.  For **Client Credentials** flow, obtain the following details:

    1.  `Client ID`

    2.  `Client Secret`

    3.  `User ID`

    4.  `Tenant ID`

5.  Define the **Mailbox Permissions and Scope**.

    Ensure that the following permissions are defined in the scope:

    1.  **Mailbox**

    2.  **Mail.Send**

    3.  **Mail.ReadWrite**

6.  Obtain the `resourceGroupName` configured for Azure SQL.

The following table provides the configuration information to contact an email server using a graph API:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td colspan="2"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="2"><p><code>&lt;app-server&gt;/&lt;deployment&gt;/WEB-INF/js.quartz.properties</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>emailService.graph.oauthUrl</code></p></td>
<td><p>The URL of the mail server.</p></td>
</tr>
<tr>
<td><p><code>emailService.graph.oauthClientId</code></p></td>
<td><p>The unique application or client ID assigned to JasperReports Server by Azure Active Directory (AD).</p></td>
</tr>
<tr>
<td><p><code>emailService.graph.oauthSecret</code></p></td>
<td><p>A secret string that the application uses to identify itself while requesting a token.</p></td>
</tr>
<tr>
<td><p><code>emailService.graph.oauthTenantId</code></p></td>
<td><p>An instance of Azure AD.</p></td>
</tr>
<tr>
<td><p><code>emailService.graph.oauthUserName</code></p></td>
<td><p>The username to connect to Azure.</p></td>
</tr>
<tr>
<td><p><code>emailService.graph.oauthPassword</code></p></td>
<td><p>The password to connect to Azure.</p></td>
</tr>
<tr>
<td><code>emailService.graph.oauthUserId</code></td>
<td>The unique object ID using which JasperReports Server is registered.</td>
</tr>
<tr>
<td><code>clientSecretCredentialFlow</code></td>
<td><p>The authentication is done either by providing the <code>clientSecret</code> or by providing the username and password.</p>
<p>Depending on the authentication you want to use, set <code>emailService.graph.clientSecretCredentialFlow</code> to <code>true </code>or <code>false</code>. If <code>emailService.graph.clientSecretCredentialFlow=true</code>, <code>clientSecret</code> is used for authentication. If set to <code>false</code>, the username and password are used for authentication.</p>
<p>**Note** - For `clientsecretcredential` flow, `clientId, tenantid, clientsecret` and `userid `are mandatory parameters. - For `username and password` flow, `clientid, username` and `password `are mandatory parameters. If any of the mandatory parameters are missed, a bean is created using the default values mentioned in the `js.quartz.properties` file.</p></td>
</tr>
<tr>
<td><code>azureSql.resourceGroupName</code></td>
<td>To fetch the list of databases, the resource group is required while creating AzureSqlManagementService bean. By default, it is set to <code>defaultResourceGroup</code>.</td>
</tr>
</tbody>
</table>

The bean for graph API is created only when the graph profile is enabled in `web.xml`. By default, the 'graph' profile in the `web.xml` file is disabled to prevent unnecessary bean creation. To enable the 'graph' profile:

```
<context-param>
<param-name>spring.profiles.active</param.name>
<param-value>default,engine,alerting-ie,jrs,graph</param.value>
</context-param>
```

### Mail Server Configuration Settings Using SendGrid API

### Prerequisite for SendGrid API

The following are the prerequisites for SendGrid API login:

1.  Create an account on [Twilio SendGrid](https://sendgrid.com/en-us).

2.  Create the SendGrid API key and set the access rights.

3.  Complete domain authentication.

The following table provides the configuration information to schedule alerts and jobs using a SendGrid API:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td colspan="2"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="2"><p><code>&lt;app-server&gt;/&lt;deployment&gt;/WEB-INF/js.quartz.properties</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><code>emailService.type</code></td>
<td><p>The email service type to be used.</p>
<p>Change it to <code>sendGrid</code>.</p></td>
</tr>
<tr>
<td><code>sendGrid.api</code></td>
<td>The API key created on SendGrid portal.</td>
</tr>
<tr>
<td><code>report.scheduler.mail.sender.from</code></td>
<td>The email ID of the authenticated sender on SendGrid portal.</td>
</tr>
<tr>
<td colspan="2"><p>**Note** The API key and the sender email ID are mandatory for sending and receiving email using SendGrid.</p></td>
</tr>
</tbody>
</table>

!!! note

    Following are the limitations while using the SendGrid API:

    - The total size of the email, including attachments, cannot exceed 30 MB.

    - The total number of recipients cannot be more than 1,000. This includes recipients in **to, cc**, and **bcc**, and each object included in personalization.

    - The total length of custom arguments must be less than 10,000 bytes.

    - Unicode encoding is not supported for the **from** field.

    - `;` and **,** are not allowed in the `to.name` , `cc.name` , and `bcc.name` personalization.

## Database Settings for the Quartz Driver Delegate Class

Quartz uses the Quartz driver delegate class to interact with the JDBC driver.

!!! note

    If you used buildomatic to install JasperReports Server, the correct value of the Quartz driver delegate class is automatically set for your database.

If you did not use buildomatic to install JasperReports Server, refer to the following table to edit the `js.quartz.properties` file and set the value of the Quartz driver delegate class to the correct value for your database.

<table>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>&lt;app-server&gt;/&lt;deployment&gt;/WEB-INF/js.quartz.properties</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Database</p></td>
<td><p>Value</p></td>
</tr>
<tr>
<td rowspan="5"><code>quartz.delegateClass</code></td>
<td><p>MySQL</p></td>
<td><code>org.quartz.impl.jdbcjobstore.StdJDBCDelegate</code></td>
</tr>
<tr>
<td><p>PostgreSQL</p></td>
<td><code>org.quartz.impl.jdbcjobstore.PostgreSQLDelegate</code></td>
</tr>
<tr>
<td><p>DB2</p></td>
<td><code>org.quartz.impl.jdbcjobstore.DB2v8Delegate</code></td>
</tr>
<tr>
<td><p>Oracle</p></td>
<td><code>org.quartz.impl.jdbcjobstore.StdJDBCDelegate</code></td>
</tr>
<tr>
<td><p>SQL Server<sup>1</sup></p></td>
<td><code>org.quartz.impl.jdbcjobstore.StdJDBCDelegate</code></td>
</tr>
</tbody><tfoot>
<tr>
<td colspan="3"><p>For SQL Server on WebSphere 8.5 use <code>org.quartz.impl.jdbcjobstore.MSSQLDelegate</code></p></td>
</tr>
</tfoot>
&#10;</table>

## Settings for the Report Scheduler Web URI

JasperReports Server uses the Report Scheduler Web URI to construct the link it sends in the output of a scheduled job. This link must be correct for the user to access the report on the server.

The port on which you run JasperReports Server and the context root of the deployed JasperReports Server web application determine the report scheduler Web URI. The default context root is `jasperserver`.

To set this value manually, edit this file:

`<app-server>/<deployment>/WEB-INF/js.quartz.properties`.

Change the properties as shown in the following table.

<table>
<tbody>
<tr>
<td><p>Property</p></td>
<td><p>App Server</p></td>
<td><p>Example Value</p></td>
</tr>
<tr>
<td rowspan="4"><code>report.scheduler.web.deployment.uri</code></td>
<td><p>Apache Tomcat</p></td>
<td><code>http://localhost:8080/</code><code>jasperserver</code><code> </code><code>-pro</code><code> </code></td>
</tr>
<tr>
<td><p>JBoss</p></td>
<td><code>http://localhost:8080/</code><code>jasperserver</code><code> </code><code>-pro</code><code> </code></td>
</tr>
<tr>
<td><p>WebLogic</p></td>
<td><code>http://localhost:7001/jasperserver-pro</code></td>
</tr>
<tr>
<td><p>WebSphere</p></td>
<td><code>http://localhost:9080/jasperserver-pro</code></td>
</tr>
</tbody>
</table>

## Settings for the Quartz Table Prefix

For databases that support schemas, such as Oracle, SQL Server, and DB2, you can set the Quartz table prefix to include the schema, if you use one. In the default configuration, only DB2 requires an explicit schema name.

!!! note

    If you installed JasperReports Server using buildomatic, the Quartz table prefix is set automatically.

To set this value, edit the file `<app-server>/<deployment>/WEB-INF/js.quartz.properties`. Change the following property:

<table>
<tbody>
<tr>
<td colspan="2"><p>Property</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td colspan="2"><code>quartz.tablePrefix</code></td>
<td><p>The prefix for the quartz table, including any schema name<span>, for example <code>JSPRSRVR.QRTZ_</code> for DB2</span>.</p></td>
</tr>
</tbody>
</table>

## Settings for Import-Export

If you manually configure the import-export shell scripts instead of using the buildomatic, make sure your settings for the Quartz driver delegate class property are correct for your database.

!!! note

    If you install using buildomatic, these settings are handled automatically (in buildomatic import-export).

To configure the import-export scripts manually, edit this file:

`<js-install>/buildomatic/conf_source/``iePro`` /js.quartz.properties`

Change the following properties:

<table>
<tbody>
<tr>
<td colspan="2"><p>Property</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td colspan="2"><code>quartz.delegateClass</code></td>
<td><p>Set to the same value as described in <span>Database Settings for the Quartz Driver Delegate Class</span>.</p></td>
</tr>
<tr>
<td colspan="2"><code>quartz.tablePrefix</code></td>
<td><p>Set to the same value as described in <span>Settings for the Quartz Table Prefix</span>.</p></td>
</tr>
</tbody>
</table>

## Setting Properties in the default_master.properties File

You can modify the `default_master.properties` file to configure the JasperReports Server functionality. Uncomment the properties that you want to have them take effect on installation. The properties are documented directly in the `default_master.properties` file:

`<js-install>/buildomatic/default_master.properties`

You will find a sample master.properties here (in the case of PostgreSQL):

`<js-install>/buildomatic/sample_conf/postgresql_master.properties`

When you run the `js-install`` .sh/bat` script (or the underlying `deploy-webapp-``pro`` ` ant target), these properties will be set in the deployed JasperReports Server in the `js.quartz.properties` file.

You can set the following properties in default_master.properties file (default values are shown):

- `notification.service.multiTenant.config=none`

- `emailService.type=mail`

- `calenderTrigger.resetStartTimeOnImport=false`

- `simpleTrigger.resetStartTimeOnImport=false`

### Report Scheduler Email Properties

You can set the following properties to configure the Report Scheduler email (default values are shown):

`quartz.mail.sender.host=mail.localhost.com`

`quartz.mail.sender.port=25`

`quartz.mail.sender.protocol=smtp`

`quartz.mail.sender.username=admin`

`quartz.mail.sender.password=password`

`quartz.mail.sender.from=admin@localhost.com`

`quartz.web.deployment.uri=http://localhost:8080/``jasperserver`` ``-pro`` `

For information about the Prerequisite for Azure Graph API login, see Mail Server Configuration Settings Using Graph API.

You can set the following properties to configure the Report Scheduler email using a graph API (default values are shown):

`emailService.graph.oauthUrl=https://graph.microsoft.com`

`emailService.graph.oauthClientId=oauthClientId`

`emailService.graph.oauthSecret=oauthSecret`

`emailService.graph.oauthTenantId=oauthTenantId`

`emailService.graph.oauthUserName=username`

`emailService.graph.oauthPassword=password`

`emailService.graph.oauthUserId=oauthUserId`

`emailService.graph.clientSecretCredentialFlow=true`

`azureSql.resourceGroupName=defaultResourceGroup`

!!! note

    When sending a file with email:

    - If the file size is under 3 MB, graph uses single POST.

    - If the file size is in between 3MB and 150 MB it uses the largeAttachment upload flow.

    For details, refer to [Outlook-Large-Attachments](https://learn.microsoft.com/en-us/graph/outlook-large-attachments).

For information about properties to be set when composing email, refer to the *Setting Properties in the jasperserver_config.properties File* section in the JasperReports® Server Administrator Guide.

### Diagnostic Properties

The following properties configure the Diagnostic functionality:

`diagnostic.jmx.usePlatformServer = false`

`diagnostic.jmx.port = 10990`

`diagnostic.jmx.name = jasperserver`

`diagnostic.jmx.rmiHost = localhost`

Look at the descriptions of the properties in the `default_master.properties` file and also refer to the *JasperReports Server Administrator Guide* for more information on these settings.

### Settings to Skip Calendar Job Execution Immediately After Import

When importing scheduled jobs, all calendar jobs with misfired triggers are re-executed. This results in unwanted and unplanned executions. This can be overcome by changing the Misfire policy on the server. But, that will impact all other jobs along with the calendar trigger.

To avoid this, you can add two new properties `calenderTrigger.resetStartTimeOnImport` and `simpleTrigger.resetStartTimeOnImport` to stop executing calendar jobs immediately after import.

These properties, when set to `false`, skip executing calendar jobs right after import. The job is executed at the next trigger (calendar or simple). On setting the properties to `true`, the start time of the job is reset to the current time and it is not considered as misfired after the import.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th colspan="2"><p>Configuring Scheduler Misfire Policy</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Property</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>calenderTrigger.resetStartTimeOnImport</code></p></td>
<td>By default, <code>calenderTrigger.resetStartTimeOnImport=false</code>. If set to <code>true</code>, then while importing the job, start time is recalculated to the import time. And, the job execution starts in the future based on the condition set in calendar trigger.</td>
</tr>
<tr>
<td><code>simpleTrigger.resetStartTimeOnImport</code></td>
<td><p>By default, <code>simpleTrigger.resetStartTimeOnImport=false</code>. If set to <code>true</code>, then job start time is refreshed to current time.</p>
<p>**Note** For old jobs with simple triggers that were completed, but remained in the system, the jobs are executed again because the start time recalculated to the current time.</p></td>
</tr>
</tbody>
</table>
