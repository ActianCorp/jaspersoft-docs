---
title: Report Scheduling API
description: Reports on the server can be executed asynchronously using the Report Scheduling API. Asynchronous report execution involves defining the report job and using the report scheduling service to...
---

# Report Scheduling API

Reports on the server can be executed asynchronously using the Report Scheduling API. Asynchronous report execution involves defining the report job and using the report scheduling service to schedule it.

## Report Jobs

A report job definition consists of:

-   Report attributes: Each job must be linked to a single JasperReport on the server. If applicable, the job must also contain values for the report input parameters.

-   Scheduling attributes: Instruct the scheduler when to execute the job. A report job can be a one-time job that can be launched immediately or at a specified moment, or a recurring job that runs repeatedly at specified times.

Two types of recurrence are supported by default:

-   Simple recurrence - You can schedule a job to repeat at fixed time intervals like every 4 hours, every 2 days, or every week. The job start date attribute is used to specify the moment of the first occurrence. You can specify the number of times the job should occur or an end date for the job.

-   Calendar recurrence - You can schedule a job to repeat at specified calendar moments like at 8 PM every work day or on the first of every month.

-   Output attributes. Instruct the scheduling service on what to do with the report output. You specify the report output formats and the repository location where the report output is saved. You can also specify one or more addresses to which email notifications are sent. The notifications can include the report output.

A report job definition is an instance of the `com.jaspersoft.jasperserver.api.engine.scheduling.domain.ReportJob`<br>
bean class. To instantiate a new report job definition, you would use code similar to the following:

``` text
ReportJob job = new ReportJob();
  job.setLabel("foo"); //set the job label
  job.setDescription("bar"); //set the job description
```

The job source is created as a sub-bean:

``` text
ReportJobSource source = new ReportJobSource();
  source.setReportUnitURI("/test/reportURI"); //set the report to run
  Map params = new HashMap();
  params.put("param1", new Integer(5));
  params.put("param2", "value2");
  source.setParametersMap(params); //set the report input parameter values
job.setSource(source); //set the job source
```

The job trigger is used to specify when the job should occur. The basic `com.jaspersoft.jasperserver.api.engine.scheduling.domain.ReportJobTrigger`<br>
bean type is abstract; two concrete types extend it: `com.jaspersoft.jasperserver.api.engine.scheduling.domain.ReportJobSimpleTrigger` and `com.jaspersoft.jasperserver.api.engine.scheduling.domain.ReportJobCalendarTrigger`.

For example, to create a job that fires 20 times every 10 days you would use code similar to this:

``` text
Date startDate = ...
  ReportJobSimpleTrigger trigger = new ReportJobSimpleTrigger();
  trigger.setStartDate(startDate);
  trigger.setOccurrenceCount(20);
  trigger.setRecurrenceInterval(10);
  trigger.setRecurrenceIntervalUnit(ReportJobSimpleTrigger.INTERVAL_DAY);
  job.setTrigger(trigger);
```

Next, you need to specify the job output attributes. To set the output filename and format, use code similar to the following:

``` text
job.setBaseOutputFilename("foo"); //the base output file name
  job.addOutputFormat(ReportJob.OUTPUT_FORMAT_PDF); //output PDF
  job.addOutputFormat(ReportJob.OUTPUT_FORMAT_HTML); //and HTML
```

You can send your output to several different locations. The most common output destination is the repository. Alternative output locations include an FTP server or a user’s local drive. To output to the `jasperserver` repository, use code similar to this:

``` text
  ReportJobRepositoryDestination repositoryDestination = new
    ReportJobRepositoryDestination();
  repositoryDestination.setFolderURI("/test/scheduled");
    // the repository folder where to output the files
  repositoryDestination.setSequentialFilenames(true);
    //append a timestamp to the file names
  job.setContentRepositoryDestination(repositoryDestination);
```

To upload the output to an FTP server instead of the repository, use code similar to this:

``` text
  FTPInfo ftpInfo = new FTPInfo();
  ftpInfo.setUserName("jsmith$mycompany");
  ftpInfo.setPassword("_________________");
  ftpInfo.setFolderPath("/Shared/Users/JSmith");
  ftpInfo.setServerName("ftp-mycompany.ftpserver.com");
  job.getContentRepositoryDestination().setOutputFTPInfo(ftpInfo);
```

