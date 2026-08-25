---
title: The inputControls Service
description: The reportExecutions service includes only a simple mechanism for setting input control (parameters) values in reports. The inputControls service provides a complete set of operations for reading and...
---

# The inputControls Service

The reportExecutions service includes only a simple mechanism for setting input control (parameters) values in reports. The inputControls service provides a complete set of operations for reading and reordering input controls, and for updating input control values. Even though the inputControls service is accessed through a URL that includes rest_v2/reports/\<resourceURI\> /inputControls, the \<resourceURI\> can be any of the following resource types that support input controls:

- `reportUnit`
- `reportOption`
- `adhocDataView`

!!! note

    rest_v2/inputControls is mainly a read-only API (for example, for reading the list of available input controls in a report, getting values of that input control, or selecting certain values from the list of available input controls). Use rest_v2/resources for mapping or updating input controls.

This chapter includes the following sections:

- Listing Input Controls
- Input Control Structure
- Listing Input Control Values
- Changing the Order of Input Controls
- Setting Input Control Values

## Listing Input Controls

The following method returns a description of the structure of the input controls for a given resource. The \<resourceURI\> can be any of the resource types that support input controls (`reportUnit`, `reportOption`, `adhocDataView`).

By default, the inputControls operation returns both the structure and the state of the input controls. The structure of an input control is its name, type, and display characteristics (such as a label). The state of an input control includes both the current value and the list of possible values, if applicable to that type. You can use the structure of each input control to create a UI for your users to enter values. The state of each input control gives you the values to display, such as the values in a dropdown selector.

Some states are small because the input control type is a single text or numeric input, and only the current value is stored. Some states may be quite large if they are a select type (select single or select multiple items) based on a list generated dynamically from your data. For example, a list of customers to select from may contain hundreds or thousands of items. The inputControls operation can take much longer to return on such large input controls that require a query on your datasource. In this case, you can specify the `exclude=state` argument to list only input control structures first. You can request the input control states separately later.

The inputControls service uses either XML or JSON data structures. If no `Accept` header is included, the response is XML by default.

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
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/reports/</span>&lt;resourceURI&gt;<br />
<span>/inputControls</span>?&lt;argument&gt;</span></p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><span>exclude</span></p></td>
<td><p>state</p></td>
<td colspan="2"><p>When specifed as <code>exclude=state</code>, the input control objects in the response contain only the structure elements and none of the state elements. Use this argument if your input controls have large lists of values and may affect performance. You can fetch these values in a separate call, usually after displaying the empty input control UI. See <span>Listing Input Control Values</span>.</p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p><span>accept: application/xml</span> (default)<br />
<span>accept: application/json</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK - The content is a list of XML or JSON objects that describe the structure of all input controls. See examples below.</p>
<p>204 NO CONTENT - The specified &lt;resourceURI&gt; does not have any input controls defined.</p></td>
<td><p>404 Not Found - When the specified &lt;resourceURI&gt; is not found in the repository.</p></td>
</tr>
</tbody>
</table>

The body of the response contains an object defining the structure and optionally the state of the input controls. The following examples show the same input control in both the XML and JSON formats, including values in the state objects:

