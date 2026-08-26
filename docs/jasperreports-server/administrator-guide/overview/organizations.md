---
title: Overview of Organizations
description: "The commercial version of JasperReports Server is built on organizations, which are logical entities within the server that have their own users, roles, and branches of the repository. As with any..."
---

# Overview of Organizations

The commercial version of JasperReports Server is built on organizations, which are logical entities within the server that have their own users, roles, and branches of the repository. As with any business structure or hierarchy, organizations may have suborganizations, which may in turn have suborganizations, and so on.

In the default JasperReports Server installation, a single organization mimics the simple structure of older versions of JasperReports Server. If you want to deploy multiple organizations, you must be aware of certain design considerations.

## Single Default Organization

After a default installation, JasperReports Server contains a single organization in which you can deploy your reports. For example, if you install the sample data, you will see a single organization that holds all sample resources, users, and roles.

Single organizations are designed to handle most business cases and are straightforward to administer. However, even with a single organization, the server still includes a root that represents the parent of the organization. For example, a system admin and an organization admin share administrative duties. Also, many features such as themes, attributes, and repository URIs can be defined at both the root and organization levels.

If your business needs more organizations, you will need to manage several levels of administrators and possibly create shared resources in the repository. The following sections provide use cases and explain the functioning of multiple levels of administrators.

## Multiple Organizations

With multiple organizations, several logical entities share a server instance, but remain entirely isolated from each other. There are many use cases for defining multiple organizations in JasperReports Server. For instance:

-   An application provider, such as a software-as-a-service (SaaS) company or a computer department, has a hosted application offered to many customers. It integrates JasperReports Server in its application to offer dashboards, reports, and analysis. A number of common reports and data sources are useful across customers, but there are customer-specific reports, as well. Machines and databases are shared by customers, according to the provider's own architecture, but within the functionality provided by JasperReports Server, each customer is a separate organization. Customers can manage their own users in the hosted application, and the server maps the application's authentication scheme to the correct organization. The organization structure provides the full power of JasperReports Server to each of the provider's customers, while ensuring that their data and reports are secure.
-   A company has many departments but wants them to share a common BI infrastructure. Corporate IT needs to deploy and maintain only a single instance of JasperReports Server, while each department is represented by an organization that manages its own users. For security and simplicity, the departments do not share databases, except in the case of sub-departments, such as Accounts Payable being a sub-department of Finance. Users access JasperReports Server directly, logging in with their department name and username. Organization administrators have defined the data sources and Domains specific to the needs of their department's users.

The organization feature is flexible enough to accommodate any combination of these scenarios and many others like it. In all cases, administrators can configure secure environments for any number of organizations, and end users experience a powerful BI platform tailored to their needs.

All organizations or hierarchies of organizations exist independently within a single instance of JasperReports Server. Neighboring organizations are isolated from one another, while parent organizations have full control of their suborganizations. Users can access only the data and resources in their own organizations or suborganizations, and administrators can define roles and set permissions to further control access.

## Levels of Administrators

Each organization has an administrator who can manage users, roles, and repository permissions in that organization and any of its suborganizations.

There are essentially three levels of administration:

-   The system administrator - Also called system admin. The default login name of the system admin is `superuser`. He exists at the root level, outside all organizations. The system admin manages the JasperReports Server installation, creates top-level organizations, and configures server-wide settings. The system admin can create, modify, and delete users, roles, and repository objects in any organization.
-   The administrator of a top-level organization - Also called organization admin. The organization admin manages all users, roles, and repository objects in an entire organization, including any suborganizations. The default login name of the organization admin is `jasperadmin`.
-   The administrator of a suborganization - Functionally equivalent to an organization admin, but limited to the suborganization's users, roles, and repository objects. This administrator can be overridden by a top-level organization admin.
