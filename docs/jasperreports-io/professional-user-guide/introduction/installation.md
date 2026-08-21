---
title: Installing JasperReports IO Using the Standalone Package
description: "The JasperReports IO service can run a maximum of 2, 5, or 10 reports concurrently, depending on your license. The following table contains the recommended system requirements for JasperReports IO..."
---

# Installing JasperReports IO Using the Standalone Package

## System Requirements

The JasperReports IO service can run a maximum of 2, 5, or 10 reports concurrently, depending on your license. The following table contains the recommended system requirements for JasperReports IO based on the maximum number of concurrent report runs:

|                                |             |               |
|--------------------------------|-------------|---------------|
| Maximum Concurrent Report Runs | Processor   | RAM           |
| 2                              | 1 - 2 cores | 512 MB - 2 GB |
| 5                              | 2 - 4 cores | 2 GB - 4 GB   |
| 10                             | 2 - 4 cores | 4 GB - 8 GB   |

## Starting JasperReports IO

JasperReports IO is available as a standalone ZIP package, downloadable from jaspersoft.com.

Different download packages are available for Windows, Linux, and macOS.

This installation package contains all the services and components needed for creating your own client applications and embeddable reports, including the JasperReports IO Professional reporting service, the JavaScript API, a web server, a sample web application, data source adapters, and a Java Runtime Environment. The reporting service and sample web application are deployed when you start the web server. The sample web application helps you get started with creating your own application by demonstrating the capabilities of the JasperReports IO reporting service and the JasperReports IO JavaScript API.

See [Managing JasperReports IO](../managing_jrio/managing_jrio.md) for information on the content and directory structure of JasperReports IO.

To start the JasperReports IO reporting service

1.  Download the standalone package for your machine's operating system.
2.  Extract the standalone package and open the extracted folder.
3.  Run the start script to launch the web server.
4.  If you are using Windows, run the `start.bat` script.
5.  If you are using Linux or macOS, run `start.sh`.

The script starts the web server. The JasperReports IO web application is ready for use.

1.  To test the demo web application, open a browser and go to the following URL: `http://localhost:8080`.

The browser opens the sample JasperReports IO web application. The sample application displays details about how to work with JasperReports IO.

1.  To shut down the web server, run the stop script.

<!-- -->

1.  If you are using Windows, run the `stop.bat` script.
2.  If you are using Linux or macOS, run `stop.sh`.
