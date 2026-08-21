---
title: Protecting Against SQL Injection
description: "SQL injection is an attack that uses malicious SQL queries in reports to gain access or do damage to your databases. By default, JasperReports Server validates query strings to protect against SQL..."
---

# Protecting Against SQL Injection

SQL injection is an attack that uses malicious SQL queries in reports to gain access or do damage to your databases. By default, JasperReports Server validates query strings to protect against SQL injection.

Whenever the server runs an SQL query, the server validates the query string with the following rules:

- SQL queries must start with SELECT.
- Queries may not contain INTO clauses.
- Queries may call stored procedures (CALL command used by JDBC drivers).
- Multiple queries separated by semi-colons (`;`) are also prohibited.
- SQL comments are allowed, but will be removed before being transmitted.

If your reports or Domains use such queries, you need to either change your queries or update the security configuration to allow them.

Users who run a report with a query that does not meet the rules see an error. Administrators can monitor the server logs to search for evidence of attempted security breaches.

SQL query validation is enabled by default when installing JasperReports Server. To turn off this protection, edit the following file:

<table>
<thead>
<tr>
<th colspan="3"><p>SQL Query Validation</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>.../WEB-INF/classes/esapi/security-config.properties</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Default Value</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>security.validation.sql.on</code></p></td>
<td><p><code>true</code></p></td>
<td><p>Turns SQL query validation on or off in the server. Any other value besides "<code>case-insensitive=false</code>” is equivalent to true.</p></td>
</tr>
</tbody>
</table>

!!! warning

    SQL query validation rules were added to comply with security guidelines for web applications. Turning off query validation or modifying the validation rules may make the server more vulnerable to web attacks.

## Customizing the Error Message

When query validation blocks a query that violates a security rule, the server displays an error in the UI. By default, security messages are intentionally generic to avoid alerting potential attackers to security errors.

We highly recommend that external deployments customize the security error message to be unique, yet still generic. You can change both the message and the error number. Choose any combination of numbers or letters so administrators can easily search the logs to detect security violations.

<table>
<thead>
<tr>
<th colspan="2"><p>Query Validation Messages</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="2"><p><code>.../WEB-INF/bundles/security.properties</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Default Value</p></td>
</tr>
<tr>
<td><p><code>message.validation.sql</code></p></td>
<td><p><code>An error has occurred. Please contact your system administrator. (6632)</code></p></td>
</tr>
</tbody>
</table>

If you translate your application into other languages, be sure to create a locale-specific copy of this file and translate these messages as well.

## Understanding Query Validation

Query validation uses a mechanism to validate every SQL query before running it. The validation process is defined by a validation rule that references a validator expression. The rule and the expression are defined in separate files.

!!! note

    The `security.properties` and `validation.properties` files contain many validation rules and expressions. These were used for general input validation in the server, but this mechanism is deprecated and no longer used. Only the expressions for SQL validation are still applicable.

<table>
<thead>
<tr>
<th colspan="2"><p>Query Validation Rule</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="2"><p><code>.../WEB-INF/classes/esapi/security.properties </code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Default Value</p></td>
</tr>
<tr>
<td><p><code>sqlQueryExecutor</code></p></td>
<td><p><code>Alpha,ValidSQL,500000,true,SQL_Query_Executor_context</code></p></td>
</tr>
</tbody>
</table>

The validation rule contains five comma-separated values:

- `Alpha` – Not used for query validation.
- `ValidSQL` – The name of the SQL validator expression in the other file.
- `500000` – The maximum length allowed for the query.
- `true` – Whether the query can be blank.
- `SQL_Query_Executor_context` – Context string for log messages.

<table>
<thead>
<tr>
<th colspan="2"><p>SQL Validator Expression</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="2"><p><code>.../WEB-INF/classes/esapi/validation.properties </code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Default Value</p></td>
</tr>
<tr>
<td><p><code>Validator.ValidSQL</code></p></td>
<td><p><code>(?is)^\\s*(select|call)\\b((?!\\b(into|delete|update|drop)\\b)[^;]);?s$</code></p></td>
</tr>
</tbody>
</table>

