---
title: Resource Descriptors
description: This chapter provides a reference by example for every type of resource descriptor that exists in the repository. Use the resources service to get and set resources with these descriptors. For...
---

# Resource Descriptors

This chapter provides a reference by example for every type of resource descriptor that exists in the repository. Use the resources service to get and set resources with these descriptors. For further information, see:

- [Chapter 1, “Working With Resources,” on page 1](working_with_resources.md) for general guidelines about using descriptors.
- [Chapter 1, “The resources Service,” on page 1](resources.md) for methods to operate on resources in the repository.

This chapter does not cover descriptors for objects that are not stored in the repository. Descriptors that represent jobs, calendars, organizations, roles, users, and attributes are described with the service that operates on them.

This chapter includes the following sections:

- Common Attributes
- Folder
- JNDI Data Source
- JDBC Data Source
- AWS Data Source
- Virtual Data Source
- Custom Data Source
- Bean Data Source
- Datatypes
- List of Values
- Query
- Input Control
- File
- Report Unit (JRXML Report)
- Report Options
- Domain (semanticLayerDataSource)
- Domain Topic
- XML/A Connection
- Mondrian Connection
- Secure Mondrian Connection
- OLAP Unit
- Mondrian XML/A Definition
- Other Types

## Common Attributes

All resource types contain the following attributes. Of these common attributes, only the label and description fields are writable.

In general, writable fields are ones that can be set by the client when sending a descriptor for a write or update operation (PUT or POST). The other fields are read-only fields that the server sets automatically.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p><span>application/repository.{resourceType}+json</span></p></th>
<th><p><span>application/repository.{resourceType}+xml</span></p></th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;uri&quot;</span> <span class="fu">:</span><span class="st">&quot;/sample/resource/uri&quot;</span><span class="fu">,</span> </span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;label&quot;</span><span class="fu">:</span><span class="st">&quot;Sample Label&quot;</span><span class="fu">,</span> </span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;description&quot;</span><span class="fu">:</span><span class="st">&quot;Sample Description&quot;</span><span class="fu">,</span> </span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;permissionMask&quot;</span><span class="fu">:</span><span class="st">&quot;0&quot;</span><span class="fu">,</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;creationDate&quot;</span><span class="fu">:</span> <span class="st">&quot;2013-07-04T12:18:47&quot;</span><span class="fu">,</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;updateDate&quot;</span><span class="fu">:</span> <span class="st">&quot;2013-07-04T12:18:47&quot;</span><span class="fu">,</span> </span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;version&quot;</span><span class="fu">:</span><span class="st">&quot;0&quot;</span></span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>    <span class="er">...</span> </span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="fu">&lt;?xml</span> <span class="ot">version=</span><span class="st">&quot;1.0&quot;</span> <span class="ot">encoding=</span><span class="st">&quot;UTF-8&quot;</span> <span class="ot">standalone=</span><span class="st">&quot;yes&quot;</span><span class="fu">?&gt;</span></span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a><span class="er">&lt;</span>{resourceType}&gt;</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">uri</span>&gt;/sample/resource/uri&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">label</span>&gt;Sample Label&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">description</span>&gt;Sample Description</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">description</span>&gt;</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">permissionMask</span>&gt;0&lt;/<span class="kw">permissionMask</span>&gt;</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">creationDate</span>&gt;2013-07-04T12:18:47</span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">creationDate</span>&gt;</span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">updateDate</span>&gt;2013-07-04T12:18:47</span>
<span id="cb2-11"><a href="#cb2-11" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">updateDate</span>&gt;</span>
<span id="cb2-12"><a href="#cb2-12" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">version</span>&gt;0&lt;/<span class="kw">version</span>&gt;</span>
<span id="cb2-13"><a href="#cb2-13" aria-hidden="true" tabindex="-1"></a>    ...</span>
<span id="cb2-14"><a href="#cb2-14" aria-hidden="true" tabindex="-1"></a><span class="er">&lt;</span>/{resourceType}&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

Only the label, description, and permission fields are writable. The other fields are generated by the server.

Throughout the rest of the resource type sections, the common attributes are included in every descriptor as `<commonAttributes>` in JSON or `{commonAttributes}` in XML.

## Folder

Folder types do not contain any additional fields beyond the common attributes shown above.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p><span>application/repository.folder+json</span></p></th>
<th><p><span>application/repository.folder+xml</span></p></th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;uri&quot;</span> <span class="fu">:</span><span class="st">&quot;&lt;resourceURI&gt;&quot;</span><span class="fu">,</span> </span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;label&quot;</span><span class="fu">:</span><span class="st">&quot;Sample Label&quot;</span><span class="fu">,</span> </span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;description&quot;</span><span class="fu">:</span><span class="st">&quot;Sample Description&quot;</span><span class="fu">,</span> </span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;permissionMask&quot;</span><span class="fu">:</span><span class="st">&quot;0&quot;</span><span class="fu">,</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;creationDate&quot;</span><span class="fu">:</span> <span class="st">&quot;2013-07-04T12:18:47&quot;</span><span class="fu">,</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;updateDate&quot;</span><span class="fu">:</span> <span class="st">&quot;2013-07-04T12:18:47&quot;</span><span class="fu">,</span> </span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;version&quot;</span><span class="fu">:</span><span class="st">&quot;0&quot;</span> </span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">folder</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">uri</span>&gt;{resourceURI}&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">label</span>&gt;Sample Label&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">description</span>&gt;Sample Description</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>      &lt;/<span class="kw">description</span>&gt;</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">permissionMask</span>&gt;0&lt;/<span class="kw">permissionMask</span>&gt;</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">creationDate</span>&gt;2013-07-04T12:18:47</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>      &lt;/<span class="kw">creationDate</span>&gt;</span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">updateDate</span>&gt;2013-07-04T12:18:47</span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a>       &lt;/<span class="kw">updateDate</span>&gt;</span>
<span id="cb2-11"><a href="#cb2-11" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">version</span>&gt;0&lt;/<span class="kw">version</span>&gt;</span>
<span id="cb2-12"><a href="#cb2-12" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">folder</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

