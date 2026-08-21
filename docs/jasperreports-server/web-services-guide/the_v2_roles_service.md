---
title: The v2/roles Service
description: "The restv2/roles service replaces the rest/role service. It provides similar methods that allow you to list, view, create, modify, and delete roles. The new service provides improved search..."
---

# The v2/roles Service

The rest_v2/roles service replaces the rest/role service. It provides similar methods that allow you to list, view, create, modify, and delete roles. The new service provides improved search functionality, including user-based role searches. Every method has two URL forms, one with an organization ID and one without.

Because the role ID and organization ID are used in the URL, this service can operate only on roles and organizations whose ID is less than 100 characters long and does not contain spaces or special symbols. Unlike resource IDs, the role ID is the role name and can be modified.
