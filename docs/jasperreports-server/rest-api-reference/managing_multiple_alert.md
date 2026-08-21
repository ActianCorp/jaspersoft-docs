---
title: Managing Multiple Alerts
description: "You can use the following REST APIs to modify, pause, resume, restart, and delete multiple alerts:"
---

# Managing Multiple Alerts

You can use the following REST APIs to modify, pause, resume, restart, and delete multiple alerts:

- Modifying Multiple Alerts
- Pausing Multiple Alerts
- Resuming Multiple Alerts
- Restarting Multiple Alerts
- Deleting Multiple Alerts

## Modifying Multiple Alerts

Contrary to REST conventions, the alert service uses the PUT method to create an alert and the POST method to modify multiple alerts. Typical user cannot modify the alert of another user but the system admin (`superuser`) can modify the alert of all users. Organization admin (`jasperadmin`) can modify only if the users and jasperadmin belong to the same organization. To modify an existing alert definition, use the GET method to read its `alert` descriptor, modify the desired properties, then use the following POST method:

<table>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>POST</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/alerts?id={ID_1}&amp;id={ID_2}&amp;...&amp;id={ID_n)</span></span></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/alert+json</span></p></td>
<td colspan="2"><p>A complete well-formed JSON <code>alert</code> descriptor, as described in <a href="alerts.md">The alert Descriptor</a>. It may include null properties and other default values. These are ignored when using the descriptor as input, as shown in the result of <a href="alerts.md">Viewing a Alert Definition</a>.</p></td>
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
<td colspan="3"><p>200 OK - The response includes the complete <code>alerts</code> descriptor updated with the submitted changes.</p></td>
<td><p>404 Not Found - When the specified <span>&lt;alertId&gt;</span> does not exist or the alerts are no longer active.</p></td>
</tr>
</tbody>
</table>

The following is an example of the request body for updating multiple alerts in JSON:

```
{
    "label":"Modified label",
    "isDescriptionModified":true,
    "triggerModel":{
    "simpleTriggerModel":{
            "timezone":"Europe/Helsinki",
        }
    }
    "baseOutputFilename":"Lalala"
}
```

The following is an example of the response body for the list of updated alert IDs in JSON:

```
{"alertId":[5594,5645]}
```

## Pausing Multiple Alerts

The following method pauses currently scheduled alert execution, also called as disabled in the user interface. Pausing keeps the alert schedule and all other details but prevents the alert from running. It does not delete the alert.

<table>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>POST</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/alerts/pause</span>/</span></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/json</span></p></td>
<td colspan="2"><p>An array or list of alert IDs to pause. See the example below. If the body of the request is empty, or the list is empty, all alerts in the scheduler is paused.</p></td>
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
<td colspan="3"><p>200 OK - The array or list of alerts that were paused. Alerts specified with the <span>&lt;alertID&gt;</span> do not exist and are ignored without any error.</p></td>
<td></td>
</tr>
</tbody>
</table>

The request and the response have the same format, an array, or list of `alertId` elements:

```
{
    "alertsId": [
        5805
    ]
}
```

## Resuming Multiple Alerts

Use the following method to resume all paused alerts. On the resume of an alert any defined trigger that occurs after the time it is resumed causes the report to run again. Missed triggers that occur before the alert is resumed are never run.

<table>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>POST</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/alerts/resume</span>/</span></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/json</span></p></td>
<td colspan="2"><p>An array or list of alert IDs to resume. See the example of request and response below. If the body of the request is empty, or the list is empty, all paused alerts are resumed.</p></td>
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
<td colspan="3"><p>200 OK - The array or list of alerts that were resumed. Alerts specified with the <span>&lt;alertID&gt;</span> do not exist and are ignored without any error.</p></td>
<td></td>
</tr>
</tbody>
</table>

The request and the response have the same format, an array, or list of alertId elements:

```
{
    "alertsId": [
        5805
    ]
}
```

## Restarting Multiple Alerts

Use the following method to rerun failed alerts. For each alert to be restarted, this method creates an immediate single-run copy of the alert, to replace the one that failed. Therefore, all alerts listed in the request body run once immediately after issuing this command. The single-run copies have a misfire policy set so that they do not trigger any further failures (MISFIRE_INSTRUCTION_IGNORE_MISFIRE_POLICY). If the single-run copies fail themselves, no further attempts are made automatically.

<table>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>POST</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/alerts/restart</span>/</span></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/json</span></p></td>
<td colspan="2"><p>An array or list of alert IDs to restart. See the example of request and response below.</p></td>
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
<td colspan="3"><p>200 OK - The array or list of alerts that were restarted.</p></td>
<td></td>
</tr>
</tbody>
</table>

The request and the response have the same format, an array, or list of alertId elements:

```
{
    "alertsId": [
        5805
    ]
}
```

## Deleting Multiple Alerts

Use the DELETE method to remove multiple alerts from the report. The below form deletes multiple alerts.

<table>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>DELETE</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/alerts</span></span></p></td>
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

The following is an example of the request body for deleting an alert in JSON:

```
{
    "alertsId": [
        5330,
        5350
    ]
}
```

The following is an example of the response body for deleting an alert in JSON:

```
{
    "alertsId": [
        5330,
        5350
    ]
}
```