Only the label and description fields are writable.

## JNDI Data Source

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p><span>application/repository.jndiJdbcDataSource+json</span></p></th>
<th><p><span>application/repository.jndiJdbcDataSource+xml</span></p></th>
</tr>
</thead>
<tbody>
<tr>
<td><pre class="text"><code>{
    &lt;commonAttributes&gt;,
    &quot;jndiName&quot;:&quot;&lt;jndiName&gt;&quot;,
    &quot;timezone&quot;:&quot;&lt;timezone&gt;&quot;
}</code></pre></td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">jndiDataSource</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    {commonAttributes}</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">jndiName</span>&gt;{jndiName}&lt;/<span class="kw">jndiName</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">timezone</span>&gt;{timezone}&lt;/<span class="kw">timezone</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">jndiDataSource</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

## JDBC Data Source

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p><span>application/repository.jdbcDataSource+json</span></p></th>
<th><p><span>application/repository.jdbcDataSource+xml</span></p></th>
</tr>
</thead>
<tbody>
<tr>
<td><pre class="text"><code>{
    &lt;commonAttributes&gt;,
    &quot;driverClass&quot;:&quot;&lt;driverClass&gt;&quot;,
    &quot;password&quot;:&quot;&lt;password&gt;&quot;,
    &quot;username&quot;:&quot;&lt;username&gt;&quot;,
    &quot;connectionUrl&quot;:&quot;&lt;connectionURL&gt;&quot;,
    &quot;timezone&quot;:&quot;&lt;timezone&gt;&quot;
}</code></pre></td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">jdbcDataSource</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    {commonAttributes}</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">driverClass</span>&gt;{driverClass}&lt;/<span class="kw">driverClass</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">password</span>&gt;{password}&lt;/<span class="kw">password</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">username</span>&gt;{username}&lt;/<span class="kw">username</span>&gt;</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">connectionUrl</span>&gt;</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>         {connectionURL}</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">connectionUrl</span>&gt;</span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">timezone</span>&gt;{timezone}&lt;/<span class="kw">timezone</span>&gt;</span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">jdbcDataSource</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

## AWS Data Source

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p><span>application/repository.awsDataSource+json</span></p></th>
<th><p><span>application/repository.awsDataSource+xml</span></p></th>
</tr>
</thead>
<tbody>
<tr>
<td><pre class="text"><code>{
    &lt;commonAttributes&gt;,
    &quot;driverClass&quot;:&quot;&lt;driverClass&gt;&quot;,
    &quot;password&quot;:&quot;&lt;password&gt;&quot;,
    &quot;username&quot;:&quot;&lt;username&gt;&quot;,
    &quot;connectionUrl&quot;:&quot;&lt;connectionURL&gt;&quot;,
    &quot;timezone&quot;:&quot;&lt;timezone&gt;&quot;,
    &quot;accessKey&quot;:&quot;&lt;accessKey&gt;&quot;,
    &quot;secretKey&quot;:&quot;&lt;secretKey&gt;&quot;,
    &quot;roleArn&quot;:&quot;&lt;roleArn&gt;&quot;,
    &quot;region&quot;:&quot;&lt;region&gt;&quot;,
    &quot;dbName&quot;:&quot;&lt;dbName&gt;&quot;,
    &quot;dbInstanceIdentifier&quot;:
        &quot;&lt;dbInstanceIdentifier&gt;&quot;,
    &quot;dbService&quot;:&quot;&lt;dbService&gt;&quot;
}</code></pre></td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">awsDataSource</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    {commonAttributes}</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">driverClass</span>&gt;{driverClass}&lt;/<span class="kw">driverClass</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">password</span>&gt;{password}&lt;/<span class="kw">password</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">username</span>&gt;{username}&lt;/<span class="kw">username</span>&gt;</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">connectionUrl</span>&gt;</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>         {connectionURL}</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">connectionUrl</span>&gt;</span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">timezone</span>&gt;{timezone}&lt;/<span class="kw">timezone</span>&gt;</span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">accessKey</span>&gt;{accessKey}&lt;/<span class="kw">accessKey</span>&gt; </span>
<span id="cb2-11"><a href="#cb2-11" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">secretKey</span>&gt;{secretKey}&lt;/<span class="kw">secretKey</span>&gt; </span>
<span id="cb2-12"><a href="#cb2-12" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">roleArn</span>&gt;{roleArn}&lt;/<span class="kw">roleArn</span>&gt; </span>
<span id="cb2-13"><a href="#cb2-13" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">region</span>&gt;{region}&lt;/<span class="kw">region</span>&gt; </span>
<span id="cb2-14"><a href="#cb2-14" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">dbName</span>&gt;{dbName}&lt;/<span class="kw">dbName</span>&gt; </span>
<span id="cb2-15"><a href="#cb2-15" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">dbInstanceIdentifier</span>&gt; </span>
<span id="cb2-16"><a href="#cb2-16" aria-hidden="true" tabindex="-1"></a>        {dbInstanceIdentifier}</span>
<span id="cb2-17"><a href="#cb2-17" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">dbInstanceIdentifier</span>&gt; </span>
<span id="cb2-18"><a href="#cb2-18" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">dbService</span>&gt;{dbService}&lt;/<span class="kw">dbService</span>&gt;</span>
<span id="cb2-19"><a href="#cb2-19" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">awsDataSource</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

