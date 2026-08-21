---
title: Types Defined in the WSDL
description: "The WSDL (Web Services Description Language) document defines the types that are returned by operations of the services. The types belong to the http://www.jasperforge.org/jasperserver/ws namespace...."
---

# 1.1 Types Defined in the WSDL

The WSDL (Web Services Description Language) document defines the types that are returned by operations of the services. The types belong to the `http://www.jasperforge.org/jasperserver/ws` namespace. The namespace is only an identifier; it is not a valid URL. For the complete reference, refer to the WSDL document in jasperserver-ws-server-4.0.jar.

The following tables summarize the services’ operations.

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
<th colspan="5"><p>Users and Roles Service</p></th>
</tr>
<tr>
<th><p>Operation</p></th>
<th><p>Parameter</p></th>
<th><p>Parameter Type</p></th>
<th><p>Return Type</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>findUsers</code></p></td>
<td><p><code>criteria</code></p></td>
<td><p><code>WSUserSearchCriteria</code></p></td>
<td><p>WSUser[]</p></td>
<td><p>Returns a list of one or more users.</p>
<p><code>criteria</code> has username mask, organization/tenant ID, <code>includeSubOrgs</code>, list of required roles, and <code>maxRecords</code>; <code>null</code> in parameters means "any."</p>
<p>Note: <code>includeSubOrgs and tenantID</code> are reserved for use in our commercial products. If they are used in community project products, they must be <code>NULL</code>.</p></td>
</tr>
<tr>
<td><p><code>putUser</code></p></td>
<td><p><code>user</code></p></td>
<td><p><code>WSUser</code></p></td>
<td><p>WSUser</p></td>
<td><p>Adds or updates a user.</p>
<p>Returns the new or updated <code>WSUser</code>.</p></td>
</tr>
<tr>
<td><p><code>deleteUser</code></p></td>
<td><p><code>user</code></p></td>
<td><p><code>WSUser</code></p></td>
<td><p><span>No return</span></p></td>
<td><p>Deletes the named user.</p></td>
</tr>
<tr>
<td><p><code>findRoles</code></p></td>
<td><p><code>criteria</code></p></td>
<td><p><code>WSRoleSearchCriteria</code></p></td>
<td><p>WSRole[]</p></td>
<td><p>Returns <code>WSRole[]</code>, a list of roles.</p>
<p><code>criteria</code> has rolename mask, organization/tenant ID, <code>includeSubOrgs</code>, <code>maxRecords</code>; <code>null</code> in parameters means "any."</p>
<p>Note: <code>includeSubOrgs and tenantID</code> are reserved for use in our commercial products. If they are used in community project products, they must be <code>NULL</code>.</p></td>
</tr>
<tr>
<td><p><code>putRole</code></p></td>
<td><p><code>role</code></p></td>
<td><p><code>WSRole</code></p></td>
<td><p>WSRole</p></td>
<td><p>Adds or updates a role.</p>
<p>Returns new or updated <code>WSRole</code>.</p></td>
</tr>
<tr>
<td rowspan="2"><p>updateRoleName</p></td>
<td><p>oldRole</p></td>
<td><p>WSRole</p></td>
<td><p>WSRole</p></td>
<td><p>Returns <code>WSRole</code>.</p></td>
</tr>
<tr>
<td><p>newName</p></td>
<td><p>String</p></td>
<td><p>WSRole</p></td>
<td><p>New name of role.</p></td>
</tr>
<tr>
<td><p><code>deleteRole</code></p></td>
<td><p><code>role</code></p></td>
<td><p><code>WSRole</code></p></td>
<td><p><span>No return</span></p></td>
<td><p>Deletes the named role.</p></td>
</tr>
</tbody>
</table>

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
<th colspan="5"><p>Organizations/Tenants Service</p></th>
</tr>
<tr>
<th><p>Operation</p></th>
<th><p>Parameter</p></th>
<th><p>Parameter Type</p></th>
<th><p>Return Type</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>getTenant</code></p></td>
<td><p><code>tenantId</code></p></td>
<td><p><code>String</code></p></td>
<td><p>WSTenant[]</p></td>
<td><p>Organization/tenant identifier.</p>
<p>Returns an organization/tenant.</p></td>
</tr>
<tr>
<td><p><code>getSubTenantList</code></p></td>
<td><p><code>tenantId</code></p></td>
<td><p><code>String</code></p></td>
<td><p><code>WSTenant[]</code></p></td>
<td><p>Organization/tenant identifier.</p>
<p>Returns <code>WSTenant[]</code>, a list of suborganizations in the specified organization.</p></td>
</tr>
<tr>
<td><p><code>putTenant</code></p></td>
<td><p><code>tenant</code></p></td>
<td><p><code>WSTenant</code></p></td>
<td><p>WSTenant</p></td>
<td><p>Adds or updates a tenant.</p>
<p>Returns the new or updated <code>WSTenant</code>.</p></td>
</tr>
<tr>
<td><p><code>deleteTenant</code></p></td>
<td><p><code>tenantId</code></p></td>
<td><p><code>String</code></p></td>
<td><p>No return</p></td>
<td><p>Deletes the named organization/tenant.</p></td>
</tr>
</tbody>
</table>

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
<th colspan="5"><p>Permissions Service</p></th>
</tr>
<tr>
<th><p>Operation</p></th>
<th><p>Parameter</p></th>
<th><p>Parameter Type</p></th>
<th><p>Return Type</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>getPermissionsForObject</code></p></td>
<td><p><code>targetURI</code></p></td>
<td><p><code>String</code></p></td>
<td><p>WSObjectPermission[]</p></td>
<td><p>Repository object URI.</p>
<p>Returns <code>WSObjectPermission[]</code>, a list of permissions for the specified object.</p></td>
</tr>
<tr>
<td><p><code>putPermissions</code></p></td>
<td><p><code>objPerm</code></p></td>
<td><p><code>WSObjectPermission</code></p></td>
<td><p>WSObjectPermission</p></td>
<td><p>Object permission.</p>
<p>Returns <code>WSObjectPermission</code>, a new or updated object permission.</p></td>
</tr>
<tr>
<td><p><code>deletePermissions</code></p></td>
<td><p><code>objPerm</code></p></td>
<td><p><code>WSObjectPermission</code></p></td>
<td><p>No return</p></td>
<td><p>Deletes the named permission.</p></td>
</tr>
</tbody>
</table>
