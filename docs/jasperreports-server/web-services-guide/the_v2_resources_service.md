---
title: The v2/resources Service
description: The REST v2/resources service replaces the original resource and resources services to search the repository and access the resources it contains. This new service provides greater performance and...
---

# The v2/resources Service

The REST v2/resources service replaces the original resource and resources services to search the repository and access the resources it contains. This new service provides greater performance and more consistent handling of resource descriptors for all repository resource types. The service has two formats, one takes search parameters to find resources, the other takes a repository URI to access resource descriptors and file contents.

## V2 Resource Descriptors

The v2/resources service introduces new resource descriptors for nearly all repository objects. This section introduces the features of the new descriptors, and the next section, V2 Resource Descriptor Types, lists all the descriptors and the specific attributes of each.

### Resource IDs

The ID of a resource is its unique name within the folder where it resides. Resource descriptors do not have an explicit ID attribute, but the ID is always the last component of the URI field in responses from the server.

When sending resource descriptors in requests, the URI field is ignored. The URI and ID of a created resource is determined in one of the following ways:

- POST operations on the v2/resources service specify a folder. The resource descriptor in the request is created in the specified folder. The ID is created automatically from the label of the resource by replacing special characters with underscores (`_`). The URI of the new resource is returned in the server's response and consists of the target folder with the automatic ID appended to it.
- PUT operations on the v2/resources service send a descriptor to create the resource at the URI specified in the request. The resource ID is the last element of this URI, as long as it is unique in the parent folder. The server's response should confirm that the resource was successfully created with the requested URI.

### Custom Media Types

In order to specify all the different types of resources, the v2/resources service relies on custom media types with the following syntax:

application/repository.\<resourceType\>+\<format\>

where:

- \<resourceType\> is the name for each type of repository resource, such as reportUnit, dataType, or jdbcDataSource. The names of all supported types are given in V2 Resource Descriptor Types.
- \<format\> is the representation format of the descriptor, either json or xml.

For example:

application/repository.dataType+json - JSON representation of a datatype resource

application/repository.reportUnit+xml - XML representation of a JRXML report

The custom media types should be used in Content-Type and Accept HTTP headers, as described in the following sections. According to the HTTP specification, headers should be case insensitive; the headers and custom media types can be upper case, lower case, or any mixture of upper and lower case.

### Accept HTTP Headers

Client applications should use the Accept HTTP header in a request to specify the desired format in the server's response. Generally, regardless of the resource type, it's enough to specify:

- Accept: application/json to get response in JSON format or
- Accept: application/xml to get response in XML fomat.

The server will respond with the specific custom media type for the requested resource, as described in the next section.

However, there are some special cases where client must specify a precise resource type:

- When requesting the resource details of the root folder, client must specify application/repository.folder+\<format\> to get its resource descriptor. Otherwise, the request is considered a search of the root folder.
- When requesting the resource details of a file resource, as opposed to the file contents, the client must specify application/repository.file+\<format\>. Without this Accept header, the response will contain the file contents. The custom media type also distinguishes between the XML descriptor of a file and the contents of an XML file.

If the client specifies a custom type in the Accept header that does not match the resource being requested, the server responds with the error code 406 Not Acceptable.

### Content-Type HTTP Headers

The Content-Type HTTP header indicates the media type being sent in the body of the request or response. For example, if the client requests a valid datatype resource, and depending on the format that the client specified in the Accept header of the request, the server's response includes:

- Content-Type: application/repository.dataType+json or
- Content-Type: application/repository.dataType+xml

When the client uploads a resource descriptor to create or update a resource, it must set the Content-Type connector accurately. For example, when uploading a datatype resource represented in XML, the client must send:

Content-Type: application/repository.dataType+xml

The server relies on the Content-Type header to parse the body of the request, and it will respond with the error code 400 Bad Request if there is a mismatch. In the example above, the following headers will result in an error:

- Content-Type: application/xml - custom media type not included
- Content-Type: application/repository.reportUnit+xml - media type mismatch
- Content-Type: application/repository.dataType+json - format mismatch