```
<inputControls>
    <inputControl>
        <description>Country multi select</description>
        <id>Country_multi_select</id>
        <label>Country multi select</label>
        <mandatory>true</mandatory>
        <masterDependencies/>
        <readOnly>false</readOnly>
     <readOnlyExpression>Product>5</readOnlyExpression>
     <visible>true|false</visible>
     <visibilityExpression>Birthdate==DATERANGE('DAY')</visibilityExpression>
        <slaveDependencies>
            <controlId>Cascading_name_single_select</controlId>
            <controlId>Cascading_state_multi_select</controlId>
        </slaveDependencies>
        <state>
            <id>Country_multi_select</id>
            <options>
                <option>
                    <label>Canada</label>
                    <selected>false</selected>
                    <value>Canada</value>
                </option>
                <option>
                    <label>Mexico</label>
                    <selected>false</selected>
                    <value>Mexico</value>
                </option>
                <option>
                    <label>USA</label>
                    <selected>true</selected>
                    <value>USA</value>
                </option>
            </options>
            <uri>/adhoc/topics/Cascading_multi_select_topic_files/Country_multi_select</uri>
        </state>
        <type>multiSelect</type>
        <uri>repo:/adhoc/topics/Cascading_multi_select_topic_files/Country_multi_select</uri>
        <validationRules>
            <mandatoryValidationRule>
                <errorMessage>This field is mandatory so you must enter data.</errorMessage>
            </mandatoryValidationRule>
        </validationRules>
        <visible>true</visible>
    </inputControl>
    ...
    <caseSensitive>true</caseSensitive>
</inputControls>
{
    "inputControl": [
        {
            "id": "Country_multi_select",
            "description": "Country multi select",
            "type": "multiSelect",
            "uri": "repo:/adhoc/topics/Cascading_multi_select_topic_files/Country_multi_select",
            "label": "Country multi select",
            "mandatory": true,
            "readOnly": false,
            "readOnlyExpression":"Product>5",
            "visible": true,
            "visibilityExpression":"Birthdate==DATERANGE('DAY')",
            "masterDependencies": [],
            "slaveDependencies": [
                "Cascading_name_single_select",
                "Cascading_state_multi_select"
            ],
            "validationRules": [
                {
                    "mandatoryValidationRule": {
                        "errorMessage": "This field is mandatory so you must enter data."
                    }
                }
            ],
            "state": {
                "uri": "/adhoc/topics/Cascading_multi_select_topic_files/Country_multi_select",
                "id": "Country_multi_select",
                "options": [
                    {
                        "selected": false,
                        "label": "Canada",
                        "value": "Canada"
                    },
                    {
                        "selected": false,
                        "label": "Mexico",
                        "value": "Mexico"
                    },
                    {
                        "selected": true,
                        "label": "USA",
                        "value": "USA"
                    }
                ]
            }
        },
        ...
    ],
    "caseSensitive": true
}
```

The following example shows two more JSON objects for single value number and date types of input controls. The number data type has limits, in this example 1 ≤ number ≤ 50, that your application should enforce when users input a value. Independently of the input limits, the values of these input controls are used as limits for a comparison filter, for example "store ID that is less than or equal to" or "Opening date after". Note that the type of filter is not reflected in the input control structure other than through a judiciously named label. Your app usually needs to know the structure of a report and the use of its input controls to properly render a UI that reflects the actual filters.

```
{
    "inputControl": [
        {
            "id": "store_id_1",
            "type": "singleValueNumber",
            "uri": "repo:/public/reports/StoreReport_files/store_id_1",
            "label": "Store ID is less than or equal to",
            "mandatory": false,
            "readOnly": false,
        "readOnlyExpression": "Product>5",
            "visible": true,
            "visibilityExpression":"Birthdate==DATERANGE('DAY')",
            "masterDependencies": [],
            "slaveDependencies": [],
            "state": {
                "uri": "/public/reports/StoreReport_files/store_id_1",
                "id": "store_id_1",
                "value": "22"
            },
            "dataType": {
                "type": "number",
                "maxValue": "50",
                "strictMax": false,
                "minValue": "1",
                "strictMin": false
            }
        },
        {
            "id": "first_opened_date_1",
            "type": "singleValueDatetime",
            "uri": "repo:/public/reports/StoreReport_files/first_opened_date_1",
            "label": "Date opened is greater than",
            "mandatory": false,
            "readOnly": false,
        "readOnlyExpression":"Product>5",
            "visible": true,
        "visibilityExpression":"Birthdate==DATERANGE('DAY')",
            "masterDependencies": [],
            "slaveDependencies": [],
        "caseSensitive": false,
            "validationRules": [
                {
                    "dateTimeFormatValidationRule": {
                        "errorMessage": "Specify a valid date/time value.",
                        "format": "yyyy-MM-dd'T'HH:mm:ss"
                    }
                }
            ],
            "state": {
                "uri": "/public/reports/StoreReport_files/first_opened_date_1",
                "id": "first_opened_date_1",
                "value": "1982-01-08T00:00:00"
            },
            "dataType": {
                "type": "datetime",
                "strictMax": false,
                "strictMin": false
            }
        }
    ],
    "caseSensitive": true
}
```

The `inputControl.handler.values.caseSensitive` property defines the `case-sensitive` behavior for input controls. This is defined in the `.../WEB-INF/js.config.properties` configuration file, with a default value True.

## Input Control Structure

The input control objects shown in the examples above contain the information needed by your application to display the input controls to your users and allow them to make a selection. The main elements are:

- ID and URI to define which input control it is.

- Mandatory, visible, and read-only flags to determine whether users should interact with this input control.

- Display characteristics such as a label and description.

