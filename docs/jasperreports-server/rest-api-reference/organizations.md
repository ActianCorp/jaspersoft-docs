---
title: The organizations Service
description: "This section describes functionality that can be restricted by the software license for JasperReports Server. If you don’t see some of the options described in this section, your license may prohibit..."
---

# The organizations Service

!!! info "Important"

    This section describes functionality that can be restricted by the software license for JasperReports Server. If you don’t see some of the options described in this section, your license may prohibit you from using them. To find out what you're licensed to use, or to upgrade your license, contact Jaspersoft.

The rest_v2/organizations service provides methods that allow you to list, view, create, modify, and delete organizations (also known as tenants). Search functionality allows you to find organizations by name and retrieve hierarchies of organizations.

Because the organization ID is used in the URL, this service can operate only on organizations whose ID is less than 100 characters long and does not contain spaces or special symbols. As with resource IDs, the organization ID is permanent and cannot be modified for the life of the organization.

Only administrative users may access the organizations service. System admins (`superuser`) can operate on top-level organizations, and organization admins (`jasperadmin`) can operate on their own organization or any suborganizations.

This chapter includes the following sections:

-   [Searching for Organizations](#searching-for-organizations)
-   [Viewing an Organization](#viewing-an-organization)
-   [Creating an Organization](#creating-an-organization)
-   [Modifying Organization Properties](#modifying-organization-properties)
-   [Setting the Theme of an Organization](#setting-the-theme-of-an-organization)
-   [Deleting an Organization](#deleting-an-organization)

## Searching for Organizations

The GET method without any organization ID searches for organizations by ID, alias, or display name. If no search is specified, it returns a list of all organizations. Searches and listings start from but do not include the logged-in user’s organization or the specified base (`rootTenantId`).

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
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/<span>rest_v2/organizations</span>?&lt;arguments&gt;</span></p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><span>q</span></td>
<td><p>Optional<br />
String</p></td>
<td colspan="2"><p>Specify a string or substring to match the organization ID, alias, or name of any organization. The search is not case-sensitive. Only the matching organizations are returned in the results, regardless of their hierarchy.</p></td>
</tr>
<tr>
<td><span>include<br />
Parents</span></td>
<td><p>Optional<br />
Boolean</p></td>
<td colspan="2"><p>When used with a search, the result includes the parent hierarchy of each matching organization. When not specified, this argument is false by default.</p></td>
</tr>
<tr>
<td><span>rootTenantId</span></td>
<td><p>Optional<br />
String</p></td>
<td colspan="2"><p>Specifies an organization ID as a base for searching and listing child organizations. The base is not included in the results. Regardless of this base, the <code>tenantFolderURI</code> values in the result are always relative to the logged-in user’s organization. When not specified, the default base is the logged-in user’s organization.</p></td>
</tr>
<tr>
<td><span>sortBy</span></td>
<td><p>Optional<br />
String</p></td>
<td colspan="2"><p>Specifies a sort order for results. When not specified, lists of organizations are in the order that they were created. The possible values are:</p>
<p><span>name</span> - Sort results alphabetically by organization name.</p>
<p><span>alias</span> - Sort results alphabetically by organization alias.</p>
<p><span>id</span> - Sort results alphabetically by organization ID.</p></td>
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
<td colspan="3"><p>200 OK - The content is a set of descriptors for all organizations in the result.</p>
<p>204 No Content - The search did not return any organizations.</p></td>
<td></td>
</tr>
</tbody>
</table>

The following example shows a search for an organization and its parent hierarchy:

GET http://localhost:8080/jasperserver-pro/rest_v2/organizations?q=acc&includeParents=true

This request has the following response, as viewed by the superuser at the root of the organization hierarchy:

``` xml
<organizations>
  <organization>
    <alias>Finance</alias>
    <id>Finance</id>
    <parentId>organizations</parentId>
    <tenantDesc></tenantDesc>
    <tenantFolderUri>/organizations/Finance</tenantFolderUri>
    <tenantName>Finance</tenantName>
    <tenantUri>/Finance</tenantUri>
    <theme>default</theme>
  </organization>

  <organization>
    <alias>Accounts</alias>
    <id>Accounts</id>
    <parentId>Finance</parentId>
    <tenantDesc></tenantDesc>
    <tenantFolderUri>/organizations/Finance/organizations/Accounts</tenantFolderUri>
    <tenantName>Accounts</tenantName>
    <tenantUri>/Finance/Accounts</tenantUri>
    <theme>default</theme>
  </organization>
</organizations>
```

## Viewing an Organization

The GET method with an organization ID retrieves a single descriptor containing the list of properties for the organization. When you specify an organization, use its unique ID, not its path.

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
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/<span>rest_v2/organizations</span>/organizationID</span></p></td>
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
<td colspan="3"><p>200 OK - The content is the descriptor for the given organization.</p></td>
<td><p>404 Not Found - When the ID does not match any organization. The content includes an error message.</p>
<p>403 Forbidden - When the logged-in user does not have permission to view the given organization</p></td>
</tr>
</tbody>
</table>

The organization descriptor is identical to the one returned when searching or listing an organization, but only a single descriptor is ever returned. The following example shows the descriptor in JSON format:

``` json
{
  "id":"Finance",
  "alias":"Finance",
  "parentId":"organizations",
  "tenantName":"Finance",
  "tenantDesc":" ",
  "tenantNote":null,
  "tenantUri":"/Finance",
  "tenantFolderUri":"/organizations/Finance",
  "theme":"default"
}
```

## Creating an Organization

To create an organization, put all information in an organization descriptor, and include it in a POST request to the organizations service, with no ID specified in the URL. The organization is created in the organization specified by the `parentId` value of the descriptor.

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
<td><p>POST</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/<span>rest_v2/organizations</span>?&lt;argument&gt;</span></p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><span>create<br />
Default<br />
Users</span></td>
<td><p>Optional<br />
Boolean</p></td>
<td colspan="2"><p>Set this argument to false to suppress the creation of default users (<code>joeuser</code>, <code>jasperadmin</code>) in the new organization. When not specified, the default behavior is true and organizations are created with the standard default users.</p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/xml</span></p>
<p><span>application/json</span></p></td>
<td colspan="2"><p>A partial or complete organization descriptor that includes the desired properties for the organization.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>201 Created - The organization was successfully created using the values in the descriptor or default values if missing.</p></td>
<td><p>404 Not Found - When the ID of the parent organization cannot be resolved.</p>
<p>400 Bad Request - When the ID or alias of the new organization is not unique on the server, or when the ID in the description contains illegal symbols. The following symbols are not allowed:</p>
<p><span>id</span> and <span>alias</span>: <code>~!+-#$%^|</code></p>
<p><span>tenantName</span>: <code>|&amp;*?&lt;&gt;/\</code></p></td>
</tr>
</tbody>
</table>

The descriptor sent in the request should contain all the properties you want to set on the new organization. Specify the `parentId` value to set the parent of the organization, not the `tenantUri` or `tenantFolderUri` properties. The following example shows the descriptor in JSON format:

``` json
{
  "id":"Audit",
  "alias":"Audit",
  "parentId":"Finance",
  "tenantName":"Audit",
  "tenantDesc":"Audit Department of Finance",
  "theme":"default"
}
```

However, all properties have defaults or can be determined based on the alias value. The minimal descriptor necessary to create an organization is simply the alias property. In this case, the organization is created as a child of the logged-in user’s home organization. For example, if the `superuser` posts the following descriptor, the server creates an organization with the name, ID, and alias of HR as a child of the root organization:

``` json
{
  "alias":"HR"
}
```

## Modifying Organization Properties

To modify the properties of an organization, use the PUT method and specify the organization ID in the URL. The request must include an organization descriptor with the values you want to change. You cannot change the ID of an organization, only its name (used for display) and its alias (used for logging in).

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
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/<span>rest_v2/organizations</span>/organizationID/</span></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/xml</span></p>
<p><span>application/json</span></p></td>
<td colspan="2"><p>A partial organization descriptor that includes the properties to change. Do not specify the following properties:</p>
<ul>
<li><code>id</code> - The organization ID is permanent and can never be modified.</li>
<li><code>parentId</code> - Organizations cannot change parents.</li>
<li><code>tenantUri</code> - Organizations cannot change the organization hierarchy.</li>
<li><code>tenantFolderUri</code> - The organization folder is automatically based on its parent, which cannot be changed.</li>
</ul></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The organization was successfully updated.</p></td>
<td><p>400 Bad Request – When some dependent resources cannot be resolved.</p></td>
</tr>
</tbody>
</table>

The following example shows a descriptor sent to update the name and description of an organization:

``` json
{
  "tenantName":"Audit Dept",
  "tenantDesc":"Audit Department of Finance Division"
}
```

## Setting the Theme of an Organization

A theme determines how the JasperReports Server interface appears to users. The administrator can create and set different themes for each organization. To set a theme through web services, use the PUT method of the REST organizations service to modify the corresponding property of the desired organization.

For example:

PUT http://localhost:8080/jasperserver-pro/rest_v2/organizations/Audit

``` json
{
  "theme":"jasper_dark"
}
```

For more information about the themes, see the JasperReports Server Administrator Guide.

## Deleting an Organization

To delete an organization, use the DELETE method and specify the organization ID in the URL. When deleting an organization, all of its resources in the repository, all of its suborganizations, all of its users, and all of its roles are permanently deleted.

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
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/<span>rest_v2/organizations</span>/organizationID/</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>204 No Content - The organization was successfully deleted.</p></td>
<td><p>400 Bad Request - When attempting to delete the organization of the logged-in user.</p>
<p>404 Not Found - When the ID of the organization cannot be resolved.</p></td>
</tr>
</tbody>
</table>
