---
title: Configuring Domains
description: "Advanced uses of Domains may consider these configurations:"
---

# Configuring Domains

Advanced uses of Domains may consider these configurations:

- Disabling the Domain Validation Check

- Setting the Level of Referential Integrity

- Optimizing Snowflake Schema Joins

When you use Domains with certain database constructs, you may need to configure JasperReports Server:

- Enabling Oracle Synonyms

- Enabling CLOB Fields

- Enabling Proprietary Types

- Extending JDBC Type Mapping

- Accessing Materialized Views

- Modifying Domain Calculated Field Variable Behavior

## Disabling the Domain Validation Check

By default, JasperReports Server validates a Domain against its data source to ensure that the Domain design maps properly to the underlying tables. This validation occurs when a Domain design file is uploaded to the server. If your data source is very large and complex, this validation can take time. If the validation takes too long, you can disable it. In this case, JasperReports Server assumes the Domain design is valid, and simply uploads it without the check.

To disable the validation edit the following configuration file:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>Configuring Domain Validation Check</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>.../WEB-INF/applicationContext-semanticLayer.xml</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Bean</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>skipDomainDatabase</code><br />
<code>Validation</code></p></td>
<td><p><code>slConfig</code></p></td>
<td><p>Set this property to <code>TRUE</code> to disable the validation check.</p></td>
</tr>
</tbody>
</table>

!!! note

    If the tables and fields referenced in the Domain design don't exist in the data source when `skipDomainDatabaseValidation` is set to `TRUE`, the **Domain** wizard won't detect the problem, but the **Choose Data** wizard returns errors when your end users work with the Domain.

## Setting the Level of Referential Integrity

Referential integrity is the verification process that occurs when opening an Ad Hoc view or a report that is based on a Domain. The server checks that all fields and measures referenced by the view or the report match those defined in the Domain. This ensures that out-of-date views or reports cannot be run if they rely on items in the Domain that were modified or removed.

In practice, when you modify a Domain to remove fields or measures, you must also modify all Ad Hoc views that depend on those fields and measures, and you must regenerate any reports based on those views. In case you don't, referential integrity will give an error so that the user knows why the report did not run, instead of failing at runtime or showing empty data. When opening an Ad Hoc view that has similar referential integrity errors, the server displays a list of missing fields and measures and prompts you to removes the items so the view is coherent when it opens.

However, in cases where Domain security makes a field unavailable to a user, this will also be detected as a referential integrity error upon opening a view or running a report. Some views and their corresponding reports may be designed for multiple users with different security access to data, and you intend to display the report with blank or zero in place of certain data. In such cases, you should change the default setting for referential integrity so that users can open views and run reports without causing an error.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>Configuring Referential Integrity</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>.../WEB-INF/applicationContext-adhoc-dataStrategy.xml</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Default</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>checkSourcesInStrictMode</code></p></td>
<td><p><code>true</code></p></td>
<td><p>By default (when true) when opening an Ad Hoc view, any mismatch between its fields and those in the Domain it references trigger a missing data dialog in the Ad Hoc editor and prompt the user to remove those fields.</p>
<p>When this configuration is set to false, the following referential integrity errors are allowed:</p>
<ul>
<li>The item's table ID or join ID does not match the one in the Domain, provided its unique item ID still matches one in another set or subset.</li>
<li>The item's type does not match the one in the Domain, provided the item is not used in any filter, calculated field, or summary function that is incompatible with the altered type.</li>
</ul>
<p>Referential integrity issues that do not meet these criteria will still trigger a missing data dialog in the Ad Hoc editor, even if this setting is false. For example, if an aggregation on a numerical field in the view is set to Average, but the field in the Domain is now a string, an error is triggered because strings cannot be averaged.</p></td>
</tr>
<tr>
<td><p><code>skipCheckSourcesForViews</code></p></td>
<td><p><code>false</code></p></td>
<td><p>When rendering an Ad Hoc view based on a Domain, the server checks that all fields and measures in the view match those of the Domain. By default (when this setting is false), if there missing fields, the sever will display an error and not display the view.</p>
<p>When this setting is true, the server will render the view even if some fields are missing for any reason, for example if they are hidden due to security in the Domain. This setting is more permissive of referential integrity errors than <code>checkSourcesInStrictMode</code> above.</p></td>
</tr>
<tr>
<td><p><code>skipCheckSourcesForReports</code></p></td>
<td><p><code>false</code></p></td>
<td><p>When running a report based on an Ad Hoc view based on a Domain, the server checks that all fields and measures in the report match those of the Domain. By default (when this setting is false), if there is a mismatch, the sever will display an error and not run the report.</p>
<p>When this setting is true, the server will run the report with missing fields and the result depends on the severity of any mismatch. Fields that are hidden due to security in a properly designed report will appear blank or zero. A report where the missing field leads to a computation error will cause the running report to fail.</p></td>
</tr>
</tbody>
</table>

