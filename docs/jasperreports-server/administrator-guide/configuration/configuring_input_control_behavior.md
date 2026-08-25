---
title: Configuring Input Control Behavior
description: "When defining text input controls, the default server behavior allows empty strings, even if you have configured a regular expression and made the input control mandatory. Use this setting to enforce..."
---

# Configuring Input Control Behavior

When defining text input controls, the default server behavior allows empty strings, even if you have configured a regular expression and made the input control mandatory. Use this setting to enforce the regular expression even on empty strings. This forces the user to provide a conforming value for the input control.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>Input Control Behavior</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>.../WEB-INF/applicationContext-cascade.xml</code></p></td>
</tr>
<tr>
<td><p>Bean</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><code>applyRegexpToEmptyString</code></p></td>
<td colspan="2"><p>The default value of <code>false</code> gives the traditional behavior: even if a regular expression is defined, it is not applied to empty strings.</p>
<p>If you want to strictly enforce the regular expression, even on empty input strings, set this property to <code>true</code>.</p></td>
</tr>
</tbody>
</table>

You can also configure the default value that appears in each type of input control. This is the value that is displayed when the input control is not given any value. By default, the display value is `~NULL~`.

Edit the file `.../WEB-INF/applicationContext-cascade.xml` to change the following entries. The examples in comments show how you can use the default value to suggest a pattern for the input. To make an input control appear blank when no value is given, set `value=""` (an empty string).

``` xml
<util:map id="globalDefaultValues" value-type="java.lang.String" key-type="java.lang.Byte">
    <!-- if DataType isn't defined-->
    <entry key="-1" value="~NULL~"></entry>
    <!--TYPE_TEXT = 1-->
    <!--<entry key="1" value="Enter value"></entry>-->
    <entry key="1" value="~NULL~"></entry>
    <!--TYPE_NUMBER = 2-->
    <!--<entry key="2" value="0"></entry>-->
    <entry key="2" value="~NULL~"></entry>
    <!--TYPE_DATE = 3-->
    <!--<entry key="3" value="2020-03-12"></entry>-->
    <entry key="3" value="~NULL~"></entry>
    <!--TYPE_DATE_TIME = 4-->
    <!--<entry key="4" value="2015-09-22T05:26:16"></entry>-->
    <entry key="4" value="~NULL~"></entry>
    <!--TYPE_TIME = 5-->
    <!--<entry key="5" value="13:37:54"></entry>-->
    <entry key="5" value="~NULL~"></entry>
</util:map>
```

Configuring Case Sensitivity

You can configure the following property to turn on/off the case sensitivity for input control behavior.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>Configuring the Case Sensitivity for Input Control Behavior</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>.../WEB-INF/js.config.properties</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><code>inputControl.handler.values.caseSensitive</code></p></td>
<td colspan="2"><p>This property is used to set input control or filter values to case insensitivity for case-insensitive databases.</p>
<p>By default, the value is <code>inputControl.handler.values.caseSensitive=true</code>. You can set this property to <code>false</code> to ignore case sensitivity.</p>
<p>When set to <code>false</code>, the parameters or input controls validator becomes case insensitive.</p>
<p>For example, if <code>inputControl.handler.values.caseSensitive=true</code> providing <code>country="usa"</code> triggers a validation exception.</p>
<p>However, if <code>inputControl.handler.values.caseSensitive=false</code></p>
<p>providing any of the following values is acceptable:</p>
<ul>
<li><code>country="USA"</code></li>
<li><code>country="UsA"</code></li>
<li><code>country="usa"</code></li>
</ul></td>
</tr>
</tbody>
</table>

!!! note

    The parameter `caseSensitive` is also added to the existing JSON model for ExistingFilters (DynamicFilterObject) in Crosstab/Table Model.

Configuring Input Control Optimization for Select All

To optimize input control behavior for Ad Hoc report, Studio Report, Ad Hoc and Report dashlet, when all available values are selected using Select All button:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>Configuring the Input Control Optimization for Select All</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>applicationContext.xml</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><code>inputControlOptimizationForSelectAll</code></p></td>
<td colspan="2"><p>When<code> inputControlOptimizationForSelectAll</code> flag is set to<code> true</code> and user has large number of available values in input control dialog and all values are selected using selectAll button then query will be optimized by using 1=1 clause instead of sending all values in IN clause.</p>
<p>When <code>inputControlOptimizationForSelectAll</code> is set to <code>false</code>, query is not optimized and all values are sent in IN clause.</p></td>
</tr>
</tbody>
</table>

!!! note

    This behavior is applicable exclusively to Multi-select Input Controls.<br>
    Reports having cascading Input control is not affected with this property, i.e. query won't be optimized for these reports.
