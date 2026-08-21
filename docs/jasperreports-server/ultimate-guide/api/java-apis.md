---
title: The Public JasperReports Server API
description: "This section describes some of the important Java interfaces available in JasperReports Server, including commercial editions and Jaspersoft OLAP modules."
---

# The Public JasperReports Server API

This section describes some of the important Java interfaces available in JasperReports Server, including commercial editions and Jaspersoft OLAP modules.

A subset of the Java classes and interfaces in JasperReports Server has been designated as the public JasperReports Server API. These classes are marked with an `@JasperServerAPI` annotation, as demonstrated in the example below.

``` text
package com.jaspersoft.jasperserver.api.metadata.jasperreports.domain;
import com.jaspersoft.jasperserver.api.JasperServerAPI;
import com.jaspersoft.jasperserver.api.metadata.common.domain.DataSource;
@JasperServerAPI
public interface ReportDataSource extends DataSource
{
…
```

The JavaDoc for the JasperReports Server API classes can be downloaded from the Support Portal (for the commercial editions) or from the Jaspersoft community site (for the community project).

Classes included in the public API are more likely to be stable from release to release, so Java developers should use them in preference to other classes that are not part of the API. Note, however, that the public API is a small subset of all JasperReports Server classes, and does not provide all of the functionality you may need, in which case you must create and use other classes.

!!! note

    These JasperReports Server Java APIs are a contract between JasperReports Server (including Jaspersoft OLAP) and other applications and services that are exposed as Java interfaces. If the APIs change in the future, the changes will be gradual.
