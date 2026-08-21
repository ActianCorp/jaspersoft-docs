---
title: Error with Manual WAR File Installation
description: "During a manual WAR file installation to migrate from earlier versions of JasperReports Server to 9.0.0, a user encountered errors when running minimal install script."
---

# Error with Manual WAR File Installation

During a manual WAR file installation to migrate from earlier versions of JasperReports Server to 9.0.0, a user encountered errors when running minimal install script.

These errors were successfully resolved by adding the following lines to the `context.xml` file:

- `jdbc/jasperserverSystemAnalytics`

- `jdbc/jasperserverAuditAnalytics`
