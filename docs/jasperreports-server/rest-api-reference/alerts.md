---
title: The alerts Service
description: "The restv2/alerts service provides the interface to create, read, update, delete, and manage single or multiple alerts in the report. When a user schedules an alert in the report to run at a given..."
---

# The alerts Service

The rest_v2/alerts service provides the interface to create, read, update, delete, and manage single or multiple alerts in the report. When a user schedules an alert in the report to run at a given time, with a given recurrence, the server stores this information in an alert. There can be any number of alerts for any number of reports, all created by different users.

With the server's user interface, the alerts service only manages alerts for the reports that are currently active. Alerts are never listed or returned for the chart reports and the reports without numeric values.

Within the alert, a trigger is said to fire when the specified condition is met. When the condition is met, the server generates the output of the scheduled alert.

For example, consider that you are working in a warehouse. You have to restock the inventory based on the storage space. A report is generated which shows the inventory for the products. You need to check the stock twice a day to maintain inventory value. You can define an alert to notify whenever a stock is low in number. Based on which, a report in the output formats like PDF, Excel is emailed to the recipient as a repository links or attachments.

This chapter includes the following sections:

-   Searching for an Alert
-   Viewing an Alert Definition
-   The alert Descriptor

## Searching for an Alert

The GET method of the alerts service has multiple arguments to search for alerts in several ways. The credentials used for authentication determine the scope of the search. Typical users can search only the alerts that they have created. An organization admin (`jasperadmin`) can search all alerts in their organization, and the system admin (`superuser`) can search all alerts on the server. This method only returns active alerts, that still have a pending trigger or are still running after their last trigger.

When used without any arguments, this method returns all scheduled alerts defined by the user in the report. The various arguments in this method help you to find an alert created by the user using administrator credentials.

You can perform a string search in the search criteria to find an alert by name in the user interface. The search criteria show results only for those alert whose name matches with the alert name column. You can also control the number of alert results to be displayed in a single alert page using the pagination and sorting order option.

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
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/alerts</span>?&lt;arguments&gt;</span></p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><span>id?</span></p></td>
<td><p>Integer</p></td>
<td colspan="2"><p>The unique identifier assigned to the alert.</p></td>
</tr>
<tr>
<td><p><span>resourceURI?</span></p></td>
<td><p><span>/path/to/report</span></p></td>
<td colspan="2"><p>The URI (repository path) of a report to schedule an alert. Performs a case-insensitive string search for this value anywhere within the resourceURI property of every alert.</p></td>
</tr>
<tr>
<td><p><span>owner?</span></p></td>
<td><p>String</p></td>
<td colspan="2"><p>The name of the user who scheduled the alert.</p></td>
</tr>
<tr>
<td><p><span>label?</span></p></td>
<td><p>String</p></td>
<td colspan="2"><p>The label to search an alert by Alert name. Performs a case-insensitive string search for this value, which contains the label property of every alert.</p></td>
</tr>
<tr>
<td><p><span>description?</span></p></td>
<td><p>String</p></td>
<td colspan="2"><p>The description of the alert.</p></td>
</tr>
<tr>
<td><p><span>resourceLabel?</span></p></td>
<td><p>String</p></td>
<td colspan="2"><p>The name of the report to find alerts in the report.</p></td>
</tr>
<tr>
<td><p><span>state?</span></p></td>
<td><p>String</p></td>
<td colspan="2"><p>The alert states - NORMAL, EXECUTING, COMPLETE, PAUSED, ERROR, UNKNOWN.</p></td>
</tr>
<tr>
<td><p><span>previousFireTime?</span></p></td>
<td><p>String</p></td>
<td colspan="2"><p>The alerts previous fire time.</p></td>
</tr>
<tr>
<td><p><span>nextFireTime?</span></p></td>
<td><p>String</p></td>
<td colspan="2"><p>The alerts next fire time.</p></td>
</tr>
<tr>
<td><p><span>example?</span></p></td>
<td><p>JSON <code>alertModel</code></p></td>
<td colspan="2"><p>Searches for an alert that matches with the JSON <code>alertModel</code>. It should be the fragment of the alert descriptor with one or more properties to be matched.</p>
<p>You can search for any parameter in the alert descriptor such as - id, version, trigger, output format, or recipient email.</p></td>
</tr>
<tr>
<td><p><span>offset?</span></p></td>
<td><p>Integer</p></td>
<td colspan="2"><p>Specifies the index of the first <code>alertsummary</code> to be returned. When used with the limit parameter, it can be used to implement pagination.</p></td>
</tr>
<tr>
<td><p><span>limit?</span></p></td>
<td><p>Integer</p></td>
<td colspan="2"><p>Specifies the number of <code>alertsummary</code> descriptors in the results. The default is -1 for no limit and thus all results are returned. When used with the offset parameter, it can be used to implement pagination of results.</p></td>
</tr>
<tr>
<td><p><span>sortType?</span></p></td>
<td></td>
<td colspan="2"><p>Possible values are: <code>NONE</code>, <code>SORTBY_ALERTID</code>, <code>SORTBY_ALERTNAME</code>, <code>SORTBY_RESOURCEURI</code>, <code>SORTBY_REPORTNAME</code>, <code>SORTBY_REPORTFOLDER</code>, <code>SORTBY_OWNER</code>, <code>SORTBY_STATUS</code>, <code>SORTBY_LASTRUN</code>, <code>SORTBY_NEXTRUN</code></p></td>
</tr>
<tr>
<td><p><span>isAscending?</span></p></td>
<td><p>true|false</p></td>
<td colspan="2"><p>Determines the sort order: ascending if true, descending if false or omitted. This argument is ignored when <code>sortType</code> is not specified.</p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p><span>accept: application/json</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK - The body contains an array or list of <code>alertsummary</code> descriptors that match the search criteria, as shown in the examples below.</p></td>
<td><p>204 No Content - When no matching alert is found in the server. After an alert finishes running its last triggered instance, it no longer shows up in search results.</p></td>
</tr>
</tbody>
</table>

