---
title: Creating a Custom Data Source
description: "If you have an existing JRDataSource implementation used with JasperReports Library that you'd like to use in JasperReports Server, you need to implement the supporting classes and configure the..."
---

# Creating a Custom Data Source

If you have an existing `JRDataSource` implementation used with JasperReports Library that you'd like to use in JasperReports Server, you need to implement the supporting classes and configure the server. You need to create or edit the following files:

<table>
<caption><p>Files Used by a Custom Data Source Implementation</p></caption>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th><p>Type</p></th>
<th><p>Path (relative to web app directory)</p></th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Java classes</p></td>
<td><p><code>WEB-INF/lib</code> or <code>WEB-INF/classes</code></p></td>
<td>The logic of your JasperReports data source, the supporting interfaces, and any optional classes compiled into JAR files.</td>
</tr>
<tr>
<td><p>Spring bean definition</p></td>
<td><p><code>WEB-INF/applicationContext-&lt;name&gt;.xml</code></p></td>
<td>The configuration of the data source within the server's web application.</td>
</tr>
<tr>
<td><p>Message catalog</p></td>
<td><p><code>WEB-INF/bundles/&lt;name&gt;.properties</code></p>
<p>also <code>&lt;name&gt;_&lt;locale&gt;.properties</code></p></td>
<td>Strings such as the name of the data source type in the New Data Source dialog, names for visible properties, and any validation messages. You can translate the strings for other locales in multiple files.</td>
</tr>
<tr>
<td><p>Query language<br />
configuration (optional)</p></td>
<td><p><code>WEB-INF/applicationContext-[pro-]remote-services.xml</code> or</p>
<p><code>WEB-INF/applicationContext-custom.xml</code> and <code>WEB-INF/js.spring.properties</code></p></td>
<td>If your JR data source is created using a query executer and you want the query language to be available in the UI, such as input control dialogs</td>
</tr>
</tbody>
</table>

These files work together to make your custom data source type available in the user interface and to instantiate your custom `JRDataSource`, as described in the following sections.

## Writing Java Classes

As seen in [Custom Data Source Architecture](custom-data-source-architecture.md), you must provide additional classes so that the server can instantiate your custom `JRDataSource` when needed with the requested parameters. This is the purpose of the `ReportDataSourceService` interface that you must implement. For code samples, see [Custom Data Source Examples](custom-data-source-examples.md).

### Implementing the ReportDataSourceService Interface

A custom data source definition requires an implementation of the `ReportDataSourceService` interface, which sets up and tears down data source connections in JasperReports Server. It defines the following methods:

<table>
<thead>
<tr>
<th colspan="3"><p>The <code>ReportDataSourceService</code> Interface</p></th>
</tr>
<tr>
<th><p>Interface</p></th>
<th><p>Method to Implement</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="3"><code>ReportDataSourceService</code></td>
<td><p><code>void setReportParameterValues(Map parameterValues)</code></p></td>
<td>Called before running a report; it creates resources needed by JasperReports Library to instantiate a <code>JRDataSource</code>, and adds them to the parameter map.</td>
</tr>
<tr>
<td><code>void closeConnection()</code></td>
<td><p>Cleans up any resources allocated in <code>setReportParameterValues()</code>.</p></td>
</tr>
<tr>
<td>Property setters and getters</td>
<td>A getter and setter method corresponding to each parameter name, including hidden properties. For example, if you defined a property with the name <code>user</code>, you need <code>getUser()</code> and <code>setUser()</code> methods.</td>
</tr>
</tbody>
</table>

### Defining Custom Data Source Properties

A custom data source definition can have properties so that users may configure each data source instance differently, in the same way that a JDBC data source has properties for JDBC driver class, URL, user name, and password. Ultimately, it is your `JRDataSource` that determines what properties are needed.

There are two kinds of properties:

-   Editable properties that must be string values. When a user launches the **New Data Source** dialog to create an instance of your custom data source definition, the editable properties have text fields for user input. These values are persisted in the repository when you save the data source.

