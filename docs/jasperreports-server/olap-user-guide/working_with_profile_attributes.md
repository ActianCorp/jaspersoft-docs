---
title: Working with Attributes
description: "The Manage menu only appears if you have an administrative role, such as ROLEADMINISTRATOR (for the all editions) and ROLESUPERUSER (for commercial editions). In commercial editions with a single..."
---

# Working with Attributes

!!! note

    The **Manage** menu only appears if you have an administrative role, such as ROLE_ADMINISTRATOR (for the all editions) and ROLE_SUPERUSER (for commercial editions). In commercial editions with a single organization, the **Manage &gt; Server Settings** menu can be made available to the jasperadmin account by assigning it ROLE_SUPERUSER; otherwise, only superuser can access the Server Settings page.

Attributes can be defined for each JasperReports Server user, organization, or server instance. They are used to categorize or tag these to define security rules around data. Administrators can view and edit attributes on the administration pages; for example:

-   On the **Manage &gt; Users** page, edit a user and click **Attributes** to define attributes that control the data displayed to that user.

-   On the **Manage &gt; Organizations** page, edit an organization and click **Attributes** to define attributes that control the data displayed to users who belong to that organization.

-   On the **Manage &gt; Server Settings** page, click **Server Attributes** to define attributes that control the data returned by this server instance.

For more information on attributes, refer to the JasperReports Server Administrator Guide and the JasperReports Server Security Guide. For a detailed example of data-level security, including a complete example of cube security based on attributes and roles, refer to the Jaspersoft OLAP Ultimate Guide.
