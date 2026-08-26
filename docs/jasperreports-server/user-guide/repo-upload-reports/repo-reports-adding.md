---
title: Adding Reports Directly to the Repository
description: "This section describes functionality that can be restricted by the software license for JasperReports Server. If you do not see some of the options described in this section, your license may..."
---

# Adding Reports Directly to the Repository

!!! info "Important"

    This section describes functionality that can be restricted by the software license for JasperReports Server. If you do not see some of the options described in this section, your license may prohibit you from using them. To find out what you are licensed to use, or to upgrade your license, contact Jaspersoft.

Using the Ad Hoc Editor, you can create reports within JasperReports Server from pre-defined Topics and Domains. You can also create reports outside of JasperReports Server and add them to the repository. To add a report to the repository, you need a valid JRXML file. To create and validate this file, you can use Jaspersoft Studio. Jaspersoft recommends Jaspersoft Studio for most users because its graphical user interface simplifies the job. If you have a thorough understanding of the file structure, you can use a text editor to create the file containing JRXML code.

You can add a report to the server’s repository in two ways:

-   From within the server

    Add the JRXML file and any other resources that the report needs as a report unit. A wizard guides you through each step.

-   From Jaspersoft Studio

    Design the report in Jaspersoft Studio, and use a connection to JasperReports Server to add the JRXML and resources to the JasperReports Server repository. See the Jaspersoft Studio User Guide for information.

    To add the sample report units to the server, you need access to the sample data in the server installation directory on the file system (&lt;js-install&gt;/samples). Contact your administrator for help with locating these files.

    !!! note

        In most cases, it is preferable to upload the JRXML file from Jaspersoft Studio. Uploading through JasperReports Server is included for completeness.

    This chapter includes examples of adding a report to the repository using the server’s wizard and the plug-in. The chapter contains the following sections:

-   [Overview of a Report Unit](repo-report-unit.md)

-   [Adding a Report Unit to the Server](repo-add-simple-report-unit.md)

-   [Defining a Query in a Report](repo-defining-query.md)

-   [Adding a Complex Report Unit to the Server](repo-adding-complex-report.md)

-   [Adding Cascading Input Controls to a Report](repo-adding-cascading-input-controls.md)

-   [Editing JRXML Report Units](repo-editing-jrxml.md)

-   [Localizing Reports](repo-localizing-reports.md)
