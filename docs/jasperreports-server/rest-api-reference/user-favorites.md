---
title: Working With Favorites
description: "The restv2/favorites service provides methods that allow you to add the resources to Favorites for quick access, remove the resources from Favorites and see the starred resources in your list of..."
---

# Working With Favorites

The rest_v2/favorites service provides methods that allow you to add the resources to Favorites for quick access, remove the resources from Favorites and see the starred resources in your list of Favorites.

This chapter includes the following sections:

-   [Adding Resources to Favorites](#adding-resources-to-favorites)
-   [Removing Resources from Favorites](#removing-resources-from-favorites)
-   [Accessing Resources in Favorites](#accessing-resources-in-favorites)

## Adding Resources to Favorites

Use the following method to add the resources to Favorites.

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
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/favorites</span></span></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/json</span></p></td>
<td colspan="2"><p>A JSON object that contains the list of resource URIs to be added to Favorites.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>201 Created - The request was successful.</p></td>
<td><p>400 Bad Request - Invalid request syntax.<br />
403 Forbidden - When the logged-in user does not have permission to access the resource.<br />
404 Not Found - When the resource specified in the request does not exist.<br />
</p></td>
</tr>
</tbody>
</table>

The following is an example of a sample payload.

Sample Request Payload:

``` json
{
    "favorites":[
     {
        "uri":"/public/audit/datasources/AuditDataSource_1"
     },
     {
        "uri":"/public/audit/datasources/AuditVirtualDataSource_1"
     }
   ]
}
```

Sample Response Payload:

``` json
{
    "favorites":[
     {
        "uri":"/public/audit/datasources/AuditDataSource_1"
     },
     {
        "uri":"/public/audit/datasources/AuditVirtualDataSource_1"
     }
   ]
}
```

If a user adds a resource to the Favorites and later an admin removes the user's access to resources, the entry stays in the `jifavoriteresource` table, but the user will not be able to view or remove the resources from the Favorites.

!!! note

    Local resources cannot be added to Favorites.

## Removing Resources from Favorites

The following method is used to remove the starred resources from the Favorites.

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
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/favorites</span>/delete</span></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/json</span></p></td>
<td colspan="2"><p>A JSON object that contains the list of resource URIs to be deleted from Favorites.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>204 No Content - The request was successful.</p></td>
<td><p>400 Bad Request - Invalid request syntax.<br />
403 Forbidden - When the logged-in user does not have permission to access the resource.<br />
404 Not Found - When the resource specified in the request does not exist.<br />
</p></td>
</tr>
</tbody>
</table>

## Accessing Resources in Favorites

Use the following method to get the list of favorites. By default, favorites is false. For more information, see [Searching the Repository](resources.md).

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
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/resources?favorites=true</span></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/json</span></p></td>
<td colspan="2"><p>A JSON object that lists the resources added to Favorites.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK - The body contains a list of Favorites representing the results of the search.</p></td>
<td><p>404 Not Found - When the resource specified in the request does not exist.<br />
204 No content - When the resources added to Favorites are not found.<br />
</p></td>
</tr>
</tbody>
</table>
