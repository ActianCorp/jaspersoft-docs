---
title: Working with Domain Files
description: "The Domain Designer offers a graphical interface for creating and editing Domains, but you can also export a Domain in XML format and edit it outside of JasperReports Server. Some features, such as..."
---

# Working with Domain Files

The Domain Designer offers a graphical interface for creating and editing Domains, but you can also export a Domain in XML format and edit it outside of JasperReports Server. Some features, such as default schemas and joins between two columns in the same table, can be configured only in the design file. In other cases, it may be easier to work directly with the XML to accomplish certain tasks. Design files can also simplify the sharing of Domains between systems.

!!! warning

    The results of using a Domain based on an inconsistent or incorrect design file are unpredictable and can be difficult to resolve. Make sure you thoroughly understand Domains and Domain syntax before editing any Domain design files.

Domain security and translation of Domain labels and descriptions are also configured via optional text-based files that you upload to the Domain. Security definitions and locale translations take effect in the Ad Hoc Editor when creating the report and in the final output when running the report.

This chapter provides an overview of XML Domain design files and best practices for working with them:

-   [Understanding Domain Design Files](understanding.md)
-   [Requirements for XML Design Files](requirements.md)

Details about XML design files, security files, and locale bundles are given in the following chapters:

-   [XML Design File Reference](../domain_syntax/xml_design_file_reference.md): The syntax of all elements in the XML design file, such as the data source, tables, joins, sets, and items.
-   [Securing Data in a Domain](../domain_security/securing_data_in_a_domain.md): A sample scenario that documents how to create a security file.
-   [Localizing Domains](../localizing/localizing_domains.md): How to create and upload locale bundles to translate labels and descriptions appearing in Domain-based reports.
