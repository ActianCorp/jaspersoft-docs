---
title: Searching the Repository
description: "The v2/resources service, when used without specifying any repository URI, is used to search the repository. The various parameters listed in the following table let you refine the search and specify..."
---

# Searching the Repository

The v2/resources service, when used without specifying any repository URI, is used to search the repository. The various parameters listed in the following table let you refine the search and specify how you receive search results. For example, the search and results pagination parameters can be used to implement an interface to repository resources in a REST client application.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>GET</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/resources</span>?&lt;parameters&gt;</p></td>
</tr>
<tr>
<td><p>Parameter</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p>q</p></td>
<td><p>String</p></td>
<td colspan="2"><p>Search for resources having the specified text in the name or description. Note that the search string does not match in the ID of resources.</p></td>
</tr>
<tr>
<td><p>folderUri</p></td>
<td><p>String</p></td>
<td colspan="2"><p>The path of the base folder for the search.</p></td>
</tr>
<tr>
<td><p>recursive</p></td>
<td><p>true|false</p></td>
<td colspan="2"><p>Indicates whether search should include all sub-folders recursively. When omitted, the default behavior is recursive (true).</p></td>
</tr>
<tr>
<td><p>type</p></td>
<td><p>String</p></td>
<td colspan="2"><p>Match only resources of the given type. Valid types are listed in <a href="v2_resource_descriptor_types.md">V2 Resource Descriptor Types</a>, for example: dataType, jdbcDataSource, reportUnit, or file. Multiple type parameters are allowed. Wrong values are ignored.</p></td>
</tr>
<tr>
<td><p>accessType</p></td>
<td><p>viewed<br />
|modified</p></td>
<td colspan="2"><p>Filters the results by access events: viewed (by current user) or modified (by current user). By default, no access event filter is applied.</p></td>
</tr>
<tr>
<td>dependsOn</td>
<td>/path/to/resource</td>
<td colspan="2">Searches for all resources depending on specified resource. Only data source and reportUnit resources may be specified. If this parameter is specified, then all the other parameters except pagination are ignored.</td>
</tr>
<tr>
<td><p>showHidden<br />
Items</p></td>
<td><p>true|false</p></td>
<td colspan="2"><p>When set to true, results include nested local resources (in _files) as if they were in the repository. For more information, see <a href="the_v2_resources_service.md">Local Resources</a>. By default, hidden items are not shown (false).</p></td>
</tr>
<tr>
<td><p>sortBy</p></td>
<td><p>optional<br />
String</p></td>
<td colspan="2"><p>One of the following strings representing a field in the results to sort by: uri, label, description, type, creationDate, updateDate, accessTime, or popularity (based on access events). By default, results are sorted alphabetically by label.</p></td>
</tr>
<tr>
<td colspan="2"><p>limit<br />
offset<br />
forceFullPage<br />
forceTotalCount</p></td>
<td colspan="2"><p>These parameters are described in <a href="paginating_search_results.md">Paginating Search Results</a></p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p>accept: application/json (default)</p>
<p>accept: application/xml</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The body contains a list of resourceLookup descriptors representing the results of the search.</p></td>
<td><p>404 Not Found – The specified folder is not found in the repository.</p>
<p>204 No Content – All type values specified are invalid.</p></td>
</tr>
</tbody>
</table>

The response of a search is a set of shortened descriptors showing only the common attributes of each resource. One additional attribute specifies the type of the resource. This allows the client to quickly receive a list of resources for display or further processing.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p>application/json</p></th>
<th><p>application/xml</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="ot">[</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="fu">{</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;uri&quot;</span> <span class="fu">:</span><span class="st">&quot;/sample/resource/uri&quot;</span><span class="fu">,</span> </span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;label&quot;</span><span class="fu">:</span><span class="st">&quot;Sample Label&quot;</span><span class="fu">,</span> </span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;description&quot;</span><span class="fu">:</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>            <span class="st">&quot;Sample Description&quot;</span><span class="fu">,</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;type&quot;</span><span class="fu">:</span><span class="st">&quot;folder&quot;</span> </span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>        <span class="st">&quot;permissionMask&quot;</span><span class="er">:</span><span class="st">&quot;0&quot;</span><span class="fu">,</span></span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;creationDate&quot;</span><span class="fu">:</span></span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>            <span class="st">&quot;2013-07-04T12:18:47&quot;</span><span class="fu">,</span></span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;updateDate&quot;</span><span class="fu">:</span></span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>            <span class="st">&quot;2013-07-04T12:18:47&quot;</span><span class="fu">,</span> </span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>        <span class="dt">&quot;version&quot;</span><span class="fu">:</span><span class="st">&quot;0&quot;</span></span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span><span class="ot">,</span></span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>    <span class="er">...</span></span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a><span class="ot">]</span></span></code></pre></div></td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">resources</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceLookup</span>&gt;</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">uri</span>&gt;/sample/resource/uri&lt;/<span class="kw">uri</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">label</span>&gt;Sample Label&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">description</span>&gt;Sample Description</span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>            &lt;/<span class="kw">description</span>&gt;</span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">type</span>&gt;folder&lt;/<span class="kw">type</span>&gt;</span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">permissionMask</span>&gt;0&lt;/<span class="kw">permissionMask</span>&gt;</span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">creationDate</span>&gt;2013-07-04T12:18:47</span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a>            &lt;/<span class="kw">creationDate</span>&gt;</span>
<span id="cb2-11"><a href="#cb2-11" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">updateDate</span>&gt;2013-07-04T12:18:47</span>
<span id="cb2-12"><a href="#cb2-12" aria-hidden="true" tabindex="-1"></a>            &lt;/<span class="kw">updateDate</span>&gt;</span>
<span id="cb2-13"><a href="#cb2-13" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">version</span>&gt;0&lt;/<span class="kw">version</span>&gt;</span>
<span id="cb2-14"><a href="#cb2-14" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceLookup</span>&gt;</span>
<span id="cb2-15"><a href="#cb2-15" aria-hidden="true" tabindex="-1"></a>    ...</span>
<span id="cb2-16"><a href="#cb2-16" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">resources</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>
