---
title: The roles Service
description: "The restv2/roles service provides methods that allow you to list, view, create, modify, and delete roles. The service provides improved search functionality, including user-based role searches. Every..."
---

# The roles Service

The rest_v2/roles service provides methods that allow you to list, view, create, modify, and delete roles. The service provides improved search functionality, including user-based role searches. Every method has two URL forms, one with an organization ID and one without.

Only administrative users may access the roles service. System admins (`superuser`) can define and set roles anywhere in the server, and organization admins (`jasperadmin`) can define and set roles within their own organization or any suborganizations.

Because the role ID and organization ID are used in the URL, this service can operate only on roles and organizations whose ID is less than 100 characters long and does not contain spaces or special symbols. Unlike resource IDs, the role ID is the role name and can be modified.

This chapter includes the following sections:

-   Searching for Roles
-   Viewing a Role
-   Creating a Role
-   Modifying a Role
-   Setting Role Membership
-   Deleting a Role

## Searching for Roles

The GET method without any role ID searches for and lists role definitions. It has options to search for roles by name or by user that belongs to the role. If no search is specified, it returns all roles. The method has two forms:

-   In the community edition of the server, or commercial editions without organizations, use the first form of the URL without an organization ID.
-   In commercial editions with organizations, use the first URL to search or list all roles starting from the logged-in user’s organization (root for the system admin), and use the second URL to search or list all roles in a specified organization.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>GET</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/roles</span>?&lt;arguments&gt;</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/organizations</span>/orgID/<span>roles</span>?&lt;arguments&gt;</span></p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><span>search</span></p></td>
<td><p>Optional<br />
String</p></td>
<td colspan="2"><p>Specify a string or substring to match the role ID (name) of any role. The search is not case-sensitive.</p></td>
</tr>
<tr>
<td><p><span>user</span></p></td>
<td><p>Optional<br />
String</p></td>
<td colspan="2"><p>Specify a username (ID) to list the roles to which this user belongs. Repeat this argument to list all roles of multiple users. In commercial editions with multiple organizations, specify users as <span>&lt;userID&gt;%7C&lt;orgID&gt;</span> (<span>%7C</span> is the | character).</p></td>
</tr>
<tr>
<td><p><span>hasAllUsers</span></p></td>
<td><p>Optional<br />
Boolean</p></td>
<td colspan="2"><p>When set to true with multiple user arguments, this method returns only the roles to which all specified users belong (intersection of all users' roles). When false or not specified, all roles of all specified users are found (union of all users' roles).</p></td>
</tr>
<tr>
<td><p><span>include<br />
SubOrgs</span></p></td>
<td><p>Optional<br />
Boolean</p></td>
<td colspan="2"><p>Limits the scope of the search or list in commercial editions with multiple tenants. When set to false, the first URL form is limited to the logged-in user’s organization, and the second URL form is limited to the organization specified in the URL. When true or not specified, the scope includes the hierarchy of all child organizations.</p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p><span>accept: application/xml</span> (default)</p>
<p><span>accept: application/json</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK - The content is a set of descriptors for all roles in the result.</p>
<p>204 No Content - The search did not return any roles.</p></td>
<td><p>404 Not Found - When the organization ID does not match any organization. The content includes an error message.</p></td>
</tr>
</tbody>
</table>

The following example shows the first form URL on a commercial edition server with multiple organizations:

GET http://localhost:8080/jasperserver/rest_v2/roles

This method returns the set of all default system and root roles defined on a server with the sample data (no organization roles have been defined yet):

``` xml
<roles>
  <role>
    <externallyDefined>false</externallyDefined>
    <name>ROLE_ADMINISTRATOR</name>
  </role>
  <role>
    <externallyDefined>false</externallyDefined>
    <name>ROLE_ANONYMOUS</name>
  </role>
  <role>
    <externallyDefined>false</externallyDefined>
    <name>ROLE_DEMO</name>
  </role>
  <role>
    <externallyDefined>false</externallyDefined>
    <name>ROLE_PORTLET</name>
  </role>
  <role>
    <externallyDefined>false</externallyDefined>
    <name>ROLE_SUPERMART_MANAGER</name>
  </role>
  <role>
    <externallyDefined>false</externallyDefined>
    <name>ROLE_SUPERUSER</name>
  </role>
  <role>
    <externallyDefined>false</externallyDefined>
    <name>ROLE_USER</name>
  </role>
</roles>
```

!!! note

    The `externallyDefined` property is true when the role is synchronized from a 3rd party such as an LDAP directory or Single Sign-On mechanism. For more information, see the JasperReports Server External Authentication Cookbook.

## Viewing a Role

The GET method with a role ID retrieves a single role descriptor containing the role properties.

