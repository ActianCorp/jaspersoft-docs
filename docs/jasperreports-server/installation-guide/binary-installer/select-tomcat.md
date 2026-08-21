---
title: Selecting a Tomcat Configuration
description: JasperReports Server requires an application server. The installer is configured to run with the Apache Tomcat server. You can choose to use a bundled Tomcat or an existing Tomcat.
---

# Selecting a Tomcat Configuration

JasperReports Server requires an application server. The installer is configured to run with the Apache Tomcat server. You can choose to use a bundled Tomcat or an existing Tomcat.

## Bundled Tomcat

If you select **I want to use the bundled Tomcat**, the installer puts an instance of Tomcat onto your system. If you are prompted for Tomcat's server port and shutdown port, you can accept the default values or enter alternate values. If a port is already in use, you receive an error. The installer looks for open Tomcat ports from 8080 up.

## Existing Tomcat

If you want to use an existing Tomcat application server, **I want to use an existing Tomcat**. **Later you** are prompted for the location of Tomcat. Browse to the folder where you installed Tomcat. Make sure that the existing Tomcat is not running. When you are prompted for Tomcat's server port and shutdown port, you can accept the default values or enter alternate values.
