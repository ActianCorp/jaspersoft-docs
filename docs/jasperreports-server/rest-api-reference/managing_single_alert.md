---
title: Managing a Single Alert
description: "You can use the following REST APIs to add, modify, view, and delete single alerts:"
---

# Managing a Single Alert

You can use the following REST APIs to add, modify, view, and delete single alerts:

-   [Creating a Single Alert](#creating-a-single-alert)
-   Reading a Single Alert
-   [Modifying a Single Alert](#modifying-a-single-alert)
-   [Deleting a Single Alert](#deleting-a-single-alert)

## Creating a Single Alert

Contrary to REST conventions, the alerts service uses the PUT method to create an alert and the POST method to modify an alert. To create an alert in the report, specify its properties in an alert descriptor and use the PUT method of the alerts service. Specify the repository path to the resource being scheduled inside the alert descriptor.

Only the authorized user who sends the alert details in the request becomes the owner of the alert, who can view the alert and receive notification.

<table>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>PUT</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/alerts</span></span></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/alert+json</span></p></td>
<td colspan="2"><p>A well-formed JSON <code>alert</code> descriptor as described in <a href="alerts.md">The alert Descriptor</a>. Specify only relevant properties in the alert descriptor and do not include any null properties.</p></td>
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
<td colspan="3"><p>201 Created - The body contains the alert descriptor of the newly created alert. It is similar to the one that was sent but now contains the <span>alertID</span> for the new alert and other default property values. The body of the response is shown below.</p></td>
<td><p>404 Not Found - When no alert is found for the report in the server.</p></td>
</tr>
</tbody>
</table>

The following is an example of the request body for creating an alert in JSON:

``` json
{
    "label": "Alert PM Excel TestNew4",
    "trigger": {
        "simpleTrigger": {
            "timezone": "America/Los_Angeles",
            "startType": 1,
            "startDate": null,
            "endDate": null,
            "occurrenceCount": -1,
            "recurrenceInterval": 1,
            "recurrenceIntervalUnit": "HOUR"
        }
    },
    "baseOutputFilename": "RevenueDetailReport",
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
        "overwriteFiles": true,
        "sequentialFilenames": false,
        "folderURI": "/public/Samples/Reports",
        "saveToRepository": false,
        "timestampPattern": null,
        "outputFTPInfo": {
            "userName": "anonymous",
            "password": "",
            "folderPath": null,
            "serverName": null,
            "type": "ftp",
            "port": 21,
            "propertiesMap":
        }
    },
    "mailNotification": {
        "toAddresses": {
            "address": [
                "xyz@tibco.com"
            ]
        },
        "messageText": "test",
        "resultSendType": "SEND_ATTACHMENT",
        "skipEmptyReports": false,
        "skipNotificationWhenJobFails": false,
        "subject": "Test Now1"
    },
    "dataPointAlert": {
        "name": "AlertUI Data",
        "dataPoint": {
            "elementUUID": "72a3ea24-62a2-4f04-a5a6-d501046ddbcc"
        },
        "operator": "less",
        "thresholdValue": 6800,
        "dataPointType": "NUMERIC",
        "resourceURI": "/public/Samples/Reports/RevenueDetailReport"
    },
    "usingDefaultReportOutputFolderURI": false,
    "outputTimeZone": "America/Los_Angeles"
}
```

!!! note

    Creating an alert with Minute value is accepted and supported only in the REST API, but this causes performance issues in the application. The available options in UI for creating an alert are in Hours, Days, or Weeks.

The following is an example of the response body for creating an alert in JSON:

``` json
{
    "id": 2582,
    "version": 0,
    "username": "superuser",
    "label": "Alert PM Excel TestNew4",
    "creationDate": "2023-10-17T22:27:39.022-07:00",
    "trigger": {
        "simpleTrigger": {
            "id": 2579,
            "version": 0,
            "timezone": "America/Los_Angeles",
            "startType": 1,
            "misfireInstruction": 0,
            "occurrenceCount": -1,
            "recurrenceInterval": 1,
            "recurrenceIntervalUnit": "HOUR"
        }
    },
    "baseOutputFilename": "RevenueDetailReport",
    "exportType": "DEFAULT",
    "outputLocale": "en_US",
    "outputTimeZone": "America/Los_Angeles",
    "source": {
        "parameters": {
            "parameterValues": {
                "ProductFamily": [
                    "Drink",
                    "Food",
                    "Non-Consumable"
                ]
            }
        },
        "reportUnitURI": "/public/Samples/Reports/RevenueDetailReport"
    },
    "outputFormats": {
        "outputFormat": [
            "PDF"
        ]
    },
    "repositoryDestination": {
        "folderURI": "/public/Samples/Reports",
        "id": 2580,
        "overwriteFiles": true,
        "sequentialFilenames": false,
        "version": 0,
        "saveToRepository": false,
        "usingDefaultReportOutputFolderURI": false,
        "outputFTPInfo": {
            "userName": "anonymous",
            "password": "",
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
        "version": 0,
        "id": 2581,
        "includingStackTraceWhenJobFails": false,
        "messageText": "test",
        "resultSendType": "SEND_ATTACHMENT",
        "skipEmptyReports": false,
        "skipNotificationWhenJobFails": false,
        "subject": "Test Now1"
    },
    "dataPointAlert": {
        "id": 2583,
        "version": 0,
        "name": "AlertUI Data",
        "dataPoint": {
            "elementUUID": "72a3ea24-62a2-4f04-a5a6-d501046ddbcc"
        },
        "operator": "less",
        "thresholdValue": "6800",
        "dataPointType": "NUMERIC",
        "resourceURI": "/public/Samples/Reports/RevenueDetailReport"
    }
}
```

The response of the PUT request is the descriptor of the newly created alert, similar to the result of the GET request shown in [Viewing an Alert Definition](alerts.md). It includes all the properties of the alert descriptor, including the server-assigned ID and all the null properties.

## Modifying a Single Alert

Contrary to REST conventions, the alert service uses the PUT method to create an alert and the POST method to modify an alert. To modify an existing alert definition, use the GET method to read its `alert` descriptor, modify the desired properties, then use the following POST method:

<table>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>POST</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/alert/{alertId}</span></span></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/alert+json</span></p></td>
<td colspan="2"><p>A complete well-formed JSON <code>alert</code> descriptor, as described in <a href="alerts.md">The alert Descriptor</a>. It may include null properties and other default values. These values are ignored when using the descriptor as input, as shown in the result of <a href="alerts.md">Viewing a Alert Definition</a>.</p></td>
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
<td colspan="3"><p>200 OK - The response includes the complete <code>alert</code> descriptor updated with the submitted changes.</p></td>
<td><p>404 Not Found - When the specified <span>&lt;alertId&gt;</span> does not exist or the alert is no longer active.</p></td>
</tr>
</tbody>
</table>

The following is an example of the request body for updating an alert in JSON:

``` json
{
    "id": null,
    "version": null,
    "username": "superuser",
    "label": "dafc4_AlertingUpdateAlertRestAlert for report without IC_Updated",
    "description": "Alert Description for report without IC_Updated",
    "creationDate": null,
    "trigger": {
        "simpleTrigger": {
            "id": null,
            "version": null,
            "timezone": null,
            "calendarName": null,
            "startType": 1,
            "startDate": null,
            "endDate": null,
            "misfireInstruction": null,
            "occurrenceCount": 2,
            "recurrenceInterval": 1,
            "recurrenceIntervalUnit": "HOUR"
        }
    },
    "baseOutputFilename": "dafc4_AlertingUpdateAlertRestOutput1697608816923",
    "exportType": null,
    "outputLocale": null,
    "outputTimeZone": "America/Los_Angeles",
    "lastError": null,
    "lastAlerted": null,
    "outputFormats": {
        "outputFormat": [
            "PDF"
        ]
    },
    "repositoryDestination": {
        "folderURI": "/organizations/organization_1/qa_automation/Alerting/0df89_AlertingUpdateAlertRest_Folder",
        "id": null,
        "outputDescription": "Report Output for alert test",
        "overwriteFiles": false,
        "sequentialFilenames": false,
        "version": null,
        "timestampPattern": null,
        "saveToRepository": false,
        "defaultReportOutputFolderURI": null,
        "usingDefaultReportOutputFolderURI": false,
        "outputLocalFolder": null,
        "outputFTPInfo": {
            "userName": "anonymous",
            "password": "",
            "folderPath": null,
            "serverName": null,
            "type": "ftps",
            "protocol": null,
            "port": 990,
            "implicit": true,
            "pbsz": 0,
            "prot": null,
            "propertiesMap":,
            "sshKey": null,
            "sshPassphrase": null
        }
    },
    "mailNotification": {
        "bccAddresses": null,
        "ccAddresses": null,
        "toAddresses": {
            "address": [
                "xyz@tibco.com"
            ]
        },
        "version": null,
        "id": null,
        "includingStackTraceWhenJobFails": null,
        "messageText": "infra-platforms-na2-26210-garsingh.pfa.jaspersoft.com: Test alert notification messageAlertingUpdateAlertResttest_updateAlertNameAndDescription_verifyAlertUpdated_29018",
        "resultSendType": "SEND_ATTACHMENT",
        "skipEmptyReports": false,
        "skipNotificationWhenJobFails": false,
        "subject": "infra-platforms-na2-26210-garsingh.pfa.jaspersoft.com: Alert test email subject_a6bcf",
        "messageTextWhenJobFails": null
    },
    "systemNotification": null,
    "dataPointAlert": {
        "id": null,
        "version": null,
        "name": "Day is greater than 2",
        "dataPoint": {
            "elementUUID": "ce4c285c-0772-451e-bb87-18c24f09b229"
        },
        "operator": "greater",
        "thresholdValue": "2",
        "dataPointType": "NUMERIC",
        "resourceURI": "/organizations/organization_1/qa_automation/Reports/Jrxml_reports/DaysSimpleReport"
    }
}
```

The following is an example of the response body for updating an alert in JSON:

``` text
{
    “alertsId”: [
        4263
    ]
}
```

## Deleting a Single Alert

Use the DELETE method to remove the alert from the report. The below form deletes a single alert.

<table>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>DELETE</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/alerts/{alertsId}</span></span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK - The body contains the ID of the deleted alert.</p></td>
<td>404 Not Found - When the specified alert is not found in the server or the alert is no longer active.</td>
</tr>
</tbody>
</table>