-   Hidden properties that can be of any type. You set these property values in the Spring configuration file to be passed to your `ReportDataSourceService` implementation. Therefore, they do not appear in the **New Data Source** dialog, nor do they need to be persisted in the repository. Use hidden properties if you want to give your `ReportDataSourceService` implementation access to a Spring bean instance.

These properties are defined in two places that must work together:

-   Your `ReportDataSourceService` implementation must have getters and setters for each property, and your code can use the values for any type of processing. For source code examples, see [Hibernate Custom Data Source](custom-data-source-examples.md).

-   The Spring beans need the list of properties to set up the New Data Source dialog, save the user values in the repository, and later instantiate your `ReportDataSourceService` when needed to fill a report. For examples of both editable and hidden properties, see the XML example in 1.1.5, “Defining the Custom Data Source in Spring,” on page 1.

### Implementing the Optional Validator Interface

A validator verifies property values entered by the user and rejects bad values with an optional message. The validators are applied to the editable properties that are returned from the **New Data Source** dialog, before a data source is being stored in the repository.

You can implement any level of validation that you need, such as:

-   Null check (presence or absence of value)

-   Type validation (string or number)

-   Syntax validation (format or contents of a string)

-   Range validation (value of a number)

Property values may include references to attributes, whose values are not determined until the data source is instantiated when running a report. An attribute has the following syntax: `{attribute('attrName')}` or `{attribute('attrName','[User|Tenant|Server]')}`. Your validator code should recognize these patterns in property value strings and allow or skip validation of the attribute reference.

To create a validator, implement the `CustomDataSourceValidator` interface as follows:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>Optional Validator Interface</p></th>
</tr>
<tr>
<th><p>Interface</p></th>
<th><p>Method to Implement</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>CustomDataSourceValidator</code></p></td>
<td><p><code>validatePropertyValues(CustomReportDataSource ds, Errors errors)</code><br />
</p></td>
<td><p>Your code checks parameters and calls <code>errors.rejectValue()</code> with the appropriate property name and error code (see <span>Defining the Message Catalog</span>).</p></td>
</tr>
</tbody>
</table>

For a source code example of the `CustomDataSourceValidator` implementation, see [Webscraper Custom Data Source](custom-data-source-examples.md).

### Implementing Optional Query Executer Interfaces

If you want to use the value of the `queryString` in the JRXML to obtain your data source, you must create implementations of the `JRQueryExecuter` and `JRQueryExecuterFactory` interfaces.

<table>
<thead>
<tr>
<th colspan="3"><p>Optional Query Executer Interfaces</p></th>
</tr>
<tr>
<th><p>Interface</p></th>
<th><p>Method to Implement</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>JRQueryExecuterFactory</code></p></td>
<td><p><code>JRQueryExecuter createQueryExecuter(JRDataset dataset, Map parameters)</code></p></td>
<td><p>Returns a <code>JRQueryExecuter</code> for the given dataset and parameter map.</p></td>
</tr>
<tr>
<td rowspan="3"><p><code>JRQueryExecuter</code></p></td>
<td><p><code>JRDataSource createDatasource()</code></p></td>
<td><p>Returns the actual data source based on the parameter map passed to the <code>JRQueryExecuterFactory</code>.</p></td>
</tr>
<tr>
<td><p><code>close()</code></p></td>
<td><p>Called when the report filling process is done with the data source.</p></td>
</tr>
<tr>
<td><p><code>cancelQuery()</code></p></td>
<td><p>Called to clean up resources if the report filling process is interrupted.</p></td>
</tr>
</tbody>
</table>

Query Executers must be registered with the JasperReports Library before use. For instructions and source code examples, see [Webscraper Custom Data Source](custom-data-source-examples.md).

### Implementing Optional Domain Support

To use your custom data source in Domains and Ad Hoc views, you must implement the `CustomDomainMetaData` interface.

