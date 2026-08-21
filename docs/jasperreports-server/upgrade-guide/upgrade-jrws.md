---
title: Upgrade JasperReports Web Studio
description: "These are the steps to upgrade JasperReports Web Studio:"
---

# Upgrade JasperReports Web Studio

These are the steps to upgrade JasperReports Web Studio:

1.  Stop Tomcat.

2.  Unzip `jasperserver-pro.war` present in the `js-jrs_10.0.0_bin.zip` package and replace the `tomcat/webapps/jasperserver-pro/jrws` folder with one provided by `jasperserver-pro.war`.

3.  Unzip `jrws-repository-jrs.war` into the `tomcat/webapps/repo` folder.

4.  Unzip `jrws-jrio-jrs.war` into the `tomcat/webapps/jrio` folder.

5.  Start Tomcat.
