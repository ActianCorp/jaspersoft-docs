---
title: JSON Descriptor Format for User Interface Components
description: Jaspersoft Studio has a JSON descriptor format that allows you to register components with Jaspersoft Studio and optionally create a specialized UI for the component. This framework is used to add...
---

# 1.1 JSON Descriptor Format for User Interface Components

Jaspersoft Studio has a JSON descriptor format that allows you to register components with Jaspersoft Studio and optionally create a specialized UI for the component. This framework is used to add custom visualizations components and JFreeChart customizers. Pre-installed samples that implement the descriptor format are available for added in CVCs and chart customizers.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th>Property Name</th>
<th>Default</th>
<th>Mandatory</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<th colspan="4"><p>Shared properties for all component types</p></th>
</tr>
&#10;<tr>
<td>label</td>
<td>-</td>
<td>Mandatory</td>
<td>Name of the component shown in dialog boxes.</td>
</tr>
<tr>
<td>description</td>
<td>-</td>
<td>Optional</td>
<td>A short description of the component; shown as a tooltip in the component chooser dialog when a user creates an instance of the component.</td>
</tr>
<tr>
<td colspan="4">Properties specific to CVCs</td>
</tr>
<tr>
<td>module</td>
<td>-</td>
<td>Mandatory</td>
<td>(Read-only) Name of the RequireJS module implemented by the minified JavaScript. Must be unique across your installed CVCs.</td>
</tr>
<tr>
<td>thumbnail</td>
<td>-</td>
<td>Optional</td>
<td>A PNG used in the component chooser dialog; you can optionally configure your component to use this for the preview of the component in design view.</td>
</tr>
<tr>
<td>ui</td>
<td>-</td>
<td>Optional</td>
<td>A nested descriptor of the properties and dataset required by this component</td>
</tr>
<tr>
<td>css</td>
<td>-</td>
<td>Optional</td>
<td>Optional css file reference (copied inside the report directory when the component is created with a wizard).</td>
</tr>
<tr>
<td>script</td>
<td>-</td>
<td>Mandatory</td>
<td>JavaScript reference copied inside the report directory when the component is created with a wizard).</td>
</tr>
<tr>
<td colspan="4">Properties specific to chart customizers</td>
</tr>
<tr>
<td>customizerClass</td>
<td>-</td>
<td>Mandatory</td>
<td>(Read only) Full name of the Java customizer class.</td>
</tr>
<tr>
<td rowspan="2">supportedPlot</td>
<td>-</td>
<td> </td>
<td>Array of chart types supported by the customizer. Chart types are designated by a numeric code, shown in the following table.</td>
</tr>
<tr>
<td colspan="3"><table>
<caption><p><em>Table 1-1 Chart Codes for supportedPlot in JSON Files</em></p></caption>
<thead>
<tr>
<th>Chart Type</th>
<th>Code in JasperReports</th>
</tr>
</thead>
<tbody>
<tr>
<td>CHART_TYPE_AREA</td>
<td>1</td>
</tr>
<tr>
<td>CHART_TYPE_BAR3D</td>
<td>2</td>
</tr>
<tr>
<td>CHART_TYPE_BAR</td>
<td>3</td>
</tr>
<tr>
<td>CHART_TYPE_BUBBLE</td>
<td>4</td>
</tr>
<tr>
<td>CHART_TYPE_CANDLESTICK</td>
<td>5</td>
</tr>
<tr>
<td>CHART_TYPE_HIGHLOW</td>
<td>6</td>
</tr>
<tr>
<td>CHART_TYPE_LINE</td>
<td>7</td>
</tr>
<tr>
<td>CHART_TYPE_PIE3D</td>
<td>8</td>
</tr>
<tr>
<td>CHART_TYPE_PIE</td>
<td>9</td>
</tr>
<tr>
<td>CHART_TYPE_SCATTER</td>
<td>10</td>
</tr>
<tr>
<td>CHART_TYPE_STACKEDBAR3D</td>
<td>11</td>
</tr>
<tr>
<td>CHART_TYPE_STACKEDBAR</td>
<td>12</td>
</tr>
<tr>
<td>CHART_TYPE_XYAREA</td>
<td>13</td>
</tr>
<tr>
<td>CHART_TYPE_XYBAR</td>
<td>14</td>
</tr>
<tr>
<td>CHART_TYPE_XYLINE</td>
<td>15</td>
</tr>
<tr>
<td>CHART_TYPE_TIMESERIES</td>
<td>16</td>
</tr>
<tr>
<td>CHART_TYPE_METER</td>
<td>17</td>
</tr>
<tr>
<td>CHART_TYPE_THERMOMETER</td>
<td>18</td>
</tr>
<tr>
<td>CHART_TYPE_MULTI_AXIS</td>
<td>19</td>
</tr>
<tr>
<td>CHART_TYPE_STACKEDAREA</td>
<td>20</td>
</tr>
<tr>
<td>CHART_TYPE_GANTT</td>
<td>21</td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

The JavaScript, CSS, and module properties are shown on Data tab of the Properties view for your component in Jaspersoft Studio. You can use additional properties in the JSON file to define additional UI, in the form of a set of input fields (text, numbers, combo box, etc...), and an optional list of datasets that can be used by the component implementation. The values entered by the user in the UI are passed to the JavaScript file specified in the script member.

|  |  |  |  |
|----|----|----|----|
| Property name | Default | Mandatory | Description |
| sections | \- | Optional | List of available sections which collects properties, in addition to js, css, and module properties, which are always present and, if we manage the custom ui, presented as read only. |

The expandable attribute is not used in the context of customizer, it is used when sections are created and they can be collapsed or expanded (you can see this in the custom visualization component). Also the read only attribute has no much sense with the customizer, it is used to define a widget that can show the value of the property but the user is not able to edit it. Also this is used in the CVC component.

resource, references required assets (such as a JavaScript file), and optionally defines a UI.
