---
title: Extended Job Search
description: "The GET method is also used for more advanced job searches. Some field of the jobsummary descriptor can be used directly as parameters, and fields of the job descriptor can also be used as search..."
---

# 1.0.1 Extended Job Search

The GET method is also used for more advanced job searches. Some field of the jobsummary descriptor can be used directly as parameters, and fields of the job descriptor can also be used as search criteria. You can also control the pagination and sorting order of the reply.

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/jobs</span>?&lt;arguments&gt;</p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p>label</p></td>
<td><p>string</p></td>
<td colspan="2"><p>The name of the report job.</p></td>
</tr>
<tr>
<td><p>owner</p></td>
<td><p>string</p></td>
<td colspan="2"><p>The username of the report job creator; the user who scheduled the report.</p></td>
</tr>
<tr>
<td><p><code>reportUnitURI?</code><br />
</p></td>
<td><p>/path/to/report</p></td>
<td colspan="2"><p>Gives the repository URI of a report to list all jobs. When this argument is omitted, this method returns all jobs for all reports.</p></td>
</tr>
<tr>
<td><p>example?</p></td>
<td><p>JSON jobModel</p></td>
<td colspan="2"><p>Searches for jobs that match the JSON jobModel. The jobModel is a fragment of a job descriptor containing one or more fields to be matched.</p></td>
</tr>
<tr>
<td><p>numberOf</p>
<p>Rows</p></td>
<td><p>integer</p></td>
<td colspan="2"><p>Turns on pagination of the result by specifying the number of jobsummary descriptors per results page.</p></td>
</tr>
<tr>
<td><p>startIndex</p></td>
<td><p>integer</p></td>
<td colspan="2"><p>Determines the page number in paginated results by specifying the index of the first jobsummary to be returned.</p></td>
</tr>
<tr>
<td><p>sortType</p></td>
<td></td>
<td colspan="2"><p>Possible values are: NONE, SORTBY_JOBID, SORTBY_JOBNAME, SORTBY_REPORTURI, SORTBY_REPORTNAME, SORTBY_REPORTFOLDER, SORTBY_OWNER, SORTBY_STATUS, SORTBY_LASTRUN, SORTBY_NEXTRUN</p></td>
</tr>
<tr>
<td><p>isAscending</p></td>
<td><p>true / false</p></td>
<td colspan="2"><p>Determines the sort order: ascending if true, descending if false or omitted.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The body contains XML that describes jobs in the scheduler that match the search criteria.</p></td>
<td><p>404 Not Found – When the specified report is not found in the server.</p></td>
</tr>
</tbody>
</table>

The body of the return value is an XML jobs descriptor containing jobsummary descriptors, as shown in section [Listing Report Jobs](listing_report_jobs.md).

The `example` parameter lets you specify a search on fields in the job descriptor, such as output formats. Some fields may be specified in both the `example` parameter and in a dedicated parameter, for example label. In that case, the search specified in the `example` parameter takes precedence.

For example, you can search for all jobs that specify and output format of PDF. The JSON string to specify this field is:

{"outputFormat":"PDF"}

And the corresponding URI, with proper encoding, is:

http://\<host\>:\<port\>/jasperserver\[-pro\]/rest_v2/jobs?example=%7b%22outputFormat%22%3a%22PDF%22%7d