- The type of input control, which also determines how it is displayed and how users interact with it, for example text box, checkboxes, radio buttons, or dropdown list. The type is one of the following values:

  <table>
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><span>bool</span> (checkbox)</td>
  <td><span>singleValue</span></td>
  </tr>
  <tr>
  <td><span>singleSelect</span> (dropdown)</td>
  <td><span>singleValueText</span></td>
  </tr>
  <tr>
  <td><span>singleSelectRadio</span></td>
  <td><span>singleValueNumber</span></td>
  </tr>
  <tr>
  <td><span>multiSelectCheckbox</span></td>
  <td><span>singleValueDate</span></td>
  </tr>
  <tr>
  <td rowspan="2"><ul>
  <li><span>multiSelect (list box)</span></li>
  </ul></td>
  <td><span>singleValueDatetime</span></td>
  </tr>
  <tr>
  <td><span>singleValueTime</span></td>
  </tr>
  </tbody>
  </table>

For all of the single-value types in the right-hand column, the structure includes an additional `dataType` object that defines limits on the data type such as `maxValue` or `strictMax`. Your app should interpret these limits and enforce them on the values that users may enter.

The input control structure also includes certain validation rules that depend on the type of input control. The presence of these rules indicates that your client should verify or validate the values it receives from your users. The rules provide messages to display when validation fails. Messages are localized if you have language bundles defined on the server and the authenticated user specifies a locale. In the current release, the following validations are possible:

- mandatoryValidationRule - This input is required (as indicated by `"mandatory": true`), and your client should ensure that the user enters a value.

```
    "mandatoryValidationRule" : {
        "errorMessage" : "This field is mandatory so you must enter data."
    }
```

- dateTimeFormatValidationRule - This input is a date or time value and your client should ensure that the user enters a valid date or time.

```
    "dateTimeFormatValidationRule" : {
        "errorMessage" : "Specify a valid date value.",
        "format" : "yyyy-MM-dd"
    }
```

The input control structure also defines cascading dependencies, if any, between the input controls. The cascading dependencies determine whether a change of values in one input control may change the possible values in another.

- masterDependencies - A list of input control IDs that this input control depends on. If one of these dependencies is modified, your application should fetch the new state of this input control.
- slaveDependencies - A list of input control IDs that depend on this input control. If this input control is modified (given a new value by your user), your application should fetch new state values for these dependencies.

The state object of an input control contains the current and possible values for this input control. The state objects are explained in the next section.

## Listing Input Control Values

The following method returns only the state objects that define the current values of a resource's input controls. The state object includes the possible values of each input control, and among these values, the one that is currently selected. Your app can use these values to generate input and selection widgets in the UI for each input control.

Use this method if you have already fetched all the input control structures using the inputControls method. The \<resourceURI\> can be any of the resource types that support input controls (`reportUnit`, `reportOption`, `adhocDataView`).

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
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/reports/</span>&lt;resourceURI&gt;<br />
<span>/inputControls/values</span>?&lt;argument&gt;</span></p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><span>freshData</span></p></td>
<td><p>true|false</p></td>
<td colspan="2"><p>When <code>freshData=true</code> is specified, the list of values for any selection input controls is refreshed with a database query. When this argument is omitted, its default value is false, and cached values for input controls are returned. Querying the database for thousands of input control list values may impact performance, which is why the server manages a cache of these values.</p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p><span>accept: application/xml</span> (default)<br />
<span>accept: application/json</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK - The content is a list of XML or JSON objects that describe the values of all input controls. See examples below.</p>
<p>204 NO CONTENT - The specified &lt;resourceURI&gt; does not have any input controls defined.</p></td>
<td><p>404 Not Found - When the specified &lt;resourceURI&gt; is not found in the repository.</p></td>
</tr>
</tbody>
</table>

The body of the response contains a list of state objects for all input controls in the given resource. The contents of each state object depend on the type of the input control. Single value types will only have a value that is the current value of the input control. Selection types have a list of options, each with a value and indicator of whether it is currently selected or not.

The following examples show the same state objects in both the XML and JSON formats:

```
<inputControlStateList>
    <inputControlState>
        <id>Country_multi_select</id>
        <options>
            <option>
                <label>Canada</label>
                <selected>false</selected>
                <value>Canada</value>
            </option>
            <option>
                <label>Mexico</label>
                <selected>false</selected>
                <value>Mexico</value>
            </option>
            <option>
                <label>USA</label>
                <selected>true</selected>
                <value>USA</value>
            </option>
        </options>
        <uri>/adhoc/topics/Cascading_multi_select_topic_files/Country_multi_select</uri>
    </inputControlState>
    ...
</inputControlStateList>
{
    "inputControlState": [
        {
            "uri": "/adhoc/topics/Cascading_multi_select_topic_files/Country_multi_select",
            "id": "Country_multi_select",
            "options": [
                {
                    "selected": false,
                    "label": "Canada",
                    "value": "Canada"
                },
                {
                    "selected": false,
                    "label": "Mexico",
                    "value": "Mexico"
                },
                {
                    "selected": true,
                    "label": "USA",
                    "value": "USA"
                }
            ]
        },
        ...
    ]
}
```

