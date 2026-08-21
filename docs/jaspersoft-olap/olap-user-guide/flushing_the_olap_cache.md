---
title: Flushing the OLAP Cache
description: "The Manage menu only appears if you have an administrative role, such as ROLEADMINISTRATOR (for the all editions) and ROLESUPERUSER (for commercial editions). In commercial editions with a single..."
---

# Flushing the OLAP Cache

!!! note

    The **Manage** menu only appears if you have an administrative role, such as ROLE_ADMINISTRATOR (for the all editions) and ROLE_SUPERUSER (for commercial editions). In commercial editions with a single organization, the **Manage \> Server Settings** menu can be made available to the jasperadmin account by assigning it ROLE_SUPERUSER; otherwise, only superuser can access the Server Settings page.

This option clears the in-memory cache that Mondrian builds. Caching is used to improve query performance. Flushing the cache is not usually necessary except when an underlying data in the database changes. For example, after running an ETL process, the cache is out of date; it may not match the data in the database.

Such data changes are not reflected in OLAP views until the application server is restarted or until the cache is flushed.

To flush the cache, click **Manage \> Server Settings**, click **OLAP Settings,** and click **Flush OLAP Cache** near the top of the page.

The OLAP cache is also automatically flushed when an existing Mondrian connection or one of its components (such as the schema or data source) is changed in the repository.

For more information on caching, see the Jaspersoft OLAP Ultimate Guide and the JasperReports Server Administrator Guide.
