---
title: Paginating Search Results
description: "Paginating search results can speed up the user experience by making smaller queries and displaying the fewer results one page at a time. By default, a page is approximately 100 repository items. If..."
---

# Paginating Search Results

Paginating search results can speed up the user experience by making smaller queries and displaying the fewer results one page at a time. By default, a page is approximately 100 repository items. If and when users request another page, your application needs to send another request to the server with the same search paramters but an updated offset number that fetches the next page.

Your application could perform further optimizations such as requesting a page and storing it before the user requests it. That way, the results can be displayed immediately, and each page can be fetched in the background while the user is looking at the previous page.

Pagination is complicated by the fact that JasperReports® Server enforces permissions after performing the query based on your search ciriteria. This means that a default search can return fewer results than a full page, but this behavior can be configured.

There are 3 different combinations of settings that you can use for pagination.

-   Default pagination - Every page may have less than a complete page of results, but this is the most performant strategy and the easiest to implement.
-   Full page pagination - Ensures that every page has exactly the number of results that you specify, but this makes the server perform more queries, and it requires extra logic in the client.
-   No pagination - Requests all search results in a single reply, which is simplest to process but can block the caller for a noticeable delay when there are many results.

The advantages and disadvantages of each pagination strategy are described in the following sections. Choose a strategy for your respository searches based on the types searches being performed, the user performing the search, and the contents of your repository. Every request to the v2/resources service can use a different pagination strategy; it's up to your client app to use the appropriate strategy and process the results accordingly.

## Default Pagination

With the default pagination, every page of results returned by the server may contain less than the designated page size. You can determine the number of actual results from the HTTP headers of the response. The headers also indicate whether there are further pages to fetch.

Default pagination has the best performance and, when configured with the right limit for the size of your repository, almost no delay in response for your users. Because results are filtered by permissions, the user credentials that you specify for the request determine how full each page is:

