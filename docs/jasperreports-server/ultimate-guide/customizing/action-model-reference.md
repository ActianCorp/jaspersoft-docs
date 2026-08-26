---
title: Action Model Reference
description: "The action model is a complex mechanism for generating menus dynamically. In particular, menus in Ad Hoc must be generated programmatically based on the contents of the reports, for example the..."
---

# Action Model Reference

The action model is a complex mechanism for generating menus dynamically. In particular, menus in Ad Hoc must be generated programmatically based on the contents of the reports, for example the context menu on a column. The following high-level steps explain how menus are generated:

When generating menus, the Ad Hoc Editor follows these steps:

1.  Whenever a page with menus is to be displayed for the first time, the server looks up the corresponding action model XML definition and uses JDOM (Java-based Document Object Model for XML) to build and cache a Document.
2.  Subsequent viewings reference the cached Document.
3.  After the page is modified (usually triggered by an Ajax Request) the server generates a client side action model in the form of a JSON expression. Based on the current page state, the client model is a filtered version of the full action model in which internationalized names and generated options are resolved, and so forth.
4.  Every time a menu is requested on the client, the server looks up the context in the JSON model, and for each action, clones the appropriate HTML template for the menu and tweaks its attributes accordingly.

!!! note

    Some pages have mostly static menus that don’t change based on page contents. Other pages, such as the Ad Hoc Editor, have dynamic menus that are updated in this way in response to changes the user makes on a page.

The following sections document the XML elements used in the action model definition files. In particular, you can define various conditions at several levels so menus appear only to certain users or based on the current state of the page.

## Context

Each context represents a distinct menu type and refers to the part of the design page that launches that menu. Examples are `reportLevel`, `columnLevel`, `fieldLevel`. They're directly equivalent to the menu levels defined in the popup-style JSP files used in previous releases.

## Condition

A condition element invokes the specified server side test as a method on the view model. The enclosed actions are included in the client action model only if the test returns true.

If the test has a leading exclamation point (!), the condition tests for false:

-   `test`: The name of the java method to be invoked on the view model.
-   `testArgs`: Array of parameters to be passed to the above test, expressed as a comma-separated string.

## Actions

Each defined action produces one or more rows in the generated menu. The following tables describe the several action types.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th colspan="2"><p><code>simpleAction</code></p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p>A standalone menu action that, when clicked, fires the specified JavaScript method.</p></td>
</tr>
<tr>
<td colspan="2"><p>Attributes</p></td>
</tr>
<tr>
<td><p><code>id</code></p></td>
<td><p>The ID of the menu row DOM object.</p></td>
</tr>
<tr>
<td><p><code>disabled</code></p></td>
<td><p>If set to <code>true</code>, disable this row initially (shows a gray block instead).</p></td>
</tr>
<tr>
<td><p><code>labelKey</code></p></td>
<td><p>The text the menu should display. If it corresponds to an localization bundle key it is translated, otherwise it is displayed as is.</p></td>
</tr>
<tr>
<td><p><code>labelCondition</code></p></td>
<td><p>Sometimes the label value is contingent on the current state. The label condition references a Java method on the view model and should return a Boolean. A <code>labelCondition</code> defines two <code>labelOption</code> sub elements (see below).</p></td>
</tr>
<tr>
<td><p><code>clientTest</code></p></td>
<td><p>Only generate a row for this action if it passes the specified JavaScript method.</p>
<p>If the <code>clientTest</code> has a leading exclamation point (!), tests for false.</p></td>
</tr>
<tr>
<td><p><code>clientTestArgs</code></p></td>
<td><p>An array of parameters pass to the above test, expressed as a comma delimited string.</p></td>
</tr>
<tr>
<td><p><code>action</code></p></td>
<td><p>The JavaScript method to be fired when the action is taken.</p></td>
</tr>
<tr>
<td><p><code>actionArgs</code></p></td>
<td><p>An array of parameters to be passed to the above test, expressed as a string delimited by the @@ string constant.</p></td>
</tr>
<tr>
<td><p><code>leaveMenuOpen</code></p></td>
<td><p>If true the menu stays displayed after action.</p></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th colspan="2"><p><span>separator</span></p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p>Not strictly an action. Outputs a separator bar. The style of the bar automatically adjusts to the current nesting level.</p></td>
</tr>
<tr>
<td colspan="2"><p>Attributes</p></td>
</tr>
<tr>
<td><p><code>attributesclientTest</code></p></td>
<td><p>Only generate a row for this action if it passes the specified JavaScript method.</p></td>
</tr>
<tr>
<td><p><code>clientTestArgs</code></p></td>
<td><p>An array of parameters to be passed to the above test, expressed as a string delimited by the @@ string constant.</p></td>
</tr>
<tr>
<td><p><code>disabled</code></p></td>
<td><p>Disable this row initially (shows a gray block instead).</p></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th colspan="2"><p><span>selectAction</span></p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p>A drop down (roll down) parent. Selectors can be nested up to three levels deep. The menu automatically renders the roll-downs in a nested fashion.</p></td>
</tr>
<tr>
<td colspan="2"><p>Attributes</p></td>
</tr>
<tr>
<td><p><code>attributesdisabled</code></p></td>
<td><p>If set to <code>true</code>, disable this row initially (shows a gray block instead).</p></td>
</tr>
<tr>
<td><p><code>opened</code></p></td>
<td><p>If set to <code>true</code>, selector is opened initially.</p></td>
</tr>
<tr>
<td><p><code>labelKey</code></p></td>
<td><p>The text for the menu to display. If it corresponds to an localization bundle key it is translated, otherwise it is displayed as is.</p></td>
</tr>
<tr>
<td><p><code>labelCondition</code></p></td>
<td><p>Sometimes the label value is contingent on the current state. The label condition references a java method on the view model and should return a Boolean. A <code>labelCondition</code> defines two <code>labelOption</code> sub elements (see below).</p></td>
</tr>
<tr>
<td><p><code>clientTest</code></p></td>
<td><p>Only generate a row for this action if it passes the specified JavaScript method.</p></td>
</tr>
<tr>
<td><p><code>clientTestArgs</code></p></td>
<td><p>An array of parameters to be passed to the above test, expressed as a string delimited by the @@ string constant.</p></td>
</tr>
</tbody>
</table>

