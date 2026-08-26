---
title: Export and Import
description: "Export and import allow you to migrate configuration resources between instances of Jaspersoft Studio. You can export the following configuration resources:"
---

# Export and Import

Export and import allow you to migrate configuration resources between instances of Jaspersoft Studio. You can export the following configuration resources:

-   global data adapters

-   JasperReports Server configurations

-   composite elements

-   text, table, and crosstab styles

-   global JasperReports properties

-   Jaspersoft Studio preferences

!!! note

    The Jaspersoft Studio application logger preferences cannot be exported, since they are determined in part by your application `INI` configuration.

You can choose to export all of these categories or only a subset of them. However, you cannot choose individual items inside a category. The result of the export is a single zip file (compressed archive), which can be imported into another Jaspersoft Studio instance. Again, you can choose which of the available categories inside the zip you want to import.

To export configuration resources

1.  Select **File &gt; Export**.

    The **Export** dialog is displayed.

2.  Select **Jaspersoft Studio &gt; Jaspersoft Studio Configuration** for the destination and click **Next**.

    The Export wizard shows the resource categories that can be exported, with the number of resources in each category. If there are no resources in a category, the category does not appear on the list.

    |  |
    |----|
    | ![Export Jaspersoft Studio Configuration Wizard](assets/images/Export%20Jaspersoft%20Studio%20Configuration%20Wizard.png) |
    | *Figure 1: Export Jaspersoft Studio Configuration Wizard* |

3.  Select the categories that you want to export and click **Next**.

4.  Enter the location and name that you want for the exported file and click **Finish**.

A zip file is created in the location that you chose.

To import configuration resources

1.  Select **File &gt; Import**.

    The **Import** dialog is displayed.

2.  Select **Jaspersoft Studio &gt; Jaspersoft Studio Configuration** and click **Next**.

3.  Enter the location and file name of the zip file that you wish to import and click **Next**.

    If the file is a valid configuration file, the wizard shows the resource categories that can be imported, with the number of resources in each category. If the file is not a valid configuration file, you receive an error message.

    |  |
    |----|
    | ![Selecting Categories to Import](assets/images/Selecting%20Categories%20to%20Import.png) |
    | *Figure 2: Selecting Categories to Import* |

4.  Select the resource categories that you want to import and click **Finish**.

5.  If there is a naming conflict between an imported resource and an existing resource in your Jaspersoft Studio configuration, choose the action in you want in the displayed dialog. For resource categories other than Jaspersoft Studio properties and JasperReports Library properties, you have three choices:

-   **Overwrite**: Overwrites the existing resources with the imported resources of the same name.

-   **Keep both**: Automatically renames the conflicting imported resources with a unique name.

-   **Skip**: Keeps the existing resources and discards the imported resources.

For Jaspersoft Studio properties and JasperReports Library properties, which do not support multiple instances, you are prompted to choose to overwrite or not.

As earlier, you must choose the same action for all conflicting resources in a category. For example, if you have multiple conflicting global data adapters, you must overwrite, keep both, or skip all global data adapters. A separate dialog is shown for each category where you have conflicting resources. You can choose different actions for different categories.
