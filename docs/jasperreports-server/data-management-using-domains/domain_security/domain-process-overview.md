---
title: Process Overview
description: The table below summarizes the steps CZS could take to create the Sales Domain and configure it to secure their data using user attributes and roles.
---

# Process Overview

The table below summarizes the steps CZS could take to create the Sales Domain and configure it to secure their data using user attributes and roles.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>Steps</p></th>
<th><p>Described in…</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><ol>
<li>Define a Domain. The CZS business case is met by a Sales Domain that includes the following fields from their JDBC data source: city, state, product department, sales amount, cost amount, and unit sales.</li>
</ol></td>
<td><p><a href="sales-domain.md">Sales Domain</a></p></td>
</tr>
<tr>
<td><ol>
<li>Identify and create access roles. CZS needs two roles: one for managers, and another for sales representatives. Both are granted access to the Sales Domain.</li>
</ol></td>
<td><p><a href="roles-users-attributes.md">Roles</a></p></td>
</tr>
<tr>
<td><ol>
<li>Create users and assign appropriate roles to each one.</li>
</ol></td>
<td><p><a href="roles-users-attributes.md">Users</a></p></td>
</tr>
<tr>
<td><ol>
<li>Identify and create attributes that determine each user’s access to data in the Domain. CZS needs two attributes: <code>Cities</code> and <code>ProductDepartment</code>.</li>
</ol></td>
<td><p><a href="roles-users-attributes.md">User Attributes</a></p></td>
</tr>
<tr>
<td><ol>
<li>Prepare to test the security implementation by enabling logging and creating an example report.</li>
</ol></td>
<td><p><a href="domain-security-testing.md">Setting Up Logging and Testing</a></p></td>
</tr>
<tr>
<td><ol>
<li>Iteratively create, upload, and test an XML file that defines the access granted to users based on the attributes defined in <span>step 4</span>.</li>
</ol></td>
<td><p><a href="creating-a-security-file.md">Creating a Domain Security File</a></p></td>
</tr>
<tr>
<td><ol>
<li>Test the Domain as various users.</li>
</ol></td>
<td><p><a href="verfiying-domain-security.md">Testing and Results</a></p></td>
</tr>
</tbody>
</table>
