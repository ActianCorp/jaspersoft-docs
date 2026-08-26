---
title: Custom Data Source Examples
description: "The WAR file installer includes several sample data source types in the <js‑install>/samples directory. You can build and deploy the examples after you have deployed JasperReports Server. These..."
---

# Custom Data Source Examples

The WAR file installer includes several sample data source types in the `<js‑install>/samples` directory. You can build and deploy the examples after you have deployed JasperReports Server. These samples include both the JasperReports Library data source implementation (`JRDataSource`) that contains the logic to access data and the interface to fill reports, and the implementation of `ReportDataSourceService` that allows the server to instantiate the `JRDataSource` at runtime.

These samples are not intended to be used in production environments. Modify and test these samples to understand how to create your own custom data source. The examples include:

-   Custom bean data source

-   Webscraper data source

-   Hibernate data source

-   Custom data source pro with metadata support for Domains

## Prerequisites

The samples directories include an Ant script that compiles the Java code for the samples and places all the required files in the correct locations in JasperReports Server. To run the Ant script, you need the correct versions of the Java Development Kit and Apache Ant.

Java Development Kit

The examples are provided as Java source files. To work with the examples, you must install the Java Development Kit (JDK). Ensure that the JAVA_HOME environment variable points to a full JDK installation. The samples are supported only with JDK 1.8.

Apache Ant

Ant is installed as part of the JasperReports Server installation process. Run Ant using the following command:

|              |                                                       |
|--------------|-------------------------------------------------------|
| **Linux:**   | `<js-install>/apache-ant/bin/ant <ant-arguments>`     |
| **Windows:** | `<js-install>\apache-ant\bin\ant.bat <ant-arguments>` |

If you cannot find Ant on your system, you can download it from <http://ant.apache.org>. The bundled Apache Ant is version 1.10.latest; the higher is recommended.

## Installing the Custom Data Source Examples

The `<js‑install>/samples/customDataSource` and `<js‑install>/samples/customDataSource-pro` directories include:

-   `readme.txt`: Text file describing how to build the examples.

-   `build.xml`: The Ant build file.

-   `src`: Java source directory.

-   `webapp`: A directory containing other files required by the examples, such as JSPs and Spring configuration files, which are copied directly to the JasperReports Server web application directory.

-   `reports`: A directory containing example JRXML files that use the sample custom data source types.

To install the samples in your JasperReports Server web application

1.  At the command line, change directories to the custom data source sample directory (`<js‑install>/samples/customDataSource`).
2.  Edit `build.xml` and set the `webAppDir` property to the root of your JasperReports Server web application.
3.  Run the Ant command (as described in Prerequisites) with no arguments. This executes the default target, which is named `deploy`. The `deploy` target initiates these actions:

-   Compiles the Java source files under the src directory.

-   Deploys the compiled Java class files to the web application.

-   Deploys files under the webapp directory to the web application.

!!! note

    See [Table 1-1, “Files Used by a Custom Data Source Implementation,” on page 1](custom-data-source-creation.md) for the final locations of the files in JasperReports Server

1.  Repeat this procedure for the sample in `<js‑install>/samples/customDataSource-pro`.
2.  For the webscraper report example, you must register its query executer factory as described in Webscraper Custom Data Source.
3.  Restart the application server.

The example custom data source types are now available from the New Data Source page in JasperReports Server.

To test the samples and create or view reports

1.  Log on to JasperReports Server as an administrator.
2.  Open the **New Data Source** page (for example, by selecting **Create &gt; Data Source** for the main menu), enter the required values for the data source type you selected, and save the data source. For more information about creating data sources, see the *JasperReports Server Administrator Guide*.
3.  To test a sample, upload the associated report from the `<js‑install>/samples/customDataSource/reports` directory and view the report.

Each of the examples is described in the following sections.

## Custom Bean Data Source

This custom data source shows how to create a data source type for a JasperReports Library data source (`JRDataSource`) implemented as a simple bean. It includes the following:

-   A `JRDataSource` implemented as an array of data declared in the source code.

-   The `ReportDataSourceService` code required by JasperReports Server to set up and tear down the `JRDataSource`.

-   The Spring bean definition file for the custom data source type:

    `<js‑install>/samples/customDataSource/webapp/WEB-INF/applicationContext‑sampleCDS.xml`

-   An example report that uses this data source type

    `<js‑install>/samples/customDataSource/reports/simpleCDS.jrxml`

## Webscraper Custom Data Source

The webscraper custom data source fetches a web page, decodes its HTML, and extracts selected data that is turned into field values in the data source. The Spring bean definition file for this custom data source type is located in:

` <js‑install>/samples/customDataSource/webapp/WEB-INF/applicationContext-webscraperDS.xml`

The webscraper data source type definition includes these elements:

