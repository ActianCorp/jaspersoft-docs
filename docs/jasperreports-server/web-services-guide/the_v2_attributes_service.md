---
title: The v2/attributes Service
description: "Attributes are name-value pairs that are associated with users, organizations, or the server. Unlike roles, attributes are not pre-defined, and thus any attribute name can be assigned any value at..."
---

# 1.1 The v2/attributes Service

Attributes are name-value pairs that are associated with users, organizations, or the server. Unlike roles, attributes are not pre-defined, and thus any attribute name can be assigned any value at any time. When running dashboards, views, or reports, certain advanced features of the server will reference attribute values of the currently logged-in user (or of the organization of the currently logged-in user), so that behavior is customized for that user.

For example, Domain security files and OLAP access grants may reference attributes in addition to roles to grant certain permissions. Attributes may also be referenced when defining the fields of a data source, thereby making database access customized for each user or organization. Finally, application developers may use the v2/attributes service in order access or store information that can enhance their embedded BI solutions.

Attributes used to be called profile attributes because they were associated only with users. As of JasperReports® Server 6.0, the attributes service applies to users, organization, and the root organization representing the server.

The rest_v2/attributes service provides methods for reading, writing, and deleting attributes on any given user account or organization. Attributes are represented as a pair of fields, one for the name of the attribute, the other for its value. For example, the following JSON structure defines an attribute:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;name&quot;</span><span class="fu">:</span> <span class="st">&quot;Attr1&quot;</span><span class="fu">,</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;value&quot;</span><span class="fu">:</span> <span class="st">&quot;Value1&quot;</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
</tbody>
</table>

Each attribute may only have one value, however that value may contain a comma-separated list that is interpreted by the server as being multi-valued. Such attributes can be used in Domain security filters that match against a collection of values.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;name&quot;</span><span class="fu">:</span> <span class="st">&quot;Attr2&quot;</span><span class="fu">,</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;value&quot;</span><span class="fu">:</span> <span class="st">&quot;Value2a,Value2b,Value2c&quot;</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
</tbody>
</table>

