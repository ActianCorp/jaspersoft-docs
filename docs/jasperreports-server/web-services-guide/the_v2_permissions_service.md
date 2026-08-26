---
title: The v2/permissions Service
description: "In the REST v2/permissions service, the syntax is expanded so that you can specify the resource, the recipient (user name or role name) and the permission value within the URL. This makes it simpler..."
---

# The v2/permissions Service

In the REST v2/permissions service, the syntax is expanded so that you can specify the resource, the recipient (user name or role name) and the permission value within the URL. This makes it simpler to set permissions because you don’t need to send a resource descriptor to describe the permissions. In order to set, modify, or delete permissions, you must use credentials or login with a user that has “administer” permissions on the target resource.

The permissions for each user and each role are indicated by the following values. These values are not a true mask; they should be treated as constants:

-   No access: 0

    -   Administer: 1

    -   Read-only: 2

    -   Read-write: 6

    -   Read-delete: 18

    -   Read-write-delete: 30

    -   Execute-only: 32

        Because a permission can apply to either a user or a role, the permissions service uses the concept of a “recipient.” A recipient specifies whether the permission applies to a user or a role, and gives the ID of the user or role, including any organization, for example:

        role:ROLE_SUPERUSER (this is a root role and thus has no organization specified)

        user:joeuser\|organization_1

        Recipients are listed when viewing permissions, and they are also used to set a permission. A recipient can be specified in a URL parameter when allowed, but in this case, the vertical bar (\|) character must be encoded as %7C.

        There are two qualities of a permission:

-   The assigned permission is one that is set explicitly for a given resource and a given user or role. Not all permissions are assigned, in which case the permission is inherited from the parent folder.

-   The effective permission is the permission that is being enforced, whether it is assigned or inherited.

!!! note

    There is one permission that is not defined: you cannot read or write the ROLE_SUPERUSER's permission on the root .
