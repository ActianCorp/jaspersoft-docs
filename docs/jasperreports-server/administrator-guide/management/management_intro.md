---
title: User and Role Management
description: "In a single-organization deployment, the administrator needs to create only the users and roles. In deployments with multiple organizations, administrators need to create organizations, populate them..."
---

# User and Role Management

In a single-organization deployment, the administrator needs to create only the users and roles. In deployments with multiple organizations, administrators need to create organizations, populate them with users, and create the roles they use afterward to set access permissions. Optionally, administrators can also define attributes to control access to data.

In a deployment with multiple organizations, there can be administrators at every level of the hierarchy, as described in [Delegated Administration](../overview/users_and_roles.md). Part of any large deployment is to designate the administrators responsible for every task. For example, system administrators might set up the top-level organizations and default roles, but each organization's admin would then create and manage the users of their particular organization.

The interface in JasperReports Server for managing organizations, users, and roles accommodate all levels of administrators. This makes it easy for them to search among hundreds of users and roles, whether in a single organization or spread across many. The interface also enforces the scope of administrative privileges. For example, it ensures that an organization administrator cannot see roles and users from parent organizations.

Attributes are name-value pairs that can be defined on users, organizations, and at the server level. These values can provide flexibility, for example allowing each organization to access a different database when using the same data source. At the user level, attributes can provide data-level security when combined with the features of Domains and OLAP.

This chapter contains the following sections:

- [Managing Organizations](managing_organizations.md)
- [Managing Users](managing_users.md)
- [Managing Roles](managing_roles.md)
- [Managing Attributes](managing_attributes.md)
