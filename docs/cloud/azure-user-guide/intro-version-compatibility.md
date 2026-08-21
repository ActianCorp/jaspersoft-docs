---
title: Compatibility Between Versions
description: "When a new version of JasperReports is distributed, some classes usually change. These modified classes typically impact the XML syntax and the jasper file structure."
---

# Compatibility Between Versions

When a new version of JasperReports is distributed, some classes usually change. These modified classes typically impact the XML syntax and the `jasper` file structure.

Before JasperReports 1.1.0, this was a serious problem and a major upgrade deterrent, since it required recompiling all the `JRXML` files in order to be used with the new library version. Things changed after the release of Version 1.1.0, in which JasperReports assured backwards compatibility, that is, the library is able to understand and execute any `jasper` file generated with a previous version of JasperReports.

With JasperReports 3.1, the `jrxml` syntax moved from a DTD-based definition to XML-based schema. The XML source declaration syntax now references a schema file, rather than a DTD. Based on what we said previously, this is not a problem since JasperReports assures backwards compatibility. However, many people are used to designing reports with early versions of iReport then generating the reports by compiling `jrxml` in JasperReports. This was always a risky operation, but it was still valid because the user was not using a new tag in the XML. With the move to an XML schema, the `jrxml` output of iReport 3.1.1 and newer can only be compiled with a JasperReports 3.1.0 or later. All versions of Jaspersoft Studio produce output that is only compatible with later versions of JasperReports Library.

For information on exporting or compiling a report to an earlier version of JasperReports Library, see Setting Compatibility with Earlier Versions of .