The `{region}` values are specified in the file .../WEB-INF/application-context.xml, with their corresponding display labels defined in .../WEB-INF/bundles/jasperserver_messages.properties. By default, the following regions are defined:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>Values of AWS {region} in<br />
<span>.../WEB-INF/application-context.xml</span></p></th>
<th><p>Labels for AWS regions in<br />
<span>.../WEB-INF/bundles/jasperserver_messages.properties</span></p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>us-east-1.amazonaws.com</code></p></td>
<td><p><code>US East (Northern Virginia) Region</code></p></td>
</tr>
<tr>
<td><code>us-west-2.amazonaws.com</code></td>
<td><code>US West (Oregon) Region</code></td>
</tr>
<tr>
<td><code>us-west-1.amazonaws.com</code></td>
<td><code>US West (Northern California) Region</code></td>
</tr>
<tr>
<td>eu-west-1.amazonaws.com</td>
<td><code>EU (Ireland) Region</code></td>
</tr>
<tr>
<td><code>eu-central-1.amazonaws.com</code></td>
<td><code>EU (Frankfurt) Region</code></td>
</tr>
<tr>
<td><code>ap-southeast-1.amazonaws.com</code></td>
<td><code>Asia Pacific (Singapore) Region</code></td>
</tr>
<tr>
<td><code>ap-southeast-2.amazonaws.com</code></td>
<td><code>Asia Pacific (Sydney) Region</code></td>
</tr>
<tr>
<td><code>ap-northeast-1.amazonaws.com</code></td>
<td><code>Asia Pacific (Tokyo) Region</code></td>
</tr>
<tr>
<td><code>sa-east-1.amazonaws.com</code></td>
<td><code>South America (São Paulo) Region</code></td>
</tr>
</tbody>
</table>

## Virtual Data Source

The `id` of each `subDataSource` must be unique. The server does not prevent duplicates, and the last one to be defined silently overwrites the previous definition.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p><span>application/repository.virtualDataSource+json</span></p></th>
<th><p><span>application/repository.virtualDataSource+xml</span></p></th>
</tr>
</thead>
<tbody>
<tr>
<td><pre class="text"><code>{
    &lt;commonAttributes&gt;,
    &quot;subDataSources&quot;:[
        {
            &quot;id&quot;:&quot;&lt;subDataSourceID&gt;&quot;,
            &quot;uri&quot;:&quot;&lt;subDataSourceURI&gt;&quot;
        },
        ...
    ]
}</code></pre></td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">virtualDataSource</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    {commonAttributes}</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">subDataSources</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">subDataSource</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">id</span>&gt;{subDataSourceID}&lt;/<span class="kw">id</span>&gt;</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">uri</span>&gt;{subDataSourceURI}&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">subDataSource</span>&gt;</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>        ...</span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">subDataSources</span>&gt;</span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">virtualDataSource</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

## Custom Data Source

The value of the `serviceClass` attribute is read-only and depends on the specific type of the custom data source, as defined in the server's applicationContext configuration files.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p><span>application/repository.customDataSource+json</span></p></th>
<th><p><span>application/repository.customDataSource+xml</span></p></th>
</tr>
</thead>
<tbody>
<tr>
<td><pre class="text"><code>{
    &lt;commonAttributes&gt;,
    &quot;serviceClass&quot;:&quot;&lt;serviceClass&gt;&quot;,
    &quot;dataSourceName&quot;:&quot;&lt;dataSourceName&gt;&quot;,
    &quot;properties&quot;:[
        {
            &quot;key&quot;:&quot;&lt;key&gt;&quot;,
            &quot;value&quot;:&quot;&lt;value&gt;&quot;
        },
        ...
    ]
}</code></pre></td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">customDataSource</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    {commonAttributes}</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">serviceClass</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>        {serviceClass}</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">serviceClass</span>&gt;</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">dataSourceName</span>&gt;</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>        {dataSourceName}</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">dataSourceName</span>&gt;</span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">properties</span>&gt;</span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">property</span>&gt;</span>
<span id="cb2-11"><a href="#cb2-11" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">key</span>&gt;{key}&lt;/<span class="kw">key</span>&gt;</span>
<span id="cb2-12"><a href="#cb2-12" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">value</span>&gt;{value}&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-13"><a href="#cb2-13" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">property</span>&gt;</span>
<span id="cb2-14"><a href="#cb2-14" aria-hidden="true" tabindex="-1"></a>        ...</span>
<span id="cb2-15"><a href="#cb2-15" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">properties</span>&gt;</span>
<span id="cb2-16"><a href="#cb2-16" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">customDataSource</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

## Bean Data Source

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p><span>application/repository.beanDataSource+json</span></p></th>
<th><p><span>application/repository.beanDataSource+xml</span></p></th>
</tr>
</thead>
<tbody>
<tr>
<td><pre class="text"><code>{
    &lt;commonAttributes&gt;,
    &quot;beanName&quot;:&quot;&lt;beanName&gt;&quot;,
    &quot;beanMethod&quot;:&quot;&lt;beanMethod&gt;&quot;
}</code></pre></td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">beanDataSource</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    {commonAttributes}</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">beanName</span>&gt;{beanName}&lt;<span class="kw">beanName</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">beanMethod</span>&gt;{beanMethod}&lt;/<span class="kw">beanMethod</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">beanDataSource</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

## Datatypes

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p><span>application/repository.dataType+json</span></p></th>
<th><p><span>application/repository.dataType+xml</span></p></th>
</tr>
</thead>
<tbody>
<tr>
<td><pre class="text"><code>{
    &lt;commonAttributes&gt;,
    &quot;type&quot;:&quot;text|number|date|dateTime|time&quot;,
    &quot;pattern&quot;:&quot;&lt;pattern&gt;&quot;,
    &quot;maxValue&quot;:&quot;&lt;maxValue&gt;&quot;,
    &quot;strictMax&quot;:&quot;true|false&quot;,
    &quot;minValue&quot;:&quot;&lt;minValue&gt;&quot;,
    &quot;strictMin&quot;:&quot;true|false&quot;
    &quot;maxLength&quot;:&quot;&lt;maxLengthInteger&gt;&quot;
}</code></pre></td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">dataType</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    {commonAttributes}</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">type</span>&gt;text|number|date|dateTime|time&lt;/<span class="kw">type</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">pattern</span>&gt;{pattern}&lt;/<span class="kw">pattern</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">maxValue</span>&gt;{maxValue}&lt;/<span class="kw">maxValue</span>&gt;</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">strictMax</span>&gt;true|false&lt;/<span class="kw">strictMax</span>&gt;</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">minValue</span>&gt;{minValue}&lt;/<span class="kw">minValue</span>&gt;</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">strictMin</span>&gt;true|false&lt;/<span class="kw">strictMin</span>&gt;</span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">maxLength</span>&gt;{maxLengthInteger}&lt;/<span class="kw">maxLength</span>&gt;</span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">dataType</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

