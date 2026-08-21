---
title: V2 Resource Descriptor Types
description: The following sections show the name and attributes of each descriptor for repositry resources used by the v2/resources service.
---

# 1.0.1 V2 Resource Descriptor Types

The following sections show the name and attributes of each descriptor for repositry resources used by the v2/resources service.

## 1.0.1.1 Common Attributes

All resource types contain the following attributes. Of these common attributes, only the label and description fields are writable.

In general, writable fields are ones that can be set by the client when sending a descriptor for a write or update operation (PUT or POST). The other fields are read-only fields that the server sets automatically.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>application/repository.{resourceType}+json</p></th>
<th><p>application/repository.{resourceType}+xml</p></th>
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

Throughout the rest of the resource type sections, the common attributes are included in every descriptor as `{commonAttributes}`.

## 1.0.1.2 Folder

Folder types do not contain any additional fields beyond the common attributes shown above.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>application/repository.folder+json</p></th>
<th><p>application/repository.folder+xml</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;uri&quot;</span> <span class="fu">:</span><span class="st">&quot;{resourceUri}&quot;</span><span class="fu">,</span> </span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;label&quot;</span><span class="fu">:</span><span class="st">&quot;Sample Label&quot;</span><span class="fu">,</span> </span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;description&quot;</span><span class="fu">:</span><span class="st">&quot;Sample Description&quot;</span><span class="fu">,</span> </span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;permissionMask&quot;</span><span class="fu">:</span><span class="st">&quot;0&quot;</span><span class="fu">,</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;creationDate&quot;</span><span class="fu">:</span> <span class="st">&quot;2013-07-04T12:18:47&quot;</span><span class="fu">,</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;updateDate&quot;</span><span class="fu">:</span> <span class="st">&quot;2013-07-04T12:18:47&quot;</span><span class="fu">,</span> </span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;version&quot;</span><span class="fu">:</span><span class="st">&quot;0&quot;</span> </span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">folder</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">uri</span>&gt;/sample/resource/uri&lt;/<span class="kw">uri</span>&gt;</span>
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

## 1.0.1.3 JNDI Data Source

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>application/repository.jndiJdbcDataSource+json</p></th>
<th><p>application/repository.jndiJdbcDataSource+xml</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="er">{commonAttributes</span><span class="fu">}</span><span class="er">,</span> </span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;jndiName&quot;</span><span class="er">:</span><span class="st">&quot;{jndiName}&quot;</span><span class="er">,</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;timezone&quot;</span><span class="er">:</span><span class="st">&quot;{timezone}&quot;</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a><span class="er">}</span></span></code></pre></div></td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">jndiDataSource</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    {commonAttributes}</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">jndiName</span>&gt;{jndiName}&lt;/<span class="kw">jndiName</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">timezone</span>&gt;{timezone}&lt;/<span class="kw">timezone</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">jndiDataSource</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

## 1.0.1.4 JDBC Data Source

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>application/repository.jdbcDataSource+json</p></th>
<th><p>application/repository.jdbcDataSource+xml</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="er">{commonAttributes</span><span class="fu">}</span><span class="er">,</span> </span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;driverClass&quot;</span><span class="er">:</span><span class="st">&quot;{driverClass}&quot;</span><span class="er">,</span> </span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;password&quot;</span><span class="er">:</span><span class="st">&quot;{password}&quot;</span><span class="er">,</span> </span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;username&quot;</span><span class="er">:</span><span class="st">&quot;{username}&quot;</span><span class="er">,</span> </span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;connectionUrl&quot;</span><span class="er">:</span><span class="st">&quot;{connectionUrl}&quot;</span><span class="er">,</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;timezone&quot;</span><span class="er">:</span><span class="st">&quot;{timezone}&quot;</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a><span class="er">}</span></span></code></pre></div></td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">jdbcDataSource</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    {commonAttributes}</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">driverClass</span>&gt;{driverClass}&lt;/<span class="kw">driverClass</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">password</span>&gt;{password}&lt;/<span class="kw">password</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">username</span>&gt;{username}&lt;/<span class="kw">username</span>&gt;</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">connectionUrl</span>&gt;</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>         {connectionUrl}</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">connectionUrl</span>&gt;</span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">timezone</span>&gt;{timezone}&lt;/<span class="kw">timezone</span>&gt;</span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">jdbcDataSource</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

## 1.0.1.5 AWS Data Source

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>application/repository.awsDataSource+json</p></th>
<th><p>application/repository.awsDataSource+xml</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="er">{commonAttributes</span><span class="fu">}</span><span class="er">,</span> </span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;driverClass&quot;</span><span class="er">:</span><span class="st">&quot;{driverClass}&quot;</span><span class="er">,</span> </span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;password&quot;</span><span class="er">:</span><span class="st">&quot;{password}&quot;</span><span class="er">,</span> </span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;username&quot;</span><span class="er">:</span><span class="st">&quot;{username}&quot;</span><span class="er">,</span> </span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;connectionUrl&quot;</span><span class="er">:</span><span class="st">&quot;{connectionUrl}&quot;</span><span class="er">,</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;timezone&quot;</span><span class="er">:</span><span class="st">&quot;{timezone}&quot;</span><span class="er">,</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;accessKey&quot;</span><span class="er">:</span><span class="st">&quot;{accessKey}&quot;</span><span class="er">,</span> </span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;secretKey&quot;</span><span class="er">:</span><span class="st">&quot;{secretKey}&quot;</span><span class="er">,</span> </span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;roleArn&quot;</span><span class="er">:</span><span class="st">&quot;{roleArn}&quot;</span><span class="er">,</span> </span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;region&quot;</span><span class="er">:</span><span class="st">&quot;{region}&quot;</span><span class="er">,</span> </span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;dbName&quot;</span><span class="er">:</span><span class="st">&quot;{dbName}&quot;</span><span class="er">,</span> </span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;dbInstanceIdentifier&quot;</span><span class="er">:</span><span class="st">&quot;{dbInstanceIdentifier}&quot;</span><span class="er">,</span> </span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;dbService&quot;</span><span class="er">:</span><span class="st">&quot;{dbService}&quot;</span></span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a><span class="er">}</span></span></code></pre></div></td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">awsDataSource</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    {commonAttributes}</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">driverClass</span>&gt;{driverClass}&lt;/<span class="kw">driverClass</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">password</span>&gt;{password}&lt;/<span class="kw">password</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">username</span>&gt;{username}&lt;/<span class="kw">username</span>&gt;</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">connectionUrl</span>&gt;</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>         {connectionUrl}</span>
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
<th>Values of AWS {region} in<br />
.../WEB-INF/application-context.xml</th>
<th>Labels for AWS regions in<br />
.../WEB-INF/bundles/jasperserver_messages.properties<br />
</th>
</tr>
</thead>
<tbody>
<tr>
<td><pre class="text"><code>us-east-1.amazonaws.com
us-west-2.amazonaws.com
us-west-1.amazonaws.com
eu-west-1.amazonaws.com
eu-central-1.amazonaws.com
ap-southeast-1.amazonaws.com
ap-southeast-2.amazonaws.com
ap-northeast-1.amazonaws.com
sa-east-1.amazonaws.com</code></pre></td>
<td><pre class="text"><code>US East (Northern Virginia) Region
US West (Oregon) Region
US West (Northern California) Region
EU (Ireland) Region
EU (Frankfurt) Region
Asia Pacific (Singapore) Region
Asia Pacific (Sydney) Region
Asia Pacific (Tokyo) Region
South America (São Paulo) Region</code></pre></td>
</tr>
</tbody>
</table>