For example, if you want to request all the alerts for a report, then use the following GET method URL (%2F is the / character) in the request:

``` text
GET http://example.com:8090/jasperserver-pro/rest_v2/alerts?reportUnitURI=%2Freports%2FAllAccounts
```

In the response from the server, the alerts are described in an `alertsummary` element, such as the following example. The `alertsummary` contains a small subset of the properties of the alert descriptor as well as the complete state descriptor:

``` json
{
    "alertsummary": [
        {
            "id": 4164,
            "version": 1,
            "label": "Test",
            "reportUnitURI": "/public/Samples/Reports/RevenueDetailReport",
            "reportLabel": "07. Revenue Detail Report",
            "state": {
                "previousFireTime": "2023-04-24T15:26:00-07:00",
                "nextFireTime": "2023-04-26T15:26:00-07:00",
                "value": "NORMAL"
            },
            "hasDataPointAlert": true,
            "owner": "superuser",
            "lastAlerted" : null
        }
    ]
}
```

The `example` parameter lets you specify a search of any property in the alert descriptor, such as output formats. You can specify any property in the alert descriptor or in any of its nested structures. Some properties may be specified in both the `example` parameter and in a dedicated parameter, for example label. In that case, the search specified in the `example` parameter takes precedence.

For example, you can search for all alerts that specify an output format of PDF and XLS. The JSON `alertModel` to specify this property is:

``` text
"outputFormats": {
"outputFormat": ["PDF", "XLS"]
}
```

Below is the corresponding URI with proper encoding is:

``` text
http://<host>:<port>/jasperserver[-pro]/rest_v2/alerts?example=%7b%22outputFormat%22%3a%22PDF%22%7d
```

## Viewing an Alert Definition

Use the GET method to retrieve details of an alert using its unique id. You can use this method to view an alert definition after searching and finding the ID of an alert that is still active.

<table>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>GET</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/alerts/{alertId}</span></span></p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p><span>accept: application/alert+json</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK - The body contains a descriptor with all details about the alert.</p></td>
<td><p>404 Not Found - When the specified alert is not found in the server. After an alert finishes running its last triggered instance, it is no longer active, then its ID will return this error.</p></td>
</tr>
</tbody>
</table>

The GET method returns a descriptor that includes the various parameters of a scheduled alert. All properties are included, many of which may be null, if not set for the chosen alert. For more information, see The alert Descriptor.

``` json
{
    "id": 4198,
    "version": 1,
    "username": "superuser",
    "label": "TestPostMan",
    "creationDate": "2023-04-28T00:46:17.945-07:00",
    "trigger": {
        "simpleTrigger": {
            "id": 4195,
            "version": 0,
            "timezone": "America/Los_Angeles",
            "startType": 1,
            "misfireInstruction": 0,
            "occurrenceCount": -1,
            "recurrenceInterval": 2,
            "recurrenceIntervalUnit": "DAY"
        }
    },
    "lastError": null,
    "baseOutputFilename": "RevenueDetailReport",
    "exportType": "DEFAULT",
    "outputLocale": "en_US",
    "outputTimeZone": "Asia/Calcutta",
    "source": {
        "reportUnitURI": "/public/Samples/Reports/RevenueDetailReport",
        "parameters": {
            "parameterValues": {
                "ProductFamily": [
                    "Drink",
                    "Food",
                    "Non-Consumable"
                ]
            }
        }
    },
    "outputFormats": {
        "outputFormat": [
            "PDF"
        ]
    },
    "repositoryDestination": {
        "folderURI": "/public/Test",
        "id": 4196,
        "overwriteFiles": true,
        "sequentialFilenames": false,
        "version": 1,
        "saveToRepository": true,
        "usingDefaultReportOutputFolderURI": false,
        "outputFTPInfo": {
            "userName": "anonymous",
            "type": "ftp",
            "port": 21,
            "implicit": true,
            "pbsz": 0,
            "propertiesMap":
        }
    },
    "mailNotification": {
        "bccAddresses": {
            "address": []
        },
        "ccAddresses": {
            "address": []
        },
        "toAddresses": {
            "address": [
                "xyz@tibco.com"
            ]
        },
        "version": 1,
        "id": 4197,
        "includingStackTraceWhenJobFails": false,
        "messageText": "test",
        "resultSendType": "SEND",
        "skipEmptyReports": false,
        "skipNotificationWhenJobFails": false,
        "subject": "test"
    },
    "dataPointAlert": {
        "id": 4199,
        "version": 0,
        "name": "Test API PostMan",
        "dataPoint": "{\"elementUUID\":\"72a3ea24-62a2-4f04-a5a6-d501046ddbcc\"}",
        "operator": "EQUALS",
        "thresholdValue": "0",
        "dataPointType": "NUMERIC",
        "resourceURI": "/public/Samples/Reports/RevenueDetailReport"
    }
}
```

