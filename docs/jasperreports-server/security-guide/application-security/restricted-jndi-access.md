---
title: Enabling JNDI Security
description: "When you have read-write access to huge volumes of data at your disposal, you can retrieve, modify, copy, or move data anytime. This increases the risk of data corruption and reduces data security...."
---

# Enabling JNDI Security

When you have read-write access to huge volumes of data at your disposal, you can retrieve, modify, copy, or move data anytime. This increases the risk of data corruption and reduces data security. It is imperative to restrict access to check the sanity and quality of data. On enabling JNDI security, read-only access is provided to data sources.

You can enable JNDI security for data sources that are already deployed on JasperReports Server. However, you must manually migrate the data sources to a secure setup. You can also enable JNDI security when deploying JasperReports Server on Tomcat or JBoss EAP or Wildfly. For details, see the JasperReports® Server Installation Guide.

You can enable JNDI restricted security to JasperReports Serverdata sources with the following setting:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th colspan="2"><p>JNDI Restricted Access</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="2"><p><code>.../WEB-INF/classes/hibernate.properties</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>metadata.hibernate.jndi.restrictedAccess.enabled</code></p></td>
<td><p>Can be set to:</p>
<ul>
<li><p><code>true</code></p></li>
<li><p><code>false</code></p></li>
</ul>
<p>By default, it is set to <code>false</code>, implying that the connection to all JNDI data sources is successful.</p>
<p>However, if set to <code>true</code>, connection to only the JNDI restricted data sources is successful, and, connection to JNDI non-restricted data sources fails.</p></td>
</tr>
</tbody>
</table>

When installing JasperReports Server manually or when setting `metadata.hibernate.jndi.restrictedAccess.enabled` to `true`, the user must update the data sources using the `jdbc/jasperserver` or the `jdbc/jasperserverAudit` connections to access older resources. The following list offers the sample data sources:

- Audit data source: `jdbc/jasperserverAudit`
- Jasperserver repository SQL data source: `jdbc/jasperserver`
- Jasperserver data source: `jdbc/jasperserver`
- Profile data source JNDI:` jdbc/jasperserver`
- Report monitoring data source: `jdbc/jasperserverAudit`
- Jasperserver SQL data source: `jdbc/jasperserver`

The sample JNDI data sources must be edited to use JNDI restricted data sources.

| Current name             | New name                           |
|--------------------------|------------------------------------|
| `jdbc/jasperserver`      | `jdbc/jasperserverSystemAnalytics` |
| `jdbc/jasperserverAudit` | `jdbc/jasperserverAuditAnalytics`  |

## Impact on Datasource, Domains, and Reports

If metadata.hibernate.jndi.restrictedAccess.enabled=false

| JNDI name | Permission | Create Datasource, Domains, and Reports | View Reports |
|----|----|----|----|
| `jasperserver` | Read-write | Yes | Yes |
| `jasperserverAudit` | Read-write | Yes | Yes |
| `jasperserverSystemAnalytics` | Read-only | Yes | Yes |
| `jasperserverAuditAnalytics` | Read-only | Yes | Yes |

If metadata.hibernate.jndi.restrictedAccess.enabled=true

| JNDI name | Permission | Create Datasource, Domains, and Reports | View Reports |
|----|----|----|----|
| `jasperserver` | Read-write | No | No |
| `jasperserverAudit` | Read-write | No | No |
| `jasperserverSystemAnalytics` | Read-only | Yes | Yes |
| `jasperserverAuditAnalytics` | Read-only | Yes | Yes |