!!! note

    If you change the referential integrity settings in order to allow certain reports to work with Domain security, you should make sure those reports work as intended for all users and ensure all other reports run correctly. If you later remove fields or measures from your Domains, you should also be diligent in manually updating all views and reports that depend on those Domains.

## Optimizing Snowflake Schema Joins

When creating a Domain on top of a snowflake schema, the default joins generated when using the Domain in the Ad Hoc Editor may take a long time and include dimensions not used in the report. For example, a schema with over a hundred dimension tables mostly connected to a subset of 5-10 fact tables may cause such behavior. The following setting can be enabled to optimize the joins generated for such a snowflake database schema. The default setting has better performance in the more common cases with fewer tables.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>Configuring Domain Join Optimization</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>.../WEB-INF/applicationContext-semanticLayer.xml</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Bean</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>specialOptimizationOn</code></p></td>
<td><p><code>graph</code><br />
<code>Operations</code><br />
</p></td>
<td><p>The default setting of <code>false</code> handles typical cases of Domains based on 10-100 tables. For snowflake schemas that typically have 100 or more tables, or for database topologies that cause slow join performance in Ad Hoc views, set this property to <code>true</code> to optimize the joins in the Ad Hoc Editor.</p></td>
</tr>
</tbody>
</table>

## Enabling Oracle Synonyms

By default, Domains can't access synonyms in an Oracle database. Settings to enable them vary depending on your application server. The settings shown here apply to Apache Tomcat. Your application server may require different values. Set the following property to enable Oracle synonyms on Tomcat. If you access your Oracle database through JNDI, you also need to configure the JNDI connection.

Be aware that the Oracle metadata service is significantly slower when synonyms are in scope.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>Enabling Oracle Synonyms</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>.../WEB-INF/applicationContext-jdbc-metadata.xml</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Bean</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>includeSynonyms</code><br />
<code>ForOracle</code></p></td>
<td><p><code>jdbcMeta</code><br />
<code>Configuration</code></p></td>
<td><p>Set the value to true:</p>
<p><code>&lt;value&gt;true&lt;/value&gt;</code></p></td>
</tr>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>.../META-INF/context.xml</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Bean</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>accessToUnderlying</code><br />
<code>ConnectionAllowed</code></p></td>
<td><p><code>&lt;Resourcename=</code><br />
<code>"jdbc/oracle"...</code><br />
</p></td>
<td><p>If you use JNDI, add the following property:</p>
<p><code>accessToUnderlying</code><br />
<code>ConnectionAllowed="true"</code></p></td>
</tr>
</tbody>
</table>

## Enabling CLOB Fields

Support for CLOB (Character Large Object) fields is dependent on your database and must be enabled manually. If you want to access CLOB fields in JasperReports Server, set the following options according to your database.

