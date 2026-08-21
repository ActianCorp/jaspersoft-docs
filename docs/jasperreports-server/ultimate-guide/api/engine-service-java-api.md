---
title: Engine Service
description: The engine service includes methods related to report execution. The engineService interface includes the getReportExecutionStatusList and getSchedulerReportExecutionStatusList methods for listing...
---

# Engine Service

The engine service includes methods related to report execution. The `engineService` interface includes the `getReportExecutionStatusList` and `getSchedulerReportExecutionStatusList` methods for listing running report jobs or scheduled running report jobs.

!!! note

    The `engineService` is used internally for report execution. Except for the `getReportExecutionStatusList` and `getSchedulerReportExecutionStatusList` methods, methods in the `engineService` service should not be accessed directly.

To retrieve the list of all currently running instances of the All Accounts report, you would use code similar to the following. The list of report jobs retrieved includes scheduled jobs as well as jobs users are running via the UI:

``` text
ReportExecutionStatusSearchCriteria criteria = new
  ReportExecutionStatusSearchCriteria();
criteria.setJobLabel("All Accounts");
List<ReportExecutionStatusInformation> reportExecutionList =
  engineService.getReportExecutionStatusList(criteria);
```

To retrieve only currently running scheduled instances of the All Accounts report, you would use code similar to this:

``` text
SchedulerReportExecutionStatusSearchCriteria criteria = new
  SchedulerReportExecutionStatusSearchCriteria();
criteria.setJobLabel("All Accounts");
List<ReportExecutionStatusInformation> reportExecutionList =
  engineService.getSchedulerReportExecutionStatusList(criteria);
```

Once you have a list of jobs, you can cancel those jobs using the `reportExecutionStatusInformation` interface:

``` text
for (ReportExecutionStatusInformation reportExecution : reportExecutionList) {
  reportExecution.cancel();
}
```