## 1.0.1.6 Virtual Data Source

The `id` of each `subDataSource` must be unique. The server does not prevent duplicates, and the last one to be defined silently overwrites the previous definition.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>application/repository.virtualDataSource+json</p></th>
<th><p>application/repository.virtualDataSource+xml</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="er">{commonAttributes</span><span class="fu">}</span><span class="er">,</span> </span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;subDataSources&quot;</span><span class="er">:</span><span class="ot">[</span> </span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>        <span class="fu">{</span> </span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;id&quot;</span><span class="fu">:</span><span class="st">&quot;{subDataSourceId}&quot;</span><span class="fu">,</span> </span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;uri&quot;</span><span class="fu">:</span><span class="st">&quot;{subDataSourceUri}&quot;</span> </span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>        <span class="fu">}</span><span class="ot">,</span> </span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>        <span class="er">...</span></span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>    <span class="ot">]</span> </span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a><span class="er">}</span></span></code></pre></div></td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">virtualDataSource</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    {commonAttributes}</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">subDataSources</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">subDataSource</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">id</span>&gt;{subDataSourceId}&lt;/<span class="kw">id</span>&gt;</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">uri</span>&gt;{subDataSourceUri}&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">subDataSource</span>&gt;</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>        ...</span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">subDataSources</span>&gt;</span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">virtualDataSource</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

## 1.0.1.7 Custom Data Source

The value of the `serviceClass` attribute is read-only and depends on the specific type of the custom data source, as defined in the server's applicationContext configuration files.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>application/repository.customDataSource+json</p></th>
<th><p>application/repository.customDataSource+xml</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="er">{commonAttributes</span><span class="fu">}</span><span class="er">,</span> </span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;serviceClass&quot;</span><span class="er">:</span><span class="st">&quot;{serviceClass}&quot;</span><span class="er">,</span>   </span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;dataSourceName&quot;</span><span class="er">:</span><span class="st">&quot;{dataSourceName}&quot;</span><span class="er">,</span> </span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;properties&quot;</span><span class="er">:</span><span class="ot">[</span> </span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>        <span class="fu">{</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;key&quot;</span><span class="fu">:</span><span class="st">&quot;{key}&quot;</span><span class="fu">,</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;value&quot;</span><span class="fu">:</span><span class="st">&quot;{value}&quot;</span></span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>        <span class="fu">}</span><span class="ot">,</span> </span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>        <span class="er">...</span></span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>    <span class="ot">]</span> </span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a><span class="er">}</span></span></code></pre></div></td>
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

## 1.0.1.8 Bean Data Source

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>application/repository.beanDataSource+json</p></th>
<th><p>application/repository.beanDataSource+xml</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="er">{commonAttributes</span><span class="fu">}</span><span class="er">,</span> </span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;beanName&quot;</span><span class="er">:</span><span class="st">&quot;{beanName}&quot;</span><span class="er">,</span> </span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;beanMethod&quot;</span><span class="er">:</span><span class="st">&quot;{beanMethod}&quot;</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a><span class="er">}</span></span></code></pre></div></td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">beanDataSource</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    {commonAttributes}</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">beanName</span>&gt;{beanName}&lt;<span class="kw">beanName</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">beanMethod</span>&gt;{beanMethod}&lt;/<span class="kw">beanMethod</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">beanDataSource</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

## 1.0.1.9 XML/A Connection

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>application/repository.xmlaConnection+json</p></th>
<th><p>application/repository.xmlaConnection+xml</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="er">{commonAttributes</span><span class="fu">}</span><span class="er">,</span> </span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;url&quot;</span><span class="er">:</span><span class="st">&quot;{xmlaServiceUrl}&quot;</span><span class="er">,</span> </span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;xmlaDataSource&quot;</span><span class="er">:</span><span class="st">&quot;{xmlaDataSource}&quot;</span><span class="er">,</span> </span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;catalog&quot;</span><span class="er">:</span><span class="st">&quot;{catalog}&quot;</span><span class="er">,</span> </span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;username&quot;</span><span class="er">:</span><span class="st">&quot;{username}&quot;</span><span class="er">,</span> </span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;password&quot;</span><span class="er">:</span><span class="st">&quot;{password}&quot;</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a><span class="er">}</span></span></code></pre></div></td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">xmlaConnection</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    {commonAttributes}</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">url</span>&gt;{xmlaServiceUrl}&lt;/<span class="kw">url</span>&gt;</span>
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

