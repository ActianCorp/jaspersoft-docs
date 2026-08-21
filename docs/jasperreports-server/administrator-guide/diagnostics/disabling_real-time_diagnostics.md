---
title: Disabling Real-Time Diagnostics
description: "By default the JMX diagnostic subsystem is always enabled, but external access is password-protected and requires opening the diagnostic port in your firewall as described in Exposing Diagnostics..."
---

# Disabling Real-Time Diagnostics

By default the JMX diagnostic subsystem is always enabled, but external access is password-protected and requires opening the diagnostic port in your firewall as described in [Exposing Diagnostics Through Jaspersoft's JMX Agent](jaspersofts_jmx_agent.md). If you wish to disable all external access, see [Disabling Remote Connections to the JMX Agent](jaspersofts_jmx_agent.md).

Internally, the diagnostics subsystem is passive and has no performance impact until it is accessed in a report through the diagnostic data source. However, if you wish to disable real-time diagnostics entirely, rename or remove the following files:

- `.../WEB-INF/applicationContext-diagnostic.xml`
- `.../WEB-INF/applicationContext-diagnostic-pro.xml`

In that case, the diagnostic data source, the sample report, and the sample Topic described in [Using the Diagnostic Data in Reports](using_the_diagnostic_data_in_reports.md) will not function either. They can be deleted from the repository.