-   The system admin (`superuser`) has access to every resource, and therefore the results are effectively unfiltered and each page is full. But the same can be true when you perform a search as jasperadmin within his organization, or even as a plain user within a folder where the user has full read permission. In these cases the default pagination is very efficient and has no partially-full pages.
-   If you are performing a sparse search, for example finding all reports that a given user has permission to access within an entire and large organization, then the results may have many partially-full page, all of differing lengths. In this case, you may prefer to use [“Full Page Pagination” on page 1](#full-page-pagination).

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>Parameters of v2/resources for Default Pagination</p></th>
</tr>
<tr>
<th><p>Parameter</p></th>
<th><p>Type/Value</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>limit<br />
</p></td>
<td><p>integer<br />
default is 100</p></td>
<td><p>This defines the page size, which is maximum number of resources to return in each response. However, with default pagination, the response is likely have less than this value of responses. The default limit is 100. You can set the limit higher or lower if you want to process generally larger or smaller pages, respectively.</p></td>
</tr>
<tr>
<td><p>offset</p></td>
<td><p>integer</p></td>
<td><p>By setting the offset to a whole multiple of the limit, you select a specific page of the results. The default offset is 0 (first page). With a limit of 100, subsequent calls should set offset=100 (second page), offset=200 (third page), etc.</p></td>
</tr>
<tr>
<td>forceFullPage</td>
<td>false (default)</td>
<td>The default is false, so you do not need to specify this parameter.</td>
</tr>
<tr>
<td><p>forceTotal<br />
Count</p></td>
<td><p>true|false</p></td>
<td><p>When true, the Total-Count header is set in every paginated response, which impacts performance. When false, the default, the header is set in the first page only. Note that Total-Count is the intermediate, unfiltered count of results, not the number of results returned by this service.</p></td>
</tr>
</tbody>
</table>

With each response, you can process the HTTP headers to help you display pagination controls:

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
<td>Result-Count</td>
<td>This is the number of results that are contained in the current response. It can be less than or equal to the limit.</td>
</tr>
<tr>
<td>Start-Index</td>
<td>The Start-Index in the response is equal to the offset specified in the request. With a limit=100, it will be 0 on the first page, 100 on the second page, etc.</td>
</tr>
<tr>
<td>Next-Offset</td>
<td>This is the offset to request the next page. With forceFullPage=false, the Next-Offset is equivalent to Start-Index+limit, except on the last page. On the the last page, the Next-Offset is omitted to indicate there are no further pages.</td>
</tr>
<tr>
<td>Total-Count</td>
<td><p>This is the total number of results before permissions are applied. This is not the total number of results for this search by this user, but it is an upper bound. Dividing this number by the limit gives the number of pages that will be required, though not every page will have the full number of results.</p>
<p>As described in the previous table, this header only appears on the first response, unless forceTotalCount=true.</p></td>
</tr>
</tbody>
</table>

## Full Page Pagination

Full Page pagination ensures that every page, except the last one, has the same number of results, the number given by the limit parameter. To do this, JasperReports® Server performs extra queries after filtering results for permission, unitl each page has the full number of results. Though small, the extra queries have a performance impact and may slow down the request. In addition, your client must read the HTTP header in every response to determine the offset value for the next page.

For full page pagination, set the pagination parameters of the v2/resources service as follows:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>Parameters of v2/resources for Full Page Pagination</p></th>
</tr>
<tr>
<th><p>Parameter</p></th>
<th><p>Type/Value</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>limit<br />
</p></td>
<td><p>integer<br />
default is 100</p></td>
<td><p>Specifies the exact number of resources to return in each response. This is eqivalent to the number of results per page. The default limit is 100. You can set the limit higher or lower if you want to process larger or smaller pages, respectively.</p></td>
</tr>
<tr>
<td><p>offset</p></td>
<td><p>integer</p></td>
<td><p>Specifies the overall offset to use for retrieving the next page of resuslts. The default offset is 0 (first page). For subsequent pages, you must specify the value given by the Next-Offset header, as described in the next table.</p></td>
</tr>
<tr>
<td>forceFullPage</td>
<td>true</td>
<td>Setting this paramter to true enables full page pagination. Depending on the type of search and user permissions, this parameter can cause signifiant performance delays.</td>
</tr>
<tr>
<td><p>forceTotal<br />
Count</p></td>
<td><p>do not use</p></td>
<td><p>When forceFullPage is true, the Total-Count header is set in every response, even if this parameter is false by default.</p></td>
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
<td>Result-Count</td>
<td>This is the number of results that are contained in the current response. With full page pagination, it is equal to the limit in every response except for the last page.</td>
</tr>
<tr>
<td>Start-Index</td>
<td>The Start-Index in the response is equal to the offset specified in the request. It changes with every request-response.</td>
</tr>
<tr>
<td>Next-Offset</td>
<td>The server calculates this value based on the extra queries it performed to fill the page swith permission-filtered results. In order to avoide duplicate results or skipped results, your client must read this number and submit it as the offset in the request for the next page. When this value is omitted from the header, it indicates there are no further pages.</td>
</tr>
<tr>
<td>Total-Count</td>
<td>This is the total number of results before permissions are applied. This is not the total number of results for this search by this user, but it is an upper bound.</td>
</tr>
</tbody>
</table>

## No Pagination

In certain cases, you can turn off pagination. Use this for small search request that you want to process as a whole, for example a listing of all reports in a folder. In this case, your receive and process all results in a single response and do not need to implement the logic for pagination. You should only use this for result sets that are known to be small.

To turn off pagination, set the pagination parameters of the v2/resources service as follows:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>Parameters of v2/resources for No Pagination</p></th>
</tr>
<tr>
<th><p>Parameter</p></th>
<th><p>Type/Value</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>limit<br />
</p></td>
<td><p>0</p></td>
<td><p>To return all results without pagination, set limit=0. Do not set limit=0 for large searches, for example from the root of the repository, because it can cause significant delays and return a very large number of results.</p></td>
</tr>
<tr>
<td><p>offset</p></td>
<td><p>do not use</p></td>
<td><p>The default offset is 0, which is the start of the single page of results.</p></td>
</tr>
<tr>
<td>forceFullPage</td>
<td>do not use</td>
<td>This setting has no meaning when there is no limit.</td>
</tr>
<tr>
<td><p>forceTotal<br />
Count</p></td>
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
<td>Result-Count</td>
<td>This is the number of results contained in the current response. Thus, this header indicates how many results you should process in the single response.</td>
</tr>
<tr>
<td>Start-Index</td>
<td>This is 0 for a single response containing all the search results.</td>
</tr>
<tr>
<td>Next-Offset</td>
<td>This header is omitted because there is no next page.</td>
</tr>
<tr>
<td>Total-Count</td>
<td>This is the total number of results before permissions are applied. It is of little use.</td>
</tr>
</tbody>
</table>
