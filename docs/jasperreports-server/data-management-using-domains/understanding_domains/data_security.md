---
title: Data Security
description: "Domains may optionally define permissions that control access to data based on user names, roles, and attributes existing in the server. This allows you to create one Domain for all users, with..."
---

# Data Security

Domains may optionally define permissions that control access to data based on user names, roles, and attributes existing in the server. This allows you to create one Domain for all users, with access to sensitive data restricted by these permissions. Users may run the same report based on the Domain, but they will see only the data that they are allowed to access.

Permissions can be set separately on the data's columns and rows. In Domains, columns display the items in the Domain; rows display the values of each item. A user can see results only where they have both column- and row-level access. When a user is designing a report in the Ad Hoc Editor, they see only the columns to which they have access. When the report runs, portions to which the user has no access are blank.

Data security for a Domain is defined in a single security file. The file is attached to the Domain as a resource, as described in [The Security Tab](../domain_designer/security-tab.md). The security file references the `id`s of tables, columns, sets, and items in the Domain design. For more information, see [Securing Data in a Domain](../domain_security/securing_data_in_a_domain.md).