## 1.0.1.10 Datatypes

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>application/repository.dataType+json</p></th>
<th><p>application/repository.dataType+xml</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="er">{commonAttributes</span><span class="fu">}</span><span class="er">,</span> </span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;type&quot;</span><span class="er">:</span><span class="st">&quot;text|number|date|dateTime|time&quot;</span><span class="er">,</span> </span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;pattern&quot;</span><span class="er">:</span><span class="st">&quot;{pattern}&quot;</span><span class="er">,</span> </span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;maxValue&quot;</span><span class="er">:</span><span class="st">&quot;{maxValue}&quot;</span><span class="er">,</span> </span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;strictMax&quot;</span><span class="er">:</span><span class="st">&quot;true|false&quot;</span><span class="er">,</span> </span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;minValue&quot;</span><span class="er">:</span><span class="st">&quot;{minValue}&quot;</span><span class="er">,</span> </span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;strictMin&quot;</span><span class="er">:</span><span class="st">&quot;true|false&quot;</span>   </span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;maxLength&quot;</span><span class="er">:</span><span class="st">&quot;{maxLengthInteger}&quot;</span></span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a><span class="er">}</span></span></code></pre></div></td>
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

## 1.0.1.11 List of Values

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>application/repository.listOfValues+json</p></th>
<th><p>application/repository.listOfValues+xml</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="er">{commonAttributes</span><span class="fu">}</span><span class="er">,</span> </span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;items&quot;</span><span class="er">:</span><span class="ot">[</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>        <span class="fu">{</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;label&quot;</span><span class="fu">:</span><span class="st">&quot;{label}&quot;</span><span class="fu">,</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;value&quot;</span><span class="fu">:</span><span class="st">&quot;{value}&quot;</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>        <span class="fu">}</span><span class="ot">,</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>        <span class="er">...</span></span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>    <span class="ot">]</span></span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a><span class="er">}</span></span></code></pre></div></td>
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

## 1.0.1.12 Query

The dataSource field of the query is nullable. Set an empty dataSource field when you want to remove a local datasource, either a reference or a local definition. When the data source of a query is not defined, the query uses the data source of its parent, for example its JRXML report (reportUnit).

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>application/repository.query+json</p></th>
<th><p>application/repository.query+xml</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="er">{commonAttributes</span><span class="fu">}</span><span class="er">,</span> </span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;value&quot;</span><span class="er">:</span><span class="st">&quot;{query}&quot;</span><span class="er">,</span> </span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;language&quot;</span><span class="er">:</span><span class="st">&quot;{language}&quot;</span><span class="er">,</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;dataSource&quot;</span><span class="er">:</span><span class="fu">{</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;dataSourceReference&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;uri&quot;</span><span class="fu">:</span><span class="st">&quot;{dataSourceUri}&quot;</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>        <span class="fu">}</span></span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span> </span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a><span class="er">}</span></span></code></pre></div></td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">query</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    {commonAttributes}</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;{query}&lt;/<span class="kw">value</span>&gt; </span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">language</span>&gt;{language}&lt;/<span class="kw">language</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">dataSourceReference</span>&gt;</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">uri</span>&gt;{dataSourceUri}&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">dataSourceReference</span>&gt;</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">query</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

## 1.0.1.13 Input Control

Input controls come in several types that require different fields. The following table shows all possible fields, not all of which are mutually compatible.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>application/repository.inputControl+json</p></th>
<th><p>application/repository.inputControl+xml</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="er">{commonAttributes</span><span class="fu">}</span><span class="er">,</span> </span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;mandatory&quot;</span><span class="er">:</span><span class="st">&quot;{true|false}&quot;</span><span class="er">,</span>  </span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;readOnly&quot;</span><span class="er">:</span><span class="st">&quot;{true|false}&quot;</span><span class="er">,</span>  </span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;visible&quot;</span><span class="er">:</span><span class="st">&quot;{true|false}&quot;</span><span class="er">,</span>  </span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;type&quot;</span><span class="er">:</span><span class="st">&quot;{inputControlTypeByteValue}&quot;</span><span class="er">,</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;usedFields&quot;</span><span class="er">:</span><span class="st">&quot;{field1;field2;...}&quot;</span><span class="er">,</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;dataType&quot;</span><span class="er">:</span> <span class="fu">{</span></span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;dataTypeReference&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;uri&quot;</span><span class="fu">:</span> <span class="st">&quot;{dataTypeResourceUri}&quot;</span></span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>        <span class="fu">}</span></span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span><span class="er">,</span>  </span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;listOfValues&quot;</span><span class="er">:</span> <span class="fu">{</span></span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;listOfValuesReference&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;uri&quot;</span><span class="fu">:</span> <span class="st">&quot;listOfValuesResourceUri&quot;</span></span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a>        <span class="fu">}</span></span>
<span id="cb1-17"><a href="#cb1-17" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span>  </span>
<span id="cb1-18"><a href="#cb1-18" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;visibleColumns&quot;</span><span class="er">:</span><span class="ot">[</span><span class="st">&quot;column1&quot;</span><span class="ot">,</span> <span class="st">&quot;colum2&quot;</span><span class="ot">,</span> <span class="er">...</span><span class="ot">]</span><span class="er">,</span>  </span>
<span id="cb1-19"><a href="#cb1-19" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;valueColumn&quot;</span><span class="er">:</span><span class="st">&quot;{valueColumn}&quot;</span><span class="er">,</span>  </span>
<span id="cb1-20"><a href="#cb1-20" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;query&quot;</span><span class="er">:</span> <span class="fu">{</span></span>
<span id="cb1-21"><a href="#cb1-21" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;queryReference&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb1-22"><a href="#cb1-22" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;uri&quot;</span><span class="fu">:</span> <span class="st">&quot;{queryResourceUri}&quot;</span></span>
<span id="cb1-23"><a href="#cb1-23" aria-hidden="true" tabindex="-1"></a>        <span class="fu">}</span></span>
<span id="cb1-24"><a href="#cb1-24" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span></span>
<span id="cb1-25"><a href="#cb1-25" aria-hidden="true" tabindex="-1"></a><span class="er">}</span></span></code></pre></div></td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">inputControl</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    {commonAttributes}</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">mandatory</span>&gt;true|false&lt;/<span class="kw">mandatory</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">readOnly</span>&gt;true|false&lt;/<span class="kw">readOnly</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">visible</span>&gt;true|false&lt;/<span class="kw">visible</span>&gt;</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">type</span>&gt;{inputControlTypeByteValue}&lt;/<span class="kw">type</span>&gt;</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">usedFields</span>&gt;{field1;field2;...}&lt;/<span class="kw">usedFields</span>&gt;</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">dataTypeReference</span>&gt;</span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">uri</span>&gt;{dataTypeResourceUri}&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">dataTypeReference</span>&gt;</span>
<span id="cb2-11"><a href="#cb2-11" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">listOfValuesReference</span>&gt;</span>
<span id="cb2-12"><a href="#cb2-12" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">uri</span>&gt;{listOfValuesResourceUri}&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb2-13"><a href="#cb2-13" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">listOfValuesReference</span>&gt;</span>
<span id="cb2-14"><a href="#cb2-14" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">queryReference</span>&gt;</span>
<span id="cb2-15"><a href="#cb2-15" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">uri</span>&gt;{queryResourceUri}&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb2-16"><a href="#cb2-16" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">queryReference</span>&gt;</span>
<span id="cb2-17"><a href="#cb2-17" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">visibleColumns</span>&gt;</span>
<span id="cb2-18"><a href="#cb2-18" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">column</span>&gt;{column1}&lt;/<span class="kw">column</span>&gt;</span>
<span id="cb2-19"><a href="#cb2-19" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">column</span>&gt;{column2}&lt;/<span class="kw">column</span>&gt;</span>
<span id="cb2-20"><a href="#cb2-20" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">column</span>&gt;...&lt;/<span class="kw">column</span>&gt;</span>
<span id="cb2-21"><a href="#cb2-21" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">visibleColumns</span>&gt;</span>
<span id="cb2-22"><a href="#cb2-22" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">valueColumn</span>&gt;{valueColumn}&lt;/<span class="kw">valueColumn</span>&gt;</span>
<span id="cb2-23"><a href="#cb2-23" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">inputControl</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

