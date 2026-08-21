---
title: Internal Users
description: "Even when you enable external authentication, JasperReports Server supports internal users, especially administrative users. For example, you can still define superuser and jasperadmin internally...."
---

# Internal Users

Even when you enable external authentication, JasperReports Server supports internal users, especially administrative users. For example, you can still define `superuser` and `jasperadmin` internally. Internal users cannot login through a separate external login screen. They can log in only through the JasperReports Server login screen, for example at http://localhost:8080/jasperserver-pro/login.html. Internal administrators such as `superuser` may have access at the root organization level. They can also set internal permissions for external users, if necessary.

An external user can have the same username as an internal user in a different organization. But if this happens within an organization, the external user won’t be able to log into JasperReports Server.
