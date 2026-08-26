---
title: SOAP Authentication
description: "The calling application must supply a valid user and password with HTTP Basic Authentication to access the web services. In basic authentication, the user ID and password are concatenated with a..."
---

# SOAP Authentication

The calling application must supply a valid user and password with HTTP Basic Authentication to access the web services. In basic authentication, the user ID and password are concatenated with a colon (:) and Base64 encoded in the HTTP request header. Usually, your client library does this for you. For example, the administrator’s default credentials are `jasperadmin:jasperadmin`, which is encoded as follows:

`Authorization: Basic amFzcGVyYWRtaW46amFzcGVyYWRtaW4=`

The web services accept the same accounts and credentials as the JasperReports Server user interface.

-   If there is only one organization, such as in the JasperReports Server default installation, you should specify the user name only: `WSUser`. For example, `jasperadmin`.
-   In deployments with multiple organizations, the organization ID or alias must be added, in the form `WSUser|TenantId` or `WSUser|TenantAlias`. For example, you could use `jasperadmin|organization_1` (`WSUser|TenantId`) or `jasperadmin|CanadaBranch `(`WSUser|TenantAlias`).
-   See section [Organizations/Tenants](organizations_tenants.md), for explanations of `WSUser`, `TenantId`, and `TenantAlias`.

If login encryption in enabled in your server, you must encrypt the password before base64-encoding it with the username. To encode the password, see section [Login Encryption](login_encryption.md).

To simplify the development of web services in Java, Jaspersoft provides a set of helper classes, including a ready-to-use client that can make it easier to integrate an external application with JasperReports Server, be it web- or desktop-based. These classes include an object model that represents resources and creates requests and operation results, along with a Marshaller and an Unmarshaller class to quickly move between XML and the Java object model. The presentation of each service includes code samples that show how to use these classes.
