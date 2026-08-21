---
title: The users Service
description: "The restv2/users service provides methods that allow you to list, view, create, modify, and delete user accounts, including setting role membership. The service provides improved search..."
---

# The users Service

The rest_v2/users service provides methods that allow you to list, view, create, modify, and delete user accounts, including setting role membership. The service provides improved search functionality, such as organization-based searches in commercial editions licensed to use organizations. Every method has two URL forms, one with an organization ID and one without.

Only administrative users may access the users service. System admins (`superuser`) can define and modify users anywhere in the server, and organization admins (`jasperadmin`) can define and modify users within their own organization or any sub-organizations.

Because the user ID and organization ID are used in the URL, this service can operate only on users and organizations whose ID is fewer than 100 characters long and does not contain spaces or special symbols. As with resource IDs, the user ID is permanent and cannot be modified for the life of the user account.

This chapter includes the following sections:

- Searching for Users
- Viewing a User
- Creating a User
- Modifying User Properties
- Deleting a User

## Searching for the Users

The GET method without any user ID searches for and lists user accounts. It has options to search for users by name or by role. If no search is specified, it returns all users. The method has two forms:

- In the community edition of the server, or commercial editions without organizations, use the first form of the URL without an organization ID.
- In commercial editions with organizations, use the first URL to list all users starting from the logged-in user’s organization (root for the system admin), and use the second URL to list all users in a specified organization.

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
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/users</span>?&lt;arguments&gt;</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/organizations</span>/orgID/<span>users</span>?&lt;arguments&gt;</span></p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><span>search</span></td>
<td><p>Optional<br />
String</p></td>
<td colspan="2"><p>Specify a string or substring to match the user ID or full name of any user. The search is not case-sensitive.</p></td>
</tr>
<tr>
<td><span>requiredRole</span></td>
<td><p>Optional<br />
String</p></td>
<td colspan="2"><p>Specify a role name to list only users with this role. Repeat this argument to filter with multiple roles. In commercial editions with multiple organizations, specify roles as <span>&lt;roleName&gt;%7C&lt;orgID&gt;</span> (<span>%7C</span> is the | character).</p></td>
</tr>
<tr>
<td><span>hasAll<br />
Required<br />
Roles</span></td>
<td><p>Optional<br />
Boolean</p></td>
<td colspan="2"><p>When set to false with multiple <span>requiredRole</span> arguments, users match if they have any of the given roles (OR operation). When true or not specified, users must match all given roles (AND operation).</p></td>
</tr>
<tr>
<td><span>include<br />
SubOrgs</span></td>
<td><p>Optional<br />
Boolean</p></td>
<td colspan="2"><p>Limits the scope of the search or list in commercial editions with multiple organizations. When set to false, the first URL form is limited to the logged-in user’s organization, and the second URL form is limited to the organization specified in the URL. When true or not specified, the scope includes the hierarchy of all child organizations.</p></td>
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
<td colspan="3"><p>200 OK: The content is a set of descriptors for all users in the result.</p>
<p>204 No Content: The search did not return any users.</p></td>
<td><p>404 Not Found: When the organization ID does not match any organization. The content includes an error message.</p></td>
</tr>
</tbody>
</table>

The following example shows the first form of the URL on a community edition server:

GET http://localhost:8080/jasperserver/rest_v2/users?search=j

The response is a set of summary descriptors for all users containing the string "j":

```
<users>
  <user>
    <externallyDefined>false</externallyDefined>
    <fullName>jasperadmin User</fullName>
    <username>jasperadmin</username>
  </user>
  <user>
    <externallyDefined>false</externallyDefined>
    <fullName>Joe User</fullName>
    <username>joeuser</username>
  </user>
</users>
```

The next example shows the second form of the URL on a commercial edition server with multiple organizations:

GET http://localhost:8080/jasperserver/rest_v2/organizations/Finance/users

On servers with multiple organizations, the summary user descriptors include the organization (tenant) ID. As shown in the following example, the same username may exist in different organizations:

