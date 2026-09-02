---
title: The jobs Service
description: The restv2/jobs service provides the interface to schedule reports and dashboards and manage those schedules. When a user schedules a report or dashboard to run at a given time and with a given...
---

# The jobs Service

The rest_v2/jobs service provides the interface to schedule reports and dashboards and manage those schedules. When a user schedules a report or dashboard to run at a given time and with a given recurrence, the server stores this information in a job. There can be any number of jobs for any number of reports and dashboards, all created by different users. As with the server's user interface, the jobs service only manages jobs that are active, which means they have a trigger that is still pending in the future. Jobs that have finished and are no longer active are never listed or returned.

Within the job, the trigger determines when it will run. A trigger is said to fire when it reaches its scheduled time, and when it does, the server generates the output associated with the job. Various other properties define the filename of the output and where it is stored, emailed, or both. For example, you can define a job to run every Monday at 6 AM, except on company holidays, to generate a report in both PDF and Excel output and have the files written to the repository with sequential filenames, with links to the output emailed to a list of recipients, and any errors emailed to administrators.

The jobs service also uses exclusion calendars that can be defined in [The jobs calendars Service](jobscalendars.md).

This chapter includes the following sections:

-   [Searching for Jobs](#searching-for-jobs)
-   [Viewing a Job Definition](#viewing-a-job-definition)
-   [The job Descriptor](#the-job-descriptor)
-   [Creating a Job](#creating-a-job)
-   [Viewing Job Status](#viewing-job-status)
-   [Modifying a Job](#modifying-a-job)
-   [Pausing Jobs](#pausing-jobs)
-   [Resuming Jobs](#resuming-jobs)
-   [Restarting Failed Jobs](#restarting-failed-jobs)
-   [Deleting Jobs](#deleting-jobs)
-   [Storing Additional Job Properties](#storing-additional-job-properties)

## Searching for Jobs

The GET method of the jobs service has multiple arguments to search for jobs in several ways. The credentials used for authentication determine the scope of the search: an ordinary user can search all of his or her own jobs, an organization admin (`jasperadmin`) can search all jobs in his or her organization, and the system admin (`superuser`) can search all jobs on the server. This method only returns active jobs that still have a pending trigger or are still running after their last trigger.

When used without any arguments, this method returns all scheduled jobs for any scheduled report, report option, or dashboard within the scope of the user. The various arguments let you search for jobs on a specific report or dashboard, or find all jobs created by a given user (with administrator credentials). You can also do a string search on the label, or do an advanced search such as by output type or email address. If you want to handle large numbers of results, you can control the pagination and sorting order of the reply.

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
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/jobs</span>?&lt;arguments&gt;</span></p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><span>label?</span></p></td>
<td><p>string</p></td>
<td colspan="2"><p>Performs a case-insensitive string search for this value anywhere within the label property of every job.</p></td>
</tr>
<tr>
<td><p><span>owner?</span></p></td>
<td><p>string</p></td>
<td colspan="2"><p>The name of the user who scheduled the report, if necessary in the format &lt;username&gt;%7C&lt;organization&gt; (%7C is the | character).</p></td>
</tr>
<tr>
<td><p><span>reportUnitURI?</span></p></td>
<td><p><span>/path/to/report</span></p></td>
<td colspan="2"><p>Optional URI (repository path) of a report, report option, or dashboard to list all of its jobs. You may need to encode the / characters in the URI with <code>%2F</code>. When specified, the results are only for the given resource.</p></td>
</tr>
<tr>
<td><p><span>example?</span></p></td>
<td><p>JSON <code>jobModel</code></p></td>
<td colspan="2"><p>Searches for jobs that match the JSON <code>jobModel</code>, which is a fragment of a job descriptor containing one or more properties to be matched. This argument lets you search for any parameter of the job descriptor, for example the trigger, exclusion calendar, output format, recipient email, or FTP output. Because the JSON fragment appears as an argument in the URL, it must be properly URL-encoded (percent-encoded) as shown in the example below.</p></td>
</tr>
<tr>
<td><p><span>limit?</span></p></td>
<td><p>integer</p></td>
<td colspan="2"><p>Specifies the number of <code>jobsummary</code> descriptors in the results. The default is -1 for no limit and thus all results are returned. When used with the offset parameter, it can be used to implement pagination of results.</p></td>
</tr>
<tr>
<td><p><span>offset?</span></p></td>
<td><p>integer</p></td>
<td colspan="2"><p>Specifies the index of the first <code>jobsummary</code> to be returned. When used with the limit parameter, it can be used to implement pagination.</p></td>
</tr>
<tr>
<td><p><span>sortType?</span></p></td>
<td></td>
<td colspan="2"><p>Possible values are: <code>NONE</code>, <code>SORTBY_JOBID</code>, <code>SORTBY_JOBNAME</code>, <code>SORTBY_REPORTURI</code>, <code>SORTBY_REPORTNAME</code>, <code>SORTBY_REPORTFOLDER</code>, <code>SORTBY_OWNER</code>, <code>SORTBY_STATUS</code>, <code>SORTBY_LASTRUN</code>, <code>SORTBY_NEXTRUN</code></p></td>
</tr>
<tr>
<td><p><span>isAscending?</span></p></td>
<td><p>true / false</p></td>
<td colspan="2"><p>Determines the sort order: ascending if true, descending if false or omitted. This has no effect when <code>sortType</code> is not specified.</p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p><span>accept: application/xml</span></p>
<p><span>accept: application/json</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK - The body contains an array or list of <code>jobsummary</code> descriptors that match the search criteria, as shown in the examples below.</p></td>
<td><p>204 No Content - When no matching job is found in the server. After a job finishes running its last triggered instance, it no longer shows up in search results.</p></td>
</tr>
</tbody>
</table>

For example, if your application wants to request all the jobs for a given report, it would send the following URL (%2F is the / character):

``` text
GET http://example.com:8090/jasperserver-pro/rest_v2/jobs?reportUnitURI=%2Freports%2FAllAccounts
```

In the response from the server, the jobs are described in a `jobsummary` element such as the following example. The `jobsummary` contains a small subset of the properties of the job descriptor as well as the complete state descriptor:

``` yaml
JSON: {
        "jobsummary": [
          {
            "id": 1898,
            "version": 0,
            "reportUnitURI": "/reports/AllAccounts",
            "label": "SampleJobName",
            "description": "Accounts Sample Job",
            "owner": "jasperadmin|organization_1",
            "reportLabel": "Accounts Report",
            "state": {
              "previousFireTime": null,
              "nextFireTime": "2022-03-15T00:00:00+03:00",
              "value": "NORMAL"
            }
            "succeededJobsCount": 8,            "failedJobsCount": 3,           },          ...
        ]
      }

XML:  <jobs>
          <jobsummary>
              <failedJobsCount>3</failedJobsCount>
              <id>1898</id>
              <label>SampleJobName</label>
              <description>Accounts Sample Job</description>
              <reportUnitURI>/reports/AllAccounts</reportUnitURI>
              <reportLabel>Accounts Report</reportLabel>
              <state>
                  <nextFireTime>2022-03-15T00:00:00+03:00</nextFireTime>
                  <value>NORMAL</value>
              </state>
              <owner>jasperadmin|organization_1</owner>
              <version>0</version>              <succeededJobsCount>8</succeededJobsCount>           </jobsummary>
          ...
      </jobs>
```

The `example` parameter lets you specify a search of any property in the job descriptor, such as output formats. You can specify any property in the job descriptor or in any of its nested structures. Some properties may be specified in both the `example` parameter and in a dedicated parameter, for example label. In that case, the search specified in the `example` parameter takes precedence.

For example, you can search for all jobs that specify an output format of PDF. The JSON `jobModel` to specify this property is:

``` json
{"outputFormat":"PDF"}
```

And the corresponding URI with proper encoding is:

``` text
http://<host>:<port>/jasperserver[-pro]/rest_v2/jobs?example=%7b%22outputFormat%22%3a%22PDF%22%7d
```

## Viewing a Job Definition

After searching and finding the ID of a job that is still active, use the GET method with that specific job ID to retrieve its detailed information.

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
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/jobs</span>/&lt;jobID&gt;/</span></p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p><span>accept: application/job+xml</span></p>
<p><span>accept: application/job+json</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK - The body contains a descriptor with all details about the job.</p></td>
<td><p>404 Not Found - When the specified job is not found in the server. After a job finishes running its last triggered instance, it is no longer active and its ID will return this error.</p></td>
</tr>
</tbody>
</table>

The method returns a descriptor that fully describes all the aspects of a scheduled job, such as recurrence, parameters, output, email notifications, and alerts, if any. All properties are included, many of which may be null if not set for the chosen job. For more information, see [The job Descriptor](#the-job-descriptor).

JSON:

``` json
{
    "id": 1906,
    "version": 0,
    "username": "jasperadmin|organization_1",
    "label": "Daily Report",
    "description": "Sample desctiption",
    "creationDate": "2019-04-21T14:52:04.955+03:00",
    "outputFormats": {
        "outputFormat": ["XLS",
        "PDF"]
    }

    "trigger": {
        "simpleTrigger": {
            "id": 0,
            "version": 0,
            "timezone": "America/Los_Angeles",
            "calendarName": null,
            "startType": 2,
            "startDate": "2019-04-21 10:00",
            "endDate": null,
            "misfireInstruction": 0,
            "occurrenceCount": 1,
            "recurrenceInterval": 1,
            "recurrenceIntervalUnit": "DAY"
        }
    },

    "source": {
        "reportUnitURI": "/adhoc/topics/Cascading_multi_select_topic",
        "parameters": {
            "parameterValues": {
                "Country_multi_select": ["Mexico"],
                "Cascading_name_single_select": ["Chin-Lovell Engineering Associates"],
                "Cascading_state_multi_select": ["DF","Jalisco","Mexico"]
            }
        }
    },

    "alert": {
        "id": 0,
        "version": -1,
        "recipient": "OWNER_AND_ADMIN",
        "toAddresses": {
            "address": []
        },
        "jobState": "FAIL_ONLY",
        "messageText": null,
        "messageTextWhenJobFails": null,
        "subject": null,
        "includingStackTrace": true,
        "includingReportJobInfo": true
    },

    "baseOutputFilename": "Cascading_multi_select_report",
    "outputLocale": null,
    "mailNotification": null,
    "outputTimeZone": null,
    "repositoryDestination": {
        "id": 0,
        "version": -1,
        "folderURI": "/temp",
        "sequentialFilenames": false,
        "overwriteFiles": false,
        "outputDescription": null,
        "timestampPattern": null,
        "saveToRepository": true,
        "defaultReportOutputFolderURI": null,
        "usingDefaultReportOutputFolderURI": false,
        "outputLocalFolder": null,
        "outputFTPInfo": {
            "userName": "anonymous",
            "password": null,
            "folderPath": null,
            "serverName": null,
            "type": "ftps",
            "protocol": null,
            "port": 990,
            "implicit": true,
            "pbsz": 0,
            "prot": null
        }
    },
}
```

XML:

``` xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<clientJob>
    <creationDate>2019-04-21T13:38:09.759+02:00</creationDate>
    <id>5484</id>
    <label>test</label>
    <username>superuser</username>
    <version>0</version>
    <outputFormats>
        <outputFormat>PDF</outputFormat>
    </outputFormats>

    <simpleTrigger>
        <id>5482</id>
        <misfireInstruction>0</misfireInstruction>
        <startDate>2019-04-21 10:00</startDate>
        <startType>2</startType>
        <timezone>Europe/Helsinki</timezone>
        <version>0</version>
        <occurrenceCount>1</occurrenceCount>
        <recurrenceInterval>1</recurrenceInterval>
        <recurrenceIntervalUnit>DAY</recurrenceIntervalUnit>
    </simpleTrigger>

    <source>
        <parameters>
            <parameterValues>
                <entry>
                    <key>Country_multi_select</key>
<value xsi:type="collection">
    <item xsi:type="xs:string">Mexico</item>
</value>
                </entry>
                <entry>
                    <key>Cascading_name_single_select</key>
<value xsi:type="collection">
    <item xsi:type="xs:string">Chin-Lovell Engineering Associates</item>
</value>
                </entry>
                <entry>
                    <key>Cascading_state_multi_select</key>
<value xsi:type="collection">
    <item xsi:type="xs:string">DF</item>
    <item xsi:type="xs:string">Jalisco</item>
    <item xsi:type="xs:string">Mexico</item>
</value>
                </entry>
            </parameterValues>
        </parameters>
        <reportUnitURI>/organizations/organization_1/adhoc/topics/Cascading_multi_select_topic<
         /reportUnitURI>
    </source>

    <outputTimeZone>Europe/Helsinki</outputTimeZone>
    <baseOutputFilename>Cascading_multi_select_topic</baseOutputFilename>
    <repositoryDestination>
        <folderURI>/organizations/organization_1/adhoc/topics</folderURI>
        <id>5483</id>
        <outputFTPInfo>
            <implicit>true</implicit>
            <password/>
            <pbsz>0</pbsz>
            <port>21</port>
            <type>ftp</type>
            <userName>anonymous</userName>
        </outputFTPInfo>
        <overwriteFiles>true</overwriteFiles>
        <saveToRepository>true</saveToRepository>
        <sequentialFilenames>false</sequentialFilenames>
        <usingDefaultReportOutputFolderURI>false</usingDefaultReportOutputFolderURI>
        <version>-1</version>
    </repositoryDestination>
</clientJob>
```

## The job Descriptor

The `job` descriptor is a complex data object with nested containers for the various properties that define a scheduled job. The `job` descriptor is both the output of the GET method to view job details and, with slightly different content, the input of the PUT and POST methods to create and modify jobs.

The properties of the `job` descriptor are defined in the following sections:

-   [General Properties of a Job](#general-properties-of-a-job), such as label and description, but also the output formats and base filename.

-   [Source and Input Controls](#source-and-input-controls) includes the repository URL of the report, report option, or dashboard, and any input controls.

-   [Simple Trigger](#simple-trigger) defines interval-based repetition of the job for a given number of occurrences.

-   [Calendar Trigger](#calendar-trigger) runs at specific time on specific days of the week or days of the month.

-   [Job Output Properties](#job-output-properties) define the file name and locations where output files are written.

-   [FTP Output](#ftp-output) defines whether the output files are written to a remote server.

-   [Job Output Email](#job-output-email) defines the recipients for successful output files.

-   [Job Status Email](#job-status-email) defines the recipients for success or error messages.

    When submitting a `job` descriptor to create or modify a job schedule, not all properties are needed. In the following tables, each property is one of the following:

-   Required - This property must have a value for input to define a valid job.

-   Optional - This property may be omitted on input, either because it is nullable, or because the server assigns a default value. The behavior is explained in the property description.

-   Conditional - The property may be required or optional depending on other property values. The behavior is explained in the property description.

-   Ignored - This property is for internal usage or output only, and the server ignores any value on input. Good practice is to omit these properties from your input.

### General Properties of a Job

A valid `job` descriptor contains the following properties:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Property (as input)</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>creationDate</code><br />
(ignored)</p></td>
<td><p>The time and date that the job was first created, managed internally by the server.</p></td>
</tr>
<tr>
<td><p><code>id</code> (ignored)</p></td>
<td><p>The ID of the job assigned by the server. Use this ID to read, modify, or delete the job.</p></td>
</tr>
<tr>
<td><p><code>version</code> (ignored)</p></td>
<td><p>An internal version number that has no outside use.</p></td>
</tr>
<tr>
<td><p><code>username</code><br />
(ignored)</p></td>
<td><p>The owner and creator of this job, including the organization name. Note that only administrators can view other users' jobs.</p></td>
</tr>
<tr>
<td><p><code>label</code><br />
(required)</p></td>
<td><p>A name for the job, like the label of a resource in the repository.</p></td>
</tr>
<tr>
<td><p><code>description</code><br />
(optional)</p></td>
<td><p>A description string for the job, which often describes the trigger and chosen output.</p></td>
</tr>
<tr>
<td><p><code>exportType</code><br />
(optional)</p></td>
<td><p>The default value is <code>DEFAULT</code>, and for scheduling a report no other value is accepted. In a schedule for a dashboard, <code>DEFAULT</code> indicates that the output will be a screenshot in the chosen format, for example an image in a Word file. When this is set to <code>DASHBOARD_DETAILED</code> for a dashboard schedule, the dashlets are exported as individual reports sequentially into the same file. Not all output formats are available depending on the value of <code>exportType</code> (see next property).</p></td>
</tr>
<tr>
<td><p><code>outputFormats</code><br />
<code>outputFormat</code><br />
(required)</p></td>
<td><p>Contains a list of output formats, each to be generated in a separate output file when the job is triggered. The possible values depend on the resource and the <code>exportType</code> above:</p>
<ul>
<li>Report (<code>exportType="DEFAULT"</code> is required): <code>CSV, DATA_CSV, DOCX, HTML, ODS, ODT, PDF, PPTX, RTF, XLSX, XLSX_NOPAG, DATA_XLSX</code></li>
<li>Dashboard with <code>exportType="DEFAULT"</code>: <code>DOCX, ODT, PDF, PNG, PPTX</code></li>
<li>Dashboard with <code>exportType="DASHBOARD_DETAILED"</code>: <code>CSV, DOCX, ODS, ODT, PDF, PPTX, RTF, XLSX</code></li>
</ul>
<p>The XLS and XLS_NOPAG (Excel 2003) output formats are deprecated. You can use XLSX and XLSX_NOPAG (Excel 2016) instead. Older jobs that are still running a request for XLS or XLS_NOPAG outputs, generate output in the XLSX or XLSX_NOPAG format.</p></td>
</tr>
<tr>
<td><p><code>outputTimeZone</code><br />
(optional)</p></td>
<td><p>The time zone to use when running the report or dashboard, for example "America/Los_Angeles". By default, the scheduler runs the report or dashboard using the server's default time zone. The time zone names are those supported by <code>java.time.ZoneID</code>, which are defined in the <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones">tz database</a>.</p>
<p>The trigger time zone and the output time zone have different purposes, even if they are often set to the same value. The trigger time zone determines when the job will run, whereas the output time zone affects anytime or date calculations in the report or dashboard. The time zone specified in a data source also affects times and dates in the output.</p></td>
</tr>
<tr>
<td><p><code>outputLocale</code><br />
(optional)</p></td>
<td><p>The locale to use when running the report or dashboard, if it is based on a domain with locales defined. By default, the scheduler runs the report or dashboard using the server's default locale. If the report or dashboard is not based on a domain with locales, this value has no effect. Use a Java locale string that is also defined in your domain, for example <code>fr</code> (French) or <code>fr_CA</code> (French from Canada).</p></td>
</tr>
<tr>
<td><p><code>baseOutput Filename</code><br />
(required)</p></td>
<td><p>The basename of the file for the generated report output. Each output format appends its corresponding file extension to this name. This name may also have a time stamp appended as specified in <a href="#job-output-properties">Job Output Properties</a>. This final output name is then used in all locations where the file is saved: repository, file system, FTP, and email attachment.</p></td>
</tr>
<tr>
<td><p><code>source</code><br />
(required)</p></td>
<td><p>A container for the properties that define the repository URI of the report, report option, or dashboard and its input controls. See <a href="#source-and-input-controls">Source and Input Controls</a>.</p></td>
</tr>
<tr>
<td><p><code>trigger</code><br />
(required)</p></td>
<td><p>A container for one of the triggers specified in <a href="#simple-trigger">Simple Trigger</a> or <a href="#calendar-trigger">Calendar Trigger</a>. The trigger determines how often the job runs and the date and time at which it runs.</p></td>
</tr>
<tr>
<td><p><code>repository Destination</code><br />
(optional)</p></td>
<td><p>A container for properties that define the folders and filenames for the output files that are generated each time a scheduled job runs successfully. Its properties are defined in <a href="#job-output-properties">Job Output Properties</a> and the optional <a href="#ftp-output">FTP Output</a>.</p></td>
</tr>
<tr>
<td><p><code>mailNotification</code><br />
(optional)</p></td>
<td><p>A container for properties that define email recipients when a job runs successfully. You can customize the contents of the email and whether the report output files are sent as attachments or links. For more information, see <a href="#job-output-email">Job Output Email</a>.</p></td>
</tr>
<tr>
<td><p><code>alert</code><br />
(optional)</p></td>
<td><p>A container for properties that define email recipients for job success and errors. For more information, see <a href="#job-status-email">Job Status Email</a>.</p></td>
</tr>
<tr>
<td>succeededJobsCount<br />
(ignored)</td>
<td>The total number of successful executions for the scheduled job.</td>
</tr>
<tr>
<td>failedJobsCount<br />
(ignored)</td>
<td>The total number of failed executions for the scheduled job.</td>
</tr>
</tbody>
</table>

### Source and Input Controls

The source is the report, report option, or dashboard being scheduled by the job, along with any required input controls.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Property (as input)</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>source</code><br />
(required)</p></td>
<td><p>A container for the following properties.</p></td>
</tr>
<tr>
<td><p><code>reportUnitURI</code><br />
(required)</p></td>
<td><p>A mandatory property that defines the repository URI of the report, report option, or dashboard to run for this job. The repository URI is relative to the scope of the user credentials used to authenticate the REST call.</p></td>
</tr>
<tr>
<td><p><code>referenceHeight</code><br />
(optional)</p></td>
<td rowspan="2"><p>When scheduling a dashboard, the default output is a screenshot and these properties specify the dimensions in pixels of the dashboard canvas. The images in the output have these dimensions, even inside another format such as PDF. The default size is 1280 width by 800 height.</p></td>
</tr>
<tr>
<td><p><code>referenceWidth</code><br />
(optional)</p></td>
</tr>
<tr>
<td><p><code>parameters parameterValues</code><br />
(conditional)</p></td>
<td><p>A container for the input controls (filters) for this job. Every required input control in the report or dashboard must have an XML <code>entry</code> or JSON list item within <code>parameterValues</code>. If there are no input controls, this property can be omitted. See the examples in <a href="#creating-a-job">Creating a Job</a> for the syntax of these properties in JSON and XML.</p></td>
</tr>
</tbody>
</table>

### Simple Trigger

The following properties define the recurrence pattern for a simple trigger.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Property (as input)</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>simpleTrigger</code><br />
(conditional)</p></td>
<td><p>A container for the following properties, itself contained in a required <code>trigger</code>. For input, you must specify either the <code>simpleTrigger</code> or the <code>calendarTrigger</code>.</p></td>
</tr>
<tr>
<td><p><code>id</code> (ignored)</p></td>
<td><p>An internal ID of the simple trigger that has no outside use.</p></td>
</tr>
<tr>
<td><p><code>version</code> (ignored)</p></td>
<td><p>An internal version number that has no outside use.</p></td>
</tr>
<tr>
<td><p><code>timezone</code><br />
(optional)</p></td>
<td><p>The timezone for all dates and times used by the trigger, for example <code>"America/Los_Angeles"</code>. By default, the trigger uses the same time zone as the server. The time zone names are those supported by <code>java.time.ZoneID</code>, which are defined in the <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones">tz database</a>.</p></td>
</tr>
<tr>
<td><p><code>startType</code><br />
(optional)</p></td>
<td><p>Determines when the job becomes active and sets the base time at which recurrence starts. Supported values:</p>
<p><code>START_TYPE_NOW</code> - The job starts immediately, and the trigger fires right away. This is the default value when this property is omitted.</p>
<p><code>START_TYPE_SCHEDULE</code> - The job starts at the <code>startDate</code>, at which time it fires.</p></td>
</tr>
<tr>
<td><p><code>startDate</code><br />
(conditional)</p></td>
<td><p>The date and time at which the job will start, required when <code>startType=START_TYPE_SCHEDULE</code>. The simple trigger fires at this time, and it begins its recurrence at this time. The format is "yyyy-MM-dd HH:mm" and the timezone property is applied.</p></td>
</tr>
<tr>
<td><p><code>endDate</code><br />
(optional)</p></td>
<td><p>The date and time at which the job will stop. The trigger will not fire after this time, even if any occurrences remain, unless a misfire occurs and the misfire policy allows it. The format is "yyyy-MM-dd HH:mm" and the timezone property is applied.</p></td>
</tr>
<tr>
<td><p><code>occurrenceCount</code><br />
(required)</p></td>
<td><p>An integer that defines how many times the trigger fires, provided the recurrence intervals happen before the <code>endDate</code>.</p></td>
</tr>
<tr>
<td><p><code>recurrence Interval</code><br />
(required)</p></td>
<td><p>The time interval between firings of the trigger, with the interval unit provided in the next property.</p></td>
</tr>
<tr>
<td><p><code>recurrence IntervalUnit</code><br />
(required)</p></td>
<td><p>The unit of time for the recurrence interval. Supported values: <code>MINUTE</code>, <code>HOUR</code>, <code>DAY</code>, or <code>WEEK</code>. For units greater than <code>MINUTE</code>, the <code>startType</code> and <code>startDate</code> determine the basis for recurrence. For example, if the trigger fires immediately and recurs every 2 days, then it fires at the current time on the subsequent days.</p></td>
</tr>
<tr>
<td><p><code>calendarName</code><br />
(optional)</p></td>
<td><p>The name of a previously defined exclusion calendar. An exclusion calendar defines a set of dates or times when the job does not run, for example a list of holidays. You can update the exclusion calendar without changing the job. For information about creating and modifying exclusion calendars, see <a href="jobscalendars.md">The calendars Service</a>.</p></td>
</tr>
<tr>
<td><p><code>misfire Instruction</code><br />
(optional)</p></td>
<td><p>An integer value that defines the behavior if the trigger did not fire when scheduled. The values of <code>misfireInstruction</code> are described in the next table. A misfire occurs if JasperReports Server or its Quartz scheduler component is offline when a trigger was supposed to happen and run a job. It can also occur if all threads of the scheduler are busy and the job cannot run when the trigger should fire. When the scheduler restarts or a thread becomes available again, it checks for any triggers that did not fire on time and takes action based on the <code>misfireInstruction</code>. The misfire instruction does not apply if the trigger fires normally but the report encounters an error. The default value is 0 when this property is omitted.</p></td>
</tr>
</tbody>
</table>

Choose a misfire policy based on how frequently your job runs and how critical it is. For example, an outage may last one to two hours, and if a daily report is critical, you may want it to run as soon as the scheduler is able. However, if a report runs every hour, you may want to ignore missed reports and wait for the next report at the scheduled time. Note that different policies may have the same effect depending on how the trigger is defined, but also the same policy may have different effects on different trigger types.

| misfireInstruction | Description for Simple Triggers |
|----|----|
| 0 (default) | No instruction (same behavior as option -1 below). Does not trigger the job that misfired, and takes no action. Because the trigger did not fire, the number of occurrences is not decremented. This is the default behavior if no `misfireInstruction` is defined. The trigger will fire the next time according to the recurrence value and unit, as if the misfire had fired at the proper time. |
| -1 | Ignore misfire policy. Instructs the scheduler that the trigger will never be evaluated for a misfire situation, and that the scheduler will simply try to fire it as soon as it can, and then update the trigger as if it had fired at the proper time. This value has the same effect as 0: take no action and do not change the number of occurrences. |
| -999 | Called the smart policy. Instructs the scheduler that on a misfire situation, the custom `updateAfterMisfire` method is called on the trigger to determine the misfire action. In this case, you must define and enable a custom trigger class on the server(this is beyond the scope of this documentation). |
| 1 | Run now: Instructs the scheduler to trigger now, which is the time the misfire is detected. If the outage covers several trigger times, they will each have a misfire, and with this value, they will each run now. |
| 2 | Instructs the scheduler that on a misfire situation, the SimpleTrigger is rescheduled to 'now' (even if the associated calendar excludes 'now') with the repeat count left as-is. This does obey the trigger end-time, so if 'now' is after the end-time, the trigger will not fire. |
| 3 | Instructs the scheduler that on a misfire situation, the SimpleTrigger is rescheduled to 'now' (even if the associated Calendar excludes 'now') with the repeat count set to what it would be, if it had not missed any firings. This does obey the trigger end-time, so if 'now' is after the end-time the trigger will not fire. |
| 4 | Ignores any missed firing of the trigger (no action is taken for the missed firing), but the repeat count is set to what it would be if the trigger had fired normally. The trigger will fire at the next scheduled time after the current time, taking into account any associated exclusion calendar or end time. The effect is that missed trigger occurrences will be skipped. |
| 5 | Ignores any missed firing of the trigger (no action is taken for the missed firing), but the repeat count is left unchanged. The trigger will fire at the next scheduled time after the current time, taking into account any associated exclusion calendar or end time. The effect is that missed trigger occurrences happen later, past the last expected occurrence. |

### Calendar Trigger

A calendar trigger lets you schedule a job to run multiple times based on any combination of time and date. Its properties let you define single values, ranges, or wild-cards for minutes, hours, days, weeks, or months. For example, you can run a report every 15 minutes from 10 AM to noon every Monday.

The following properties define the recurrence pattern of a calendar trigger:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Property (as input)</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>calendarTrigger</code><br />
(conditional)</p></td>
<td><p>A container for the following properties, itself contained in a required <code>trigger</code>. For input, you must specify either the <code>simpleTrigger</code> or the <code>calendarTrigger</code>.</p></td>
</tr>
<tr>
<td><p><code>id</code> (ignored)</p></td>
<td><p>An internal ID of the calendar trigger that has no outside use.</p></td>
</tr>
<tr>
<td><p><code>version</code> (ignored)</p></td>
<td><p>An internal version number that has no outside use.</p></td>
</tr>
<tr>
<td><p><code>timezone</code><br />
(optional)</p></td>
<td><p>The timezone for all dates and times used by the trigger, for example <code>"America/Los_Angeles"</code>. By default, the trigger uses the same time zone as the server. The time zone names are those supported by <code>java.time.ZoneID</code>, which are defined in the <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones">tz database</a>.</p></td>
</tr>
<tr>
<td><p><code>startType</code><br />
(optional)</p></td>
<td><p>Determines when the job becomes active. Supported values:</p>
<p><code>START_TYPE_NOW</code> - The job starts immediately, and the trigger may fire right away. This is the default value when this property is omitted.</p>
<p><code>START_TYPE_SCHEDULE</code> - The trigger will not fire until the specified <code>startDate</code>.</p></td>
</tr>
<tr>
<td><p><code>startDate</code><br />
(conditional)</p></td>
<td><p>The date and time at which the job will be active, required when <code>startType=START_TYPE_SCHEDULE</code>. The trigger will not fire before this time; it will only fire for calendar occurrences that happen after this time. The format is "yyyy-MM-dd HH:mm" and the timezone property is applied.</p></td>
</tr>
<tr>
<td><p><code>endDate</code><br />
(optional)</p></td>
<td><p>The date and time at which the job will stop. The trigger will not fire after this time, unless a misfire occurs and the misfire policy allows it. The format is "yyyy-MM-dd HH:mm" and the timezone property is applied.</p></td>
</tr>
<tr>
<td><p><code>calendarName</code><br />
(optional)</p></td>
<td><p>The name of a previously defined exclusion calendar. An exclusion calendar defines a set of dates or times when the job will not run, for example a list of holidays. You can update the exclusion calendar without changing the job. For information about creating and modifying exclusion calendars, see <a href="jobscalendars.md">The calendars Service</a>.</p></td>
</tr>
<tr>
<td><p><code>minutes</code><br />
(required)</p></td>
<td><p>Specifies the minute or minutes at which the trigger fires on a given hour. The value can consist of the following tokens:</p>
<ul>
<li>A single minute value between 0 and 59.</li>
<li>A range of minutes, for example 0-10 means the trigger fires every minute starting from HH:00 to HH:10. Minute values and ranges can be concatenated using commas as separators.</li>
<li>A minute value with an increment, for example 5/10 means that the trigger fires every 10 minutes starting from HH:05.</li>
<li><code>*</code> means the trigger fires every minute of the hour.</li>
</ul></td>
</tr>
<tr>
<td><p><code>hours</code><br />
(required)</p></td>
<td><p>Specifies the hour or hours during which the trigger fires on a given day. The minutes property determines when during the hour that the trigger fires, possibly multiple times. All hours are specified in the 24-hour format. The value can consist of the following tokens:</p>
<ul>
<li>A single hour value between 0 and 23.</li>
<li>A range of hours, for example 8-16 means the trigger fires every hour from 8 AM to 4 PM. Hour values and ranges can be concatenated using commas as separators.</li>
<li>An hour value with an increment, for example, 10/2 means the trigger fires during the hour every 2 hours starting from 10 AM.</li>
<li><code>*</code> means the trigger fires during every hour.</li>
</ul></td>
</tr>
<tr>
<td><p><code>months</code><br />
(required)</p></td>
<td><p>A list of <code>month</code> values during which the trigger fires. Can be used in addition to <code>weekDays</code> or <code>monthDays</code> below to suppress the trigger during certain months. The month values are 1 for January and 12 for December. In JSON, it has the following syntax:</p>
<div class="language-text highlight"><pre><code>&quot;months&quot;: {
    &quot;month&quot;: [&quot;3&quot;, &quot;6&quot;, &quot;9&quot;, &quot;12&quot;]
}</code></pre></div></td>
</tr>
<tr>
<td><p><code>daysType</code><br />
(required)</p></td>
<td><p>Determines how the trigger days are defined:</p>
<ul>
<li><code>WEEK</code> means the trigger fires on a weekly pattern defined in the <code>weekDays</code> below.</li>
<li><code>MONTH</code> means the trigger fires on a monthly pattern defined in the <code>monthDays</code> below.</li>
<li><code>ALL</code> means the trigger fires every single day at the time or times defined by the <code>hours</code> and <code>minutes</code> properties.</li>
</ul></td>
</tr>
<tr>
<td><p><code>weekDays</code><br />
(conditional)</p></td>
<td><p>Specifies a list of days of the week on which the trigger fires, to be repeated every week. This is required if <code>daysType=WEEK</code>, and ignored otherwise. The day values are 1 for Sunday and 7 for Saturday. On the designated days, the trigger fires at the time or times defined by the <code>hours</code> and <code>minutes</code> properties. In JSON, it has the following syntax:</p>
<div class="language-text highlight"><pre><code>&quot;weekDays&quot;: {
    &quot;day&quot;: [&quot;1&quot;, &quot;4&quot;, &quot;6&quot;]
}</code></pre></div></td>
</tr>
<tr>
<td><p><code>monthDays</code><br />
(conditional)</p></td>
<td><p>Specifies the days of the month on which the trigger fires, to be repeated every month. This is required if <code>daysType=MONTH</code>, and ignored otherwise. On the designated days, the trigger fires at the time or times defined by the <code>hours</code> and <code>minutes</code> properties. The value can consist of the following tokens:</p>
<ul>
<li>A single day value between 1 and 31.</li>
<li>A range of days, for example 2-5 means the trigger fires during each day starting from the 2nd to the 5th of the month. Day values and ranges can be concatenated using commas as separators, for example <code>"1,3,5-22"</code>.</li>
<li>A day value with an increment, for example 1/5 means the trigger fires every 5 days starting on the 1st of the month.</li>
<li><code>*</code> means the trigger fires during every day.</li>
</ul></td>
</tr>
<tr>
<td><p><code>misfire Instruction</code><br />
(optional)</p></td>
<td><p>An integer value that defines the behavior if the trigger did not fire when scheduled. The values of <code>misfireInstruction</code> are described in the next table. A misfire occurs if JasperReports Server or its Quartz scheduler component is offline when a trigger was supposed to happen and run a job. It can also occur if all threads of the scheduler are busy and the job cannot run when the trigger should fire. When the scheduler restarts or a thread becomes available again, it checks for any triggers that did not fire on time and takes action based on the <code>misfireInstruction</code>. The misfire instruction does not apply if the trigger fires normally but the report encounters an error. The default value is 0 when this property is omitted.</p></td>
</tr>
</tbody>
</table>

For example, the following calendar trigger should run at 3:30 AM every Monday in every month.

``` text
"trigger": {
    "calendarTrigger": {
        "timezone": "America/Denver",
        "startType": 2,
        "startDate": "2022-02-22 00:00",
        "misfireInstruction": 0,
        "minutes": "30",
        "hours": "3",
        "daysType": "WEEK",
        "weekDays": {
            "day": ["2"]
        },
        "months": {
            "month": ["1","2","3","4","5","6","7","8","9","10","11","12"]
        }
    }
}
```

Choose a misfire policy based on how frequently your job runs and how critical it is. For example, an outage may last one to two hours, and if a daily report is critical, you may want it to run as soon as the scheduler is able. However, if a report runs every hour, you may want to ignore missed reports and wait for the next scheduled time. Note that different policies may have the same effect depending on how the trigger is defined, but also the same policy may have different effects on different trigger types.

| misfireInstruction | Description for Calendar Triggers |
|----|----|
| 0 (default) | No instruction (same behavior as option -1 below). Does not trigger the job that misfired, and takes no action. This is the default behavior if no `misfireInstruction` is defined. The trigger will fire the next time according to the times and days that were defined. |
| -1 | Ignore misfire policy. Instructs the scheduler that the trigger will never be evaluated for a misfire situation, and that the scheduler will simply try to fire it as soon as it can, and then update the trigger as if it had fired at the proper time. This value has the same effect as 0: take no action and wait for the next calendar trigger. |
| -999 | Called the smart policy. Instructs the scheduler that on a misfire situation, the custom `updateAfterMisfire` method is called on the trigger to determine the misfire action. In this case, you must define and enable a custom trigger class on the server (this is beyond the scope of this documentation). |
| 1 | Run now: instructs the scheduler to trigger now, which is the time the misfire is detected. If the outage covers several trigger times, they will each have a misfire, and with this value, they will each run now. |
| 2 | Ignores any missed firings of the trigger (no action is taken for the missed firing), but updates the trigger to fire at the next scheduled time after now, taking into account any associated exclusion calendar or end time. The effect is that missed trigger occurrences will be skipped. |

### Job Output Properties

The output properties define the folders and filenames for the output files that are generated each time a scheduled job runs successfully.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Property (as input)</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>repository Destination</code><br />
(optional)</p></td>
<td><p>A container for the following properties.</p></td>
</tr>
<tr>
<td><p><code>id</code> (ignored)</p></td>
<td><p>An internal ID of the repository destination that has no outside purpose.</p></td>
</tr>
<tr>
<td><p><code>version</code> (ignored)</p></td>
<td><p>An internal version number that has no outside purpose.</p></td>
</tr>
<tr>
<td><p><code>saveToRepository</code><br />
(optional)</p></td>
<td><p>A boolean that determines whether the output is written as file resources in the repository. The default value is true. Use the next two parameters to specify the location of the files. When false, no output is written to the repository, local file system, or remote FTP, and the output files are sent only by email if configured.</p></td>
</tr>
<tr>
<td><p><code>UsingDefaultReport OutputFolderURI</code><br />
(optional)</p></td>
<td><p>A boolean that determines if the output is written to the default folder: /public/Samples/Reports or /public/Samples/Dashboards (these folders can be configured as described in the <span>JasperReports Server Administrator Guide</span>). By default, this is false and you must specify the <code>folderURI</code>.</p></td>
</tr>
<tr>
<td><p><code>folderURI</code><br />
(conditional)</p></td>
<td><p>Defines a folder in the repository where the output file resources will be saved. This repository URI is relative to the scope of the user who authenticates the REST call. This property is required if you do not use the default output folder above.</p></td>
</tr>
<tr>
<td><p><code>outputDescription</code><br />
(optional)</p></td>
<td><p>A string that becomes the description of the output file resources in the repository.</p></td>
</tr>
<tr>
<td><p><code>sequential Filenames</code><br />
(optional)</p></td>
<td><p>A boolean that indicates whether output files have the time stamp pattern in the next parameter appended to the base filename. The default value is false.</p></td>
</tr>
<tr>
<td><p><code>timestampPattern</code><br />
(conditional)</p></td>
<td><p>A string containing "yyyyMMddHHmm" tokens to append a timestamp to the base filename. This takes effect if <code>sequentialFilenames</code> is true. For example, an hourly trigger might use "yyyyMMdd-HHmm" but a daily trigger only "yyyy-MM-dd". Characters in the pattern must be valid in file names where the output is being written (repository, local file system, or remote FTP). There is an implicit "-" (dash) character added between the base file name and the pattern, for example, the pattern "MM-dd" becomes basename-02-14.pdf.</p></td>
</tr>
<tr>
<td><p><code>overwriteFiles</code><br />
(optional)</p></td>
<td><p>A boolean to determine the behavior when a newly generated output file has the same name as a previous one. When true, the new file overwrites the old one. When false, the old file is not overwritten and the new file is not stored, though it is sent by email if configured. The default value is true. Use the <code>sequentialFilenames</code> and <code>timestampPattern</code> to create unique file names if you wish to store every generated output.</p></td>
</tr>
<tr>
<td><p><code>outputLocalFolder</code><br />
(optional)</p></td>
<td><p>Specifies a path in the local file system (of the JasperReports Server host) for writing output files. The user running the server process must have write permission in that location. When specified, file system output is always in addition to repository output, and the output is written to both the repository and the local folder.</p>
<p>Before setting this property, the server must be configured to allow it. In the file <span>.../WEB-INF/applicationContext.xml</span>, you must set the <code>enableSaveToHostFS</code> property to <code>true</code>. However, this setting also enables file system output from the scheduler user interface for all users, which could be a security risk.</p>
<p>The file names to be written are the same as for the repository, therefore the <code>baseOutputFilename</code> and sequential pattern must be valid on the host file system. The file overwrite and sequential filename behavior also apply to file system output.</p></td>
</tr>
<tr>
<td><p><code>outputFTPInfo</code><br />
(optional)</p></td>
<td><p>Contains parameters for writing output files to a remote FTP location. For more information, see <a href="#ftp-output">FTP Output</a>.</p></td>
</tr>
</tbody>
</table>

### FTP Output

You have the option to specify output to a remote server through FTP (File Transfer Protocol). When specified, FTP output is always in addition to repository output, and the output is written to both the repository and the FTP location. The file names to be written are the same as for the repository, therefore the `baseOutputFilename` and sequential pattern must be valid on the FTP file system. The file overwrite and sequential filename behavior also apply to FTP output.

Specify the FTP server, authentication, remote path, and other FTP settings in the following properties:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Property (as input)</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>outputFTPInfo</code><br />
(optional)</p></td>
<td><p>A container for the following properties, itself contained in <code>repositoryDestination</code>.</p></td>
</tr>
<tr>
<td><p><code>type</code><br />
(optional)</p></td>
<td><p>Type of FTP connection requested: <code>ftp</code> (default), <code>ftps</code>, or <code>sftp</code>.</p></td>
</tr>
<tr>
<td><p><code>serverName</code><br />
(optional)</p></td>
<td><p>The domain and host name of the FTP server, for example "ftp.example.com".</p></td>
</tr>
<tr>
<td><p><code>port</code><br />
(optional)</p></td>
<td><p>Integer value that specifies the port number of the FTP server. The default value depends on the connection type: <code>ftp</code> = 21, <code>ftps</code> = 990, and <code>sftp</code> = 22.</p></td>
</tr>
<tr>
<td><p><code>userName</code><br />
(conditional)</p></td>
<td><p>The login user name for the FTP server.</p></td>
</tr>
<tr>
<td><p><code>password</code><br />
(conditional)</p></td>
<td><p>The login password for the given userName on the FTP server.</p></td>
</tr>
<tr>
<td><p><code>folderPath</code><br />
(conditional)</p></td>
<td><p>The path of the folder where the job output resources should be created.</p></td>
</tr>
<tr>
<td><p><code>implicit</code><br />
(optional)</p></td>
<td><p>Specifies the security mode for FTPS, Implicit if true (default) or Explicit if false. If implicit is true, the default port is set to 990.</p></td>
</tr>
<tr>
<td><p><code>protocol</code><br />
(optional)</p></td>
<td><p>Specifies the secure socket protocol to be used, for example SSL or TLS.</p></td>
</tr>
<tr>
<td><p><code>prot</code><br />
(optional)</p></td>
<td><p>Specifies the PROT command for FTP. Supported values:</p>
<ul>
<li>C - Clear</li>
<li>S - Safe (SSL protocol only)</li>
<li>E - Confidential (SSL protocol only)</li>
<li>P - Private</li>
</ul></td>
</tr>
<tr>
<td><p><code>pbsz</code><br />
(optional)</p></td>
<td><p>Specifies the protection buffer size: a decimal integer from 0 to (2^32)-1. The default is 0.</p></td>
</tr>
<tr>
<td><p><code>sshKey</code><br />
(conditional)</p></td>
<td><p>When using SFTP authentication, store the SSH key file in the repository and specify its repository URI in this property. For more information about secure files in the repository, see the <span>JasperReports Server Administrator Guide</span>.</p></td>
</tr>
<tr>
<td><p><code>sshPassphrase</code><br />
(conditional)</p></td>
<td><p>When using SFTP authentication, specify the passphrase for the SSH private key file stored in the repository.</p></td>
</tr>
</tbody>
</table>

The following example shows a simple use of `outputFTPInfo` in XML:

``` xml
<job>
    <reportUnitURI>/reports/samples/AllAccounts</reportUnitURI>
    <label>MyJob</label>
    <description>MyJob description</description>
    <baseOutputFilename>WeeklyAccountsReport</baseOutputFilename>
    <repositoryDestination>
        <folderURI>/reports/samples</folderURI>
        <overwriteFiles>true</overwriteFiles>
        <sequentialFilenames>false</sequentialFilenames>
        <outputFTPInfo>
            <serverName>ftpserver.example.com</serverName>
            <userName>ftpUser</userName>
            <password>ftpPassword</password>
            <folderPath>/shared/users/ftpUser</scheduledOutput>
        </outputFTPInfo>
    </repositoryDestination>
    <outputFormats>
        <outputFormat>XLS</outputFormat>
        <outputFormat>PDF</outputFormat>
    </outputFormats>
  ...
</job>
```

### Job Output Email

When a job runs successfully, the properties in `mailNotification` specify email recipients for the report output files. You can specify subject and body content, and you can choose to send output as attachments or links. When a job fails, no report output is sent but you have the option to configure an error message in [Job Status Email](#job-status-email).

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Property (as input)</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>mailNotification</code><br />
(optional)</p></td>
<td><p>This container and the following properties are optional. When omitted, the report output is not sent by email.</p></td>
</tr>
<tr>
<td><p><code>id</code> (ignored)</p></td>
<td><p>An internal ID of the <code>mailNotification</code> container that has no outside purpose.</p></td>
</tr>
<tr>
<td><p><code>version</code> (ignored)</p></td>
<td><p>An internal version number that has no outside purpose.</p></td>
</tr>
<tr>
<td><p><code>toAddresses</code><br />
(required)</p></td>
<td><p>A list of addresses to which job output emails are sent. This property is required if you are sending an output email.</p></td>
</tr>
<tr>
<td><p><code>ccAddresses</code><br />
(optional)</p></td>
<td><p>A list of addresses to which job output emails are CC'd.</p></td>
</tr>
<tr>
<td><p><code>bccAddresses</code><br />
(optional)</p></td>
<td><p>A list of addresses to which job output emails are BCC'd.</p></td>
</tr>
<tr>
<td><p><code>subject</code><br />
(optional)</p></td>
<td><p>A string that is used as a subject line for all output emails from this job.</p></td>
</tr>
<tr>
<td><p><code>messageText</code><br />
(optional)</p></td>
<td><p>A string that is used in the body of output emails for this job, unless HTML output is selected for the email body below.</p></td>
</tr>
<tr>
<td><p><code>resultSendType</code><br />
(required)</p></td>
<td><p>Determines whether output files are attached to the notification email. Each value has a different behavior and you must set this property based on your other properties:</p>
<p><code>SEND</code> - The links to the report output in the repository are appended to the message body, and no files are attached. This option is valid only if <code>saveToRepository</code> is set to true in the job descriptor.</p>
<p><code>SEND_ATTACHMENT</code> - The output files are sent as individual attachments to the email.</p>
<p><code>SEND_EMBED</code> - The HTML output is embedded in the email body, and any other output files are sent as individual attachments. This option is valid only if HTML output is specified in <code>outputFormats</code> for a report.</p>
<p><code>SEND_ATTACHMENT_ZIP_ALL</code> - The output files are sent as a single zipped attachment to the email.</p>
<p><code>SEND_EMBED_ZIP_ALL_OTHERS</code> - The HTML output is embedded in the email body, and any other output files are sent as a single zipped attachment. This option is valid only if HTML output is specified in <code>outputFormats</code> for a report.</p></td>
</tr>
<tr>
<td><p><code>skipEmptyReports</code><br />
(optional)</p></td>
<td><p>A boolean that suppresses the output email when the report is empty (successful completion but no content).</p></td>
</tr>
<tr>
<td><p><code>skipNotification WhenJobFails</code><br />
(ignored)</p></td>
<td rowspan="2"><p>Two legacy properties that do not affect email notification. Use the properties in the <code>alert</code> container below to specify failure notifications.</p></td>
</tr>
<tr>
<td><p><code>includingStack TraceWhenJobFails</code><br />
(ignored)</p></td>
</tr>
</tbody>
</table>

### Job Status Email

The second type of notifications is job success and failure emails specified in the `alert` container. These messages indicate whether the job ran successfully or not, and contain an error message in case of failure. They do not include the report output in case of success.

Regardless of any settings here, the scheduler sends completion status to the job owner and the administrators of the same organization on each job trigger, assuming those users have email addresses defined in their profiles. You can change this behavior, as described in the configuration chapter of the JasperReports Server Administrator Guide. The scheduler also sends a server message in case of job failure (visible to administrators in **View &gt; Messages**).

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Property (as input)</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>alert</code><br />
(optional)</p></td>
<td><p>This container and the following properties are optional. When omitted, the server sends only the default notifications listed above.</p></td>
</tr>
<tr>
<td><p><code>id</code> (ignored)</p></td>
<td><p>An internal ID of the <code>alert</code> container that has no outside purpose.</p></td>
</tr>
<tr>
<td><p><code>version</code> (ignored)</p></td>
<td><p>An internal version number that has no outside purpose.</p></td>
</tr>
<tr>
<td><p><code>jobState</code><br />
(required)</p></td>
<td><p>Selects which job status events trigger an email notification: <code>ALL</code>, <code>FAIL_ONLY</code>, <code>SUCCESS_ONLY</code>, or <code>NONE</code>. This property is required if you are sending a status email, however <code>NONE</code> is the same as not specifying an <code>alert</code>.</p></td>
</tr>
<tr>
<td><p><code>toAddresses</code><br />
(required)</p></td>
<td><p>A list of addresses to which job status emails are sent. This property is required if you are sending a status email.</p></td>
</tr>
<tr>
<td><p><code>subject</code><br />
(optional)</p></td>
<td><p>A string that is used as a subject line for all status email from this job.</p></td>
</tr>
<tr>
<td><p><code>messageText</code><br />
(optional)</p></td>
<td><p>A string that is used in the body of an email for a successful job completion.</p></td>
</tr>
<tr>
<td><p><code>messageTextWhen JobFails</code> (optional)</p></td>
<td><p>A string that is used in the body of an email when the job fails. Additional information can be added to failure notifications with the following two properties.</p></td>
</tr>
<tr>
<td><p><code>includingReport JobInfo</code> (optional)</p></td>
<td><p>Appends the job info (label and id) to the email body.</p></td>
</tr>
<tr>
<td><p><code>includingStack Trace</code> (optional)</p></td>
<td><p>In the case of a job failure, appends the stack trace to the email body. This includes the exception that caused the report to fail.</p></td>
</tr>
</tbody>
</table>

## Creating a Job

Contrary to REST conventions, the jobs service uses the PUT method to create a job and the POST method to modify a job. To schedule a report, report option, or dashboard, specify its properties in a `job` descriptor and use the PUT method of the jobs service. Specify the repository path to the resource being scheduled inside the job descriptor.

The user who is authenticated when making this request become the owner of the job that is created. This affects who can view the job and who receives notifications.

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
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/jobs</span>/</span></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/job+xml</span></p>
<p><span>application/job+json</span></p></td>
<td colspan="2"><p>A well-formed XML or JSON <code>job</code> descriptor as described in <a href="#the-job-descriptor">The job Descriptor</a>. You need to only specify the relevant properties in the job descriptor. Do not include any null properties.</p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p><span>accept: application/job+xml</span></p>
<p><span>accept: application/job+json</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>201 Created - The body contains the job descriptor of the newly created job. It is similar to the one that was sent but now contains the <span>jobID</span> for the new job and other default property values.</p></td>
<td><p>404 Not Found - When the report specified in the job descriptor is not found in the server.</p></td>
</tr>
</tbody>
</table>

The following example shows a basic job descriptor in JSON:

``` json
{
    "label": "Sample Job Name",
    "description": "Sample description",
    "trigger": {
        "simpleTrigger": {
            "timezone": "America/Los_Angeles",
            "startType": 2,
            "startDate": "2019-04-21 10:00",
            "occurrenceCount": 1,
            "recurrenceInterval": 1,
            "recurrenceIntervalUnit": "DAY"
        }
    },
    "source": {
        "reportUnitURI": "/adhoc/topics/Cascading_multi_select_topic",
        "parameters": {
            "parameterValues": {
                "Country_multi_select": ["Mexico"],
                "Cascading_name_single_select": ["Chin-Lovell Associates"],
                "Cascading_state_multi_select": ["DF","Jalisco","Mexico"]
            }
        }
    },
    "baseOutputFilename": "Cascading_multi_select_report",
    "outputTimeZone": "America/Los_Angeles",
    "repositoryDestination": {
        "saveToRepository": true,
        "folderURI": "/temp",
        "overwriteFiles": true,
        "sequentialFilenames": false
    },
    "outputFormats": {
        "outputFormat": ["PDF", "XLS"]
    }
}
```

The following example shows a basic job descriptor in XML. As of release 7.5, input values must use the special type syntax below to pass strings, integers, and dates. The collection element is required even for a single value, and the item element is always of type string, as shown below:

``` xml
<job>
    <label>Sample Job Name</label>
    <description>Sample description</description>
    <simpleTrigger>
        <timezone>America/Los_Angeles</timezone>
        <startType>2</startType>
        <startDate>2019-04-21 10:00</startDate>
        <occurrenceCount>1</occurrenceCount>
        <recurrenceInterval>1</recurrenceInterval>
        <recurrenceIntervalUnit>DAY</recurrenceIntervalUnit>
    </simpleTrigger>
    <source>
        <reportUnitURI>/adhoc/topics/Cascading_multi_select_topic</reportUnitURI>
        <parameters>
            <parameterValues>
                <entry>
                    <key>StringParameter</key>
                    <value
                           xsi:-type="collection">
                        <item
                              xsi:type="xs:string">Mexico</item></value>
                </entry>
                <entry>
                    <key>IntegerParameter</key>
                    <value
                           xsi:-type="collection">
                        <item
                              xsi:type="xs:string">123456</item></value>
                </entry>
                <entry>
                    <key>DateParameter</key>
                    <value
                           xsi:-type="collection">
                        <item
                              xsi:type="xs:string">2021-12-31</item></value>
                </entry>
            </parameterValues>
        </parameters>
    </source>
    <baseOutputFilename>Cascading_multi_select_report</baseOutputFilename>
    <outputTimeZone>America/Los_Angeles</outputTimeZone>
    <repositoryDestination>
        <saveToRepository>true</saveToRepository>
        <folderURI>/temp</folderURI>
        <overwriteFiles>true</overwriteFiles>
        <sequentialFilenames>false</sequentialFilenames>
    </repositoryDestination>
    <outputFormats>
        <outputFormat>PDF</outputFormat>
        <outputFormat>XLS</outputFormat>
    </outputFormats>
</job>
```

If needed, you can configure the server to accept the other parameters and keep them with the newly created job, but the default is to store only the required properties. For more information, see [Storing Additional Job Properties](#storing-additional-job-properties).

The response of the PUT request is the descriptor of the newly created job, similar to the result of the GET request shown in [Viewing a Job Definition](#viewing-a-job-definition). It includes all the properties of the job descriptor, including the server-assigned ID and all the null properties.

## Viewing Job Status

The following method returns the current state of a job:

<table>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>GET</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/jobs/</span>&lt;jobID&gt;<span>/state</span>/</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK - Body contains the <code>state</code> descriptor.</p></td>
<td><p>404 Not Found - When the specified <span>&lt;jobID&gt;</span> does not exist or the job is no longer active.</p></td>
</tr>
</tbody>
</table>

The following example shows a typical response in XML:

``` xml
<state>
    <nextFireTime>2022-03-29T18:01:00-07:00</nextFireTime>
    <previousFireTime>2022-03-28T18:01:00-07:00</previousFireTime>
    <value>NORMAL</value>
</state>
```

Either of the fire times may be missing, for example there is no `previousFireTime` if the job has not fired yet, or there is no `nextFireTime` if the job is currently running its last trigger time. The `value` property can be: `NORMAL`, `EXECUTING`, `PAUSED`, or some error state.

## Modifying a Job

Contrary to REST conventions, the jobs service uses the PUT method to create a job and the POST method to modify a job. There are two POST methods for editing the properties of a job. The first method is simpler but the second method is more versatile.

The first method replaces the entire definition of a single job with a new descriptor. To modify an existing job definition, use the GET method to read its `job` descriptor, modify the desired properties, then use the following POST method:

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
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/jobs</span>/&lt;jobID&gt;/</span></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/job+xml</span></p>
<p><span>application/job+json</span></p></td>
<td colspan="2"><p>A complete, well-formed XML or JSON <code>job</code> descriptor, as described in <a href="#the-job-descriptor">The job Descriptor</a>. It may include null properties and other default values that are ignored when using the descriptor as input, as in the result of <a href="#viewing-a-job-definition">Viewing a Job Definition</a>.</p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p><span>accept: application/job+xml</span></p>
<p><span>accept: application/job+json</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK - The response includes the complete <code>job</code> descriptor updated with the submitted changes.</p></td>
<td><p>404 Not Found - When the specified <span>&lt;jobID&gt;</span> does not exist or the job is no longer active.</p></td>
</tr>
</tbody>
</table>

The second POST method lets you modify individual properties in one or more existing jobs. See the examples below:

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
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/jobs</span>?&lt;arguments&gt;</span></p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><span>id</span></p></td>
<td><p><span>jobID</span> string</p></td>
<td colspan="2"><p>Can be used multiple times to create a list of job IDs to update.</p></td>
</tr>
<tr>
<td><p><span>replace<br />
Trigger<br />
IgnoreType</span></p></td>
<td><p>true / false</p></td>
<td colspan="2"><p>Specify true when you send a new trigger type. By default, this is false, and the trigger can be updated but not changed to a different type.</p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/json</span></p>
<p><span>application/xml</span></p></td>
<td colspan="2"><p>A well-formed <code>jobModel</code> descriptor, which is a fragment of a job descriptor containing only the properties to be updated. See the examples below.</p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p><span>accept: application/json</span></p>
<p><span>accept: application/xml</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK - The array or list of jobs that were modified.</p></td>
<td><p>404 Not Found - When the specified <span>&lt;jobID&gt;</span> does not exist or the job is no longer active.</p></td>
</tr>
</tbody>
</table>

In this usage, the POST method allows you to send a partial job description, called a `jobModel` that contains any subset of the job descriptor's properties. This update applies to one or more jobs whose ID is specified by the `id` argument. For example, the following simple request updates the job description in several jobs:

``` text
POST http://localhost:8080/jasperserver-pro/rest_v2/jobs?id=3798&id=3802&id=3806

<jobModel>
    <description>This description updated in bulk</description>
</jobModel>
```

The `jobModel` provides two mechanisms to perform more complex updates:

-   You can describe nested structures by using the nestedName`Model` equivalent element. Like the `jobModel`, nested model elements contain only the subset that you want to modify. Thus you could change one value within a parameter, the end date within a schedule, or an email address within a notification.
-   You can remove the definition of an element by using the `is`PropertyName`Modified` element and giving it the value true. This indicates that the element's new value is null, and thus that the element should be removed altogether from the job descriptor.

In the following example, the description is removed from the target jobs, the trigger's time zone is modified, and the file name is changed. Note that XML descriptors do not use the `trigger` container and thus do not have a `triggerModel` container:

JSON:

``` json
 {
          "label":"Modified label",
          "isDescriptionModified":true,
          "triggerModel":{
              "simpleTriggerModel":{
                  "timezone":"Europe/Helsinki",
              }
          }
          "baseOutputFilename":"NewOutputName"
      }
```

XML:

``` xml
<jobModel>
          <label>Modified label</label>
          <isDescriptionModified>true</isDescriptionModified>
          <simpleTriggerModel>
              <timezone>Europe/Helsinki</timezone>
          </simpleTriggerModel>
          <baseOutputFilename>NewOutputName</baseOutputFilename>
      </jobModel>
```

The response has an array or list of `jobId` elements that were updated:

JSON:

``` json
 {"jobId":[8322,8326]}
```

XML:

``` xml
<jobIdList>
          <jobId>8322</jobId>
          <jobId>8326</jobId>
      </jobIdList>
```

## Pausing Jobs

The following method pauses currently scheduled job execution, also called disabled in the user interface. Pausing keeps the job schedule and all other details but prevents the job from running. It does not delete the job.

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
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/jobs/pause</span>/</span></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/xml</span></p>
<p><span>application/json</span></p></td>
<td colspan="2"><p>An array or list of job IDs to pause. See the example below. If the body of the request is empty, or the list is empty, all jobs in the scheduler are paused.</p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p><span>accept: application/json</span></p>
<p><span>accept: application/xml</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK - The array or list of jobs that were paused. Jobs specified with a <span>&lt;jobID&gt;</span> that does not exist are ignored without error.</p></td>
<td></td>
</tr>
</tbody>
</table>

The request and the response have the same format, an array, or list of `jobId` elements:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">JSON</span><span class="kw">:</span><span class="at"> </span><span class="kw">{</span><span class="st">&quot;jobId&quot;</span><span class="at">:[1236</span><span class="kw">,</span><span class="at">1240</span><span class="kw">,</span><span class="at">1244</span><span class="kw">,</span><span class="at">1248]</span><span class="kw">}</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a><span class="fu">XML</span><span class="kw">:</span><span class="at">  &lt;jobIdList&gt;</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="at">          &lt;jobId&gt;1236&lt;/jobId&gt;</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a><span class="at">          &lt;jobId&gt;1240&lt;/jobId&gt;</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a><span class="at">          &lt;jobId&gt;1244&lt;/jobId&gt;</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a><span class="at">          &lt;jobId&gt;1248&lt;/jobId&gt;</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a><span class="at">      &lt;/jobIdList&gt;</span></span></code></pre></div></td>
</tr>
</tbody>
</table>

## Resuming Jobs

Use the following method to resume any or all paused jobs in the scheduler. Resuming a job means that any defined trigger in the schedule that occurs after the time it is resumed will cause the report to run again. Missed triggers that occur before the job is resumed are never run.

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
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/jobs/resume</span>/</span></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/xml</span></p>
<p><span>application/json</span></p></td>
<td colspan="2"><p>An array or list of job IDs to resume. See the example below. If the body of the request is empty, or the list is empty, all paused jobs in the scheduler is resumed.</p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p><span>accept: application/json</span></p>
<p><span>accept: application/xml</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK - The array or list of jobs that were resumed. Jobs specified with a <span>&lt;jobID&gt;</span> that does not exist are ignored without error.</p></td>
<td></td>
</tr>
</tbody>
</table>

The request and the response have the same format, an array, or list of `jobId` elements:

JSON:

``` json
{"jobId":[1236,1240]}
```

XML:

``` xml
 <jobIdList>
          <jobId>1236</jobId>
          <jobId>1240</jobId>
      </jobIdList>
```

## Viewing Jobs Historical Data

The `jobsAudit/jobsHistoricalData` service provides the execution history for a scheduled job. Each log includes the run status, duration, start and end times, and any associated execution errors.

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
<td colspan="3"><p><code>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/jobsAudit/jobsHistoricalData/{jobId}</code></p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><span>jobId?</span></p></td>
<td><p>Integer</p></td>
<td colspan="2"><p>The identifier of the scheduled job whose execution history is returned.</p></td>
</tr>
<tr>
<td><p><span>sortType?</span></p></td>
<td><p>String</p></td>
<td colspan="2"><p>Specifies the field used to sort the returned execution history.</p>
<p>Possible values are: NONE, SORTBY_EXECUTION_TIME, SORTBY_START_TIME, SORTBY_END_TIME, SORTBY_STATUS, SORTBY_ERROR;</p></td>
</tr>
<tr>
<td colspan="4">Options</td>
</tr>
<tr>
<td colspan="4"><span>accept: application/json</span></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK - The server returns a JSON structure containing the execution history for the specified scheduled job.</p></td>
<td><p>404 Not Found - When the specified job does not exist or the job is no longer active.</p>
<p>403 Forbidden - When audit properties or jobsHistoricalData property not enabled.</p>
<p>Error code: <code>feature.disabled</code></p>
<p>Error message: Jobs Historical Data endpoint is blocked. Enable the jobs historical data and audit configurations to proceed.</p></td>
</tr>
</tbody>
</table>

The following example shows the response in JSON and XML:

JSON:

``` json
{
"historicalData": [     {          "executionTime": 492,         "status": "FAILED",         "startTime": "2026-03-29T21:26:00.011+05:30",
         "endTime": "2026-03-29T21:26:00.503+05:30",
         "error": "Folder not found at \"/public/Test\""      }   ] }
```

!!! note

    The historical data is available only when the Jobs Historical Data and auditing properties are enabled on the server. For more information see the **Configuring the Scheduler Dashboard** section in the [JasperReports® Server Administrator Guide.](https://community.jaspersoft.com/documentation/jasperreports-server/tibco-jasperreports-server-administration-guide/v1000/jasperreports-server-admin-guide-_-overview-_-overview_intro/)

## Restarting Failed Jobs

Use the following method to rerun failed jobs in the scheduler. For each job to be restarted, the scheduler creates an immediate single-run copy of the job, to replace the one that failed. Therefore, all jobs listed in the request body will run once immediately after issuing this command. The single-run copies have a misfire policy set so that they do not trigger any further failures (`MISFIRE_INSTRUCTION_IGNORE_MISFIRE_POLICY`). If the single-run copies fail themselves, no further attempts are made automatically.

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
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/jobs/restart</span>/</span></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/xml</span></p>
<p><span>application/json</span></p></td>
<td colspan="2"><p>An array or list of job IDs to restart. See the example below.</p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p><span>accept: application/json</span></p>
<p><span>accept: application/xml</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK - The array or list of jobs that were restarted.</p></td>
<td></td>
</tr>
</tbody>
</table>

The request and the response have the same array or list of `jobId` elements:

JSON:

``` json
 {"jobId":[8320,8324]}
```

XML:

``` xml
<jobIdList>
          <jobId>8320</jobId>
          <jobId>8324</jobId>
      </jobIdList>
```

## Deleting Jobs

Use the DELETE method to remove jobs from the scheduler. The first form deletes a single job:

<table>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>DELETE</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/jobs</span>/&lt;jobID&gt;/</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK - The body contains the ID of the deleted job.</p></td>
<td>404 Not Found - When the specified job is not found in the server or the job is no longer active.</td>
</tr>
</tbody>
</table>

The second form deletes multiple jobs:

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
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/jobs</span>?&lt;arguments&gt;</span></p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><span>id</span></p></td>
<td><p>Multiple String</p></td>
<td colspan="2"><p>Enter as many job IDs as you want to delete, for example:</p>
<p><span>?id=5594&amp;id=5640&amp;id=5762</span></p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p><span>accept: application/xml</span></p>
<p><span>accept: application/json</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK - The content is a list of deleted jobs, as shown in the example below.</p></td>
<td></td>
</tr>
</tbody>
</table>

The list of deleted jobs in the response has an array or list of `jobId` elements:

JSON:

``` json
{"jobId":[5594,5640,5762]}
```

XML:

``` xml
 <jobIdList>
          <jobId>5594</jobId>
          <jobId>5640</jobId>
          <jobId>5762</jobId>
      </jobIdList>
```

## Storing Additional Job Properties

When sending a job descriptor as described in Scheduling a Report, the server does not store all properties in the descriptor, only the ones needed to define the job. If you wish to keep any additional parameters in the newly created job, you can configure the server so that all valid job properties submitted to the `jobs` service are stored.

Locate the following file and modify the configuration bean. After saving the new configuration, you must restart the server for the change to take effect.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>Storing Additional Job Parameters</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><span>.../WEB-INF/applicationContext-cascade.xml</span></p></td>
</tr>
<tr>
<td><p>Bean</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><code>allowExtraReportParameters</code></p></td>
<td colspan="2"><p>The default value is <code>false</code>, and only essential job properties are stored when creating a job.</p>
<p>When set to <code>true</code>, all valid job descriptor properties sent when creating the job are stored in the newly created job.</p></td>
</tr>
</tbody>
</table>
