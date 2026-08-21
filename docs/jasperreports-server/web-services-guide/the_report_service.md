---
title: The report Service
description: The rest/report service is superseded by The v2/reports Service and The v2/reportExecutions Service.
---

# The report Service

!!! note

    The rest/report service is superseded by [The v2/reports Service](the_v2_reports_service.md) and [The v2/reportExecutions Service](the_v2_reportexecutions_service.md).

The report service uses a combination of the PUT, GET, and POST methods to run reports and make them available in multiple ways through the API:

- The PUT method generates the report in any number of formats, stores the output in the session, and returns an identifier.
- The GET method with the identifier and file ID downloads any one of the file outputs.
- The POST method can be used to regenerate the report, for example in different formats, and supports page-by-page downloading of the PDF output.

The report service relies on the user session to store the report output in memory. While this does not follow the stateless nature of REST implementations, it reflects the performance optimization strategies in the JasperReports Server architecture. Filling and generating a report is resource intensive, so it is better to fill and generate once and store multiple output files temporarily than to generate the report from scratch for every output type that is requested.
