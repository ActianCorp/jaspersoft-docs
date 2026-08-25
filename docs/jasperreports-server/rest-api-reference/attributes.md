---
title: The attributes Service
description: "Attributes are name-value pairs that are associated with users, organizations, or the server. Unlike roles, attributes are not predefined, and thus any attribute name can be assigned to any value at..."
---

# The attributes Service

Attributes are name-value pairs that are associated with users, organizations, or the server. Unlike roles, attributes are not predefined, and thus any attribute name can be assigned to any value at any time. When running dashboards, views, or reports, certain advanced features of the server reference attribute values of the currently logged in user (or of the organization of the currently logged in user), so that behavior is customized for that user.

For example, Domain security files and OLAP access grants may reference attributes in addition to roles to grant certain permissions. Attributes may also be referenced when defining the fields of a data source, thereby making database access customized for each user or organization. Finally, application developers may use the attributes service to access or store information that can enhance their embedded BI solutions.

The `rest_v2/attributes` service provides methods for reading, writing, and deleting attributes at the server, organization, or user level. Only administrative users may access the attributes service. System admins (`superuser`) can set attributes anywhere in the server, and organization admins (`jasperadmin`) can set attributes within their own organization or any suborganizations. Because of the nature of attributes, organization admins may see attributes from parent organizations and override them if allowed to do so by the parent administrator.

Attributes used to be called profile attributes because they were associated only with users. As of JasperReports Server 6.0, the attributes service applies to users, organization, and the root organization representing the server.

This chapter includes the following sections:

- Attribute Descriptors

- Secure Attributes

- Entities with Attributes

- Permissions for Accessing Attributes

- Referencing Attributes

- Attribute Limitations

- Viewing Attributes

- Setting Attributes

- Deleting Attributes

## Attribute Descriptors

Attributes are represented as a pair of string fields, one for the name of the attribute, the other for its value. For example, the following JSON structure defines an attribute:

``` json
{
    "name": "Attr1",
    "value": "Value1"
}
```

Each attribute may only have one value, however that value may contain a comma-separated list that, in certain uses, is interpreted by the server as being multi-valued. Such attributes can be used in Domain security filters that match against a collection of values.

``` json
{
    "name": "Attr2",
    "value": "Value2a,Value2b,Value2c"
}
```

Attributes with the same name may be defined on different entities. For example, a user has a specific value for an attribute, the organization they belong to have a default value for the same attribute, and the server level has yet another value for it. In this example, three separate attributes are defined, but they have the same name because they occur on different entities. The mechanisms described in Referencing Attributes can take advantage of this to implement default values.

## Secure Attributes

JasperReports Server 6.0 also introduced the notion of the secure attribute that can be used to store sensitive information such as a password. Secure attributes have the following properties:

- Their values are stored in encrypted form in the server's internal database.

- Their values are write only through the REST service and their value is never returned.

- Their values are never displayed in the user interface. Only ●●● or \*\*\* symbols are shown.

- Their value is decrypted only when referenced internally, for example as the password field in a data source.

When reading the value of a secure attribute, the server returns the field `"secure": "true"` instead of the `"value"` field. Applications that read attributes must test for this case:

``` json
{
    "name": "Attr3",
    "secure": "true"
}
```

When setting the value of a secure attribute, your application should specify both the secure field and the value field.

``` json
{
    "name": "Attr3"
    "value": "SecureValue3"
    "secure": "true"
}
```

Applications that set secure attributes should consider enabling HTTPS so that the clear-text value of the attribute is encrypted in all communication with the server.

## Entities with Attributes

The entities that may have attributes are user accounts, organizations, and the server itself, represented by the root organization. The entity is specified in the URL invoking the attributes service. The URL has the following form:

http://\<host\>:\<port\>/jasperserver\[-pro\]/rest_v2/\<entity\>attributes\<parameters\>

The syntax of \<entity\> depends on the target entity for the operation and the type of server.

| Commercial Edition | Syntax of \<entity\>                           |
|--------------------|------------------------------------------------|
| User               | organizations/organizationID/users/userID/     |
| Organization-level | organizations/organizationID/                  |
| Server Admin       | users/userID/                                  |
| Server-level       | \<blank\> (the attributes apply to the "root") |
| Community Edition  | Syntax of \<entity\>                           |
| User               | users/userID/                                  |
| Server-level       | \<blank\> (the attributes apply to the "root") |

!!! note

    When specifying the organization, use its unique ID, not its path. In commercial edition, servers that use the single default organization, you must specify `organization_1`.

## Permissions for Accessing Attributes

Only API calls that include administrator credentials may view, set, or delete attributes on users, organizations, or the server. Non-administrative users cannot view or edit attributes, even on their own user account.