!!! note

    If a selection-type input control has a null value, it is given as `~NULL~`. If no selection is made, its value is given as `~NOTHING~`.

The internal structure of the `inputControlState` object in an `inputControls/Values` response is the same as that of a `state` object in an `inputControls` response.

The following example shows two more JSON `inputControlState` objects for single value number and date types of input controls.

```
{
    "inputControlState": [
        {
            "uri": "/public/reports/StoreReport_files/store_id_1",
            "id": "store_id_1",
            "value": "22"
        },
        {
            "uri": "/public/reports/StoreReport_files/first_opened_date_1",
            "id": "first_opened_date_1",
            "value": "1982-01-08T00:00:00"
        }
    ]
}
```

Note that the state objects do not contain the input control type, therefore your app must determine how to read each state object based on the input control structure that it has previously fetched and stored in memory. There are two ways you can match the list of input control values to their previously fetched structure:

- Each state object has the ID and URI of its corresponding input control. The URI of an input control is equivalent to \<resourceURI\>\_files/\<inputControlID\>. Use the ID or URI of each state object to match the ID or URI of each input control structure in your app.
- Input controls are positional: the order of input controls is determined when creating the resource and saved in the resource. All responses from the inputControls methods, both structure and values, contain the complete list of input controls in the same order.

## Changing the Order of Input Controls

You cannot use the inputControls service to modify any input control structures, such as types, labels, visibility, or dependencies, because doing so would break the reports that rely on them. Also, input controls definitions may simply be referenced in a resource and their structure defined in other repository folders. However, you may use the following method to change the order of the input controls.

Changing the order of the input controls is persistent in the parent resource as stored in the repository, but it does not affect the running of a report or their display in a viewer.

Note that if you manage your list of input control structures and states based on the unchanging order of input controls, this operation invalidates your current order in memory. You need to update your list of stored input controls, or use IDs or URIs to match structures and states.

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
<td><p>PUT</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/reports/</span>&lt;resourceURI&gt;<span>/inputControls/</span></span></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/xml</span><br />
<span>application/json</span></p></td>
<td colspan="2"><p>An XML or JSON object that lists the full structure, including the state object, of all input controls in the new order. You cannot modify any fields in the input control structures. They must be sent exactly as received from the <span>inputControls</span> service, except for the order of objects in the list.</p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p><span>accept: application/xml</span> (default)<br />
<span>accept: application/json</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK - The content is an XML or JSON object that lists all input control structures, including their state objects. This should be identical to the content that was sent.</p></td>
<td><p>403 Forbidden - If any input control structure in the request list does not match its current structure.</p>
<p>404 Not Found - When the specified &lt;resourceURI&gt; is not found in the repository.</p></td>
</tr>
</tbody>
</table>

## Setting Input Control Values

After your app has fetched all structures and values and created a UI, you can interact with the input controls and set new values. Use the following methods to send the new values and selections to the server. The server performs validation and returns an error if certain conditions are not satisfied. Before sending new values your application should validate user input in the following ways:

- It must prevent certain input, such as accepting values for a read-only input control or making multiple selections in a single-select input control.
- It should enforce constraints, such as ensuring that a mandatory input control is not null or has at least one selection.
- It should also validate values against any input control limits, such as minimum and maximum values.

After sending new values, use the response to update any changes in selection list values. For example, if you change an input control with cascading dependencies, the server responds with the new selection lists for the dependent input controls. After all new values have been set, you can call the reportExecutions service to run the report again.

