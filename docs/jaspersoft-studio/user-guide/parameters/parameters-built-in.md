---
title: Default Parameters
description: "JasperReports provides some built-in parameters (internal to the reporting engine). You can read the built-in parameters, but you cannot modify or delete them. Some important built-in parameters are:"
---

# Default Parameters

JasperReports provides some built-in parameters (internal to the reporting engine). You can read the built-in parameters, but you cannot modify or delete them. Some important built-in parameters are:

- **REPORT_CONNECTION** - For a report using JDBC, this parameter holds the JDBC connection used to run the SQL query.
- **REPORT_DATA_SOURCE** - This parameter contains the data source used to fill the report (if available).
- **REPORT_LOCALE** - This parameter contains the locale used to fill the report.

Some built-in parameters are specific to a query language. For example, if you are using the Hibernate query language, the reports automatically include the `HIBERNATE_SESSION` parameter that holds the Hibernate session for the HQL query.

The built-in parameters are:

| Parameter | Description |
|----|----|
| `REPORT_CONTEXT` |  |
| `REPORT_PARAMETERS_MAP` | This is the `java.util.Map` passed to the `fillReport` method. It contains the parameter values defined by the user. |
| `JASPER_REPORT` | This parameter gives access to the current `JasperReport` template object that is being filled. |
| `REPORT_CONNECTION` | This is the JDBC connection passed to the report when the report is created through an SQL query. |
| `REPORT_MAX_COUNT` | This limits the number of records filling a report. If no value is provided, no limit is set. |
| `REPORT_DATA_SOURCE` | This is the data source used by the report when it is not using a JDBC connection. |
| `REPORT_SCRIPTLET` | This represents the scriptlet instance used during report creation. If no scriptlet is specified, this parameter uses an instance of `net.sf.jasperreports.engine.JRDefaultScriptlet`. |
| `REPORT_LOCALE` | This specifies the locale used to fill the report. If no locale is provided, the system default is used. |
| `REPORT_RESOURCE_BUNDLE` | This is the resource bundle loaded for this report. |
| `REPORT_TIME_ZONE` | This is used to set the time zone used to fill the report. If no value is provided, the system default is used. |
| `REPORT_FORMAT_FACTORY` | This is an instance of a `net.sf.jasperreports.engine.util.FormatFactory`. The user can replace the default one and specify a custom version using a parameter. Another way to use a particular format factory is by setting the report property `format factory class`. |
| `REPORT_CLASS_LOADER` | This parameter can be used to set the class loader to use when filling the report. |
| `REPORT_URL_HANDLER_FACTORY` | Class used to create URL handlers. If specified, it replaces the default. |
| `REPORT_FILE_RESOLVER` | This is an instance of `net.sf.jasperreports.engine.util.FileResolver` used to resolve resource locations that can be passed to the report to replace the default implementation. |
| `REPORT_TEMPLATES` | This is an optional collection of styles (`JRTemplate`) that can be used in addition to those defined in the report. |
| `SORT_FIELDS` | This is an in-memory field-based data source sorting. The sorting is activated by the presence of one or more `<sortField>` elements in the report template. |
| `FILTER` | A `DatasetFilter` is used in addition to `JRDataset.getFilterExpression()` for filtering dataset rows. |
| `REPORT_VIRTUALIZER` | This defines the class for the report filler that implements the `JRVirtualizer` interface for filling the report. |
| `IS_IGNORE_PAGINATION` | You can switch the pagination system on and off with this parameter (it must be a Boolean object). By default, pagination is used except when exporting to HTML and Excel formats. |

JasperReports Default Parameters
