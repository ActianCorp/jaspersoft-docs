---
title: Using JasperReports Extensions in Jaspersoft Studio
description: "JasperReports provides several ways to extend its functionality. In general, extensions (like components, fonts, query executors, chart themes) are packaged in JARs. To use these extensions in..."
---

# Using JasperReports Extensions in Jaspersoft Studio

JasperReports provides several ways to extend its functionality. In general, extensions (like components, fonts, query executors, chart themes) are packaged in JARs. To use these extensions in Jaspersoft Studio, add the required JARs to the Jaspersoft Studio classpath. The Jaspersoft Studio classpath is composed of static and reloadable paths. Extensions must be set as static paths, while objects that do not require a proper descriptor or special loading mechanism (such as scriptlets and custom data sources) can be reloadable.