In commercial editions of the server, operations on attributes follow the visibility rules for organizations:

- Organization admins (`jasperadmin` by default) can view and edit attributes on their own organization, their users, any of their suborganizations, and the users in any suborganizations.

- Organization admins cannot view or edit attributes in any parent or sibling organizations.

- Only the server admin (`superuser` by default) can view and edit attributes at the server level, represented as the root organization.

- Server admins can view and edit attributes on any organization or suborganization in the server, as well as on any user account in any organization.

- Only a server admin can view and edit attributes on other server admins (users of the root organization).

## Referencing Attributes

As mentioned, several internal mechanisms of the server read attributes on users and organizations to use their values in some way:

- Domain security files: You can reference attribute values associated with the logged in user (or his organization) to create rules to access data in the Domain. For more information, see the chapter "Advanced Domains Features" in the JasperReports Server User Guide.

- Data source definitions: The fields that define a data source, such as its server, port number, database, and user credentials, can all reference attributes of the logged in user's organization (or a server-specific attribute). In this way, different organizations or different servers can share the same data source yet still access a different database. For more information, see the chapter "Data Sources" in the JasperReports Server Administrator Guide.

The server provides two different methods to reference attributes:

- Categorical reference: Requests the value of a named attribute from a specific entity, either the logged in user's profile, the logged in user's organization, or from the server-wide set of attributes. If the named attribute is not defined in the specified entity, an error is returned.

- Hierarchical reference: Searches for the value of a named attribute first in the logged in user's account, and if not found, then in the logged in user's organization, and if still not found, then at the server level. This allows attributes to be defined at several levels, with the definition at a lower level (the user profile) having higher priority, and the definition at a higher lever (the organization or server level) providing a default value. If the named attribute is not defined at any level, an error is returned.

The methods you use to reference attributes then determines the entities where you need to create attributes and the values of those attributes.

## Attribute Limitations

Attributes have the following limitations in the attributes service:

- The user ID and organization ID are specified in the URL, and therefore must be less than 100 characters long and not contain spaces or special symbols.

- Attribute names and attribute values being written with this service are limited to 255 characters and may not be empty (null) nor contain only whitespace characters.

The attributes service detects these conditions and returns errors accordingly:

| Error Code | Description |
|----|----|
| too_long_name | The attribute's name is longer than 255 characters. |
| too_long_value | The attribute's value is longer than 255 characters. |
| empty_name | The attribute's name is empty or contains only whitespaces. |
| empty_value | The attribute's value is empty or contains only whitespaces. |

Some methods of the attributes service operate on multiple attributes on a given entity. Such batch operations are not transactional, meaning the operation terminates with no rollback functionality when encountering an error. Attributes that have been processed (modified or deleted) before the error remain so, and attributes after the error are not processed.

All attribute operations apply to a single specific entity. There are no operations for reading or setting attributes on multiple entities.

## Viewing Attributes

The GET method of the attributes service retrieves the list of attributes, if any, defined for the specified entity (a user, an organization, or the server-level). For possible values of \<entity\> in the URL, see Entities with Attributes.

There are two syntaxes. The following one is for reading multiple attributes or all attributes at once.

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
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/</span>&lt;entity&gt;<span>attributes</span>?&lt;arguments&gt;</span></p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><span>name</span></p></td>
<td><p>Optional<br />
String</p></td>
<td colspan="2"><p>Specify an attribute name to list the value of that specific attribute. Repeat this argument to view multiple attributes. When this argument is omitted, all attributes and their values are returned for the given entity.</p></td>
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
<td colspan="3"><p>200 OK - The content is the list of attributes for the given entity.</p>
<p>204 No Content - The search did not return any attributes or the entity has no attributes.</p></td>
<td><p>404 Not Found - When the user ID or organization ID does not match any user or organization. The content includes an error message.</p></td>
</tr>
</tbody>
</table>

The list of attributes includes the name and value of each attribute. The following example shows user-level attributes in JSON format:

GET http://localhost:8080/jasperserver-pro/rest_v2/organizations/organzation_1/users/joeuser/attributes

``` json
{
  "attribute":[
    {
      "name": "Attr1",
      "value":"Value1"
    },
    ...
    {
      "name": "AttrN",
      "value":"ValueN"
    }
  ]
}
```

The second syntax reads a single attribute by specifying its name in the URL:

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
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/</span>&lt;entity&gt;<span>attributes</span>/attrName</span></p></td>
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
<td colspan="3"><p>200 OK - The content is a single attribute for the given entity.</p></td>
<td><p>404 Not Found - When the user ID, organization ID, or attribute name does not match any user, organization, or attribute. The content includes an error message.</p></td>
</tr>
</tbody>
</table>