To send the output to a user’s local drive, use code similar to this:

``` text
job.getContentRepositoryDestination().setOutputLocalFolder("C:\Users\JSmith\JRS");
```

Optionally, you can instruct the reporting scheduler to send a notification once the job completes. This notice normally goes to the user who created the report:

``` text
ReportJobMailNotification mailNotification = new ReportJobMailNotification();
  mailNotification.addTo("john@smith.com"); //the recipient
  mailNotification.setSubject("Scheduled report"); //the subject
  mailNotification.setMessageText("Executed report.\n"); //the message body
  mailNotification.setResultSendType(
    ReportJobMailNotification.RESULT_SEND_ATTACHMENT);
    //send the report output as attachments
  mailNotification.setSkipNotificationWhenJobFails(true);
  //prevents email for failed jobs
  job.setMailNotification(mailNotification);
```

!!! note

    `ReportJobMailNotification` has a number of field types, including `RESULT_SEND`, which embeds a link in the email, `RESULT_SEND_ATTACHMENT` that sends the results as a zipped attachment, `RESULT_SEND_ATTACHMENT_NOZIP`, and `RESULT_SEND_EMBED`, which embeds the results as HTML content in the email. `RESULT_SEND` can be used only when the output is saved to the repository using `setContentRepositoryDestination()`.

You can also optionally email an alert to the job creator, an administrative user, or both. For example, to send an alert when the job fails, use a code similar to the following:

``` text
ReportJobAlert alert = new ReportJobAlert();
  alert.setRecipient(ReportJobAlert.Recipient.ADMIN);
  // sets first recipient. Other options are OWNER, BOTH, NONE
  alert.setMessageText("Report failed"); //the message body
  alert.setJobState(ReportJobAlert.JobState.FAIL_ONLY);
  ArrayList<String> to_Addresses = new ArrayList<String>();
  //list of additional addresses to receive cc
  to_Addresses.add("admin@smith.com");
  to_Addresses.add("admin.smith@gmail.com");
  alert.setToAddresses(to_Addresses);
  job.setAlert(alert);
```

!!! note

    The ADMIN recipient is set by role. The default is ROLE_ADMINISTRATOR. The ADMIN recipient can be changed in the `administratorRole` bean in `<js-src>/jasperserver/jasperserver-war/src/main/webapp/WEB-INF/applicationContext-report-scheduling.xml`.

    For example, suppose you have used Manage &gt; Roles in the JasperServer user interface to add the role ROLE_SCHEDULER_ADMIN. To set that user as the recipient for all ADMIN email alerts, modify the `administratorRole` bean as follows:

    `<entry key="administratorRole" value="ROLE_SCHEDULER_ADMIN">`

## Report Job Model

A report job model allows you to specify scheduling and output attributes for multiple report jobs at the same time. A report job model takes a list of report job IDs and a single set of attributes for all report jobs in the list.

A report job model definition consists of:

-   Scheduling attributes. Instruct the scheduler when to execute the job. A report job model can specify a one-time job, a simple recurring job, or a calendar recurring job.

-   Output attributes. Instruct the scheduling service what to do with the report output.

You need to define only those attributes you want to update. Empty attributes are left unchanged in the original report jobs.

A report job model definition is an instance of the `com.jaspersoft.jasperserver.api.engine.scheduling.domain.ReportJobModel`<br>
bean class, which extends `ReportJob`.

To instantiate a new report job model definition, you should use code similar to the following:

``` text
ReportJobModel jobModel= new ReportJobModel();
```

To set the destination, mail notification, and schedule for a report job model, you should use code similar to the following:

``` text
  ReportJobRepositoryDestinationModel destinationModel = new
    ReportJobRepositoryDestinationModel();
  destinationModel.setFolderURI("/test/operations");
  jobModel.setContentRepositoryDestinationModel(destinationModel);
ReportJobMailNotificationModel mailNotificationModel = new
    ReportJobMailNotificationModel();
  mailNotificationModel.setSkipNotificationWhenJobFails(false);
  //send email even when job fails
  mailNotificationModel.setIncludeStackTraceWhenJobFails
  //send stack trace when job fails
  jobModel.setMailNotificationModel(mailNotificationModel);
Date startDate = ...
  ReportJobSimpleTriggerModel trigger = new ReportJobSimpleTriggerModel();
  trigger.setStartDate(startDate);
  trigger.setOccurrenceCount(20);
  trigger.setRecurrenceInterval(10);
  trigger.setRecurrenceIntervalUnit(ReportJobSimpleTrigger.INTERVAL_DAY);
  jobModel.setTriggerModel(trigger);
```

