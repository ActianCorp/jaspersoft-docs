---
title: Changes in 7.1 That May Affect Your Upgrade
description: "The layout of the login page changed in JasperReports Server 7.1. There were no changes to the CSS classes, but some default values were changed. If you have customized the login page, you should..."
---

# Changes in 7.1 That May Affect Your Upgrade

## Changes to the Login Page

The layout of the login page changed in JasperReports Server 7.1. There were no changes to the CSS classes, but some default values were changed. If you have customized the login page, you should make sure your customizations still have the desired effect in 7.1, and make any necessary changes.

If you have not customized the Login page, this change will not affect you.

## Changes to Absolute Paths in Reports

Prior to 7.1, you could use absolute paths in reports, for example:

`repo:/organizations/organization_1/reports/main_jrxml.jrxml`

If you have a reference to an image, a subreport, or other resource that has an absolute path, or if you use a \$P parameter which later gets resolved as an absolute path, the report will cause an error. You need to update the report and use a path which is visible to a tenant user. Consider using relative path, or the public folder in case if reports needs to work for several tenants.

# Changes in 6.4 That May Affect Your Upgrade

## Removal of the Impala Connector

JasperReports Server provides new and updated drivers for various databases. In the 6.2 release, the previous connector for Impala that had been available on the Jaspersoft community website was replaced with two new options:

- TIBCO Impala JDBC driver (also called Progress)

- Simba JDBC driver (Cloudera-endorsed JDBC interface)

By default, the new release supports the new JDBC drivers, and the old Impala connector cannot be used. You should update your Impala data sources to use the new drivers. For more information, see the JasperReports Server Administrator Guide.

If you wish to continue using the Impala connector that was previously available from the community website, modify the install as described below.

1.  Add the following files to the \<js-install\>/WEB-INF/lib directory:
    - hive-service-0.12.0-cdh5.1.3.jar
    - zookeeper-3.4.5-cdh5.1.3.jar
    - avro-1.7.5-cdh5.1.3.jar
    - commons-compress-1.4.1.jar
    - hadoop-core-1.2.1.jar
    - hive-ant-0.12.0-cdh5.1.3.jar
    - hive-common-0.12.0-cdh5.1.3.jar
    - hive-exec-0.12.0-cdh5.1.3.jar
    - hive-jdbc-0.12.0-cdh5.1.3.jar
    - jasperserver-hive-connector-bugfix-SNAPSHOT.jar
    - js-hive-datasource-1.2.1-cdh5.jar
    - paranamer-2.3.jar
    - parquet-hadoop-bundle-1.2.5-cdh5.1.3.jar
    - xz-1.0.jar
2.  Delete the file applicationContext-HiveDatasource.xml from the \<js-install\>/WEB-INF directory:

If you do not add the files listed, data sources that use the old Impala connector will cause errors when running reports that rely on them.