## List of Values

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p><span>application/repository.listOfValues+json</span></p></th>
<th><p><span>application/repository.listOfValues+xml</span></p></th>
</tr>
</thead>
<tbody>
<tr>
<td><pre class="text"><code>{
    &lt;commonAttributes&gt;,
    &quot;items&quot;:[
        {
            &quot;label&quot;:&quot;&lt;label&gt;&quot;,
            &quot;value&quot;:&quot;&lt;value&gt;&quot;
        },
        ...
    ]
}</code></pre></td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">listOfValues</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    {commonAttributes}</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">items</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">item</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">label</span>&gt;{label}&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">value</span>&gt;{value}&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">item</span>&gt;</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>        ...</span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">items</span>&gt;</span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">listOfValues</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

## Query

The dataSource field of the query may be null. Set an empty dataSource field when you want to remove a local data source, either a reference or a local definition. When the data source of a query is not defined, the query uses the data source of its parent, for example its JRXML report (reportUnit).

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p><span>application/repository.query+json</span></p></th>
<th><p><span>application/repository.query+xml</span></p></th>
</tr>
</thead>
<tbody>
<tr>
<td><pre class="text"><code>{
    &lt;commonAttributes&gt;,
    &quot;value&quot;:&quot;&lt;query&gt;&quot;,
    &quot;language&quot;:&quot;&lt;language&gt;&quot;,
    &quot;dataSource&quot;:{
        &quot;dataSourceReference&quot;: {
            &quot;uri&quot;:&quot;&lt;dataSourceURI&gt;&quot;
        }
    }
}</code></pre></td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">query</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    {commonAttributes}</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;{query}&lt;/<span class="kw">value</span>&gt; </span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">language</span>&gt;{language}&lt;/<span class="kw">language</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">dataSourceReference</span>&gt;</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">uri</span>&gt;{dataSourceURI}&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">dataSourceReference</span>&gt;</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">query</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

## Input Control

Input controls come in several types that require different fields. The following table shows all possible fields, not all of which are mutually compatible.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p><span>application/repository.inputControl+json</span></p></th>
<th><p><span>application/repository.inputControl+xml</span></p></th>
</tr>
</thead>
<tbody>
<tr>
<td><pre class="text"><code>{
    &lt;commonAttributes&gt;,
    &quot;mandatory&quot;:&quot;true|false&quot;,
    &quot;readOnly&quot;:&quot;true|false&quot;, &quot;readOnlyExpression&quot;:&quot;&lt;comparisonExpression&gt;&quot;,
    &quot;visible&quot;:&quot;true|false&quot;,
   &quot;visibilityExpression&quot;:&quot;&lt;comparisonExpression&gt;&quot;,   &quot;type&quot;:&quot;&lt;inputControlTypeByteValue&gt;&quot;,
    &quot;usedFields&quot;:&quot;&lt;field1;field2;...&gt;&quot;,
    &quot;dataType&quot;: {
        &quot;dataTypeReference&quot;: {
            &quot;uri&quot;: &quot;&lt;dataTypeResourceURI&gt;&quot;
        }
    },
    &quot;listOfValues&quot;: {
        &quot;listOfValuesReference&quot;: {
            &quot;uri&quot;: &quot;&lt;listOfValuesResourceURI&gt;&quot;
        }
    }
    &quot;visibleColumns&quot;:[&quot;column1&quot;, &quot;colum2&quot;, ...],
    &quot;valueColumn&quot;:&quot;&lt;valueColumn&gt;&quot;,
    &quot;query&quot;: {
        &quot;queryReference&quot;: {
            &quot;uri&quot;: &quot;&lt;queryResourceURI&gt;&quot;
        }
    }
}</code></pre></td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">inputControl</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    {commonAttributes}</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">mandatory</span>&gt;true|false&lt;/<span class="kw">mandatory</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a> &lt;<span class="kw">readOnly</span>&gt;true|false&lt;/<span class="kw">readOnly</span>&gt; &lt;<span class="kw">readOnlyExpression</span>&gt;{comparisonExpression}&lt;/<span class="kw">readOnlyExpression</span>&gt;  &lt;<span class="kw">visible</span>&gt;true|false&lt;/<span class="kw">visible</span>&gt;&lt;<span class="kw">visibilityExpression</span>&gt;{comparisonExpression}&lt;/<span class="kw">visibilityExpression</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">type</span>&gt;{inputControlTypeByteValue}&lt;/<span class="kw">type</span>&gt;</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">usedFields</span>&gt;{field1;field2;...}&lt;/<span class="kw">usedFields</span>&gt;</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">dataTypeReference</span>&gt;</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">uri</span>&gt;{dataTypeResourceURI}&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">dataTypeReference</span>&gt;</span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">listOfValuesReference</span>&gt;</span>
<span id="cb2-11"><a href="#cb2-11" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">uri</span>&gt;{listOfValuesResourceURI}&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb2-12"><a href="#cb2-12" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">listOfValuesReference</span>&gt;</span>
<span id="cb2-13"><a href="#cb2-13" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">queryReference</span>&gt;</span>
<span id="cb2-14"><a href="#cb2-14" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">uri</span>&gt;{queryResourceURI}&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb2-15"><a href="#cb2-15" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">queryReference</span>&gt;</span>
<span id="cb2-16"><a href="#cb2-16" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">visibleColumns</span>&gt;</span>
<span id="cb2-17"><a href="#cb2-17" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">column</span>&gt;{column1}&lt;/<span class="kw">column</span>&gt;</span>
<span id="cb2-18"><a href="#cb2-18" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">column</span>&gt;{column2}&lt;/<span class="kw">column</span>&gt;</span>
<span id="cb2-19"><a href="#cb2-19" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">column</span>&gt;...&lt;/<span class="kw">column</span>&gt;</span>
<span id="cb2-20"><a href="#cb2-20" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">visibleColumns</span>&gt;</span>
<span id="cb2-21"><a href="#cb2-21" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">valueColumn</span>&gt;{valueColumn}&lt;/<span class="kw">valueColumn</span>&gt;</span>
<span id="cb2-22"><a href="#cb2-22" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">inputControl</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