There are two forms of this operation, one that returns the full input control structures, and the other that returns only the state values.

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
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/reports/</span>&lt;resourceURI&gt;<br />
<span>/inputControls</span>?&lt;argument&gt;</span></p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><span>freshData</span></p></td>
<td><p>true|false</p></td>
<td colspan="2"><p>When <code>freshData=true</code> is specified, the list of values for any selection input controls is refreshed with a database query. When this argument is omitted, its default value is false, and cached values for input controls are returned. Querying the database for thousands of input control list values may impact performance, which is why the server manages a cache of these values.</p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/xml</span></p></td>
<td colspan="2"><p>An XML object that lists the new value for just those input controls that are modified, for example:</p>
<div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">reportParameters</span>&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">reportParameter</span> <span class="ot">name=</span><span class="st">&quot;Country_multi_select&quot;</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">value</span>&gt;Mexico&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">reportParameter</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>     &lt;<span class="kw">reportParameter</span> <span class="ot">name=</span><span class="st">&quot;Cascading_state_multi_select&quot;</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">value</span>&gt;Guerrero&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">value</span>&gt;Sinaloa&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">reportParameter</span>&gt;</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">reportParameters</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td colspan="2"><p><span>application/json</span></p></td>
<td colspan="2"><p>A JSON object that lists the new value for just those input controls that are modified. In JSON, the value of every input control is given as an array of string values, even for numbers, single-select controls, or multi-select controls with a single value. This example is equivalent to the XML example above:</p>
<div class="sourceCode" id="cb2"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;Country_multi_select&quot;</span><span class="fu">:</span><span class="ot">[</span><span class="st">&quot;Mexico&quot;</span><span class="ot">]</span><span class="fu">,</span></span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;Cascading_state_multi_select&quot;</span><span class="fu">:</span><span class="ot">[</span><span class="st">&quot;Guerrero&quot;</span><span class="ot">,</span> <span class="st">&quot;Sinaloa&quot;</span><span class="ot">]</span></span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p><span>accept: application/xml</span> (default)<br />
<span>accept: application/json</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK - The content is a list of XML or JSON structure objects that describes all input controls and their values, including the newly sent values and any new list values arising from cascading dependencies.</p></td>
<td><p>403 Forbidden - If any input control value in the request list is invalid as determined by its type or limit validation.</p>
<p>404 Not Found - When the specified &lt;resourceURI&gt; is not found in the repository.</p></td>
</tr>
</tbody>
</table>

When sending the values shown in the table above, the JSON response is a list of input control structures that begins with the following element:

```
{
    "inputControl": [
        {
            "id": "Country_multi_select",
            "description": "Country multi select",
            "type": "multiSelect",
            "uri": "repo:/adhoc/topics/Cascading_multi_select_topic_files/Country_multi_select",
            "label": "Country multi select",
            "mandatory": true,
            "readOnly": false,
           "readOnlyExpression":"Product>5",
            "visible": true,
              "visibilityExpression":"Birthdate==DATERANGE('DAY')",
            "masterDependencies": [],
            "slaveDependencies": [
                "Cascading_name_single_select",
                "Cascading_state_multi_select"
            ],
            "validationRules": [
                {
                    "mandatoryValidationRule": {
                        "errorMessage": "This field is mandatory so you must enter data."
                    }
                }
            ],
            "state": {
                "uri": "/adhoc/topics/Cascading_multi_select_topic_files/Country_multi_select",
                "id": "Country_multi_select",
                "options": [
                    {
                        "selected": false,
                        "label": "Canada",
                        "value": "Canada"
                    },
                    {
                        "selected": true,
                        "label": "Mexico",
                        "value": "Mexico"
                    },
                    {
                        "selected": false,
                        "label": "USA",
                        "value": "USA"
                    }
                ]
            }
        },
        ...
    ]
}
```