## The alert Descriptor

The `alert` descriptor is a complex data object with nested containers for the various properties that defines a scheduled alert. The `alert` descriptor is the output of the GET method with slightly different content, and the input of the PUT and POST methods.

The properties of the `alert` descriptor are defined in the following sections:

-   General Properties of a Alert, such as label and description, but also the output format and base filename.

-   Source and Input Controls includes the repository URL of the report or report option and the parameter value of any input control if any of them are present and applied to the same report.

-   Simple Trigger defines interval-based repetition of the alert for a given number of occurrences.

-   Calendar Trigger runs at specific times, specific days of the week or days of the month.

-   Alert Output Properties define the file name and locations where output files are written.

-   FTP Output defines whether the output files are written to a remote server.

-   Alert Output Email defines the recipients for successful output files.

-   [Alert DataPoint](alerts.md) defines the numeric values for which an alert is created.

    When submitting an `alert` descriptor to create or modify an alert schedule, not all properties are needed. In the following tables, each property is one of the following:

-   **Required** - This property must have a value for input to define a valid alert.

-   **Optional** - This property may be omitted on input, either because it is nullable, or because the server assigns a default value. The behavior is explained in the property description.

-   **Conditional** - The property may be required or optional depending on other property values. The behavior is explained in the property description.

-   **Ignored** - This property is for internal usage or output only, and the server ignores any value on input. Good practice is to omit these properties from your input.

### General Properties of an Alert

A valid `alert` descriptor contains the following properties:

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
<td><p><code>id</code> (required)</p></td>
<td><p>The ID of the alert assigned by the server. Use this ID to modify, delete, or view the alert.</p></td>
</tr>
<tr>
<td><p><code>version</code> (optional)</p></td>
<td><p>An internal version number, which is used for optimistic locking of an alert object.</p></td>
</tr>
<tr>
<td><p><code>username</code><br />
(required)</p></td>
<td><p>The owner and creator of this alert, including the organization name. Note that only administrators can view other users' alerts.</p></td>
</tr>
<tr>
<td><p><code>label</code><br />
(required)</p></td>
<td><p>A name for the alert, like the label of a resource in the repository.</p></td>
</tr>
<tr>
<td><p><code>description</code><br />
(optional)</p></td>
<td><p>A description string for the alert, which often describes the trigger and chosen output.</p></td>
</tr>
<tr>
<td><p><code>creationDate</code><br />
(required)</p></td>
<td><p>The time and date when the alert was first created and managed internally by the server.</p></td>
</tr>
<tr>
<td><p><code>trigger</code><br />
(optional)</p></td>
<td><p>A container for one of the triggers specified in <span>Simple Trigger</span> or <span>Calendar Trigger</span>. The trigger determines how often the alert runs and the date and time at which it runs.</p></td>
</tr>
<tr>
<td><p><code>source</code><br />
(required)</p></td>
<td><p>A container for the properties that define the repository URI of the report to run parameters. For more information, see <span>Source and Input Controls</span>.</p></td>
</tr>
<tr>
<td><p><code>exportType</code><br />
(optional)</p></td>
<td><p>The default value is <code>DEFAULT</code>, and for scheduling an alert in the report no other value is accepted. Not all output formats are available depending on the value of <code>exportType</code> (see next property).</p></td>
</tr>
<tr>
<td><p><code>outputFormats</code><br />
(required)</p></td>
<td><p>It contains a list of output formats, each to be generated in a separate output file when the alert is triggered. The possible values depend on the resource and the <code>exportType</code>above.</p>
<p>Report (<code>exportType="DEFAULT"</code> is required): <code>PDF, HTML, RTF, CSV, ODT, TXT, DOCX, ODS, XLSX, XLSX_NOPAG, DATA_SNAPSHOT, DATA_CSV</code></p>
<p>The XLS and XLS_NOPAG (Excel 2003) output formats are deprecated. You can use XLSX and XLSX_NOPAG (Excel 2016) instead.</p></td>
</tr>
<tr>
<td><p><code>outputTimeZone</code><br />
(optional)</p></td>
<td><p>The time zone to use when running the report, for example "America/Los_Angeles". By default, the alert is set on the report using the server's default time zone. The time zone names are those supported by <code>java.time.ZoneID</code>, which are defined in the <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones">tz database</a>.</p>
<p>The trigger time zone and output time zone have different purposes even when they are often set to the same value. The trigger time zone determines when the alert is scheduled to run. The output time zone affects anytime or date calculations in the report. The time zone specified in a data source also affects the time and dates in the output.</p></td>
</tr>
<tr>
<td><p><code>outputLocale</code><br />
(optional)</p></td>
<td><p>The locale to use when running the report. By default, the alert is scheduled using the server's default locale. If the report is not based on a Domain with locales, this value has no effect. Use a Java locale string that is also defined in your Domain, for example <code>en</code> (England) or <code>en_CA</code> (England or Canada).</p></td>
</tr>
<tr>
<td><p><code>baseOutput</code><br />
<code>Filename</code><br />
(required)</p></td>
<td><p>The basename of the file for the generated report alert output. Each output format appends its corresponding file extension to this name. This name may also have a time stamp appended as specified in Alert Output Properties. This final output name is then used in all locations where the file is saved: repository, file system, FTP, and email attachment.</p></td>
</tr>
<tr>
<td><p><code>repository</code><br />
<code>Destination</code><br />
(required)</p></td>
<td><p>A container for properties that define the folders and filenames for the output files that are generated each time a scheduled alert runs successfully. Its properties are defined in <span>Alert Output Properties</span> and the optional <span>FTP Output</span>.</p></td>
</tr>
<tr>
<td><p><code>mailNotification</code><br />
(required)</p></td>
<td><p>A container for properties that define email recipients when an alert runs successfully. You can customize the contents of the email and whether the report output files are sent as attachments or links. For more information, see <span>Alert Output Email</span>.</p></td>
</tr>
<tr>
<td><p><code>systemNotification</code><br />
(optional)</p></td>
<td><p>A container for properties that define system status when an alert runs successfully. You can customize the contents of the email and whether the report output files are sent as attachments or links. For more information, see <span>Alert Output Email</span>.</p></td>
</tr>
<tr>
<td><p><code>lastError</code><br />
(optional)</p></td>
<td><p>If an alert fails, the <code>lastError</code> field gets populated with the failure message.</p></td>
</tr>
<tr>
<td><p><code>lastAlerted</code><br />
(optional)</p></td>
<td><p>If an alert is successful, then only the <code>lastAlerted</code> field gets populated with the time when it was alerted.</p></td>
</tr>
</tbody>
</table>

