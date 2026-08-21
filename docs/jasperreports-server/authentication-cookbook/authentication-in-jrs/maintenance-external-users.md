---
title: Maintenance of External Users
description: The advantage of an external authority is that it provides a single place to manage user accounts across applications. So JasperReports Server can use the same login information you maintain for your...
---

# Maintenance of External Users

The advantage of an external authority is that it provides a single place to manage user accounts across applications. So JasperReports Server can use the same login information you maintain for your other applications. When a user logs in, the server receives the username then maps the roles and organization. If these have changed from the previous login, the server can synchronize the locally stored external user information.

However, external authentication does not actively replicate the contents of the external authority in JasperReports Server. If users are deleted from the external authority, or role definitions change, JasperReports Server’s local information is not updated with these changes. The external user or role definitions remain in the server’s internal database, but authentication is still secure because they can't be used to log in.

In general, the mapping and synchronization maintain the external users and roles in JasperReports Server, but administrators must handle new roles, and you may want to cleanup deleted users, as explained in the following sections.