The Oracle JDBC driver implementation uses the `CLOB` JDBC type for CLOB fields.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>CLOB Support for Oracle</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>.../WEB-INF/applicationContext-jdbc-metadata.xml</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Bean</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>jdbc2JavaType</code><br />
<code>Mapping</code></p></td>
<td><p><code>jdbcMeta</code><br />
<code>Configuration</code></p></td>
<td><p>This property contains a map of database field types to Java types. Find the line for CLOB that is commented out:</p>
<div class="sourceCode" id="cb1"><pre class="sourceCode html"><code class="sourceCode html"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="co">&lt;!--entry key=&quot;CLOB&quot; value=&quot;&quot;/--&gt;</span></span></code></pre></div>
<p>Modify it as follows:</p>
<div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">entry</span> <span class="ot">key=</span><span class="st">&quot;CLOB&quot;</span> <span class="ot">value=</span><span class="st">&quot;java.lang.String&quot;</span>/&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

The MySQL JDBC driver implementation uses either the `CLOB` JDBC type, the `LONGVARBINARY` JDBC type, or both to represent CLOB fields, depending on their length.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>CLOB Support for MySQL</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>.../WEB-INF/applicationContext-jdbc-metadata.xml</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Bean</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>jdbc2JavaType</code><br />
<code>Mapping</code></p></td>
<td><p><code>jdbcMeta</code><br />
<code>Configuration</code></p></td>
<td><p>This property contains a map of database field types to Java types. Find the following lines:</p>
<div class="sourceCode" id="cb1"><pre class="sourceCode html"><code class="sourceCode html"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="co">&lt;!--entry key=&quot;CLOB&quot; value=&quot;&quot;/--&gt;</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a><span class="co">&lt;!--entry key=&quot;LONGVARBINARY&quot; value=&quot;&quot;/--&gt;</span></span></code></pre></div>
<p>And modify them as follows:</p>
<div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">entry</span> <span class="ot">key=</span><span class="st">&quot;CLOB&quot;</span> <span class="ot">value=</span><span class="st">&quot;java.lang.String&quot;</span>/&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">entry</span> <span class="ot">key=</span><span class="st">&quot;LONGVARBINARY&quot;</span> <span class="ot">value=</span><span class="st">&quot;java.lang.String&quot;</span>/&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

!!! note

    Due to a limitation, `CLOB` and `NTEXT` fields cannot be sorted or compared in a query. For example, trying to add a `CLOB` field as a crosstab column with domain query optimization enabled will result in an error message.

## Enabling Proprietary Types

JasperReports Server provides a JDBC-to-Java type mapping for all standard JDBC column types for use in Domains. However, some databases have proprietary types that you may need to map to a Java type with a special configuration. Some proprietary types, such as NVARCHAR2 for Oracle, are already mapped by default.

As a prerequisite, the proprietary type must be logically equivalent to one of following Java classes:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td><div class="language-text highlight"><pre><code>java.lang.Boolean
java.lang.Byte
java.lang.Character
java.lang.Double
java.lang.Float</code></pre></div></td>
<td><div class="language-text highlight"><pre><code>java.lang.Integer
java.lang.Long
java.lang.Short
java.lang.String
java.math.BigDecimal</code></pre></div></td>
<td><div class="language-text highlight"><pre><code>java.sql.Date
java.sql.Time
java.sql.Timestamp
java.util.Date</code></pre></div></td>
</tr>
</tbody>
</table>

There are two ways to create a mapping for a proprietary type, as shown in the following table:

- Modify the generic mapping for `NUMERIC` types. By default, any numeric type that doesn't match one of the other types is mapped to `BigDecimal`.
- Create a secondary mapping under the special `OTHER` key, where the secondary key can be your custom type name.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>Proprietary Database Type Mapping</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>.../WEB-INF/applicationContext-jdbc-metadata.xml</code></p></td>
</tr>
<tr>
<td><p>Properties</p></td>
<td><p>Bean</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>jdbc2Java</code><br />
<code>TypeMapping</code></p></td>
<td><p><code>jdbcMeta</code><br />
<code>Configuration</code></p></td>
<td><p>If your proprietary type is not already defined in this file, you can add it:</p>
<ul>
<li>To modify the generic mapping, edit this line:</li>
</ul>
<div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">entry</span> <span class="ot">key=</span><span class="st">&quot;NUMERIC&quot;</span> <span class="ot">value=</span><span class="st">&quot;java.math.BigDecimal&quot;</span>/&gt;</span></code></pre></div>
<ul>
<li>To add a secondary key to the <code>OTHER</code> key, follow this example:</li>
</ul>
<div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">entry</span> <span class="ot">key=</span><span class="st">&quot;OTHER&quot;</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">map</span>&gt;</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">entry</span> <span class="ot">key=</span><span class="st">&quot;NVARCHAR2&quot;</span> <span class="ot">value=</span><span class="st">&quot;java.lang.String&quot;</span>/&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">map</span>&gt;</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">entry</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>

