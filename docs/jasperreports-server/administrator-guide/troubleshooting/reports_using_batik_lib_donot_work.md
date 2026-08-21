---
title: Reports Using Batik Libraries Fail
description: "If you have upgraded JasperReports Server to 9.0, on running JRXML reports, using Batik libraries, the NullPointerException error is triggered. The report functioned correctly in the earlier versions..."
---

# Reports Using Batik Libraries Fail

If you have upgraded JasperReports Server to 9.0, on running JRXML reports, using Batik libraries, the `NullPointerException` error is triggered. The report functioned correctly in the earlier versions of JasperReports Server.

To fix this issue, Batik security restriction should be turned off.

To turn off the security restriction, set `net.sf.jasperreports.svg.allow.external.resources=true` in the `WEB-INF/classes/jasperreports.properties` file.
