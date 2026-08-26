---
title: "Roles, Users, and Attributes"
description: "Domain security can reference a user’s roles to determine the access permissions to grant. The following roles meet CZS’s needs:"
---

# Roles, Users, and Attributes

## Roles

Domain security can reference a user’s roles to determine the access permissions to grant. The following roles meet CZS’s needs:

-   ROLE_SALES_MANAGER is assigned to sales managers.
-   ROLE_SALES_REP is assigned to sales representatives.

CZS grants each role access to view the Sales Domain. For details about creating roles and assigning privileges, refer to the JasperReports Server Administrator Guide. The following shows CZS’s ROLE_SALES_REP:

![js CZS Roles](../assets/images/js-CZS-Roles.png)

*Figure 1: CZS Sales Representative Role*

## Users

CZS created a user for each of their employees and assigned roles based on each employee’s level of responsibility:

| User   | Role               |
|--------|--------------------|
| Alexi  | ROLE_SALES_MANAGER |
| Pete   | ROLE_SALES_REP     |
| Rita   | ROLE_SALES_MANAGER |
| Yasmin | ROLE_SALES_REP     |

For details about creating users, refer to the JasperReports Server Administrator Guide.

## User Attributes

A user attribute is a name-value pair defined at the user level that corresponds to some data in a Domain. CZS wants to be able to describe their users in terms of product lines that they sell and the cities where they sell them. So each user is assigned two attributes in addition to a role:

-   The `Cities` profile attribute corresponds to the City field in the Geography item group in the Sales Domain.
-   The `ProductDepartment` attribute corresponds to the Department field in the Product item group in the Sales Domain.

<table>
<caption><p>UserAttributes of All CZS Users</p></caption>
<thead>
<tr>
<th rowspan="2"><p>User</p></th>
<th colspan="2"><p>Profile Attributes</p></th>
</tr>
<tr>
<th><p>Cities</p></th>
<th><p>Product/Department</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Rita</p></td>
<td><p>San Francisco, Los Angeles, Sacramento</p></td>
<td><p>Television, Wireless Devices</p></td>
</tr>
<tr>
<td><p>Pete</p></td>
<td><p>San Francisco</p></td>
<td><p>Television</p></td>
</tr>
<tr>
<td><p>Yasmin</p></td>
<td><p>San Francisco</p></td>
<td><p>Wireless Devices</p></td>
</tr>
<tr>
<td><p>Alexi</p></td>
<td><p>Osaka, Sakai</p></td>
<td><p>Wireless Devices</p></td>
</tr>
</tbody>
</table>

When these attributes are used in the security file in an access grant definition, each user’s attributes determine the data returned for them by the Domain. For example, Rita’s attribute value for `Cities` is `San Francisco, Los Angeles, Sacramento`. So she sees data for all those cities.

The following figure shows the configuration of Rita’s user account. Notice Rita’s attributes listed below her roles:

![js CZS Users](../assets/images/js-CZS-Users.png)

*Figure 2: CZS User Rita’s Configuration*