-   In the community edition of the server, or commercial editions without organizations, use the first form of the URL.
-   In commercial editions with organizations, use the second URL to specify the role’s organization. When specifying the organization, use its unique ID, not its path. When logged in as the system admin (`superuser`), use the first URL to specify the roles of the root organization.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>GET</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/roles</span>/roleID</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/organizations</span>/orgID/<span>roles</span>/roleID</span></p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p><span>accept: application/xml</span> (default)</p>
<p><span>accept: application/json</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK - The content is the descriptor for the given role.</p></td>
<td><p>404 Not Found - When the role ID or organization ID does not match any role or organization. The content includes an error message.</p></td>
</tr>
</tbody>
</table>

After adding roles to an organization, the following example shows the simple role descriptor for an organization role in JSON format:

GET http://localhost:8080/jasperserver-pro/rest_v2/organizations/Finance/roles/ROLE_MANAGER

``` json
{
  "name":"ROLE_MANAGER",
  "externallyDefined":false,
  "tenantId":"Finance"
}
```

## Creating a Role

To create a role, send the PUT request to the roles service with the intended role ID (name) specified in the URL.

-   In the community edition of the server, or commercial editions without organizations, use the first form of the URL.
-   In commercial editions with organizations, use the second URL to specify the user’s organization. When specifying the organization, use its unique ID, not its path. When logged in as the system admin (`superuser`), use the first URL to create roles in the root organization.

Roles do not have any properties to specify other than the role ID, but the request must include a descriptor that can be empty.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>PUT</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/roles</span>/roleID</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/organizations</span>/orgID/<span>roles</span>/roleID</span></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/xml</span></p>
<p><span>application/json</span></p></td>
<td colspan="2"><p>An empty role descriptor, either <span>&lt;role&gt;&lt;/role&gt;</span> or <span></span>. The role descriptor has the following properties, but they are not needed:</p>
<ul>
<li><code>name</code> - The roleID value in the URL takes precedence, and any value in the descriptor is ignored.</li>
<li><code>tenantID</code> - The orgID value in the URL takes precedence, and any value in the descriptor is ignored.</li>
<li><code>externallyDefined</code> - The <code>externallyDefined</code> property is true when the role is synchronized from a 3rd party such as an LDAP directory. If you omit this property, its default value is false. If you include it, it must be set to false.</li>
</ul></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>201 Created - The role was successfully created. The response contains the full descriptor of the new role.</p></td>
<td><p>404 Not Found - When the organization ID cannot be resolved.</p></td>
</tr>
</tbody>
</table>

## Modifying a Role

To change the name of a role, send a PUT request to the roles service and specify the new name in the role descriptor.

-   In the community edition of the server, or commercial editions without organizations, use the first form of the URL.
-   In commercial editions with organizations, use the second URL to specify the user’s organization. When specifying the organization, use its unique ID, not its path. When logged in as the system admin (`superuser`), use the first URL to modify roles in the root organization.

The only property of a role that you can modify is the role's name, which is also its roleID. After the update, all members of the role are members of the new role name, and all permissions associated with the old role name are updated to the new role name.

!!! note

    Only repository permissions based on the role are updated to the new role name. If you have domain security files based on the role name, they must be updated manually by uploading a modified security file. For more information, see the JasperReports Server Data Management Using Domains.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>PUT</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/roles</span>/roleID</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/organizations</span>/orgID/<span>roles</span>/roleID</span></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/xml</span></p>
<p><span>application/json</span></p></td>
<td colspan="2"><p>A role descriptor that needs only the <code>name</code> property:</p>
<ul>
<li><code>name</code> - The new name for the role, which also becomes its new roleID.</li>
<li><code>tenantID</code> - The orgID value in the URL takes precedence, and any value in the descriptor is ignored.</li>
<li><code>externallyDefined</code> - The <code>externallyDefined</code> property is true when the role is synchronized from a 3rd party such as an LDAP directory. If you omit this property, its default value is false. If you include it, it must be set to false.</li>
</ul></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK - The role was successfully updated. The response contains the full descriptor of the updated role.</p></td>
<td><p>404 Not Found - When the organization ID cannot be resolved.</p></td>
</tr>
</tbody>
</table>

## Setting Role Membership

To assign role membership to a user, set the roles property on the user account with the PUT method of the users service. For details, see [1.1, “Modifying User Properties,” on page 1](users.md).

## Deleting a Role

To delete a role, send the DELETE method and specify the role ID (name) in the URL.

-   In the community edition of the server, or commercial editions without organizations, use the first form of the URL.
-   In commercial editions with organizations, use the second URL to specify the user’s organization. When specifying the organization, use its unique ID, not its path. When logged in as the system admin (`superuser`), use the first URL to delete the roles of the root organization.

When this method is successful, the role is permanently deleted.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>DELETE</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/roles</span>/roleID</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/organizations</span>/orgID/<span>roles</span>/roleID</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>204 No Content - The role was successfully deleted.</p></td>
<td><p>404 Not Found - When the ID of the organization cannot be resolved.</p></td>
</tr>
</tbody>
</table>