### JSON Format

JasperReports® Server uses the standard JSON (JavaScript Object Notation) format to send and receive representations of resources and other structures. The JSON marshalling and unmarshalling (parsing) uses the following conventions:

- Attributes with no value or a null value are not transmitted in a request.
- Unknown properties that JasperReports® Server does not recognize are ignored without error.
- Dates should be given in [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) format.

### Nested Resources

Many types of resources in the repository are defined in terms of other resources. For example, some types of input controls require a query, and the query itself requires a data source. The nested query and data source can be defined in two ways:

- Referenced resources - a link to a valid resource defined elsewhere in the repository. JasperReports® Server manages the references between resources by enforcing permissions and protecting dependencies from deletion.
- Local resources - a resource descriptor nested within the parent descriptor. The nested resource is fully defined within the parent resource and not available for being referenced from elsewhere.

Both types of nested resources are further described in the following sections.

### Referenced Resources

Referenced resources are defined by special structures within the descriptors of other resources. For example, in the following query resource, the data source field contains a dataSourceReference object that contains the URI of the target reference:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;version&quot;</span><span class="fu">:</span> <span class="dv">0</span><span class="fu">,</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;permissionMask&quot;</span><span class="fu">:</span> <span class="dv">1</span><span class="fu">,</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;creationDate&quot;</span><span class="fu">:</span> <span class="st">&quot;2013-10-03T16:32:37&quot;</span><span class="fu">,</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;updateDate&quot;</span><span class="fu">:</span> <span class="st">&quot;2013-10-03T16:32:37&quot;</span><span class="fu">,</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;label&quot;</span><span class="fu">:</span> <span class="st">&quot;Country Query&quot;</span><span class="fu">,</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;description&quot;</span><span class="fu">:</span> <span class="kw">null</span><span class="fu">,</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;uri&quot;</span><span class="fu">:</span> <span class="st">&quot;/adhoc/topics/Cascading_multi_select_topic_files/Country_multi_select_files/</span></span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a><span class="st">            country_query&quot;</span><span class="fu">,</span></span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;dataSource&quot;</span><span class="fu">:</span> <span class="fu">{</span> <span class="er">contents</span> <span class="fu">},</span> <span class="er">&lt;*&gt;</span></span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;value&quot;</span><span class="fu">:</span> <span class="st">&quot;select distinct billing_address_country from accounts order by billing_address_country&quot;</span><span class="fu">,</span></span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;language&quot;</span><span class="fu">:</span> <span class="st">&quot;sql&quot;</span></span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a><span class="er">&lt;*&gt;</span> <span class="er">or</span> <span class="st">&quot;dataSourceReference&quot;</span><span class="er">:</span> <span class="fu">{</span></span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>           <span class="dt">&quot;uri&quot;</span><span class="fu">:</span> <span class="st">&quot;/datasources/JServerJNDIDS&quot;</span></span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a>       <span class="fu">}</span><span class="er">,</span></span></code></pre></div></td>
</tr>
</tbody>
</table>

To create referenced resources, send requests to the server that contain the appropriate reference objects for the target resource. See the V2 Resource Descriptor Types for the specific reference objects available in each resource descriptor.

