---
title: Ad Hoc Designer Function Names with Special Characters
description: "In Ad Hoc Designer, special characters are not allowed in calculated function names. When you use special characters in calculated function names, an error is displayed. The only special characters..."
---

# Ad Hoc Designer Function Names with Special Characters

In Ad Hoc Designer, special characters are not allowed in calculated function names. When you use special characters in calculated function names, an error is displayed. The only special characters allowed in calculated function names are space, and underscore.

<table>
<thead>
<tr>
<th colspan="3"><p>Validation Rule for Special Characters</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>WEB-INF/classes/esapi/validation.properties</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><code>Validator.ClientFunctionName</code></td>
<td colspan="2"><p>Sets the validation rule for special characters in Ad Hoc Designer.</p></td>
</tr>
</tbody>
</table>

To support REST API, the same validation rule must be duplicated in `WEB-INF/applicationContext-pro-remote-services.xml` as well.

```
<bean id="functionNameRegex" class="java.lang.String">
        <constructor-arg value="^[^\\s][a-zA-Z0-9\\s_]+$" /> <!-- pattern to allow function name -->
    </bean>
```
