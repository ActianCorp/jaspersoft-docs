---
title: Users and Roles API
description: Access to all JasperReports Server functionality is based on assigned user-level and role-level permissions. So managing users and roles is a critical aspect of the public API.
---

# Users and Roles API

Access to all JasperReports Server functionality is based on assigned user-level and role-level permissions. So managing users and roles is a critical aspect of the public API.

The `com.jaspersoft.jasperserver.api.metadata.user.service.UserAuthorityService` interface has methods for creating, modifying, and removing users and roles. The API manipulates only these two types of entities for which public interfaces are available:

- Users: represented by the `com.jaspersoft.jasperserver.api.metadata.user.domain.User` interface.

- Roles: represented by the `com.jaspersoft.jasperserver.api.metadata.user.domain.Role` interface.

You can define a new user in a few easy steps:

``` text
User workingUser = userAuthService.newUser(null);
workingUser.setUsername("john");
workingUser.setTenantID("organization_1");
workingUser.setPassword("changeme");
workingUser.setFullName("John Doe");
workingUser.setEnabled(true);
workingUser.setExternallyDefined(false);
userAuthService.putUser(null, workingUser);
```

The `setTenantId` method specifies the organization that the user belongs to. However, note the following:

- If you are using commercial editions of JasperReports Server, you should use this method in most cases, but if your instance hosts only a single organization, this method should set most user’s organization to the default (organization_1).

- If you are defining a special administrative user (similar to superuser) that should not be affiliated with an organization, do not call `setTenantId`.

To get the user information from the database, you can call the `getUser` method by providing the username.

You can remove users from the database by name with the `deleteUser` method.

Equivalent methods for managing roles are available in the `UserAuthorityService`. You can assign users to roles using the following two methods:

``` java
public void addRole(ExecutionContext context, User aUser, Role role);
public void removeRole(ExecutionContext context, User aUser, Role role);
```

Additional methods for finding users with specific roles are available. You can find details about them if you consult the Javadoc for the `UserAuthorityService` interface.
