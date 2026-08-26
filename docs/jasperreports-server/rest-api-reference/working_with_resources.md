---
title: Working With Resources
description: The JasperReports Server repository stores the resources such as data sources and reports that REST clients can interact with. Before you can use the restv2/resources service to access the...
---

# Working With Resources

The JasperReports Server repository stores the resources such as data sources and reports that REST clients can interact with. Before you can use the rest_v2/resources service to access the repository, you should understand how resources are represented. This chapter introduces concepts that are common to all resources as well as complex topics such as nested resources.

For further information, see:

-   [Chapter 1, “Resource Descriptors,” on page 1](resource_descriptors.md) for a reference to every type of resource and its attributes.

-   [Chapter 1, “The resources Service,” on page 1](resources.md) for methods to operate on resources in the repository.

    This chapter includes the following sections:

-   Resource URI

-   Custom Media Types

-   Accept HTTP Headers

-   Content-Type HTTP Headers

-   JSON Format

-   Nested Resources

-   Referenced Resources

-   Local Resources

-   Optimistic Locking

-   Update-only Passwords

## Resource URI

Resources (such as reports, images, queries, and data sources) are stored in the server's repository. The repository is organized like a file system, with a root and a hierarchical set of folders. Each object in the repository is considered a resource: a folder is a resource of type folder, a JRXML report is a resource of type reportUnit, and images are of type file.

Every resource has an ID that is unique within the folder where it resides. The IDs of all parent folders create a path, and appending the resource's own ID to the path gives the URI (Universal Resource Identifier) of the resource in the repository. Resource descriptors do not have an explicit ID attribute, but the ID is always the last component of the URI field in responses from the server.

In commercial editions of the server, the URI of a resource is relative to the organization of the user whose credentials are used to authenticate the request. Thus the path /datasources/JServerJdbcDS for an organization_1 user is the same resource as the path /organizations/organization_1/datasources/JServerJdbcDS for the system admin (`superuser`). The /public folder is a special path that is absolute for any user in any organization (including `superuser`).

!!! note

    As with all server operations, the folders and resources that are visible and accessible to a given user depend on permissions that are set in the repository on those folders and resources. REST services return an error when attempting an operation on resources that the authenticated user does not have permission to access.

The URI and ID of a created resource is determined in one of the following ways:

-   POST operations on the resources service specify a folder. The resource descriptor in the request is created in the specified folder. The ID is created automatically from the label of the resource by replacing special characters with underscores (`_`). The URI of the new resource is returned in the server's response and consists of the target folder with the automatic ID appended to it.
-   PUT operations on the resources service send a descriptor to create the resource at the URI specified in the request. The resource ID is the last element of this URI, as long as it is unique in the parent folder. The server's response should confirm that the resource was successfully created with the requested URI.

All resources also have a label string and a description string that can be presented to your client's users. The label and description support special characters (such as spaces, punctuation, and accented characters) and even Unicode if configured in your server during installation.

## Custom Media Types

In order to specify all the different types of resources, the resources service relies on custom media types with the following syntax:

application/repository.&lt;resourceType&gt;+&lt;format&gt;

where:

-   &lt;resourceType&gt; is the name for each type of repository resource, such as reportUnit, dataType, or jdbcDataSource. The names of all supported types are given in [Chapter 1, “Resource Descriptors,” on page 1](resource_descriptors.md).
-   &lt;format&gt; is the representation format of the descriptor, either json or xml.

For example:

application/repository.dataType+json – JSON representation of a datatype resource

application/repository.reportUnit+xml – XML representation of a JRXML report

The custom media types should be used in Content-Type and Accept HTTP headers, as described in the following sections. According to the HTTP specification, headers should be case insensitive; the headers and custom media types can be upper case, lower case, or any mixture of upper and lower case.

## Accept HTTP Headers

Client applications should use the Accept HTTP header in a request to specify the desired format in the server's response. Generally, regardless of the resource type, it's enough to specify:

-   Accept: application/json to get response in JSON format or

-   Accept: application/xml to get response in XML format.

    The server will respond with the specific custom media type for the requested resource, as described in the next section.

    However, there are some special cases where client must specify a precise resource type:

-   When requesting the resource details of the root folder, client must specify application/repository.folder+&lt;format&gt; to get its resource descriptor. Otherwise, the request is considered a search of the root folder.

-   When requesting the resource details of a file resource, as opposed to the file contents, the client must specify application/repository.file+&lt;format&gt;. Without this Accept header, the response will contain the file contents. The custom media type also distinguishes between the XML descriptor of a file and the contents of an XML file.

If the client specifies a custom type in the Accept header that does not match the resource being requested, the server responds with the error code 406 Not Acceptable.

## Content-Type HTTP Headers

The Content-Type HTTP header indicates the media type being sent in the body of the request or response. For example, if the client requests a valid datatype resource, and depending on the format that the client specified in the Accept header of the request, the server's response includes:

-   Content-Type: application/repository.dataType+json or