<table>
<thead>
<tr>
<th colspan="3"><p>Optional Domain MetaData Interfaces</p></th>
</tr>
<tr>
<th><p>Interface</p></th>
<th><p>Method to Implement</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="4"><code>CustomDomainMetaData</code></td>
<td><p><code>getFieldMapping()</code></p></td>
<td>Mapping between names in the data source and names to show in the Domain, as key value pairs.</td>
</tr>
<tr>
<td><code>getJRFieldList()</code></td>
<td><p>Returns the list of <code>JRFieldName</code> (name, type, description), equivalent to columns, for your custom data source.</p></td>
</tr>
<tr>
<td><code>getQueryLanguage()</code></td>
<td>Returns the query language specified in the query executor you are using.</td>
</tr>
<tr>
<td><code>getQueryText()</code></td>
<td>Returns the query text used by the custom data source.</td>
</tr>
</tbody>
</table>

For source code examples, see the links to Java files in [Custom Data Source Pro](custom-data-source-examples.md) and [Pre-installed Data Source Types](pre-installed-data-sources.md).

## Defining the Custom Data Source in Spring

To configure your data source, you must add a Spring bean that references the `customDataSourceFactory` so that it will be visible to the server at run time. To do this, create a new file in the web application:

`.../WEB-INF/applicationContext-<name>.xml`

Within this file, there are two ways to configure your data source:

-   If you implemented the `ReportDataSourceService` interface, use the `CustomDataSourceDefinition` class.

-   If your data source extends `DataAdapterDefinition`, you can configure your data source as a data adapter.

### Using CustomDataSourceDefinition

This class has the following properties:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><p>Properties of <code>CustomDataSourceDefinition</code> Class</p></th>
</tr>
<tr>
<th><p>Name</p></th>
<th><p>Required</p></th>
<th><p>Value</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>factory</code></p></td>
<td><p>Yes</p></td>
<td><p>A fixed value of <code>ref="customDataSourceFactory"</code></p>
<p>This bean manages all the custom data sources.</p></td>
</tr>
<tr>
<td><p><code>name</code></p></td>
<td><p>Yes</p></td>
<td><p>A unique name that identifies this data source to the custom data source framework. It is also used as a prefix for all messages in the message catalog. Choose the name that is not used by other custom data sources.</p></td>
</tr>
<tr>
<td><p><code>serviceClassName</code></p></td>
<td><p>Yes</p></td>
<td><p>The class name for your <code>ReportDataSourceService</code> implementation.</p></td>
</tr>
<tr>
<td><p><code>validator</code></p></td>
<td><p>—</p></td>
<td><p>An instance of your <code>CustomDataSourceValidator</code> implementation.</p></td>
</tr>
<tr>
<td><p><code>property</code><br />
<code>Definitions</code></p></td>
<td><p>—</p></td>
<td><p>Information describing each property used by the data source implementation, structured as a list of maps. See the table below.</p></td>
</tr>
</tbody>
</table>

The `propertyDefinitions` property is a list of maps, each one describing a property of the custom data source implementation. Each map includes these entry keys:

<table>
<thead>
<tr>
<th colspan="3"><p>Entry Keys for <code>propertyDefinitions</code> Property</p></th>
</tr>
<tr>
<th><p>Name</p></th>
<th><p>Required</p></th>
<th><p>Value</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>name</code></p></td>
<td><p>Yes</p></td>
<td><p>Name of property that matches a Java Bean property in the <code>ReportDataSourceService</code> implementation; also used in message catalog keys.</p></td>
</tr>
<tr>
<td><p><code>default</code></p></td>
<td><p>—</p></td>
<td><p>A default value for the property.</p></td>
</tr>
<tr>
<td><p><code>hidden</code></p></td>
<td><p>—</p></td>
<td><p>If a property has the <code>hidden</code> entry key set to <code>true</code>, then its value is fixed to that of the <code>default</code> entry key. Such properties are not visible in the <strong>New Data Source</strong> dialog, nor are they persisted. This is handy for making Spring beans accessible to <code>ReportDataSourceService</code> implementations.</p></td>
</tr>
</tbody>
</table>