The response is a single attribute name-value pair. The following example shows an organization-level attribute in JSON format:

GET http://localhost:8080/jasperserver-pro/rest_v2/organizations/organization_1/attributes/Attr2

``` json
{
  "name": "Attr2",
  "value":"Value2a,Value2b,Value2c"
}
```

### Viewing Dashboard Web Page Domain Whitelist Attributes

This GET request on the attributes service is used to populate the list of approved domains for embedding web pages. These whitelist values are utilized by the user interface and Visualize.js to manage which external sites can be added to dashboards.

#### Endpoint

Retrieve dashboard webpage domain whitelist values used in the user interface and Visualize.js.

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
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/attributes/dashboardDomainWhitelistValues</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK - The content is the list of whitelist attributes.</p>
<p>200 OK - Empty value</p></td>
<td><p>401 Unauthorized - The request has not been applied to the target resource because it lacks valid authentication credentials for that resource.</p>
<p>403 Access denied - Access is denied.</p></td>
</tr>
</tbody>
</table>

- Permissions: **ROLE_USER, ROLE_ADMINISTRATOR**

Since the superuser possesses the **ROLE_ADMINISTRATOR** role, they also have access to this API.

Sample response:

Attribute not configured for user

``` json
{"dashboardWebpageDomainWhitelist":[""]}
```

Attribute configured for user

``` json
{"dashboardWebpageDomainWhitelist": ["value.com", "value2.com", "value3.com"]
}
```

- Permissions: **ROLE_DEMO**

Sample response:

``` json
{"message":"Access is denied","errorCode":"access.denied"}
```

- Permissions: **ROLE_SUPERUSER**

Sample response:

Attribute not configured for user

``` json
{
    "dashboardWebpageDomainWhitelist": [
        ""
    ]
        }
```

Attribute configured for user

``` json
{
    "dashboardWebpageDomainWhitelist": [
        "http://www.example.com",
        "https://www.test.com"
    ]
}
```

## Setting Attributes

The PUT method of the attributes service adds or replaces attributes on the specified entity (a user, an organization, or the server-level). For possible values of \<entity\> in the URL, see Entities with Attributes.

There are two syntaxes. The following one is for adding or replacing all attributes at once.

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
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/</span>&lt;entity&gt;<span>attributes</span></span></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/xml</span></p>
<p><span>application/json</span></p></td>
<td colspan="2"><p>An attribute descriptor that includes the new list of attributes. All previously defined attributes are replaced by this new list.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>201 Created - When the attributes were successfully created on the given entity.</p>
<p>200 OK - When the attributes were successfully updated.</p></td>
<td><p>404 Not Found - When the user ID or organization ID does not match any user or organization. The content includes an error message.</p>
<p>400 Bad Request - When an attribute name or value is null, blank, or too long (see <span>Attribute Limitations</span>). If one attribute causes an error, the operation stops and returns an error, but the attributes that were already set remain.</p></td>
</tr>
</tbody>
</table>

The following example shows how to set all attributes on an organization. The list of attributes in JSON format defines the name and value of each attribute.

PUT http://localhost:8080/jasperserver-pro/rest_v2/organizations/organization_1/attributes

``` json
{
  "attribute":[
    {
      "name": "Attr1",
      "value":"newValue1"
    },
    {
      "name": "Attr2",
      "value":"newValue2a, newValue2b"
    },
    {
      "name": "Attr3"
      "value": "SecureValue3"
      "secure": "true"
    }
  ]
}
```

The second syntax of the PUT attributes method is for adding or replacing individual attributes.

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
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/</span>&lt;entity&gt;<span>attributes</span>/attrName</span></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/xml</span></p>
<p><span>application/json</span></p></td>
<td colspan="2"><p>A single attribute name-value pair. The attribute name must match the <span>attrName</span> exactly as it appears in the URL. If this attribute name already exists on the specified user, this attribute’s value is updated. If the attribute does not exist, it is added to the user’s list of attributes.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>201 Created - When the attribute was successfully created on the given entity.</p>
<p>200 OK - When the attribute was successfully updated.</p></td>
<td><p>404 Not Found - When the user ID or organization ID does not match any user or organization. The content includes an error message.</p></td>
</tr>
</tbody>
</table>

The content in the request is a single attribute, for example:

PUT http://localhost:8080/jasperserver-pro/rest_v2/organizations/organization_1/users/<br>
joeuser/attributes/Attr2

``` json
{
  "name": "Attr2",
  "value":"NewValue2"
}
```

## Deleting Attributes

