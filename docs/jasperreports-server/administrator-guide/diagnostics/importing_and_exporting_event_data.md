---
title: Importing and Exporting Event Data
description: Audit and monitoring data can be imported and exported with the utilities described in the chapter Import and Export.
---

# Importing and Exporting Event Data

Audit and monitoring data can be imported and exported with the utilities described in the chapter [Import and Export](../importexport/importexport_intro.md).

- To export audit data, use the `--include-audit-events` option in the export command.
- To export monitoring data use the `--include-monitoring-events` option in the export command.
- To import audit data, import the catalog containing audit data with the `--include-audit-events` option.
- To import monitoring data, import the catalog containing audit data with the `--include-monitoring-events` option.

!!! note

    Data in temp folders is not exported.
