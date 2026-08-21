---
title: Configuring Other Database Connections
description: "Use these settings to connect to a database other than PostgreSQL using the database vendor's driver."
---

# Configuring Other Database Connections

## Configuring Databases Drivers

Use these settings to connect to a database other than PostgreSQL using the database vendor's driver.

### Configuring a MySQL Connection

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Database Setting</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Host</p></td>
<td><p>localhost</p></td>
</tr>
<tr>
<td><p>Name or SID</p></td>
<td><p>For JasperServerDataBase: jasperserver</p>
<p>For AuditDataBase:</p>
<ul>
<li>For Compact installation: jasperserver</li>
<li>For Split installation: jsaudit</li>
</ul></td>
</tr>
<tr>
<td><p>User</p></td>
<td><p>root</p></td>
</tr>
<tr>
<td><p>Password</p></td>
<td><p>password</p></td>
</tr>
<tr>
<td><p>Port</p></td>
<td><p>3306</p></td>
</tr>
<tr>
<td>characterEncoding</td>
<td>UTF-8</td>
</tr>
<tr>
<td>autoReconnect</td>
<td>true</td>
</tr>
<tr>
<td>tinyInt1isBit</td>
<td>false</td>
</tr>
<tr>
<td>autoReconnectForPools</td>
<td>true</td>
</tr>
<tr>
<td><p>Hibernate Dialect</p></td>
<td><p>MySQLInnoDBDialect</p></td>
</tr>
<tr>
<td><p>Quartz Driver Delegate</p></td>
<td><p>StdJDBCDelegate</p></td>
</tr>
</tbody>
</table>

Enter the following for **Test Table Name** in [Step 19](weblogic_install_procedure.md):

| Parameter Name | JasperReports Server | JasperReports Server Audit | JasperServerSystemDataBase | AuditAnalyticsDataBase | Foodmart | Sugar CRM |
|----|----|----|----|----|----|----|
| Name | JasperServerDataBase | AuditDataBase | Jasper Server System DataBase | Audit Analytics DataBase | FoodmartDataBase | SugarcrmDataBase |
| User | root | root | jasperuser | jasperuser | foodmart | sugarcrm |
| Test Table Name | JIReportJob | JIAuditEvent | JIReportJob | JIAuditEvent | account | accounts |

### Configuring an Oracle Connection

To use the Oracle driver, enter the following properties:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Database Setting</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Host</p></td>
<td><p>localhost</p></td>
</tr>
<tr>
<td><p>Name or SID</p></td>
<td><p>Orcl</p></td>
</tr>
<tr>
<td><p>User</p></td>
<td><p>For JasperServerDataBase: jasperserver</p>
<p>For AuditDataBase:</p>
<ul>
<li>For Compact installation: jasperserver</li>
<li>For Split installation: jsaudit</li>
</ul></td>
</tr>
<tr>
<td><p>Password</p></td>
<td><p>password</p></td>
</tr>
<tr>
<td><p>Port</p></td>
<td><p>1521</p></td>
</tr>
<tr>
<td><p>Hibernate Dialect</p></td>
<td><p>OracleJICustomDialect</p></td>
</tr>
<tr>
<td><p>Quartz Driver Delegate</p></td>
<td><p>StdJDBCDelegate</p></td>
</tr>
</tbody>
</table>

Enter the following for **Test Table Name** in [Step 19](weblogic_install_procedure.md):

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
<td>AuditDataBase</td>
<td>Jasper Server System DataBase</td>
<td>Audit Analytics DataBase</td>
<td><p>FoodmartDataBase</p></td>
<td><p>SugarcrmDataBase</p></td>
</tr>
<tr>
<td>User</td>
<td>jasperserver</td>
<td>For Compact installation: jasperserver<br />
For Split installation: jsaudit</td>
<td>jasperuser</td>
<td>jasperuser</td>
<td>foodmart</td>
<td>sugarcrm</td>
</tr>
<tr>
<td><p>Test Table Name</p></td>
<td><p>DUAL</p></td>
<td>DUAL</td>
<td>DUAL</td>
<td>DUAL</td>
<td><p>DUAL</p></td>
<td><p>DUAL</p></td>
</tr>
</tbody>
</table>