### Source and Input Controls

The source is the report being scheduled by the alert along with any required input controls.

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
<td><p><code>reportUnitURI</code><br />
(required)</p></td>
<td><p>A mandatory property that defines the repository URI or the report options to schedule an alert in the report. The repository URI is relative to the scope of the user credentials used to authenticate the REST call.</p></td>
</tr>
<tr>
<td><p><code>parameters</code><br />
<code>parameterValues</code><br />
(optional)</p></td>
<td><p>A container for the input controls (filters) for an alert. Every required input control in the report must have a JSON list item within <code>parameterValues</code>. If there are no input controls, this property can be omitted. See the example in <a href="managing_single_alert.md">Creating a Alert</a> for the syntax of these properties in JSON.</p></td>
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
<td><p><code>timezone</code><br />
(optional)</p></td>
<td><p>The timezone for all dates and times used by the trigger, for example <code>"America/Los_Angeles"</code>. By default, the trigger uses the same time zone as the server. The time zone names are those supported by <code>java.time.ZoneID</code>, which are defined in the <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones">tz database</a>.</p></td>
</tr>
<tr>
<td><p><code>calendarName</code><br />
(optional)</p></td>
<td><p>The name of a previously defined exclusion calendar. An exclusion calendar defines a set of dates or times when the alert cannot be scheduled. For example, a list of holidays. You can update the exclusion calendar without changing the alert.</p></td>
</tr>
<tr>
<td><p><code>startType</code><br />
(optional)</p></td>
<td><p>Determines when the alert becomes active and sets the base time at which recurrence starts. Supported values:</p>
<p><code>START_TYPE_0</code> - The scheduled alert starts immediately, and the trigger fires right away. This is the default value when this property is omitted.</p>
<p><code>START_TYPE_1</code> - The scheduled alert starts at the specified <code>startDate</code> on which the trigger is set to fire.</p></td>
</tr>
<tr>
<td><p><code>startDate</code><br />
(conditional)</p></td>
<td><p>The date and time at which the alert is scheduled to start, required when <code>startType=START_TYPE_1</code>. The simple trigger fires and begins its recurrence at this time. The format is "yyyy-MM-dd HH:mm" and the timezone property is applied.</p></td>
</tr>
<tr>
<td><p><code>endDate</code><br />
(optional)</p></td>
<td><p>The date and time at which the alert stops. The trigger does not fire after this time, even if any occurrences remain unless a misfire occurs, and the misfire policy allows it. The format is "yyyy-MM-dd HH:mm" and the timezone property is applied.</p></td>
</tr>
<tr>
<td><p><code>misfire</code><br />
<code>Instruction</code><br />
(optional)</p></td>
<td><p>An integer value that defines the behavior if the trigger did not fire when scheduled. The values of <code>misfireInstruction</code> are described in the <span>next table</span>.</p>
<p>A misfire occurs if the alert is inactive or when there are no available threads in the Quartz thread pool for executing the alert. The different trigger types have different misfire instructions available to them. By default they use a 'smart policy' instruction - which has dynamic behavior based on trigger type and configuration. When the alert starts, it searches for any persistent triggers that have misfired, and it then updates each of them based on their individually configured misfire instructions.</p></td>
</tr>
<tr>
<td><p><code>occurrenceCount</code><br />
(required)</p></td>
<td><p>An integer that defines how many times the trigger fires, provided the recurrence intervals happen before the <code>endDate</code>.</p></td>
</tr>
<tr>
<td><p><code>recurrence</code><br />
<code>Interval</code><br />
(required)</p></td>
<td><p>The time interval between firings of the trigger, with the interval unit provided in the next property.</p></td>
</tr>
<tr>
<td><p><code>recurrence</code><br />
<code>IntervalUnit</code><br />
(required)</p></td>
<td><p>The unit of time for the recurrence interval. Supported values: <code>MINUTE</code>, <code>HOUR</code>, <code>DAY</code>, or <code>WEEK</code>. For units greater than <code>MINUTE</code>, the <code>startType</code> and <code>startDate</code> determine the basis for recurrence. For example, if the trigger fires immediately and recurs every 2 days, it fires at the current time on the subsequent days.</p></td>
</tr>
</tbody>
</table>

