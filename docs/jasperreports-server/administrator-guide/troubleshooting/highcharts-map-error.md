---
title: Configuring Highcharts Maps for Non-Default Server Locations
description: "When JasperReports® Server is deployed on a non-default server location (any location/port other than localhost:8080), an error is displayed when creating or accessing a Highcharts Map component."
---

# Configuring Highcharts Maps for Non-Default Server Locations

When JasperReports® Server is deployed on a non-default server location (any location/port other than `localhost:8080`), an error is displayed when creating or accessing a Highcharts Map component.

To solve this, the Highcharts Map collection URL must be configured.

To configure the URL, add the `com.jaspersoft.jasperreports.highcharts.maps.collection.base.url=<url-to-the-highmaps-collection-folder>` property to the `jasperserver-pro/WEB-INF/classes/jasperreports.properties` file.

For example, `com.jaspersoft.jasperreports.highcharts.maps.collection.base.url=https://<hostname>:<port>/jasperserver-pro/highmaps`
