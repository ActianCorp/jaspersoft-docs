---
title: The permission Service
description: The permission service lets you view and set access permission on repository folders and resources. Only administrative users and users granted the Administer permission may view and set permissions.
---

# The permission Service

The permission service lets you view and set access permission on repository folders and resources. Only administrative users and users granted the Administer permission may view and set permissions.

As it is implemented, the permission service returns and sets only explicit permissions on resources. The lack of an explicit permission for a given role or user means that the permission is inherited from its parent folder. To find the value of inherited permissions on a given resource, you must obtain the permissions of all of its parent folders.
