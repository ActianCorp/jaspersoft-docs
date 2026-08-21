---
title: Parameters
description: Parameters are values usually passed to the report from the application that originally requested it. They can be used for configuring report features at generation time (like the value to use in an...
---

# Parameters

Parameters are values usually passed to the report from the application that originally requested it. They can be used for configuring report features at generation time (like the value to use in an SQL query), or to supply additional data that is not provided by the data source (like a custom report title, an application-specific path for images).

Report parameters have many functions in a report. They can be used in the `where` condition of an SQL query, or to provide additional data to the report (like the value of a title or a name of the user that runs the report).

A parameter is defined by a name and a Class, which is a Java class type. For example, a parameter of type `java.sql.Connection` may be used to populate a subreport, while a simple `java.lang.Boolean` parameter may be used to show or hide a section of the report.

This chapter contains the following sections:

- [Managing Parameters](parameters_managing.md)

- [Default Parameters](parameters-built-in.md)

- [Using Parameters in Queries](parameters_queries.md)

- [Parameters Prompt](parameters-prompt.md)

- [Parameter Sets](parameters-sets.md)