The following list shows the numerical code and meaning for the {inputControlTypeByteValue}. The input control type determines the other fields that are required. The list of required fields may appear in a field named usedFields, separated by semi-colons (`;`).

| "type" | Type of Input Control | Other Fields Required (usedFields) |
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

## 1.0.1.14 File

The repository.file+\<format\> descriptor is used to identify the file type. The content field is used only when uploading a file resource as base-64 encoded content. For other ways to upload file contents, see [Uploading File Resources](uploading_file_resources.md). The content field is absent when requesting a file resource descriptor. For more information, see [Downloading File Resources](downloading_file_resources.md).

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>application/repository.file+json</p></th>
<th><p>application/repository.file+xml</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="er">{commonAttributes</span><span class="fu">}</span><span class="er">,</span> </span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;type&quot;</span><span class="er">:</span><span class="st">&quot;pdf|html|xls|rtf|csv|odt|txt</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="st">            |docx|ods|xlsx|img|font|jrxml</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a><span class="st">            |jar|prop|jrtx|xml|css</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a><span class="st">            |olapMondrianSchema</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a><span class="st">            |accessGrantSchema</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a><span class="st">            |unspecified}&quot;</span><span class="er">,</span></span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>    <span class="er">//</span> <span class="er">content</span> <span class="er">is</span> <span class="er">write-only;</span></span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>    <span class="er">//</span> <span class="er">it</span> <span class="er">is</span> <span class="er">not</span> <span class="er">included</span> <span class="er">in</span> <span class="er">a</span> <span class="er">response</span></span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;content&quot;</span><span class="er">:</span><span class="st">&quot;{base64EncodedContent}&quot;</span></span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a><span class="er">}</span></span></code></pre></div></td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">file</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    {commonAttributes}</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">type</span>&gt;pdf|html|xls|rtf|csv|odt|txt</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>        |docx|ods|xlsx|img|font|jrxml</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>        |jar|prop|jrtx|xml|css</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>        |olapMondrianSchema</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>        |accessGrantSchema|unspecified}</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">type</span>&gt;</span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">content</span>&gt;{base64EncodedContent}&lt;/<span class="kw">content</span>&gt;</span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">file</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

## 1.0.1.15 Report Unit (JRXML Report)

A report unit contains mostly references to the files that make up a report within the server. A report unit is a composite resource that may contain other local resources. In this case, the URIs that it references include a URI in the following format:

\<reportUnitURI\>\_files/\<localResourceID\>

For example, the main JRXML of a sample report is referenced as follows:

/reports/samples/Cascading_multi_select_report_files/Cascading_multi_select_report