!!! note

    The default value for the *Validator.ValidSQL* property is a single-line string:<br>
    `(?is)^\\s*(select|call)\\b((?!\\b(into|delete|update|drop)\\b)[^;]);?s$`

The validator expression is a regular expression that must match the query string. The default expression enforces the following:

- Queries may only use the SELECT statement, which is read-only. The following write statements are forbidden: `DROP, INSERT, UPDATE, DELETE`
- SELECT statements may not use the INTO clause that could copy data.
- CALL statements for stored procedures are allowed.
- Multiple queries separated by semi-colons (`;`) will be rejected. The following example causes a security error: `SELECT f1,f2 FROM tbl_1; SELECT f3 from tbl_2;`

!!! warning

    The rule and validator expression are commented by default because the server implements the same SQL validation with an internal mechanism. If you wish to customize the SQL validation, uncomment the rule and create a validator expression as described below.

## Customizing Query Validation

If you wish to use a different validator expression for queries, always create a validator expression with a new name in `validation.properties`. Then substitute that name in the validation rule in `security.properties`. For example, if you wish to forbid queries from running stored procedures in your database, add the following validator expression in `validation.properties`:

```
#Validator.ValidSQL=(?is)^\\s*(select|call)\\b((?!\\binto\\b)[^;])*;?\\s*$
Validator.ValidSQLnoProc=(?is)^\\s*(select)\\b((?!\\binto\\b)[^;])*;?\\s*$
```

Then you would uncomment and modify the validation rule in `security.properties` as follows:

```
# Main SQL execution point
sqlQueryExecutor=Alpha,ValidSQLnoProc,500000,true,SQL_Query_Executor_context
```

It is also possible to have two or more validation rules that are applied sequentially (logical AND) until one fails. The rules must have the same name but with a numerical suffix, for example:

```
# Main SQL execution point
sqlQueryExecutor=Alpha,ValidSQL,500000,true,SQL_Query_Executor_context
sqlQueryExecutor2=Alpha,ValidSQLCustom,500000,true,SQL_Custom_Executor_context
```

!!! note

    With multiple rules for query validation, each rule is applied in the order listed until one fails. When one rule fails, the whole validation fails.

## Performance Issues

By default, the internal SQL validation mechanism accesses the query metadata to allow semicolons (`;`) in the data part of the query, for example in table names. This access can cause a performance issues with certain JDBC drivers, in which case you can disable it as follows:

<table>
<thead>
<tr>
<th colspan="3"><p>Advanced Input Validation</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>.../WEB-INF/classes/esapi/security-config.properties</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Default Value</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>validate.sql.via.metadata.query.execution</code></p></td>
<td><p>true</p></td>
<td><p>Set this value to false to disable semicolon checking in query metadata if SQL validation causes performance issues with your JDBC driver.</p></td>
</tr>
</tbody>
</table>

# Further Security Configuration

The security configuration file contains other default security settings. In particular, they can warn you when a security file has a syntax error and could not be loaded. Changing these defaults is possible but not recommended:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>Advanced Input Validation</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>.../WEB-INF/classes/esapi/security-config.properties</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Default Value</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>log.msg.security.off</code></p></td>
<td><p>SECURITY for [%s] is OFF</p></td>
<td><p>If security is turned OFF, this message is logged. This message in the logs can alert administrators if the security configuration has been tampered with.</p></td>
</tr>
<tr>
<td><p><code>msg.cannot.load</code></p></td>
<td><p>Security configuration [%s]<br />
cannot be loaded.</p></td>
<td><p>If there is an error in the security configuration files, this message is logged. This is a severe error and should be resolved by the administrator.</p></td>
</tr>
</tbody>
</table>