## Options

Some actions can have child elements, as described in the following tables.

<table>
<thead>
<tr>
<th colspan="2"><p><span>option</span></p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p>Child of <code>selectAction</code>. Defines a static menu option. Use this when you can't define options programmatically.</p></td>
</tr>
<tr>
<td colspan="2"><p>Attributes</p></td>
</tr>
<tr>
<td><p><code>id</code></p></td>
<td><p>The ID of the menu row DOM object.</p></td>
</tr>
<tr>
<td><p><code>disabled</code></p></td>
<td><p>If set to <code>true</code>, disable this row initially (shows a gray block instead).</p></td>
</tr>
<tr>
<td><p><code>button</code></p></td>
<td><p>If set to <code>true</code> the option displayed as a button (as in formula builder).</p></td>
</tr>
<tr>
<td><p><code>labelKey</code></p></td>
<td><p>The text for the menu to display. If it corresponds to an localization bundle key it is translated, otherwise it is displayed as is.</p></td>
</tr>
<tr>
<td><p><code>labelCondition</code></p></td>
<td><p>Sometimes the label value is contingent on the current state. The label condition references a java method on the view model and should return a Boolean. A <code>labelCondition</code> defines two <code>labelOption</code> sub elements (see below).</p></td>
</tr>
<tr>
<td><p><code>clientTest</code></p></td>
<td><p>Only generate a row for this action if it passes the specified JavaScript method.</p></td>
</tr>
<tr>
<td><p><code>clientTestArgs</code></p></td>
<td><p>An array of parameters to be passed to the above test, expressed as a comma delimited string.</p></td>
</tr>
<tr>
<td><p><code>allowsInputTest</code></p></td>
<td><p>Show an input box in this option if it passes the specified JavaScript method.</p></td>
</tr>
<tr>
<td><p><code>allowsInputTestArgs</code></p></td>
<td><p>An array of parameters to be passed to the above test, expressed as a string delimited by the @@ string constant.</p></td>
</tr>
<tr>
<td><p><code>action</code></p></td>
<td><p>The JavaScript method to be fired when the action is taken.</p></td>
</tr>
<tr>
<td><p><code>actionArgs</code></p></td>
<td><p>An array of parameters to be passed to the above test, expressed as a comma delimited string.</p></td>
</tr>
<tr>
<td><p><code>isSelectedTest</code></p></td>
<td><p>Indicate a check mark next to this option if it passes the specified JavaScript method.</p></td>
</tr>
<tr>
<td><p><code>isSelectedTestArgs</code></p></td>
<td><p>An array of parameters to be passed to the above test, expressed as a string delimited by the @@ string constant.</p></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th colspan="2"><p><span>generatedOptions</span></p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p>Child of <code>selectAction</code>. Defines a set of dynamically-defined options.</p></td>
</tr>
<tr>
<td colspan="2"><p>Reserved Variables (in addition to standard reserved variables)</p></td>
</tr>
<tr>
<td><p><code>${optionId}</code></p></td>
<td><p>Programmatically assigned ID. If function returns a Map this is the key part of each key-value pair, if it returns a Collection it is the <code>toString</code> value of each element.</p></td>
</tr>
<tr>
<td><p><code>${optionValue}</code></p></td>
<td><p>Programmatically assigned display value. If function returns a Map this is the value part of each key-value pair, if it returns a Collection it is the <code>toString</code> value of each element.</p></td>
</tr>
<tr>
<td><p><code>$R{&lt;String&gt;}</code></p></td>
<td><p>When used in a label expression attempts to internationalize the enclosed String and if it fails it returns the literal value.</p></td>
</tr>
<tr>
<td colspan="2"><p>Attributes</p></td>
</tr>
<tr>
<td><p><code>id</code></p></td>
<td><p>The ID of the menu row DOM object.</p></td>
</tr>
<tr>
<td><p><code>function</code></p></td>
<td><p>The name of the java method to invoke on the view model that is used to generate the options. The function can return either a Map or a Collection. The type of object returned affects how the <code>${optionValue}</code> and <code>${optionId}</code> reserved variables are interpreted (see above).</p></td>
</tr>
<tr>
<td><p><code>functionArgs</code></p></td>
<td><p>An array of parameters to pass to the above test, expressed as a string delimited by the @@ string constant.</p></td>
</tr>
<tr>
<td><p><code>labelKey</code></p></td>
<td><p>The text for the menu to display. If it corresponds to an localization bundle key it is translated, otherwise it is displayed as is.</p></td>
</tr>
<tr>
<td><p><code>labelCondition</code></p></td>
<td><p>Sometimes the label value is contingent on the current state. The label condition references a java method on the view model and should return a Boolean. A <code>labelCondition</code> defines two <code>labelOption</code> sub elements (see below).</p></td>
</tr>
<tr>
<td><p><code>labelExpression</code></p></td>
<td><p>Allows a custom label to be defined and allows full use of all reserved variables. (for example, <code>labelExpression="${optionValue}") $R{ADH_252_DATA_ROWS}"</code>).</p></td>
</tr>
<tr>
<td><p><code>clientTest</code></p></td>
<td><p>Only generate a row for this action if it passes the specified JavaScript method.</p></td>
</tr>
<tr>
<td><p><code>clientTestArgs</code></p></td>
<td><p>An array of parameters to be passed to the above test, expressed as a string delimited by the @@ string constant. If no actionArgs are specified, the ${optionId} variable is automatically assigned as an argument.</p></td>
</tr>
<tr>
<td><p><code>allowsInputTest</code></p></td>
<td><p>Show an input box in this option if it passes the specified JavaScript method.</p></td>
</tr>
<tr>
<td><p><code>allowsInputTestArgs</code></p></td>
<td><p>An array of parameters to be passed to the above test, expressed as a string delimited by the @@ string constant. If no actionArgs are specified, the ${optionId} variable is automatically assigned as an argument.</p></td>
</tr>
<tr>
<td><p><code>action</code></p></td>
<td><p>The JavaScript method to be fired when the action is taken.</p></td>
</tr>
<tr>
<td><p><code>actionArgs</code></p></td>
<td><p>An array of parameters to be passed to the above test, expressed as a comma delimited string. If no actionArgs are specified, the ${optionId} variable is automatically be assigned as an argument.</p></td>
</tr>
<tr>
<td><p><code>leaveMenuOpen</code></p></td>
<td><p>If true the menu stays displayed after action (for all generated options).</p></td>
</tr>
<tr>
<td><p><code>isSelectedTest</code></p></td>
<td><p>Indicate a check mark next to this option if it passes the specified JavaScript method.</p></td>
</tr>
<tr>
<td><p><code>isSelectedTestArgs</code></p></td>
<td><p>An array of parameters to be passed to the above test, expressed as a string delimited by the @@ string constant. If no actionArgs are specified, the ${optionId} variable is automatically assigned as an argument.</p></td>
</tr>
<tr>
<td colspan="2"><p>Default Settings (DOM attributes set automatically on each generated Option)</p></td>
</tr>
<tr>
<td><p><code>id</code></p></td>
<td><p>If not specified as an a attribute defaults to the ${optionId} variable.</p></td>
</tr>
<tr>
<td><p><code>clientTestArgs</code></p></td>
<td><p>If not specified as an a attribute defaults to the ${optionId} variable.</p></td>
</tr>
<tr>
<td><p><code>actionArgs</code></p></td>
<td><p>If not specified as an a attribute defaults to the ${optionId} variable.</p></td>
</tr>
<tr>
<td><p><code>isSelectedArgs</code></p></td>
<td><p>If not specified as an a attribute defaults to the ${optionId} variable.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th colspan="2"><p><span>labelOption</span></p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p>Child of <code>labelFunction</code>. Every <code>labelFunction</code> element should have two <code>labelOption</code> elements as children. One of them is used to define the action label depending on the result of the <code>labelCondition</code>.</p></td>
</tr>
<tr>
<td colspan="2"><p>Attributes</p></td>
</tr>
<tr>
<td><p><code>attributesfunction</code><br />
<code>Response</code></p></td>
<td><p>A Boolean string. If the parent <code>labelCondition</code> result matches this Boolean value, this <code>labelOption</code> is used.</p></td>
</tr>
<tr>
<td><p><code>labelKey</code></p></td>
<td><p>The text for the menu to display. If it corresponds to an localization bundle key it is translated, otherwise it is displayed as <code>isgenerateFromTemplate</code>.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th colspan="2"><p><span>generateFromTemplate</span></p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p>Programmatically generates multiple actions by specifying a function to iterate over the enclosed template. The template can be any valid action structure, it can include multiple actions and/or nested actions.</p></td>
</tr>
<tr>
<td colspan="2"><p>Reserved Variables (in addition to standard reserved variables)</p></td>
</tr>
<tr>
<td><p><code>${templateInjection</code><br />
<code>Index}</code></p></td>
<td><p>The zero-based index of the current iteration.</p></td>
</tr>
<tr>
<td><p><code>${templateInjection</code><br />
<code>Id}</code></p></td>
<td><p>Programmatically assigned ID. If function returns a Map this is the key part of each key-value pair, if it returns a Collection it is the <code>toString</code> value of each element.</p></td>
</tr>
<tr>
<td><p><code>${templateInjection</code><br />
<code>Value}</code></p></td>
<td><p>Programmatically assigned value. If function returns a Map this is the value part of each key-value pair, if it returns a Collection it is the <code>toString</code> value of each element.</p></td>
</tr>
<tr>
<td colspan="2"><p>Attributes</p></td>
</tr>
<tr>
<td><p><code>function</code></p></td>
<td><p>The name of the java method to be invoked on the view model that is used as the template iterator. The function can return either a Map or a Collection. The type of object returned affects how the reserved variables <code>${templateInjectionId}</code> and <code>${templateInjectionValue}</code> are interpreted (see above).</p></td>
</tr>
<tr>
<td><p><code>functionArgs</code></p></td>
<td><p>An array of parameters to be passed to the above test, expressed as a string delimited by the @@ string constant.</p></td>
</tr>
<tr>
<td colspan="2"><p>Child Elements</p></td>
</tr>
<tr>
<td colspan="2"><p>Any valid action structure, which is used as the template.</p></td>
</tr>
</tbody>
</table>

## Special Expressions

The following special expressions are converted to built-in variable values when used as arguments for client functions:

| Expression    | Definition                                              |
|---------------|---------------------------------------------------------|
| `${selected}` | The JavaScript array of selected objects on the client. |
| `${event}`    | The JavaScript event object.                            |
| `${label}`    | The generated label for this menu.                      |

## Menu DHTML API

This is a set of JavaScript functions defined on actionModel.js to dynamically manipulate a menu’s look and feel after it's been displayed. You can use them to change the Ad Hoc Editor menus in run-time. Most of them take the `menuRow` or the `menuRow`’s identifier as arguments. Some have additional arguments as well. For more information about the additional arguments, refer to the code itself.

| Function             | Description                                       |
|----------------------|---------------------------------------------------|
| `hideInputForOption` | Hide the input box on the option.                 |
| `showInputForOption` | Show the input box on the option.                 |
| `setRowColor`        | Set the `backgroundColor` to the specified color. |
| `resetRowColor`      | Restore original background color.                |
| `getLabel`           | Return the current label for this row.            |
| `setLabel`           | Set the label for this row.                       |
| `disableRow`         | Grey out the row.                                 |
| `enableRow`          | Restore the row to active state.                  |