For more information, see V2 Resource Descriptors.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>application/repository.reportUnit+json</p></th>
<th><p>application/repository.reportUnit+xml</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="er">{commonAttributes</span><span class="fu">}</span><span class="er">,</span> </span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;alwaysPromptControls&quot;</span><span class="er">:</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>        <span class="st">&quot;{true|false}&quot;</span><span class="er">,</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    <span class="er">//</span> <span class="er">default</span> <span class="er">is</span> <span class="st">&quot;popupScreen&quot;</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;controlsLayout&quot;</span><span class="er">:</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>        <span class="st">&quot;{popupScreen|separatePage</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a><span class="st">          |topOfPage|inPage}&quot;</span><span class="er">,</span></span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;inputControlRenderingView&quot;</span><span class="er">:</span></span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>        <span class="st">&quot;{inputControlRenderingView}&quot;</span><span class="er">,</span>    </span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;reportRenderingView&quot;</span><span class="er">:</span></span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>        <span class="st">&quot;{reportRenderingView}&quot;</span><span class="er">,</span></span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;dataSource&quot;</span><span class="er">:</span><span class="fu">{</span></span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;dataSourceReference&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;uri&quot;</span><span class="fu">:</span><span class="st">&quot;{dataSourceUri}&quot;</span></span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a>        <span class="fu">}</span></span>
<span id="cb1-17"><a href="#cb1-17" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span><span class="er">,</span></span>
<span id="cb1-18"><a href="#cb1-18" aria-hidden="true" tabindex="-1"></a>    <span class="er">//</span> <span class="st">&quot;query&quot;</span> <span class="er">is</span> <span class="er">nullable</span></span>
<span id="cb1-19"><a href="#cb1-19" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;query:&quot;</span> <span class="fu">{</span></span>
<span id="cb1-20"><a href="#cb1-20" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;queryReference&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb1-21"><a href="#cb1-21" aria-hidden="true" tabindex="-1"></a>            <span class="er">uri</span><span class="fu">:</span> <span class="st">&quot;{queryResourceUri}&quot;</span></span>
<span id="cb1-22"><a href="#cb1-22" aria-hidden="true" tabindex="-1"></a>        <span class="fu">}</span></span>
<span id="cb1-23"><a href="#cb1-23" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span><span class="er">,</span>  </span>
<span id="cb1-24"><a href="#cb1-24" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;jrxml&quot;</span><span class="er">:</span> <span class="fu">{</span></span>
<span id="cb1-25"><a href="#cb1-25" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;jrxmlFileReference&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb1-26"><a href="#cb1-26" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;uri&quot;</span><span class="fu">:</span> <span class="st">&quot;{jrxmlFileResourceUri}&quot;</span></span>
<span id="cb1-27"><a href="#cb1-27" aria-hidden="true" tabindex="-1"></a>        <span class="fu">}</span> <span class="er">or</span></span>
<span id="cb1-28"><a href="#cb1-28" aria-hidden="true" tabindex="-1"></a>        <span class="st">&quot;jrxmlFile&quot;</span><span class="er">:</span> <span class="fu">{</span></span>
<span id="cb1-29"><a href="#cb1-29" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;label&quot;</span><span class="fu">:</span> <span class="st">&quot;Main jrxml&quot;</span><span class="fu">,</span></span>
<span id="cb1-30"><a href="#cb1-30" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;type&quot;</span><span class="fu">:</span> <span class="st">&quot;jrxml&quot;</span></span>
<span id="cb1-31"><a href="#cb1-31" aria-hidden="true" tabindex="-1"></a>        <span class="fu">}</span></span>
<span id="cb1-32"><a href="#cb1-32" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span></span>
<span id="cb1-33"><a href="#cb1-33" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;inputControls&quot;</span><span class="er">:</span> <span class="ot">[</span></span>
<span id="cb1-34"><a href="#cb1-34" aria-hidden="true" tabindex="-1"></a>        <span class="fu">{</span></span>
<span id="cb1-35"><a href="#cb1-35" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;inputControlReference&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb1-36"><a href="#cb1-36" aria-hidden="true" tabindex="-1"></a>                <span class="dt">&quot;uri&quot;</span><span class="fu">:</span> <span class="st">&quot;{inputControlUri}&quot;</span></span>
<span id="cb1-37"><a href="#cb1-37" aria-hidden="true" tabindex="-1"></a>            <span class="fu">}</span></span>
<span id="cb1-38"><a href="#cb1-38" aria-hidden="true" tabindex="-1"></a>        <span class="fu">}</span><span class="ot">,</span></span>
<span id="cb1-39"><a href="#cb1-39" aria-hidden="true" tabindex="-1"></a>        <span class="er">...</span></span>
<span id="cb1-40"><a href="#cb1-40" aria-hidden="true" tabindex="-1"></a>    <span class="ot">]</span><span class="er">,</span></span>
<span id="cb1-41"><a href="#cb1-41" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;resources&quot;</span><span class="er">:</span> <span class="ot">[</span></span>
<span id="cb1-42"><a href="#cb1-42" aria-hidden="true" tabindex="-1"></a>        <span class="st">&quot;resource&quot;</span><span class="er">:</span> <span class="fu">{</span></span>
<span id="cb1-43"><a href="#cb1-43" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;name&quot;</span><span class="fu">:</span> <span class="st">&quot;{resourceName}&quot;</span><span class="fu">,</span></span>
<span id="cb1-44"><a href="#cb1-44" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;file&quot;</span><span class="fu">:</span> <span class="fu">{</span><span class="er">contents</span><span class="fu">}</span> <span class="er">&lt;*&gt;</span></span>
<span id="cb1-45"><a href="#cb1-45" aria-hidden="true" tabindex="-1"></a>            <span class="fu">}</span></span>
<span id="cb1-46"><a href="#cb1-46" aria-hidden="true" tabindex="-1"></a>        <span class="er">}</span><span class="ot">,</span></span>
<span id="cb1-47"><a href="#cb1-47" aria-hidden="true" tabindex="-1"></a>        <span class="er">...</span></span>
<span id="cb1-48"><a href="#cb1-48" aria-hidden="true" tabindex="-1"></a>    <span class="ot">]</span></span>
<span id="cb1-49"><a href="#cb1-49" aria-hidden="true" tabindex="-1"></a><span class="er">}</span></span>
<span id="cb1-50"><a href="#cb1-50" aria-hidden="true" tabindex="-1"></a><span class="er">&lt;*&gt;</span> <span class="er">or</span> <span class="st">&quot;fileReference&quot;</span><span class="er">:</span> <span class="fu">{</span></span>
<span id="cb1-51"><a href="#cb1-51" aria-hidden="true" tabindex="-1"></a>          <span class="dt">&quot;uri&quot;</span><span class="fu">:</span> <span class="st">&quot;{fileResourceUri}&quot;</span></span>
<span id="cb1-52"><a href="#cb1-52" aria-hidden="true" tabindex="-1"></a>       <span class="fu">}</span></span></code></pre></div></td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">reportUnit</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    {commonAttributes}</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">alwaysPromptControls</span>&gt;true|false</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">alwaysPromptControls</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>    <span class="co">&lt;!-- default is &quot;popupScreen&quot; --&gt;</span></span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">controlsLayout</span>&gt;</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>        popupScreen|separatePage</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>        |topOfPage|inPage</span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">controlsLayout</span>&gt;</span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">inputControlRenderingView</span>&gt;</span>
<span id="cb2-11"><a href="#cb2-11" aria-hidden="true" tabindex="-1"></a>        {inputControlRenderingView}</span>
<span id="cb2-12"><a href="#cb2-12" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">inputControlRenderingView</span>&gt;</span>
<span id="cb2-13"><a href="#cb2-13" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">reportRenderingView</span>&gt;</span>
<span id="cb2-14"><a href="#cb2-14" aria-hidden="true" tabindex="-1"></a>        {reportRenderingView}</span>
<span id="cb2-15"><a href="#cb2-15" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">reportRenderingView</span>&gt;</span>
<span id="cb2-16"><a href="#cb2-16" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">dataSource</span>&gt;</span>
<span id="cb2-17"><a href="#cb2-17" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">dataSourceReference</span>&gt;</span>
<span id="cb2-18"><a href="#cb2-18" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">uri</span>&gt;{dataSourceUri}&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb2-19"><a href="#cb2-19" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">dataSourceReference</span>&gt;</span>
<span id="cb2-20"><a href="#cb2-20" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">dataSource</span>&gt;</span>
<span id="cb2-21"><a href="#cb2-21" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">query</span>&gt;</span>
<span id="cb2-22"><a href="#cb2-22" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">queryReference</span>&gt;</span>
<span id="cb2-23"><a href="#cb2-23" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">uri</span>&gt;{queryResourceUri}&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb2-24"><a href="#cb2-24" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">queryReference</span>&gt;</span>
<span id="cb2-25"><a href="#cb2-25" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">query</span>&gt;</span>
<span id="cb2-26"><a href="#cb2-26" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">jrxml</span>&gt;  </span>
<span id="cb2-27"><a href="#cb2-27" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">jrxmlFileReference</span>&gt;</span>
<span id="cb2-28"><a href="#cb2-28" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">uri</span>&gt;{jrxmlFileResourceUri}&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb2-29"><a href="#cb2-29" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">jrxmlFileReference</span>&gt;</span>
<span id="cb2-30"><a href="#cb2-30" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">jrxml</span>&gt;</span>
<span id="cb2-31"><a href="#cb2-31" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">inputControls</span>&gt;</span>
<span id="cb2-32"><a href="#cb2-32" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">inputControlReference</span>&gt;</span>
<span id="cb2-33"><a href="#cb2-33" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">uri</span>&gt;{inputControlUri}&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb2-34"><a href="#cb2-34" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">inputControlReference</span>&gt;</span>
<span id="cb2-35"><a href="#cb2-35" aria-hidden="true" tabindex="-1"></a>        ...</span>
<span id="cb2-36"><a href="#cb2-36" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">inputControls</span>&gt;</span>
<span id="cb2-37"><a href="#cb2-37" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resources</span>&gt;</span>
<span id="cb2-38"><a href="#cb2-38" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">resource</span>&gt;</span>
<span id="cb2-39"><a href="#cb2-39" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">name</span>&gt;{resourceName}&lt;/<span class="kw">name</span>&gt;</span>
<span id="cb2-40"><a href="#cb2-40" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">file</span>&gt;contents&lt;/<span class="kw">file</span>&gt; {*}</span>
<span id="cb2-41"><a href="#cb2-41" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">resource</span>&gt;</span>
<span id="cb2-42"><a href="#cb2-42" aria-hidden="true" tabindex="-1"></a>        ...</span>
<span id="cb2-43"><a href="#cb2-43" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resources</span>&gt;    </span>
<span id="cb2-44"><a href="#cb2-44" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">reportUnit</span>&gt;</span>
<span id="cb2-45"><a href="#cb2-45" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb2-46"><a href="#cb2-46" aria-hidden="true" tabindex="-1"></a>{*} or &lt;<span class="kw">fileReference</span>&gt;</span>
<span id="cb2-47"><a href="#cb2-47" aria-hidden="true" tabindex="-1"></a>          &lt;<span class="kw">uri</span>&gt;{fileResourceUri}&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb2-48"><a href="#cb2-48" aria-hidden="true" tabindex="-1"></a>       &lt;/<span class="kw">fileReference</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

