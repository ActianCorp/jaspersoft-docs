---
title: The v2/reportExecutions Service
description: "The v2/reports service allows clients to easily run a report, wait for the reply, and receive the output. This is called synchronous report execution because the client must wait for the response...."
---

# The v2/reportExecutions Service

The v2/reports service allows clients to easily run a report, wait for the reply, and receive the output. This is called synchronous report execution because the client must wait for the response. When managing large reports that may take minutes to complete, or when running a large number of reports simultaneously, sychronous report execution slows down the client or uses many threads, each waiting for a report.

The v2/reportExecutions service provides asynchronous report execution, so that the client does not need to wait for report output. Instead, the client obtains a reqest ID and periodicallychecks the status of the report to know when it is ready. When the report is finished, the client can download the output. The client can also send an asynchronous request for other export formats (PDF, Excel, and others) of the same report. Again the client can check the status of the export and download the result when the export has completed.

Reports being scheduled on the server also run asynchronously, and the v2/reportExecutions allows you to access jobs that are triggered by the scheduler. Finally, the v2/reportExecutions service allows the client to stop any report execution or job that has been triggered.