Any report job attributes not updated by `ReportJobModel` remain unchanged. In the example above, the existing email recipient, subject, and message remain the same for the updated jobs, as well as any existing alerts.

The report scheduling service also uses `ReportJobModel` to retrieve a list of all active report jobs that match the attributes specified in the report job model. The list of report jobs retrieved from `ReportJobModel` can be sorted using the `ReportJobSortType` subclass of `ReportJobModel`. See [section 1.0.1.5, “Report Scheduling Service,” on page 1](report-scheduling-java-api.md) for more information.

## Report Job Summary

Report job summaries hold information returned by the scheduler service. The `ReportJobSummary` class has a number of methods that allow you to retrieve specific information about the summary. Some useful methods are:

-   `getStateCode`: Returns the execution state of the report job, such as `STATE_COMPLETE`, `STATE_EXECUTING`, etc.

-   `getNextFireTime`: Returns the next time the job is scheduled to run, `null` if not scheduled in the future.

-   `getPreviousFireTime`: Returns the last time that the job was run, `null` if the job has not yet been executed.

## Report Job ID Holder

The `ReportSchedulingService` assigns every active report job a report job ID. This ID can be wrapped using the `ReportJobIDHolder` class. `ReportJobIDHolder` is used by some report scheduling API methods.

## Report Scheduling Service

The scheduling service is used to schedule a report job and provide information about existing jobs. The built-in scheduling service implementation consists of a Hibernate-based component that persists job definitions and a Quartz scheduler that schedules and fires the jobs.

Once a report job definition is created, it is passed to the scheduling service:

``` text
ReportSchedulingService schedulingService = ...
  ReportJob job = ...
  schedulingService.scheduleJob(executionContext, job);
```

!!! note

    The `ReportSchedulingService` is not a Java object included in the API, instead, you must inject a `ReportSchedulingService` instance (that is, define a bean called `reportSchedulingService` using Spring). Your bean should include custom code to produce the desired behavior. For more information on defining a bean, see [section 1.0.1, “Accessing API Implementations Using the Spring Framework,” on page 1](accessing-java-apis-using-spring.md).

The scheduling service also contains methods for the removing one or more existing report jobs: `removeScheduledJob` and `removeScheduledJobs`.

To load the full report job definition for a job, use the `getScheduledJob` method. You can alter the job definition then update it using the `updateScheduledJob` service method.

You can alter and update a list of report jobs using the `updateScheduledJobs` service method. `updateScheduledJob` takes a `ReportJobModel` and updates the specified jobs to match the attributes in the `ReportJobModel`. Unspecified attributes remain unchanged. The trigger is handled somewhat differently from the other attributes. A Boolean parameter, `replaceTriggerIgnoreType`, specifies one of two options:

-   `true`: Replace the trigger in all listed report jobs with the trigger in the `ReportJobModel`.

-   `false`: If a trigger is present in the report job model, check that all listed report jobs have the same trigger type (`SimpleTrigger` or `CalendarTrigger`) as the report job model. If one or more report jobs have a different trigger type, the update fails for all report jobs.

For example, to update two report jobs, including the trigger, to match the parameters in a specified report job model, you should use code similar to the following:

``` text
List<ReportJob> reportJobs = new ArrayList<ReportJob>();
  reportJobs.add(job_01);
  reportJobs.add(job_02);
ReportJobModel jobModel = ...
updateScheduledJobs(executionContext, reportJobs, jobModel,
  true) //replaceTriggerIgnoreType - when true, replace trigger in the report jobs
          with the trigger from the model.
```

!!! warning

    Use caution when updating the job trigger, because the original Quartz trigger is dropped and a new trigger that corresponds to the updated attributes is created.

