---
title: The options Service
description: This chapter describes the restv2/reports/options service. Report options are sets of input control values that are saved in the repository. A report option is always associated with a report.
---

# The options Service

This chapter describes the `rest_v2/reports/options` service. Report options are sets of input control values that are saved in the repository. A report option is always associated with a report.

A report option contains input control values that you can read and modify with the inputControls service. Therefore, you should use the methods of the options service to create and list report option resources in the repository, and use the methods of the inputControls service to view and modify the values contained in a report option. For more information, see [The inputControls Service](inputcontrols.md).

This chapter includes the following sections:

-   [Listing Report Options](#listing-report-options)

-   [Creating Report Options](#creating-report-options)

-   [Updating Report Options](#updating-report-options)

-   [Deleting Report Options](#deleting-report-options)

## Listing Report Options

The following method retrieves a list of report options summaries. The summaries give the name of the report options, but not the input control values that are associated with it.

<table>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>GET</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/reports</span>/path/to/report<span>/options</span>/</span></p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p><code>accept: application/json</code></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK - The content is a JSON object that lists the names of the report options for the given report.</p></td>
<td><p>404 Not Found - When the specified report URI is not found in the repository.</p></td>
</tr>
</tbody>
</table>

The body of the response contains the labels of the report options, for example:

``` json
{
  "reportOptionsSummary": [{
    "uri": "/reports/samples/Options",
    "id": "Options",
    "label": "Options"
  },
  {
    "uri": "/reports/samples/Options_2",
    "id": "Options_2",
    "label": "Options 2"
  }]
}
```

## Creating Report Options

The following method creates a report option for a given report. A report option is defined by a set of values for all the report’s input controls.

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
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/reports</span>/path/to/report<span>/options</span>?&lt;arguments&gt;</span></p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><span>label</span></p></td>
<td><p>string</p></td>
<td colspan="2"><p>The name to give the new report option.</p></td>
</tr>
<tr>
<td><p><span>overwrite?</span></p></td>
<td><p>true / false</p></td>
<td colspan="2"><p>If set to true, any report option with the same label is replaced.</p>
<p>If set to false or omitted, any report option with the same label will not be replaced.</p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/json</span></p></td>
<td colspan="2"><p>A JSON object that lists the input control selections. See the example below.</p></td>
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
<td colspan="3"><p>200 OK - The content is a JSON object that describes the new selection of input control values.</p></td>
<td><p>404 Not Found - When the specified report URI is not found in the repository.</p></td>
</tr>
</tbody>
</table>

In this example, we create options for the sample report named Cascading_multi_select_report:

http://&lt;host&gt;:&lt;port&gt;/jasperserver\[-pro\]/rest_v2/reports/reports/samples/Cascading_multi_select_report/options?label=MyReportOption

With the following request body:

``` json
{
   "Country_multi_select":["Mexico"],
   "Cascading_state_multi_select":["Guerrero", "Sinaloa"]
}
```

When successful, the server responds with a JSON object that describes the new report options, for example:

``` json
{
  "uri":"/reports/samples/MyReportOption",
  "id":"MyReportOption",
  "label":"MyReportOption"
}
```

## Updating Report Options

Use the following method to modify the values in a given report option. You can also use the methods of the inputControls service to view and modify the values contained in a report option. For more information, see [The inputControls Service](inputcontrols.md).

<table>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>PUT</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/reports</span>/path/to/report<span>/options</span>/&lt;optionID&gt;/</span></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/json</span></p></td>
<td colspan="2"><p>A JSON object that lists the input control selections. See the example below.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK</p></td>
<td><p>404 Not Found - When the specified report URI is not found in the repository.</p></td>
</tr>
</tbody>
</table>

For example, we change the report option we created in [1.1, “Creating Report Options,” on page 1](#creating-report-options) with the following header:

http://&lt;host&gt;:&lt;port&gt;/jasperserver\[-pro\]/rest_v2/reports/reports/samples/Cascading_multi_select_report/options/MyReportOption

And the following request body:

``` json
{
   "Country_multi_select":["USA"],
   "Cascading_state_multi_select":["CA", "WA"]
}
```

## Deleting Report Options

Use the following method to delete a given report option.

<table>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>DELETE</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/reports</span>/path/to/report<span>/options</span>/&lt;optionID&gt;/</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK</p></td>
<td><p>404 Not Found - When the specified report URI is not found in the repository.</p></td>
</tr>
</tbody>
</table>