```
<users>
  <user>
    <externallyDefined>false</externallyDefined>
    <fullName>jasperadmin</fullName>
    <tenantId>Finance</tenantId>
    <username>jasperadmin</username>
  </user>
  <user>
    <externallyDefined>false</externallyDefined>
    <fullName>jasperadmin</fullName>
    <tenantId>Audit</tenantId>
    <username>jasperadmin</username>
  </user>
  <user>
    <externallyDefined>false</externallyDefined>
    <fullName>Joe User</fullName>
    <tenantId>Finance</tenantId>
    <username>joeuser</username>
  </user>
  <user>
    <externallyDefined>false</externallyDefined>
    <fullName>Joe User</fullName>
    <tenantId>Audit</tenantId>
    <username>joeuser</username>
  </user>
</users>
```

!!! note

    The `externallyDefined` property is true when the user is synchronized from a 3rd party such as an LDAP directory or Single Sign-on. For more information, see the JasperReports Server External Authentication Cookbook.

## Viewing a User

The GET method with a user ID (`username`) retrieves a single descriptor containing the full list of user properties and roles.

- In the community edition of the server, or commercial editions without organizations, use the first form of the URL.
- In commercial editions with organizations, use the second URL to specify the user’s organization. When specifying the organization, use its unique ID, not its path. When logged in as the system admin (`superuser`), use the first URL to specify users of the root organization.

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
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/users</span>/userID</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/organizations</span>/orgID/<span>users</span>/userID</span></p></td>
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
<td colspan="3"><p>200 OK: The content is the descriptor for the given user.</p></td>
<td><p>404 Not Found: When the user ID or organization ID does not match any user or organization. The content includes an error message.</p></td>
</tr>
</tbody>
</table>

The full user descriptor includes detailed information about the user account, including any roles. The following example shows the descriptor in XML format:

GET http://localhost:8080/jasperserver/rest_v2/users/joeuser

```
<user>
  <enabled>true</enabled>
  <externallyDefined>false</externallyDefined>
  <fullName>Joe User</fullName>
  <previousPasswordChangeTime>2013-04-19T18:53:07.602-07:00
  </previousPasswordChangeTime>
  <roles>
    <role>
      <externallyDefined>false</externallyDefined>
      <name>ROLE_USER</name>
    </role>
  </roles>
  <username>joeuser</username>
</user>
```

In servers with multiple organizations, the full descriptor includes the organization (tenant) ID. The following example shows the descriptor in JSON format:

GET http://localhost:8080/jasperserver/rest_v2/organizations/Finance/users/joeuser

```
{
  "fullName":"joeuser",
  "emailAddress":"",
  "externallyDefined":false,
  "enabled":true,
  "previousPasswordChangeTime":1366429181984,
  "tenantId":"Finance",
  "username":"joeuser",
  "roles":[
    {"name":"ROLE_USER","externallyDefined":false}]
}
```

## Creating a User

To create a user account, put all required information in a user descriptor, and include it in a PUT request to the users service, with the intended user ID (username) specified in the URL.

- In the community edition of the server, or commercial editions without organizations, use the first form of the URL.
- In commercial editions with organizations, use the second URL to specify the user’s organization. When specifying the organization, use its unique ID, not its path. When logged in as the system admin (`superuser`), use the first URL to create users in the root organization.

To create a user, the user ID in the URL must be unique on the server or in the organization. If the user ID exists, that user account is modified, as described in 1.1, “Modifying User Properties,” on page 1.

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
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/users</span>/userID</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/organizations</span>/orgID/<span>users</span>/userID</span></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/xml</span></p>
<p><span>application/json</span></p></td>
<td colspan="2"><p>A user descriptor that includes at least the <code>fullName</code> and <code>password</code> for the user. Even if the <code>username</code> and <code>tenantID</code> are specified in the descriptor, their values in the URL take precedence. See the table below for other properties in the user descriptor.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>201 Created: The user was successfully created using the values in the descriptor. The response contains the full descriptor of the new user.</p></td>
<td><p>404 Not Found: When the organization ID cannot be resolved.</p></td>
</tr>
</tbody>
</table>