The following list shows the numerical code and meaning for {inputControlTypeByteValue}. The input control type determines the other fields that are required. The list of required fields may appear in a field named usedFields, separated by semi-colons (`;`).

| Type | Type of Input Control | Other Fields Required (usedFields) |
|----|----|----|
| 1 | Boolean | None |
| 2 | Single value | dataType |
| 3 | Single-select list of values | listOfValues |
| 4 | Single-select query | query; queryValueColumn |
| 5 | Not used |  |
| 6 | Multi-select list of values | listOfValues |
| 7 | Multi-select query | query; queryValueColumn |
| 8 | Single-select list of values radio buttons | listOfValues |
| 9 | Single-select query radio buttons | query; queryValueColumn |
| 10 | Multi-select list of values check boxes | listOfValues |
| 11 | Multi-select query check boxes | query; queryValueColumn |

## File

The repository.file+\<format\> descriptor is used to identify the file type.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p><span>application/repository.file+json</span></p></th>
<th><p><span>application/repository.file+xml</span></p></th>
</tr>
</thead>
<tbody>
<tr>
<td><pre class="text"><code>{
    &lt;commonAttributes&gt;,
    &quot;type&quot;:&quot;pdf|html|rtf|csv|odt|txt
            |docx|ods|xlsx|img|font|jrxml
            |jar|prop|jrtx|xml|css
            |olapMondrianSchema
            |accessGrantSchema
            |unspecified&quot;,
    &quot;content&quot;:&quot;&lt;base64EncodedContent&gt;&quot;
}</code></pre></td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">file</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    {commonAttributes}</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">type</span>&gt;pdf|html|rtf|csv|odt|txt</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>        |docx|ods|xlsx|img|font|jrxml</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>        |jar|prop|jrtx|xml|css</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>        |olapMondrianSchema</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>        |accessGrantSchema|unspecified</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">type</span>&gt;</span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">content</span>&gt;{base64EncodedContent}&lt;/<span class="kw">content</span>&gt;</span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">file</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

The `content` field is write-only: it is absent when requesting the file resource descriptor and used only when uploading a file resource as base-64 encoded content. For other ways to upload file contents, see [1.1, “Uploading File Resources,” on page 1](file_resources.md). To download file contents, see [1.1, “Downloading File Resources,” on page 1](file_resources.md).

## Report Unit (JRXML Report)

A report unit contains mostly references to the files that make up a report within the server. A report unit is a composite resource that may contain other local resources (see [1.1, “Nested Resources,” on page 1](working_with_resources.md)). In this case, the URIs that it references include a URI in the following format:

\<reportUnitURI\>\_files/\<localResourceID\>

For example, the main JRXML of a sample report is referenced as follows:

/reports/samples/Cascading_multi_select_report_files/Cascading_multi_select_report

