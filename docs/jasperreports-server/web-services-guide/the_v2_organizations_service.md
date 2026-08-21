---
title: The v2/organizations Service
description: "This section describes functionality that can be restricted by the software license for JasperReports Server. If you don’t see some of the options described in this section, your license may prohibit..."
---

# The v2/organizations Service

!!! info "Important"

    This section describes functionality that can be restricted by the software license for JasperReports Server. If you don’t see some of the options described in this section, your license may prohibit you from using them. To find out what you're licensed to use, or to upgrade your license, contact Jaspersoft.

In commercial editions of JasperReports Server 5.1 and later, the rest_v2/organizations service replaces the rest/organization service. It provides similar methods that allow you to list, view, create, modify, and delete organizations (also known as tenants). New functionality allows you to search for organizations by name and retrieve hierarchies of organizations.

Because the organization ID is used in the URL, this service can operate only on organizations whose ID is less than 100 characters long and does not contain spaces or special symbols. As with resource IDs, the organization ID is permanent and cannot be modified for the life of the organization.
