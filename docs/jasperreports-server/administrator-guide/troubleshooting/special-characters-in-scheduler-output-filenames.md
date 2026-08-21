---
title: Special Characters in Scheduler Output File Names
description: "In scheduler, special characters are not allowed in the output file names. When you use special characters in output file names, an error is displayed."
---

# Special Characters in Scheduler Output File Names

In scheduler, special characters are not allowed in the output file names. When you use special characters in output file names, an error is displayed.

A new property `skip.filename.validation.unsupportedSymbols` in the `js.config.properties` file controls the validation of unsupported characters in the output file name. By default, this property is set to `false`. To bypass the validation process, to allow unsupported characters in the file name, this property should be set to `true`.

<table>
<thead>
<tr>
<th colspan="3"><p>Control Validation of Unsupported Characters</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>jasperserver/buildomatic/conf_source/templates/js.config.properties</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><code>skip.filename.validation.unsupportedSymbols</code></td>
<td colspan="2"><p>Validates unsupported characters in the file name. By default, the value is <code>false</code>.</p></td>
</tr>
</tbody>
</table>

!!! note

    Even when the `skip.filename.validation.unsupportedSymbols=false`, `#`, `%`, and `/` are excluded from validation as:

    - `#`: breaks into a new string

    - `/`: creates a sub-folder

    - `%`: expects a hexadecimal character
