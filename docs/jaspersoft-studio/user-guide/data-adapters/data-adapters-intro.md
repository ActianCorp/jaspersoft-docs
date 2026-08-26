---
title: Data Adapters
description: "A data adapter is a resource that specifies how and where to obtain data. Specifically, it is an object that contains information about how to connect to or retrieve the data, and the logic to do..."
---

# Data Adapters

A data adapter is a resource that specifies how and where to obtain data. Specifically, it is an object that contains information about how to connect to or retrieve the data, and the logic to do that. Data adapters are stored in jrdax files and simplify porting of the report configuration and data source creation between JasperReports environments. Whether you use a report with a data adapter jrdax file in Jaspersoft Studio, publish it to JasperReports Server or deploy it to a custom JasperReports environment. JasperReports Library can use it to obtain the data you specify.

This chapter starts by telling you how to create and use data adapters based on the data adapter types available in Jaspersoft Studio. Data adapters are designed to simplify the complexities of working with data in the JasperReports Library. However, data adapters are only one of the ways that JasperReports Library can get data from a data source. As you get more familiar with Jaspersoft Studio, you may want to go a little deeper and learn about data in JasperReports Library and the `JRDataSource` interface.

Usually data adapters are stored as jrdax files in the same project as the report to simplify deployment to JasperReports Server or another environment. In Jaspersoft Studio, data adapters can also be stored in the Repository Explorer, in which case they are visible from all the projects. If you plan to deploy the report outside Jaspersoft Studio, it is better to store it in the project from the beginning.

This chapter has the following sections:

-   [Working with Data Adapters](data-adapters-creating.md)

-   [Using Data Adapters in Reports and Datasets](data-adapters-using-in-reports.md)

-   [Creating and Using Database JDBC Connections](data-adapters-jdbc-connection.md)

-   [Working with a Collection of JavaBeans Data Adapter](data-adapters-java-beans.md)

-   [Working with XML Data Adapters](data-adapters-xml.md)

-   [Using XML/A Data Adapters](data-adapters-xmla.md)

-   [Working with CSV Data Adapters](data-adapters-csv.md)

-   [Using the Empty Record Data Adapter](data-adapters-empty.md)

-   [Using the Random Data Adapter](data-adapters-random.md)

-   [Working with the JRDataSource Interface](data-adapters-jrdatasource.md)

-   [A Close Look at TIBCO Spotfire Information Links](data-adapters-spotfire-info-links.md)