## 1.0.1.16 Report Options

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>application/repository.reportOptions+json</p></th>
<th><p>application/repository.reportOptions+xml</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="er">{commonAttributes</span><span class="fu">}</span><span class="er">,</span> </span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;reportUri&quot;</span><span class="er">:</span><span class="st">&quot;{reportUri}&quot;</span><span class="er">,</span>   </span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;reportParameters&quot;</span><span class="er">:</span><span class="ot">[</span>  </span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>        <span class="fu">{</span> </span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;name&quot;</span><span class="fu">:</span><span class="st">&quot;{parameterName}&quot;</span><span class="fu">,</span> </span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;value&quot;</span><span class="fu">:</span><span class="ot">[</span> </span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>                <span class="st">&quot;value_1&quot;</span><span class="ot">,</span> </span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>                <span class="st">&quot;value_2&quot;</span><span class="ot">,</span> </span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>                <span class="er">...</span></span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>            <span class="ot">]</span> </span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>        <span class="fu">}</span><span class="ot">,</span>  </span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>        <span class="er">...</span>    </span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>    <span class="ot">]</span>  </span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a><span class="er">}</span></span></code></pre></div></td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">reportOptions</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    {commonAttributes}</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">reportUri</span>&gt;{reportUri}&lt;/<span class="kw">reportUri</span>&gt;</span>
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

## 1.0.1.17 Domain (semanticLayerDataSource)