Choose a misfire policy based on how critical it is and how frequently you want to get notified about the alert. For example, an outage may last 1-2 hours, and if a daily report is critical, then you might want to get notified about the alert as early as possible. But, if a report runs every hour, then you might want to ignore missed alerts on the reports and wait for the next alert at the scheduled time.

!!! note

    Different policies might have the same effect depending on how the trigger is defined. Also, the same policy may have different effects on different trigger types.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>misfireInstruction</th>
<th>Description for Simple Triggers</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>0 (default)</p></td>
<td><p>No instruction (same behavior as option -1 below). Does not trigger the alert that misfired, and takes no action. As the trigger did not fire, the number of occurrences is not decremented. This is the default behavior when no <code>misfireInstruction</code> is defined. The trigger fire the next time according to the recurrence value and unit, as if the misfire had fired at the proper time.</p></td>
</tr>
<tr>
<td><p>-1</p></td>
<td><p>Ignore misfire policy. Instructs the alert that the trigger is never evaluated for a misfire situation. In this case, the alert simply tries to fire it as soon as it can, and then update the trigger as if it had fired at the correct time. This value has the same effect as 0: take no action and do not change the number of occurrences.</p></td>
</tr>
<tr>
<td><p>-999</p></td>
<td><p>Called the smart policy. Instructs the alert that on a misfire situation, the custom <code>updateAfterMisfire</code> method is called on the trigger to determine the misfire action. In this case, you must define and enable a custom trigger class on the server (This is out of the scope of this document).</p></td>
</tr>
<tr>
<td><p>1</p></td>
<td><p>Run now: instructs the alert that on a misfire situation, the trigger wants to be fired now by the alert.</p></td>
</tr>
<tr>
<td><p>2</p></td>
<td><p>Instructs the alert that during a misfire situation, the SimpleTrigger has to be rescheduled to 'now' (even if the associated Calendar excludes 'now') with the repeat count left 'as-is'.</p>
<p>This follows the trigger end-time rule, so if 'now' is after the end-time, then the trigger does not fire.</p></td>
</tr>
<tr>
<td><p>3</p></td>
<td><p>Instructs the alert that on a misfire situation, the SimpleTrigger need to be rescheduled to 'now' (even if the associated Calendar excludes 'now') with the repeat count set to any value, if it had not missed any firings. This follows the trigger end-time, so if 'now' is after the end-time, then the trigger does not fire after the end time.</p></td>
</tr>
<tr>
<td><p>4</p></td>
<td><p>Instructs the alert that on a misfire situation, the SimpleTrigger need to be rescheduled to the next scheduled time after 'now' - considering any associated Calendar, and with the repeat count set to any value, if it had not missed any firings.</p></td>
</tr>
<tr>
<td><p>5</p></td>
<td><p>Instructs the alert that on a misfire situation, the SimpleTrigger wants to be rescheduled to the next scheduled time after 'now' - considering any associated Calendar, and with the repeat count left unchanged.</p></td>
</tr>
</tbody>
</table>

### Calendar Trigger