The default value for the `controlsLayout` is `popupScreen`. The `reportRenderingView` and the `inputControlRenderingView` can be left as empty strings (`""`), while the `query` can be null.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p><span>application/repository.reportUnit+json</span></p></th>
<th><p><span>application/repository.reportUnit+xml</span></p></th>
</tr>
</thead>
<tbody>
<tr>
<td><pre class="text"><code>{
    &lt;commonAttributes&gt;,
    &quot;controlsLayout&quot;:&quot;&lt;popupScreen|separatePage
          |topOfPage|inPage&gt;&quot;,</code></pre></td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">reportUnit</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    {commonAttributes}</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">controlsLayout</span>&gt;popupScreen|separatePage</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>        |topOfPage|inPage&lt;/<span class="kw">controlsLayout</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td><pre class="text"><code>    &quot;alwaysPromptControls&quot;:&quot;true|false&quot;,
    &quot;inputControlRenderingView&quot;:
        &quot;&lt;inputControlRenderingView&gt;&quot;,
    &quot;reportRenderingView&quot;:
        &quot;&lt;reportRenderingView&gt;&quot;,
    &quot;dataSource&quot;:{
        &quot;dataSourceReference&quot;: {
            &quot;uri&quot;:&quot;&lt;dataSourceURI&gt;&quot;
        }
    },
    &quot;query:&quot; {
        &quot;queryReference&quot;: {
            uri: &quot;&lt;queryResourceURI&gt;&quot;
        }
    },
    &quot;jrxml&quot;: {
        &quot;jrxmlFileReference&quot;: {
            &quot;uri&quot;: &quot;&lt;jrxmlFileResourceURI&gt;&quot;
        } or
        &quot;jrxmlFile&quot;: {
            &quot;type&quot;: &quot;jrxml&quot;,
            &quot;label&quot;: &quot;Main jrxml&quot;,
            &quot;content&quot;: &quot;&lt;base64Encoded&gt;
        }
    },
    &quot;inputControls&quot;: [
        {
            &quot;inputControlReference&quot;: {
                &quot;uri&quot;: &quot;&lt;inputControlURI&gt;&quot;
            }
        },
        ...
    ],
    &quot;resources&quot;: {
        &quot;resource&quot;: [{
            &quot;name&quot;: &quot;&lt;resourceName&gt;&quot;,
            &quot;fileReference&quot;: {
                &quot;uri&quot;: &quot;&lt;fileResourceURI&gt;&quot;
            }
        }],
        &quot;resource&quot;: [{
            &quot;name&quot;: &quot;Logo&quot;,
            &quot;file&quot;: {
                &quot;fileResource&quot;: {
                    &quot;type&quot;: &quot;img&quot;,
                    &quot;label&quot;: &quot;Logo.png&quot;,
                    &quot;content&quot;:&quot;&lt;base64Encoded&gt;&quot;
                }
            }
        }]
        ...
    }
}</code></pre></td>
<td><div class="sourceCode" id="cb4"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb4-1"><a href="#cb4-1" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">alwaysPromptControls</span>&gt;true|false</span>
<span id="cb4-2"><a href="#cb4-2" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">alwaysPromptControls</span>&gt;</span>
<span id="cb4-3"><a href="#cb4-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">inputControlRenderingView</span>&gt;</span>
<span id="cb4-4"><a href="#cb4-4" aria-hidden="true" tabindex="-1"></a>        {inputControlRenderingView}</span>
<span id="cb4-5"><a href="#cb4-5" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">inputControlRenderingView</span>&gt;</span>
<span id="cb4-6"><a href="#cb4-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">reportRenderingView</span>&gt;</span>
<span id="cb4-7"><a href="#cb4-7" aria-hidden="true" tabindex="-1"></a>        {reportRenderingView}</span>
<span id="cb4-8"><a href="#cb4-8" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">reportRenderingView</span>&gt;</span>
<span id="cb4-9"><a href="#cb4-9" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">dataSource</span>&gt;</span>
<span id="cb4-10"><a href="#cb4-10" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">dataSourceReference</span>&gt;</span>
<span id="cb4-11"><a href="#cb4-11" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">uri</span>&gt;{dataSourceURI}&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb4-12"><a href="#cb4-12" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">dataSourceReference</span>&gt;</span>
<span id="cb4-13"><a href="#cb4-13" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">dataSource</span>&gt;</span>
<span id="cb4-14"><a href="#cb4-14" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">query</span>&gt;</span>
<span id="cb4-15"><a href="#cb4-15" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">queryReference</span>&gt;</span>
<span id="cb4-16"><a href="#cb4-16" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">uri</span>&gt;{queryResourceURI}&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb4-17"><a href="#cb4-17" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">queryReference</span>&gt;</span>
<span id="cb4-18"><a href="#cb4-18" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">query</span>&gt;</span>
<span id="cb4-19"><a href="#cb4-19" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">jrxml</span>&gt;  </span>
<span id="cb4-20"><a href="#cb4-20" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">jrxmlFileReference</span>&gt;</span>
<span id="cb4-21"><a href="#cb4-21" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">uri</span>&gt;{jrxmlFileResourceURI}&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb4-22"><a href="#cb4-22" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">jrxmlFileReference</span>&gt;</span>
<span id="cb4-23"><a href="#cb4-23" aria-hidden="true" tabindex="-1"></a>        or &lt;<span class="kw">jrxmlFile</span>&gt;</span>
<span id="cb4-24"><a href="#cb4-24" aria-hidden="true" tabindex="-1"></a>               &lt;<span class="kw">type</span>&gt;jrxml&lt;/<span class="kw">type</span>&gt;</span>
<span id="cb4-25"><a href="#cb4-25" aria-hidden="true" tabindex="-1"></a>               &lt;<span class="kw">label</span>&gt;Main report&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb4-26"><a href="#cb4-26" aria-hidden="true" tabindex="-1"></a>               &lt;<span class="kw">content</span>&gt;{base64Encoded}</span>
<span id="cb4-27"><a href="#cb4-27" aria-hidden="true" tabindex="-1"></a>               &lt;/<span class="kw">content</span>&gt;</span>
<span id="cb4-28"><a href="#cb4-28" aria-hidden="true" tabindex="-1"></a>           &lt;/<span class="kw">jrxmlFile</span>&gt;</span>
<span id="cb4-29"><a href="#cb4-29" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">jrxml</span>&gt;</span>
<span id="cb4-30"><a href="#cb4-30" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">inputControls</span>&gt;</span>
<span id="cb4-31"><a href="#cb4-31" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">inputControlReference</span>&gt;</span>
<span id="cb4-32"><a href="#cb4-32" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">uri</span>&gt;{inputControlURI}&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb4-33"><a href="#cb4-33" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">inputControlReference</span>&gt;</span>
<span id="cb4-34"><a href="#cb4-34" aria-hidden="true" tabindex="-1"></a>        ...</span>
<span id="cb4-35"><a href="#cb4-35" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">inputControls</span>&gt;</span>
<span id="cb4-36"><a href="#cb4-36" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resources</span>&gt;</span>
<span id="cb4-37"><a href="#cb4-37" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">resource</span>&gt;</span>
<span id="cb4-38"><a href="#cb4-38" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">name</span>&gt;{resourceName}&lt;/<span class="kw">name</span>&gt;</span>
<span id="cb4-39"><a href="#cb4-39" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">fileReference</span>&gt;</span>
<span id="cb4-40"><a href="#cb4-40" aria-hidden="true" tabindex="-1"></a>                &lt;<span class="kw">uri</span>&gt;{fileResourceURI}&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb4-41"><a href="#cb4-41" aria-hidden="true" tabindex="-1"></a>            &lt;/<span class="kw">fileReference</span>&gt;</span>
<span id="cb4-42"><a href="#cb4-42" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">resource</span>&gt;</span>
<span id="cb4-43"><a href="#cb4-43" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">resource</span>&gt;</span>
<span id="cb4-44"><a href="#cb4-44" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">name</span>&gt;Logo&lt;/<span class="kw">name</span>&gt;</span>
<span id="cb4-45"><a href="#cb4-45" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">file</span>&gt;</span>
<span id="cb4-46"><a href="#cb4-46" aria-hidden="true" tabindex="-1"></a>                &lt;<span class="kw">type</span>&gt;img&lt;/<span class="kw">type</span>&gt;</span>
<span id="cb4-47"><a href="#cb4-47" aria-hidden="true" tabindex="-1"></a>                &lt;<span class="kw">label</span>&gt;Logo.png&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb4-48"><a href="#cb4-48" aria-hidden="true" tabindex="-1"></a>                &lt;<span class="kw">content</span>&gt;{base64Encoded}</span>
<span id="cb4-49"><a href="#cb4-49" aria-hidden="true" tabindex="-1"></a>                &lt;/<span class="kw">content</span>&gt;</span>
<span id="cb4-50"><a href="#cb4-50" aria-hidden="true" tabindex="-1"></a>            &lt;/<span class="kw">file</span>&gt;</span>
<span id="cb4-51"><a href="#cb4-51" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">resource</span>&gt;</span>
<span id="cb4-52"><a href="#cb4-52" aria-hidden="true" tabindex="-1"></a>        ...</span>
<span id="cb4-53"><a href="#cb4-53" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resources</span>&gt;    </span>
<span id="cb4-54"><a href="#cb4-54" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">reportUnit</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

