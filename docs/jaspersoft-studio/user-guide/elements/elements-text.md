---
title: Text Elements
description: "Two elements are specifically designed to display text in a report: static text and text field. Static text is used for creating labels or printing static text set at design time that is not meant to..."
---

# Text Elements

Two elements are specifically designed to display text in a report: static text and text field. Static text is used for creating labels or printing static text set at design time that is not meant to change when the report is generated. That said, in some cases you still use a text field to print labels too, since the nature of the static text elements prevents the ability to display text dynamically translated in different languages when the report is run with a specific locale and it is configured to use a resource bundle using the JasperReports internationalization capabilities.

A text field is similar to a static text string, but the content (the text in the field) is provided using an expression (which can be a simple static text string itself). That expression can return several kinds of value types, allowing the user to specify a pattern to format that value. Since the text specified dynamically can have an arbitrary length, a text field provides several options about how the text must be treated regarding alignment, position, line breaks and so on. Optionally, the text field is able to grow vertically to fit the content when required.

By default both text elements are transparent with no border, with a black text color. The most used text properties can be modified using the text tool bar displayed when a text element is selected. Text element properties can also be modified using the Properties view.

Text fields support hyperlinks as well. See [, “Hyperlinks,” on page 1](anchors-bookmarks-hyperlinks.md) for more information.

## Static Text

The static text element is used to show non-dynamic text in reports. The only parameter that distinguishes this element from a generic text element is the Text property, where the text to view is specified: it is a normal text, not an expression, and so it is not necessary to enclose it in double quotes to respect the conventions of Java, Groovy, or JavaScript syntax.

## Text Fields

A text field allows you to print an arbitrary section of text (or a number or a date) created using an expression. The simplest case of use of a text field is to print a constant string (`java.lang.String`) created using an expression like this:

`"This is a text"`

A text field that prints a constant value like the one returned by this expression can be easily replaced by a static field. Actually, the use of an expression to define the content of a text field provides a high level of control on the generated text (even if it is just constant text). A common case is when labels have to be internationalized and loaded from a resource bundle. In general, an expression can contain fields, variables, and parameters, so you can print in a text field the value of a field and set the format of the value to present. For this purpose, a text field expression does not have to necessarily return a string (that is a text value): the `text field expression class name `property specifies what type of value is returned by the expression. It can be one of the following:

<table>
<thead>
<tr>
<th colspan="3"><p>Valid Expression Types</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>java.lang.Object</code></p></td>
<td><p><code>java.sql.Time</code></p></td>
<td><p><code>java.lang.Long</code></p></td>
</tr>
<tr>
<td><p><code>java.lang.Boolean</code></p></td>
<td><p><code>java.lang.Double</code></p></td>
<td><p><code>java.lang.Short</code></p></td>
</tr>
<tr>
<td><p><code>java.lang.Byte</code></p></td>
<td><p><code>java.lang.Float</code></p></td>
<td><p><code>java.math.BigDecimal</code></p></td>
</tr>
<tr>
<td><p><code>java.util.Date</code></p></td>
<td><p><code>java.lang.Integer</code></p></td>
<td><p><code>java.lang.String</code></p></td>
</tr>
<tr>
<td><p><code>java.sql.Timestamp</code></p></td>
<td><p><code>java.io.InputStream</code></p></td>
<td></td>
</tr>
</tbody>
</table>

An incorrect expression class is frequently the cause of compilation errors. If you use Groovy or JavaScript, you can choose `String` as the expression type without causing an error when the report is compiled. The side effect is that without specifying the right expression class, the pattern (if set) is not applied to the value.

Let us see what properties can be set for a text field:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td><code>Blank when null </code></td>
<td><p>If set to true, this option avoids printing the text field content if the expression result is a null object that produces the text<code> “null”</code> when converted in a string.</p></td>
</tr>
<tr>
<td><code>Evaluation time </code></td>
<td><p>Determines in which phase of the report creation the<code> Text field Expression</code> has to be elaborated.</p></td>
</tr>
<tr>
<td><code>Evaluation group </code></td>
<td><p>The group to which the evaluation time is referred if it is set to<code> Group.</code></p></td>
</tr>
<tr>
<td><code>Stretch with overflow </code></td>
<td><p>Deprecated. Replaced with <code>Text Adjust</code>.</p></td>
</tr>
<tr>
<td><code>Text Adjust</code></td>
<td><p>This option allows the text field to adapt vertically to the content, if the element is not sufficient to contain all the text lines. Select the required option from the following:</p>
<ul>
<li><code>CutText</code>: The text is cut if it does not fit the text field element size.</li>
<li><code>StretchHeight</code>: The text field element is stretched in height to accommodate the entire content.</li>
<li><code>ScaleFont</code>: The font size of the text is scaled down so that the entire content fits the text field element size.</li>
</ul></td>
</tr>
<tr>
<td><code>Pattern</code></td>
<td><p>The pattern property allows you to set a mask to format a value. It is used only when the expression class is congruent with the pattern to apply, meaning you need a numeric value to apply a mask to format a number, or a date to use a date pattern.</p></td>
</tr>
</tbody>
</table>