-   Content-Type: application/repository.dataType+xml

    When the client uploads a resource descriptor to create or update a resource, it must set the Content-Type connector accurately. For example, when uploading a datatype resource represented in XML, the client must send:

    Content-Type: application/repository.dataType+xml

    The server relies on the Content-Type header to parse the body of the request, and it will respond with the error code 400 Bad Request if there is a mismatch. In the example above, the following headers will result in an error:

-   Content-Type: application/xml – custom media type not included

-   Content-Type: application/repository.reportUnit+xml – media type mismatch

-   Content-Type: application/repository.dataType+json – format mismatch

## JSON Format

JasperReports Server uses the standard JSON (JavaScript Object Notation) format to send and receive representations of resources and other structures. The JSON marshalling and unmarshalling (parsing) uses the following conventions:

-   Attributes with no value or a null value are not transmitted in a request.
-   Unknown properties that JasperReports Server does not recognize are ignored without error.
-   Dates should be given in [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) format.

## Nested Resources

Many types of resources in the repository are defined in terms of other resources. For example, some types of input controls require a query, and the query itself requires a data source. The nested query and data source can be defined in two ways:

-   Referenced resources - a link to a valid resource defined elsewhere in the repository. JasperReports Server manages the references between resources by enforcing permissions and protecting dependencies from deletion.
-   Local resources - a resource descriptor nested within the parent descriptor. The nested resource is fully defined within the parent resource and not available for being referenced from elsewhere.

Both types of nested resources are further described in the following sections.

## Referenced Resources

Referenced resources are defined by special structures within the descriptors of other resources. For example, in the following query resource, the data source field contains a `dataSourceReference` object that contains the URI of the target reference:

``` json
{
    "version": 0,
    "permissionMask": 1,
    "creationDate": "2013-10-03T16:32:37",
    "updateDate": "2013-10-03T16:32:37",
    "label": "Country Query",
    "description": null,
    "uri": "/adhoc/topics/Cascading_multi_select_topic_files/Country_multi_select_files/
            country_query",
    "dataSource": { contents }, <*>
    "value": "select distinct billing_address_country from accounts order by billing_address_country",
    "language": "sql"
}

<*> or "dataSourceReference": {
           "uri": "/datasources/JServerJNDIDS"
       },
```

To create referenced resources, send requests to the server that contain the appropriate reference objects for the target resource. See 1.1, “Referenced Resources,” on page 1 for the specific reference objects available in each resource descriptor.

When reading resources with referenced resources, the `uri` attribute gives the repository URI of the reference. To simplify the parsing of referenced resources, the resources service GET method supports the expanded=true parameter. Instead of following references and requiring two or more GET requests, the expanded=true parameter returns all referenced resources fully expanded within the parent resource, as if it were a local resource.

The following resource types support referenced resources, and the table gives the name of the field that contains the referenced URI, and the name of the expanded type that replaces the reference.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th><p>Resource Type</p></th>
<th><p>Reference Attribute(s)</p></th>
<th><p>Expanded Name and Descriptor</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><span>query</span></p></td>
<td><p><span>dataSourceReference</span></p></td>
<td><p><span>awsDataSource</span>, <span>beanDataSource</span>, <span>customDataSource</span>, <span>jdbcDataSource</span>, <span>jndiJdbcDataSource</span>, <span>virtualDataSource</span>, <span>semanticLayerDataSource</span> or <span>advDataSource (adhocDataView)</span></p></td>
</tr>
<tr>
<td rowspan="3"><p><span>inputControl</span></p></td>
<td><p><span>datatypeReference</span></p></td>
<td><p><span>dataType</span></p></td>
</tr>
<tr>
<td><p><span>listOfValuesReference</span></p></td>
<td><p><span>listOfValues</span></p></td>
</tr>
<tr>
<td><p><span>queryReference</span></p></td>
<td><p><span>query</span></p></td>
</tr>
<tr>
<td rowspan="5"><p><span>reportUnit</span></p></td>
<td><p><span>jrxmlFileReference</span></p></td>
<td><p><span>jrxmlFile</span> with file attributes</p></td>
</tr>
<tr>
<td><p><span>dataSourceReference</span></p></td>
<td><p>see <span>query dataSourceReference</span></p></td>
</tr>
<tr>
<td><p><span>queryReference</span></p></td>
<td><p><span>query</span></p></td>
</tr>
<tr>
<td><p><span>inputControlReference</span></p></td>
<td><p><span>inputControl</span></p></td>
</tr>
<tr>
<td><p><span>fileReference</span> (images, ...)</p></td>
<td><p><span>fileResource</span> with file attributes</p></td>
</tr>
<tr>
<td rowspan="4"><p><span>semanticLayerDataSource</span><br />
(Domain)</p></td>
<td><p><span>dataSourceReference</span></p></td>
<td><p>see <span>query dataSourceReference</span></p></td>
</tr>
<tr>
<td><p><span>schemaFileReference</span></p></td>
<td><p><span>schemaFile</span> with file attributes</p></td>
</tr>
<tr>
<td><p><span>fileReference</span> (bundle)</p></td>
<td><p><span>file</span> of appropriate type</p></td>
</tr>
<tr>
<td><p><span>securityFileReference</span></p></td>
<td><p><span>securityFile</span> with file attributes</p></td>
</tr>
<tr>
<td><p><span>olapUnit</span></p></td>
<td><p><span>olapConnectionReference</span></p></td>
<td><p><span>xmlaConnection</span>,<br />
<span>mondrianConnection</span>,<br />
or <span>secureMondrianConnection</span></p></td>
</tr>
<tr>
<td rowspan="2"><p><span>mondrianConnection</span></p></td>
<td><p><span>dataSourceReference</span></p></td>
<td><p>see <span>query dataSourceReference</span></p></td>
</tr>
<tr>
<td><p><span>schemaReference</span></p></td>
<td><p><span>schema</span> with file attributes</p></td>
</tr>
<tr>
<td rowspan="3"><p><span>secureMondrianConnection</span></p></td>
<td><p><span>dataSourceReference</span></p></td>
<td><p>see <span>query dataSourceReference</span></p></td>
</tr>
<tr>
<td><p><span>schemaReference</span></p></td>
<td><p><span>schema</span> with file attributes</p></td>
</tr>
<tr>
<td><p><span>accessGrantSchemaReference</span></p></td>
<td><p><span>accessGrantSchema</span> with file attributes</p></td>
</tr>
<tr>
<td><p><span>mondrianXmlaDefinition</span></p></td>
<td><p><span>mondrianConnectionReference</span></p></td>
<td><p><span>mondrianConnection</span><br />
or <span>secureMondrianConnection</span></p></td>
</tr>
</tbody>
</table>

