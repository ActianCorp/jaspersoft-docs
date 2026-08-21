---
title: Understanding Domains
description: Domains model and present data that report creators may not understand in raw form. Production databases typically contain data in tables optimized for storage and retrieval. A Domain is a virtual...
---

# Understanding Domains

Domains model and present data that report creators may not understand in raw form. Production databases typically contain data in tables optimized for storage and retrieval. A Domain is a virtual view, created and stored in JasperReports Server without modifying the data source, that models and presents the data in a way that is more accessible to report creators and readers. Columns with data relevant to users can be joined across several tables, filtered by business need, and augmented with calculated fields.

A Domain is a metadata layer that models and presents data accessed through a data source. You can use Domains to structure the data and present it in business terms appropriate to your audience. You can also limit access to data based on the security permissions of the person running the report and provide translations for static report text. Domains in JasperReports Server are used to create Ad Hoc views and reports.

By extension, a Domain is also the dataset that it selects and makes available in a more usable form. When creating a Domain, you define the view and the metadata that selects and presents the data that you want. When using a Domain, users see the data you have made available and create Ad Hoc reports with it.

## Who uses Domains?

Domains help make data accessible to different types of users:

- Database administrators or business analysts create Domains, choosing and modeling the data to expose, and creating user-friendly labels where appropriate. These users have an understanding of the raw data as it appears in the data source.

!!! note

    In the default server installation, Domain creators must have organization-level admin privileges. See JasperReports Server Administrator Guide for more information.

- Report designers use Domains to create Ad Hoc views in JasperReports Server or reports in Jaspersoft Studio. These users understand the data in the context of their specific business case, but might not understand the raw data in the original data source.
- Report readers see only the data they need and understand.

## What Does a Domain Do?

A Domain has multiple levels that allow you to model and present data:

- Select catalogs (if you are using a Trino-based data source to create a domain), schemas and tables from your data source on the Data Management tab, as well as create derived tables using SQL queries. See [The Data Management Tab](../domain_designer/data-management.md) and [Derived Tables](../advanced_domains/derived_tables.md) for more information.
- Define joins between any included tables and/or derived tables on the Joins tab. See [The Joins Tab](../domain_designer/joins-tab.md) for more information.
- Set conditions on field values to limit the data accessed through the Domain on the Pre-filters tab. For more information, see [The Pre-filters Tab](../domain_designer/prefilters-tab.md). You can also filter data using calculated fields. For more information, see [Calculated Fields](../advanced_domains/calculated_fields.md).

!!! note

    A Domain design often includes data filtering, but report creators can filter data even further or create input controls for report readers to use.

- Choose which tables and columns to expose to users on the Data Presentation tab, and optionally define or change display properties. See [The Data Presentation Tab](../domain_designer/presentation-tab.md) for more information.
- Create or upload a security file that defines access permissions on the Security tab. See [The Security Tab](../domain_designer/security-tab.md) for more information.
- Upload locale bundles for the display names on the Locales tab. See [The Locales Tab](../domain_designer/locales-tab.md) for more information.

Each Domain is stored in the repository as an XML design file along with the files the Domain references, such as a data source, locale bundles for localization, or a security file. You can create Domains in the Domain Designer, or you can upload a Domain design file in XML format. Security files can be created similarly in the Domain Designer or uploaded as an XML file. Localization bundles must be created in text format and uploaded. See [Securing Data in a Domain](../domain_security/securing_data_in_a_domain.md), and [Localizing Domains](../localizing/localizing_domains.md) for more information.

## Planning a Domain

Plan Domain features before you begin the creation process:

- Decide on the data source and define it in the server repository.
- If you need to combine several data sources into a single data source, choose your data virtualization strategy. Either define each data source in the repository and then create a virtual data source that combines them, or use Jaspersoft Advanced Data Services and define a data source based on that. See [Domains and Data Virtualization](../advanced_domains/data_virtualization.md) for more information.
- If you want to use attributes, make sure they are defined and that you understand how they will work. This is especially important if you are using attributes for schema names. See [Using Attributes in the Domain Designer](../advanced_domains/attributes_in_the_domain_designer.md) for more information.
- Know the elements of your design: tables and columns to choose, joins to perform, pre-filters to define, and items you want to present to users.
- Determine whether the users of the Domain need localized resources, such as translated labels and local formats such as dates.
- Determine a security policy for the data retrieved through the Domain. Is there any data that should be restricted to only certain users or roles in your server?