## Report Options

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p><span>application/repository.reportOptions+json</span></p></th>
<th><p><span>application/repository.reportOptions+xml</span></p></th>
</tr>
</thead>
<tbody>
<tr>
<td><pre class="text"><code>{
    &lt;commonAttributes&gt;,
    &quot;reportUri&quot;:&quot;&lt;reportURI&gt;&quot;,
    &quot;reportParameters&quot;:[
        {
            &quot;name&quot;:&quot;&lt;parameterName&gt;&quot;,
            &quot;value&quot;:[
                &quot;value_1&quot;,
                &quot;value_2&quot;,
                ...
            ]
        },
        ...
    ]
}</code></pre></td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">reportOptions</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    {commonAttributes}</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">reportUri</span>&gt;{reportURI}&lt;/<span class="kw">reportUri</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">reportParameters</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">reportParameter</span>&gt;</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">name</span>&gt;{parameterName}&lt;/<span class="kw">name</span>&gt;</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">value</span>&gt;value_1&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">value</span>&gt;value_2&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>            ...</span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">reportParameter</span>&gt;</span>
<span id="cb2-11"><a href="#cb2-11" aria-hidden="true" tabindex="-1"></a>        ...</span>
<span id="cb2-12"><a href="#cb2-12" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">reportParameters</span>&gt;</span>
<span id="cb2-13"><a href="#cb2-13" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">reportOptions</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

## Domain (semanticLayerDataSource)

For more information about accessing the schema of a Domain, see [Chapter 1, “Working With Domains,” on page 1](metadata.md).

When the `locale` property is left empty, the default locale bundle is used.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p><span>application/repository.semanticLayerDataSource+json</span></p></th>
<th><p><span>application/repository.semanticLayerDataSource+xml</span></p></th>
</tr>
</thead>
<tbody>
<tr>
<td><pre class="text"><code>{
    &lt;commonAttributes&gt;,
    &quot;dataSource&quot;:{
        &quot;dataSourceReference&quot;: {
            &quot;uri&quot;:&quot;&lt;dataSourceURI&gt;&quot;
    }   },
    &quot;schema&quot;: {
        &quot;schemaFileReference&quot;: {
            &quot;uri&quot;: &quot;&lt;schemaFileURI&gt;&quot;
    }   },
    &quot;bundles&quot;: [{
        &quot;locale&quot;: &quot;&lt;localeString&gt;&quot;,
        &quot;file&quot;: {
            &quot;fileReference&quot;: {&quot;uri&quot;:
                &quot;&lt;propertiesFileURI&gt;&quot;
        }   }   },
        ...
    ],
    &quot;securityFile&quot;: {
        &quot;securityFileReference&quot;: {
            &quot;uri&quot;: &quot;&lt;securityFileURI&gt;&quot;
}   }   }</code></pre></td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">semanticLayerDataSource</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    {commonAttributes}</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">dataSourceReference</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">uri</span>&gt;{dataSourceURI}&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">dataSourceReference</span>&gt;</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">schemaFileReference</span>&gt;</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">uri</span>&gt;{schemaFileURI}&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">schemaFileReference</span>&gt;</span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">bundles</span>&gt;</span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">bundle</span>&gt;</span>
<span id="cb2-11"><a href="#cb2-11" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">locale</span>&gt;{localeString}&lt;/<span class="kw">locale</span>&gt;</span>
<span id="cb2-12"><a href="#cb2-12" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">fileReference</span>&gt;</span>
<span id="cb2-13"><a href="#cb2-13" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">uri</span>&gt;{propertiesFileURI}&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb2-14"><a href="#cb2-14" aria-hidden="true" tabindex="-1"></a>            &lt;/<span class="kw">fileReference</span>&gt;</span>
<span id="cb2-15"><a href="#cb2-15" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">bundle</span>&gt; </span>
<span id="cb2-16"><a href="#cb2-16" aria-hidden="true" tabindex="-1"></a>        ...</span>
<span id="cb2-17"><a href="#cb2-17" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">bundles</span>&gt; </span>
<span id="cb2-18"><a href="#cb2-18" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">securityFileReference</span>&gt;</span>
<span id="cb2-19"><a href="#cb2-19" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">uri</span>&gt;{securityFileURI}&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb2-20"><a href="#cb2-20" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">securityFileReference</span>&gt;</span>
<span id="cb2-21"><a href="#cb2-21" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">semanticLayerDataSource</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

## Domain Topic

A Domain Topic is a Topic created by selecting database fields from a Domain. It is structurally equivalent to a JRXML report, and thus it has the same type attributes (see Report Unit (JRXML Report)). The only difference is that the data source field will reference a Domain (semanticLayerDataSource).

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p><span>application/repository.domainTopic+json</span></p></th>
<th><p><span>application/repository.domainTopic+xml</span></p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Same attributes as<br />
<span>application/repository.reportUnit+json</span></p></td>
<td><p>Same attributes as<br />
<span>application/repository.reportUnit+xml</span></p></td>
</tr>
</tbody>
</table>

## XML/A Connection

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p><span>application/repository.xmlaConnection+json</span></p></th>
<th><p><span>application/repository.xmlaConnection+xml</span></p></th>
</tr>
</thead>
<tbody>
<tr>
<td><pre class="text"><code>{
    &lt;commonAttributes&gt;,
    &quot;url&quot;:&quot;&lt;xmlaServiceURL&gt;&quot;,
    &quot;xmlaDataSource&quot;:&quot;&lt;xmlaDataSource&gt;&quot;,
    &quot;catalog&quot;:&quot;&lt;catalog&gt;&quot;,
    &quot;username&quot;:&quot;&lt;username&gt;&quot;,
    &quot;password&quot;:&quot;&lt;password&gt;&quot;
}</code></pre></td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">xmlaConnection</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    {commonAttributes}</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">url</span>&gt;{xmlaServiceURL}&lt;/<span class="kw">url</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">xmlaDataSource</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>        {xmlaDataSource}</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">xmlaDataSource</span>&gt;</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">catalog</span>&gt;{catalog}&lt;/<span class="kw">catalog</span>&gt;</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">username</span>&gt;{username}&lt;/<span class="kw">username</span>&gt;</span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">password</span>&gt;{password}&lt;/<span class="kw">password</span>&gt;</span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">xmlaConnection</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

