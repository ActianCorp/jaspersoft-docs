---
title: Security Issues Fixed
description: "The following security issues have been fixed in this release of JasperReports Server:"
---

# Security Issues Fixed

The following security issues have been fixed in this release of JasperReports Server:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th>Key</th>
<th>Area of the Product Affected</th>
<th>Type of Vulnerability</th>
<th>Description and Impact on Users</th>
</tr>
</thead>
<tbody>
<tr>
<td>JS-69327</td>
<td>System JNDI data sources usage</td>
<td>Access to sensitive information</td>
<td><p>JNDI security now enables access control to data sources. The new version includes two new JNDI data sources, namely <code>jasperserverSystemAnalytics</code>, and <code>jasperserverAuditAnalytics</code>, both configured with read-only access. Administrators can enable access control to the jasperserver JNDIs by changing the <code>metadata.hibernate.jndi.restrictedAccess.enabled</code> property in hibernate properties.</p>
<p>For more information, see <em>JasperReports Server Administrator Guide</em> and <em>JasperReports Server Security Guide</em>.</p></td>
</tr>
<tr>
<td>JS-67049</td>
<td>Query execution via Domain Designer and REST API</td>
<td>Access to sensitive information</td>
<td>A fix has been implemented to address the security vulnerability. The configuration has been extended to enhance access control, ensuring better protection of sensitive information during query execution via Domain Designer and the REST API. For more information, the JasperReports Server Security Guide.</td>
</tr>
<tr>
<td>JS-67608</td>
<td>N/A</td>
<td>Dependency on third-party libraries</td>
<td><p>Upgraded woodstox-core and jackson to resolve following CVEs:</p>
<ul>
<li>CVE-2022-40152</li>
<li>CVE-2022-40153</li>
<li>CVE-2022-40154</li>
<li>CVE-2022-40155</li>
<li>CVE-2022-40156</li>
</ul></td>
</tr>
<tr>
<td>JS-70861</td>
<td>N/A</td>
<td>Dependency on third-party libraries</td>
<td><p>Upgraded activemq-client to resolve following CVE:</p>
<ul>
<li>CVE-2023-46604</li>
</ul></td>
</tr>
<tr>
<td>JS-70896</td>
<td>N/A</td>
<td>Dependency on third-party libraries</td>
<td><p>Upgraded snappy-java to resolve following CVEs:</p>
<ul>
<li>CVE-2023-34455</li>
<li>CVE-2023-34454</li>
</ul></td>
</tr>
<tr>
<td>JS-70077</td>
<td>N/A</td>
<td>Dependency on third-party libraries</td>
<td><p>Upgraded spring-core to 5.3.29 and spring-security to 5.7.10, sqlite-jdbc to 3.42.0.0, and removed dependency on quartz-commonj to resolve following CVEs:</p>
<ul>
<li>CVE-2022-31690</li>
<li>CVE-2022-31692</li>
<li>CVE-2023-20862</li>
<li>CVE-2019-13990</li>
<li>CVE-2023-32697</li>
</ul></td>
</tr>
<tr>
<td>JS-69762</td>
<td>N/A</td>
<td>Dependency on third-party libraries</td>
<td><p>Upgraded sqlite-jdbc to 3.42.0.0, and removed dependency on quartz-commonj to resolve following CVEs:</p>
<ul>
<li>CVE-2019-13990</li>
<li>CVE-2023-32697</li>
</ul></td>
</tr>
<tr>
<td>JS-69772</td>
<td>N/A</td>
<td>Dependency on third-party libraries</td>
<td><p>Upgraded accessors-smart, ftpserver-core, guava, jackson, removed dependency on snappy-java to resolve following CVEs:</p>
<ul>
<li>CVE-2023-1370</li>
<li>CVE-2023-22551</li>
<li>CVE-2023-2976</li>
<li>CVE-2022-45688</li>
<li>CVE-2023-35116</li>
<li>CVE-2022-45688</li>
<li>CVE-2023-34455</li>
<li>CVE-2023-34454</li>
<li>CVE-2023-34453</li>
</ul></td>
</tr>
<tr>
<td>JS-70098</td>
<td>N/A</td>
<td>Dependency on third-party libraries</td>
<td><p>Upgraded snowflake-jdbc, jjwt-api, json-path, mariadb-java-client to resolve following CVEs:</p>
<ul>
<li>CVE-2023-30535</li>
<li>CVE-2022-45688</li>
<li>CVE-2022-45688</li>
<li>CVE-2015-2325</li>
<li>CVE-2021-46669</li>
<li>CVE-2020-28912</li>
<li>CVE-2022-27449</li>
<li>CVE-2022-27385</li>
</ul></td>
</tr>
</tbody>
</table>
