---
title: Multiple Organizations in JasperReports Server
description: "This section describes functionality that can be restricted by the software license for JasperReports Server. If you don’t see some of the options described in this section, your license may prohibit..."
---

# Multiple Organizations in JasperReports Server

!!! note

    This section describes functionality that can be restricted by the software license for JasperReports Server. If you don’t see some of the options described in this section, your license may prohibit you from using them. To find out what you're licensed to use, or to upgrade your license, contact Jaspersoft.

Some commercial editions allow several distinct organizations to coexist within the same server instance. Each organization, also known as a tenant, has its own users, roles, and possibly a hierarchy of sub-organizations, each of which is invisible to other organizations. For information about deploying multiple organizations, see the JasperReports Server Administrator Guide.

When you deploy JasperReports Server, there are three distinct cases with respect to the organization architecture:

| Edition and Usage | Impact on External Authentication Configuration |
|----|----|
| Commercial edition with multiple organizations | Configuring external authentication for multiple organizations requires extra steps. In the chapter for each authentication mechanism, look for the additional section on mapping the organization. All other configurations for external authentication remain the same. |
| Commercial edition with no organizations | When JasperReports Server has the organization architecture, but only implements a single default organization, the organization ID is mapped automatically. You can skip any section that refers to mapping the organization ID. |
| Community Project | JasperReports Server Community Project does not use the organization architecture. You can skip any section that refers to mapping the organization ID. |

!!! note

    Another name for multiple organizations is multi-tenancy, sometimes abbreviated `mt` in file and bean names. However, the `mt` prefix appears in both community and commercial editions.

## Default Admins in Organizations

You can set one or more default admins that are created when you create a new organization using external authentication. The sample files are set up to create a `jasperadmin` in each new organization by default. For information on how to customize default admin users, see the section on organizations in the chapter corresponding to your authentication mechanism.

!!! note

    Default admins for new organizations can be customized only when using external authentication. When you create organizations manually, the `jasperadmin` user is created.
