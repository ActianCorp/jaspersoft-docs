---
title: The resources Service
description: The restv2/resources service searches the repository and accesses the resources it contains. This service provides performance and consistent handling of resource descriptors for all repository...
---

# The resources Service

The rest_v2/resources service searches the repository and accesses the resources it contains. This service provides performance and consistent handling of resource descriptors for all repository resource types. The service has two formats. One format takes search parameters to find resources, and the other format takes a repository URI to access resource descriptors and file contents.

For further information, see:

-   [Chapter 1, “Working With Resources,” on page 1](working_with_resources.md) for general guidelines about using descriptors.

-   [Chapter 1, “Resource Descriptors,” on page 1](resource_descriptors.md) for a reference to every type of resource and its attributes.

-   [Chapter 1, “Working With File Resources,” on page 1](file_resources.md) to download and upload file resources.

-   [Chapter 1, “Working With Domains,” on page 1](metadata.md) to view domains and their nested resources.

    This chapter includes the following sections:

-   [Searching the Repository](#searching-the-repository)

-   [Paginating Search Results](#paginating-search-results)

-   [Viewing Resource Details](#viewing-resource-details)

-   [Creating a Resource](#creating-a-resource)

-   [Modifying a Resource](#modifying-a-resource)

-   [Copying a Resource](#copying-a-resource)

-   [Moving a Resource](#moving-a-resource)

-   [Deleting Resources](#deleting-resources)

## Searching the Repository

The resources service, when used without specifying any repository URI, is used to search the repository. The various parameters listed in the following table let you refine the search and specify how you receive search results. For example, the search and results pagination parameters can be used to implement an interface to repository resources in a REST client application.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th>Method</th>
<th colspan="2">URL</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>GET</p></td>
<td colspan="2"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/resources</span>?&lt;arguments&gt;</span></p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><span>q</span></p></td>
<td><p>String</p></td>
<td><p>Search for resources having the specified text in the name or description. Note that the search string does not match in the ID of resources.</p></td>
</tr>
<tr>
<td><p><span>folderUri</span></p></td>
<td><p>String</p></td>
<td><p>The path of the base folder for the search.</p></td>
</tr>
<tr>
<td><p><span>recursive</span></p></td>
<td><p>true|false</p></td>
<td><p>Indicates whether the search should include all subfolders recursively. When omitted, the default behavior is recursive (true).</p></td>
</tr>
<tr>
<td><p><span>excludeFolder</span></p></td>
<td><p>String</p></td>
<td><p>A folder to exclude from the results, for example excludeFolder=/public.</p></td>
</tr>
<tr>
<td><p><span>type</span></p></td>
<td><p>String</p></td>
<td><p>Match only resources of the given type. Valid types are listed in <a href="resource_descriptors.md">Chapter 1, “Resource Descriptors,” on page 1</a>, for example: <span>dataType</span>, <span>jdbcDataSource</span>, <span>reportUnit</span>, or <span>file</span>. Multiple type parameters are allowed. Wrong values are ignored.</p></td>
</tr>
<tr>
<td><p><span>accessType</span></p></td>
<td><p>viewed<br />
|modified</p></td>
<td><p>Filters the results by access events: <span>viewed</span> (by current user) or <span>modified</span> (by current user). By default, no access event filter is applied.</p></td>
</tr>
<tr>
<td><span>dependsOn</span></td>
<td><span>/path/to/resource</span></td>
<td>Searches for all resources depending on the specified resource. Only data source and <span>reportUnit</span> resources may be specified. If this parameter is specified, then all the other parameters except pagination are ignored.</td>
</tr>
<tr>
<td><p><span>showHidden<br />
Items</span></p></td>
<td><p>true|false</p></td>
<td><p>When set to true, the results include nested local resources (in <span>_files</span>) as if they were in the repository. For more information, see <a href="working_with_resources.md">1.1, “Local Resources,” on page 1</a>. By default, hidden items are not shown (false).</p></td>
</tr>
<tr>
<td><p><span>favorites</span></p></td>
<td><p>true|false</p></td>
<td><p>When it is set to true, the service lists the resources that are added to Favorites. By default favorites is false.</p></td>
</tr>
<tr>
<td><p><span>sortBy</span></p></td>
<td><p>optional<br />
String</p></td>
<td><p>One of the following strings representing a field in the results to sort by: <span>uri</span>, <span>label</span>, <span>description</span>, <span>type</span>, <span>creationDate</span>, <span>updateDate</span>, <span>accessTime</span>, or <span>popularity</span> (based on access events). By default, results are sorted alphabetically by label.</p></td>
</tr>
<tr>
<td colspan="2"><p><span>limit</span><br />
<span>offset</span><br />
<span>forceFullPage</span><br />
<span>forceTotalCount</span></p></td>
<td><p>Pagination is enabled by default, and the default limit is 100 results. By default, permissions are applied after raw results, such that the search returns fewer than 100 items but there are more pages of results. If you work with large repositories, you must handle pagination issues. These parameters are described in <a href="#paginating-search-results">1.1, “Paginating Search Results,” on page 1</a>.</p></td>
</tr>
<tr>
<td colspan="3"><p>Options</p></td>
</tr>
<tr>
<td colspan="3"><p><span>accept: application/json</span> (default)</p>
<p><span>accept: application/xml</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK - The body contains a list of <span>resourceLookup</span> descriptors representing the results of the search.</p></td>
</tr>
</tbody>
</table>

The response of a search is a set of shortened descriptors showing only the common attributes of each resource. One additional attribute specifies the type of the resource. This allows the client to receive a list of resources for display or further processing quickly.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><p><span>application/json</span></p></th>
<th><p><span>application/xml</span></p></th>
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

## Paginating Search Results

Paginating search results can speed up the user experience by making smaller queries and displaying the fewer results one page at a time. By default, a page is approximately 100 repository items. If and when users request another page, your application needs to send another request to the server with the same search parameters but an updated offset number that fetches the next page.

!!! note

    When any folder in your repository contains more than 100 subfolders and resources, then the search results are paginated by default. This means you will not receive all results in a single request. In this case, you must use the pagination parameters to obtain more pages or change the pagination strategy as explained below.

Your application could perform further optimizations such as requesting a page and storing it before the user requests it. That way, the results can be displayed immediately, and each page can be fetched in the background while the user is looking at the previous page.

Pagination is complicated by the fact that JasperReports Server enforces permissions after performing the query based on your search parameters. This means that a default search can return fewer results than a full page, but this behavior can be configured.

There are 3 different combinations of settings that you can use for pagination.

-   Default pagination - Every page may have less than a complete page of results, but this is the fastest strategy and the easiest to implement.
-   Full page pagination - Ensures that every page has exactly the number of results that you specify, but this makes the server perform more queries, and it requires extra logic in the client.
-   No pagination - Requests all search results in a single reply, which is the simplest to process but can block the caller for a noticeable delay when there are many results.

The advantages and disadvantages of each pagination strategy are described in the following sections. Choose a strategy for your repository searches based on the types of searches being performed, the user performing the search, and the contents of your repository. Every request to the resources service can use a different pagination strategy. It is up to your client app to use the appropriate strategy and process the results accordingly.

### Default Pagination

With the default pagination, every page of results returned by the server may contain less than the designated page size. You can determine the number of actual results from the HTTP headers of the response. The headers also indicate whether there are further pages to fetch.

Default pagination has the best performance and, when configured with the right limit for the size of your repository, almost no delay in response for your users. Because results are filtered by permissions, the user credentials that you specify for the request determine how full each page is:

-   The system admin (`superuser`) has access to every resource, and therefore the results are effectively unfiltered and each page is full. But the same can be true when you perform a search as jasperadmin within his organization, or even as a plain user within a folder where the user has full read permission. In these cases, the default pagination is very efficient and has no partially full pages.
-   If you are performing a sparse search, for example finding all reports that a given user has permission to access within an entire and large organization, then the results may have many partially full pages, all of differing lengths. In this case, you may prefer to use [1.1, “Full Page Pagination,” on page 1](#full-page-pagination).

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>Arguments to resources for Default Pagination</p></th>
</tr>
<tr>
<th><p>Argument</p></th>
<th><p>Type/Value</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><span>limit</span><br />
</p></td>
<td><p>integer<br />
default is 100</p></td>
<td><p>This defines the page size, which is the maximum number of resources to return in each response. However, with default pagination, the response likely had less than this value of responses. The default limit is 100. You can set the limit higher or lower if you want to process generally larger or smaller pages, respectively.</p></td>
</tr>
<tr>
<td><p><span>offset</span></p></td>
<td><p>integer</p></td>
<td><p>By setting the offset to a whole multiple of the limit, you select a specific page of the results. The default offset is 0 (first page). With a limit of 100, subsequent calls should set <span>offset=100</span> (second page), <span>offset=200</span> (third page), etc.</p></td>
</tr>
<tr>
<td><span>forceFullPage</span></td>
<td>false (default)</td>
<td>The default is false, so you do not need to specify this parameter.</td>
</tr>
<tr>
<td><p><span>forceTotal<br />
Count</span></p></td>
<td><p>true|false</p></td>
<td><p>When true, the <span>Total-Count</span> header is set in every paginated response, which impacts performance. When false, the default, the header is set in the first page only. Note that <span>Total-Count</span> is the intermediate, unfiltered count of results, not the number of results returned by this service.</p></td>
</tr>
</tbody>
</table>

With each response, you can process the HTTP headers to help you display the pagination controls:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th colspan="2"><p>Headers in Responses for Default Pagination</p></th>
</tr>
<tr>
<th>Header</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><span>Result-Count</span></td>
<td>This is the number of results that are contained in the current response. It can be less than or equal to the limit.</td>
</tr>
<tr>
<td><span>Start-Index</span></td>
<td>The <span>Start-Index</span> in the response is equal to the offset specified in the request. With a <span>limit=100</span>, it is 0 on the first page, 100 on the second page, etc.</td>
</tr>
<tr>
<td><span>Next-Offset</span></td>
<td>This is the offset to request the next page. With <span>forceFullPage=false</span>, the <span>Next-Offset</span> is equivalent to the <span>Start-Index+limit</span>, except on the last page. On the last page, the <span>Next-Offset</span> is omitted to indicate there are no further pages.</td>
</tr>
<tr>
<td><span>Total-Count</span></td>
<td><p>This is the total number of results before permissions are applied. This is not the total number of results for this search by this user, but it is an upper bound. Dividing this number by the limit gives the number of pages that will be required, though not every page will have the full number of results.</p>
<p>As described in the previous table, this header only appears on the first response, unless <span>forceTotalCount=true</span>.</p></td>
</tr>
</tbody>
</table>

### Full Page Pagination

Full Page pagination ensures that every page, except the last one, has the same number of results, the number given by the limit parameter. To do this, JasperReports Server performs extra queries after filtering results for permission, until each page has the full number of results. Though small, the extra queries have a performance impact and may slow down the request. In addition, your client must read the HTTP header in every response to determine the offset value for the next page.

For full page pagination, set the pagination parameters of the resources service as follows:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>Arguments of resources for Full Page Pagination</p></th>
</tr>
<tr>
<th><p>Argument</p></th>
<th><p>Type/Value</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><span>limit</span><br />
</p></td>
<td><p>integer<br />
default is 100</p></td>
<td><p>Specifies the exact number of resources to return in each response. This is equivalent to the number of results per page. The default limit is 100. You can set the limit higher or lower if you want to process larger or smaller pages, respectively.</p></td>
</tr>
<tr>
<td><p><span>offset</span></p></td>
<td><p>integer</p></td>
<td><p>Specifies the overall offset to use for retrieving the next page of results. The default offset is 0 (first page). For subsequent pages, you must specify the value given by the <span>Next-Offset</span> header, as described in the next table.</p></td>
</tr>
<tr>
<td><span>forceFullPage</span></td>
<td>true</td>
<td>Setting this parameter to true enables full page pagination. Depending on the type of search and user permissions, this parameter can cause significant performance delays.</td>
</tr>
<tr>
<td><p><span>forceTotal<br />
Count</span></p></td>
<td><p>do not use</p></td>
<td><p>When <span>forceFullPage</span> is true, the <span>Total-Count</span> header is set in every response, even if this parameter is false by default.</p></td>
</tr>
</tbody>
</table>

With each response, you must process the HTTP headers as follows:

<table>
<thead>
<tr>
<th colspan="2"><p>Headers in Responses for Full Page Pagination</p></th>
</tr>
<tr>
<th>Header</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><span>Result-Count</span></td>
<td>This is the number of results that are contained in the current response. With full page pagination, it is equal to the limit in every response except for the last page.</td>
</tr>
<tr>
<td><span>Start-Index</span></td>
<td>The <span>Start-Index</span> in the response is equal to the offset specified in the request. It changes with every request-response.</td>
</tr>
<tr>
<td><span>Next-Offset</span></td>
<td>The server calculates this value based on the extra queries that it performed to fill the page with permission-filtered results. To avoid duplicate results or skipped results, your client must read this number and submit it as the offset in the request for the next page. When this value is omitted from the header, it indicates that there are no further pages.</td>
</tr>
<tr>
<td><span>Total-Count</span></td>
<td>This is the total number of results before permissions are applied. This is not the total number of results for this search by this user, but it is an upper bound.</td>
</tr>
</tbody>
</table>

### No Pagination

In certain cases, you can turn off pagination. Use this for the small search request that you want to process as a whole, for example a listing of all reports in a folder. In this case, you receive and process all results in a single response and do not need to implement the logic for pagination. You should only use this for result sets that are known to be small.

To turn off pagination, set the pagination parameters of the resources service as follows:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>Arguments to resources for No Pagination</p></th>
</tr>
<tr>
<th><p>Argument</p></th>
<th><p>Type/Value</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><span>limit</span><br />
</p></td>
<td><p>0</p></td>
<td><p>To return all results without pagination, set limit=0. Do not set limit=0 for large searches, for example from the root of the repository, because it can cause significant delays and return a very large number of results.</p></td>
</tr>
<tr>
<td><p><span>offset</span></p></td>
<td><p>do not use</p></td>
<td><p>The default offset is 0, which is the start of the single page of results.</p></td>
</tr>
<tr>
<td><span>forceFullPage</span></td>
<td>do not use</td>
<td>This setting has no meaning when there is no limit.</td>
</tr>
<tr>
<td><p><span>forceTotal<br />
Count</span></p></td>
<td><p>do not use</p></td>
<td><p>The Total-Count header is included in the first (and only) response. Note that Total-Count is the intermediate, unfiltered count of results, not the number of results returned by this service.</p></td>
</tr>
</tbody>
</table>

With each response, you must process the HTTP headers as follows:

<table>
<thead>
<tr>
<th colspan="2"><p>Headers in Responses for No Pagination</p></th>
</tr>
<tr>
<th>Header</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><span>Result-Count</span></td>
<td>This is the number of results contained in the current response. Thus, this header indicates how many results you should process in the single response.</td>
</tr>
<tr>
<td><span>Start-Index</span></td>
<td>This is 0 for a single response containing all the search results.</td>
</tr>
<tr>
<td><span>Next-Offset</span></td>
<td>This header is omitted because there is no next page.</td>
</tr>
<tr>
<td><span>Total-Count</span></td>
<td>This is the total number of results before permissions are applied. It is of little use.</td>
</tr>
</tbody>
</table>

## Viewing Resource Details

Use the GET method and a resource URI to request the resource's complete descriptor.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th>Method</th>
<th colspan="3">URL</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>GET</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/resources</span>/path/to/resource?&lt;argument&gt;</span></p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><span>expanded</span></p></td>
<td><p>true|false</p></td>
<td colspan="2"><p>When true, all nested resources are given as full descriptors. The default behavior, false, has all nested resources given as references. For more information, see <a href="working_with_resources.md">1.1, “Local Resources,” on page 1</a>.</p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p><span>accept: application/json</span> (default)</p>
<p><span>accept: application/xml</span></p>
<p><span>accept: application/repository.folder+&lt;format&gt;</span> (specifically to view the folder resource)</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK - The response indicates the content-type and contain the corresponding descriptor, for example:</p>
<p><span>application/repository.dataType+json</span></p></td>
<td><p>404 Not Found - The specified resource is not found in the repository.</p></td>
</tr>
</tbody>
</table>

## Creating a Resource

The POST and PUT methods offer alternative ways to create resources. Both take a resource descriptor but each handles the URL differently.

With the POST method, specify a folder in the URL, and the new resource ID is created automatically from the label attribute in its descriptor.

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
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/resources</span>/path/to/folder?&lt;argument&gt;</span></p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><span>create<br />
Folders</span></p></td>
<td><p>true|false</p></td>
<td colspan="2"><p>By default, this is true, and the service will create all parent folders if they do not already exist. When set to false, the folders specified in the URL must all exist, otherwise the service returns an error.</p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/repository.<br />
&lt;resourceType&gt;+json</span></p>
<p><span>application/repository.<br />
&lt;resourceType&gt;+xml</span></p></td>
<td colspan="2"><p>A well-defined descriptor of the specified type and format. See <a href="resource_descriptors.md">Chapter 1, “Resource Descriptors,” on page 1</a></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>201 Created - The request was successful and, for confirmation, the response contains the full descriptor of the resource that was just created.</p></td>
<td><p>400 Bad Request - Mismatch between the content-type and the fields or syntax of the actual descriptor.</p></td>
</tr>
</tbody>
</table>

With the PUT method, specify a unique new resource ID as part of the URL. For more information, see [1.1, “Resource URI,” on page 1](working_with_resources.md).

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
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/resources</span>/path/to/resource<br />
?&lt;arguments&gt;</span></p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><span>create<br />
Folders</span></p></td>
<td><p>true|false</p></td>
<td colspan="2"><p>True by default, and the service will create all parent folders if they do not already exist. When set to false, the folders specified in the URL must all exist, otherwise the service returns an error.</p></td>
</tr>
<tr>
<td><p><span>overwrite</span></p></td>
<td><p>true|false</p></td>
<td colspan="2"><p>When true, the resource given in the URL is overwritten even if it is a different type than the resource descriptor in the content. The default is false.</p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/repository.<br />
&lt;resourceType&gt;+json</span></p>
<p><span>application/repository.<br />
&lt;resourceType&gt;+xml</span></p></td>
<td colspan="2"><p>A well defined descriptor of the specified type and format. See <a href="resource_descriptors.md">Chapter 1, “Resource Descriptors,” on page 1</a></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>201 Created - The request was successful and, for confirmation, the response contains the full descriptor of the resource that was just created.</p></td>
<td><p>400 Bad Request - Mismatch between the content-type and the fields or syntax of the actual descriptor.</p></td>
</tr>
</tbody>
</table>

The POST method also supports a way to create complex resources and their nested resources in a single multipart request.

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
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/resources</span>/path/to/folder</span></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>multipart/form-data</span></p></td>
<td colspan="2"><p>Root resource multipart item name: <span>resource</span></p>
<p>Root resource multipart Content-type and corresponding item names:</p>
<ul>
<li><p><span>mondrianConnection</span></p>
<ul>
<li><span>schema</span> - Mondrian schema XML file</li>
</ul></li>
<li><p><span>secureMondrianConnection</span></p>
<ul>
<li><span>schema</span> - Mondrian schema XML file</li>
<li><span>accessGrantSchemas.accessGrantSchema[{itemIndex}]</span> - XML file</li>
</ul></li>
<li><p><span>semanticLayerDataSource</span></p>
<ul>
<li><span>schema</span> - Domain schema XML file</li>
<li><span>securityFile</span> - XML security file</li>
<li><span>bundles.bundle[{bundleIndex}]</span> - Properties file for internationalization</li>
</ul></li>
<li><p><span>reportUnit</span></p>
<ul>
<li>jrxml - Report unit JRXML file</li>
<li><span>files.{fileName}</span> - Report unit attached resource file (for example, images)</li>
</ul></li>
</ul></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>201 Created - The request was successful and, for confirmation, the response contains the full descriptor of the resource that was just created.</p></td>
<td><p>400 Bad Request - Mismatch between the content-type and the fields or syntax of the actual descriptor.</p></td>
</tr>
</tbody>
</table>

## Modifying a Resource

Use the PUT method to overwrite an entire resource. PUT sends the entire descriptor for the resource. Specify the path of the target resource in the URL, and specify a resource of the same type in the descriptor. If you want to replace a resource of a different type, specify the overwrite=true argument. The createFolders argument isn't used for updates because the resource and the folders in its path must exist already.

The resource descriptor must completely describe the updated resource, not use individual fields. The descriptor must also use only references for nested resources, not other resources expanded inline. To update a local resource, use the PUT method with the hidden folder \_file in the path, and send a complete descriptor for the updated resource. For more information, see [1.1, “Local Resources,” on page 1](working_with_resources.md).

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
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/resources</span>/path/to/resource<br />
?&lt;arguments&gt;</span></p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><span>overwrite</span></p></td>
<td><p>true|false</p></td>
<td colspan="2"><p>When true, the resource given in the URL is overwritten even if it is a different type than the resource descriptor in the content. The default is false.</p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/repository.<br />
&lt;resourceType&gt;+json</span></p>
<p><span>application/repository.<br />
&lt;resourceType&gt;+xml</span></p></td>
<td colspan="2"><p>A well defined descriptor of the specified type and format. See <a href="resource_descriptors.md">Chapter 1, “Resource Descriptors,” on page 1</a>.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>201 Created - The resource was replaced and the response contains the full descriptor of the updated resource.</p></td>
<td><p>400 Bad Request - Mismatch between the content-type and the fields or syntax of the actual descriptor.</p></td>
</tr>
</tbody>
</table>

## Copying a Resource

Copying a resource uses the Content-Location HTTP header to specify the source of the copy operation. If any resource descriptor is sent in the request, it is ignored.

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
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/resources</span>/path/to/folder<br />
?&lt;arguments&gt;</span></p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><span>create<br />
Folders</span></p></td>
<td><p>true|false</p></td>
<td colspan="2"><p>True by default, and the service will create all parent folders if they do not already exist. When set to false, the folders specified in the URL must all exist, otherwise the service returns an error.</p></td>
</tr>
<tr>
<td><p><span>overwrite</span></p></td>
<td><p>true|false</p></td>
<td colspan="2"><p>When true, the target resource given in the URL is overwritten even if it is a different type than the resource descriptor in the content. The default is false.</p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p><span>Content-Location: {resourceSourceUri}</span> - Specifies the resource to be copied.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>201 Created - The request was successful and, for confirmation, the response contains the full descriptor of the resource that was just copied.</p></td>
<td><p>404 Not Found - When the <span>{resourceSourceUri}</span> is not valid.</p></td>
</tr>
</tbody>
</table>

## Moving a Resource

Moving a resource uses the PUT method, whereas copying it uses the POST method.

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
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/resources</span>/path/to/folder<br />
?&lt;arguments&gt;</span></p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><span>create<br />
Folders</span></p></td>
<td><p>true|false</p></td>
<td colspan="2"><p>True by default, and the service will create all parent folders if they do not already exist. When set to false, the folders specified in the URL must all exist, otherwise the service returns an error.</p></td>
</tr>
<tr>
<td><p><span>overwrite</span></p></td>
<td><p>true|false</p></td>
<td colspan="2"><p>When true, the target resource given in the URL is overwritten even if it is a different type than the resource descriptor in the content. The default is false.</p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p><span>Content-Location: {resourceSourceUri}</span> - Specifies the resource to be moved.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>201 Created - The request was successful and, for confirmation, the response contains the full descriptor of the resource that was just moved.</p></td>
<td><p>404 Not Found - When the <span>{resourceSourceUri}</span> is not valid.</p></td>
</tr>
</tbody>
</table>

## Deleting Resources

The DELETE method has two forms, one for single resources and one for multiple resources.

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
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/resources</span>/path/to/resource</span><br />
</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>204 No Content - The request always returns 204. If the resource existed, it has been deleted.</p></td>
<td><p>204 No Content - The request always returns 204, even if the resource path is invalid.</p></td>
</tr>
</tbody>
</table>

To delete multiple resources at once, specify multiple URIs with the resourceUri parameter.

<table>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>DELETE</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/resources</span>?resourceUri={uri}&amp;...</span></p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><span>resourceUri</span></p></td>
<td><p>string</p></td>
<td colspan="2"><p>Specifies a resource to delete. You may need to encode the / characters in the URI with <code>%2F</code>. Repeat this parameter to delete multiple resources.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>204 No Content - The request always returns 204. The resources with valid URIs are deleted.</p></td>
<td><p>204 No Content - The request always returns 204. No action is taken for invalid URIs.</p></td>
</tr>
</tbody>
</table>