The user descriptor includes the following properties when being sent for creating or updating a user:

| Property | Description |
|----|----|
| `username` | This can be omitted because the `userID` in the URL takes precedence. If a value is specified, it has no effect. |
| `tenantID` | This can be omitted because the `orgID` in the URL takes precedence. If a value is specified, it has no effect. |
| `fullName` | A string giving the name of the user that appears in the user interface, for example `Joe User`. This property is required when creating a user. |
| `password` | A string giving the password of the user. This property is required when creating a user. |
| `emailAddress` | The email address is optional, but when specified, the user can receive notifications such as when a scheduled report is available. |
| `roles` | The roles are optional because ROLE_USER is automatically assigned to all users and does not need to be specified. To assign further roles to the user, specify an array of roles with the `name` and `tenantId` properties. See the example below. |
| `enabled` | When false, the user cannot log in. If this property is omitted during user creation, its value is true (enabled) by default. Set this value to false if you want to create the user but not allow access to the server yet. |
| `previousPasswordChangeTime` | This property is set automatically by the server. Any value submitted in the descriptor is ignored. |
| `externallyDefined` | The `externallyDefined` property is true when the user is synchronized from a 3rd party such as an LDAP directory or Single Sign-on. When creating a user through the REST API, this property should be set to false. For more information, see the JasperReports Server External Authentication Cookbook. |

The following example shows the user descriptor in JSON format:

```
{
  "fullName":"Joe User",
  "emailAddress":"juser@example.com",
  "externallyDefined":false,
  "enabled":false,
  "password":"mySecretPassword",
  "roles":[
    {"name":"ROLE_MANAGER", "tenantId":"organization_1"}]
}
```

## Modifying User Properties

To modify the properties of a user account, put all desired information in a user descriptor, and include it in a PUT request to the users service, with the existing user ID (username) specified in the URL. See the properties of the descriptor in the table above.

- In the community edition of the server, or commercial editions without organizations, use the first form of the URL.
- In commercial editions with organizations, use the second URL to specify the user’s organization. When specifying the organization, use its unique ID, not its path. When logged in as the system admin (`superuser`), use the first URL to modify users of the root organization.

To modify a user, the user ID in the URL must exist on the server or in the organization. If the user ID does not exist, a user account is created, as described in 1.1, “Creating a User,” on page 1.

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
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/users</span>/userID</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/organizations</span>/orgID/<span>users</span>/userID</span></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/xml</span></p>
<p><span>application/json</span></p></td>
<td colspan="2"><p>A user descriptor that includes the properties you want to change. The <code>username</code> and <code>tenantID</code> properties have no effect in the descriptor. Their values in the URL always take precedence. For other properties, see the table in <span>Creating a User</span>.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK: The user properties were successfully updated.</p></td>
<td><p>404 Not Found: When the organization ID cannot be resolved.</p></td>
</tr>
</tbody>
</table>

To add a role to the user, specify the entire list of roles with the desired role added. To remove a role from a user, specify the entire list of roles with the desired role removed. The following example shows the descriptor in JSON format:

```
{
  "enabled":true,
  "password":"newPassword",
  "roles":[
    {"name":"ROLE_USER"},
    {"name":"ROLE_STOREMANAGER", "tenantId":"organization_1"}]
}
```

## Deleting a User

To delete a user, send the DELETE method and specify the user ID in the URL.

- In the community edition of the server, or commercial editions without organizations, use the first form of the URL.
- In commercial editions with organizations, use the second URL to specify the user’s organization. When specifying the organization, use its unique ID, not its path. When logged in as the system admin (`superuser`), use the first URL to delete users of the root organization.

When this method is successful, the user is permanently deleted.

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
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/users</span>/userID</span></p>
<p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/organizations</span>/orgID/<span>users</span>/userID</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>204 No Content: The user was successfully deleted.</p></td>
<td><p>404 Not Found: When the ID of the organization cannot be resolved.</p></td>
</tr>
</tbody>
</table>