In the second form, you send the same content in the request, but the URL includes the IDs of the modified input controls and your requested values.

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
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/reports/</span>&lt;resourceURI&gt;<br />
<span>/inputControls/</span>&lt;inputControlid1&gt;;&lt;inputControlid2&gt;;...<span>/values</span>?&lt;argument&gt;</span></p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><span>freshData</span></p></td>
<td><p>true|false</p></td>
<td colspan="2"><p>When <code>freshData=true</code> is specified, the list of values for any selection input controls is refreshed with a database query. When this argument is omitted, its default value is false, and cached values for input controls are returned. Querying the database for thousands of input control list values may impact performance, which is why the server manages a cache of these values.</p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/xml</span></p></td>
<td colspan="2"><p>An XML object that lists the new value for just those input controls that are modified, for example:</p>
<div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">reportParameters</span>&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">reportParameter</span> <span class="ot">name=</span><span class="st">&quot;Country_multi_select&quot;</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">value</span>&gt;Mexico&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">reportParameter</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>     &lt;<span class="kw">reportParameter</span> <span class="ot">name=</span><span class="st">&quot;Cascading_state_multi_select&quot;</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">value</span>&gt;Guerrero&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">value</span>&gt;Sinaloa&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">reportParameter</span>&gt;</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">reportParameters</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td colspan="2"><p><span>application/json</span></p></td>
<td colspan="2"><p>A JSON object that lists the new value for just those input controls that are modified. In JSON, the value of every input control is given as an array of string values, even for numbers, single-select controls, or multi-select controls with a single value. This example is equivalent to the XML example above:</p>
<div class="sourceCode" id="cb2"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;Country_multi_select&quot;</span><span class="fu">:</span><span class="ot">[</span><span class="st">&quot;Mexico&quot;</span><span class="ot">]</span><span class="fu">,</span></span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;Cascading_state_multi_select&quot;</span><span class="fu">:</span><span class="ot">[</span><span class="st">&quot;Guerrero&quot;</span><span class="ot">,</span> <span class="st">&quot;Sinaloa&quot;</span><span class="ot">]</span></span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p><span>accept: application/xml</span> (default)<br />
<span>accept: application/json</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK - The content is a list of XML or JSON state objects of all input control values, including the newly sent values and any new list values arising from cascading dependencies.</p></td>
<td><p>403 Forbidden - f any input control value in the request list is invalid as determined by its type or limit validation.</p>
<p>404 Not Found - When the specified &lt;resourceURI&gt; is not found in the repository.</p></td>
</tr>
</tbody>
</table>

When sending the values shown in the table above, the JSON response is a list of state objects that begins with the following element:

```
{
    "inputControlState": [
        {
            "uri": "/adhoc/topics/Cascading_multi_select_topic_files/Country_multi_select",
            "id": "Country_multi_select",
            "options": [
                {
                    "selected": false,
                    "label": "Canada",
                    "value": "Canada"
                },
                {
                    "selected": true,
                    "label": "Mexico",
                    "value": "Mexico"
                },
                {
                    "selected": false,
                    "label": "USA",
                    "value": "USA"
                }
            ]
        },
        ...
    ]
}
```

### Getting Total Available Values

This method is used to get the total available values and limit the count of the total available values retrieved when input controls are paginated.

Provide inputs for the following fields in the request body:

- Offset - Specify the values to be returned for each input control.
- Limit - Specify the total number of values to be returned for each input control.
- Criteria - Specify the texts or words to be returned for each input control. If specified, then it searches not only for the complete text, but also for the values provided in the texts for the specified criteria. For example, specifying "ry" in the criteria field returns all the values containing "ry" texts.
- Select - This field is newly added. Specify either "selectedValues" or "allValues" in this field.
  - If "selectedValues" is chosen, then the returned available values have the default-selected values.
  - If "allValues" is chosen, then the returned available values have all the values selected.
  - If any other value other than "selectedValues" or "allValues" is provided, then this field is ignored.

!!! note

    If the "values" and "select" field both are provided in the request, then the "select" field with valid values is considered over the "values" field.