For more information about accessing the schema of a Domain, see [The v2/domains/metadata Service](the_v2_domains_metadata_service.md).

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>application/repository.semanticLayerDataSource+json</p></th>
<th><p>application/repository.semanticLayerDataSource+xml</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="er">{commonAttributes</span><span class="fu">}</span><span class="er">,</span> </span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;dataSource&quot;</span><span class="er">:</span><span class="fu">{</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;dataSourceReference&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;uri&quot;</span><span class="fu">:</span><span class="st">&quot;{dataSourceUri}&quot;</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>        <span class="fu">}</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span><span class="er">,</span> </span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;schema&quot;</span><span class="er">:</span> <span class="fu">{</span></span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;schemaFileReference&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;uri&quot;</span><span class="fu">:</span> <span class="st">&quot;{schemaFileResourceUri}&quot;</span></span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>        <span class="fu">}</span></span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span><span class="er">,</span> </span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;bundles&quot;</span><span class="er">:</span> <span class="ot">[</span></span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>        <span class="fu">{</span></span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>            <span class="er">//</span> <span class="er">empty</span> <span class="er">localeString</span> <span class="er">indicates</span> <span class="er">default</span> <span class="er">bundle</span></span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;locale&quot;</span><span class="fu">:</span> <span class="st">&quot;{localeString}&quot;</span><span class="fu">,</span></span>
<span id="cb1-17"><a href="#cb1-17" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;file&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb1-18"><a href="#cb1-18" aria-hidden="true" tabindex="-1"></a>                <span class="dt">&quot;fileReference&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb1-19"><a href="#cb1-19" aria-hidden="true" tabindex="-1"></a>                    <span class="dt">&quot;uri&quot;</span><span class="fu">:</span> <span class="st">&quot;{propertiesFileResourceUri}&quot;</span></span>
<span id="cb1-20"><a href="#cb1-20" aria-hidden="true" tabindex="-1"></a>                <span class="fu">}</span></span>
<span id="cb1-21"><a href="#cb1-21" aria-hidden="true" tabindex="-1"></a>            <span class="fu">}</span></span>
<span id="cb1-22"><a href="#cb1-22" aria-hidden="true" tabindex="-1"></a>        <span class="fu">}</span><span class="ot">,</span> </span>
<span id="cb1-23"><a href="#cb1-23" aria-hidden="true" tabindex="-1"></a>        <span class="er">...</span></span>
<span id="cb1-24"><a href="#cb1-24" aria-hidden="true" tabindex="-1"></a>    <span class="ot">]</span><span class="er">,</span> </span>
<span id="cb1-25"><a href="#cb1-25" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;securityFile&quot;</span><span class="er">:</span> <span class="fu">{</span></span>
<span id="cb1-26"><a href="#cb1-26" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;securityFileReference&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb1-27"><a href="#cb1-27" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;uri&quot;</span><span class="fu">:</span> <span class="st">&quot;{securityFileResourceUri}&quot;</span></span>
<span id="cb1-28"><a href="#cb1-28" aria-hidden="true" tabindex="-1"></a>        <span class="fu">}</span></span>
<span id="cb1-29"><a href="#cb1-29" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span></span>
<span id="cb1-30"><a href="#cb1-30" aria-hidden="true" tabindex="-1"></a><span class="er">}</span></span></code></pre></div></td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">semanticLayerDataSource</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    {commonAttributes}</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">dataSourceReference</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">uri</span>&gt;{dataSourceUri}&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">dataSourceReference</span>&gt;</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">schemaFileReference</span>&gt;</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">uri</span>&gt;{schemaFileResourceUri}&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">schemaFileReference</span>&gt;</span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">bundles</span>&gt;</span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">bundle</span>&gt;</span>
<span id="cb2-11"><a href="#cb2-11" aria-hidden="true" tabindex="-1"></a>            <span class="co">&lt;!-- &lt;locale/&gt; indicates default bundle --&gt;</span></span>
<span id="cb2-12"><a href="#cb2-12" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">locale</span>&gt;{localeString}&lt;/<span class="kw">locale</span>&gt;</span>
<span id="cb2-13"><a href="#cb2-13" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">fileReference</span>&gt;</span>
<span id="cb2-14"><a href="#cb2-14" aria-hidden="true" tabindex="-1"></a>                &lt;<span class="kw">uri</span>&gt;{propertiesFileResourceUri}&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb2-15"><a href="#cb2-15" aria-hidden="true" tabindex="-1"></a>            &lt;/<span class="kw">fileReference</span>&gt;</span>
<span id="cb2-16"><a href="#cb2-16" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">bundle</span>&gt; </span>
<span id="cb2-17"><a href="#cb2-17" aria-hidden="true" tabindex="-1"></a>        ...</span>
<span id="cb2-18"><a href="#cb2-18" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">bundles</span>&gt; </span>
<span id="cb2-19"><a href="#cb2-19" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">securityFileReference</span>&gt;</span>
<span id="cb2-20"><a href="#cb2-20" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">uri</span>&gt;{securityFileResourceUri}&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb2-21"><a href="#cb2-21" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">securityFileReference</span>&gt;</span>
<span id="cb2-22"><a href="#cb2-22" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">semanticLayerDataSource</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

## 1.0.1.18 Domain Topic

A Domain Topic is a Topic created by selecting database fields from a Domain. It is structurally equivalent to a JRXML report, and thus it has the same type attributes (see Report Unit (JRXML Report)). The only difference is that the data source field will reference a Domain (semanticLayerDataSource).

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>application/repository.domainTopic+json</p></th>
<th><p>application/repository.domainTopic+xml</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Same attributes as<br />
application/repository.reportUnit+json</p></td>
<td><p>Same attributes as<br />
application/repository.reportUnit+xml</p></td>
</tr>
</tbody>
</table>

## 1.0.1.19 Mondrian Connection

Mondrian connections without the access grant schemas are used in the communuity edition of JasperReports® Server.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>application/repository.mondrianConnection+json</p></th>
<th><p>application/repository.mondrianConnection+xml</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="er">{commonAttributes</span><span class="fu">}</span><span class="er">,</span> </span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;dataSource&quot;</span><span class="er">:</span><span class="fu">{</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;dataSourceReference&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;uri&quot;</span><span class="fu">:</span><span class="st">&quot;{dataSourceUri}&quot;</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>        <span class="fu">}</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span><span class="er">,</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;schema&quot;</span><span class="er">:</span> <span class="fu">{</span></span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;schemaReference&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;uri&quot;</span><span class="fu">:</span> <span class="st">&quot;{schemaFileResourceUri}&quot;</span></span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>        <span class="fu">}</span></span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span></span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a><span class="er">}</span></span></code></pre></div></td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">mondrianConnection</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    {commonAttributes}</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">dataSourceReference</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">uri</span>&gt;{dataSourceUri}&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">dataSourceReference</span>&gt;</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">schemaReference</span>&gt;</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">uri</span>&gt;{schemaFileResourceUri}&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">schemaReference</span>&gt;</span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">mondrianConnection</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

