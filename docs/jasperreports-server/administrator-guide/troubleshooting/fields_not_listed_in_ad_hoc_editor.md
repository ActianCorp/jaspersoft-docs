---
title: Fields Not Listed in Ad Hoc Editor
description: "The Ad Hoc Editor supports only certain datatypes. If a Topic contains a field with an unsupported type, the field does not appear when you open the Topic in the Ad Hoc Editor. These are the..."
---

# Fields Not Listed in Ad Hoc Editor

The Ad Hoc Editor supports only certain datatypes. If a Topic contains a field with an unsupported type, the field does not appear when you open the Topic in the Ad Hoc Editor. These are the datatypes supported in the Ad Hoc Editor:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td><ul>
<li><code>java.lang.String</code></li>
<li><code>java.lang.Byte</code></li>
<li><code>java.lang.Short</code></li>
<li><code>java.lang.Integer</code></li>
<li><code>java.lang.Long</code></li>
<li><code>java.lang.Float</code></li>
<li><code>java.lang.Double</code></li>
<li><code>java.lang.Number</code></li>
</ul></td>
<td><ul>
<li><code>java.util.Date</code></li>
<li><code>java.sql.Date</code></li>
<li><code>java.sql.Time</code></li>
<li><code>java.sql.Timestamp</code></li>
<li><code>java.math.BigDecimal</code></li>
<li><code>java.math.BigInteger</code></li>
<li><code>java.lang.Boolean</code></li>
<li><code>java.lang.Object</code></li>
</ul></td>
</tr>
</tbody>
</table>

Unsupported datatypes may occur when editing Topics manually, and sometimes with data sources for big data, in particular MongoDB. The connector for MongoDB uses the datatype of a given value in the last document containing that value, and errors in input files may cause unexpected types. For example, omitting the single quotes in the JSON format causes a string type to be interpreted as a numeric type.

If your Topic or Domain fields do not appear in the Ad Hoc Editor, you can enable logging on the following class to see details of fields with unsupported datatypes:

```
com.jaspersoft.ji.adhoc.metadata.AdhocTopicMetadata
```

For information about enabling logging, see [Configuring System Logs](../diagnostics/configuring_system_logs.md).