## Extending JDBC Type Mapping

Some database types are not even mapped to a JDBC type. In particular, Oracle uses `TIMESTAMP WITH TIME ZONE` and `TIMESTAMP WITH LOCAL TIME ZONE` that must be mapped in order to appear in JasperReports Server. If there are other types in your database, you can override or extend the JDBC type mapping with the following configuration:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>Extending JDBC Type Mapping</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>.../WEB-INF/applicationContext-jdbc-metadata.xml</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Bean</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>codeToJdbcType</code><br />
<code>Mapping</code></p></td>
<td><p><code>jdbcMeta</code><br />
<code>Configuration</code></p></td>
<td><p>This property contains a map of database type codes to JDBC types. By default the codes for Oracle <code>TIMESTAMP</code> types are mapped:</p>
<div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">entry</span> <span class="ot">key=</span><span class="st">&quot;-101&quot;</span> <span class="ot">value=</span><span class="st">&quot;TIMESTAMP&quot;</span>/&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">entry</span> <span class="ot">key=</span><span class="st">&quot;-102&quot;</span> <span class="ot">value=</span><span class="st">&quot;TIMESTAMP&quot;</span>/&gt;</span></code></pre></div>
<p>Add or replace these entries to map additional types from your database.</p></td>
</tr>
</tbody>
</table>

### Overriding JDBC Type Mapping for Selected Database

The `applicationContext-jdbc-metadata.xml` file contains `jdbcMetaConfiguration`. It is global for all drivers and contains the following two properties, that are used to map JDBC type to Java types:

- `jdbc2JavaTypeMapping`
- `codeToJdbcTypeMapping`

In some cases, database or JDBC driver vendors may use the same Type Code or JDBC type for different data types. To address this, JasperReports Server allows the definition of custom mappings for specific databases while keeping the global configuration intact.

For example, the native MS SQL Server driver might return code 92 for a column of type `Time(3)`. By default, JasperReports Server maps code 92 to `java.sql.Types.TIME`. However, different JDBC drivers may interpret this code differently; for instance, the Progress SQL Server driver maps it to `java.sql.Types.TIMESTAMP`. To adjust MS SQL Server behaviour, a specific configuration for the MS SQL Server driver can be added to override the default mapping.

Follow these steps to customize the configuration:

1.  Find the `<bean class="com.jaspersoft.jasperserver.api.engine.common.domain.JdbcDriverMetaConfigurationImpl">` in the `../WEB-INF/applicationContext-jdbc-metadata.xml` file.

2.  Uncomment the bean and set its properties:

    ``` xml
    <bean class="com.jaspersoft.jasperserver.api.engine.common.domain.JdbcDriverMetaConfigurationImpl">
        <property name="databaseProductName" value="Microsoft SQL Server"/>
        <property name="codeToJdbcTypeMapping">
            <map>
                <entry key="92" value="TIMESTAMP"/>
                <entry key="8" value="FLOAT_OR_DOUBLE_TYPE"/>
            </map>
        </property>
    </bean>
    ```

    Ensure that the class is set to `com.jaspersoft.jasperserver.api.engine.common.domain.JdbcDriverMetaConfigurationImpl`, indicating that this bean can override the default configuration per driver type. The `databaseProductName` value should be set to the JDBC Driver Name found in the driver's official documentation or retrieved by executing `getDatabaseProductName()` in Java code.

3.  Restart JasperReports Server.

In this specific configuration for the MS SQL Server driver, the `codeToJdbcTypeMapping` property is adjusted to override the default mappings for code 92 and code 8.