## 1.0.1.20 Secure Mondrian Connection

Secure Mondrian Connections are available only in commercial releases of JasperReports® Server.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>application/repository.secureMondrianConnection+json</p></th>
<th><p>application/repository.secureMondrianConnection+xml</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="er">{commonAttributes</span><span class="fu">}</span><span class="er">,</span> </span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;dataSource&quot;</span><span class="er">:</span><span class="fu">{</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;dataSourceReference&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;uri&quot;</span><span class="fu">:</span><span class="st">&quot;{dataSourceUri}&quot;</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>        <span class="fu">}</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span><span class="er">,</span> </span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;schema&quot;</span><span class="er">:</span> <span class="fu">{</span></span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;schemaReference&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;uri&quot;</span><span class="fu">:</span> <span class="st">&quot;{schemaFileResourceUri}&quot;</span></span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>        <span class="fu">}</span></span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span><span class="er">,</span> </span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;accessGrantSchemas&quot;</span><span class="er">:</span> <span class="ot">[</span></span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>        <span class="fu">{</span></span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;accessGrantSchemaReference&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a>                <span class="dt">&quot;uri&quot;</span><span class="fu">:</span> <span class="st">&quot;{accessGrantSchemaFileResourceUri}&quot;</span></span>
<span id="cb1-17"><a href="#cb1-17" aria-hidden="true" tabindex="-1"></a>            <span class="fu">}</span></span>
<span id="cb1-18"><a href="#cb1-18" aria-hidden="true" tabindex="-1"></a>        <span class="fu">}</span><span class="ot">,</span></span>
<span id="cb1-19"><a href="#cb1-19" aria-hidden="true" tabindex="-1"></a>        <span class="er">...</span></span>
<span id="cb1-20"><a href="#cb1-20" aria-hidden="true" tabindex="-1"></a>    <span class="ot">]</span></span>
<span id="cb1-21"><a href="#cb1-21" aria-hidden="true" tabindex="-1"></a><span class="er">}</span></span></code></pre></div></td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">secureMondrianConnection</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    {commonAttributes}</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">dataSourceReference</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">uri</span>&gt;{dataSourceUri}&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">dataSourceReference</span>&gt;</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">schemaReference</span>&gt;</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">uri</span>&gt;{schemaFileResourceUri}&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">schemaReference</span>&gt;</span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">accessGrantSchemas</span>&gt;</span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">accessGrantSchemaReference</span>&gt;</span>
<span id="cb2-11"><a href="#cb2-11" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">uri</span>&gt;{accessGrantSchemaFileResourceUri}&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb2-12"><a href="#cb2-12" aria-hidden="true" tabindex="-1"></a>        &lt;/<span class="kw">accessGrantSchemaReference</span>&gt;</span>
<span id="cb2-13"><a href="#cb2-13" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">accessGrantSchemas</span>&gt;</span>
<span id="cb2-14"><a href="#cb2-14" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">secureMondrianConnection</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

## 1.0.1.21 OLAP Unit

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>application/repository.olapUnit+json</p></th>
<th><p>application/repository.olapUnit+xml</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="er">{commonAttributes</span><span class="fu">}</span><span class="er">,</span> </span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;mdxQuery&quot;</span><span class="er">:</span><span class="st">&quot;{mdxQuery}&quot;</span><span class="er">,</span> </span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;olapConnection&quot;</span><span class="er">:</span> <span class="fu">{</span> </span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;olapConnectionReference&quot;</span><span class="fu">:</span> <span class="fu">{</span>         </span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;uri&quot;</span><span class="fu">:</span> <span class="st">&quot;{olapConnectionReferenceUri}&quot;</span>      </span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>        <span class="fu">}</span>  </span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span> </span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a><span class="er">}</span></span></code></pre></div></td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">olapUnit</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    {commonAttributes}</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">mdxQuery</span>&gt;{mdxQuery}&lt;/<span class="kw">mdxQuery</span>&gt;  </span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">olapConnectionReference</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">uri</span>&gt;{olapConnectionReferenceUri}&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">olapConnectionReference</span>&gt; </span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">olapUnit</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

## 1.0.1.22 Mondrian XML/A Definition

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>application/repository.mondrianXmlaDefinition+json</p></th>
<th><p>application/repository.mondrianXmlaDefinition+xml</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="er">{commonAttributes</span><span class="fu">}</span><span class="er">,</span> </span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;catalog&quot;</span><span class="er">:</span><span class="st">&quot;{catalog}&quot;</span><span class="er">,</span> </span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    <span class="st">&quot;mondrianConnection&quot;</span><span class="er">:</span> <span class="fu">{</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;mondrianConnectionReference&quot;</span><span class="fu">:</span> <span class="fu">{</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>            <span class="dt">&quot;uri&quot;</span><span class="fu">:</span> <span class="st">&quot;{mondrianConnectionResourceUri}&quot;</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>        <span class="fu">}</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span> </span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a><span class="er">}</span></span></code></pre></div></td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">mondrianXmlaDefinition</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    {commonAttributes}</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">catalog</span>&gt;{catalog}&lt;/<span class="kw">catalog</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">mondrianConnectionReference</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">uri</span>&gt;{mondrianConnectionResourceUri}&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">mondrianConnectionReference</span>&gt;</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">mondrianXmlaDefinition</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

## 1.0.1.23 Other Types

The following types are defined in commercial editions of the server and appear in the repository. However, they are meant only to describe the corresponding resources as read-only objects in the repository. The REST API does not support services for clients to create or modify these types.

The types in the following table contain only the Common Attributes.

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
<td><p>application/repository.dashboard+json<br />
application/repository.dashboard+xml</p></td>
<td><p>The dashboard resource descriptors are deprecated and subject to change.</p></td>
</tr>
<tr>
<td><p>application/repository.adhocDataView+json<br />
application/repository.adhocDataView+xml</p></td>
<td><p>The Ad Hoc view type is not fully defined yet and subject to change. Ad Hoc views may be referenced as data sources in other repository types, in which case they are called advDataSource.</p></td>
</tr>
</tbody>
</table>