When reading resources with referenced resources, the `uri` attribute gives the repository URI of the reference. To simplify the parsing of referenced resources, the v2/resources service GET method supports the expanded=true parameter. Instead of following references and requiring two or more GET requests, the expanded=true parameter returns all referenced resources fully expanded within the parent resource, as if it were a local resource.

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
<td><p>query</p></td>
<td><p>dataSourceReference</p></td>
<td><p>awsDataSource, beanDataSource, customDataSource, jdbcDataSource, jndiJdbcDataSource, virtualDataSource, semanticLayerDataSource or advDataSource (adhocDataView)</p></td>
</tr>
<tr>
<td><p>inputControl</p></td>
<td><p>datatypeReference<br />
listOfValuesReference<br />
queryReference</p></td>
<td><p>dataType<br />
listOfValues<br />
query</p></td>
</tr>
<tr>
<td><p>reportUnit</p></td>
<td><p>jrxmlFileReference<br />
dataSourceReference<br />
queryReference<br />
inputControlReference<br />
fileReference (images, ...)</p></td>
<td><p>jrxmlFile with file attributes<br />
see query dataSourceReference<br />
query<br />
inputControl<br />
fileResource with file attributes</p></td>
</tr>
<tr>
<td><p>semanticLayerDataSource<br />
(Domain)</p></td>
<td><p>dataSourceReference<br />
schemaFileReference<br />
fileReference (bundle)<br />
securityFileReference</p></td>
<td><p>see query dataSourceReference<br />
schemaFile with file attributes<br />
file of appropriate type<br />
securityFile with file attributes<br />
</p></td>
</tr>
<tr>
<td><p>olapUnit</p></td>
<td><p>olapConnectionReference</p></td>
<td><p>xmlaConnection,<br />
mondrianConnection,<br />
or secureMondrianConnection</p></td>
</tr>
<tr>
<td><p>mondrianConnection</p></td>
<td><p>dataSourceReference<br />
schemaReference</p></td>
<td><p>see query dataSourceReference<br />
schema with file attributes</p></td>
</tr>
<tr>
<td><p>secureMondrianConnection</p></td>
<td><p>dataSourceReference<br />
schemaReference<br />
accessGrantSchemaReference</p></td>
<td><p>see query dataSourceReference<br />
schema with file attributes<br />
accessGrantSchema with file attributes</p></td>
</tr>
<tr>
<td><p>mondrianXmlaDefinition</p></td>
<td><p>mondrianConnectionReference</p></td>
<td><p>mondrianConnection<br />
or secureMondrianConnection</p></td>
</tr>
</tbody>
</table>

### Local Resources

Nested resources that are not referenced resources must be defined locally within the parent resource. The nested resource is defined by a complete resource descriptor of the appropriate type. The following example shows a data source that is defined locally within the parent query resource:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;version&quot;</span><span class="fu">:</span> <span class="dv">0</span><span class="fu">,</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;permissionMask&quot;</span><span class="fu">:</span> <span class="dv">1</span><span class="fu">,</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;creationDate&quot;</span><span class="fu">:</span> <span class="st">&quot;2013-10-03T16:32:37&quot;</span><span class="fu">,</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;updateDate&quot;</span><span class="fu">:</span> <span class="st">&quot;2013-10-03T16:32:37&quot;</span><span class="fu">,</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;label&quot;</span><span class="fu">:</span> <span class="st">&quot;Country Query&quot;</span><span class="fu">,</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;description&quot;</span><span class="fu">:</span> <span class="kw">null</span><span class="fu">,</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;uri&quot;</span><span class="fu">:</span> <span class="st">&quot;/adhoc/topics/Cascading_multi_select_topic_files/Country_multi_select_files/country_query&quot;</span><span class="fu">,</span></span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;dataSource&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;jndiJdbcDataSource&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;version&quot;</span><span class="fu">:</span> <span class="dv">0</span><span class="fu">,</span></span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;permissionMask&quot;</span><span class="fu">:</span> <span class="dv">1</span><span class="fu">,</span></span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;creationDate&quot;</span><span class="fu">:</span> <span class="st">&quot;2013-10-03T16:32:05&quot;</span><span class="fu">,</span></span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;updateDate&quot;</span><span class="fu">:</span> <span class="st">&quot;2013-10-03T16:32:05&quot;</span><span class="fu">,</span></span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;label&quot;</span><span class="fu">:</span> <span class="st">&quot;my JNDI ds&quot;</span><span class="fu">,</span></span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;description&quot;</span><span class="fu">:</span> <span class="st">&quot;Local JNDI Data Source&quot;</span><span class="fu">,</span></span>
<span id="cb1-17"><a href="#cb1-17" aria-hidden="true" tabindex="-1"></a>            <span class="er">//</span> <span class="er">URI</span> <span class="er">of</span> <span class="er">expanded</span> <span class="er">nested</span> <span class="er">resource</span> <span class="er">is</span> <span class="er">ignored.</span> <span class="er">Resource</span> <span class="er">is</span> <span class="er">created</span> <span class="er">locally</span></span>
<span id="cb1-18"><a href="#cb1-18" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;uri&quot;</span><span class="fu">:</span> <span class="st">&quot;/datasources/JServerJNDIDS&quot;</span><span class="fu">,</span></span>
<span id="cb1-19"><a href="#cb1-19" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;jndiName&quot;</span><span class="fu">:</span> <span class="st">&quot;jdbc/sugarcrm&quot;</span><span class="fu">,</span></span>
<span id="cb1-20"><a href="#cb1-20" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;timezone&quot;</span><span class="fu">:</span> <span class="kw">null</span></span>
<span id="cb1-21"><a href="#cb1-21" aria-hidden="true" tabindex="-1"></a>        <span class="fu">}</span></span>
<span id="cb1-22"><a href="#cb1-22" aria-hidden="true" tabindex="-1"></a>    <span class="fu">},</span></span>
<span id="cb1-23"><a href="#cb1-23" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;value&quot;</span><span class="fu">:</span> <span class="st">&quot;select distinct billing_address_country from accounts order by billing_address_country&quot;</span><span class="fu">,</span></span>
<span id="cb1-24"><a href="#cb1-24" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;language&quot;</span><span class="fu">:</span> <span class="st">&quot;sql&quot;</span></span>
<span id="cb1-25"><a href="#cb1-25" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
</tbody>
</table>