The following XML defines a `CustomDataSourceDefinition` bean for the custom bean data source example:

``` xml
<bean id="myCustomDataSource" class="com.jaspersoft.jasperserver.api.engine.jasperreports.util.CustomDataSourceDefinition">
  <property name="factory" ref="customDataSourceServiceFactory"/>
  <property name="name" value="myCustomDataSource"/>
  <property name="serviceClassName" value="example.cds.    CustomSimplifiedDataSourceService"/>
  <property name="validator">
    <bean class="example.cds.CustomTestValidator"/>
  </property>
  <property name="propertyDefinitions">
    <list>
      <map>
        <entry key="name" value="foo"/>
      </map>
      <map>
        <entry key="name" value="bar"/>
        <entry key="default" value="b"/>
      </map>
      <map>
        <entry key="name" value="repository"/>
        <entry key="hidden" value="true"/>
        <entry key="default" value-ref="repositoryService"/>
      </map>
    </list>
  </property>
</bean>
```

### Using a Data Adapter

You can create a custom data source based on a data adapter in JasperReports Library. In this case, your query executer gets the custom data source properties from the data adapter.

To do this, you must first create an instance of your class in your custom data source definition Java code, implementing any additional properties you want:

``` java
public class MyCustomDataSourceDefinition extends DataAdapterDefinition {
...
}
```

Then you must create a bean for the data source in your XML file, using the class you defined in your Java file. In addition, you must specify the correct data adapter implementation in your `dataAdapterClassName` property. For example, the following XML defines a bean for the Mongo DB Query example:

``` xml
<bean id="mongoDBQueryDataSource" class="example.cdspro.MongoDbDataSourceDefinition">
  <property name="factory" ref="customDataSourceServiceFactory"/>
  <property name="name" value="mongoDBQueryDataSource"/>
  <property name="dataAdapterClassName" value="com.jaspersoft.mongodb.adapter.MongoDbDataAdapterImpl"/>
</bean>
```

## Defining the Message Catalog

The message catalog contains labels and messages displayed in the New Data Source dialog when creating and editing custom data source instances. The various types of messages are shown in the following table, along with message naming conventions:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th colspan="2"><p>Messages about Instances of Custom Data Sources</p></th>
</tr>
<tr>
<th><p>Message Type</p></th>
<th><p>Naming Convention</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Name of the custom data source type</p></td>
<td><p><code>&lt;cdsname&gt;.name</code> where <code>&lt;cdsname&gt;</code> is the value of the name property of the custom data source in its Spring definition.</p></td>
</tr>
<tr>
<td><p>Name of the custom data source property</p></td>
<td><p><code>&lt;cdsname&gt;.properties.&lt;propname&gt;</code> where <code>&lt;propname&gt;</code> is the name of the property that the user must define when creating a custom data source.</p></td>
</tr>
<tr>
<td><p>Validation messages</p></td>
<td><p><code>&lt;cdsname&gt;.&lt;propname&gt;.&lt;error&gt;</code> where <code>&lt;propname&gt;</code> is the name of the property that is invalid, and <code>&lt;error&gt;</code> is the type of error.</p>
<p>The <code>CustomDataSourceValidator</code> implementation will call <code>errors.rejectValue()</code> for errors detected in property values for the custom data source. The second argument to <code>errors.rejectValue()</code> must match one of the messages defined in this catalog.</p></td>
</tr>
<tr>
<td>Query language</td>
<td><code>query.language.&lt;qlname&gt;.label</code> where <code>&lt;qlname&gt;</code> is the name of the query language. Define this property if you implement the optional query language and want to give your query language a different name, or want to have localized names for it in a bundle.</td>
</tr>
</tbody>
</table>

For example, the webscraper message catalog contains the following:

``` properties
webScraperDataSource.name=Web Scraper Data Source
webScraperDataSource.properties.url=URL
webScraperDataSource.properties.path=DOM Path
webScraperDataSource.url.required=A value is required for the URL
webScraperDataSource.path.required=A value is required for the DOM path
```