Attributes with the same name may be defined on different entities. For example, a user has a specific value for an attribute, the organization he belongs to has a default value for the same attribute, and the server level has yet another value for it. In this example, three separate attributes are defined, but they have the same name because they occur on different entities. The mechanisms described in [1.1.4, “Referencing Attributes,” on page 1](#114-referencing-attributes) can take advantage of this to implement default values.

## 1.1.1 Secure Attributes

JasperReports® Server 6.0 also introduces the notion of secure attribute that can be used to store sensitive information such as a password. Secure attributes have the following properties:

-   Their values are stored in encrypted form in the server's internal database.
-   Their values are write-only through the REST service; their value is never returned.
-   Their values are never displayed in the user interface; only ●●● or \*\*\* symbols are shown.
-   Their value is decrypted only when referenced internally, for example as the password field in a data source.

When reading the value of a secure attribute, the server returns the field `"secure": "true"` instead of the `"value"` field. Applications that read attributes must test for this case:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;name&quot;</span><span class="fu">:</span> <span class="st">&quot;Attr3&quot;</span><span class="fu">,</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;secure&quot;</span><span class="fu">:</span> <span class="st">&quot;true&quot;</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
</tbody>
</table>

When setting the value of a secure attribute, your application should specify both the secure field and the value field.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;name&quot;</span><span class="fu">:</span> <span class="st">&quot;Attr3&quot;</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;value&quot;</span><span class="er">:</span> <span class="st">&quot;SecureValue3&quot;</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;secure&quot;</span><span class="er">:</span> <span class="st">&quot;true&quot;</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
</tbody>
</table>

Applications that set secure attributes should consider enabling HTTPS so that the clear-text value of the attribute is encrypted in all communication with the server.

## 1.1.2 Entities with Attributes

The entities that may have attributes are user accounts, organizations, and the server itself, represented by the root organization. The entity is specified in the URL invoking the v2/attributes service. The URL has the following form:

http://&lt;host&gt;:&lt;port&gt;/jasperserver\[-pro\]/rest_v2/&lt;entity&gt;attributes&lt;parameters&gt;

The syntax of &lt;entity&gt; depends on the target entity for the operation and the type of server.

| Commercial Edition | Syntax of &lt;entity&gt;                           |
|--------------------|----------------------------------------------------|
| User               | organizations/organizationID/users/userID/         |
| Organization-level | organizations/organizationID/                      |
| Server Admin       | users/userID/                                      |
| Server-level       | &lt;blank&gt; (the attributes apply to the "root") |
| Community Edition  | Syntax of &lt;entity&gt;                           |
| User               | users/userID/                                      |
| Server-level       | &lt;blank&gt; (the attributes apply to the "root") |

!!! note

    When specifying the organization, use its unique ID, not its path. In commercial edition servers that use the single default organization, you must specify `organization_1`.

## 1.1.3 Permissions for Accessing Attributes

Only API calls that include administrator credentials may view, set, or delete attributes on users, organizations, or the server. Non-administrative users can't view or edit attributes, even on their own user account.

In commercial editions of the server, operations on attributes follow the visibility rules for organizations:

-   Organization admins (`jasperadmin` by default) can view and edit attributes on their own organization, their users, any of their sub-organizations, and the users in any sub-organizations.
-   Ogranization admins can't view or edit attributes in any parent or sibling organizations.
-   Only the server admin (`superuser` by default) can view and edit attributes at the server level, represented as the root organization.
-   Server admins can view and edit attributes on any organization or sub-organization in the server, as well as on any user account in any organization.
-   Only a server admin can view and edit attributes on other server admins (users of the root organization).

## 1.1.4 Referencing Attributes

As mentioned, several internal mechanisms of the server read attributes on users and organizations and make use of their values in some way:

-   Domain security files: you can reference attribute values associated with the logged-in user (or his organization) to create rules to access data in the Domain. For more information, see the chapter "Advanced Domains Features" in the JasperReports® Server User Guide.

-   Data source definitions: the fields that define a data source, such as its server, port number, database, and user credentials, can all reference attributes of the logged-in user's organization (or a server-specific attribute). In this way, different organizations or different servers can share the same data source yet still access a different database. For more information, see the chapter "Data Sources" in the JasperReports® Server Administrator Guide.

    The server provides two different methods to reference attributes:

-   Categorical reference: requests the value of a named attribute from a specific entity, either the logged-in user's profile, the logged-in user's organization, or from the server-wide set of attributes. If the named attribute is not defined in the specified entity, an error is returned.

-   Hierarchical reference: searches for the value of a named attribute first in the logged-in user's account, and if not found, then in the logged-in user's organization, and if still not found, then at the server level. This allows attributes to be defined at several levels, with the defintion at a lower level (the user profile) having higher priority, and the definition at a higher lever (the organization or server level) providing a default value. If the named attritute is not defined at any level, an error is returned.

The methods you use to reference attributes will then determine the entities where you need to create attributes and the values of those attributes.

## 1.1.5 Attribute Limitations

Attributes have the following limitations in the v2/attributes service:

-   The user ID and organization ID are specified in the URL, and therefore must be less than 100 characters long and not contain spaces or special symbols.
-   Attribute names and attribute values being written with this service are limited to 255 characters and may not be empty (null) nor contain only whitespace characters.

The v2/attributes service detects these conditions and returns errors accordingly:

| ErrorCode      | Description                                              |
|----------------|----------------------------------------------------------|
| too_long_name  | Attribute's name is longer than 255 characters.          |
| too_long_value | Attribute's value is longer than 255 characters.         |
| empty_name     | Attribute's name is empty or contains only whitespaces   |
| empty_value    | Attribute's value is empty or contains only whitespaces. |

Some methods of the v2/attributes service operate on multiple attributes on a given entity. Such batch operations are not transactional, meaning the operation terminates with no rollback functionality when encountering an error. Attributes that have been processed (modified or deleted) before the error remain so, and attributes after the error are not processed.

All attribute operations apply to a single specific entity; there are no operations for reading or setting attributes on multiple entities.