Pass the following arguments to get the total available values of the input control based on selected offset, limit, criteria, and select fields.

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
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/reports/</span>{reportUnitURI}<span>/inputControls/values</span>/pagination</p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><span>freshData</span></p></td>
<td><p>true|false</p></td>
<td colspan="2"><p>When <code>freshData=true</code> is specified, then the total count of the list of values for any selected input control is refreshed with the database query.</p>
<p>When <code>freshData=false</code> is specified, then the total cached values for input controls are returned. The default value is false.</p></td>
</tr>
<tr>
<td><span>includeTotalCount</span></td>
<td>true|false</td>
<td colspan="2"><p>When <code>includeTotalCount=true</code> is specified, each <code>inputControlState</code> includes the total count of all the values and not the total number of paginated values.</p>
<p>When <code>includeTotalCount=false</code> is specified, then <code>inputControlState</code>does not include any value in the response. The default value is true.</p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/xml</span></p></td>
<td colspan="2"><p>An XML object that lists the total available values for input control based on modified <span>offset</span>, <span>limit</span>, <span>criteria</span>, and <span>select</span> fields. For example:</p>
<div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">reportParameters</span>&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">reportParameter</span> <span class="ot">name=</span><span class="st">&quot;Country_multi_select&quot;</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">limit</span>&gt;2&lt;/<span class="kw">limit</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">offset</span>&gt;1&lt;/<span class="kw">offset</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">select</span>&gt;selectedValues&lt;/<span class="kw">select</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">reportParameter</span>&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">reportParameter</span> <span class="ot">name=</span><span class="st">&quot;Cascading_name_single_select&quot;</span>&gt;</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">criteria</span>&gt;Adams Construction&lt;/<span class="kw">criteria</span>&gt;</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">select</span>&gt;allValues&lt;/<span class="kw">select</span>&gt;</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">reportParameter</span>&gt;</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">reportParameter</span> <span class="ot">name=</span><span class="st">&quot;Cascading_state_multi_select&quot;</span>&gt;</span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;CA&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">reportParameter</span>&gt;</span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">reportParameters</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td colspan="2"><p><span>application/json</span></p></td>
<td colspan="2"><p>A JSON object that lists the total available values for input control based on modified <span>offset</span>, <span>limit</span>, <span>criteria</span>, and <span>select</span> fields. For example:</p>
<div class="sourceCode" id="cb2"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a> <span class="dt">&quot;reportParameter&quot;</span><span class="fu">:</span> <span class="ot">[</span></span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>   <span class="fu">{</span></span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>     <span class="dt">&quot;name&quot;</span><span class="fu">:</span> <span class="st">&quot;Country_multi_select&quot;</span><span class="fu">,</span></span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>     <span class="dt">&quot;limit&quot;</span><span class="fu">:</span> <span class="dv">2</span><span class="fu">,</span></span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>     <span class="dt">&quot;offset&quot;</span><span class="fu">:</span> <span class="dv">1</span><span class="fu">,</span></span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>     <span class="dt">&quot;select&quot;</span><span class="fu">:</span> <span class="st">&quot;selectedValues&quot;</span></span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span><span class="ot">,</span></span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>   <span class="fu">{</span></span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a>     <span class="dt">&quot;name&quot;</span><span class="fu">:</span> <span class="st">&quot;Cascading_name_single_select&quot;</span><span class="fu">,</span></span>
<span id="cb2-11"><a href="#cb2-11" aria-hidden="true" tabindex="-1"></a>     <span class="dt">&quot;criteria&quot;</span><span class="fu">:</span> <span class="st">&quot;Adams Construction&quot;</span><span class="fu">,</span></span>
<span id="cb2-12"><a href="#cb2-12" aria-hidden="true" tabindex="-1"></a>     <span class="dt">&quot;select&quot;</span><span class="fu">:</span> <span class="st">&quot;allValues&quot;</span></span>
<span id="cb2-13"><a href="#cb2-13" aria-hidden="true" tabindex="-1"></a>    <span class="fu">}</span><span class="ot">,</span></span>
<span id="cb2-14"><a href="#cb2-14" aria-hidden="true" tabindex="-1"></a>   <span class="fu">{</span></span>
<span id="cb2-15"><a href="#cb2-15" aria-hidden="true" tabindex="-1"></a>     <span class="dt">&quot;name&quot;</span><span class="fu">:</span> <span class="st">&quot;Cascading_state_multi_select&quot;</span><span class="fu">,</span></span>
<span id="cb2-16"><a href="#cb2-16" aria-hidden="true" tabindex="-1"></a>     <span class="dt">&quot;value&quot;</span><span class="fu">:</span> <span class="ot">[</span></span>
<span id="cb2-17"><a href="#cb2-17" aria-hidden="true" tabindex="-1"></a>     <span class="st">&quot;CA&quot;</span></span>
<span id="cb2-18"><a href="#cb2-18" aria-hidden="true" tabindex="-1"></a>    <span class="ot">]</span></span>
<span id="cb2-19"><a href="#cb2-19" aria-hidden="true" tabindex="-1"></a>   <span class="fu">}</span></span>
<span id="cb2-20"><a href="#cb2-20" aria-hidden="true" tabindex="-1"></a> <span class="ot">]</span></span>
<span id="cb2-21"><a href="#cb2-21" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p><span>accept: application/xml</span> (default)<br />
<span>accept: application/json</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK–The content is a list of XML or JSON state objects of total available values of input control.</p></td>
<td><p>500 Unexpected Error–An unexpected error occurs while passing any incorrect value.</p>
<p>400 Serialization Error–An error occurs determined by its type. This issue occurs on sending a malformed or wrong XML/JSON object in the request. For example, missing an open/closed tag or a completely wrong object representation that does not match an example object.</p>
<p>400 Out of range Error–An error occurs when the limit or offset for the input control is specified out of range.</p></td>
</tr>
</tbody>
</table>

When sending the values shown in the table above, the JSON response has the total available values but the number of values are limited based on the offset, limit, and search criteria.

```
{
  "inputControlState": [
    {
      "uri": "/organizations/organization_1/adhoc/topics/Cascading_multi_select_topic_files/Country_multi_select",
      "id": "Country_multi_select",
      "totalCount": "4",
      "options": [
       {
         "selected": false,
         "label": "Mexico",
         "value": "Mexico"
       },
       {
         "selected": true,
         "label": "USA",
         "value": "USA"
       }
      ]
    },
    {
       "uri": "/organizations/organization_1/adhoc/topics/Cascading_multi_select_topic_files/Cascading_state_multi_select",
       "id": "Cascading_state_multi_select",
       "totalCount": "3",
       "options": [
         {
           "selected": true,
           "label": "USA | CA",
           "value": "CA"
         },
         {
           "selected": false,
           "label": "USA | OR",
           "value": "OR"
         },
         {
          "selected": false,
          "label": "USA | WA",
          "value": "WA"
         }
       ]
     },
     {
       "uri": "/organizations/organization_1/adhoc/topics/Cascading_multi_select_topic_files/Cascading_name_single_select",
       "id": "Cascading_name_single_select",
       "totalCount": "2",
       "options": [
          {
            "selected": true,
            "label": "Steelman-Adams Construction Partners",
            "value": "Steelman-Adams Construction Partners"
          },
          {
            "selected": true,
            "label": "Winter-Adams Construction Associates",
            "value": "Winter-Adams Construction Associates"
          }
        ]
      }
   ]
}
```

### Getting Default Selected Values

This method is used to get the default selected values when the input controls are paginated. For example, when a Report, Scheduler, or Dashboard is initially loaded, the input controls API excludes only the values defined in the "state" to avoid the values to be included in the response.

Pass the following arguments to get only the default-selected values of the input control field in the response.

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
<td colspan="3"><p>../rest_v2/reports/{reportUnitURI}/inputControls/selectedValues</p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><span>freshData</span></p></td>
<td><p>true|false</p></td>
<td colspan="2"><p>When <code>freshData=true</code> is specified, the total count of the list of selected values of input controls is refreshed with a database query.</p>
<p>When <code>freshData=false</code> is specified, the total count of cached values for input controls are returned. The default value is false.</p></td>
</tr>
<tr>
<td><span>withLabel</span></td>
<td>true|false</td>
<td colspan="2"><p>When <code>withLabel = true</code> is specified, the returned options field for each input control has a label field along with the value. In this process, an additional overhead is required to fetch labels from the DB/cache.</p>
<p>When <code>withLabel = false</code> is specified, the returned options field for each input control does not include any label field.</p>
<p>In this process, values are the default values and they are fetched from JRXML. The default value is true.</p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p><span>accept: application/xml</span> (default)<br />
<span>accept: application/json</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK–The content is a list of XML or JSON state objects of default-selected values of input control.</p></td>
<td><p>500 Unexpected Error–An unexpected error that has occurred while passing any value.</p>
<p>400 Serialization Error–An error occurs determined by its type. This issue occurs on sending a malformed or wrong XML/JSON object in the request. For example, missing an open/closed tag or a completely wrong object representation that does not match an example object.</p>
<p>400 Out of range Error–An error occurs when the limit or offset for the input control is specified out of range.</p></td>
</tr>
</tbody>
</table>

The following example shows a simple use of the `select` field in JSON:

```
{

    "selectedValue": [

        {
            "id": "Country_multi_select",

            "options": [
                {
                    "label": "USA",

                    "value": "USA"
                }
            ]
        },

        {
            "id": "Cascading_state_multi_select",

            "options": [

               {
                    "label": "USA | CA",

                    "value": "CA"
                }
            ]
        },

        {
            "id": "Cascading_name_single_select",

            "options": [
                {
                    "label": "A & U Stalker Telecommunications, Inc",
                    "value": "A & U Stalker Telecommunications, Inc"
                }
            ]
        }
    ]
}
```

The following example shows a simple use of the `select` field in XML:

```
<selectedValues>

    <selectedValue id="Country_multi_select">
        <options>
            <label>USA</label>

            <value>USA</value>

        </options>
    </selectedValue>

    <selectedValue id="Cascading_state_multi_select">
        <options>
            <label>USA | CA</label>
            <value>CA</value>
        </options>

    </selectedValue>

    <selectedValue id="Cascading_name_single_select">

        <options>
            <label>A & U Stalker Telecommunications, Inc</label>
            <value>A & U Stalker Telecommunications, Inc</value>

        </options>
    </selectedValue>
</selectedValues>
```
