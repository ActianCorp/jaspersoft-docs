---
title: Changes in 9.0 That May Affect Your Upgrade
description: "As of release 9.0, Progress drivers are removed from JasperReports Server. If you have any resources that use or depend on any of the following Progress Drivers:"
---

# Changes in 9.0 That May Affect Your Upgrade

## Progress Driver Removal

As of release 9.0, Progress drivers are removed from JasperReports Server. If you have any resources that use or depend on any of the following Progress Drivers:

- TIautorest-6.0.1.005359.jar

- TIcassandra-6.0.3.jar

- TIdb2-5.1.4.000288.jar

- TIgooglebigquery-6.0.0.001346.jar

- TIhive-5.14.1.jar

- TIimpala-5.14.2.jar

- TImongodb-6.0.2.000510.jar

- TIoracle-6.0.0.000790.jar

- TIredshift-5.14.1.jar / TIredshift-6.0.0.000366.jar

- TIsforce-6.0.0.001533.jar

- TIsparksql-6.0.1.000124.jar

- TIsqlserver-6.0.0.000541.jar

  then you must manually install drivers that are recommended by the database vendor. After installing new drivers, update the resources in JasperReports Server to use the new drivers.

## Additional Steps to Migrate JasperReports Server on MS SQL Server, Oracle, DB2

The migration to JasperReports Server 9.0 and a shift from Progress drivers to Database vendor drivers can bring challenges, particularly with the behavior of resources. You may experience instances where, following the upgrade, the resources either stop functioning or display altered behaviors. This discrepancy is often caused by the variance in how Progress JDBC drivers and Native drivers interpret certain data types.

Let us review some patterns of the problems identified during this migration and explore two strategies to address these issues:

1.  Update your resources to reflect data type changes:

    One approach to resolve such issues is to update your resources to align with the changes in data types. Progress JDBC drivers may read certain data types differently than native vendors, leading to discrepancies in resource behavior. After identifying such cases in reports, domains and adhoc views, modify affected resources to reflect the new data type conventions.

2.  Override the default data type mapping

For users who prefer to keep the old data type mapping, another solution is to override the default JDBC data type mapping. This involves finding what data types behave differently in your resources and configuring JasperReports Server to use old type mapping for certain database. While this approach maintains consistency with the previous setup, it's crucial to thoroughly test and validate the reports to ensure accuracy and reliability.

### SQL Server

#### Handling SQL Server Time and Float columns in JasperReports Server domains

When using a migrated domain, adhoc view, or adhoc report, you may encounter a message indicating missing fields or columns. This issue occurs due to the transition from the Progress driver, which interpreted Time columns as Timestamp and Float as Float, to the SQL Server native driver, where Time is read as Time and Float as Double. To revert this change in data types, we have introduced additional configuration beans that enable users to override the default type mapping.

To revert to old behavior:

1.  Edit `../WEB-INF/applicationContext-jdbc-metadata.xml`.
2.  find `<bean class="com.jaspersoft.jasperserver.api.engine.common.domain.JdbcDriverMetaConfigurationImpl">` which has property `<property name="databaseProductName" value="Microsoft SQL Server"/>`.
3.  Uncomment the whole bean.
4.  Restart JasperReports Server.

After the change is applied, when using a SQL Server JDBC/JNDI connection in Domains or AdHoc, all Time fields will be interpreted as Timestamp, and all Float columns (with JDBC code 8) will be treated as Double.

#### Using SQL Server Time field as a parameter or field in a JRXML report

Executing a report unit may result in exceptions like **The data types time and datetime are incompatible in the equal to operator.** This can occur when a Time field, initially treated as Timestamp or DateTime, is referenced in the WHERE clause of an SQL Query, resulting in a type mismatch.

You can resolve this issue using any of the following two options:

- update JRXML and SQL query to reflect type change.
- force the SQL Server JDBC driver to return Time as DateTime by updating the JDBC connection URL and adding `sendTimeAsDatetime=false`.

### Oracle

#### Handling Oracle Float and Double Precision Types in JasperReports Server Domains

When using a migrated domain, adhoc view, or adhoc report, users may encounter a message indicating missing fields or columns. This issue occurs due to the transition from the Progress driver, which interpreted Float or Double Precision columns as Double, to the Oracle native driver, where these types are interpreted as Float. To revert this change in data types, we have introduced additional configuration beans that enable users to override the default types mapping.

To revert to old behavior perform:

1.  Edit `../WEB-INF/applicationContext-jdbc-metadata.xml`.
2.  Find `"<bean class="com.jaspersoft.jasperserver.api.engine.common.domain.JdbcDriverMetaConfigurationImpl">" which has property "<property name="databaseProductName" value="Oracle"/>"`.
3.  Uncomment that whole bean.
4.  Restart JasperReports Server.

After change is applied, when using a Oracle JDBC/JNDI connection in Domains or AdHoc, all Float or Double Precision fields will be interpreted as Double.