The DELETE method of the attributes service removes attributes from the specified entity (a user, an organization, or the server-level). When attributes are removed, both the name and the value of the attribute are removed, not only the value. For possible values of \<entity\> in the URL, see Entities with Attributes.

There are two syntaxes. The following one is for deleting multiple attributes or all attributes at once.

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
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/</span>&lt;entity&gt;<span>attributes</span>?&lt;arguments&gt;</span></p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><span>name</span></p></td>
<td><p>Optional<br />
String</p></td>
<td colspan="2"><p>Specify an attribute name to remove that attribute. Repeat this argument to delete multiple attributes. When this argument is omitted, all attributes are deleted from the given entity.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>204 No Content - The attributes were successfully removed from the given entity.</p></td>
<td><p>404 Not Found - When the user ID or organization ID does not match any user or organization. The content includes an error message.</p>
<p>400 Bad Request - When an attribute name is null, blank, or too long (see <span>Attribute Limitations</span>). If one attribute causes an error, the operation stops and returns an error, but the attributes that were already deleted remain deleted.</p></td>
</tr>
</tbody>
</table>

The second syntax deletes a single attribute named in the URL from the specified entity.

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
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/</span>&lt;entity&gt;<span>attributes</span>/attrName</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>204 No Content - The attribute was successfully removed from the given entity.</p></td>
<td><p>404 Not Found - When the user ID, organization ID, or attribute name does not match any user, organization, or attribute. The content includes an error message.</p>
<p>400 Bad Request - When an attribute name is null, blank, or too long (see <span>Attribute Limitations</span>).</p></td>
</tr>
</tbody>
</table>

!!! note

    servers that use the single default organization, you must specify `organization_1`.

## Permissions for Accessing Attributes

Only API calls that include administrator credentials may view, set, or delete attributes on users, organizations, or the server. Non-administrative users cannot view or edit attributes, even on their own user account.

In commercial editions of the server, operations on attributes follow the visibility rules for organizations:

- Organization admins (`jasperadmin` by default) can view and edit attributes on their own organization, their users, any of their suborganizations, and the users in any suborganizations.
- Organization admins cannot view or edit attributes in any parent or sibling organizations.
- Only the server admin (`superuser` by default) can view and edit attributes at the server level, represented as the root organization.
- Server admins can view and edit attributes on any organization or suborganization in the server, as well as on any user account in any organization.
- Only a server admin can view and edit attributes on other server admins (users of the root organization).

## Referencing Attributes

As mentioned, several internal mechanisms of the server read attributes on users and organizations to use their values in some way:

- Domain security files: You can reference attribute values associated with the logged in user (or his organization) to create rules to access data in the Domain. For more information, see the chapter "Advanced Domains Features" in the JasperReports Server User Guide.
- Data source definitions: The fields that define a data source, such as its server, port number, database, and user credentials, can all reference attributes of the logged in user's organization (or a server-specific attribute). In this way, different organizations or different servers can share the same data source yet still access a different database. For more information, see the chapter "Data Sources" in the JasperReports Server Administrator Guide.

The server provides two different methods to reference attributes:

- Categorical reference: Requests the value of a named attribute from a specific entity, either the logged in user's profile, the logged in user's organization, or from the server-wide set of attributes. If the named attribute is not defined in the specified entity, an error is returned.
- Hierarchical reference: searches for the value of a named attribute first in the logged in user's account, and if not found, then in the logged in user's organization, and if still not found, then at the server level. This allows attributes to be defined at several levels, with the definition at a lower level (the user profile) having higher priority, and the definition at a higher lever (the organization or server level) providing a default value. If the named attribute is not defined at any level, an error is returned.

The methods you use to reference attributes then determines the entities where you need to create attributes and the values of those attributes.

## Attribute Limitations

Attributes have the following limitations in the attributes service:

- The user ID and organization ID are specified in the URL, and therefore must be less than 100 characters long and not contain spaces or special symbols.
- Attribute names and attribute values being written with this service are limited to 255 characters and may not be empty (null) nor contain only whitespace characters.

The attributes service detects these conditions and returns errors accordingly:

| Error Code | Description |
|----|----|
| too_long_name | The attribute's name is longer than 255 characters. |
| too_long_value | The attribute's value is longer than 255 characters. |
| empty_name | The attribute's name is empty or contains only whitespaces. |
| empty_value | The attribute's value is empty or contains only whitespaces. |

Some methods of the attributes service operate on multiple attributes on a given entity. Such batch operations are not transactional, meaning the operation terminates with no rollback functionality when encountering an error. Attributes that have been processed (modified or deleted) before the error remain so, and attributes after the error are not processed.

All attribute operations apply to a single specific entity. There are no operations for reading or setting attributes on multiple entities.