### Configuring a DB2 Connection

To use the DB2 driver, enter the properties below.

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
<th>Database Setting</th>
<th>JasperReports<br />
Server</th>
<th>JasperReports Server Audit</th>
<th>Foodmart</th>
<th>Sugar CRM</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Host</p></td>
<td colspan="4"><p>localhost</p></td>
</tr>
<tr>
<td><p>Name or SID</p></td>
<td><p>JSPRSRVR</p></td>
<td>For Compact installation: JSPRSRVR<br />
For Split installation: JSAUDIT</td>
<td>foodmart</td>
<td>sugarcrm</td>
</tr>
<tr>
<td>currentSchema</td>
<td>JSPRSRVR</td>
<td>For Compact installation: JSPRSRVR<br />
For Split installation: JSAUDIT</td>
<td>FOODMART</td>
<td>SUGARCRM</td>
</tr>
<tr>
<td><p>User</p></td>
<td colspan="4"><p>db2inst1</p></td>
</tr>
<tr>
<td><p>Password</p></td>
<td colspan="4"><p>password</p></td>
</tr>
<tr>
<td><p>Port</p></td>
<td colspan="4"><p>50000</p></td>
</tr>
<tr>
<td><p>Hibernate Dialect</p></td>
<td colspan="4"><p>DB2JICustomDialect</p></td>
</tr>
<tr>
<td><p>Quartz Driver Delegate</p></td>
<td colspan="4"><p>DB2v8Delegate</p></td>
</tr>
</tbody>
</table>

Enter the following for **Test Table Name** in [Step 19](weblogic_install_procedure.md):

| Parameter Name | JasperReports Server | JasperReports Server Audit | Foodmart | Sugar CRM |
|----|----|----|----|----|
| Name | JasperServerDataBase | AuditDataBase | FoodmartDataBase | SugarcrmDataBase |
| User | db2inst1 | db2inst1 | foodmart | sugarcrm |
| Test Table Name | JIREPORTJOB | JIREPORTJOB | ACCOUNT | ACCOUNTS |

### Configuring a SQL Server Connection

To use the SQL Server driver, enter the following properties:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Database Setting</th>
<th><p>SQL Server</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Host</p></td>
<td><p>localhost</p></td>
</tr>
<tr>
<td><p>Name or SID</p></td>
<td><p>For JasperServerDataBase:</p>
<p>jasperserver</p>
<p>For AuditDataBase:</p>
<ul>
<li>For Compact installation: jasperserver</li>
<li>For Split installation: jsaudit</li>
</ul></td>
</tr>
<tr>
<td><p>User</p></td>
<td><p>sa</p></td>
</tr>
<tr>
<td><p>Password</p></td>
<td><p>sa</p></td>
</tr>
<tr>
<td><p>Port</p></td>
<td><p>1433</p></td>
</tr>
<tr>
<td><p>Hibernate Dialect</p></td>
<td><p>SQLServerJICustomDialect</p></td>
</tr>
<tr>
<td><p>Quartz Driver Delegate</p></td>
<td><p>StdJDBCDelegate</p></td>
</tr>
</tbody>
</table>

Enter the following for **Test Table Name** in [Step 19](weblogic_install_procedure.md):

| Parameter Name | JasperReports Server | JasperReports Server Audit | JasperServerSystemDataBase | AuditAnalyticsDataBase | Foodmart | Sugar CRM |
|----|----|----|----|----|----|----|
| Name | JasperServerDataBase | AuditDataBase | JasperServer System DataBase | Audit Analytics DataBase | FoodmartDataBase | SugarcrmDataBase |
| User | sa | sa | jasperuser | jasperuser | foodmart | sugarcrm |
| Test Table Name | jireportjob | jireportjob | jireportjob | jireportjob | account | accounts |
