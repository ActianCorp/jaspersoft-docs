---
title: Changes in 8.0 That May Affect Your Upgrade
description: "The Split installation has been introduced from this release. The Audit, Access, and Monitoring events can be moved to a different audit database using the Split installation or upgrade, which..."
---

# Changes in 8.0 That May Affect Your Upgrade

## Split Installation Updates

The Split installation has been introduced from this release. The Audit, Access, and Monitoring events can be moved to a different audit database using the Split installation or upgrade, which improves the performance of JasperReports server.

You have the option to choose from the following installations:

- Compact installation: The Repository, Audit, Access, and Monitoring tables are created in the repository database.
- Split installation: The Repository tables are created in the repository database. The Audit, Access, and Monitoring tables are created in a different audit database other than the repository database.

The default installation is the Compact installation.

!!! note

    With this release, the **jiaccessevent.user_id** type has been changed from numeric (integer data type) to a field (text data type). Due to this change, after the upgrade to version 8.0, you need to recreate any visualizations or domains that have the **user_id** column to display the data of the column.
