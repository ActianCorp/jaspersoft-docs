---
title: Ad Hoc Report Execution Through Hyperlink
description: "When you run an Ad Hoc Report through drill-down hyperlink, the report runs automatically when the Always Prompt option in input control is turned off. However, if the Always Prompt option is turned..."
---

# Ad Hoc Report Execution Through Hyperlink

When you run an Ad Hoc Report through drill-down hyperlink, the report runs automatically when the **Always Prompt** option in input control is turned off. However, if the **Always Prompt** option is turned on, the report runs on appling the input control.

Ideally, the report should run through a drill-down hyperlink when parameter values are provided, regardless of **Always Prompt** set in the report input control or not. **Always Prompt** should only apply to direct execution of reports from the JasperReports Server web UI and not via the hyperlink.

Only the hyperlinks with **Target** as **Self** are marked as drill-down, and **Always Prompt** is bypassed in the linked report.

To mark the other hyperlink targets as **Self**, choose any one of the options listed below:

- pass the `force.drill.down` hyperlink parameter:

  ``` xml
  <hyperlinkParameter name="force.drill.down">
      <hyperlinkParameterExpression><![CDATA[true]]></hyperlinkParameterExpression></hyperlinkParameter>
  ```

- set the `jrxml` property:

  ``` xml
  <property name="net.sf.jasperreports.htmlviewer.force.drill.down" value="true"/>
  ```

- set the property in the `jasperreports.properties config` file globally:

  ``` properties
  net.sf.jasperreports.htmlviewer.force.drill.down=true
  ```

!!! note

    - If the hyperlink parameter and report-level property are not present, then the global-level value takes precedence.

    - If the hyperlink parameter is not present, the report-level value takes precedence over the global-level value.

    - If the hyperlink parameter property is set to any value, then it takes precedence over report level value as well as global-level value.
