---
title: The v2/users Service
description: "The restv2/users service replaces the rest/user service. It provides similar methods that allow you to list, view, create, modify, and delete user accounts, including setting role membership. The new..."
---

# The v2/users Service

The rest_v2/users service replaces the rest/user service. It provides similar methods that allow you to list, view, create, modify, and delete user accounts, including setting role membership. The new service provides improved search functionality, such as organization-based searches in commercial editions licensed to use organizations. Every method has two URL forms, one with an organization ID and one without.

Because the user ID and organization ID are used in the URL, this service can operate only on users and organizations whose ID is less than 100 characters long and does not contain spaces or special symbols. As with resource IDs, the user ID is permanent and cannot be modified for the life of the user account.