Use nested descriptors such as the ones above to create resources that contain local resources. Descriptors can be nested to any level, as long as the syntax of each descriptor is valid. See V2 Resource Descriptor Types for the correct syntax of both the parent and the nested resource.

Internally, the v2/repository service handles local resources as normal resources contained in a hidden folder. The hidden folder containing local resources has the following name:

\<parentURI\>\_files/

and local resources can be accessed at the following URI:

\<parentURI\>\_files/\<resourceID\>

In the example above, we can see that the parent query resource is a nested resource itself. Its URI shows us that it is the query resource for a query-based input-control of a topic resource:

/adhoc/topics/Cascading_multi_select_topic_files/Country_multi_select_files/country_query

and the new nested data source will have the following URI:

/adhoc/topics/Cascading_multi_select_topic_files/Country_multi_select_files/country_query_files/my_JNDI_ds

The ID of the nested resource (my_JNDI_ds) is created automatically from the label of the nested resource.

The \_files folder that exists in all parents of local resources is hidden so that its local resources do not appear in repository searches. You can set the showHiddenItems=true parameter on the v2/resources request to search a \_files folder for all local resources, such as in a JRXML report (reportUnit).

Local resources in the hidden \_files folder can also be created and updated separately from their parent resources by using PUT and POST methods of the v2/resources service and specifying the complete URI of the local resource as shown above.

### Optimistic Locking

The v2/resources service supports optimistic locking on all write and update operations (PUT, POST, and PATCH). When using the service to search the repository and receive descriptors of the resources, all descriptors contain a version number field. Clients should return the same version number when writing or updating a given resources. The server compares the version number in the modify request the current version of the resource to assure that no other client has updated the same resource.

If the version numbers do not match, the server replies with error code 409 Conflict. In that case, the client should request the resource again (read operation with GET) and send the modify request with an updated version number.

When a modify operation is successful, the server increments the version number on the affected resource and returns the new descriptor with the new version as confirmation that the operation was successful.

### Update-only Passwords

Some resource descriptors such as jdbcDataSource and xmlaConnection contain a password field. All password fields are blank or missing when reading (GET) a resource descriptor. This prevents anyone, even administrators from seeing existing passwords.

Write or update operations (PUT or POST) may send the password field in descriptors that support it. In this case, the password value is updated in the resource in the repository. Make sure that resources with sensitive passwords have the proper permissions so that only authorized users can modify them.