## Local Resources

Nested resources that are not referenced resources must be defined locally within the parent resource. The nested resource is defined by a complete resource descriptor of the appropriate type. The following example shows a data source that is defined locally within the parent query resource:

``` json
{
    "version": 0,
    "permissionMask": 1,
    "creationDate": "2013-10-03T16:32:37",
    "updateDate": "2013-10-03T16:32:37",
    "label": "Country Query",
    "description": null,
    "uri": "/adhoc/topics/Cascading_multi_select_topic_files/Country_multi_select_files/country_query",
    "dataSource": {
        "jndiJdbcDataSource": {
            "version": 0,
            "permissionMask": 1,
            "creationDate": "2013-10-03T16:32:05",
            "updateDate": "2013-10-03T16:32:05",
            "label": "my JNDI ds",
            "description": "Local JNDI Data Source",
            // URI of expanded nested resource is ignored. Resource is created locally
            "uri": "/datasources/JServerJNDIDS",
            "jndiName": "jdbc/sugarcrm",
            "timezone": null
        }
    },
    "value": "select distinct billing_address_country from accounts order by billing_address_country",
    "language": "sql"
}
```

Use nested descriptors such as the ones above to create resources that contain local resources. Descriptors can be nested to any level, as long as the syntax of each descriptor is valid. See 1.1, “Nested Resources,” on page 1 for the correct syntax of both the parent and the nested resource.

Internally, the resources service handles local resources as normal resources contained in a hidden folder. The hidden folder containing local resources has the following name:

&lt;parentURI&gt;\_files/

and local resources can be accessed at the following URI:

&lt;parentURI&gt;\_files/&lt;resourceID&gt;

In the example above, we can see that the parent query resource is a nested resource itself. Its URI shows us that it is the query resource for a query-based input-control of a topic resource:

/adhoc/topics/Cascading_multi_select_topic_files/Country_multi_select_files/country_query

and the new nested data source will have the following URI:

/adhoc/topics/Cascading_multi_select_topic_files/Country_multi_select_files/country_query_files/my_JNDI_ds

The ID of the nested resource (my_JNDI_ds) is created automatically from the label of the nested resource.

The \_files folder that exists in all parents of local resources is hidden so that its local resources do not appear in repository searches. You can set the `showHiddenItems=true` parameter on the resources request to search for a \_files folder in all local resources, such as in a JRXML report (reportUnit).

Local resources in the hidden \_files folder can also be created and updated separately from their parent resources by using PUT and POST methods of the resources service and specifying the complete URI of the local resource as shown above.

## Optimistic Locking

The resources service supports optimistic locking on all write and update operations (PUT and POST). When using the service to search the repository and receive descriptors of the resources, all descriptors contain a version number field. Clients should return the same version number when writing or updating a given resources. The server compares the version number in the modify request the current version of the resource to assure that no other client has updated the same resource.

If the version numbers do not match, the server replies with error code 409 Conflict. In that case, the client should request the resource again (read operation with GET) and send the modify request with an updated version number.

When a modify operation is successful, the server increments the version number on the affected resource and returns the new descriptor with the new version as confirmation that the operation was successful.

## Update-only Passwords

Some resource descriptors such as jdbcDataSource and xmlaConnection contain a password field. All password fields are blank or missing when reading (GET) a resource descriptor. This prevents anyone, even administrators from seeing existing passwords.

Write or update operations (PUT or POST) may send the password field in descriptors that support it. In this case, the password value is updated in the resource in the repository. Make sure that resources with sensitive passwords have the proper permissions so that only authorized users can modify them.

For complete security, you should only send passwords over HTTPS connections, otherwise they appear unencrypted in network packets.