A calendar trigger lets you schedule an alert to run multiple times based on any combination of time and date. Its properties let you define single values, ranges, or wild-cards for minutes, hours, days, weeks, or months. For example, you can run a report every 15 minutes from 10 AM to noon every Monday.

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
<td><p><code>minutes</code><br />
(required)</p></td>
<td><p>Specifies the minute or minutes at which the trigger fires on a given hour. The value can consist of the following tokens:</p>
<ul>
<li>A single minute value 0-59.</li>
<li>A range of minutes, for example 0-10 means the trigger fires every minute starting from HH:00 to HH:10. Minute values and ranges can be concatenated using commas as separators.</li>
<li>A minute value with an increment, for example 5/10 means that the trigger fires every 10 minutes starting from HH:05.</li>
<li><code>*</code> means the trigger fires every minute of the hour.</li>
</ul></td>
</tr>
<tr>
<td><p><code>hours</code><br />
(required)</p></td>
<td><p>Specifies the hour or hours during which the trigger fires on a given day. All hours are specified in a 24-hour format. The value can consist of the following tokens:</p>
<ul>
<li>A single hour value between 0-23.</li>
<li>A range of hours, for example 8-16 means the trigger fires every hour from 8 AM to 4 PM. Hour values and ranges can be concatenated using commas as separators.</li>
<li>An hour value with an increment, for example 10/2 means the trigger fires during the hour every 2 hours starting from 10 AM.</li>
<li><code>*</code> means the trigger fires during every hour.</li>
</ul></td>
</tr>
<tr>
<td><p><code>months</code><br />
(required)</p></td>
<td><p>A list of <code>month</code> values during which the trigger fires. It can be used in addition to <code>weekDays</code> or <code>monthDays</code> below to suppress the trigger during certain months. The month values are 1 for January and 12 for December. In JSON, it has the following syntax:</p>
<div class="language-text highlight"><pre><code>&quot;months&quot;: {
    &quot;month&quot;: [&quot;1&quot;, &quot;11&quot;, &quot;6&quot;]
}</code></pre></div></td>
</tr>
<tr>
<td><p><code>daysType</code><br />
(required)</p></td>
<td><p>Determines how the trigger days are defined:</p>
<ul>
<li><code>WEEK</code> means the trigger fires on a weekly pattern defined in the <code>weekDays</code> below.</li>
<li><code>MONTH</code> means the trigger fires on a monthly pattern defined in the <code>monthDays</code> below.</li>
<li><code>ALL</code> means that the trigger fires every day at the time or times defined by the <code>hours</code> and <code>minutes</code> properties.</li>
</ul></td>
</tr>
<tr>
<td><p><code>weekDays</code><br />
(conditional)</p></td>
<td><p>Specifies a list of days of the week on which the trigger fires, which has to be repeated every week. This is required if <code>daysType=WEEK</code>, else ignored otherwise. The day values are 1 for Sunday and 7 for Saturday. On the designated days, the trigger fires at the time or times defined by the <code>hours</code> and <code>minutes</code> properties. In JSON, it has the following syntax:</p>
<div class="language-text highlight"><pre><code>&quot;weekDays&quot;: {
    &quot;day&quot;: [&quot;1&quot;, &quot;4&quot;, &quot;6&quot;]
}</code></pre></div></td>
</tr>
<tr>
<td><p><code>monthDays</code><br />
(conditional)</p></td>
<td><p>Specifies the days of the month on which the trigger fires, to be repeated every month. This is required if <code>daysType=MONTH</code>, and ignored otherwise. On the designated days, the trigger fires at the time or times defined by the <code>hours</code> and <code>minutes</code> properties. The value can consist of the following tokens:</p>
<ul>
<li>A single day value 1-31.</li>
<li>A range of days. For example, 2-5 means the trigger fires during each day starting from the 2nd to 5th of the month. Day values and ranges can be concatenated using commas as separators, for example, <code>"1,3,5-22"</code>.</li>
<li>A day value with an increment, for example, 1/5 means that the trigger fires every 5 days starting on the first of the month.</li>
<li><code>*</code> means the trigger fires during every day.</li>
</ul></td>
</tr>
</tbody>
</table>

Choose a misfire policy based on how critical it is and how frequently you want to get notified about the alert. For example, an outage may last 1-2 hours, and if a daily report is critical, then you might want to get notified about the alert as soon as possible. But, if a report runs every hour, you might want to ignore missed alerts on the reports and wait for the next alert at the scheduled time.

!!! note

    Different policies might have the same effect depending on how the trigger is defined. Accordingly, the same policy might have different effects on different trigger types.

| misfireInstruction | Description for Calendar Triggers |
|----|----|
| 0 (default) | No instruction (same behavior as option -1 below). Does not trigger the alert that misfired, and takes no action. As the trigger did not fire, the number of occurrences is not decremented. This is the default behavior when no `misfireInstruction` is defined. The trigger fires the next time according to the recurrence value and unit, as if the misfire had fired at the proper time. |
| -1 | Ignore misfire policy. Instructs the alert that the trigger is never evaluated for a misfire situation. In such cases, the alert simply tries to fire the trigger as early as possible. Subsequently, it then updates the trigger as if it had fired at the correct time. This value has the same effect as 0: take no action and do not change the number of occurrences. |
| -999 | Called the smart policy. Instructs the alert that on a misfire situation, the custom `updateAfterMisfire` method is called on the trigger to determine the misfire action. In this case, you must define and enable a custom trigger class on the server (This is out of the scope of this document). |
| 1 | Run now: instructs the alert that on a misfire situation, the trigger wants to be fired now by the alert. |
| 2 | Instructs the alert that during a misfire situation, the SimpleTrigger has to be rescheduled to 'now' (even if the associated calendar excludes 'now') with the repeat count left 'as-is'. This follows the trigger end-time, so if 'now' is after the end-time, the trigger does not fire. |
| 3 | Instructs the alert that on a misfire situation, the SimpleTrigger has to be rescheduled to 'now' (even if the associated Calendar excludes 'now') with the repeat count set to any value, if it had not missed any firings. This does follow the trigger end-time, so if 'now' is after the end-time, the trigger does not fire. |
| 4 | Instructs the alert that on a misfire situation, the SimpleTrigger has to be rescheduled to the next scheduled time after 'now' - considering any associated Calendar with the repeat count set to any value, if it had not missed any firings. |
| 5 | Instructs the alert that on a misfire situation, the SimpleTrigger has to be rescheduled to the next scheduled time after 'now' - considering any associated Calendar with the repeat count left unchanged. |

### Alert Output Properties

