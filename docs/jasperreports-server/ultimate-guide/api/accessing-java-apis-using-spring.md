---
title: Accessing API Implementations Using the Spring Framework
description: "Many of the implementations of the API interfaces are singletons, usually services instantiated by the Spring Framework. The Spring bean configuration files control how these singletons are created..."
---

# Accessing API Implementations Using the Spring Framework

Many of the implementations of the API interfaces are singletons, usually services instantiated by the Spring Framework. The Spring bean configuration files control how these singletons are created and configured, so it's important to understand the files before writing Java code that will run in JasperReports Server using the API.

The following is a brief overview of Spring 5.3.29 and is not meant to cover all the possible ways to configure Spring. For more information on Spring, refer to its reference documentation at <https://docs.spring.io/spring-framework/docs/5.3.29/reference/html/>.

The Spring configuration files use XML to define Java singleton instances, called beans. In the JasperReports Server web application, these files are located in the WEB-INF directory. Their file names begin with applicationContext and end in .xml. For example, the file `WEB-INF/applicationContext-adhoc.xml` contains Ad Hoc-related beans:

-   Each instance of a singleton is defined by a `<bean>` element.

-   Its type is specified by the `class` attribute.

-   Its reference ID is specified by the `id` attribute.

-   Properties of the instance are set with the `<property>` element: JasperReports Server.

-   The `name` attribute corresponds to a Java property that follows JavaBean conventions. For example, a property with name `abc` should have a getter method `getAbc()` and a setter method `setAbc()`.

-   Using the `value` attribute, properties can be set with a constant value.

-   Using the `ref` attribute, properties can be set with a reference to another bean.

Below is part of a definition from a sample custom data source implementation. It demonstrates all the conventions above. The original file is `samples/customDataSource/webapp/WEB-INF/applicationContext-hibernateDS.xml` in the JasperReports Server distribution.

``` text
<!-- define a custom data source -->
<bean id="hibernateDataSource" class="com.jaspersoft.jasperserver.api.engine.jasperreports.util.  CustomDataSourceDefinition">
    <!-- this property is always the same; it registers the custom ds -->
    <property name="factory" ref="customDataSourceServiceFactory"/>
    <!-- name used in message catalog and elsewhere -->
    <property name="name" value="hibernateDataSource"/>
```

To add your own instances to the server, you first need information about the specific enhancement you want to implement. This determines which Java implementations are required. A good example is creating a custom data source, which is documented in [Chapter 1, “Custom Data Sources,” on page 1](../custom_data_sources/custom-datasources.md).

Once you have a Java class you want to instantiate along with JasperReports Server, you can deploy it by modifying the webapp directory as follows:

-   Add your compiled Java class files to `WEB-INF/classes`, or create a JAR and add it to `WEB-INF/lib`.

-   Create a new Spring bean file under `WEB-INF`, using the naming convention described above.

-   Add a `<bean>` element for each object instance you want to create.

-   For each property you want to set, you must have a public setter and getter.

-   For each API implementation you want to access:

    -   Add a setter and getter to your implementation. Their types must match the Java type of the API.

    -   Find out the ID of the API instance you want. Some IDs are listed in the table below.

    -   Add a `<property>` element to your bean with a `ref` attribute whose value is the ID of the API instance.

As an example of a reference to another bean, please refer to the `factory` property in the Spring file excerpt above. The `CustomDataSourceDefinition` instance uses the `factory` property to refer to a singleton implementation of `CustomReportDataSourceServiceFactory`, which has a bean ID of `custom-DataSourceServiceFactory`:

-   The `CustomDataSourceDefinition` implementation defines a factory JavaBean property by implementing the following setter and getter:

    -   `public void setFactory(CustomReportDataSourceServiceFactory factory)`.
    -   `public CustomReportDataSourceServiceFactory getFactory()`.

-   The `<bean>` element contains a `<property>` element with `name` set to `factory` and `ref` set to `customDataSourceServiceFactory`.

The following table contains the APIs described in the rest of this section, along with their corresponding bean IDs and descriptions of their functions.

**JasperReports Server Public Java API**

| API | Bean ID | Function |
|----|----|----|
| RepositoryService | `repositoryService` | Search, retrieve, and modify persistent objects in the repository. |
| EngineService | `engineService` | Run reports and handle report metadata. |
| ReportDataSourceService and ReportDataSourceServiceFactory | n/a | Implement data sources used for running reports and other purposes. |
| ReportSchedulingService | `reportSchedulingService` | Manage report schedules. |
| UserAuthorityService | `userAuthorityService` | Manage internal users and roles. |
| OlapConnectionService | `olapConnectionService` | Manage OLAP-specific repository and model runtime. |
| OlapManagementService | `olapManagementService` | Manage OLAP server run time. |
| ObjectPermissionService | `objectPermissionService` | Search, retrieve, and modify metadata repository object permissions. |