#### Using Oracle Numeric types with Precision and Scale in JRXML Report

When using Oracle numeric fields with precision and scale, such as Numeric (10,4), in JRXML reports, discrepancies may occur in values with trailing zeros. For instance, the value '6.1200' in a report might be displayed as '6.12.' This occurs due to the Oracle native driver's behavior of not preserving trailing zeros, which was previously managed by the Progress driver during formatting.

To resolve this issue, it is recommended to control value formatting within the JRXML, than relying on the database driver. To implement this fix, edit the JRXML file and introduce field formatting by adding:

`<textField pattern="#,###.0000" isBlankWhenNull="true">`

#### Using Aggregate Functions for Oracle Date types in JRXML Reports

After the migration of adhoc resources dependent on JRXML topics to the Oracle native driver, you may encounter difference in the results of aggregate functions on date fields. Additionally, the Hide Duplicate Rows adhoc function might return identical (duplicate) values. This discrepancy occurs from the difference in how Oracle database handles date values compared to the Progress driver.

Oracle database lacks a dedicated date type and stores dates with hours, minutes, and seconds. Oracle's DATE type is similar to Timestamp type. So for such date fields, Oracle native driver returns date values with their associated hours, minutes, and seconds, while the Progress driver always sets these time components to zero.

The consequences are noticeable when applying aggregate functions, particularly Range, as different results may be displayed when non-zero hours/minutes/seconds/miliseconds values are stored in the Oracle database. Detecting the differences in milliseconds between two values may be challenging, especially because the Oracle native driver returns the column type as `java.sql.Date`. If in JRXML the same type is set, the JasperReports Server AdHoc functionality restricts changing the format to display hours, seconds, and milliseconds.

There are two methods to align behavior with that of the Progress driver:

1.  The initial approach relies on editing the report query. By utilizing the SQL TRUNCATE function for the date field, the Oracle driver will return the date along with zeroed hours, minutes, seconds, and milliseconds. For instance:

    Original Query:

    `SELECT id, date_entered FROM my_table`

    Modified Query:

    `SELECT id, TRUNC(date_entered) FROM my_table`

2.  The alternative method is to edit the JRXML file and modifying the required field type to Timestamp.

#### Handling Oracle Date and Timestamp Fields Referenced in Domains

After migrating to Oracle native driver, some domains may produce issues with complex joins that references Timestamp as strings.

Consider the following example:

``` sql
SELECT *
FROM (
    SELECT
        "EMPLOYEE"."SALARY" AS "EMPLOYEE_SALARY1",
        "STORE"."FIRST_OPENED_DATE" AS "STORE_FIRST_OPENED_DATE"
    FROM "FOODMART"."STORE" "STORE"
    INNER JOIN "FOODMART"."EMPLOYEE" "EMPLOYEE"
        ON ("STORE"."STORE_ID" = "EMPLOYEE"."STORE_ID" AND "STORE"."FIRST_OPENED_DATE" < '1985-03-04')
)
WHERE ROWNUM <= 1000
```

In this scenario, the Timestamp value `1985-03-04` is treated as a string by the database.

When running reports or views relying on such domain schemas, an Oracle exception `ORA-01843: not a valid month` may occur.

Oracle requires proper conversion of the string to a Date or Timestamp. Without explicit date format and locale provided, the Oracle native driver uses the database system format and locale. This behavior is different from Progress Oracle driver, which consistently uses ANSI format by default.

To resolve this issue, edit the Domain Schema and append `ts` to the date value in complex join condition. For example, `1985-03-04` should be represented as `ts'1985-03-04'`.

Alternatively, you can use the `to_timestamp` function: `to_timestamp('1985-03-04 00:00:00', 'YYYY-MM-DD HH24:MI:SS.FF')`.

### DB2

#### Adjustments in DB2 Error Messages After Migrating to Native Driver

After the migration to the native DB2 driver, you may observe a change in the format of SQL error messages, which now provide fewer details as compared to how Progress DB2 driver handled errors. Instead of receiving error descriptions directly, you will get messages containing SQLCODE and SQLERROR.

Let's compare the error messages for the same SQL error:

|   | SQL error | SQL State | Vendor code |
|----|----|----|----|
| Progress Driver | \[TibcoSoftware\]\[DB2 JDBC Driver\]\[DB2\]PRODUCT1_ID NOT COLUMN OF INSERTED/UPDATED TABLE, OR ANY TABLE IN A FROM CLAUSE | 42703 | 206 |
| DB2 Native Driver | DB2 SQL Error: SQLCODE=-206, SQLSTATE=42703, SQLERRMC=PRODUCT1_ID, DRIVER=4.32.28 | 42703 | 206 |

While this change doesn't impact the functionality, for investigating failing queries you may now need to refer to the official DB2 Java driver documentation and use SQLCODE and SQLSTATE to search for the corresponding error description. The new format, though different, still provides the essential information needed for error analysis.

## AdHoc Component in Reports