The output properties define the folders and filenames for the output files that are generated each time a scheduled alert runs successfully.

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
<td><p><code>repository</code><br />
<code>Destination</code><br />
(optional)</p></td>
<td><p>A container for the following properties.</p></td>
</tr>
<tr>
<td><p><code>saveToRepository</code><br />
(optional)</p></td>
<td><p>A boolean that determines whether the alert output is written as file resources in the repository. The default value is true. Use the next two parameters to specify the location of the files. When false, no alert output is written to the repository, local file system, or remote FTP. The output files are then only sent by email.</p></td>
</tr>
<tr>
<td><p><code>defaultReport</code><br />
<code>OutputFolderURI</code><br />
(optional)</p></td>
<td><p>Defines a default alert report folder in the repository of the alert owner. The output file resources are saved in this path: "defaultReportOutputFolderURI":"/some/folder/uri".</p></td>
</tr>
<tr>
<td><p><code>UsingDefaultReport</code><br />
<code>OutputFolderURI</code><br />
(optional)</p></td>
<td><p>A boolean that determines if the output is written to the default folder: "usingDefaultReportOutputFolderURI": {true|false}(these folders can be configured as described in the <em>JasperReports Server Administrator Guide</em>). By default, this is false and you must specify the <code>folderURI</code>.</p></td>
</tr>
<tr>
<td><p><code>folderURI</code><br />
(conditional)</p></td>
<td><p>Defines a folder in the repository where the output file resources are saved in this path: "folderURI":"/some/folder/uri". This repository URI is relative to the scope of the user who authenticates the REST call. This property is required if you do not use the default output folder above.</p></td>
</tr>
<tr>
<td><p><code>outputDescription</code><br />
(optional)</p></td>
<td><p>A string that becomes the description of the alert output file resources in the repository. The description is used as it is by all output resources.</p></td>
</tr>
<tr>
<td><p><code>sequentialFilenames</code><br />
(optional)</p></td>
<td><p>A boolean that indicates if a timestamp is to be added to the names of the alert output resources. The timestamp added to the output resource names are created from the alert execution time using the specified pattern. The default value is false.</p></td>
</tr>
<tr>
<td><p><code>timestampPattern</code><br />
(conditional)</p></td>
<td><p>A string containing "yyyyMMddHHmm" tokens to append a timestamp to the base filename. This takes effect if <code>sequentialFilenames</code> is true. For example, an hourly trigger might use "yyyyMMdd-HHmm" but a daily trigger only "yyyy-MM-dd". Characters in the pattern must be valid in file names where the output is being written (repository, local file system, or remote FTP). There is an implicit "-" (dash) character added between the base file name and the pattern, for example, the pattern "MM-dd" becomes basename-02-14.pdf.</p></td>
</tr>
<tr>
<td><p><code>overwriteFiles</code><br />
(optional)</p></td>
<td><p>A boolean to determine the behavior when a newly generated output file has the same name as a previous one.</p>
<p>When true, the alert owner does not have the permission to overwrite an existing resource, and the alert execution fails.</p>
<p>When false, the alert fails if the repository already contains a resource with the same name as one of the alert output resources. The default value is false.</p></td>
</tr>
<tr>
<td><p><code>outputLocalFolder</code><br />
(optional)</p></td>
<td><p>Specifies a path in the local file system (of the JasperReports Server host) under which alert output resources would be created.</p>
<p>The local path is the path in the JRS host's local file system. This functionality is by default disabled and this field is ignored. You can enable it in the file <span>.../WEB-INF/applicationContext.xml</span>, by setting the <code>enableSaveToHostFS</code> property to <code>true</code>.</p></td>
</tr>
<tr>
<td><p><code>outputFTPInfo</code><br />
(optional)</p></td>
<td><p>It contains parameters for writing alert output files to a remote FTP location. For more information, see <span>FTP Output</span>.</p></td>
</tr>
</tbody>
</table>

### FTP Output

You have the option to specify output to a remote server through FTP (File Transfer Protocol). When specified, FTP output is always in addition to repository output, and the output is written to both the repository and the FTP location. The file names to be written are the same as for the repository, therefore the `baseOutputFilename`, and sequential pattern must be valid on the FTP file system. The file overwrite and sequential filename behavior also apply to FTP output.

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
<td><p>The type of FTP connection requested: <code>ftp</code> (default), <code>ftps</code>, or <code>sftp</code>.</p></td>
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
<td><p>The login username for the FTP server.</p></td>
</tr>
<tr>
<td><p><code>password</code><br />
(conditional)</p></td>
<td><p>The login password for the given userName on the FTP server.</p></td>
</tr>
<tr>
<td><p><code>folderPath</code><br />
(conditional)</p></td>
<td><p>The path of the folder under which the alert output resources should be created.</p></td>
</tr>
<tr>
<td><p><code>implicit</code><br />
(optional)</p></td>
<td><p>Specifies the security mode for FTPS. If true, then it is implicit (default), and when false, it is explicit. If the implicit is true, the default port is set to 990.</p></td>
</tr>
<tr>
<td><p><code>protocol</code><br />
(optional)</p></td>
<td><p>Specifies the secure socket protocol to be used, for example SSL or TLS.</p></td>
</tr>
<tr>
<td><p><code>prot</code><br />
(optional)</p></td>
<td><p>Specifies the PROT command for FTP. Supported values are:</p>
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
<td><p>When using SFTP authentication, store the SSH key file in the repository and specify its repository URI in this property. For more information about securing files in the repository, see the <em>JasperReports Server Administrator Guide</em>.</p></td>
</tr>
<tr>
<td><p><code>sshPassphrase</code><br />
(conditional)</p></td>
<td><p>When using SFTP authentication, specify the passphrase for the SSH private key file stored in the repository.</p></td>
</tr>
</tbody>
</table>