## Mondrian Connection

Mondrian connections without the access grant schemas are used in the Community edition of JasperReports Server.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p><span>application/repository.mondrianConnection+json</span></p></th>
<th><p><span>application/repository.mondrianConnection+xml</span></p></th>
</tr>
</thead>
<tbody>
<tr>
<td><pre class="text"><code>{
    &lt;commonAttributes&gt;,
    &quot;dataSource&quot;:{
        &quot;dataSourceReference&quot;: {
            &quot;uri&quot;:&quot;&lt;dataSourceURI&gt;&quot;
        }
    },
    &quot;schema&quot;: {
        &quot;schemaReference&quot;: {
            &quot;uri&quot;: &quot;&lt;schemaFileResourceURI&gt;&quot;
        }
    }
}</code></pre></td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">mondrianConnection</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    {commonAttributes}</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">dataSourceReference</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">uri</span>&gt;{dataSourceURI}&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">dataSourceReference</span>&gt;</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">schemaReference</span>&gt;</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">uri</span>&gt;{schemaFileResourceURI}&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">schemaReference</span>&gt;</span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">mondrianConnection</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

## Secure Mondrian Connection

Secure Mondrian connections are available only in commercial releases of JasperReports Server.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p><span>application/repository.secureMondrianConnection+json</span></p></th>
<th><p><span>application/repository.secureMondrianConnection+xml</span></p></th>
</tr>
</thead>
<tbody>
<tr>
<td><pre class="text"><code>{
    &lt;commonAttributes&gt;,
    &quot;dataSource&quot;:{
        &quot;dataSourceReference&quot;: {
            &quot;uri&quot;:&quot;&lt;dataSourceURI&gt;&quot;
        }
    },
    &quot;schema&quot;: {
        &quot;schemaReference&quot;: {
            &quot;uri&quot;: &quot;&lt;schemaFileResourceURI&gt;&quot;
        }
    },
    &quot;accessGrantSchemas&quot;: [
        {
            &quot;accessGrantSchemaReference&quot;: {
                &quot;uri&quot;: &quot;&lt;accessGrantSchemaFileResourceURI&gt;&quot;
            }
        },
        ...
    ]
}</code></pre></td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">secureMondrianConnection</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    {commonAttributes}</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">dataSourceReference</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">uri</span>&gt;{dataSourceURI}&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">dataSourceReference</span>&gt;</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">schemaReference</span>&gt;</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">uri</span>&gt;{schemaFileResourceURI}&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">schemaReference</span>&gt;</span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">accessGrantSchemas</span>&gt;</span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">accessGrantSchemaReference</span>&gt;</span>
<span id="cb2-11"><a href="#cb2-11" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">uri</span>&gt;{accessGrantSchemaFileResourceURI}&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb2-12"><a href="#cb2-12" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">accessGrantSchemaReference</span>&gt;</span>
<span id="cb2-13"><a href="#cb2-13" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">accessGrantSchemas</span>&gt;</span>
<span id="cb2-14"><a href="#cb2-14" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">secureMondrianConnection</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

## OLAP Unit

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p><span>application/repository.olapUnit+json</span></p></th>
<th><p><span>application/repository.olapUnit+xml</span></p></th>
</tr>
</thead>
<tbody>
<tr>
<td><pre class="text"><code>{
    &lt;commonAttributes&gt;,
    &quot;mdxQuery&quot;:&quot;&lt;mdxQuery&gt;&quot;,
    &quot;olapConnection&quot;: {
        &quot;olapConnectionReference&quot;: {
            &quot;uri&quot;: &quot;&lt;olapConnectionReferenceURI&gt;&quot;
        }
    }
}</code></pre></td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">olapUnit</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    {commonAttributes}</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">mdxQuery</span>&gt;{mdxQuery}&lt;/<span class="kw">mdxQuery</span>&gt;  </span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">olapConnectionReference</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">uri</span>&gt;{olapConnectionReferenceURI}&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">olapConnectionReference</span>&gt; </span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">olapUnit</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

## Mondrian XML/A Definition

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p><span>application/repository.mondrianXmlaDefinition+json</span></p></th>
<th><p><span>application/repository.mondrianXmlaDefinition+xml</span></p></th>
</tr>
</thead>
<tbody>
<tr>
<td><pre class="text"><code>{
    &lt;commonAttributes&gt;,
    &quot;catalog&quot;:&quot;&lt;catalog&gt;&quot;,
    &quot;mondrianConnection&quot;: {
        &quot;mondrianConnectionReference&quot;: {
            &quot;uri&quot;: &quot;&lt;mondrianConnectionResourceURI&gt;&quot;
        }
    }
}</code></pre></td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">mondrianXmlaDefinition</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    {commonAttributes}</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">catalog</span>&gt;{catalog}&lt;/<span class="kw">catalog</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">mondrianConnectionReference</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">uri</span>&gt;{mondrianConnectionResourceURI}&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">mondrianConnectionReference</span>&gt;</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">mondrianXmlaDefinition</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

## Other Types

The following types are defined in commercial editions of the server and appear in the repository. However, they are meant only to describe the corresponding resources as read-only objects in the repository. The REST API does not support services for clients to create or modify these types.

The types in the following table contain only the common attributes described in Common Attributes.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>Type String</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><span>application/repository.dashboard+json</span><br />
<span>application/repository.dashboard+xml</span></p></td>
<td><p>The dashboard resource descriptors are deprecated and subject to change.</p></td>
</tr>
<tr>
<td><p><span>application/repository.adhocDataView+json</span><br />
<span>application/repository.adhocDataView+xml</span></p></td>
<td><p>The Ad Hoc view type is not fully defined yet and subject to change. Ad Hoc views may be referenced as data sources in other repository types, in which case they are called <span>advDataSource</span>.</p></td>
</tr>
</tbody>
</table>
