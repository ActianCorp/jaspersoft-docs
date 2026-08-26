---
title: JasperReport Structure
description: The repository resource that aggregates all information needed to run a report is called a JasperReport. A JasperReport is based on a JRXML file that conforms to the JasperReports Library that the...
---

# JasperReport Structure

The repository resource that aggregates all information needed to run a report is called a JasperReport. A JasperReport is based on a JRXML file that conforms to the JasperReports Library that the server uses to render reports.

A JasperReport is a complex resource composed of other resources:

-   The main JRXML file that defines the report

-   A data source that supplies data for the report.

-   A query if none is specified in the main JRXML.

    -   The query may specify its own data source, which overrides the data source defined in the report.

-   Input controls for parameters that users may enter before running the report. Input controls are composed of either a datatype definition or a list of values.

-   Any additional file resources, such as images, fonts, and resource bundles referenced by the report template.

-   If the report includes subreports, the JRXML files for the subreports.

The collection of all the resources referenced in a JasperReport is sometimes called a report unit. End users usually see and interact with a JasperReport as a single resource in the repository, but report creators must define all of the component resources.

## Referencing Resources in the Repository

There are several ways to define and reference all the resources in a JasperReport.

In environments without JasperReports Server, reports are stored in the file system, and shared resources are usually stored on a network drive accessible to all developers and users. This solution is sometimes impractical, as you cannot always add such resources to the classpath, and the use of absolute paths has its own limitations. Also, storing the resources in the file system discourages their reuse. Developers may invest time recreating resources because they do not know they exist.

By storing resources in the repository, JasperReports Server makes it easy and reliable to share resources such as images, style templates, and subreports among reports. The repository mimics a folder and file structure, so references to external files can be handled as references to external resources in the repository.

The `repo:`syntax used in some previous versions is no longer required. Regular file paths are recognized and managed within the repository.

When you upload your JRXML to the repository, your file references become valid repository references, and you can store all your resources in well-known locations in the repository. This simplifies the process of uploading your reports, because you don't have to upload the resources each time. Also, you can manage these resources either through Jaspersoft Studio, the JasperReports Server user interface, or the server's REST API. For example, when you update a logo image, all reports that reference that resource displays the new logo.

## Absolute References

Absolute references are the URIs of resources in the JRXML of a report. A path may refer to the file system where the JRXML was created, but when uploaded to the server, it refers to folders in the repository.

The path must start with one of the following:

`/` to represent the root of the current user's organization. For example, `/images/logo` is the path to a resource in the /images folder.

`../` to represent the folder where the JasperReport is uploaded. For example, `../myLogo` is the path to a resource in the same folder as the JasperReport.

As with a file system path, the repository path is composed of the resource ID of every parent folder, ending with the ID of the resource. Jaspersoft Studio supports absolute references by allowing you to drag resources from the repository tree view into the design area.

!!! note

    If you implement organizations, the absolute path is relative to the user's organization, as described in [Multiple Organizations in the Repository](multiple_organizations.md).

When uploading the JRXML with absolute resource references as part of a JasperReport in the server, you need to ensure only that the resource with the given path exists in the repository before running the report. When the report runs, the server locates the resource in the repository and uses it to render the report.

Because file resources such as images, fonts, and JARs are the only resources for which you can create references directly in JRXML, they are the only resources for which you can create absolute references.

One disadvantage of absolute references is that JasperReports Server does not maintain the dependency between the JRXML and the absolute reference. When uploading the JRXML, there is no warning if the resource does not exist, and the server allows you to delete the resource from the repository even if it is still being referenced. If the resource is not available, running the report fails with an error.

## Local Resources and External References

JasperReports Server provides more flexibility and power when you use indirect references instead of absolute references. Indirect references are placeholder names that must be manually linked to the resource when uploading the JasperReport. The syntax for an indirect reference contains only a resource placeholder name, for example:

`logoImage`

When you upload a JRXML with an indirect reference, the server prompts you to provide the resource. You have two options:

-   Create a new resource, in this case by uploading an image that becomes part of the JasperReport. This is called a local resource. You cannot access this resource from elsewhere in the repository, it exists only within the JasperReport.
-   Select a resource from the repository. This is called an external reference because it is external to the JasperReport. Any number of reports can link to the same external resource, and the resource can be managed independently of them.

While indirect references require slightly more work than absolute references in the JRXML, the server manages the dependency. Local resources exist as part of a JasperReport, and external references cannot be deleted until they are no longer referenced.

In cases where you do not want to reference existing resources, local resources allow reports to be highly customized, and self-contained. A local resource defined inside the JasperReport has all the same properties as a repository resource, but it is not accessible in the repository. Users must edit the JasperReport to access any resources it defines locally.

Indirect references are used implicitly in several other cases when you define a JasperReport:

-   The main JRXML itself is either a local resource created by uploading a file or an external reference to an existing JRXML file resource in the repository.
-   Every report must have a data source, and JasperReports Server gives you the option to either create a new local resource or use an external reference to an existing data source.
-   Every report must also have a query that matches its data source. You may choose to create a local query resource or use an external reference to an existing query.
-   Parameters in a report are implicitly handled as an indirect reference to an input control. For every parameter named in your main JRXML, you must define an input control either as a local resource or external reference.

Every level of indirect referencing is independent of the other. For example, when creating a JasperReport, you may choose to create an input control as a local resource, but that input control may have an external reference to its datatype. The server still manages the dependency between the local input control and the datatype resource in the repository.

Local resources and external references are used by several resources, for example when creating input controls, query resources, Domains, and OLAP resources.

## References in Subreports

A subreport is a subordinate JRXML file within a JasperReport. As with all other resources referenced by the main JRXML, the subreport JRXML file may be specified by an absolute reference, a local resource, or an external reference.

As a JRXML file, a subreport can reference other resources of its own. However, the subreport is run as part of the main JRXML, and any references in the subreport are interpreted relative to the JasperReport resource (represented by the main JRXML) and the context in which the JasperReport is being run.

## Data Snapshots

Report resources can also store a snapshot of the report data. A snapshot is a copy of the data that the query returns when the data is refreshed. This data snapshot is an internal structure not visible or accessible from the repository. However, when data snapshots are enabled, a data snapshot is stored in the repository with each report. When users open a report, the report viewer retrieves and displays the data from the snapshot. Users then have the option of refreshing the data in the report viewer, and if they have permissions, saving the data snapshot back into the report resource.

For more information about interacting with data snapshots, see the JasperReports Server User Guide. To enable snapshots, see [Enabling Data Snapshots](../configuration/enabling_data_snapshots.md).
