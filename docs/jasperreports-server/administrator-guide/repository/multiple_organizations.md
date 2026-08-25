---
title: Multiple Organizations in the Repository
description: "If you implement multiple organizations, there are certain considerations when designing the repository structure for your deployment."
---

# Multiple Organizations in the Repository

If you implement multiple organizations, there are certain considerations when designing the repository structure for your deployment.

## Organization Folders

In the repository, each organization has its own branch, contained in a folder named after the organization. JasperReports Server automatically restricts a user's view and access to their organization's folder. Organization admins can create any folder structure needed within their organization.

Top-level organizations are contained in a folder called Organizations at the root of the folder hierarchy. The top folder of a suborganization is contained in a folder called Organizations in the parent organization. Administrators can view and browse the Organizations folder, and the folders of any suborganizations. As administrators of the parent organization, they can also create folders and resources in suborganizations.

!!! note

    By default, users in an organization can also view and create folders and resources in any suborganization. An administrator can control this by changing the folder permissions.

The Organizations folder in every organization is a special folder that is managed by the server. Administrators can't create folders or resources directly in the Organizations folder. The server creates the folder for each suborganization when the administrator creates a new organization through the **Manage \> Organizations** page. Administrators can create folders and resources in the Folder Template folder in the Organizations folder; these resources are copied into new organizations. For more information, see [Default Folders for Organizations](../management/managing_organizations.md).

## Design Considerations

Careful design of the JasperReports Server repository leads to a clear and robust BI environment and easy, secure access for users. One of the main decisions is how you want your organizations and users to access resources: which resources are shared across organizations as opposed to those specific to an organization. Consider these use cases:

- Organizations have private resources - Data sources, reports, an other resources are stored in each organization's own folders, and perhaps only a few resources such as company logos would be shared among them.
- Organizations share resources - Resources are kept in the public folders where they can be used by all organizations and users. You may have common data sources and reports across customers, but the underlying data is partitioned by organization. Data level security restricts what users see when running public reports.
- Organization share resources, but have some customizations - For example, users in the organization create reports that are private and stored locally, but they access resources in the public folders.
- Organizations are hierarchical - One organization contains others. By default, the parent organization can access all the resources of its child organizations. If you don't want this, you must avoid creating suborganizations or customize the server's multi-organization architecture.

## Referencing Resources in the Repository

All resources in the repository can be referenced by Universal Resource Identifiers (URIs) that specify resource names and folder paths. Because of the hierarchy of organizations, references are relative to the user accessing them. JasperReports Server transforms relative references into actual resource locations in the repository based on the user's organization and the organization's main folder. By default, folder locations are transformed in the following ways:

- For organization members, locations in /public are not transformed, but those in the organization's main folder are transformed to the actual location, for example, /organizations/organization_1.<br>
  So if a user in org_1 runs a report that references /images/myLogo image resource, the actual path in the repository that is fetched is /organizations/org_1/images/myLogo. If the report also references /public/sharedLogo, the server fetches the resource in /public/sharedLogo.

- For a system admin (`superuser`) , locations throughout the repository are not transformed. They see the actual repository path names.

  If a system admin runs the same report in the example above, the reference to /images/myLogo attempts to fetch a resource named /image/myLogo, which works only if there is a folder at the root of the repository named images with a copy of myLogo. The report fails (or is missing a resource) when run by the system admin, unless he logs in as that user through the **Manage \> Users** page.

This transformation enables URIs to reference different resources depending on the organization of the user who accesses them. For example, a report may have an organization-specific logo as an image. We can set up the report as follows:

- Logo URI specified in the JRXML: /images/orgLogo. When transformed for each user, the URI accesses a location relative to his organization's main folder.
- Every organization using this report must have a folder named /images containing an image resource with the ID orgLogo. When a user in any organization runs the report, the server fetches the organization-specific image and displays it.

There are two exceptions to references being transformed. In these cases, the references must be literal:

- In report units, references to data sources, JRXMLs, or input controls.
- In OLAP connections, references to data sources or schemas.

Also, because these references are not transformed, you must observe the following:

- For maintenance tasks on an organization's report units and OLAP connections, you must log into that organization and do the tasks there. You cannot administer the resources as superuser or another organization's admin.
- The two resources (report units and OLAP connections) cannot reference objects across organizations or even in their own parent organization. The reference would not be transformed; it would be taken literally and would fail. For example, if the data source for a report unit is in the /dataSources folder of This_Org, users in That_Org cannot access it because their reference cannot cross organizations.

!!! note

    To test the absolute references, you should log in as an admin of the organization using the references. See [Testing User Permissions](permissions.md).

## Best Practices

Here are some best practices for resources in a repository shared by multiple organizations:

- The system admin (`superuser`) must log in as an organization user to maintain or run an organization's resources.
- Resources with absolute references to resources in organization folders work only for the users within the organization or the parent organization.
- If a JRXML that accesses organization resources with URIs must run across organizations, all organizations must have identical folders, object names, and expected object types for those resources.
- The public folder should be used for resources that are shared across organizations.
