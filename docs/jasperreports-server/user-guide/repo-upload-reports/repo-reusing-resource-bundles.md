---
title: Reusing Domain Localization Files
description: "The location of a resource bundle determines whether it's reusable and the conditions under which the server uses it. To resolve a $R expression in a report, the server scans resource bundles at two..."
---

# Reusing Domain Localization Files

The location of a resource bundle determines whether it's reusable and the conditions under which the server uses it. To resolve a \$R expression in a report, the server scans resource bundles at two levels in the order described in this table.

| Order | Level | Description |
|----|----|----|
| 1 | Report/ Repository | A report-level bundle declares the resource bundle base name in the header of its JRXML file. The Romanian resource bundle is a report-level bundle. A repository-level bundle is independent of any specific report and can be linked to multiple reports, as described in JasperReports Server Data Management Using Domains. |
| 2 | Server | A server-wide bundle typically contains server messages and labels of user interface components, as described in the JasperReports Server Administrator Guide. This bundle typically resides in the WEB-INF/bundles directory of the server. |

First, the server searches the report/repository level and stops scanning resource bundles if it finds a resolution to the \$R expression. If the server does not find a resolution, it scans the server level for the resource ID of the field and uses this ID.
