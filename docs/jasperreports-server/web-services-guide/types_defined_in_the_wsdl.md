---
title: Types Defined in the WSDL
description: "The WSDL defines several types that are used by the parameters and operation result of the service. The types belong to the http://www.jasperforge.org/jasperserver/ws namespace. The namespace is only..."
---

# Types Defined in the WSDL

The WSDL defines several types that are used by the parameters and operation result of the service. The types belong to the `http://www.jasperforge.org/jasperserver/ws` namespace. The namespace is only an identifier; it is not a valid URL.

This section provides a partial list of the types used for report scheduling; for the complete reference, refer to the WSDL document. The report scheduling types include:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th><p>Type</p></th>
<th><p>Type Element</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><code>Job</code></p></td>
<td><p>Encapsulates all the attributes of a report job. This type is used when full report job details are passed to or returned by an operation.</p></td>
</tr>
<tr>
<td></td>
<td><p><code>ID</code>and<code>version</code></p></td>
<td><p>Required when updating a report job</p></td>
</tr>
<tr>
<td></td>
<td><p><code>reportUnitURI</code></p></td>
<td><p>URI of the report</p></td>
</tr>
<tr>
<td></td>
<td><p><code>username</code></p></td>
<td><p>Set automatically to the name of the calling user when a report job is created</p></td>
</tr>
<tr>
<td></td>
<td><p><code>label</code></p></td>
<td><p>Job label.</p></td>
</tr>
<tr>
<td></td>
<td><p><code>simpleTrigger</code>or<code>calendarTrigger</code></p></td>
<td><p>Job trigger, which can be either a simple (fixed interval) trigger or a calendar trigger</p></td>
</tr>
<tr>
<td></td>
<td><p><code>parameters</code></p></td>
<td><p>List of report parameter/input control values</p></td>
</tr>
<tr>
<td></td>
<td><p><code>baseOutputFilename</code></p></td>
<td><p>Base name for the job output</p></td>
</tr>
<tr>
<td></td>
<td><p><code>outputFormats</code></p></td>
<td><p>List of job output formats (as strings). JasperReports Server has built-in support for the following formats: PDF, HTML, XLS, RTF and CSV.</p></td>
</tr>
<tr>
<td></td>
<td><p><code>outputLocale</code></p></td>
<td><p>String representation of a <code>java.util.Locale</code> to be used as report locale</p></td>
</tr>
<tr>
<td></td>
<td><p><code>repositoryDestination</code></p></td>
<td><p>Location in the repository where the report output is saved</p></td>
</tr>
<tr>
<td></td>
<td><p><code>mailNotification</code></p></td>
<td><p>Information regarding the email notification that is sent when the job executes. Set this value to NULL to suppress notifications.</p>
<p><span>Note:</span> To use this feature, you must configure a mail server, as described in <span>JasperReports Server Administrator Guide.</span></p></td>
</tr>
<tr>
<td colspan="2"><p><code>JobSimpleTrigger</code></p></td>
<td><p>Job trigger that fires at fixed intervals</p></td>
</tr>
<tr>
<td></td>
<td><p><code>startDate</code>and<code>endDate</code></p></td>
<td><p>Start and end dates of the job</p></td>
</tr>
<tr>
<td></td>
<td><p><code>timezone</code></p></td>
<td><p>Time zone of the start and end dates</p></td>
</tr>
<tr>
<td></td>
<td><p><code>occurrenceCount</code></p></td>
<td><p>How many times to run the job. If a single run job is wanted, use <code>1</code> as occurrence count; if the job is to be fired indefinitely or until the end date, use <code>-1</code>.</p></td>
</tr>
<tr>
<td></td>
<td><p><code>recurrenceInterval</code>and<code>recurrenceIntervalUnit</code></p></td>
<td><p>Interval at which the job should recur: <code>MINUTE</code>, <code>HOUR</code>, <code>DAY</code>, <code>WEEK</code>.</p></td>
</tr>
<tr>
<td colspan="2"><p><code>JobCalendarTrigger</code></p></td>
<td><p>Job trigger that fires at a time specified by a CRON-like expression</p></td>
</tr>
<tr>
<td></td>
<td><p><code>startDate</code>and<code>endDate</code></p></td>
<td><p>Start and end dates of the job</p></td>
</tr>
<tr>
<td></td>
<td><p><code>timezone</code></p></td>
<td><p>Time zone of the start and end dates</p></td>
</tr>
<tr>
<td></td>
<td><p><code>minutes</code></p></td>
<td><p>Minute or minutes of the day when the job is to run.</p></td>
</tr>
<tr>
<td></td>
<td><p><code>hours</code></p></td>
<td><p>Hour or hours of the day when the job is to run.</p></td>
</tr>
<tr>
<td></td>
<td><p><code>daysType</code></p></td>
<td><p>How <span>days are specified. Possible values are </span><code>ALL</code><span>, </span><code>WEEK,</code><span> and </span><code>MONTH.</code></p></td>
</tr>
<tr>
<td></td>
<td><p><code>weekDays</code></p></td>
<td><p>Used when <code>daysType</code> is <code>WEEK</code>; this indicates the days of the week from Saturday (1) to Sunday (7).</p></td>
</tr>
<tr>
<td></td>
<td><p><code>monthDays</code></p></td>
<td><p>Used when <code>daysType</code> is <code>MONTH</code>, this indicates the month days.</p></td>
</tr>
<tr>
<td></td>
<td><p><code>months</code></p></td>
<td><p>Months (from 0 to 11) on which the job should be triggered.</p></td>
</tr>
<tr>
<td colspan="2"><p><code>JobRepositoryDestination</code></p></td>
<td><p>Information about where to save the report job output in the repository.</p></td>
</tr>
<tr>
<td></td>
<td><p><code>folderURI</code></p></td>
<td><p>URI of the folder where the report output will be saved.</p></td>
</tr>
<tr>
<td></td>
<td><p><code>sequentialFilenames</code></p></td>
<td><p>Flag indicating whether to append timestamps to the base output name.</p></td>
</tr>
<tr>
<td colspan="2"><p><code>JobMailNotification</code></p></td>
<td><p>Encapsulates the attributes of the mail notification to send regarding the report job.</p></td>
</tr>
<tr>
<td></td>
<td><p><code>toAddresses</code></p></td>
<td><p>List of email addresses to which the notification will be sent.</p></td>
</tr>
<tr>
<td></td>
<td><p><code>subject</code></p></td>
<td><p>Subject of the email notification.</p></td>
</tr>
<tr>
<td></td>
<td><p><code>resultSendType</code></p></td>
<td><p>Indicates whether to attach the report output to the email; the value is either SEND (only the messages is sent) or SEND_ATTACHMENT (the report output is sent along as a message attachment)<span>.</span></p></td>
</tr>
<tr>
<td colspan="2"><p><code>JobSummary</code></p></td>
<td><p>Used when a list of report jobs is retrieved via the service. The full report job information can be retrieved individually for required jobs.</p></td>
</tr>
<tr>
<td></td>
<td><p><code>id</code></p></td>
<td><p>Unique identifier of the job.</p></td>
</tr>
<tr>
<td></td>
<td><p><code>label</code></p></td>
<td><p>Display label of the job.</p></td>
</tr>
<tr>
<td></td>
<td><p><code>state</code></p></td>
<td><p>State of the job. For example, NORMAL indicates that the job is waiting for next execution; EXECUTING means the job is running.</p></td>
</tr>
<tr>
<td></td>
<td><p><code>previousFireTime</code></p></td>
<td><p>Most recent run time.</p></td>
</tr>
<tr>
<td></td>
<td><p><code>nextFireTime</code></p></td>
<td><p>Next run time.</p></td>
</tr>
</tbody>
</table>