In certain scenarios, MS SQL Server may return code 8 for columns of the Float type. This default code is later mapped to `java.sql.Types.DOUBLE`. However, challenges arise when the same code is used for other data types like Real or Double, and this behavior can vary between JDBC driver vendors. For example, the Progress JDBC driver interprets such columns as `java.lang.Float`.

To resolve this difference, a specialized mapping is introduced by assigning code 8 to `FLOAT_OR_DOUBLE_TYPE`. This addition adds an extra check performed later in the `jdbc2JavaTypeMapping` property:

``` xml
<property name="jdbc2JavaTypeMapping">
    <map>
        <!-- ... other mappings ... -->
        <entry key="FLOAT_OR_DOUBLE_TYPE">
            <map>
                <entry key="float" value="java.lang.Float"/>
                <entry key="otherColumnTypes" value="java.lang.Double"/>
            </map>
        </entry>
    </map>
</property>
```

In this configuration:

- For columns identified as float, JasperReports Server maps the type to `java.lang.Float`.
- For other floating-point types like double, real, or numeric, identified by the value `otherColumnTypes`, the mapping is set to `java.lang.Double`.

## Accessing Materialized Views

Domains access tables and views by default, but some databases support other structures such as materialized views. These alternate table structures don't show up by default, but you can often configure Domains to display and access them.

If the JDBC driver for your database assigns a standard table type identifier to the materialized view, you can access it in Domains, Ad Hoc views, and reports. To find the table type, use a JDBC client such as the [SQuirreL tool](http://squirrel-sql.sourceforge.net/) to view your database schema. In SQuirreL, use the **Objects** tab to browse the tables and views organized by table type. Look for your materialized view and note its table type.

The table type values are defined in the [DatabaseMetaData.html.getTables()](http://docs.oracle.com/javase/7/docs/api/java/sql/DatabaseMetaData.html#getTables(java.lang.String,%20java.lang.String,%20java.lang.String,%20java.lang.String%5B%5D)) documentation. When you know the string corresponding to your table type, add it to the following configuration value:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>Accessing Materialized Views</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>.../WEB-INF/applicationContext-jdbc-metadata.xml</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Bean</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>tableTypes</code></p></td>
<td><p><code>jdbcMeta</code><br />
<code>Configuration</code></p></td>
<td><p>Uncomment the JDBC table type corresponding to the materialized view or other table structure in your databases, for example:</p>
<p><code>&lt;value&gt;LOCAL TEMPORARY&lt;/value&gt;</code></p></td>
</tr>
</tbody>
</table>

## Modifying Domain Calculated Field Variable Behavior

The property `resolveDomainCalcFieldVariableInAdvance` included in `WEB-INF/applicationContext-adhoc-dataStrategy.xml` for `bean id="commonDomainDataStrategy"` allows you to calculate a domain calculated field in two ways. The default value is set to `false`, and the behavior overrides the `lookupExpression(Variable var)` in `ColumnCalculation`.

For example, if you have a domain calculated field expression such as “coverage / allowance”, it will translate to sum(coverage) / sum(allowance) instead of sum(coverage / allowance).

You can change the default domain calculated field variable behavior to use a sum aggregation (the original behavior prior to JasperReports Server 7.8) with the following configuration:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>Modifying Domain Calculated Field Variable Behavior</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Configuration File</p></td>
</tr>
<tr>
<td colspan="3"><p><code>.../WEB-INF/applicationContext-adhoc-dataStrategy.xml</code></p></td>
</tr>
<tr>
<td><p>Property</p></td>
<td><p>Bean</p></td>
<td><p>Description</p></td>
</tr>
<tr>
<td><p><code>resolveDomainCalcFieldVariableInAdvance</code></p></td>
<td><p><code>commonDomainDataStrategy</code></p></td>
<td><p>Set value to <code>true</code>:</p>
<p><code>&lt;property name="resolveDomainCalcFieldVariableInAdvance" value="true"/&gt;</code></p></td>
</tr>
</tbody>
</table>