If you use your JasperReports Server in multiple languages, you can provide multiple copies of the message catalog, with translated strings (known as a message bundle). Each file name contains the locale to which it applies, according to the Java convention, for example `cdstest_fr.properties`. By convention, all message catalogs or bundles are stored in:

`.../WEB-INF/bundles`

To configure your message catalog, add a bean definition such as the following to the Spring definition file that you created in Defining the Custom Data Source in Spring:

``` xml
<bean class="com.jaspersoft.jasperserver.api.common.util.spring.GenericBeanUpdater">
  <property name="definition" ref="addMessageCatalog"/>
  <property name="value" value="WEB-INF/bundles/cdstest"/>
</bean>
```

For the `value` property, specify the path and name of your message catalog file, omitting the `.properties` extension.

## Adding the Custom Query Language to the UI

If you implemented the optional Query Executer, you must add it to the Spring configuration to make the query language for your custom data source definition appear in the UI. Query languages can be selected from a drop down list when defining query resources such as query-based input controls. The server matches the name of the query language to your data source to use its custom query executor class.

If you are using a commercial edition of JasperReports Server, edit the file `.../WEB-INF/applicationContext-pro-remote-services.xml` and locate the `queryLanguagesPro` bean. Add the name of your query language to the list, for example:

``` xml
    <bean id="queryLanguagesPro" parent="queryLanguagesCe"
          class="org.springframework.beans.factory.config.ListFactoryBean">
        <property name="sourceList">
            <list merge="true">
                <value>sl</value>
                <value>MyQueryLanguage</value>
            </list>
        </property>
    </bean>
```

If you are using the community edition of JasperReports Server, edit the file `.../WEB-INF/applicationContext-remote-services.xml` and locate the `queryLanguagesCe` list. Add the name of your query language to the list, for example:

``` xml
    <util:list id="queryLanguagesCe">
        <value>sql</value>
        <value>hql</value>
        <value>domain</value>
        <value>HiveQL</value>
        <value>MongoDbQuery</value>
        <value>cql</value>
        <value>MyQueryLanguage</value>
    </util:list>
```

The name must be a language supported by your query executor.

Alternatively, you can add your query executor as a separate bean without modifying the existing Spring configuration. In that case you would:

-   Create a bean similar to `queryLanguagesPro` above, but that extends `queryLanguagesPro` if you are using a commercial edition. Save this bean with `id=customQueryLanguage` in a file named `.../WEB-INF/applicationContext-customQueryLang.xml`. Of course, you can use your own names for the id and file name.

-   Edit the file `.../WEB-INF/js.spring.properties` and modify the following line:

``` properties
bean.queryLanguages=queryLanguagesPro
```

so that it references the id of your new bean, for example:

``` properties
bean.queryLanguages=customQueryLanguage
```

After editing and saving the files, restart JasperReports Server.

## Installing a Custom Data Source Type

To install your custom data source type in JasperReports Server, add all the files it requires to the server web application directory. For the correct locations, refer to Files Used by a Custom Data Source Implementation.

After adding the files and making the configuration changes specified in the previous sections, restart JasperReports Server.

## Using a Custom Data Source Type

When you create a new data source type in JasperReports Server, it appears in the list of available types in the New Data Source dialog. If the custom data source is not listed as an available data source type, the custom data source is not properly installed.

When the new type is selected, JasperReports Server displays the fields and labels for the visible properties you configured. Users may enter values directly, or they may use attribute syntax to specify user, organization, or system attribute values. The server resolves any attribute values before passing the values to your `ReportDataSourceService` at run time.

When the form is submitted, the property values are validated with your optional `CustomDataSourceValidator` implementation and appropriate validation messages are displayed. Once the data source is validated, you can save it to the repository. The data source can now be used in a JRXML report. When you run a JRXML report, Domain, Ad Hoc view, or dashboard that uses this data source, the saved property values are used by your `ReportDataSourceService` implementation to instantiate your `JRDataSource` which then provides the data to run the report.
