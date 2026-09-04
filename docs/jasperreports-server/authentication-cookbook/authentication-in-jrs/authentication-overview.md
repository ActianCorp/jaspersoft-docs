---
title: Authentication
description: "This cookbook describes how to configure JasperReports Server to use external authentication in place of the built‑in user authentication. The benefits of external authentication include:"
---

# Authentication

This cookbook describes how to configure JasperReports Server to use external authentication in place of the built‑in user authentication. The benefits of external authentication include:

-   Centralized identity management within your enterprise.
-   Single sign-on capabilities if the authentication mechanism supports it.

For deployments that include the Jaspersoft OLAP component within JasperReports Server, external authentication applies transparently to Jaspersoft OLAP users.

This guide covers the following authentication mechanisms:

-   Lightweight Directory Access Protocol (LDAP). See [LDAP Authentication](../ldap/ldap-introduction.md).
-   Central Authentication Service (CAS). See [CAS Authentication](../cas/cas-introduction.md).
-   Authentication via an external database. See [External Database Authentication](../external-db/external-db-introduction.md).
-   Authentication when the user has already been reliably authenticated by another external system. See [Token-based Authentication](../token/tokenauth-introduction.md).

You can also create custom code to run on the server after the user has been authenticated, or use custom authentication providers. See [Advanced Topics](../advanced-topics/advanced-topics.md) for an overview of these topics. Details are beyond the scope of this guide.

!!! note

    The procedures in this guide assume you're familiar with JasperReports Server installation, deployment, and administration. You must have system administrator privileges within JasperReports Server and its application server and read and write access to their files on the host.

If you're setting up external authentication, you may need to understand how JasperReports Server performs internal authentication, or how external roles and organizations in JasperReports Server are created when external authorization has been set up. This chapter gives background information that can help you configure external authentication correctly.

This chapter contains the following sections:

-   [Locating and Working With Sample Files](sample-files.md)
-   [Default Internal Authentication](internal-authentication-steps.md)
-   [Organizations and Users in JasperReports Server](organizations-users-roles.md)
