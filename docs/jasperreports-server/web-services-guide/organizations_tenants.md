---
title: Organizations/Tenants
description: "This section describes functionality that can be restricted by the software license for JasperReports Server. If you don’t see some of the options described in this section, your license may prohibit..."
---

# Organizations/Tenants

!!! info "Important"

    This section describes functionality that can be restricted by the software license for JasperReports Server. If you don’t see some of the options described in this section, your license may prohibit you from using them. To find out what you're licensed to use, or to upgrade your license, contact Jaspersoft.

At present, there is no practical difference between organizations and tenants; both kinds of entity are administered with these `tenant` operations:

-   `getTenant`. Returns a list of tenants that meet specified criteria.
-   `getSubTenantList`. Returns a list of sub-tenants (units within a tenant).
-   `putTenant`. Returns the named tenant. If the object is not already in the database, the call creates a new one.
-   `deleteTenant`. Deletes the named tenant.
