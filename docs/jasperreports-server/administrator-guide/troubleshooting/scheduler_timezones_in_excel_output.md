---
title: Scheduler Timezones in Excel Output
description: "When scheduling a report, you can specify the timezone that should be applied to the output instead of using the data source's timezone. This works for all outputs except Excel (XLS), both paginated..."
---

# Scheduler Timezones in Excel Output

When scheduling a report, you can specify the timezone that should be applied to the output instead of using the data source's timezone. This works for all outputs except Excel (XLS), both paginated and non-paginated. To overcome this limitation, you must explicitly enable timezone usage in XLS output.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>Setting Timezones in Scheduled Excel (XLS) Reports</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>.../WEB-INF/classes/jasperreports.properties</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Value</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>net.sf.jasperreports.export.</code><br />
<code>xls.use.timezone</code><br />
</p></td>
<td><p><code>true</code><br />
</p></td>
<td><p>Define this property as <code>true</code> to apply timezones in scheduled Excel (XLS) reports.</p></td>
</tr>
</tbody>
</table>

This property can also be defined on individual elements in the report's JRXML if only certain fields should apply the timezone.

# Incorrect Time Stamp Pattern Appearing in Excel Export

When exporting reports to Excel, the time stamp appears in the following pattern "`mmm d, yyyy h:mm:ss \a`" instead of "`MMM d, yyyy h:mm:ss AM/PM`".

To resolve this, you need to add mapping to the map in `applicationContext.xml`. It ensures date patterns in Java 11 will convert to corresponding Excel date patterns. And Excel export will have the correct time stamp, that is, "`MMM d, yyyy h:mm:ss AM/PM`".

To add the mapping

1.  Open the file `.../WEB-INF/applicationContext-webapp.xml` for editing.

2.  Locate the `formatPatternsMap` bean and add the following new entry.

    ``` xml
    <entry key="d MMM, yyyy, h:mm:ss a" value="d MMM, yyyy h:mm:ss AM/PM"/>
    ```

3.  Restart the server.
