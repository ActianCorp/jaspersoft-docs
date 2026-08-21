---
title: Understanding Domain Design Files
description: "When you design a Domain, you specify the tables in the data source, derived tables, joins, calculated fields, and filters, as well as how those elements appear to users. You can design a Domain in..."
---

# Understanding Domain Design Files

When you design a Domain, you specify the tables in the data source, derived tables, joins, calculated fields, and filters, as well as how those elements appear to users. You can design a Domain in JasperReports Server interactively through the Domain Designer, or you can use the file-based format to create or modify Domains. A text file containing a Domain design in XML is called a Domain design file.

The XML in a design file is a hierarchy of elements and attributes that specifies all the settings in the Domain. The elements and attributes are defined by an XML schema provided in an XSD file. In addition, there are constraints on a Domain design that are not expressed in the XML schema. A design file can be modified or written from scratch in an editor and uploaded to the server, as long as it conforms to the XML schema and the design constraints.

For information about exporting and uploading design files, see [Importing and Exporting Domain Design Files](../advanced_domains/importing_and_exporting.md).

!!! note

    XML is not the native format of the Domain design. The XML file is only a representation from which the design can be inferred. A design has additional constraints that are not mapped in the XML format.

## Design File Use Cases

Due to the complexity of a valid design file, it is usually much easier to begin with a basic design file exported from the Domain Designer or to modify an existing design file. Common use cases for working with design files include:

- Enhancing a design: You can use the design file to add features that can't be defined in the Domain Designer. To do this, use the Domain Designer to define as much of the design as possible, then export the design file and modify the exported file directly. Some features can only be defined in the design file. You can still upload these files to the Domain Designer and you can modify the other features of the Domain.
- Defining presentation for large Domains: The Domain Designer makes it easy to select all tables and columns and expose them as sets and items, but editing the labels and descriptions of dozens of items may be faster when they appear in a single design file.
- Making repetitive changes: If the database changes or you want to move a design file to a different system, you may need to edit many elements in the same way. Using search-and-replace in an external editor can speed up this process.
- Programatically creating Domain designs: If you are creating many similar Domains, you may be able to start with a valid design file and generate similar design files that meet the constraints of JasperReports Server.
- Creating files for security and translations: These optional files refer to elements of the Domain design, and it is often more convenient to copy-paste them between external files. For translation files, you can export a template from the Domain Designer as a basis for the translation files. See [Importing and Exporting Domain Design Files](../advanced_domains/importing_and_exporting.md).

After editing, a design file can be uploaded, validated, and used to define the design of a new or existing Domain. With a few exceptions, when you open the design in the Domain Designer again, the modifications are editable in the Designer. For example, a description you added in the XML design file appears on the Data Presentation tab and you can edit it in the Designer. Other elements of the XML file appear on some or all of the Domain Designer tabs.

## Features That Cannot Be Defined in the Domain Designer

The following elements can be edited only in the design file. Design files with these elements can still be opened in the Domain Designer, and other elements can be edited:

- Joins that use `or` or `not` between two join expressions. These appear in the Domain Designer as read-only joins. See [Read-Only Joins](../advanced_domains/advanced_joins.md) for more information.
- Joins between two columns in the same table. These appear in the Domain Designer as read-only joins. See [Read-Only Joins](../advanced_domains/advanced_joins.md) for more information.
- The `defaultSchema` property when using JasperReports Server attributes for a schema name. This does not appear in the Domain Designer directly, but is used when the attribute exists but has null value. See [schemaMap](../domain_syntax/representing_data_sources.md) for more information.
- Individually selected columns of a table. You can only select whole tables on the Data Management tab of the Domain Designer.