With the introduction of the AdHoc Component feature, every new AdHoc report generated from an AdHoc view automatically activates this functionality. This integration ensures that any modifications made in the AdHoc view are automatically reflected in its associated AdHoc Report. AdHoc Reports created prior to or imported from earlier JasperReports Server versions will maintain their existing behavior and won't dynamically incorporate AdHoc view changes. To use the AdHoc Component feature for your AdHoc Reports, it's recommended to recreate reports from the AdHoc views in JasperReports Server 9.0.

!!! note

    The AdHoc Component feature relies on new report templates shipped with JasperReports Server 9.0, located at "/public/templates." It's important to be aware that these templates have the same names as before. During the import of older resources, there is a risk of overwriting these templates by accident. In such cases, although AdHoc reports may be generated and function correctly, they will be based on legacy report templates. To fix this, you can re-import these templates that are shipped as part of our export-minimal-catalogs. The templates and can be imported using the `js-ant import-minimal-pro` command (for details, see the JasperReports Server Installation Guide).

If your deployment uses custom AdHoc templates, it is advised to update them to the new format based on the templates found in `/public/templates`.

## JasperReports Server and JasperReports Web Studio Integration

The introduction of the latest JasperReports Web Studio brings a requirement to deploy two additional applications crucial for the normal functioning of JasperReports Web Studio. These applications can be deployed either on the same application server as JasperReports Server or remotely.

Consider allocating additional memory for your application server to meet the demand generated by the deployment of two additional applications for JasperReports Web Studio. The amount of required memory depends on the usage pattern of JasperReports Web Studio. Typically, the memory requirements for JasperReports Web Studio are significantly lower than those for the main JasperReports Server application.

## Advanced Date Time Calculations

To support new calculations, the following Date grouping functions were renamed:

- Quarter renamed to Quarter and Year (examples, Q1 2024, Q2 2024, Q3 2024, Q4 2024).

- Month renamed to Month and Year (examples, January 2024, February 2024).

## Updates to JNDI Data Sources

With the addition of the new JNDI Security feature, it is required to create the new JNDI resources even if the feature is currently disabled. If there are plans to enable this feature, ensure that all resources dependent on `jdbc/jasperserver` transition to `jdbc/jasperserverSystemAnalytics`. Similarly, resources using `jdbc/jasperserverAudit` should migrate to `jdbc/jasperserverAuditAnalytics`.

## OAuth with OpenID

The introduction of OAuth support requires migration of configurations for previous deployments of JasperReports Server. If your deployment relied on OAuth configurations customized within `applicationContext-externalAuth-*.xml`, it is required to migrate these configurations to the new format.

For more information, seeJasperReports® Server External Authentication Cookbook.

## Alerting in Report Viewer

The Alerting feature in the Report Viewer operates on the Quartz engine, similar to the Scheduler. To support the increased load from Alert executions on the JasperReports Server system, the configuration of `org.quartz.threadPool.threadCount` is increased from 2 to 4. If your deployment has modified this property, it is recommended to increase it by adding additional threads specifically for Alerting tasks. It's important to note that the introduction of new Alerting tasks may result in additional load on the overall system performance. However, the footprint of Alerting tasks is comparable to Scheduler tasks, because Alert executions perform report executions when triggered, similar to how scheduled jobs do it. It is recommended to adjust the system configuration based on your usage of the Alerting feature to optimize performance.

## Improvements in the Existing Column Names of the Schedules Page

The view of the Schedules page has been improved with updates to the following existing column names:

| Old Column Names | New Column           | Remarks |
|------------------|----------------------|---------|
| Job name         | Job name/Description | Updated |
| Resource         | Resource/URL         | Updated |
| Owner            | User                 | Updated |

## Disabled Deletion of "AnonymousUser"

The ability to delete the system user "AnonymousUser" is now disabled. This role is strictly an internal system user that is required for the normal functioning of JasperReports Server.

## Container Element for viz.js

Due to security reasons when setting a container for viz.js, that container element cannot be a Script Element or an Element that has children script tags.

## Configuring Scheduler for Dashboard

JasperReports Server allows you to enable the scheduler and headless browser to load the dashboard on the server side and export it. You need to set the `deploy.base.local.url` property in the ` js.config.properties` file when "detailed" is selected during `Export`.

## Important Notes about Compact and Split installations

- Users are able to upgrade from 8.2 Compact to 9.0 Compact using samedb and newdb.

- Users are able to upgrade from 8.2 Split to 9.0 Split using samedb and newdb.

- Users will not be able to upgrade:

  - From 8.2 Compact to 9.0 Split.
  - From 8.2 Split to 9.0 Compact.

If users need 9.0 Split installations but they are on 8.2 Compact, the required upgrade path is to:

1.  Upgrade 8.2 Compact to 9.0 Compact.
2.  Then, migrate from 9.0 Compact to 9.0 Split.

For more information on these installation options, see the *Installation* and *Upgrade* guides.