-   URL: An HTTP URL that refers to the HTML page containing the desired content.

-   DOM path: An XPath expression that locates HTML elements to be turned into rows in the data source.

-   Field paths: XPath expressions for each field defined in the JRXML. JasperReports Server uses these paths to locate the field value in each row selected by the DOM path.

The data source takes two parameters: the URL of the web page and the XPath that determines how elements in the HTML page become rows in the data source. The parameters can either be specified by a data source definition in the repository or by a query string in the JRXML. The `<js-install>/samples/customDataSource/reports/webscrapertest.jrxml` report has no query. Instead, it relies on an instance of the custom data source that you must create in the repository. Set the URL and DOM Path according the website you are trying to access.

-   When a data source of this type is used in a report, dashboard, or Ad Hoc view, JasperReports Server creates a `JRDataSource` by:

    Using the URL to issue a GET request for an HTML page.

-   Converting the HTML response into XML using JTidy (<http://jtidy.sourceforge.net>).

-   Using the DOM path to select XML elements from the converted response.

-   Creating a new data source row for each selected element.

-   Determining the context for each field based on its field path.

!!! note

    Web sites are frequently redesigned and the URLs used by any website are subject to change. This can affect your reports.

In order to use the webscraper data source, you must first register the webscraper query executer factory. One way to do this is as follows:

1.  Install the samples using ant as described in Installing the Custom Data Source Examples.

2.  Open the file `.../WEB-INF/classes/jasperreports.properties` for editing.

3.  Add the following at the end of the file:

    ``` bash
    # registering query executer for webscraperQEtest.jrxml example
    net.sf.jasperreports.query.executer.factory.webscraper=example.cds.WebScraperQueryExecuterFactory
    ```

4.  Save the file.

5.  Restart your application server.

For more information about registering query executors, see the Report Query section in the *JasperReports Library Ultimate Guide*.

## Hibernate Custom Data Source

The Hibernate custom data source type implementation supports Hibernate Query Language (HQL) queries in report units in JasperReports Server. The Spring bean definition file and related Java code for the Hibernate custom data source example are in the following locations in the `<js‑install>/samples/customDataSource/` directory:

-   `webapp/WEB-INF/applicationContext-hibernateDS.xml`: Spring bean XML to configure the Hibernate data source

-   `src/example/cds/HibernateDataSourceService.java`: implementation of ReportDataSourceService for the data source

-   `src/example/cds/HibernateSessionFactoryFinder.java`: a helper class used to locate a `SessionFactory` instance for `HibernateDataSourceService`

    The implementation works with the JasperReports Library's support for HQL queries to create a data source. The library will use the `JRHibernateQueryExecuter` to run an HQL query in a report unit, and this query executer needs a Hibernate `Session` object. The Hibernate custom data source will create the session from a Hibernate `SessionFactory` configured as a Spring bean in JasperReports Server.

    The Hibernate data source configuration on the data source menu in JasperReports Server includes the following element:

-   Session Factory Bean Name: A `SessionFactory` created with a named Spring bean of class `SessionFactory`, `HibernateDaoSupport`, or one of their subclasses.

The sample Hibernate test report contains an HQL query on the JasperReports Server repository, which uses Hibernate internally.

To run the Hibernate data source example

1.  Install the samples using ant as described in Installing the Custom Data Source Examples.

2.  Create a new Hibernate data source:

    1.  Create a data source and select **Hibernate** for the type.
    2.  Enter `sessionFactory` for the name of the `SessionFactory` bean – this is the id of the repository's Hibernate `SessionFactory`.
    3.  Save the data source and give it a name when prompted.

3.  Upload and configure the sample report:

    1.  Navigate to the repository location where you want to save the report.
    2.  Right-click and select **Add Resource &gt; JasperReport**. The **Add JasperReport** page is displayed.
    3.  On the **Set Up** page, enter a name for the report unit.
    4.  Select **Upload a Local File**, click **Browse**, select `<js‑install>/samples/customDataSource/reports/hqlTest.jrxml`, and click **OK**.
    5.  On the **Data Source** page, click **Select data source from repository** and browse to the data source created in the previous step.
    6.  Click **Submit** to save the report.

4.  Run the new report, and it should show a list of resources in the repository.

## Custom Data Source Pro

The Custom Data Source Pro example works in commercial editions of JasperReports Server. It uses an additional class to expose metadata, so that the data source can be used in Domains and Ad Hoc views.

This example is located in the `<js‑install>/samples/customDataSource-pro` directory. It includes the following:

-   A `JRDataSource` implemented as an array of data declared in the source code.

-   The example implements Domain support using the `CustomDomainMetaData` class.

-   Its Spring bean definition file is located in:

`<js-install>/samples/customDataSource-pro/webapp/WEB-INF/applicationContext-sampleCDSWithMetData.xml`
