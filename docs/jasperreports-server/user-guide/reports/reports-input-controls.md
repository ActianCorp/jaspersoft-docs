---
title: Running a Report with Input Controls or Filters
description: An input control is graphical widgets that filter the data that appears in a report. The perfect input control limits the data to what you want to see—and nothing more. When you run a report based on...
---

# Running a Report with Input Controls or Filters

An input control is graphical widgets that filter the data that appears in a report. The perfect input control limits the data to what you want to see—and nothing more. When you run a report based on a Domain Topic that defines a filter, the server can render the filter as an input control. The JasperReports Server interface uses "input controls", "filters", and "options" interchangeably.

If your system administrator has enabled the data snapshot feature (described in [Data Snapshots](reports-column-menu.md)), it is important to note that the default input controls - that is, the input controls as defined when the original Jaspersoft Studio- or Ad Hoc View-based report is run - will overwrite any changes made to them the next time you run a report. For instance, suppose you run a report, update the input controls, then save the report. Later, when you run a report from the Jaspersoft Studio or Ad Hoc View source again. That new report replaces the report you ran earlier, and your input control changes are lost.

To avoid this, save a version of the report with your selected data preloaded. That way, when subsequent reports are run from the same source, they will not overwrite your report. See [Saving Input Control Values](reports-saving-input-controls.md) for more information.