### Alert Output Email

When an alert runs successfully, the properties in `mailNotification` specify email recipients for the report output files. You can specify subject and body content, and you can choose to send output as attachments or links. However, if an alert fails, no report output is sent.

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
<td><p><code>toAddresses</code><br />
(required)</p></td>
<td><p>A list of addresses to which alert output emails are sent. This property is required if you are sending an output email.</p></td>
</tr>
<tr>
<td><p><code>ccAddresses</code><br />
(optional)</p></td>
<td><p>A list of addresses to which alert output emails are CC'd.</p></td>
</tr>
<tr>
<td><p><code>bccAddresses</code><br />
(optional)</p></td>
<td><p>A list of addresses to which alert output emails are BCC'd.</p></td>
</tr>
<tr>
<td><p><code>subject</code><br />
(required)</p></td>
<td><p>A string that is used as a subject line for all output emails from this alert.</p></td>
</tr>
<tr>
<td><p><code>messageText</code><br />
(optional)</p></td>
<td><p>A string that is used in the body of output emails for the alert. At alert execution time, links to the output and errors might get appended to the notification message text.</p></td>
</tr>
<tr>
<td><p><code>resultSendType</code><br />
(required)</p></td>
<td><p>Determines whether the notification would include the alert output as attachments, or include links to the output in the repository. Each value has a different behavior and you must set this property based on your other properties:</p>
<p><code>SEND</code> - The email notification should contain links to the alert output generated in the repository.</p>
<p><code>SEND_ATTACHMENT</code> - The email notification should contain the alert output as attachments.</p>
<p><code>SEND_ATTACHMENT_NOZIP</code> - The email notification should contain the alert output in non-ZIP format attachments.</p>
<p><code>SEND_EMBED</code> - The email notification should embed the HTML alert output in the email body.</p>
<p><code>SEND_ATTACHMENT_ZIP_ALL</code> - The email notification should contain the alert output as attachments in one ZIP file.</p>
<p><code>SEND_EMBED_ZIP_ALL_OTHERS</code> - The email notification should embed the HTML alert output in the email body and put the other output type attachments in one ZIP file.</p></td>
</tr>
<tr>
<td><p><code>skipEmptyReports</code><br />
(optional)</p></td>
<td><p>A boolean that specifies whether the email notification should be skipped for alert executions to the produce empty reports (successful completion but no content). The default value is false.</p></td>
</tr>
<tr>
<td><code>messageTextWhenAlertFails</code>
<p>(optional)</p></td>
<td>The text of the email notification when the alert fails. At alert execution time, links to the output and errors might get appended to the notification message text.</td>
</tr>
<tr>
<td><p><code>skipNotification</code><br />
<code>WhenAlertFails</code></p>
<p>(optional)</p></td>
<td><p>A boolean that specifies whether the mail notification should be send if the alert fails. The default value is false.</p></td>
</tr>
<tr>
<td><p><code>includingStack</code><br />
<code>TraceWhenAlertFails</code><br />
(optional)</p></td>
<td>A boolean that specifies whether the mail notification would include a detailed stack trace of an exception. The default value is false.</td>
</tr>
</tbody>
</table>

### Alert DataPoint

When an alert runs successfully, the properties in `datapointalert` specify the numeric values of the report using which the alert is created. You can specify the following values to create an alert in the report.

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
<td><p><code>dataPointAlert</code></p>
<p>(required)</p></td>
<td>A container for the following properties.</td>
</tr>
<tr>
<td><code>id</code>
<p>(required)</p></td>
<td>The ID of the alert data point assigned by the server.</td>
</tr>
<tr>
<td><code>version</code>
<p>(optional)</p></td>
<td>An internal version number, which is used for optimistic locking of an alert data point object.</td>
</tr>
<tr>
<td><p><code>name</code></p>
<p>(required)</p></td>
<td><p>Specifies the name of the data point alert.</p></td>
</tr>
<tr>
<td><p><code>dataPoint</code></p>
<p>(required)</p></td>
<td><p>Determines the element UUID from the report on which the alert is created.</p></td>
</tr>
<tr>
<td><p><code>operator</code></p>
<p>(required)</p></td>
<td><p>Supported values are: <code>equals</code>, <code>notEqual</code>, <code>less</code>, <code>lessOrEqual</code>, <code>greater</code>, <code>greaterOrEqual</code></p></td>
</tr>
<tr>
<td><p><code>thresholdValue</code></p>
<p>(required)</p></td>
<td><p>The value for which the alert should be triggered.</p></td>
</tr>
<tr>
<td><p><code>dataPointType</code></p>
<p>(required)</p></td>
<td><p>The supported values are numeric.</p></td>
</tr>
<tr>
<td><p><code>resourceURI</code></p>
<p>(required)</p></td>
<td><p>The report URI on which the data point is present.</p></td>
</tr>
</tbody>
</table>
