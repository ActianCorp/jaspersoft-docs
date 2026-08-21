---
title: Input Controls with Custom Expressions
description: "You can add custom Input Controls from the following sections on the Create Input Control page:"
---

# Input Controls with Custom Expressions

You can add custom Input Controls from the following sections on the **Create Input Control** page:

- **Name and Description**:

  - **Custom Prompt Text**: This is an optional field and can be used to explain users how to use the Input Control. It can also be used to provide a customized label for the input control instead of **Prompt Text**. It enables you to write an expression or call custom function to change the Input Control title dynamically.

    For example:

    Simple label for string: `‘String’`

    Custom label: `$P` or `$R`

    A tooltip appears when you hover over the question mark icon.

    ![custom ic custom prompt tooltip](../assets/images/custom-ic-custom-prompt-tooltip.png)

- **Display Settings**:

  - **Enable/Disable Input Control \> Conditional**: This section enables you to control editing the value of the Input Control. Based on the condition defined, you may or may not be able to edit the value of the Input Control. When selected, the associated **Custom Expression** input is enabled.

    A tooltip appears when you hover over the question mark icon next to the **Conditional \> Custom Expression** input field.

    ![custom ic conditional tooltip](../assets/images/custom-ic-conditional-tooltip.png)

  - **Show/Hide Input Control \> Conditional**: This section determines the visibility of the Input Control. Based on the condition defined, the Input Control may be shown or hidden. When selected, the associated **Custom Expression** input field is enabled.

    The tooltip is also displayed when you hover over the question mark icon next to the **Conditional \> Custom Expression** input field.

Following are the expression formats for **Custom Expression**:

|                        |                      |
|------------------------|----------------------|
| Input Control Type     | Expression Format    |
| Single value number    | IC name == value     |
| Single value string    | IC name == 'value'   |
| Single value date      | IC name == d'value'  |
| Single value time      | IC name == t'value'  |
| Single value timestamp | IC name == ts'value' |

## Supported Expressions

The supported expressions include:

- Comparisons: \<, \>, \<=, \>=, ==

- Addition, Subtraction: +, -

- Multiplication, Division: \*, /

- Function call

- Relative dates

### Expression Formats Accepted

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td>Input Control Type</td>
<td><strong>Expression Format Accepted</strong></td>
</tr>
<tr>
<td><p>Single Value</p>
<p>(String/ Number/ Date/ Time/ DateTime)</p></td>
<td><ul>
<li><p>Filter_By == 'Store Manager'</p></li>
<li><p>StoreId == 1</p></li>
<li><p>StartDate &gt; d'2005-01-01'</p></li>
<li><p>StartTime == t'04:46:18'</p></li>
<li><p>DateOpened &gt; ts'2005-11-30 19:19:05</p></li>
<li><p>Birthdate == DATERANGE(‘DAY’)</p></li>
</ul></td>
</tr>
<tr>
<td>Boolean</td>
<td><ul>
<li><p>CoffeeBar == true</p></li>
<li><p>CoffeeBar</p></li>
<li><p>CoffeeBar == false</p></li>
<li><p>not CoffeeBar</p></li>
</ul></td>
</tr>
<tr>
<td><p>Single Select</p>
<p>(String/ Number/ Date/ Time/ DateTime/ Relative Date)</p></td>
<td><ul>
<li><p>Country == 'Mexico'</p></li>
<li><p>NumberSet(StoreId) == -3 or NumberSet(StoreId) &gt; 4</p></li>
<li><p>DateSet(Birthdate) == d'1915-07-03'</p></li>
<li><p>DateSet(TimeStart) == t’19:19:00’</p></li>
<li><p>DateSet(FirstOpenedDateSSLOVTimeStamp) &gt; ts'1966-01-24 00:00:00'</p></li>
<li><p>Birthdate == DATERANGE(‘YEAR-110’)</p></li>
</ul></td>
</tr>
<tr>
<td>Multi Select</td>
<td><ul>
<li><p>'Mexico' in Country and 'Canada' in Country</p></li>
<li><p>0.11 in DoubleSet(ConversionRatio) and 0.7 in DoubleSet(ConversionRatio)</p></li>
<li><p>d'1915-07-03' in DateSet(Birthdate, 'YYYY-MM-DD') and d'1969-06-20' in DateSet(Birthdate, 'YYYY-MM-DD') and d'1910-06-21' in DateSet(Birthdate, 'YYYY-MM-DD')</p></li>
<li><p>t'19:19:00' in DateSet(TimeStart, 'hh:mm:ss') and t'21:00:00' in DateSet(TimeStart, 'hh:mm:ss')</p></li>
<li><p>ts'1974-06-14 00:00:00' in DateSet(FirstOpenedDate, 'YYYY-MM-DD hh:mm:ss') and ts'2009-09-27 00:00:00' in DateSet(FirstOpenedDate, 'YYYY-MM-DD hh:mm:ss')</p></li>
<li><p>DATERANGE('YEAR-110') in DateSet(Birthdate)</p></li>
</ul></td>
</tr>
</tbody>
</table>

!!! note

    `Relative date SEMI` type is not supported for custom Input Controls.

### Expressions for Title

Users can change titles by using expressions, calling custom functions, or utilizing keys from a resource bundle. If you choose to use resource bundle keys, you must first add the corresponding bundle on the **Controls & Resources** page and specify the resource bundle file name using the `resourceBundle` attribute within the `<jasperReport>` tag of the JRXML file. For example, `resourceBundle = 'testbundle'`.

- 'StoreId for \$P{Country} '

- ‘\$R{sales.key} record’

- str(‘country.key’)

- ‘\$R{country.key} some other text’

- '\$R{country.key}' == 'This is country title from bundle'

For information about Input Controls for Custom Functions, see the JasperReports Server Administrator Guide.
