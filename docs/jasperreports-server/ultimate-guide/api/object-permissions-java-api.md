---
title: Object Permissions API
description: An object permission represents the right to perform a certain action on a repository resource by a user. Access to all functionality relies on a security mechanism that checks if the user has the...
---

# Object Permissions API

An object permission represents the right to perform a certain action on a repository resource by a user. Access to all functionality relies on a security mechanism that checks if the user has the right to perform the current action on the given object or resource. The `com.jaspersoft.jasperserver.api.metadata.user.service.ObjectPermissionService`<br>
interface grants or revokes permissions on an object to users and roles. It has methods for creating and removing permissions on objects and recipients.

An object permission is represented by an implementation instance of the `com.jaspersoft.jasperserver.api.metadata.user.domain.ObjectPermission`<br>
interface and holds information about the recipient (`User` or `Role` instance), the type of permissions granted to the user (combination of numeric constants defined in the Spring Security class `org.springframework.security.acl.basic.SimpleAclEntry`), and the resource to which they apply.

The following shows how to create an object permission on an image resource within the repository:

``` text
Resource resource = ..an existing repository resource..
ObjectPermission permission = objectPermissionService.newObjectPermission(null);
permission.setURI(resource.getURIString());
permission.setPermissionRecipient(user);
permission.setPermissionMask(SimpleAclEntry.READ);
objectPermissionService.putObjectPermission(null, permission);
```

You can revoke object permissions with one of the following public methods exposed by this service:

``` java
public void deleteObjectPermission(ExecutionContext context,
  ObjectPermission objPerm);
public void deleteObjectPermissionForObject(ExecutionContext context,
  Object targetObject);
public void deleteObjectPermissionsForRecipient(ExecutionContext context,
  Object recipient);
```