Two methods of the scheduling service let you retrieve a list of jobs. The retrieved list consists of instances of `com.jaspersoft.jasperserver.api.engine.scheduling.domain.ReportJobSummary` that contain basic job attributes, plus runtime attributes like job status and previous/next fire times.

-   `getScheduledJobSummaries` can be used as follows:

    -   Retrieves job summaries of all active report jobs defined in the scheduler.
    -   With a `reportUnitURI`, retrieves the list of job summaries for scheduled jobs for a report unit.
    -   With a `ReportJobModel` along with other parameters, retrieves the list of scheduled job summaries that match the criteria specified by the `ReportJobModel`.

-   `getJobsByNextFireTime` retrieves the list of all jobs with a next fire time in a specified time interval.

For example, to get all active jobs that match a report job model, you should use code similar to the following:

``` text
ReportJobModel reportJobCriteria = ...
int startIndex = 5 //return all jobs after the first 5 (starts with 0)
int numberOfRows = 30 //number of jobs returned per page
getScheduledJobSummaries(executionContext, reportJobCriteria,
  startIndex,
  numberOfRows,
  SORTBY_REPORTNAME, //value of enum class ReportJobModel.ReportJobSortType
  true); //when true, sort in ascending order
```

To get all scheduled jobs whose next fire time is between `startDate` and `endDate`, you should use a code similar to the following. The next fire time is the value retrieved by `ReportJobSummary.getNextFireTime`.

``` text
List<ReportJobSummary> jobList = new
Date startDate = ...
Date endDate = ...
List<ReportJobSummary> jobList =
  schedulingService.getJobsByNextFireTime(executionContext,
    null, startDate, endDate, null);
```

The `pause` and `resume` methods let you pause or resume a list of jobs. To pause all the jobs retrieved by the previous call, use code similar to the following. If an alert is set, pausing the job triggers the alert:

``` text
schedulingService.pause(jobList, true);
```

The `pauseByID` and `resumeByID` methods let you pause or resume a `ReportJobIDHolder` list.

## Report Jobs Scheduler

The `ReportJobsScheduler` service includes methods for adding, getting, and deleting calendars. Calendars in `ReportJobsScheduler` service are implementations of the Quartz `Calendar` interface. They specify times during which scheduled jobs are not fired. For information about Quartz calendars, see the [Quartz API documentation](https://www.quartz-scheduler.org/documentation/quartz-2.3.0/).

!!! note

    The `ReportJobsScheduler` service is used internally by the central scheduling service. Except for the calendar methods, most methods in the `ReportJobsScheduler` service should not be accessed directly by the report scheduling code.

For example, to register the Quartz calendar `myHolidayCalendar()`, with the `ReportJobsScheduler`, you should use a code similar to the following:

``` text
ReportJobsScheduler.addCalendar("US Holiday Calendar",
  myHolidayCalendar(),
  true, //overwrite any existing calendar with the same name
  true) //update existing triggers that refer to this calendar
```

Other methods allow you to delete a calendar, retrieve a calendar by name, or get a list of the names of all registered calendars: `deleteCalendar`, `getCalendar`, and `getCalendarNames`.

Once you have added a calendar, you can use it in any number of job triggers. For example, to create a trigger that tells a job to run every Monday at 1:00 A.M., unless it is a United States holiday as specified in `myHolidayCalendar()`, you should use code similar to the following:

``` text
  ReportJobCalendarTrigger weeklyTrigger = new ReportJobCalendarTrigger();
    weeklyTrigger.setMinutes("0");
    weeklyTrigger.setHours("1");
    weeklyTrigger.setDaysTypeCode(weeklyTrigger.DAYS_TYPE_WEEK);
    weeklyTrigger.setWeekDays(2); //sets the day of the week; Monday is 2
    weeklyTrigger.setTimezone("America/Los_Angeles");
    weeklyTrigger.setStartType(weeklyTrigger.START_TYPE_NOW);
    weeklyTrigger.setCalendarName("US Holiday Calendar");
      //tells the job not to run on holidays as specified by this calendar
```

You can use a trigger like this to set the holiday calendar for a number of `ReportJobs` using `ReportJobModel`. Set `replaceTriggerIgnoreType` to true to ensure that the trigger is updated for all `ReportJobs`.
