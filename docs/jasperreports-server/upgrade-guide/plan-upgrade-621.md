---
title: Changes in 6.2.1 That May Affect Your Upgrade
description: "JasperReports Server provides new and updated drivers for various databases. In this release, the previous connector for Impala that was available on the Jaspersoft community website is replaced with..."
---

# Changes in 6.2.1 That May Affect Your Upgrade

## Removal of the Impala Connector

JasperReports Server provides new and updated drivers for various databases. In this release, the previous connector for Impala that was available on the Jaspersoft community website is replaced with two new options:

- TIBCO Impala JDBC driver (also called Progress)
- Simba JDBC driver (Cloudera-endorsed JDBC interface)

By default, the new release supports the new JDBC drivers, and the old Impala connector cannot be used. You should update your Impala data sources to use the new drivers. For more information, see the JasperReports Server Administrator Guide.

If you wish to continue using the Impala connector from the community website, you must replace the following JAR files in the .../WEB-INF/lib directory:

| Replace                 | With This                        |
|-------------------------|----------------------------------|
| hive-service-0.13.1.jar | hive-service-0.12.0-cdh5.1.3.jar |
| zookeeper-3.4.6.jar     | zookeeper-3.4.5-cdh5.1.3.jar     |

Unless you replace the files listed in the table, data sources that use the old Impala connector will cause errors when running reports that rely on them.

# Changes in 6.2 That May Affect Your Upgrade

## Renaming of Ad Hoc Templates

Due to minor changes to Ad Hoc templates in 6.2, the default template files have been renamed, for example, actual_size.510.jrxml has been renamed actual_size.620.jrxml. During upgrade, templates with an earlier version number are overwritten by the new template. If you have customized the default template and kept the same file name, your changes will be overwritten. To avoid this, make a copy of your customized template with a unique name and upload it to your template directory (by default, **Public \> Templates**) using **Add Resource \> File \> Style Template**.

In general, if you want to customize the Ad Hoc templates, we recommend you rename the existing template and set the new template as a default, rather than overwriting the existing template. See the JasperReports Server Administrator Guide for more information.
